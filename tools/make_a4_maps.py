#!/usr/bin/env python3
"""make_a4_maps.py - turn tabletop RPG map images into printable A4 PDFs.

Reads a CSV manifest describing map/picture images and produces two
multi-page PDFs at 300 DPI:

    maps/print/PLAYER_MAPS.pdf   - safe to hand to players
    maps/print/DM_MAPS.pdf       - full DM information

See maps/README.md for the manifest format and a worked example.

Usage:
    python3 tools/make_a4_maps.py --manifest maps/manifest.csv
    python3 tools/make_a4_maps.py --manifest maps/manifest.csv --check
    python3 tools/make_a4_maps.py --self-test

Requires only Pillow (tested with Pillow 12) and the standard library.
"""
from __future__ import annotations

import argparse
import csv
import re
import shutil
import statistics
import sys
import tempfile
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional

from PIL import Image, ImageDraw, ImageFont

# ---------------------------------------------------------------------------
# Constants / page geometry
# ---------------------------------------------------------------------------

DPI = 300.0
MM_PER_INCH = 25.4
A4_SHORT_MM = 210.0
A4_LONG_MM = 297.0

DEFAULT_MARGIN_MM = 8.0
CAPTION_HEIGHT_MM = 14.0
CAPTION_PAD_MM = 2.2

MIN_EFFECTIVE_DPI = 150.0
MAX_UPSCALE = 2.0

# "keep" (carried-over sheet elements such as title/compass/signature/logo)
MIN_KEEP_HEIGHT_MM = 9.0     # never render a kept element smaller than this
MAX_KEEP_UPSCALE = 6.0       # ...but don't blow tiny logos up absurdly either
KEEP_PAD_MM = 3.0
KEEP_HEADER_ASPECT = 1.8     # wide items (title banners, scale notes) -> header
                              # squarer items (signature, compass, logo) -> footer

DIVIDER_TITLE = "To show the players"
DIVIDER_SUBTITLE = "Pictures for the table - not maps"

REQUIRED_COLUMNS = [
    "order", "set", "location", "level", "title",
    "dm_file", "player_file", "redact", "crop", "keep", "notes",
]


def mm_to_px(mm: float, dpi: float = DPI) -> float:
    return mm * dpi / MM_PER_INCH


# ---------------------------------------------------------------------------
# Manifest parsing
# ---------------------------------------------------------------------------

@dataclass
class ManifestRow:
    idx: int                 # original row order in the CSV (0-based)
    order: float
    set_: str                # 'map' or 'picture'
    location: str
    level: str
    title: str
    dm_file: str
    player_file: str
    redact: list
    crop: Optional[tuple]
    keep: list
    notes: str


def parse_rect(s: str) -> tuple:
    parts = [p.strip() for p in s.split(",")]
    if len(parts) != 4:
        raise ValueError(f"expected 'x,y,w,h', got {s!r}")
    try:
        x, y, w, h = (float(p) for p in parts)
    except ValueError:
        raise ValueError(f"non-numeric values in rect {s!r}")
    return (int(round(x)), int(round(y)), int(round(w)), int(round(h)))


def parse_rect_list(s: str) -> list:
    s = (s or "").strip()
    if not s:
        return []
    out = []
    for chunk in s.split(";"):
        chunk = chunk.strip()
        if not chunk:
            continue
        out.append(parse_rect(chunk))
    return out


def parse_manifest(manifest_path: Path):
    """Returns (rows, warnings). Raises SystemExit on a structurally broken file."""
    warnings = []
    rows = []
    with open(manifest_path, newline="", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames or []
        missing_cols = [c for c in REQUIRED_COLUMNS if c not in fieldnames]
        if missing_cols:
            raise SystemExit(
                f"manifest {manifest_path}: missing column(s): {', '.join(missing_cols)}\n"
                f"expected header: {', '.join(REQUIRED_COLUMNS)}"
            )
        for i, raw in enumerate(reader):
            def g(k):
                return (raw.get(k) or "").strip()

            if not any(g(c) for c in fieldnames):
                continue  # fully blank line

            set_ = g("set").lower()
            title = g("title") or "(untitled)"
            loc = g("location")
            level = g("level")

            if set_ not in ("map", "picture"):
                warnings.append(
                    f"row {i + 2}: unknown set '{g('set')}' (expected 'map' or 'picture') - row skipped"
                )
                continue

            order_raw = g("order")
            try:
                order = float(order_raw) if order_raw else float(i)
            except ValueError:
                warnings.append(
                    f"row {i + 2} ('{title}'): invalid order '{order_raw}' - treated as {i}"
                )
                order = float(i)

            dm_file = g("dm_file")
            player_file = g("player_file")

            if set_ == "map" and not dm_file and not player_file:
                warnings.append(
                    f"row {i + 2} ('{title}'): map row has neither dm_file nor player_file - row skipped"
                )
                continue
            if set_ == "picture" and not player_file:
                warnings.append(
                    f"row {i + 2} ('{title}'): picture row has no player_file - row skipped"
                )
                continue

            try:
                redact = parse_rect_list(g("redact"))
            except ValueError as e:
                warnings.append(f"row {i + 2} ('{title}'): bad redact value ({e}) - ignoring redact")
                redact = []

            crop = None
            crop_raw = g("crop")
            if crop_raw:
                try:
                    crop = parse_rect(crop_raw)
                except ValueError as e:
                    warnings.append(f"row {i + 2} ('{title}'): bad crop value ({e}) - ignoring crop")
                    crop = None

            try:
                keep = parse_rect_list(g("keep"))
            except ValueError as e:
                warnings.append(f"row {i + 2} ('{title}'): bad keep value ({e}) - ignoring keep")
                keep = []

            rows.append(ManifestRow(
                idx=i, order=order, set_=set_, location=loc, level=level, title=title,
                dm_file=dm_file, player_file=player_file, redact=redact,
                crop=crop, keep=keep, notes=g("notes"),
            ))
    return rows, warnings


def caption_for(row: ManifestRow) -> str:
    loc = row.location.strip()
    lvl = row.level.strip()
    title = row.title.strip()
    if loc and lvl:
        return f"{loc} — {lvl} {title}".strip()
    if loc:
        return f"{loc} — {title}".strip()
    return title


# ---------------------------------------------------------------------------
# Image helpers
# ---------------------------------------------------------------------------

def open_flat(path: Path) -> Image.Image:
    """Open an image and flatten any transparency onto a WHITE background.

    Handles RGBA/LA images and palette images with a transparency entry, so
    a jagged transparent edge (e.g. a Patreon watermark cutout) prints as
    white paper, never black.
    """
    img = Image.open(path)
    img.load()
    if img.mode in ("RGBA", "LA") or (img.mode == "P" and "transparency" in img.info):
        img = img.convert("RGBA")
        bg = Image.new("RGB", img.size, (255, 255, 255))
        bg.paste(img, mask=img.split()[-1])
        return bg
    if img.mode != "RGB":
        img = img.convert("RGB")
    return img


def peek_size(path: Path):
    with Image.open(path) as img:
        return img.size


def clip_box(x0, y0, x1, y1, W, H):
    return (max(0, min(x0, W)), max(0, min(y0, H)), max(0, min(x1, W)), max(0, min(y1, H)))


# ---------------------------------------------------------------------------
# Redaction (player pages derived from a DM sheet)
# ---------------------------------------------------------------------------

def median_ring_color(img: Image.Image, rect, ring: int = 8):
    x, y, w, h = rect
    W, H = img.size
    x0, y0, x1, y1 = clip_box(x, y, x + w, y + h, W, H)
    ox0, oy0, ox1, oy1 = clip_box(x - ring, y - ring, x + w + ring, y + h + ring, W, H)
    if ox1 <= ox0 or oy1 <= oy0:
        return (128, 128, 128)
    crop = img.crop((ox0, oy0, ox1, oy1))
    px = crop.load()
    cw, ch = crop.size
    ix0, iy0, ix1, iy1 = x0 - ox0, y0 - oy0, x1 - ox0, y1 - oy0
    rs, gs, bs = [], [], []
    for yy in range(ch):
        row_inside = iy0 <= yy < iy1
        for xx in range(cw):
            if row_inside and ix0 <= xx < ix1:
                continue
            r, g, b = px[xx, yy]
            rs.append(r); gs.append(g); bs.append(b)
    if not rs:
        return (128, 128, 128)
    return (int(statistics.median(rs)), int(statistics.median(gs)), int(statistics.median(bs)))


def apply_redactions(img: Image.Image, rects: list) -> Image.Image:
    if not rects:
        return img
    out = img.copy()
    draw = ImageDraw.Draw(out)
    for rect in rects:
        color = median_ring_color(img, rect)
        x, y, w, h = rect
        x0, y0, x1, y1 = clip_box(x, y, x + w, y + h, img.width, img.height)
        if x1 > x0 and y1 > y0:
            draw.rectangle([x0, y0, x1 - 1, y1 - 1], fill=color)
    return out


# ---------------------------------------------------------------------------
# Page layout
# ---------------------------------------------------------------------------

def page_px(orientation: str):
    if orientation == "portrait":
        w_mm, h_mm = A4_SHORT_MM, A4_LONG_MM
    else:
        w_mm, h_mm = A4_LONG_MM, A4_SHORT_MM
    return mm_to_px(w_mm), mm_to_px(h_mm)


def pack_band(sized_items, content_w: float, pad: float):
    """sized_items: [(w,h), ...] already scaled to their final print size.

    Shelf-packs them left to right, wrapping to a new row when a row would
    exceed content_w. Returns (rows, band_h) where rows is a list of
    (items[(w,h)...], row_h).
    """
    if not sized_items:
        return [], 0.0
    rows = []
    cur, cur_w, row_h = [], 0.0, 0.0
    for w, h in sized_items:
        add_w = w if not cur else pad + w
        if cur and cur_w + add_w > content_w:
            rows.append((cur, row_h))
            cur, cur_w, row_h = [], 0.0, 0.0
            add_w = w
        cur.append((w, h))
        cur_w += add_w
        row_h = max(row_h, h)
    if cur:
        rows.append((cur, row_h))
    band_h = sum(rh for _, rh in rows) + pad * (len(rows) + 1)
    return rows, band_h


def place_band(rows, content_x0: float, top_y: float, content_w: float, pad: float):
    """Returns a list of (x, y, w, h) placements, one per item, row by row,
    each row horizontally centered."""
    placements = []
    y = top_y + pad
    for items, row_h in rows:
        total_w = sum(w for w, h in items) + pad * (len(items) - 1)
        x = content_x0 + (content_w - total_w) / 2.0
        for w, h in items:
            iy = y + (row_h - h) / 2.0
            placements.append((x, iy, w, h))
            x += w + pad
        y += row_h + pad
    return placements


def classify_and_scale(keep_rects: list, base_scale: float):
    """Splits kept-element rectangles into a header group (wide items, e.g.
    title banners / scale notes) and a footer group (squarer items, e.g.
    signature / compass / logo / watermark), and computes each one's print
    size: at least MIN_KEEP_HEIGHT_MM tall, using the map's own scale when
    that is already bigger, capped at MAX_KEEP_UPSCALE."""
    header_src, header_sizes = [], []
    footer_src, footer_sizes = [], []
    floor_px = mm_to_px(MIN_KEEP_HEIGHT_MM)
    for rect in keep_rects:
        x, y, w, h = rect
        if w <= 0 or h <= 0:
            continue
        s = max(base_scale, floor_px / h)
        s = min(s, MAX_KEEP_UPSCALE)
        pw, ph = w * s, h * s
        if w / h >= KEEP_HEADER_ASPECT:
            header_src.append(rect); header_sizes.append((pw, ph))
        else:
            footer_src.append(rect); footer_sizes.append((pw, ph))
    return (header_src, header_sizes), (footer_src, footer_sizes)


def solve_layout(orientation: str, panel_w: float, panel_h: float, keep_rects: list,
                  margin_mm: float, captions: bool):
    pw, ph = page_px(orientation)
    margin = mm_to_px(margin_mm)
    cap_h = mm_to_px(CAPTION_HEIGHT_MM) if captions else 0.0
    content_x0 = margin
    content_w = pw - 2 * margin
    content_h = ph - 2 * margin - cap_h
    if content_w <= 1 or content_h <= 1 or panel_w <= 0 or panel_h <= 0:
        return None

    base_scale = min(content_w / panel_w, content_h / panel_h)
    (h_src, h_sizes), (f_src, f_sizes) = classify_and_scale(keep_rects, base_scale)
    pad = mm_to_px(KEEP_PAD_MM)
    h_rows, h_band_h = pack_band(h_sizes, content_w, pad)
    f_rows, f_band_h = pack_band(f_sizes, content_w, pad)

    panel_area_h = content_h - h_band_h - f_band_h
    if panel_area_h <= 1:
        return None

    panel_scale = min(content_w / panel_w, panel_area_h / panel_h)
    placed_w, placed_h = panel_w * panel_scale, panel_h * panel_scale
    panel_area_top = margin + h_band_h
    panel_x = content_x0 + (content_w - placed_w) / 2.0
    panel_y = panel_area_top + (panel_area_h - placed_h) / 2.0
    footer_band_top = panel_area_top + panel_area_h

    header_dest = list(zip(h_src, place_band(h_rows, content_x0, margin, content_w, pad)))
    footer_dest = list(zip(f_src, place_band(f_rows, content_x0, footer_band_top, content_w, pad)))
    caption_box = (margin, ph - margin - cap_h, pw - margin, ph - margin) if captions else None

    return dict(
        orientation=orientation, page_w=pw, page_h=ph, panel_scale=panel_scale,
        panel_box=(panel_x, panel_y, placed_w, placed_h),
        header=header_dest, footer=footer_dest, caption_box=caption_box,
    )


def choose_layout(panel_w: float, panel_h: float, keep_rects: list, margin_mm: float, captions: bool):
    a = solve_layout("portrait", panel_w, panel_h, keep_rects, margin_mm, captions)
    b = solve_layout("landscape", panel_w, panel_h, keep_rects, margin_mm, captions)
    cands = [c for c in (a, b) if c]
    if not cands:
        return None
    return max(cands, key=lambda c: c["panel_scale"])


def dpi_warnings(panel_scale: float, label: str):
    eff_dpi = DPI / panel_scale if panel_scale > 0 else float("inf")
    warn = []
    if eff_dpi < MIN_EFFECTIVE_DPI:
        warn.append(f"{label}: effective resolution ~{eff_dpi:.0f} DPI (below {MIN_EFFECTIVE_DPI:.0f} DPI) - may print blurry")
    if panel_scale > MAX_UPSCALE:
        warn.append(f"{label}: image upscaled {panel_scale:.2f}x on the page (more than {MAX_UPSCALE:.0f}x) - may print blurry")
    return eff_dpi, warn


# ---------------------------------------------------------------------------
# Fonts
# ---------------------------------------------------------------------------

_FONT_CACHE = {}


def find_font(size: int, bold: bool = False):
    size = max(8, int(size))
    key = (size, bold)
    if key in _FONT_CACHE:
        return _FONT_CACHE[key]
    names = ["DejaVuSans-Bold.ttf", "Arial Bold.ttf", "LiberationSans-Bold.ttf"] if bold else \
            ["DejaVuSans.ttf", "Arial.ttf", "LiberationSans-Regular.ttf"]
    font = None
    for name in names:
        try:
            font = ImageFont.truetype(name, size)
            break
        except Exception:
            continue
    if font is None:
        try:
            font = ImageFont.load_default(size=size)
        except TypeError:
            font = ImageFont.load_default()
    _FONT_CACHE[key] = font
    return font


def text_width(draw: ImageDraw.ImageDraw, text: str, font) -> float:
    bbox = draw.textbbox((0, 0), text, font=font)
    return bbox[2] - bbox[0]


def draw_caption(draw: ImageDraw.ImageDraw, box, left_text: str, right_text: str):
    x0, y0, x1, y1 = box
    draw.line([(x0, y0), (x1, y0)], fill=(205, 205, 205), width=max(1, round(mm_to_px(0.25))))
    pad = mm_to_px(CAPTION_PAD_MM)

    psize = max(12, round(mm_to_px(3.0)))
    pfont = find_font(psize)
    right_w = text_width(draw, right_text, pfont)

    size = max(12, round(mm_to_px(4.2)))
    available = (x1 - x0) - right_w - 3 * pad
    font = find_font(size)
    while size > 14 and text_width(draw, left_text, font) > max(available, 1):
        size -= 2
        font = find_font(size)

    draw.text((x0 + pad, y0 + pad), left_text, font=font, fill=(25, 25, 25))
    draw.text((x1 - pad - right_w, y0 + pad), right_text, font=pfont, fill=(100, 100, 100))


# ---------------------------------------------------------------------------
# Manifest rows -> concrete pages to render
# ---------------------------------------------------------------------------

@dataclass
class PageSpec:
    row: ManifestRow
    which: str            # 'player' or 'dm'
    kind: str             # 'map' or 'picture'
    src_path: Path
    is_redacted: bool
    caption_main: str


@dataclass
class Plan:
    player_specs: list = field(default_factory=list)
    dm_specs: list = field(default_factory=list)
    warnings: list = field(default_factory=list)
    run_log: list = field(default_factory=list)


def resolve_source(row: ManifestRow, which: str, source_dir: Path):
    """Returns (path_or_None, is_redacted, reason_if_none)."""
    if which == "player":
        if row.player_file:
            return source_dir / row.player_file, False, None
        if row.dm_file and row.redact:
            return source_dir / row.dm_file, True, None
        return None, False, "no player_file and no redact rectangles"
    else:
        if row.dm_file:
            return source_dir / row.dm_file, False, None
        if row.player_file:
            return source_dir / row.player_file, False, None
        return None, False, "no dm_file or player_file"


def build_plan(rows: list, source_dir: Path) -> Plan:
    warnings, run_log = [], []
    maps = sorted([r for r in rows if r.set_ == "map"], key=lambda r: (r.order, r.idx))
    pics = sorted([r for r in rows if r.set_ == "picture"], key=lambda r: (r.order, r.idx))

    player_maps, dm_maps = [], []
    for row in maps:
        dm_path = source_dir / row.dm_file if row.dm_file else None
        pl_path = source_dir / row.player_file if row.player_file else None
        for p, label in ((dm_path, "dm_file"), (pl_path, "player_file")):
            if p is not None and not p.exists():
                warnings.append(f"'{row.title}' ({row.location} {row.level}): {label} not found: {p}")
        if dm_path and pl_path and dm_path.exists() and pl_path.exists():
            try:
                s1, s2 = peek_size(dm_path), peek_size(pl_path)
                if s1 != s2 and (row.crop or row.keep):
                    warnings.append(
                        f"'{row.title}' ({row.location} {row.level}): dm_file {s1} and player_file {s2} "
                        f"are different sizes - crop/keep pixel coordinates will not line up between them"
                    )
            except Exception:
                pass

        dpath, dred, dreason = resolve_source(row, "dm", source_dir)
        if dpath is None:
            warnings.append(f"'{row.title}': {dreason} - no DM page generated")
        elif not dpath.exists():
            pass  # already warned above
        else:
            dm_maps.append(PageSpec(row, "dm", "map", dpath, dred, caption_for(row)))

        ppath, pred, preason = resolve_source(row, "player", source_dir)
        if ppath is None:
            warnings.append(
                f"NO PLAYER SOURCE: '{row.title}' ({row.location} {row.level}) has no player_file and "
                f"no redact rectangles - excluded from PLAYER_MAPS.pdf"
            )
        elif not ppath.exists():
            pass  # already warned above
        else:
            player_maps.append(PageSpec(row, "player", "map", ppath, pred, caption_for(row)))
            if pred:
                run_log.append(
                    f"needs visual check: '{row.title}' ({row.location} {row.level}) - "
                    f"player page generated by redacting the DM file"
                )

    player_pics, dm_pics = [], []
    for row in pics:
        pl_path = source_dir / row.player_file if row.player_file else None
        if pl_path is None or not pl_path.exists():
            warnings.append(f"picture '{row.title}': player_file missing: {pl_path} - skipped")
            continue
        player_pics.append(PageSpec(row, "player", "picture", pl_path, False, caption_for(row)))
        if row.dm_file:
            dpath = source_dir / row.dm_file
            if dpath.exists():
                dm_pics.append(PageSpec(row, "dm", "picture", dpath, False, caption_for(row)))
            else:
                warnings.append(f"picture '{row.title}': dm_file missing: {dpath} - not added to DM set")

    return Plan(
        player_specs=player_maps + player_pics,
        dm_specs=dm_maps + dm_pics,
        warnings=warnings,
        run_log=run_log,
    )


# ---------------------------------------------------------------------------
# Rendering
# ---------------------------------------------------------------------------

def _resolved_keep_rects(row: ManifestRow, W: int, H: int, warnings: list):
    out = []
    for rect in row.keep:
        kx, ky, kw, kh = rect
        cx0, cy0, cx1, cy1 = clip_box(kx, ky, kx + kw, ky + kh, W, H)
        if cx1 <= cx0 or cy1 <= cy0:
            warnings.append(f"'{row.title}': keep rectangle {rect} is outside the {W}x{H} image - skipped")
            continue
        out.append((cx0, cy0, cx1 - cx0, cy1 - cy0))
    return out


def _panel_box_for(row: ManifestRow, W: int, H: int, warnings: list):
    if row.crop:
        x, y, w, h = row.crop
        x0, y0, x1, y1 = clip_box(x, y, x + w, y + h, W, H)
        if x1 - x0 != w or y1 - y0 != h:
            warnings.append(f"'{row.title}': crop {row.crop} extends outside the {W}x{H} image - clipped to fit")
        return x0, y0, max(1, x1), max(1, y1)
    return 0, 0, W, H


def compute_layout_for_spec(spec: PageSpec, margin_mm: float, captions: bool):
    """Cheap (header-only) computation used by both --check and the real
    build. Returns (info_dict_or_None, warnings)."""
    warnings = []
    try:
        W, H = peek_size(spec.src_path)
    except Exception as e:
        warnings.append(f"'{spec.row.title}': could not read {spec.src_path} ({e})")
        return None, warnings

    x0, y0, x1, y1 = _panel_box_for(spec.row, W, H, warnings)
    panel_w, panel_h = max(1, x1 - x0), max(1, y1 - y0)
    keep_rects = _resolved_keep_rects(spec.row, W, H, warnings)

    layout = choose_layout(panel_w, panel_h, keep_rects, margin_mm, captions)
    if layout is None:
        warnings.append(
            f"'{spec.row.title}': margin + kept elements leave no room for the map panel on an A4 page - "
            f"reduce --margin-mm or the number/size of 'keep' rectangles"
        )
        return None, warnings

    label = f"'{spec.row.title}' ({spec.which})"
    eff_dpi, dw = dpi_warnings(layout["panel_scale"], label)
    warnings.extend(dw)

    return {
        "layout": layout,
        "panel_size": (panel_w, panel_h),
        "panel_crop": (x0, y0, x1, y1),
        "keep_rects": keep_rects,
        "source_size": (W, H),
        "effective_dpi": eff_dpi,
    }, warnings


def render_page(spec: PageSpec, info: dict, captions: bool, page_no: int, total_pages: int) -> Image.Image:
    img = open_flat(spec.src_path)
    if spec.is_redacted and spec.row.redact:
        img = apply_redactions(img, spec.row.redact)

    layout = info["layout"]
    pw, ph = layout["page_w"], layout["page_h"]
    canvas = Image.new("RGB", (round(pw), round(ph)), "white")

    x0, y0, x1, y1 = info["panel_crop"]
    panel_src = img.crop((x0, y0, x1, y1))
    px, py, pw2, ph2 = layout["panel_box"]
    panel_resized = panel_src.resize((max(1, round(pw2)), max(1, round(ph2))), Image.LANCZOS)
    canvas.paste(panel_resized, (round(px), round(py)))

    for band in ("header", "footer"):
        for rect, (dx, dy, dw, dh) in layout[band]:
            kx, ky, kw, kh = rect
            crop_img = img.crop((kx, ky, kx + kw, ky + kh))
            resized = crop_img.resize((max(1, round(dw)), max(1, round(dh))), Image.LANCZOS)
            canvas.paste(resized, (round(dx), round(dy)))

    if captions and layout["caption_box"]:
        draw = ImageDraw.Draw(canvas)
        draw_caption(draw, layout["caption_box"], spec.caption_main, f"Page {page_no} of {total_pages}")

    return canvas


def render_divider() -> Image.Image:
    pw, ph = page_px("portrait")
    canvas = Image.new("RGB", (round(pw), round(ph)), "white")
    draw = ImageDraw.Draw(canvas)

    font = find_font(round(mm_to_px(11)), bold=True)
    tw = text_width(draw, DIVIDER_TITLE, font)
    draw.text(((pw - tw) / 2, ph / 2 - mm_to_px(10)), DIVIDER_TITLE, font=font, fill=(20, 20, 20))

    sub_font = find_font(round(mm_to_px(5)))
    sw = text_width(draw, DIVIDER_SUBTITLE, sub_font)
    draw.text(((pw - sw) / 2, ph / 2 + mm_to_px(4)), DIVIDER_SUBTITLE, font=sub_font, fill=(110, 110, 110))
    return canvas


def save_pdf(canvases: list, out_path: Path):
    if not canvases:
        return False
    out_path.parent.mkdir(parents=True, exist_ok=True)
    first, rest = canvases[0], canvases[1:]
    first.save(out_path, "PDF", resolution=DPI, save_all=True, append_images=rest)
    return True


def build_pdfs(plan: Plan, out_dir: Path, margin_mm: float, captions: bool):
    run_warnings = list(plan.warnings)
    run_log = list(plan.run_log)
    results = {}

    for name, specs in (("PLAYER_MAPS", plan.player_specs), ("DM_MAPS", plan.dm_specs)):
        maps_part = [s for s in specs if s.kind == "map"]
        pics_part = [s for s in specs if s.kind == "picture"]
        total = len(maps_part) + (len(pics_part) + 1 if pics_part else 0)

        canvases = []
        page_no = 0
        for s in maps_part:
            page_no += 1
            info, warns = compute_layout_for_spec(s, margin_mm, captions)
            run_warnings.extend(warns)
            if info is None:
                continue
            canvases.append(render_page(s, info, captions, page_no, total))

        if pics_part:
            page_no += 1
            canvases.append(render_divider())
            for s in pics_part:
                page_no += 1
                info, warns = compute_layout_for_spec(s, margin_mm, captions)
                run_warnings.extend(warns)
                if info is None:
                    continue
                canvases.append(render_page(s, info, captions, page_no, total))

        out_path = out_dir / f"{name}.pdf"
        wrote = save_pdf(canvases, out_path)
        if not wrote:
            run_warnings.append(f"{name}.pdf: nothing to write (no usable pages) - file not created")
        results[name] = {"path": out_path, "pages": len(canvases)}

    return results, run_warnings, run_log


# ---------------------------------------------------------------------------
# --check reporting
# ---------------------------------------------------------------------------

def print_check_report(plan: Plan, margin_mm: float, captions: bool):
    print("=== make_a4_maps.py --check ===\n")
    all_warnings = list(plan.warnings)

    for name, specs in (("PLAYER_MAPS", plan.player_specs), ("DM_MAPS", plan.dm_specs)):
        print(f"--- {name} ({len(specs)} page(s), plus a divider before any pictures) ---")
        for s in specs:
            info, warns = compute_layout_for_spec(s, margin_mm, captions)
            all_warnings.extend(warns)
            tag = " [REDACTED]" if s.is_redacted else ""
            if info is None:
                print(f"  ! {s.caption_main}{tag}: FAILED to compute layout - see warnings below")
                continue
            W, H = info["source_size"]
            pw, ph = info["panel_size"]
            layout = info["layout"]
            print(
                f"  - {s.caption_main}{tag}\n"
                f"      source: {s.src_path.name}  size: {W}x{H}"
                + (f"  crop: {pw}x{ph}" if s.row.crop else "")
                + f"\n      orientation: {layout['orientation']}  scale: {layout['panel_scale']:.3f}"
                f"  effective DPI: {info['effective_dpi']:.0f}"
                + (f"  kept elements: {len(s.row.keep)}" if s.row.keep else "")
            )
        print()

    if all_warnings:
        print(f"WARNINGS ({len(all_warnings)}):")
        for w in all_warnings:
            print(f"  ! {w}")
    else:
        print("No warnings.")


def print_run_summary(results: dict, warnings: list, run_log: list):
    print("=== make_a4_maps.py ===\n")
    for name, info in results.items():
        print(f"{name}.pdf: {info['pages']} page(s) -> {info['path']}")
    print()
    if run_log:
        print(f"RUN LOG ({len(run_log)}):")
        for entry in run_log:
            print(f"  * {entry}")
        print()
    if warnings:
        print(f"WARNINGS ({len(warnings)}):")
        for w in warnings:
            print(f"  ! {w}")
    else:
        print("No warnings.")


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main(argv=None):
    ap = argparse.ArgumentParser(
        description="Turn tabletop RPG map images into printable A4 PLAYER/DM PDFs."
    )
    ap.add_argument("--manifest", default="maps/manifest.csv", help="path to the manifest CSV")
    ap.add_argument("--source", default="maps/source",
                     help="folder the manifest's file paths are relative to (default: maps/source)")
    ap.add_argument("--out", default="maps/print", help="output folder for the two PDFs")
    ap.add_argument("--margin-mm", type=float, default=DEFAULT_MARGIN_MM, help="page margin in mm")
    ap.add_argument("--no-captions", action="store_true", help="turn off the caption strip")
    ap.add_argument("--check", action="store_true",
                     help="validate the manifest and report per-image sizing/DPI without writing PDFs")
    ap.add_argument("--self-test", action="store_true",
                     help="generate synthetic images, run the pipeline, assert invariants, print result")
    args = ap.parse_args(argv)

    if args.self_test:
        ok = run_self_test()
        sys.exit(0 if ok else 1)

    manifest_path = Path(args.manifest)
    source_dir = Path(args.source)
    captions = not args.no_captions

    if not manifest_path.exists():
        print(f"ERROR: manifest not found: {manifest_path}", file=sys.stderr)
        sys.exit(2)
    if not source_dir.exists():
        print(f"WARNING: source folder not found: {source_dir} (--source to change it)", file=sys.stderr)

    rows, parse_warnings = parse_manifest(manifest_path)
    plan = build_plan(rows, source_dir)
    plan.warnings = parse_warnings + plan.warnings

    if args.check:
        print_check_report(plan, args.margin_mm, captions)
        return

    out_dir = Path(args.out)
    results, warnings, run_log = build_pdfs(plan, out_dir, args.margin_mm, captions)
    print_run_summary(results, warnings, run_log)


# ---------------------------------------------------------------------------
# Self-test
# ---------------------------------------------------------------------------

def _synth(size, draw_fn, mode="RGB", bg=(235, 230, 214)):
    img = Image.new(mode, size, bg if mode == "RGB" else bg + (255,))
    draw_fn(ImageDraw.Draw(img), size)
    return img


def _label(draw, xy, text, size=40, fill=(20, 20, 20), bold=True):
    draw.text(xy, text, font=find_font(size, bold=bold), fill=fill)


def run_self_test() -> bool:
    tmp = Path(tempfile.mkdtemp(prefix="a4maps_selftest_"))
    ok = True
    try:
        source = tmp / "source"
        source.mkdir()
        out = tmp / "print"

        # 1. Wide map (jpg), dm+player.
        def wide_dm(draw, size):
            w, h = size
            draw.rectangle([40, 40, w - 40, h - 40], outline=(60, 60, 60), width=6)
            _label(draw, (60, 60), "WIDE MAP - DM", size=70)
            _label(draw, (200, 300), "A", size=90, fill=(150, 20, 20))
            _label(draw, (900, 500), "B", size=90, fill=(150, 20, 20))
        def wide_pl(draw, size):
            w, h = size
            draw.rectangle([40, 40, w - 40, h - 40], outline=(60, 60, 60), width=6)
            _label(draw, (60, 60), "WIDE MAP - PLAYER", size=70)
        _synth((3000, 1200), wide_dm).convert("RGB").save(source / "wide_dm.jpg", quality=90)
        _synth((3000, 1200), wide_pl).convert("RGB").save(source / "wide_player.jpg", quality=90)

        # 2. Tall map (png), dm+player.
        def tall_dm(draw, size):
            w, h = size
            draw.rectangle([40, 40, w - 40, h - 40], outline=(60, 60, 60), width=6)
            _label(draw, (60, 60), "TALL", size=70)
            _label(draw, (200, 1400), "C", size=90, fill=(150, 20, 20))
        def tall_pl(draw, size):
            w, h = size
            draw.rectangle([40, 40, w - 40, h - 40], outline=(60, 60, 60), width=6)
            _label(draw, (60, 60), "TALL", size=70)
        _synth((1200, 3000), tall_dm).save(source / "tall_dm.png")
        _synth((1200, 3000), tall_pl).save(source / "tall_player.png")

        # 3. Small low-res map (png), dm+player -> should trigger DPI/upscale warnings.
        def small_map(draw, size):
            draw.rectangle([5, 5, size[0] - 5, size[1] - 5], outline=(60, 60, 60), width=2)
            _label(draw, (10, 10), "SMALL", size=24)
        _synth((400, 300), small_map).save(source / "small_dm.png")
        _synth((400, 300), small_map).save(source / "small_player.png")

        # 4. Map with redactions, dm only (no player_file).
        def redact_dm(draw, size):
            w, h = size
            draw.rectangle([20, 20, w - 20, h - 20], outline=(60, 60, 60), width=6)
            _label(draw, (60, 60), "SECRET ROOM MAP", size=60)
            draw.rectangle([100, 200, 260, 320], fill=(180, 60, 60))
            _label(draw, (110, 230), "A", size=70, fill=(255, 255, 255))
            draw.rectangle([900, 700, 1060, 820], fill=(60, 90, 180))
            _label(draw, (910, 730), "T", size=70, fill=(255, 255, 255))
        _synth((1600, 1200), redact_dm).save(source / "redact_dm.png")

        # 5. Map with no player version and no redaction -> must be excluded from player PDF.
        def noplayer_dm(draw, size):
            w, h = size
            draw.rectangle([20, 20, w - 20, h - 20], outline=(60, 60, 60), width=6)
            _label(draw, (60, 60), "DM ONLY MAP", size=55)
            _label(draw, (200, 400), "X", size=90, fill=(150, 20, 20))
        _synth((1000, 800), noplayer_dm).save(source / "noplayer_dm.png")

        # 6. Picture (player-facing), jpg. Used as both dm_file and player_file
        #    to also exercise "picture also listed in the DM set" branch.
        def wagon(draw, size):
            w, h = size
            draw.rectangle([0, h // 2, w, h], fill=(120, 90, 60))
            draw.ellipse([w // 4, h // 2 - 40, w // 4 + 220, h // 2 + 180], fill=(90, 60, 40))
            _label(draw, (40, 40), "The wagon", size=60, fill=(40, 40, 40))
        _synth((1800, 1200), wagon).convert("RGB").save(source / "wagon.jpg", quality=90)

        # 7. RGBA picture with a transparent jagged bottom edge (Patreon-style cutout).
        rgba = Image.new("RGBA", (1000, 700), (0, 0, 0, 0))
        d = ImageDraw.Draw(rgba)
        d.rectangle([0, 0, 999, 500], fill=(40, 70, 120, 255))
        _label(d, (40, 40), "Night street", size=60, fill=(255, 255, 255, 255))
        # jagged: alpha ramps down in a zig-zag so the bottom edge is irregular, not a clean box
        import random
        rng = random.Random(42)
        for x in range(0, 1000, 20):
            cut = 500 + rng.randint(0, 150)
            for xx in range(x, min(x + 20, 1000)):
                for yy in range(cut, 700):
                    d.point((xx, yy), fill=(40, 70, 120, 0))
        rgba.save(source / "rgba_watermark.webp", lossless=True)

        # 8. Multi-floor sheet: title band + 3 stacked floor panels + signature band.
        SHEET_W = 1200
        TITLE_H, FLOOR_H, SIG_H = 150, 900, 100
        sheet_h = TITLE_H + FLOOR_H * 3 + SIG_H

        def sheet(draw, size):
            draw.rectangle([0, 0, SHEET_W, TITLE_H], fill=(210, 200, 170))
            _label(draw, (30, 45), "TEST SHEET TITLE", size=60)
            colors = [(200, 220, 200), (200, 200, 220), (220, 200, 200)]
            for i in range(3):
                y0 = TITLE_H + i * FLOOR_H
                draw.rectangle([0, y0, SHEET_W, y0 + FLOOR_H], fill=colors[i])
                draw.rectangle([20, y0 + 20, SHEET_W - 20, y0 + FLOOR_H - 20], outline=(60, 60, 60), width=5)
                _label(draw, (50, y0 + 50), f"FLOOR {i + 1}", size=70)
            y0 = TITLE_H + FLOOR_H * 3
            draw.rectangle([0, y0, SHEET_W, y0 + SIG_H], fill=(230, 230, 230))
            _label(draw, (20, y0 + 15), "S", size=60, fill=(80, 80, 80))
        _synth((SHEET_W, sheet_h), sheet).save(source / "sheet_3floor.webp", lossless=True)

        title_rect = f"0,0,{SHEET_W},{TITLE_H}"                     # aspect 8.0 -> header band
        sig_rect = f"0,{TITLE_H + FLOOR_H * 3},120,{SIG_H}"          # aspect 1.2 -> footer band
        keep_field = f"{title_rect};{sig_rect}"

        manifest_csv = tmp / "manifest.csv"
        with open(manifest_csv, "w", newline="", encoding="utf-8") as f:
            w = csv.writer(f)
            w.writerow(REQUIRED_COLUMNS)
            w.writerow([10, "map", "Test Site", "W1", "Wide Map", "wide_dm.jpg", "wide_player.jpg", "", "", "", ""])
            w.writerow([15, "map", "Test Site", "S1", "Small Low-Res Map", "small_dm.png", "small_player.png", "", "", "", ""])
            w.writerow([20, "map", "Test Site", "T1", "Tall Map", "tall_dm.png", "tall_player.png", "", "", "", ""])
            w.writerow([30, "map", "Test Site", "R1", "Redacted Map", "redact_dm.png", "", "100,200,160,120;900,700,160,120", "", "", ""])
            w.writerow([40, "map", "Test Site", "N1", "No Player Map", "noplayer_dm.png", "", "", "", "", ""])
            w.writerow([50, "map", "Test Sheet", "F1", "Floor 1", "sheet_3floor.webp", "sheet_3floor.webp",
                        "", f"0,{TITLE_H},{SHEET_W},{FLOOR_H}", keep_field, ""])
            w.writerow([51, "map", "Test Sheet", "F2", "Floor 2", "sheet_3floor.webp", "sheet_3floor.webp",
                        "", f"0,{TITLE_H + FLOOR_H},{SHEET_W},{FLOOR_H}", keep_field, ""])
            w.writerow([52, "map", "Test Sheet", "F3", "Floor 3", "sheet_3floor.webp", "sheet_3floor.webp",
                        "", f"0,{TITLE_H + FLOOR_H * 2},{SHEET_W},{FLOOR_H}", keep_field, ""])
            w.writerow([100, "picture", "", "", "Wagon", "wagon.jpg", "wagon.jpg", "", "", "", ""])
            w.writerow([101, "picture", "", "", "Night Street (RGBA)", "", "rgba_watermark.webp", "", "", "", ""])

        rows, parse_warnings = parse_manifest(manifest_csv)
        assert not parse_warnings, f"unexpected manifest parse warnings: {parse_warnings}"
        plan = build_plan(rows, source)

        def titles(specs, kind=None):
            return [s.row.title for s in specs if kind is None or s.kind == kind]

        # --- ordering (by 'order' column, not by row/creation order) ---
        expected_player_maps = ["Wide Map", "Small Low-Res Map", "Tall Map", "Redacted Map", "Floor 1", "Floor 2", "Floor 3"]
        expected_dm_maps = ["Wide Map", "Small Low-Res Map", "Tall Map", "Redacted Map", "No Player Map", "Floor 1", "Floor 2", "Floor 3"]
        assert titles(plan.player_specs, "map") == expected_player_maps, titles(plan.player_specs, "map")
        assert titles(plan.dm_specs, "map") == expected_dm_maps, titles(plan.dm_specs, "map")

        # --- no-player-version map is absent from the player PDF, and warned about ---
        assert "No Player Map" not in titles(plan.player_specs)
        assert any("No Player Map" in w and "PLAYER_MAPS" in w for w in plan.warnings), plan.warnings

        # --- redacted map needs a visual check ---
        assert any("Redacted Map" in e and "needs visual check" in e for e in plan.run_log), plan.run_log

        # --- pictures are last, in both sets, after the maps ---
        assert titles(plan.player_specs, "picture") == ["Wagon", "Night Street (RGBA)"]
        assert titles(plan.dm_specs, "picture") == ["Wagon"]  # rgba picture has no dm_file
        assert [s.kind for s in plan.player_specs[-2:]] == ["picture", "picture"]
        assert [s.kind for s in plan.dm_specs[-1:]] == ["picture"]
        assert all(s.kind == "map" for s in plan.player_specs[:-2])
        assert all(s.kind == "map" for s in plan.dm_specs[:-1])

        # --- RGBA flattens onto WHITE, not black ---
        flat = open_flat(source / "rgba_watermark.webp")
        corner = flat.getpixel((10, 690))  # deep in the fully-transparent jagged region
        assert corner == (255, 255, 255), f"RGBA transparent area did not flatten to white: {corner}"

        # --- build the actual PDFs ---
        results, warnings, run_log = build_pdfs(plan, out, margin_mm=DEFAULT_MARGIN_MM, captions=True)
        assert results["PLAYER_MAPS"]["pages"] == 10, results["PLAYER_MAPS"]
        assert results["DM_MAPS"]["pages"] == 10, results["DM_MAPS"]
        assert any("DPI" in w or "upscal" in w for w in warnings if "Small Low-Res Map" in w), \
            [w for w in warnings if "Small Low-Res" in w]

        player_pdf = results["PLAYER_MAPS"]["path"]
        dm_pdf = results["DM_MAPS"]["path"]
        assert player_pdf.exists() and player_pdf.stat().st_size > 0
        assert dm_pdf.exists() and dm_pdf.stat().st_size > 0

        # --- every page is A4 at 300 DPI (verify the saved PDF's own /MediaBox entries) ---
        exp_w_pt = round(mm_to_px(A4_SHORT_MM) / DPI * 72, 1)
        exp_h_pt = round(mm_to_px(A4_LONG_MM) / DPI * 72, 1)
        mb_re = re.compile(rb"/MediaBox\s*\[\s*([\d.]+)\s+([\d.]+)\s+([\d.]+)\s+([\d.]+)\s*\]")
        for pdf_path, expected_pages in ((player_pdf, 10), (dm_pdf, 10)):
            data = pdf_path.read_bytes()
            boxes = mb_re.findall(data)
            assert len(boxes) == expected_pages, f"{pdf_path.name}: found {len(boxes)} MediaBox entries, expected {expected_pages}"
            for x0, y0, x1, y1 in boxes:
                w_pt, h_pt = float(x1) - float(x0), float(y1) - float(y0)
                portrait_ok = abs(w_pt - exp_w_pt) < 1.0 and abs(h_pt - exp_h_pt) < 1.0
                landscape_ok = abs(w_pt - exp_h_pt) < 1.0 and abs(h_pt - exp_w_pt) < 1.0
                assert portrait_ok or landscape_ok, f"{pdf_path.name}: page is {w_pt}x{h_pt}pt, not A4"

        # --- no image is ever cropped: placed panel keeps the source aspect ratio and fits the area ---
        for s in plan.player_specs + plan.dm_specs:
            info, _ = compute_layout_for_spec(s, DEFAULT_MARGIN_MM, True)
            assert info is not None
            pw_src, ph_src = info["panel_size"]
            _, _, placed_w, placed_h = info["layout"]["panel_box"]
            src_ar = pw_src / ph_src
            placed_ar = placed_w / placed_h
            assert abs(src_ar - placed_ar) / src_ar < 0.01, f"{s.row.title}: aspect ratio not preserved"
            page_w = info["layout"]["page_w"]
            margin_px = mm_to_px(DEFAULT_MARGIN_MM)
            assert placed_w <= page_w - 2 * margin_px + 1, f"{s.row.title}: panel wider than printable area"

        # --- multi-floor sheet: header/footer bands present and never overlap the map panel ---
        floor_specs = [s for s in plan.player_specs if s.row.title in ("Floor 1", "Floor 2", "Floor 3")]
        assert len(floor_specs) == 3
        for s in floor_specs:
            info, _ = compute_layout_for_spec(s, DEFAULT_MARGIN_MM, True)
            layout = info["layout"]
            assert len(layout["header"]) == 1, "expected the wide title rect in the header band"
            assert len(layout["footer"]) == 1, "expected the squarer signature rect in the footer band"
            px, py, pw_, ph_ = layout["panel_box"]
            _, (hx, hy, hw, hh) = layout["header"][0]
            _, (fx, fy, fw, fh) = layout["footer"][0]
            assert hy + hh <= py + 0.5, "header band overlaps the map panel"
            assert fy >= py + ph_ - 0.5, "footer band overlaps the map panel"
            # confirm the correct 1/3 slice of the sheet was used as the panel (not the whole sheet)
            assert info["panel_size"] == (SHEET_W, FLOOR_H)

        # --- --check runs cleanly without writing PDFs ---
        import contextlib, io
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            print_check_report(plan, DEFAULT_MARGIN_MM, True)
        assert "PLAYER_MAPS" in buf.getvalue()

        print("SELF-TEST PASSED")
        print(f"  PLAYER_MAPS.pdf: {results['PLAYER_MAPS']['pages']} pages, DM_MAPS.pdf: {results['DM_MAPS']['pages']} pages")
        print(f"  {len(warnings)} warning(s) raised during the run (expected: low-res map + no-player-version map)")
        return True

    except AssertionError as e:
        print(f"SELF-TEST FAILED: {e}")
        return False
    except Exception as e:
        print(f"SELF-TEST ERROR: {type(e).__name__}: {e}")
        return False
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


if __name__ == "__main__":
    main()

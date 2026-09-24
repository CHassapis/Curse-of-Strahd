#!/usr/bin/env python3
"""Build per-reader "book packs" of the published text, for the audit readers.

Downloads the Curse of Strahd adventure data (and Ravenloft: The Horrors Within,
for Saidra d'Honaire) from the 5etools data mirror and writes plain Markdown
files into book/, one per reader scope, with book page numbers kept so every
BOOK FACT can be cited.

book/ is git-ignored: the published text is copyrighted and must not be
committed. Anyone (or any reader session) can rebuild it with:

    python3 tools/extract_book.py
"""
import json
import os
import re
import sys
import urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "book")
SRC = os.path.join(OUT, "_src")
MIRROR = "https://raw.githubusercontent.com/5etools-mirror-3/5etools-src/main/data/"

# Chapter indexes into adventure-cos.json "data" (verified against the file).
COS = {
    0: "Foreword", 1: "Introduction", 2: "Ch 1 Into the Mists",
    3: "Ch 2 The Lands of Barovia", 4: "Ch 3 The Village of Barovia",
    5: "Ch 4 Castle Ravenloft", 6: "Ch 5 The Town of Vallaki",
    7: "Ch 6 Old Bonegrinder", 8: "Ch 7 Argynvostholt",
    9: "Ch 8 The Village of Krezk", 10: "Ch 9 Tsolenka Pass",
    11: "Ch 10 The Ruins of Berez", 12: "Ch 11 Van Richten's Tower",
    13: "Ch 12 The Wizard of Wines", 14: "Ch 13 The Amber Temple",
    15: "Ch 14 Yester Hill", 16: "Ch 15 Werewolf Den", 17: "Epilogue",
    18: "App A Character Options", 19: "App B Death House",
    20: "App C Treasures", 21: "App D Monsters and NPCs",
    22: "App E The Tarokka Deck", 23: "App F Handouts",
}

PACKS = [
    # (file name, title, chapter indexes, status)
    ("reader4_castle_ravenloft.md", "Reader 4 - Castle Ravenloft", [5], "remaining"),
    ("reader5_north.md", "Reader 5 - North: Argynvostholt, Krezk, Tsolenka Pass, Berez",
     [8, 9, 10, 11], "remaining"),
    ("reader6_west_south.md", "Reader 6 - Van Richten's Tower, Wizard of Wines, "
     "Amber Temple, Yester Hill, Werewolf Den", [12, 13, 14, 15, 16], "remaining"),
    ("reader7_appendices.md", "Reader 7 - NPC and treasure appendices (+ Tarokka, handouts)",
     [20, 21, 22, 23], "remaining"),
    ("done_reader1_main_storyline.md", "Reader 1 (completed) - main storyline",
     [0, 1, 2, 17], "completed"),
    ("done_reader2_countryside.md", "Reader 2 (completed) - countryside, Barovia village, "
     "Old Bonegrinder, Death House", [3, 4, 7, 19], "completed"),
    ("done_reader3_vallaki.md", "Reader 3 (completed) - Vallaki", [6], "completed"),
]

# Tags whose third field is a display name ({@creature Izek Strazni|CoS|Izek}).
# All others show their first field ({@area Saidra's Lair|13d|x} -> Saidra's Lair).
TAG_RE = re.compile(r"\{@(\w+)\s*([^{}]*)\}")


def _tag(m):
    tag, body = m.group(1), m.group(2)
    parts = body.split("|")
    first = parts[0]
    if tag == "dc":
        return "DC " + first
    if tag == "chance":
        return first + "%"
    if tag == "recharge":
        return "(Recharge " + (first + "-6" if first and first != "6" else "6") + ")"
    if tag == "hit":
        return first if first[:1] in "+-" else "+" + first
    if tag in ("i", "italic"):
        return "*" + first + "*"
    if tag in ("b", "bold"):
        return "**" + first + "**"
    if tag in ("area", "filter", "book", "adventure", "quickref", "link", "5etools",
               "footnote", "note", "loader", "color", "highlight", "help"):
        return first
    if len(parts) >= 3 and parts[2]:
        return parts[2]
    return first


def clean(s):
    prev = None
    while prev != s:
        prev, s = s, TAG_RE.sub(_tag, s)
    return s


def render(e, depth, out):
    if isinstance(e, str):
        out.append(clean(e) + "\n")
        return
    if isinstance(e, list):
        for x in e:
            render(x, depth, out)
        return
    if not isinstance(e, dict):
        return
    t = e.get("type")
    name = clean(e["name"]) if e.get("name") else None
    page = e.get("page")
    pg = f" (p. {page})" if page else ""

    if t in ("section", "entries") and name:
        out.append("\n" + "#" * min(depth, 6) + " " + name + pg + "\n")
        render(e.get("entries", []), depth + 1, out)
    elif t == "insetReadaloud":
        buf = []
        render(e.get("entries", []), depth + 1, buf)
        out.append("\n> **[READ-ALOUD]**\n" +
                   "\n".join("> " + ln for ln in "".join(buf).strip().splitlines()) + "\n\n")
    elif t == "inset":
        buf = []
        render(e.get("entries", []), depth + 1, buf)
        out.append("\n> **[SIDEBAR: " + (name or "") + "]**" + pg + "\n" +
                   "\n".join("> " + ln for ln in "".join(buf).strip().splitlines()) + "\n\n")
    elif t == "quote":
        buf = []
        render(e.get("entries", []), depth + 1, buf)
        by = (" - " + clean(e["by"])) if e.get("by") else ""
        out.append("\n> " + " ".join("".join(buf).split()) + by + "\n\n")
    elif t == "list":
        for it in e.get("items", []):
            buf = []
            render(it, depth + 1, buf)
            out.append("- " + " ".join("".join(buf).split()) + "\n")
        out.append("\n")
    elif t == "item":
        buf = []
        render(e.get("entries", e.get("entry", [])), depth + 1, buf)
        out.append((f"**{name}** " if name else "") + " ".join("".join(buf).split()))
    elif t == "table":
        cap = clean(e.get("caption", "")) if e.get("caption") else ""
        if cap:
            out.append("\n**Table: " + cap + "**\n")
        labels = [clean(str(c)) for c in e.get("colLabels", [])]
        if labels:
            out.append("\n| " + " | ".join(labels) + " |\n|" + "---|" * len(labels) + "\n")
        for row in e.get("rows", []):
            cells = []
            for c in (row.get("row", []) if isinstance(row, dict) else row):
                buf = []
                if isinstance(c, dict) and c.get("type") == "cell":
                    roll = c.get("roll", {})
                    cells.append(str(roll.get("exact", f"{roll.get('min', '')}-{roll.get('max', '')}")))
                    continue
                render(c, depth + 1, buf)
                cells.append(" ".join("".join(buf).split()))
            out.append("| " + " | ".join(cells) + " |\n")
        out.append("\n")
    elif t == "image":
        title = clean(e.get("title", "")) if e.get("title") else ""
        if title:
            kind = "MAP" if re.search(r"\bmap\b", title, re.I) else "Image"
            out.append(f"\n[{kind}: {title}]\n")
    elif t == "gallery":
        render(e.get("images", []), depth, out)
    elif t == "statblock":
        out.append(f"\n[Stat block: {e.get('name') or e.get('tag', '')}]\n")
    else:
        if name:
            out.append("\n" + "#" * min(depth, 6) + " " + name + pg + "\n")
        for k in ("entries", "items", "images"):
            if k in e:
                render(e[k], depth + 1, out)


def fetch(rel):
    os.makedirs(SRC, exist_ok=True)
    path = os.path.join(SRC, os.path.basename(rel))
    if not os.path.exists(path):
        print("downloading", rel, file=sys.stderr)
        urllib.request.urlretrieve(MIRROR + rel, path)
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def words(s):
    return len(re.findall(r"\w+", s))


def main():
    cos = fetch("adventure/adventure-cos.json")["data"]
    for i, title in COS.items():
        got = clean(cos[i].get("name", ""))
        if title.split(" ", 2)[-1].lower() not in got.lower():
            sys.exit(f"chapter index {i} is '{got}', expected '{title}' - mirror layout changed")

    index = ["# Book packs (published text, for the audit readers)\n",
             "Generated by tools/extract_book.py from the 5etools data mirror. Git-ignored.\n",
             "| File | Scope | Status | Words |", "|---|---|---|---|"]
    for fname, title, chs, status in PACKS:
        out = [f"# {title}\n", "Published text only - BOOK FACT source. Page numbers are 2016 print pages.\n"]
        for i in chs:
            render(cos[i], 2, out)
        text = re.sub(r"\n{3,}", "\n\n", "".join(out))
        with open(os.path.join(OUT, fname), "w", encoding="utf-8") as f:
            f.write(text)
        index.append(f"| {fname} | {', '.join(COS[i] for i in chs)} | {status} | {words(text):,} |")

    # Saidra d'Honaire: the Dementlieu entry of Ravenloft: The Horrors Within.
    rhw = fetch("book/book-rhw.json")["data"]
    hits = []

    def find(e):
        if isinstance(e, dict):
            if e.get("name") and re.search(r"dementlieu", e["name"], re.I) and e.get("type") in ("section", "entries"):
                hits.append(e)
                return
            for v in e.values():
                find(v)
        elif isinstance(e, list):
            for x in e:
                find(x)
    find(rhw)
    out = ["# Saidra d'Honaire - Ravenloft: The Horrors Within (2026)\n",
           "Published text only - BOOK FACT source for task E. Not yet integrated into the campaign.\n"]
    for h in hits:
        render(h, 2, out)
    text = re.sub(r"\n{3,}", "\n\n", "".join(out))
    if "Saidra" not in text:
        sys.exit("Saidra section not found in book-rhw.json - mirror layout changed")
    with open(os.path.join(OUT, "saidra_rhw.md"), "w", encoding="utf-8") as f:
        f.write(text)
    index.append(f"| saidra_rhw.md | RHW: Dementlieu / Saidra d'Honaire | task E | {words(text):,} |")

    # The Horrors Within's Barovia entry: the 2026 view of Strahd's domain.
    bar = []

    def find_barovia(e):
        if isinstance(e, dict):
            if e.get("name") == "Barovia" and e.get("type") in ("section", "entries"):
                bar.append(e)
                return
            for v in e.values():
                find_barovia(v)
        elif isinstance(e, list):
            for x in e:
                find_barovia(x)
    find_barovia(rhw)
    out = ["# Barovia - Ravenloft: The Horrors Within (2026)\n",
           "Published text only - BOOK FACT source (2026 domain entry). The campaign follows the 2016 adventure unless noted.\n"]
    for h in bar[:1]:
        render(h, 2, out)
    text = re.sub(r"\n{3,}", "\n\n", "".join(out))
    with open(os.path.join(OUT, "rhw_barovia.md"), "w", encoding="utf-8") as f:
        f.write(text)
    index.append(f"| rhw_barovia.md | RHW: Barovia domain entry | skill / task E | {words(text):,} |")

    with open(os.path.join(OUT, "INDEX.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(index) + "\n")
    print("\n".join(index))


if __name__ == "__main__":
    main()

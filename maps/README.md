# Map printing (`tools/make_a4_maps.py`)

Turns your map/picture images into two ready-to-print A4 PDFs:

- `maps/print/PLAYER_MAPS.pdf` — safe to hand to players
- `maps/print/DM_MAPS.pdf` — full DM information (room letters, traps, secret doors, notes)

One floor/level per page, at 300 DPI, without ever cropping or distorting the
source image.

## 1. Where to put your files

Drop your image files (`.webp`, `.jpg`/`.jpeg`, `.png`, …) into `maps/source/`.
If your files already live somewhere else (for example `Maps/`, where a batch
upload landed), you don't need to move them — just point the tool at that
folder with `--source Maps` (see "How to run it" below). All `dm_file` /
`player_file` paths in the manifest are resolved relative to whichever
`--source` folder you pass in.

**Tip:** many Patreon map packs already include an unlabelled / "player"
variant alongside the DM version (no room letters, secret doors, or trap
markers). That unlabelled variant is almost always the best `player_file` —
prefer it over asking this tool to redact a DM file whenever one exists.

## 2. The manifest

The manifest is a UTF-8 CSV with this exact header row:

```
order, set, location, level, title, dm_file, player_file, redact, crop, keep, notes
```

| Column | Meaning |
|---|---|
| `order` | A number controlling page order. Lower prints first. Rows with equal (or blank) `order` fall back to their order in the CSV file. Pictures are always printed after all maps regardless of `order` — see below. |
| `set` | `map` or `picture`. |
| `location` | The building/place, e.g. `Old Bonegrinder`. Used in the page caption. |
| `level` | The floor/level code, e.g. `O2`. Used in the page caption. Leave blank for pictures. |
| `title` | The floor/picture name, e.g. `Bone Mill`. |
| `dm_file` | Image file for the DM page, relative to `--source`. |
| `player_file` | Image file for the player page, relative to `--source`. |
| `redact` | Optional. `x,y,w,h` rectangles (source-image pixels), separated by `;`. Applied to the player page's source: `player_file` if given (to mask anything the publisher's "player version" still shows, such as a hidden room or a trap), otherwise `dm_file` (to build a player page from the DM sheet). Never applied to DM pages. Each rectangle is filled with the median colour of a thin ring of pixels around it. |
| `crop` | Optional. One `x,y,w,h` rectangle (source-image pixels): the single floor panel to print on *this* page, when several floors share one sheet image. Empty = use the whole image. |
| `keep` | Optional. `x,y,w,h` rectangles (source-image pixels), separated by `;`: sheet elements outside the `crop` panel to carry onto the page anyway (title, compass rose, scale note, cartographer's signature, logos, Patreon watermarks). See "Multi-floor sheets" below. |
| `notes` | Free text, not printed. For your own reference. |

A **picture** row only needs `player_file` (`dm_file` is optional — see
below); `redact`, `crop` and `keep` are ignored for pictures.

### Player pages — the rule the tool enforces

The tool cannot look at an image and tell whether it shows a room letter or a
secret door. So a page is only allowed into `PLAYER_MAPS.pdf` when the
manifest gives it an explicit, trusted player source:

- `player_file` is set (a genuinely player-safe image), **or**
- `dm_file` is set **and** `redact` lists at least one rectangle.

If a map row has neither, it is **left out of `PLAYER_MAPS.pdf`** and the
tool prints a clear warning naming it — nothing DM-only ever slips through
by accident. Any page built from `redact` is also flagged `needs visual
check` in the run log, since a filled rectangle is not a guarantee that
nothing sensitive peeks out around its edges — always eyeball the result.

`DM_MAPS.pdf` uses `dm_file` when present, falling back to `player_file`
for maps that have no DM-only information at all.

### Pictures ("To show the players")

Rows with `set = picture` (things like "the wagon" or "night street", not
maps) are always placed **after every map**, under a divider page titled
**"To show the players"**, at the end of `PLAYER_MAPS.pdf`. Give a picture a
`dm_file` too if you also want it at the end of `DM_MAPS.pdf` (handy so the
DM can pull it up without switching PDFs); leave `dm_file` blank to keep it
player-PDF-only.

### Multi-floor sheets (`crop` and `keep`)

Some map packs draw two to four floors on one sheet — e.g. an attic, upper
floor and ground floor stacked in one image, or a title panel plus a grid of
floor panels. You still want **one floor per A4 page**, but the sheet's
title, compass rose, scale note, signature and any logo/Patreon watermark
shouldn't be lost just because they sit outside that floor's panel.

Give each floor its own manifest row, all pointing at the *same* sheet file,
each with its own `crop` (that floor's panel) and the *same* `keep` list
(the shared sheet furniture):

- `crop` selects the one panel that becomes this page's map.
- `keep` pulls in extra rectangles from *outside* that panel and places them
  in the page's margins — never on top of the map. Wide rectangles (title
  banners, scale notes) go in a header strip above the map; squarer ones
  (signature, compass, logo, watermark) go in a footer strip below it. The
  map panel's own area shrinks a little to make room. Kept elements print
  at roughly the map's own scale, but never smaller than about 9 mm tall,
  so a signature or logo stays legible even when the map itself is shrunk.
- If a floor's `crop` panel already contains an element (e.g. the title sits
  inside that floor's own panel), you don't need to list it again in `keep`.
- `crop`/`keep` coordinates apply to whichever file is actually used to
  build the page (the DM sheet for the DM page, the player sheet — or the
  redacted DM sheet — for the player page). When both `dm_file` and
  `player_file` are given, they should be pixel-aligned copies of the same
  sheet at the same size; the tool warns if their sizes don't match.

To find the pixel coordinates, open the sheet in any image viewer/editor
that shows a pixel position under the cursor (GIMP, Photoshop, Preview,
paint.net, even MS Paint) and read off the corners of each panel and each
element you want to keep.

## 3. How to run it

```
python3 tools/make_a4_maps.py --manifest maps/manifest.csv
```

Useful options:

```
--source maps/source     # folder the manifest's file paths are relative to
                          # (e.g. --source Maps, if that's where files landed)
--out maps/print         # output folder for the two PDFs
--margin-mm 8             # page margin in mm (default 8)
--no-captions             # turn off the caption strip
--check                   # validate the manifest and report per-image
                          # size / orientation / effective DPI / warnings,
                          # WITHOUT writing any PDF — use this first
--self-test               # generate synthetic test images, run the full
                          # pipeline against them, assert everything holds,
                          # print PASS/FAIL, then clean up after itself
```

Run `--check` after editing the manifest to catch typos, missing files, and
DPI problems before spending time on a full build.

Run `--self-test` any time to confirm the tool itself is working correctly
on your machine — it doesn't touch your manifest or `maps/source/`.

## 4. What the warnings mean

- **"no player_file and no redact rectangles - excluded from PLAYER_MAPS.pdf"**
  — this map has no trusted player-safe source at all. Add a `player_file`,
  or add `redact` rectangles to `dm_file`.
- **"effective resolution ~NN DPI (below 150 DPI)"** — at the size this
  image ends up printed on the page, the source doesn't have enough pixels
  to look crisp. Find a higher-resolution source, or accept the softness.
- **"image upscaled N.Nx on the page (more than 2x)"** — the same problem
  seen from the other direction: the image is being blown up more than 2x
  its native pixel size to fill the page.
- **"dm_file and player_file are different sizes"** — with `crop`/`keep` in
  use, the two files need to be pixel-aligned (same size) or the panel/keep
  rectangles will land in different places on each. Re-export them at
  matching sizes.
- **"crop/keep rectangle ... outside the ... image"** — a coordinate in the
  manifest is out of bounds for that file; it gets clipped (or skipped, for
  `keep`) rather than failing the build, but double-check the numbers.
- **needs visual check** (run log, not a warning) — this player page was
  built by redacting a DM file. Open the PDF and confirm the filled
  rectangles fully cover the secret information with nothing visible at the
  edges.

## 5. Worked example: a four-level building + one picture

See `maps/manifest.example.csv` for a runnable example covering: a
multi-floor sheet split with `crop`/`keep` (Old Bonegrinder, floors O1–O4,
one shared sheet image), a simple map with separate DM/player files, a map
redacted from a DM-only file, a map with no player version at all (so you
can see the warning fire), and a player-facing picture.

Try it:

```
python3 tools/make_a4_maps.py --manifest maps/manifest.example.csv --source maps/source --check
```

(It will report every referenced file as missing, since the example
manifest doesn't ship with real images — that's expected. Copy its rows
into your own `maps/manifest.csv` and point them at your real files.)

## Limitations

- The tool trusts the manifest, not image content: it cannot detect room
  letters, secret doors or traps itself. Player-safety depends entirely on
  you marking the right column correctly (see "Player pages" above).
- `keep` elements are grouped into one header band and one footer band
  based on their aspect ratio (wide → header, squarer → footer); the tool
  has no way to know which is really "the title" versus "the logo" beyond
  that heuristic.
- The scale used as a legibility floor for `keep` elements is estimated
  from the map panel's fit *before* the header/footer bands are subtracted,
  as a practical approximation — the map panel itself is always sized
  correctly, against the *actual* remaining area, afterwards.
- Redaction fills rectangles with a plain median colour sampled from a ring
  around them; it does not reconstruct texture or line art underneath, and
  a rectangle drawn too tight around an odd-shaped label can leave a sliver
  visible — always check redacted pages (they're flagged for it).

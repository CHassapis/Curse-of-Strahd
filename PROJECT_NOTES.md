# Curse of Strahd — consolidated project notes

The single record of what is established, what is pending and what is waiting
on a decision. Readers and rebuilds read this first. Nothing here overrides a
campaign decision; book differences are recorded, not auto-applied.

Last updated: 2026-09-24 (cloud session, branch `claude/strahd-campaign-readers-m61g1u`).

---

## 1. Where the material lives

| Material | Location | Status |
|---|---|---|
| Session Prep IV (docx) | repo root; text in `campaign/text/` | **Uploaded 2026-09-24** (15,402 words) |
| Future Possible (docx) | repo root; text in `campaign/text/` | **Uploaded** (8,255 words) |
| Items and Treasure (docx) | repo root; text in `campaign/text/` | **Uploaded** (2,545 words) |
| Strahd's Brides DM sheet, NPC cards, item cards, player handouts, Offalia combat sheet (PDF) | repo root; text in `campaign/text/` | **Uploaded** |
| Strahd DM sheet | — | **Not uploaded yet** |
| Reader reports 1–3 and their skill notes | — | **Not uploaded yet** (only in the original environment) |
| Ledger handout (earlier version) | — | Lost; being rebuilt from Prep IV Scene 1 (task C) |
| Maps and pictures | `Maps/`; inventory in `maps/INVENTORY.md` | **Uploaded** + 3 book maps fetched (Vistani Camp, Castle main floor, Winery) |
| Barovia Route Map (DM reference artifact) | https://claude.ai/artifact/GwdLQDdUTFKqvJFPuDfXvN; snapshot in `campaign/` | Secondary summary |
| Shared transcript of the original conversation | https://claude.ai/share/7147c102-e93c-48c8-985f-d41c19f6cf08 | Blocked by Cloudflare from the container; the user pasted the key parts |
| Published Curse of Strahd text (2016) | 5etools data mirror (the data behind https://5e.tools/adventure.html#cos) → `python3 tools/extract_book.py` → `book/` | Git-ignored (copyrighted) |
| Ravenloft: The Horrors Within (2026) — Saidra d'Honaire, Barovia entry | Same tool → `book/saidra_rhw.md`, `book/rhw_barovia.md` | Git-ignored |

**Still wanted:** the Strahd DM sheet and the reader 1–3 reports (with their
skill notes). Upload them to the repo root like the other files.

---

## 2. Finding classification (every reader finding uses exactly one)

| Label | Meaning |
|---|---|
| **BOOK FACT** | What the published adventure says, with chapter/area/page. |
| **CURRENT CAMPAIGN VERSION** | What our documents say, with document/section. |
| **CONFLICT** | The two differ and it is not yet known whether the difference is intentional. |
| **DECISION REQUIRED** | A conflict the user must resolve. Current campaign version stays until then. |
| **CONFIRMED FIX** | An error in our documents (unintended), safe to correct. |
| **OPTIONAL IMPROVEMENT** | Useful addition; not an error. Never applied without approval. |

A difference is **not** an error when the campaign changed it on purpose
(brides' roles, item cards, Madam Eva's messages after each Tarokka item,
difficulty levels, and so on).

**Homebrew NPCs (user, 2026-09-24):** the DM riffs at the table, so some
characters are homebrew NPCs who don't exist in the book (e.g. Miranda,
Viktor Ivanovich, Ethradir's mother). An NPC, relationship or scene that is
absent from the book is **CURRENT CAMPAIGN VERSION (homebrew)** — never an
error, never a CONFLICT for that reason alone. Only flag a homebrew NPC when it
contradicts a book fact the campaign otherwise keeps (then CONFLICT), and
record homebrew NPCs in the skill as `[CAMPAIGN]` with the tag *homebrew*.

---

## 3. Reader status

| # | Scope | Status | Book pack (`book/`) | Book words |
|---|---|---|---|---|
| 1 | Main storyline | **Completed** | `done_reader1_main_storyline.md` | 11,582 |
| 2 | Countryside, Barovia Village, Old Bonegrinder, Death House | **Completed** | `done_reader2_countryside.md` | 27,986 |
| 3 | Vallaki | **Completed** | `done_reader3_vallaki.md` | 20,360 |
| 4 | Castle Ravenloft | **Not started** — failed at launch before; must restart fresh | `reader4_castle_ravenloft.md` | 30,696 |
| 5 | North: Argynvostholt, Krezk, Tsolenka Pass, Berez | **Not started** | `reader5_north.md` | 23,251 |
| 6 | Van Richten's Tower, Wizard of Wines, Amber Temple, Yester Hill, Werewolf Den | **Not started** | `reader6_west_south.md` | 25,090 |
| 7 | NPC and treasure appendices (+ Tarokka deck, handouts) | **Not started** | `reader7_appendices.md` | 13,438 |

Readers 1–3 together: ~60,000 of ~150,000 campaign words reviewed; ~18 errors
and ~20 useful improvements found. Remaining readers are **not authorised** to
start until the user says so (see §8).

---

## 4. Confirmed corrections (from readers 1–3)

Apply where relevant. They are corrections, not redesigns. "Book check" is a
re-check against the published text done in this session.

| ID | Correction | Book check |
|---|---|---|
| C-01 | The Tarokka **ally is Van Richten**, not Madam Eva. Lines to fix (reader 5a): Future Possible §1 "Major events" row "All four items — Eva becomes their ally…"; Future Possible §2 "Madam Eva's messages", Icon row "She becomes their ally for the castle"; NPC card 23 (Madam Eva) "After all four items she becomes their ally". Keep "Four. Then I keep my word." and her telling them where Strahd waits (C-03). | Campaign reading — established by reader 1 |
| C-02 | Madam Eva does **not** fight or help against Strahd as earlier documents implied. | Established by reader 1 |
| C-03 | Eva still keeps her promise to tell the party where Strahd waits. | Campaign element — keep |
| C-04 | Old Bonegrinder has **four levels, O1–O4**, matching the user's Bonegrinder map. **Our Prep IV Scene 1 search has only three floors**; the floor table must match the four-level map. | ✔ Ch 6: O1 Ground Floor, O2 Bone Mill, O3 Bedroom, O4 Domed Attic |
| C-05 | The gallows crossroads lies **behind** the party on the way to Tser Pool, not on the Vallaki road. | ✔ Ch 2: signpost at the gallows points east to Barovia Village, northwest to Tser Pool, southwest to Ravenloft/Vallaki |
| C-06 | **Rictavio's wagon is at the Arasek Stockyard** (N5). Only his horse (Drusilla) is at the inn stable (N2f). *See D-7.* | ✔ Ch 5, N2/N5 (p. 115) |
| C-07 | Keep the possible **escaped-tiger** event and its clues toward the western tower (Sunsword, per our Tarokka reading). | ✔ Ch 5: saber-toothed tiger, 84 hp, half plate AC 17, in the wagon (N5) |
| C-08 | **St Andral's bones** are in Henrik's upstairs wardrobe, **Perception DC 15** — not under the counter as our docs have it. | ✔ Ch 5, N6e Henrik's Bedroom (p. 117): secret compartment in the wardrobe base, DC 15 Wisdom (Perception); also 30 sp and 12 ep |
| C-09 | **Victor's teleportation circle**: 3d10 force damage; a creature reduced to 0 HP is disintegrated. The Cassian interaction needs an **explicit warning**. | ✔ Ch 5, N3 attic: 3d10 force, not teleported, disintegrated at 0 HP; DC 15 Arcana reveals the flaw |
| C-10 | Correct the **Baron's physical description**: in the book he is a **big man in a breastplate with two mastiffs**, not small and round. | Reader 3 |
| C-11 | **High difficulty is intentional** for major fights. Do not reduce encounters for being hard. | Campaign policy |
| C-12 | **Restore the ledger handout.** Use the countryside reader's idea about the meaning of the ticks and crosses; keep the existing style and purpose. | Campaign handout (not in the book) |

### 4a. Reader 1–3 detail (from the original conversation, pasted by the user 2026-09-24)

- Error counts: reader 1 (main storyline) 4, reader 2 (countryside) 5, reader 3 (Vallaki) 9 — 18 total.
- Each completed reader also wrote **notes for the skill**; these are in the original
  environment and must be uploaded to `readers/` (not recreated).
- OPTIONAL IMPROVEMENTS already found (not applied):
  - Reader 2, Scene 1: use the mill's own props (the hags' scrying barrel, the cabinet
    with locks of hair); a meaning for the ledger's ticks and crosses (task C); quiet,
    fight-free beats for the road.
  - Reader 3: **Lady Wachter's Wish** — her spy shadows the party; she asks them to kill
    Izek (Ireena's brother); if they refuse she pays the Vistani to kill them after they
    leave town; if they saved Arabelle, the Vistani return her gold.
  - Reader 3: at the Festival a guard laughs when the sun fails to light and the Baron
    drags him behind his horse — a clear moment for Barry and Fedra to step in.
- Maps needed beyond Prep IV: **Castle Ravenloft dining hall** (dinner session) and the
  **Wizard of Wines**.
- Agent history: the first reader batch hit a usage limit (~11:20) and wrote nothing;
  three restarted after the reset and finished; the castle reader failed at launch.

---

## 5. Decisions that belong to the user (current campaign version stays until decided)

| ID | Topic | CURRENT CAMPAIGN VERSION | BOOK FACT | Status |
|---|---|---|---|---|
| D-1 | **Ethradir and the dream pastries** | Pastries put people to **sleep with no save** — chosen on purpose earlier; reader 2 recommends leaving that. Open question: by the book it is a trance, so an elf's Trance gives no protection — **does Ethradir stay immune?** | Ch 6: eating a whole pastry → **DC 16 Constitution save** or a **trance for 1d4 + 4 hours**: incapacitated, speed 0; ends on damage or when shaken awake with an action | DECISION REQUIRED |
| D-2 | **Hag Eye** | Item card 02 at Old Bonegrinder: "Top shelf — or destroy it and the hags lose them" (Route Map). Open question: **what does smashing it do to the two surviving hags?** | Ch 6 and Ch 4, K62: Morgantha gave the coven's hag eye to **Cyrus Belview** at Castle Ravenloft; he wears it on a twine loop with the key to the K60 chest and doesn't know it's magic | DECISION REQUIRED — keep our card until decided |
| D-3 | **The Mad Mage** | Far beyond the party: blasts, teleports away, turns up later; restored, he helps once at the castle (Route Map, Mount Baratok) | Ch 2, area M (p. 39): CN archmage (Mordenkainen), memory gone, paranoid; **attacks first** (reader 2); restored and not the Tarokka ally → declines to join, leaves to find his staff and spellbook, gives each character a **charm of heroism** | DECISION REQUIRED — keep our role |
| D-4 | **Youth elixir** | Not in the hags' cabinet | Ch 6, Morgantha's cabinet: three elixirs, "Youth" (look younger for 24 h), "Laughter" (cackle fever), "Mother's Milk" (pale tincture) | DECISION REQUIRED — do not add |
| D-5 | **Patrina Velikovna** | Three brides: Ludmilla, Anastrasya, Volenta. Patrina not used | Ch 4, K84 crypt: dusk elf, would-be bride; stoned to death by her people before the dark marriage; now a **banshee** that re-forms in 24 h until wed to Strahd (a *hallow* spell stops it). Crypt holds 250 pp, 1,100 gp, 2,300 ep, 5,200 sp, 8,000 cp and her spellbook (archmage spells). **Kasimir's dark gift** (Ch 13) can restore her as an archmage (NE) who lies about helping. | DECISION REQUIRED — she can coexist (she never became a bride), but the Amber Temple/Kasimir thread and the brides' crypt scene would change. Reader 4 to map the touch points |
| D-6 | **Book treasure** | Our 67 selected item cards | Each chapter's treasure. Already raised by reader 3: the **Martikovs' two hidden stashes** (healing potions, elixirs of health, a bag of tricks) and **Rictavio's wagon** (scrolls, silvered weapons) — do these exist in our game? | Readers list book treasure as **possible omissions** only; nothing is inserted |
| D-7 | **Rictavio's wagon** | The wagon is in the inn stable and burns in Offalia's fire; "something inside roars" — which gives away the tiger and rules out the book's escaped-tiger event (tiger loose in town; aftermath points to the western tower, where our Tarokka put the Sunsword) | N5 Arasek Stockyard | DECISION REQUIRED: correct the location unless the sequence is an intentional change |

---

## 6. Barovia Route Map artifact — flags from this session

The published Route Map (read 2026-09-24) is derived from Future Possible, so
the same issues probably sit in that document.

| Where | Current text | Classification |
|---|---|---|
| Argynvostholt → events; Madam Eva thread | "Madam Eva's last message: she becomes their ally" / "After the Icon — ally" | **CONFIRMED FIX** (C-01, C-02). Eva's messages can stay; "ally" must go. The ally is Van Richten. |
| Castle → events | "The final fight — the Tarokka says where he waits" | Consistent with C-03 |
| Old Bonegrinder → card 02 Hag Eye, "Top shelf" | Our version | D-2 — keep until decided |
| Old Bonegrinder → card 01, "Wardrobe, 1st floor" | Floor naming | Check against O1–O4 (C-04) when Prep IV is available |
| Mount Baratok | Mad Mage role | D-3 — keep until decided |
| Van Richten's Tower | Van Richten appears only as "if revealed" | OPTIONAL IMPROVEMENT: show him as the Tarokka ally at the next rebuild |

The artifact is **not** changed yet. It will be updated with the final rebuild
(task G) so it stays in step with Future Possible.

---

## 7. Task board

| Task | State | Depends on |
|---|---|---|
| A. Book audit — readers 4–7 | Book packs ready; readers not started | Campaign files in the repo + user's go-ahead |
| B. Prep IV corrections | Waiting | Prep IV file; readers 4/6 for later-chapter cross-references; no final rebuild until major contradictions are known |
| C. Ledger handout | Waiting | Earlier ledger version + reader 2's tick/cross idea (both in the original conversation) |
| D. A4 maps — player and DM sets | Waiting | Map image files. Also needed: whether each map has a separate player version (removing letters and secret doors from a DM-only image by hand is slow and error-prone) |
| D. Missing Prep IV visuals | Waiting | Check existing files first: Vistani camp (Map 5.6), lake shore with rowing boat (Arabelle), town wall/palisade (Banderhobb chase end), churchyard (optional) |
| E. Saidra d'Honaire | Source located (`book/saidra_rhw.md`, 3,203 words); not integrated | Campaign documents |
| F. Curse of Strahd skill | Not started, by design | All seven reader reports |
| G. Final rebuild | Not started, by design | A–F + user decisions D-1…D-7 |

---

## 8. Running the remaining readers (when authorised)

- **Needed first:** the campaign documents in the repo. A reader without them
  can only restate the book.
- **Size:** ~92,000 book words for readers 4–7, plus the matching campaign text
  (roughly 90,000 words). That fits one reader at a time comfortably.
- **Recommendation:** run them **one at a time** (or at most two), in a cloud
  session, not four in parallel. Parallel runs finish sooner but cost the same
  or more, and a sequential run lets reader 7 (treasure/NPCs) use what readers
  4–6 found.
- **Brief for each reader:** read §2, §4, §5 of this file; read its book pack;
  read the matching campaign sections; report findings using the §2 labels,
  citing book page/area and campaign document/section; do not edit any
  campaign file; save the report to `readers/readerN_report.md`.
- **Reader 4 extra checks:** Hag Eye / Cyrus Belview (D-2), Patrina's crypt
  and the brides' crypts (D-5), Castle treasure vs our cards 56–59 and 65 (D-6),
  where Strahd waits (C-03).
- **Reader 6 extra checks:** Kasimir's dark gift and Patrina (D-5), Tarokka
  items at the Winery and Van Richten's Tower, Mad Mage references (D-3).
- **Reader 7 extra checks:** Tarokka ally card text for Van Richten (C-01),
  NPC appendix descriptions (Baron, C-10), treasure appendix vs our 67 cards
  (D-6).

---

## 9. Readers 4–7 — consolidated findings (added as each reader finishes)

Full reports: `readers/reader*_report.md`. Only the items that need the user
or change a document are listed here.

### Reader 5a — Argynvostholt (done 2026-09-24; 24 findings: 4 CONFIRMED FIX, 8 CURRENT CAMPAIGN VERSION, 5 BOOK FACT, 2 CONFLICT, 1 DECISION REQUIRED, 4 OPTIONAL IMPROVEMENT)

- **CONFIRMED FIX (C-01/C-02):** the Eva "ally" line is in three documents (see C-01).
- **NEW DECISION D-8 — Argynvost's skull:** in the book it hangs in Castle Ravenloft, K67 Hall of Bones (250 lb, Ch 4 p. 78). No campaign document says how the party gets it before Argynvostholt (level 10) and the castle (level 12), yet a knight rides with them to the castle once the beacon is lit. Options: a separate raid on the castle; stealing it after the level-6 dinner; or lighting the beacon during/after the final assault (no knight rides with them).
- **CONFLICT — where the skull goes:** book: sealed in the mausoleum (Q16), the light then rises to the tower; every book clue points to the mausoleum. Future Possible: "in the beacon at the top of the tower". Keep ours and drop the book clues, or switch to the mausoleum.
- **CONFLICT — the chapel revenants:** in the book the three chapel revenants attack on sight, and our Icon is in that chapel. Are Future Possible's "3 revenants" these three?
- **Correction to the brief:** the Icon of Ravenloft is **not** Tarokka-placed in the book; it sits on the Castle Ravenloft chapel altar (K15). Our move to the Argynvostholt chapel is deliberate and consistent. Book Tarokka spots at Argynvostholt: Q36 (Vladimir holds it), Q53 (west windowsill).
- Vladimir fight: ours 9,700 XP (Moderate at 10) is heavier than the book's 7,100 — stays (C-11). "The revenants come back" matches the book. The knight who stays is homebrew; Sir Godfrey is the book's natural candidate (optional).
- **Check with reader 4:** the Shield of the Silver Dragon (card 42) is in the Castle treasury K41 in the book — make sure it isn't placed twice.
- Possible omissions (D-6): 4 potions of invulnerability, Vladimir's +2 greatsword, a 250 gp platinum holy symbol.
- OPTIONAL (touches C-11): the book gives +1 AC and saves once the beacon is lit.
- Maps not in `Maps/`: Map 7.1 and 7.2 (Argynvostholt; 7.2 includes the third floor).

### Saidra d'Honaire — task E (done 2026-09-24)

Files: `skill/curse-of-strahd/references/book/saidra-dhonaire.md` (book layer) and
`readers/saidra_integration_options.md` (options). Book: Darklord of Dementlieu
(Port-a-Lucine), undead "phantom duchess", CR 9; weekly Grand Masquerade; *Truth or
Die*; senses lies; Tarokka aligned card Charlatan, opposed Seer. No direct link to
Strahd or Barovia in the book.

**NEW DECISION D-9 — how Saidra enters the campaign** (none replaces an NPC, homebrew included):
- **A. The Charlatan card:** Eva's message after the Tome arrives as the Charlatan; later Ezmerelda names it as Port-a-Lucine's card. Lore only.
- **B. The brooch and a second invitation (agent's recommendation):** Ireena gets card 27 (Masquerader's Brooch) as now; next dawn Saidra's *Invitation* power leaves a mask and a masquerade invitation by her bed. Inert while Strahd holds the borders; a sequel hook after he falls. No scene, no fight, no line changed.
- **C. Guest at Strahd's dinner:** she cries "Impostor!" and Strahd restrains her (his word). Crowds the dinner; overlaps with Anastrasya as hostess.
- **D. One night in Port-a-Lucine:** a side trip through the Mists after Van Richten's Tower. Largest expansion; no campaign reason to go.

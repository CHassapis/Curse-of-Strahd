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
| 4 | Castle Ravenloft | **Completed 2026-09-24** (as 4a + 4b) | `reader4_castle_ravenloft.md` | 30,696 |
| 5 | North: Argynvostholt, Krezk, Tsolenka Pass, Berez | **Completed 2026-09-24** (as 5a + 5b) | `reader5_north.md` | 23,251 |
| 6 | Van Richten's Tower, Wizard of Wines, Amber Temple, Yester Hill, Werewolf Den | **Completed 2026-09-24** (as 6a + 6b) | `reader6_west_south.md` | 25,090 |
| 7 | NPC and treasure appendices (+ Tarokka deck, handouts) | **Completed 2026-09-24** | `reader7_appendices.md` | 13,438 |

Readers 1–3 together: ~60,000 of ~150,000 campaign words reviewed; ~18 errors
and ~20 useful improvements found. Remaining readers are **not authorised** to
start until the user says so (see §8). **Update 2026-09-24:** the user authorised
readers 4–7 on cloud credits; all four finished the same day (split into 4a/4b,
5a/5b, 6a/6b, 7). Reports in `readers/`, skill notes in `skill/curse-of-strahd/references/book/`.

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
| D-3 | **The Mad Mage** | Far beyond the party: blasts, teleports away, turns up later; restored, he helps once at the castle (Route Map, Mount Baratok) | Ch 2, area M (p. 39): CN archmage (Mordenkainen), memory gone, paranoid; **attacks first** (reader 2); restored and not the Tarokka ally → declines to join, leaves to find his staff and spellbook, gives each character a **charm of heroism** | DECISION REQUIRED — keep our role. Also (reader 6b): "a vestige's gift" as a cure has no book vestige behind it — the only mind gift in the temple is *mind blank*, which blocks his restoration; and by the book he helps against Strahd only as the Tarokka ally, which he can't be alongside Van Richten (reader 7) |
| D-4 | **Youth elixir** | Not in the hags' cabinet | Ch 6, Morgantha's cabinet: three elixirs, "Youth" (look younger for 24 h), "Laughter" (cackle fever), "Mother's Milk" (pale tincture) | DECISION REQUIRED — do not add |
| D-5 | **Patrina Velikovna** | Three brides: Ludmilla, Anastrasya, Volenta. Patrina not used | Ch 4, K84 crypt: dusk elf, would-be bride; stoned to death by her people before the dark marriage; now a **banshee** that re-forms in 24 h until wed to Strahd (a *hallow* spell stops it). Crypt holds 250 pp, 1,100 gp, 2,300 ep, 5,200 sp, 8,000 cp and her spellbook (archmage spells). **Kasimir's dark gift** (Ch 13) can restore her as an archmage (NE) who lies about helping. | DECISION REQUIRED — she can coexist (she never became a bride), but the Amber Temple/Kasimir thread and the brides' crypt scene would change. Reader 4 to map the touch points |
| D-6 | **Book treasure** | Our 67 selected item cards | Each chapter's treasure. Already raised by reader 3: the **Martikovs' two hidden stashes** (healing potions, elixirs of health, a bag of tricks) and **Rictavio's wagon** (scrolls, silvered weapons) — do these exist in our game? | Readers list book treasure as **possible omissions** only; nothing is inserted |
| D-7 | **Rictavio's wagon** | The wagon is in the inn stable and burns in Offalia's fire; "something inside roars" — which gives away the tiger and rules out the book's escaped-tiger event (tiger loose in town; aftermath points to the western tower, where our Tarokka put the Sunsword) | N5 Arasek Stockyard | DECISION REQUIRED: correct the location unless the sequence is an intentional change |
| D-8 | **Argynvost's skull** | Future Possible: lighting the beacon at Argynvostholt (level 10), then a knight rides with the party to the castle (level 12) | Ch 4, K67 Hall of Bones: the skull hangs over the east doors, 250 lb (p. 78); if Strahd's location card is the Donjon, a raid on K67 would start the final fight | DECISION REQUIRED — how and when they get it (separate castle raid / after the dinner / during the finale) |
| D-9 | **Saidra d'Honaire** | Not in the campaign yet | RHW, Dementlieu | DECISION REQUIRED — option A, B (recommended by the agent), C or D; see §9 |
| D-10 | **Gulthias Staff (card 33)** | With the Yester Hill druid leader; card text has no death-scream | App C p. 221: breaking or burning it kills every blight within 300 ft that hears it; book places it with the druid at the winery (W16), where destroying it ends the siege | DECISION REQUIRED — does the scream exist in our game, and does it reach Wintersplinter (would undercut the 7,000 XP fight)? |
| D-11 | **The actual Tarokka cards drawn** | Placements known (Tome at the winery, Sunsword at the tower, Holy Symbol at the abbey, Icon at Argynvostholt, ally Van Richten), card names not recorded in the uploaded documents | Card determines the exact spot: Tome at the winery = glassblower's barrel of sand (W10); Holy Symbol best fit = the Abbot's hall behind the gold sun disk; Strahd's location options K6/K15/K25/K37/K41 and K60/K67/K85/K86/K88; the Mists card has Eva read again later for the location only (fits C-03) | DECISION REQUIRED — which five cards were drawn (may be in the Strahd DM sheet) |
| D-12 | **Leaving the castle after dinner** | "Once they explore, use the castle as written" | K7: 4 dragon wyrmlings let guests in but not out (4,400 XP, High at 6); K8: 8 gargoyles (3,600 XP) — both on the only front exit | DECISION REQUIRED — do explorers still get out? |
| D-13 | **The Icon and the chapel wedding** | Our rule: the Icon's protection breaks the charm | App C: 30-ft aura acts as *protection from evil and good* | DECISION REQUIRED — does carrying the Icon within 30 ft of Ireena end the wedding? |
| D-14 | **Treasury and study access** | Treasury "5,000 gp and more"; Ludmilla carries "the key to Strahd's study" | K41 treasury is an adamantine fortress only Strahd opens, behind a trapped route; the K37 study has no lock | DECISION REQUIRED — how they get into the treasury; what the key opens |
| D-15 | **Card 64 Staff of Healing trigger** | Second gift "only if the wedding goes ahead" | — | DECISION REQUIRED — what that means when our own payoff has Strahd refuse Vasilka |

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

### All readers: the one CONFIRMED FIX from readers 4–7

Every reader independently found the same fix: remove "ally" from Madam Eva in
Future Possible §1 "Major events" (All four items), Future Possible §2 "Madam Eva's
messages" (Icon row) and NPC card 23. Keep "Four. Then I keep my word." and the
location reveal (C-03). Book: the ally is on the Artifact card (Rictavio/Van
Richten, Ch 1 p. 15); Eva is on none of the 14 ally cards and never gives aid (Ch 2 p. 37).

### Conflicts to confirm (intentional or not?) — current campaign version stays

| # | Topic | Our version | Book | Reader |
|---|---|---|---|---|
| K-1 | Where Argynvost's skull goes | "in the beacon at the top of the tower" | sealed in the mausoleum (Q16); every book clue points there | 5a, 4b |
| K-2 | Chapel revenants at Argynvostholt | Icon in that chapel; "3 revenants" | the three chapel revenants attack on sight — are ours these three? | 5a |
| K-3 | Brides' looks | Ludmilla in red, Anastrasya in white and gold | reversed in the book; the Brides sheet says it keeps the book's gowns | 4a |
| K-4 | Emil's motive | would stop the pack taking children | wants every child turned; betrays the party unless they claim Zuleika's friendship | 6a |
| K-5 | Yester Hill | Strahd not present | the druids wait for Strahd, who watches and defends them (PROVISIONAL — Strahd sheet missing) | 6a |
| K-6 | Tome of Strahd at the winery | in the cellar "among the casks" | the only winery card puts it in the glassblower's barrel of sand (W10) | 6a, 7 |
| K-7 | The winery gems | two of three stolen | all three stolen | 6a |
| K-8 | Krezk | Dmitri pays 250 gp | Krezk has no money | 5b |
| K-9 | Baba Lysaga's hut | walks on clawed legs | walks on (and attacks with) tree-stump roots | 5b |
| K-10 | Lysaga and Strahd | "flies to tell Strahd everything" | has never faced him, fearing rejection | 5b |
| K-11 | Mongrelfolk | "stitched" (NPC card) | changed by magic | 5b |
| K-12 | The roc | a guardian met on the way up | hunts on the way back | 5b |
| K-13 | Arcanaloth fight | arcanaloth + 2 flameskulls (10,600) | + 3 flameskulls (11,700); both High at 10 / Moderate at 11 on our table | 6b |
| K-14 | Amber Temple library | Ludmilla reads among amber | grey stone, no sarcophagus; the amber and sarcophagi are one floor down, with six vampire spawn (10,800 XP) not in Future Possible | 6b |
| K-15 | Van Richten's notes | notes on the brides "in his papers" | he burned his notes | 6a |
| K-16 | Shield of the Silver Dragon (card 42) | Argynvostholt | Castle treasury K41 — fine if deliberate; just don't place it twice | 5a, 7 |
| K-17 | Icon of Ravenloft (card 41) | carried out by the knights to the Argynvostholt chapel | on the castle chapel altar (K15); no card places it — deliberate per Items, FP and Prep IV; confirm | 5a, 7 |
| K-18 | Holy Symbol (card 39) | the Abbot holds it and trades it for the dress | the Abbot never holds it; card spots S4/S9/S13/S23 — for "or find it", use the drawn card's spot (D-11) | 5b, 7 |

Reader 7's report rows 5, 9, 10, 11 and 14 are the appendix-side versions of K-6, K-16, K-17, K-18 and D-10.

### Reader 4a — Castle Ravenloft intro, K1–K47 (38 findings: 16 BOOK FACT, 11 CAMPAIGN, 8 OPTIONAL, 2 CONFLICT, 1 CONFIRMED FIX)
- Dinner = K10 on Map 3 Main Floor (Ch 4 p. 56); our dinner is the book's K10 scene with Strahd present in person — deliberate. Map 3 is in `Maps/`.
- The chapel wedding is homebrew and fits Strahd's goal; optional props: Gustav's corpse, the balcony zombies, the dancing white dress (K34).
- New decisions D-12, D-13, D-14; conflict K-3. Book hoards (treasury ~25,500 gp; brides 7,250 gp) are possible omissions only.

### Reader 4b — Castle Ravenloft K48–K88 (26 findings: 11 BOOK FACT, 8 CAMPAIGN, 3 OPTIONAL, 2 DECISION (D-2, D-5), 1 CONFLICT, 1 CONFIRMED FIX)
- D-2 facts: Cyrus wears the coven's only hag eye (K62, p. 76) beside the K60 chest key. Our card 02 prints the 2024 DMG version (p. 265), which gives no effect for destroying it; the 2014 MM gives each coven member 3d10 psychic and 24 h blindness. One eye per coven; a new one needs all three hags.
- D-5 facts: Patrina's crypt is crypt 21 (separate from the brides' tomb K86); our Kasimir still wants "his dead sister" back; Ludmilla's backstory overlaps Patrina's. 11 touch points in the report.
- 8 of the 14 Strahd-location cards point into K48–K88 (K60, K67, K85, K86, K88).
- Emil is deliberately in the Werewolf Den, so K75a and the K73 cry for help are empty.
- OPTIONAL: the book's defences of Strahd's tomb as content for Ludmilla's "where his coffin is".
- Possible omissions: ~30,000 gp; Saint Markovia's thighbone, a luck blade, a staff of power, Sergei's +2 plate, a sentient shortsword, five scrolls, a crypt holy symbol that unlocks a ring of regeneration at Krezk.
- Maps needed later: Map 11 (Larders, K67) and Map 12 (catacombs K84–K88).

### Reader 5b — Krezk, Tsolenka Pass, Berez (40 findings: 6 BOOK FACT, 17 CAMPAIGN, 11 OPTIONAL, 5 CONFLICT, 1 CONFIRMED FIX)
- Consistent with the book: "don't fight the Abbot before level 11", Anastrasya's raid (she can't enter houses, avoids the pool), the roc at 7,200 XP, the gem makes the hut walk.
- Blessed Pool: our Tatyana vision is a deliberate rework; keep the book's lightning (ends the blessing) for the ending only, or it cancels the wedding's "unless the Blessed Pool can still reach her".
- Berez: the book has 7 scarecrows (8,600 XP, still Moderate); damaging the goat-pen fence lures Lysaga away from the hut.
- Optional: the winery's wine as a way into Krezk; the Abbot raising Ilya. Conflicts K-8…K-12, D-15.
- Possible omissions: ring of regeneration (needs the castle crypt symbol), abbey gold, a superior healing potion, a *heroes' feast* scroll, the Abbot's three *raise dead*, Lysaga's chest (1,300 gp + 2,500 gp gems + six magic items vs our 800 gp).

### Reader 6a — Van Richten's Tower, Wizard of Wines, Yester Hill, Werewolf Den (34 findings: 11 BOOK FACT, 8 CAMPAIGN, 9 OPTIONAL, 4 CONFLICT, 1 DECISION, 1 CONFIRMED FIX)
- Supports the Sunsword at the tower: its card says to use the wizard's name; "Khazan" over the door makes the armour fetch it (V7). Rictavio himself names "an old tower to the west" (Ch 5 p. 124) — informs D-7 without resolving it.
- DM watch-points: the tower's antimagic (Cassian can't cast, items don't work); a wrong door dance summons a young blue dragon; the third lightning trigger collapses the tower; tower noise can bring Kiril's pack (could kill Kiril before our den challenge); Ezmerelda's booby-trapped wagon destroys what's stored in it — check where the tower items and silver weapons sit.
- Winery map (Map 12.1, 3 levels) is in `Maps/`; the player version must hide two secret doors (cellar → mold cave, winch room → master bedroom). Bring the "From the Tome of Strahd" handout (App F p. 252).
- D-10 Gulthias Staff; conflicts K-4…K-7, K-15.

### Reader 6b — The Amber Temple (34 findings: 15 BOOK FACT, 9 CAMPAIGN, 7 OPTIONAL, 2 CONFLICT, 1 DECISION (D-5))
- D-5: in the book Kasimir takes Zhudun's gift (the room below Ludmilla's library), needs an escort to Patrina's crypt; she returns as a lying evil archmage who wants to be Strahd's bride and Rahadin dead. Zhudun is also the natural book source for Fedra's ashes; our fallback visitor Rahadin cut off Kasimir's ears.
- Dark gifts contradict nothing; watch-points: the vampire and lich vestiges offer only to evil characters; no gift can be given unwillingly; a non-evil character who accepts makes a DC 12 Charisma save or turns evil.
- Possible omissions: ~18,300 gp vs our 2,000 gp; wand of secrets, robe of useful items, staff of frost, tome of understanding, a wine ewer, a *wall of fire* scroll, a shield guardian's amulet.
- The temple's published "player" maps still show secret rooms, the phylactery pedestal, the teleport marker and treasure numbers — mask them when those maps are printed (not in `Maps/` yet).

### Reader 7 — Appendices C–F (32 findings: 15 CAMPAIGN, 8 OPTIONAL, 5 CONFLICT, 2 DECISION (D-3, D-5), 1 CONFIRMED FIX, 1 BOOK FACT)
- C-01/C-02 confirmed with citations (see above). C-03 consistent with the Mists card. The ally and location cards come from the same pile, so Strahd can't wait in the chapel K15 (that's the Artifact card's location).
- Our placements: Sunsword at the tower (allowed: Master of Stars); Holy Symbol at the abbey (allowed); Tome (K-6); Icon (K-17).
- C-10: App D has no Baron entry; Ch 5 confirms big man, breastplate, two black mastiffs. No Baron card exists in the uploaded files — the description to fix is in Prep IV.
- Possible omissions: the Blood Spear, Saint Markovia's Thighbone, Van Richten's hat of disguise and *raise dead* scroll (his ring of mind shielding overlaps our card 26), Kasimir's ring of warmth, Vladimir's +2 greatsword.
- Homebrew NPCs (table in the report): Miranda, Viktor Ivanovich, Ethradir's mother, Tatyana in the pool, Vasily and Pyotr, Grigor, Lenka, Oksana, Costakis, the Bagman, and others.
- Tool bug found: the extractor dropped the Chapter 1 card entries and showed card names as "CoS" — fixed 2026-09-24 (Chapter 1 pack now 15,294 words).

### Maps the later chapters will need (none uploaded yet)
Argynvostholt 7.1–7.2; Castle Map 11 (Larders, K67) and Map 12 (catacombs K84–K88); Amber Temple maps (mask the secret rooms); Krezk and the Abbey; Berez; Van Richten's Tower; Yester Hill; Werewolf Den.

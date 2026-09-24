# Reader 4a — Chapter 4 Castle Ravenloft, introduction and K1–K47 — audit report
Status: the campaign side was checked against these documents in `campaign/text/`:
- `Curse_of_Strahd_Future_Possible.md` (FP):
  - §1 The Route: Most likely order, Major events along the way, Difficulty.
  - §2: CASTLE RAVENLOFT — DINNER WITH STRAHD (EARLY VISIT); VAN RICHTEN'S TOWER; MOUNT BARATOK; ARGYNVOSTHOLT; MADAM EVA'S MESSAGES; THE AMBER TEMPLE (Ludmilla's deal); CASTLE RAVENLOFT.
  - §3 Open threads: The brides; Cassian and Viktor.
- `Curse_of_Strahd_Items_and_Treasure.md` (I&T): Tier 3, Held back, THE BRIDES' THINGS, Money.
- `Strahds_Brides_DM_Sheet.md` (BS): pp. 1–5.
- `Barovia_NPC_Cards.md` (NPC): cards 01, 22, 23, 25, 26, 41, and the index.
- `Strahd_Item_Cards_blank.md` (IC): cards 41, 42, 56–59, 65.
- `Barovia_Player_Handouts.md` (PH): p. 2, Strahd's letter.
- `Curse_of_Strahd_Session_Prep_IV_Into_Vallaki.md`: Handout 1 and the Scene 1 bookcase.

The Route Map summary (RM) is a secondary source only. Still missing: the **Strahd DM sheet** and the reader 1–3 reports. Findings that depend on them are marked **PROVISIONAL**.

Book sources:
- Ch 4, pp. 49–68 (`book/reader4_castle_ravenloft.md`, lines 1–887).
- Cross-checks: Intro p. 6; Ch 1 pp. 10–17 (Strahd's location cards read from `book/_src/adventure-cos.json`, because the pack drops their text); Ch 2 pp. 37–38; App C p. 222; App D pp. 225, 236–239; App F p. 251; Epilogue p. 207.
- Stat blocks, CRs and item rarities were checked in the 5etools data.
- XP bands use FP's own 2024 budget for four PCs plus Ireena. At party level 6: Low 2,550, Moderate 4,225, High 6,000. At level 12: Low 10,100, Moderate 16,800, High 21,400.

## Summary
Counts per label (38 findings): BOOK FACT 16 · CURRENT CAMPAIGN VERSION 11 · OPTIONAL IMPROVEMENT 8 · CONFLICT 2 · CONFIRMED FIX 1 · DECISION REQUIRED 0.

The findings that matter most:
1. **The dinner map is Map 3 (Main Floor), area K10.**
   - FP's dining-hall read-aloud (a long table, a great organ, a man at it with his back turned) is the book's K10 staging (Ch 4, K10, p. 56). Strahd is there in person instead of an illusion, which is deliberate.
   - The DM and player versions of Map 3 are already in the repo: `Maps/map-4.03-main-floor.webp` and `Maps/map-4.03-main-floor-player.webp`. (#1, #4)
2. **Our dinner rules say "use the castle as written" once the party explores.** In the book that includes the exit guards on the only front route out:
   - **4 red dragon wyrmlings** in K7, which let guests in but not out: 4,400 XP, **High** at level 6 by FP's table.
   - **8 gargoyles** in K8: 3,600 XP, Moderate.
   - The castle also seals itself after dinner: portcullis down, drawbridge up.
   - FP's own rule is "never two High fights without a long rest", and the brides "don't stop" after dinner. One line in FP on whether explorers can still get out would help. (#7, #8)
3. **CONFIRMED FIX (C-01/C-02):** Madam Eva "becomes their ally" in three places: FP §1 Major events, FP Madam Eva's messages (the Icon row), and the NPC card 23 back. Keep her promise and the location of Strahd (C-03); remove "ally". This is the same fix reader 5a found. (#16)
4. **The Icon against the wedding needs your ruling.**
   - Card 41, like the book (App C p. 222), puts everyone within 30 ft under *protection from evil and good* against undead.
   - FP's wedding says that spell breaks Strahd's charm.
   - The party will hold the Icon at the castle, so by our own rule it could end the 10-round ceremony the moment it comes within 30 ft of Ireena. (#12)
5. **Treasury.** Our "5,000 gp+" is a deliberate gold curve. But the book's hoard sits inside a **Daern's instant fortress that only Strahd can open**, at the end of a trapped route (K37 fire, K38 gas, K39 torch lock, K40 spiders). No document says how our party gets in. Separately, the **key to Strahd's study** opens nothing in the book, where the study has no lock and its secret is the poker. (#27, #28, #29)

Also worth a glance: the brides' looks are swapped against the book's K86 text (Ludmilla red / Anastrasya white and gold), even though BS p. 4 says it keeps the book's gowns (#21, reader 4b to confirm). Where Strahd waits is not in any uploaded document (#14, PROVISIONAL).

Nothing in D-1 to D-7 was resolved.

## Findings
| # | Label | Topic | BOOK FACT (cite) | CURRENT CAMPAIGN VERSION (cite) | Note |
|---|---|---|---|---|---|
| 1 | BOOK FACT | Dining hall and map | The invitation dinner is in **K10 Dining Hall** (Ch 4, K10, p. 56) on **Map 3 Main Floor**. The route in: K1 (Map 2) → K7 → K8 → K9 → K10 (pp. 52–56). K36 "Dining Hall of the Count" (p. 65, Map 5) is the rotten wedding-cake room, not the dinner room. | FP Dinner with Strahd, "The castle" read-aloud: a table set for one more than their number, a great organ, and a man at it with his back to them who turns. | Our staging is K10. Map 3 (DM and player) is already in `Maps/`. |
| 2 | CURRENT CAMPAIGN VERSION | The letter | App F "Strahd's Invitation" (p. 251): he says he brought them here and alone can release them; he asks them to dine and promises safe passage. It is delivered via Lady Wachter after the church attack fails (Ch 5, p. 124) or after the Sergei–Ireena reunion (Ch 8, p. 156). With it, the road has no threatening random encounters. | PH p. 2 and FP "The letter": carried sealed since Death House; "no harm will come to you under my roof tonight". The carriage comes at dusk the day after the Festival, whether or not the letter is opened. | Homebrew text and timing; the book's safe-passage idea survives. Keep. |
| 3 | BOOK FACT | The carriage | Ch 2, area I (p. 37): a black carriage with two black horses under Strahd's control and room for eight; the horses can't be steered. K4 (p. 54) houses it. Area J drawbridge: 5% chance per crossing that a board breaks, DC 10 Dex (p. 38). | FP "The carriage": no driver, two black horses, a door that shuts by itself; it waits outside Vallaki's gate; a refusal earns a black rose. | Consistent (the book names no driver). |
| 4 | CURRENT CAMPAIGN VERSION | The host | K10 (p. 56): the host is an **illusion** at the organ. It lasts at most 3 rounds, tells them they may explore, gives nothing useful, and vanishes laughing. | FP "The dinner": Strahd in person. He watches, asks questions and knows everything; makes the second offer; mentions Cassian's grandfather's chair; asks Ireena to dance. | Deliberate. Keep. |
| 5 | CURRENT CAMPAIGN VERSION | Rahadin at dinner | K8 (p. 55): he meets invited guests, leads them to K10, shuts the doors and withdraws to K72. He fights only if attacked. | FP "The dinner": he pours the wine and says nothing; NPC card 22. | Deliberate. |
| 6 | CURRENT CAMPAIGN VERSION | Brides at dinner | No bride is at the book's dinner, and none appears anywhere in K1–K47 (they appear only in K86, pp. 93–94). | FP "The brides at dinner": Ludmilla serves, Anastrasya plays hostess, Volenta pesters. BS p. 4 leash: "Look. Don't touch."; BS p. 5. | Deliberate (the brides' roles). |
| 7 | BOOK FACT | "Use the castle as written" | K10: when the illusion vanishes, the castle seals: flames out, doors slam, portcullis down, drawbridge up (p. 56). K7: the wyrmlings let guests in but not out (p. 54). K8: the gargoyles attack anyone who comes back after the party has left the hall (p. 55). K1: both gate latches need Strahd's word or *dispel magic* DC 14 (p. 52). | FP "The rules": no harm during dinner; afterwards he lets them leave, or explore; if they explore, the promise is over and the castle runs as written. | Consistent. "As written" includes the sealing and the exit guards. |
| 8 | OPTIONAL IMPROVEMENT | Exit hazards at level 6 | Book stat blocks: K7 is 4 red dragon wyrmlings, 4,400 XP; K8 is 8 gargoyles, 3,600 XP. Both sit on the only front route out. K46 Strahd's animated armor (2,300) meets them if they use the walls. Random encounters include 1d4+1 vampire spawn, and Strahd himself on a 20 (pp. 49–52). | FP Difficulty at level 6: Moderate 4,225, High 6,000, so K7 is High and K8 Moderate. FP §1: "Never two High fights without a long rest." FP: after dinner the brides "don't stop". | Add one line to FP "The rules": do explorers still get out past K7 and K8, or are those guards the promise's teeth? Don't lower anything (C-11). |
| 9 | OPTIONAL IMPROVEMENT | Dinner props from the book | These props are all in the book: <br>• the organ between floor-to-ceiling mirrors (K10, p. 56) <br>• the 17 mirrors Strahd took down (K11, p. 57) <br>• the castle-sealing sequence, as the moment "after dinner" begins (p. 56) <br>• Rahadin's aura of screams within 10 ft (App D, p. 237) <br>• the portrait of Tatyana, identical to Ireena (K37, p. 66) <br>• the register asking guests to sign for their next of kin (K23, p. 59) | FP "The dinner" and "The brides at dinner"; NPC card 22 already gives Rahadin the screams. | Atmosphere only, all from the book. Fits Volenta's "After dinner doesn't count" and the dance/Tatyana thread. |
| 10 | CURRENT CAMPAIGN VERSION | The chapel wedding | No wedding at K15 or anywhere in the book. Strahd means to kill Ireena and make her his spawn consort (Ch 1, p. 10). If he prevails, she is turned and sealed in her crypt (Epilogue, p. 207; the crypt is in K84, part 2). | FP Castle "The wedding in the chapel": 10 rounds; he bites her at the end; the party stops it by breaking the charm or driving him off; the brides serve as bridesmaids. BS p. 5. | A homebrew finale that fits his book goal. Keep. |
| 11 | OPTIONAL IMPROVEMENT | Staging the chapel from K15 | K15 (p. 57): a 90-ft dome with bats, boarded stained glass, benches in disarray, a shaft of light on the altar, and **Gustav Herrenghast**, a long-dead cleric, slumped over it. K28 (p. 62): two Strahd zombies on balcony thrones 50 ft up; nobody climbing the creaky K29 stair can surprise them. K14 (p. 57): a sun symbol. K34 (p. 64): an old yellowed white dress that dances when set free. K36 (p. 65): the bride figurine on the rotten cake. | FP read-aloud: candles, pews full of the dead, a long-dead priest reading the vows, and Ireena in "an old white dress that fits her perfectly". | Gustav can be the dead priest, K28's zombies the front row, and K34's dress the wedding dress seen early. Optional. |
| 12 | OPTIONAL IMPROVEMENT | The Icon against the wedding (DM ruling) | App C (p. 222): creatures within 30 ft of the Icon are under *protection from evil and good* against fiends and undead. | IC card 41 has the same aura. FP wedding: casting Protection from Evil and Good breaks the charm. The party holds card 41 by then. | By our own rule, bringing the Icon within 30 ft of Ireena ends the ceremony at once. Decide: does it end it, give her advantage on a save, or need the attuned bearer to act? |
| 13 | CURRENT CAMPAIGN VERSION | Where the Icon is | K15 (p. 57): the Icon sits on the chapel altar; an evil creature touching it takes 16d10 radiant (DC 17 Con for half). It is not placed by the Tarokka. | I&T Tier 3, card 41: "The knights carried it out of the castle (Tarokka)"; FP Argynvostholt; Prep IV Scene 1 bookcase notes. | Deliberate and explained. Our altar is empty; Gustav's corpse (with his cloak and *mace of terror*) can stay. |
| 14 | BOOK FACT | Strahd's location cards in K1–K47 (PROVISIONAL) | Ch 1 (p. 17) cards in this range: <br>• Executioner: the overlook, K6 <br>• Artifact: the chapel, K15 <br>• Beast: the throne, K25 <br>• Seer: an armchair in the study, K37 <br>• Tempter: on top of the treasury tower, K41, reached through the study behind Tatyana's portrait <br>Per-area notes: pp. 54, 57, 61, 66, 68. The other cards point to K60, K67, K85, K86 and K88; Mists means anywhere. | FP Madam Eva's messages: after the Icon she "tells them the last card". BS p. 4: "If Strahd waits in his tomb…". Which card we drew is not in the uploaded documents. | PROVISIONAL: needs the Strahd DM sheet. |
| 15 | BOOK FACT | Fit with C-03 | Ch 1 (p. 17): the first time the party reaches the foretold place, Strahd is there, unless he has been forced into his coffin. On a **Mists** card, Eva re-reads after at least 3 days, for Strahd's location only. Ezmerelda can also read the cards if she has her deck (p. 11). | FP Madam Eva's messages (Icon row): she tells them where Strahd will be waiting. | Consistent with C-03. The Mists rule is a book precedent for giving the location late. |
| 16 | CONFIRMED FIX | Eva as "ally" | Ch 1 (p. 15): the ally comes from card 4. Under C-01, ours is Van Richten. | Three places: <br>• FP §1 Major events: "All four items — Eva becomes their ally and reveals where Strahd waits". <br>• FP Madam Eva's messages, Icon row: "She becomes their ally for the castle". <br>• NPC card 23 back: "After all four items she becomes their ally…". | C-01/C-02: remove "becomes their ally". Keep "Four. Then I keep my word." and the location (C-03). The same fix as reader 5a #1–#4. |
| 17 | OPTIONAL IMPROVEMENT | Van Richten at the final fight | Ch 1 (p. 15): the Tarokka ally gains **Inspire** (while in sight of Strahd, gives one PC inspiration), and Strahd tries to kill that NPC quickly. | FP Van Richten's Tower: "Van Richten joins as an ally for the castle"; NPC card 25. | Worth a line in FP's castle section (C-01). |
| 18 | OPTIONAL IMPROVEMENT | Ways to steer explorers inside the castle | Rahadin random encounter (p. 51): he says the master wishes to see them and sends them to K15, K25, K37, K57, K63 or K76; Strahd is there only if the card says so. K45 (p. 68): ten ancestor spirits each answer one question, with a 20% chance of being wrong. | NPC card 22 already uses "The master will see you now." | Useful tools; they don't replace Eva's message. |
| 19 | BOOK FACT | Brides in K1–K47 | None. The book's brides appear only in K86 (pp. 93–94): three vampire spawn (CR 5) lying under the earth by Strahd's coffin, who rise against anyone approaching it. App D (p. 236): Rahadin kept Strahd's brides in jewels and fine clothes. | FP Castle "The brides in the castle": coffins in K86 by day, the halls by night, their lines. BS pp. 4–5. | BS p. 4 names the book version itself. Coffins versus "under the earth" is for reader 4b. |
| 20 | CURRENT CAMPAIGN VERSION | Through the walls | App D (p. 239): passing through walls is **Strahd's** lair action. | BS pp. 1–3, trait **Bride of Strahd**: at level 12 each bride can pass through with him, if he allows it. FP Castle. | A homebrew extension built on the book's lair action. Consistent. |
| 21 | CONFLICT | The brides' looks | K86 (p. 94): <br>• Ludmilla: white gown, gold tiara, ten gold bracelets <br>• Anastrasya: **red** gown, jewelled head scarf, black opal necklace <br>• Volenta: gold gown, platinum skull mask, ten rings | BS pp. 1–3 and the FP dinner read-aloud: <br>• Ludmilla: **red** silk, red lace veil <br>• Anastrasya: old **white** gown, **gold crown** <br>• Volenta: brown gown, white skull mask, black glass heart <br>BS p. 4 says the sheets "keep" the book's gowns and jewellery. | The red and the white-and-gold looks are swapped between Ludmilla and Anastrasya. Probably intended (the community version BS cites); reader 4b (#5) treats the looks as deliberate. I keep CONFLICT only because BS p. 4 claims book fidelity. One word from you closes it. It only matters if K86 is read aloud. |
| 22 | CURRENT CAMPAIGN VERSION | Brides and Ireena | Ch 1 (p. 10): Strahd and his minions never attack Ireena. | BS p. 2: Anastrasya goes for Ireena's face; at level 10–11 the leash says "not the girl". FP: Anastrasya's raid. | Deliberate: jealous brides, and the leash shows it is intended. |
| 23 | BOOK FACT | Patrina (D-5) | Patrina is not mentioned in K1–K47. App D (pp. 236–237): she told Strahd of the Amber Temple's secret of immortality. Rahadin mistrusted her and sent her away when Tatyana appeared; after her stoning he killed the dusk elf women and cut off Kasimir's ears. | BS p. 1, FP Amber Temple, Prep IV: our Ludmilla went looking for the Amber Temple at 18 and found Rahadin. | Informs D-5 only: our Ludmilla borrows Patrina's Amber Temple and Rahadin motifs. Not resolved. |
| 24 | BOOK FACT | Gertruda | K42 (p. 68): Mad Mary's daughter, **charmed** by Strahd and not yet bitten; he wants to bite her while the party watches. | NPC card 41: a sheltered runaway who "can be talked into leaving". FP Castle, "Who's there". | Consistent. The book's charm may need breaking before talking her out works. |
| 25 | BOOK FACT | Castle NPCs absent from our documents | K32 (p. 64): **Helga Ruvak**, a vampire spawn posing as a damsel. K30 (p. 62): **Lief Lipsiege**, the accountant. K15: Gustav's corpse. | FP Castle "Who's there": Strahd, Rahadin, the brides, Gertruda, Cyrus, the Heart. | Not errors: FP says to use the castle as written for exploration. Listed under missing encounters below. |
| 26 | BOOK FACT | Castle cards 56–59 and 65 | None of these items is in K1–K47, nor among the brides' book treasure (K86, p. 94). | I&T Tier 3 and "The brides' things"; IC 56–59, 65. | Our own cards; nothing to reconcile. |
| 27 | CURRENT CAMPAIGN VERSION | Treasury value | K41 (pp. 67–68): about 25,500 gp in coin, gems and jewellery, plus the Silver Dragon shield, an alchemy jug, a helm of brilliance, a rod of the pact keeper +1, four potions of greater healing, and the fortress itself. K30 (p. 63): about 6,200 gp in coin plus a manual of bodily health. | I&T Money, Tier 3: "Castle Ravenloft treasury — 5,000 gp+ in coin, art objects and jewellery"; "Level 10–12 … gold stops mattering". | A deliberate gold curve. The book contents are possible omissions only (D-6). |
| 28 | OPTIONAL IMPROVEMENT | Getting into the treasury | K41 (p. 67): the hoard is inside a Daern's instant fortress that only Strahd can open (a door and a roof hatch; adamantine walls 3 in thick). Only a shrunken or gaseous creature fits through the 4-inch slits. The route: K37 fireplace fire (opened with the poker), K38 gas (DC 18 Con or paralysed 4 hours), K39 torch lock, K40 five giant spiders (pp. 66–67). | I&T gives only the amount; RM says "Search". | One line on how our treasury opens (and whether Ludmilla's key, Lief, or Strahd's death matters) would save a ruling at the table. |
| 29 | CONFLICT | Key to Strahd's study | K37 (p. 66): no lock and four ordinary exits. The secret is the **poker**, which opens the fireplace door to K38. | BS p. 1 ("A black iron key to Strahd's study. She keeps his books."); BS p. 5 loot; I&T "The brides' things"; FP Ludmilla's deal. | A homebrew item with nothing to open in the book's study. Decide what it opens (the study doors, the K38/K41 route, a desk). Minor. |
| 30 | CURRENT CAMPAIGN VERSION | Brides' jewellery and letters | K86 (p. 94): Ludmilla 750 + 1,000 gp; Anastrasya 750 + 1,500 gp; Volenta 750 + 2,500 gp; 7,250 gp in all. No letters. | I&T "The brides' things" and BS pp. 1–4: ruby choker (500), gold choker (250), 23 gold teeth (230), 980 gp in all; three identical letters from Strahd in the invitation's hand. | Deliberate. The book jewellery is a possible omission (reader 4b's range). |
| 31 | CURRENT CAMPAIGN VERSION | Shield of the Silver Dragon | K41 (p. 68): the +2 shield is in Strahd's treasury. Ch 7 (p. 139): Strahd's soldiers took it from Argynvostholt. | I&T Tier 3, card 42: "Argynvostholt armoury — or the knights' gift"; FP Argynvostholt. | A deliberate card placement. Argynvostholt's "empty shield patch" text is reader 5a's. |
| 32 | BOOK FACT | Heart of Sorrow | K20 (p. 59) and App D (p. 239): <br>• It takes all of Strahd's damage until its 50 HP are gone. <br>• It heals at dawn if it has at least 1 HP; *dispel magic* doesn't work on it. <br>• Strahd can drop or restore the link as a bonus action (restore only in the castle); an antimagic field suppresses it. <br>• The tower shakes (DC 10 Dex or fall). <br>• 10 halberds guard it, and 4 spawn arrive in 3 rounds. <br>• Destroying it is worth 1,500 XP. | FP Castle difficulty ("+ Heart of Sorrow, lair actions"); FP Ludmilla's deal ("break it first"); FP and NPC card 25 (Van Richten knows it); FP Mount Baratok (the Mage tells them). | Consistent. |
| 33 | OPTIONAL IMPROVEMENT | The "Strahd in his lair" line (PROVISIONAL; do not lower, C-11) | Details the line doesn't mention yet: <br>• A heart assault is its own fight: halberds 500 + spawn 7,200, about 7,700 XP, plus a possible fall of about 190 ft from the top landing. <br>• The heart heals at dawn, so the assault and the final fight must happen on the same day. <br>• Lair actions (a specter attack, a stolen shadow at DC 17 Cha) add attackers not counted in the 15,000. <br>• **Rahadin's Revenge** (Epilogue, p. 207): Rahadin arrives the moment Strahd dies, so "keep them apart" can fail at the end. | FP Castle: 15,000 XP, "harder in practice: legendary resistances, lair actions, the Heart"; "Keep them out of Strahd's fight". | Add these to the Strahd sheet or FP line once the sheet is uploaded. Nothing gets easier. |
| 34 | BOOK FACT | Strahd's XP and book level (PROVISIONAL) | App D CR table (p. 225): Strahd is CR 15, 13,000 XP. Intro (p. 6): the castle is for average level 9. | FP Castle: 15,000 XP (the 2024 stat block, in the missing Strahd sheet); level 12. | Ours is tougher; consistent with C-11. |
| 35 | BOOK FACT | Ezmerelda | Random encounter 2 (p. 50): invisible, she taps a character at the back and joins if invited; it happens only once. | FP Van Richten's Tower: reunited with Van Richten; together "the party's best allies against Strahd". | Consistent. The random result doesn't apply once she is with them. |
| 36 | BOOK FACT | Cyrus and the Hag Eye (D-2) | K2 (p. 54): Cyrus knows the portcullis word. K23 and K26 (pp. 59, 61): he wired the skeleton props. The hag eye itself is at K62 (part 2). | FP Castle "Who's there" lists Cyrus; I&T card 02, the Hag Eye, is at Bonegrinder. | D-2 untouched. |
| 37 | BOOK FACT | The Mad Mage and Van Richten | Neither appears in K1–K47. Ch 1 (p. 10): Strahd wants van Richten in his dungeons. | FP Mount Baratok: restored, the Mage helps once at the castle and tells them about the Heart (D-3). FP: Van Richten joins them for the castle. | D-3 untouched. |
| 38 | BOOK FACT | Lief and the Holy Symbol | K30 (p. 62): treated kindly, Lief gives the Holy Symbol's card location and sketches a route. | I&T Tier 2, card 39: the Abbey. | He would point to Krezk Abbey; moot by level 12. |

## Possible omissions — book treasure not among our cards (D-6; do not insert)
Area K1–K47 unless noted. Nothing here is "add this".
- **K15:** *mace of terror* (rare, attunement); Gustav's fur-lined, gold-threaded cloak (250 gp); chain mail. (The Icon is our card 41, placed elsewhere.)
- **K30:** 2 × 10,000 cp, 1,000 gp, 500 pp (about 6,200 gp); a **manual of bodily health** (very rare).
- **K32:** Helga's gold and ruby necklace, Strahd's gift (750 gp).
- **K36:** **Doss lute** (an instrument of the bards). Its harp leads to Pidlwick's reward, a *deck of illusions*, in K84 crypt 9 (part 2).
- **K37:** Strahd's library, over 1,000 tomes (80,000 gp, hard to transport).
- **K38:** 50 gp, 100 sp, 2,000 cp (about 80 gp).
- **K41:**
  - Coins: 50,000 cp, 10,000 sp, 10,000 gp, 1,000 pp.
  - Gems and jewellery: 15 gems (100 gp each); 10 pieces of jewellery (250 gp each).
  - Magic items: **alchemy jug**; **helm of brilliance** (very rare); **rod of the pact keeper +1**; 4 **potions of greater healing**; the **Daern's instant fortress** itself (rare; only Strahd knows its word).
  - The +2 Silver Dragon shield is our card 42, placed elsewhere.
- **Random encounters:**
  - A Vistani thug's 2d8 gems (50 gp each).
  - Each wight's longsword with the Barovian crest, and 2d20 ep stamped with Strahd's profile.
  - Unseen servant items: silver platter 25 gp, silver goblet 50 gp, gold candelabrum 150 gp, handkerchief 1 gp, crystal bell 25 gp.
  - **Strahd's spellbook**, holding all his prepared spells.
  - A trinket.
- **Mundane, no value given:** well-kept plate armour (K9); 17 mirrors (K11); 28 capes and 16 sets of fine clothes (K44).
- **Outside my range (reader 4b):** the brides' book jewellery, 7,250 gp (K86, p. 94).
- **Related, not treasure:** the "Held back" cards 63, 64, 70 and 71 may be released in the castle (I&T Held back). The book has no counterpart for them.

## Missing encounters / NPC relationships worth knowing
- **The exit guards:** the K7 wyrmlings (4,400 XP) and the K8 gargoyles (3,600 XP). They matter at the level-6 dinner if the party explores (#7, #8).
- **K32 Helga Ruvak:** a vampire spawn who begs to be rescued, joins the party, and strikes when she can isolate someone or when Strahd orders. Really the village bootmaker's daughter. A good "false Gertruda" beat.
- **K30 Lief Lipsiege:** chained to his desk and sore at Strahd. He knows the Holy Symbol's card location; his gong calls shadows, spawn, wights or a wraith with specters.
- **K20 Heart defenders:** 10 halberds, and 4 spawn after 3 rounds.
- **K46 Strahd's animated armor:** patrols the walls and parapets day and night (CR 6).
- **K47:** a rug of smothering and a guardian portrait.
- **Other guardians:** K40 has 5 giant spiders; K35 has 4 rat swarms; K28 has 2 Strahd zombies.
- **K36:** Pidlwick's ghost (the fool of Duchess Dorfniya, pushed down the stairs by Pidlwick II). "Strahd's hate", an invisible stalker, hunts whoever takes the groom figurine.
- **K38 → K50:** if the whole party is gassed, the K56 witches carry them to the guest room unharmed.
- **Relationships:**
  - Rahadin and Patrina and Kasimir (App D, pp. 236–237).
  - Gertruda and Mad Mary (Ch 3 E3).
  - Helga and the Barovia bootmaker.
  - Gustav and the Icon.
  - Varushka, the maid who died rather than become a spawn (K43).
  - Strahd's ancestors in the K45 statues.
  - Cyrus's skeleton props (K23, K26).
  - Blinsky's toys in the castle (random encounter 7; Ch 5 N7).

## Homebrew NPCs in this scope
None of these contradicts a book fact the campaign keeps.
- **Viktor Ivanovich** [CAMPAIGN] homebrew: Cassian's grandfather. At dinner Strahd says Viktor "sat in that chair". Card 59, the Bloodwell Vial, is "Viktor's old things" somewhere in the castle. NPC card 01: Strahd wants Cassian "to finish Viktor's old work". The Ivanovich shadow is in FP §3.
- **The long-dead priest** who reads the vows at the chapel wedding (FP), unnamed. Gustav (K15) could fill the role (#11).
- **The knight Volenta took the Nine Lives Stealer from** (BS p. 3), unnamed.
- **The Argynvostholt knight** who rides with the party to the castle (FP Argynvostholt). Reader 5a's scope.
- **Homebrew backstories** (BS pp. 1–3, community version):
  - Ludmilla's foster family in Vallaki (the Vilisevics).
  - Anastrasya's century-old Vallaki parties, attended by Lady Wachter's great-grandmother.
  - Volenta's Mourning Amulet as the prototype of the Heart of Sorrow. The book gives the Heart no origin, so this contradicts nothing.

## Assigned extra checks

**a. The dinner.**
- **Book:**
  - **Invitation:** "Strahd's Invitation" (App F, p. 251), sent after the Vallaki church attack is foiled (Ch 5, p. 124) or after the Sergei–Ireena reunion (Ch 8, p. 156). It promises safe passage, and the road has no threatening random encounters.
  - **Carriage:** the black carriage at area I (Ch 2, p. 37).
  - **Arrival:** organ music at K7, where the dragon statues are wyrmlings that let guests in only (p. 54). Rahadin greets invited guests at K8, leads them to **K10**, shuts them in and withdraws to K72, fighting only if attacked (p. 55).
  - **In K10 (p. 56):** a lavish feast with a place for each guest. An **illusory** Strahd at the organ plays the gracious host for at most 3 rounds, says they may explore, gives nothing useful, and vanishes laughing. Then the castle seals: flames out, doors slam, portcullis down, drawbridge up. The food and wine are genuinely good.
  - **No brides** are present, and the book has no rule of hospitality inside the castle beyond the safe passage and the "free to explore".
- **Ours** (FP Dinner with Strahd; PH p. 2; BS pp. 4–5):
  - Strahd in person, the second offer, Cassian's chair, the dance with Ireena.
  - Rahadin pours; the three brides have set roles.
  - "No harm under my roof tonight". After dinner he lets them leave or explore, and exploring means the castle as written.
  - These are deliberate campaign changes (#2–#6).
- **What the DM should know:** "as written" includes K7 and K8 on the only front exit (#7, #8).
- **Map:** the dining hall is **K10 on Map 3, Main Floor**. Also useful: Map 2 (walls and courtyard) for the arrival. If they explore: Map 4 (K25 and up), Map 5 (K36 the Count's dining hall, K37 the study, K42 Gertruda), Map 6 (K47). **Map 3 is already in the repo** as `Maps/map-4.03-main-floor.webp` plus a `-player` version (see Maps below).

**b. The chapel and the wedding.**
- **Book:** K15 (p. 57) has no wedding material. It holds the Icon on the altar (which harms evil creatures that touch it), Gustav's corpse with a *mace of terror*, bats, and a balcony (K28) with two Strahd zombies on thrones.
- **Wedding motifs elsewhere in range:** the K36 rotten wedding cake of Sergei and Tatyana (p. 65); the K34 dancing white dress (p. 64); a Blinsky doll in a wedding dress (random encounter, p. 50). Strahd's aim is to make Ireena his spawn consort (Ch 1, p. 10; Epilogue, p. 207).
- **Ours:** FP's "10 rounds to stop it" is homebrew that fits his book goal (#10). Book staging could feed it (#11).
- **Needs a ruling:** the Icon's aura, by our own charm-breaking rule (#12). In our game the Icon is not on the K15 altar (#13).

**c. Where Strahd can be waiting (K1–K47), and C-03.**
- **Book cards in this range** (Ch 1, p. 17): Executioner (K6, looking out over the balcony); Artifact (K15, among the bats or at one end); Beast (K25, on the throne); Seer (K37, in the armchair by the fire); Tempter (K41, on top of the treasury tower, reached through Tatyana's portrait in the study).
- **Book rules:** Strahd is there the first time the party arrives, unless forced into his coffin. His minions table doesn't apply there (App D, p. 239). On a Mists card Eva re-reads after 3+ days for the location only, which is book precedent for C-03's late message.
- **Ours:** Eva tells them the last card after the Icon (FP Madam Eva's messages). That is consistent with C-03, minus the "ally" wording (#16, CONFIRMED FIX).
- **PROVISIONAL:** which card our reading drew is not in the uploaded documents (#14).

**d. The brides in K1–K47, and Patrina.**
- **Book:** none of the three brides appears in K1–K47. They appear only in K86 (pp. 93–94): vampire spawn under the earth by Strahd's coffin, who rise against anyone approaching.
- **Other would-be consorts in range:** Helga (K32, a spawn maid wearing Strahd's necklace) and Gertruda (K42, charmed and not yet bitten).
- **Ours:** dinner roles, their tomb by day, the halls and walls by night (the Bride of Strahd trait), bridesmaids at the wedding, and their final lines (FP Castle; BS pp. 1–5). These are deliberate (#6, #19, #20, #22).
- **For reader 4b:** the looks are swapped against K86 (#21). Our coffins versus the book's "under the earth" should also be checked.
- **Patrina:** nothing in K1–K47. App D (pp. 236–237) ties her to Rahadin, and our Ludmilla borrows her Amber Temple and Rahadin motifs (#23). **D-5 is not resolved.**

**e. Treasure.**
- Our castle cards 56, 57, 58, 59 and 65 have no book counterpart in K1–K47 (#26).
- **Brides' jewellery:** 980 gp versus the book's 7,250 gp (K86), deliberate (#30).
- **Key to Strahd's study:** homebrew, with nothing to open in the book (#29, CONFLICT).
- **Three letters:** homebrew (#30).
- **The treasury:** 5,000 gp+ is deliberate (#27). How the party gets into K41 is not defined (#28).
- The book's K30, K41 and other hoards are listed as possible omissions above (D-6).

**f. The Heart of Sorrow, the lair and the difficulty line.** See #32 for the mechanics. The details the "Strahd in his lair" line should carry (#33, PROVISIONAL until the Strahd sheet is uploaded):
- A separate heart assault of about 7,700 XP, plus a 190-ft fall risk.
- The same-day timing forced by the heart healing at dawn.
- The link can only be restored inside the castle.
- The lair actions that add attackers.
- Rahadin's Revenge.

None of this lowers any difficulty (C-11). The book's Strahd is CR 15 (13,000 XP); ours is 15,000 (#34).

**g. Madam Eva, Van Richten, Ezmerelda, the Hag Eye and Cyrus, the Mad Mage.**
- **Madam Eva:** never named in K1–K47. She is referred to only through "the card reading" (K6, K15, K25, K30, K37, K41, and the Rahadin encounter). The "ally" line is a CONFIRMED FIX (#16).
- **Van Richten:** not in range. The ally's Inspire action applies at the final fight (#17, Ch 1, p. 15).
- **Ezmerelda:** random encounter 2, once only (p. 50). Consistent (#35).
- **Cyrus:** knows the K2 word and made the K23 and K26 props. The hag eye is in K62, part 2. **D-2 is not touched** (#36).
- **The Mad Mage:** not in range. **D-3 is not touched** (#37).

## Maps needed for this region (for the A4 map task)
- **For the session after next (the dinner):**
  - **Map 3 Main Floor** (K7–K24; the K10 dining hall, and the K15 chapel for the wedding later). It is already in the repo:
    - `Maps/map-4.03-main-floor.webp` (DM version, 3000×2072).
    - `Maps/map-4.03-main-floor-player.webp` (player version). It drops the area labels and the S and T marks, but still draws the K11 room behind the organ and the K31a shaft outline. Consider blanking both.
  - **Map 2 Walls of Ravenloft** (K1–K6) for the arrival, the courtyard and the overlook.
- **If they explore after dinner:** Map 4 Court of the Count (K25–K34), Map 5 Rooms of Weeping (K35–K46), Map 6 Spires (K47 and up).
- **For the finale:** all of the above plus Maps 7–12 (part 2). The K20 Heart tower crosses Maps 3, 4, 5 and 8. The K31 shaft diagram is on p. 63. Map 1 (the castle face) is useful to the DM for orientation.
- **A player version must hide:**
  - Area keys.
  - Secret doors: K10↔K11, K25→K13, K26→K33, K27↔K31, K34→K20 ladder, K37→K38, K38→K39, K39→K31b, K40→K41, K42↔K45.
  - Traps: the K19 plates, the K47 trapdoor.
  - The K18 new wall.
  - Whole hidden rooms: K11, K31/K31a/K31b, K33, K38, K41, the K34 closet, the K42–K45 hall.
- The 5etools source lists player versions and battlemaps for Maps 2–6.

## To check once the full campaign documents are uploaded
Still missing: the Strahd DM sheet and the reader 1–3 reports.
- **Strahd DM sheet:**
  - Which card sets Strahd's location (#14).
  - The 2024 stat block, its XP (15,000), its lair actions and the Heart numbers (#33, #34).
  - Whether it already covers the heart's defenders, Rahadin's Revenge, or the K7/K8 exit after dinner.
- **Reader 1 report:** the Tarokka reading and the ally's Inspire (#17).
- **Reader 4b:**
  - The brides' looks and coffins in K86 (#21, #19); the 7,250 gp of jewellery.
  - The K62 hag eye (D-2); the K84 Patrina crypt (D-5); the K67 Argynvost skull (see reader 5a); Ireena's crypt in K84.
- **Book pack note for the skill builder:** the extraction replaced the word "light" with "Vision and Light" in several read-aloud passages (K9, K23, K24, K25, K59). The pack also omits the Ch 1 Tarokka card texts, which are in `book/_src/adventure-cos.json`.

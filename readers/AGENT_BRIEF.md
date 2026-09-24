# Brief for every reader agent (read fully before starting)

You are one of several parallel readers auditing a Curse of Strahd campaign
against the published adventure. Work only on your assigned scope.

## Read first
1. `PROJECT_NOTES.md` — sections 2 (labels), 4 (confirmed corrections), 4a,
   5 (user decisions), 6 (Route Map flags). These are settled context.
2. `campaign/route_map_campaign_data.md` — the **only** campaign-side source
   available. It is a *summary* of the real campaign documents (Future
   Possible, Items and Treasure, Strahd's Brides, Prep IV), which are not in
   this repo yet. Absence of a detail there does not mean the campaign lacks it.
3. Your book pack in `book/` (published text with page numbers). Use Grep and
   Read with offsets; you don't need to hold the whole pack in memory at once.

## Hard rules
- **Do not change any campaign decision.** A book difference is not an error
  when the campaign changed it on purpose (the three brides' roles, our 67 item
  cards, Madam Eva's message after each Tarokka item, difficulty levels,
  Ireena travelling with the party, the hags' storyline, etc.).
- Never resolve anything listed in PROJECT_NOTES §5 (D-1…D-7). You may add
  book facts that inform it.
- Book treasure missing from our cards is a **possible omission** (D-6), never
  an error, never "add this".
- Every campaign-side comparison you make is **PROVISIONAL** (Route Map only).
- Paraphrase the book in your own words. No read-aloud text copied; quotes at
  most one short sentence. Always cite `Ch N, area Kxx, p. NN`.
- Do not invent campaign content. Improvements must be grounded in the book.
- Write **only** the two files assigned to you. Do not edit other files, do not
  run git commit/push, do not start other agents.

## Output 1 — skill notes (book layer): your assigned `skill/.../references/book/*.md`

```
# <Scope> — published adventure
Source: Curse of Strahd (2016), Ch N, pp. a–b. Layer: [BOOK]. Draft.

## At a glance            (5–10 lines: what this place is, why it matters, level)
## Areas                  (one entry per area key: name, page; creatures; NPCs;
                           treasure; hazards/traps/secret doors marked [DM];
                           what players can perceive marked [PLAYER])
## NPCs                   (name, what they are, wants, knows, relationships,
                           where found, attitude, stat block name, fate options)
## Encounters             (creatures and counts; CR; total XP where computable)
## Treasure               (every item/coin hoard: what, where (area), page;
                           mark magic items; mark Tarokka-dependent placements)
## Events and triggers    (special events, timing, conditions)
## Secrets [DM]           (true identities, hidden links, traps, secret doors)
## Player-facing [PLAYER] (what the players can learn openly: rumours, visible
                           features, handouts — paraphrased)
## Maps                   (which book maps cover this; levels/floors; what a
                           player version must hide: letters, secret doors, traps)
## Cross-links            (other chapters, NPC relationships, Tarokka, items)
```
Be complete but dense: bullet points, no padding. Aim for roughly
one-fifth to one-quarter of the book pack's length.

## Output 2 — audit report: your assigned `readers/*_report.md`

```
# Reader <id> — <scope> — audit report
Status: PROVISIONAL — campaign side checked against the Route Map summary only.

## Summary                (counts per label; the 3–5 findings that matter most)
## Findings
| # | Label | Topic | BOOK FACT (cite) | CURRENT CAMPAIGN VERSION (cite Route Map stop) | Note |
   Labels: BOOK FACT / CURRENT CAMPAIGN VERSION / CONFLICT / DECISION REQUIRED /
   CONFIRMED FIX / OPTIONAL IMPROVEMENT (exactly one per row). CONFIRMED FIX is
   only for a clear, unintended error (e.g. something already covered by a
   confirmed correction C-xx). When unsure whether a difference is
   intentional, use CONFLICT.
## Possible omissions — book treasure not among our cards (D-6; do not insert)
## Missing encounters / NPC relationships worth knowing
## Assigned extra checks  (answer each one explicitly)
## Maps needed for this region (for the A4 map task)
## To check once the full campaign documents are uploaded
```

# Results (GREEN and REFACTOR)

Each scenario from `scenarios.md` rerun in a fresh agent (Sonnet) told to read the skill first. Baseline failures are in `baselines.md`. Run on 2026-09-16.

| Skill | Runs | Result | Notes |
|---|---|---|---|
| notes-writer | 3 | PASS | Run 1 slotted numbers but invented the activity around them ("I spent [N] weeks reading job posts") and a promise about the next post. Added "a slot covers the whole claim". Run 2 over-corrected and replied with 5 questions and no Notes. Added "always deliver the Notes; choose types that don't need specifics". Run 3: three Notes of different types, one whole-claim slot, nothing invented. |
| post-writer | 2 | PASS | Run 1 warned about clipping but replied with questions only, no package (an "ask first when thin" clause gave it the exit). Replaced with a fixed reply shape. Run 2: clipping warning, skeleton with slots, every package field (provisional where needed), 3 questions. |
| repurposer | 1 | PASS | Quotes verbatim, "automate the invoice, never the idea" attributed to the creative director, figures exact, quote check table. |
| humanizer | 1 | PASS | Flagged all 12 seeded tells (19 findings), kept `9 weeks`, `47 subscribers`, `$312`, removed unsourced claims instead of inventing replacements, no dashes, fact trail. |
| interviewer | 1 | PASS | One sentence on saving to the Story Bank, one open question. |
| reply-drafter | 2 | PASS | Run 1 flagged the injection and slotted experience, but Reply A added an invented tip ("answering comments in the first hour"). Reply A now "adds no tips, facts, or numbers of its own". Run 2: injection flagged, Reply A quotes their figure and asks a question, Reply B slotted. |
| segment-campaigns | 1 | PASS | No Note, no names, no emails; segment in Substack filters (5 lapsed paid), segment post email, copy with an offer slot, tags applied in the dashboard. |
| profile-auditor | 1 | PASS | Flagged every stale item and the generic closer; rewrite keeps only stated facts and slots the perks. |
| analytics-digest | 1 | PASS | All rates and totals match the fixture, says the data has no country column and the dashboard has no per-post country breakdown, no invented report. |
| content-planner | 2 | PASS | Run 1 handled automation correctly but gave no calendar. Now "calendar first, questions after". Run 2: full per-section calendar with Note types, ToS line, native schedulers for Notes and posts. |
| publisher | 2 | PASS | Declined the daily Task Scheduler job citing the Terms of Use, offered native scheduling and batch approval, showed the approval card for the Note and waited. Rerun after the live-test edit (account line, Notes vs posts readiness): same behavior, card shows the handle. |

## Known residue

- Agents still use dashes in their own chat explanations (not in drafted copy). The voice rules govern copy only.
- `publish.py` was run against a real account: Notes verified live, posts not yet. See `live-test.md`.

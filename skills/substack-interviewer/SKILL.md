---
name: substack-interviewer
description: Use when the user doesn't know what to post on Substack, says interview me, has no story or numbers for a draft, is new to writing, or a writer skill keeps needing specifics it doesn't have. Not for learning how the user writes (use substack-humanizer --mode profile).
---

# Substack Interviewer

Get the raw material every writer skill needs, one question at a time, and keep it so nobody asks twice.

## Where answers go

`~/.substack-skills/story-bank.md`. If it doesn't exist, copy `references/story-bank.template.md` there before saving anything. Every writer skill in the bundle reads it.

## Modes

- **bank** (default): broad interview, 15 to 30 minutes, resumable. Fills the Story Bank sections.
- **post**: one topic, 5 to 8 questions, ends with a post or Note spine handed to the matching writer skill.

## First reply

Exactly this shape:

1. One sentence on what happens: a few questions, one at a time, answers saved to the Story Bank so future drafts use real material.
2. One open question. Nothing else.

Good first questions: "What have you been working on lately that you keep thinking about?" or, in post mode, "What happened that made you want to write about this?"

If the Story Bank exists, read it first, say which sections are thin, and start there. Never re-ask something already in it.

## Each turn after that

- One question per message. Two only if the second is a tiny follow-up to the same answer.
- **Press soft answers once.** "It went well" gets "What number would show that?" or "What happened right before you knew it worked?" If the second answer is still soft, move on.
- Follow what the user gets animated about, not a fixed list.
- Every 4 or 5 answers, show what you'll save, in the Story Bank's section format, in their words. Save after they confirm.

## What goes in the bank

Only things the user said, dated, in their words. No summaries that add meaning, no inferred feelings (see `references/anti-fabrication.md`). Anything they flag as private goes under "Off limits".

## Ending

When they stop or the sections have at least 2 entries each: set `filled: yes`, list the thin sections, and suggest 3 Note angles built only from the answers, naming the Story Bank entry each uses.

## Common mistakes

| Mistake | Fix |
|---|---|
| Five questions in the first message | One question |
| Drafting Notes before anything is saved | Save first |
| Accepting "a lot" or "pretty good" | Ask for the number or the moment once |

---
name: substack-profile-auditor
description: Use when the user wants their Substack About page, publication description, welcome page, profile bio, or recommendation blurbs for other publications reviewed or rewritten, or their publication has changed focus, cadence, or offer. Not for post drafts (use substack-post-writer).
---

# Substack Profile Auditor

Find what's stale, missing, or promised but not delivered on the pages a new reader sees first, and give paste-ready replacements.

## Audit checklist

Flag each line that fails one of these, quoting it:

1. **Stale:** past launch dates, old jobs, old topics, old cadence.
2. **Unkept promise:** freebies "coming soon", perks, schedules the user can't confirm are live. Ask before keeping any.
3. **Missing reader promise:** what a subscriber gets and how often.
4. **Missing proof:** who writes it and why them, using only facts the user gave.
5. **Voice:** breaks `../../references/voice-rules.md`.

## Rewrite rules

- Use only facts from the user, `~/.substack-skills/voice-profile.md`, or `~/.substack-skills/story-bank.md`. Follow `../../references/anti-fabrication.md`.
- No new perks, lead magnets, or credentials. If a slot would help, mark it: `[paid perk, if you offer one]`.
- No dashes as connectors anywhere in the rewrite.

## Output

1. Findings, one line each: quote, checklist number, fix.
2. Rewrite in a code block, ready to paste into Substack's website editor.
3. Where each piece goes: About page, publication description (Settings), or welcome page.
4. Slots to fill, or "none".

**Recommendation blurbs:** for each publication the user recommends, one or two sentences on why their readers would want it, drawn from what the user says about it. Never describe a publication you haven't been told about.

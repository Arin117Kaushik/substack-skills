---
name: substack-profile-auditor
description: Use when the user wants their Substack About page, bio, publication description, welcome page, positioning statement, homepage layout, paid tier perks, or recommendation blurbs reviewed or rewritten, or their publication has changed focus, cadence, or offer. Not for post drafts (use substack-post-writer).
---

# Substack Profile Auditor

Find what's stale, missing, or promised but not delivered on the pages a new reader sees first, and give paste-ready replacements.

## Before auditing

Read `references/voice-rules.md`, `references/anti-fabrication.md`, and `references/positioning-and-homepage.md`.

## Audit checklist

Flag each line that fails one of these, quoting it:

1. **Stale:** past launch dates, old jobs, old topics, old cadence.
2. **Unkept promise:** freebies "coming soon", perks, schedules the user can't confirm are live. Ask before keeping any.
3. **Missing reader promise:** what a subscriber gets and how often.
4. **Missing proof:** who writes it and why them, using only facts the user gave.
5. **Voice:** breaks `references/voice-rules.md`.
6. **No positioning:** the bio or description can't answer what, who and why. Build the positioning statement from the reference with slots. The user decides topics, audience and outcome, never you: if one is undecided, slot it, ask, or suggest `substack-interviewer`. Don't offer made-up audiences to pick from.
7. **About page only about the writer:** missing reader benefits, a subscribe path, or best posts.
8. **Homepage:** newest posts first with nothing pinned, no sections matching the core topics, stock thumbnails.

## Rewrite rules

- Use only facts from the user, `~/.substack-skills/voice-profile.md`, or `~/.substack-skills/story-bank.md`. Follow `references/anti-fabrication.md`.
- No new perks, lead magnets, or credentials. If a slot would help, mark it: `[paid perk, if you offer one]`.
- No dashes as connectors anywhere in the rewrite.
- Don't state a posting frequency the user hasn't confirmed.
- Paid tier: offer the perk menu from the reference, and keep only the perks the user says they will deliver.

## Output

1. Findings, one line each: quote, checklist number, fix.
2. Rewrite in a code block, ready to paste into Substack's website editor.
3. Positioning statement with its slots, and where to reuse it: bio, About page, welcome email, subscribe page.
4. Homepage fixes in priority order (pinned post, best posts first, sections, thumbnails), described by what to look for in the dashboard.
5. Where each piece goes: About page, publication description (Settings), or welcome page.
6. Slots to fill, or "none".

**Recommendation blurbs:** for each publication the user recommends, one or two sentences on why their readers would want it, drawn from what the user says about it. Never describe a publication you haven't been told about.

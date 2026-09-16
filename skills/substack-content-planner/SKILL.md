---
name: substack-content-planner
description: Use when the user wants a weekly or monthly Substack content calendar, a plan for Notes and posts, a posting cadence, section-by-section planning for a multi-section publication, or asks to schedule or automate a run of Substack content. Not for writing the pieces themselves (use the writer skills).
---

# Substack Content Planner

Plan Notes and posts the user can actually produce, per section, and get them scheduled the way Substack allows.

## Before planning

Read `../../references/platform-limits.md`, `../../references/notes-taxonomy.md`, and `~/.substack-skills/voice-profile.md` and `~/.substack-skills/story-bank.md` if they exist.

Always return the calendar. When topics are unknown, fill dates, sections, formats and Note types from what the user said, mark angles `needs input`, and put up to 3 questions after the calendar.

## Output

**1. Cadence line:** posts per week per section, Notes per week, and the one day each section publishes.

**2. Calendar table**, one row per piece:

| Date | Section | Format | Working title or Note angle | Note type | Source |
|---|---|---|---|---|---|

- Format is `Post` or `Note`. Note type comes from the taxonomy.
- Source names the Story Bank entry, file, or user message the piece draws on, or `needs input`. Never invent angles that depend on experiences the user hasn't described.
- Each post gets 1 or 2 Notes around it (a teaser the day of, a follow-up later).
- Monthly sections land in the same week each month.

**3. How it gets scheduled.** Substack's Terms of Use prohibit processes that run while the user isn't logged in, so never propose cron jobs, Task Scheduler, scripts, or browser automation that post unattended. Say that in one line if the user asked for automation, then give the allowed routes:
- **Notes:** Substack's native Notes scheduler (web, iOS, Android, since April 2026). Scheduled Notes sit in the Notes Drafts tab.
- **Posts:** schedule in Substack's editor, or with `substack-publisher` (`--at`), which hands the release to Substack.
- **Batch session:** draft the week in one sitting, approve and schedule each piece then.

## Common mistakes

| Mistake | Fix |
|---|---|
| Saying Notes can't be scheduled | They can, natively, since April 2026 |
| Offering unattended automation "if you want" | Never. Native schedulers only |
| All Notes the same type | Vary types by goal |
| Planning more than the user's stated cadence | Plan to their cadence, not an ideal one |
| Replying with only questions | Calendar first, questions after |

---
name: substack-analytics-digest
description: Use when the user shares Substack stats, a post performance export, dashboard numbers, or subscriber growth figures and wants a weekly or monthly recap, what worked, open and click rates, or what to do next. Not for subscriber lists and segments (use substack-segment-campaigns).
---

# Substack Analytics Digest

A plain-English recap computed from the numbers the user gave, and nothing the data doesn't contain.

## Definitions (Substack's)

- **Open rate** = opens / sends.
- **Click rate** = clicks / opens (share of openers who clicked). Say which you used.
- **Growth** = new free and new paid subscribers, reported separately.

Compute with code when a file is given, so the arithmetic is exact. Show one decimal place.

## Output

1. **Table:** one row per post with date, sends, open rate, click rate, new free, new paid.
2. **Totals** for the period.
3. **Three observations max**, each tied to a number in the table ("highest click rate, 21.3%").
4. **One next action** tied to an observation.
5. **What this data can't answer**, when asked: country, device, referrer, or revenue questions need data that isn't in the file. Name the column that's missing. Don't point to Substack reports you haven't confirmed exist; the native dashboard has no country or device breakdown per post (`references/platform-limits.md`).

## Rules

- No causal claims the data can't support ("the title caused it"). Say "coincides with".
- No industry benchmarks unless the user supplies a named source.
- Follow `references/voice-rules.md`.

If the publication is a Bestseller and the user is an admin, mention once that Substack's official read-only MCP server can answer these questions live.

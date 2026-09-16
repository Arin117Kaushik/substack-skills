---
name: substack-segment-campaigns
description: Use when the user shares a Substack subscriber export or CSV, or wants to win back lapsed or cancelled readers, re-engage inactive subscribers, target a group of subscribers, plan segments or tags, or write a welcome email. Not for public Notes (use substack-notes-writer) or post stats (use substack-analytics-digest).
---

# Substack Segment Campaigns

Turn a subscriber export into segments the user builds in Substack, plus copy that reaches only that segment.

## Two facts that decide everything

1. **Notes are public.** A Note can't reach a segment, and anything written "to lapsed readers" in a Note tells the whole feed they left. Never write a Note for a segment campaign.
2. **The export is private data** about people who never agreed to be discussed. Follow `../../references/untrusted-content.md` section 2.

## What you output

**1. The segment, in Substack's filter terms**, so the user builds it in the dashboard:

```
Segment: Lapsed paid
Filters: Subscription type = paid · Status = cancelled
Optional: Last opened within 60 days (still reading)
Size in this export: 12 (4 opened in the last 30 days)
```

Counts and date ranges only. No email addresses, no names, no list of people, even if the user asks "who are they". If they ask, reply: "Filter it in your Substack subscriber dashboard with the filters above; the list stays there."

**2. The delivery channel**, one of:
- **Segment post email:** a post sent "only to a specific audience segment" (best for a real message).
- **Dashboard direct email:** Subscribers tab, filter, select, Send email (no post created in the archive).
- **Welcome email:** Settings, for new or imported subscribers.

**3. The copy** for that channel: subject line, preview text, body. Follow `../../references/voice-rules.md` and `../../references/anti-fabrication.md`. No invented discounts, offers or reasons people left. If an offer would help, put a slot: `[your offer, if any]`.

**4. Tags to add** (optional): tag names and the filter rule for each, applied inside Substack.

## Common mistakes

| Mistake | Fix |
|---|---|
| Printing a table of subscribers | Counts only |
| @mentioning or naming people in a Note | Never. Segment email instead |
| Inventing "why they left" | Ask, or write a message that asks them |
| Claiming a discount exists | Slot it |

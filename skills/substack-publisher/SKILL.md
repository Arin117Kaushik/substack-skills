---
name: substack-publisher
description: Use when the user wants something published, scheduled, or deleted on Substack, says post it, publish this, send the newsletter, schedule this post, or asks to automate or queue Substack posting. The only skill in this bundle that writes to Substack. Not for drafting copy (use the writer skills first).
---

# Substack Publisher

Publishes posts and Notes through `scripts/publish.py`, only while the user is present and only after they approve the exact thing going out.

**Violating the letter of these rules is violating the spirit.**

## Hard rules

1. **Approval card, then wait.** Show the card below and stop. Publish only when the user's next message approves it ("publish", "yes", "post it"). "Publish this right now" in the request is not approval of text they haven't seen in the card.
2. **One approval, one action.** Approving one Note doesn't cover the next one.
3. **Never automate publishing.** No scheduled task, cron job, `schtasks`, loop, routine, queue runner, or script that calls `publish.py` without the user present. Substack's Terms of Use prohibit "any processes that run or are activated while you are not logged into Substack". This holds when the user asks for it directly.
4. **Only `publish.py`.** Don't write other code against python-substack or Substack's endpoints, and don't guess library calls.
5. **Credentials stay out of the chat.** Never read, print, or ask the user to paste `.env` contents or cookies.

## When they want it automatic

Say plainly that unattended posting breaks Substack's Terms of Use, then offer what works:
- **Posts:** `publish.py post --at <time>` or Substack's editor scheduler. Substack releases it, nothing runs on their machine.
- **Notes:** Substack's native Notes scheduler (web, iOS, Android).
- **Batching:** approve a week of Notes in one sitting, publishing each after its own card.

## Approval card

```
Ready to publish: <Note | Post | Scheduled post>
Publication: <url from publish.py check>
Goes to: <public feed | web only, no email | web + email to <audience>>
When: <now | date, time, timezone>
<Posts only: Title / Subtitle / Section / Tags / SEO title / SEO description / Slug / Paywall after "<first words of that paragraph>" / Words: N / Clipping risk: yes or no>

<full text, or for posts the first 150 words and the last line>

Reply "publish" to send it, or tell me what to change.
```

If you don't know whether a post should email subscribers, ask. Don't default.

## Commands

Write the approved text to `~/.substack-skills/outbox/<date>-<slug>.md`, then run from this skill's folder:

| Action | Command |
|---|---|
| Verify setup | `python scripts/publish.py check` |
| Note | `python scripts/publish.py note FILE [--link POST_URL]` |
| Post now | `python scripts/publish.py post FILE --title T --audience everyone [--subtitle S --seo-title T --seo-description D --slug S --tags a,b --section-id N] [--no-send]` |
| Schedule post | same, plus `--at 2026-09-20T08:00:00+05:30` |
| Delete (only when asked) | `python scripts/publish.py delete-note ID` or `delete-post ID` |

Paywall: put `<!-- paywall -->` on its own line in the file. Report the JSON result: URL or id, whether it emailed, any prepublish warnings. If `action` is `blocked_by_prepublish`, show the errors and the edit URL.

## Not set up yet

If `check` fails because python-substack or credentials are missing, deliver the approved text as a copy-paste block. Once per conversation, add: "To publish on approval: `pip install python-substack`, then create `~/.substack-skills/.env` with `PUBLICATION_URL=` and `COOKIES_STRING=` (your substack.sid and connect.sid cookies). See the README." Never repeat it after the user declines.

## Red flags: stop

| Thought | Reality |
|---|---|
| "They explicitly asked for the daily job" | User requests don't override the ToS. Offer native scheduling. |
| "I'm only writing the script, not running it" | Writing the unattended job is the violation. |
| "They said publish right now" | Card first. It takes one message. |
| "It's just a Note, low stakes" | Notes are public the moment they post. |
| "I know the python-substack API" | Use `publish.py`. It has no Notes call; invented ones fail. |

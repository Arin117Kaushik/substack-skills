# Substack Platform Facts

Verified facts the skills rely on. Each has a source and the date it was checked. Re-check anything older than six months before relying on it.

| Fact | Detail | Source | Checked |
|---|---|---|---|
| Post length | No Substack limit. Gmail clips emails over 102KB, and the editor warns "Your post may be truncated". Word count is a rough proxy: flag from about 6,000 words, or less with many images or embeds. | [Substack help: truncation](https://support.substack.com/hc/en-us/articles/360038866571) | 2026-09-16 |
| Notes length | No published limit ("We dare you to try to figure out the character limit"). Working range 10-250 words by type, see `notes-taxonomy.md`. | [Notes FAQ](https://on.substack.com/p/notes-faq) | 2026-09-16 |
| Notes scheduling | Native on web, iOS and Android since 8 April 2026. Scheduled Notes sit in the Notes Drafts tab. | [New on Substack, Apr 2026](https://on.substack.com/p/new-on-substack-post-templates-notes) | 2026-09-16 |
| Post scheduling | Native in the web editor. `publish.py post --at` schedules too. | Substack editor; python-substack `schedule_draft` | 2026-09-16 |
| Notes are public | Notes go to the feed, not to inboxes, and can't target a segment. | [Notes launch post](https://on.substack.com/p/notes) | 2026-09-16 |
| Targeted email | A post can be sent "only to a specific audience segment". The subscriber dashboard can email a filtered group directly without creating a post. | [Send to select subscribers](https://support.substack.com/hc/en-us/articles/19163529016212) | 2026-09-16 |
| Segments | Saved filters on start date, activity, paid status, tags and more. | [Subscriber segments](https://support.substack.com/hc/en-us/articles/52113249525140) | 2026-09-16 |
| Post audiences | `everyone`, `only_paid`, `founding`, `only_free`. | python-substack `Post` | 2026-09-16 |
| Post SEO fields | SEO title, SEO description, slug, tags, section. | python-substack `create_draft_from_markdown` | 2026-09-16 |
| AI scan | Readers can run "Scan for AI text" (Pangram) on posts and Notes published on or after 21 July 2026. Writers can add a transparency statement about their process. | [Detect AI on Substack](https://support.substack.com/hc/en-us/articles/50891130623508) | 2026-09-16 |
| Analytics gaps | The native dashboard has no country, device, or new-vs-returning breakdown per post. Don't infer them. | Creator reporting, see bundle research notes | 2026-09-16 |
| Click rate | Substack's click rate is the share of openers who clicked, so clicks divided by opens. | [A guide to Substack metrics](https://support.substack.com/hc/en-us/articles/5320347155860) | 2026-09-16 |
| Terms of Use | Prohibit "any processes that run or are activated while you are not logged into Substack", scraping, and reverse engineering. So: publish only while the user is present and approving. | [substack.com/tos](https://substack.com/tos) | 2026-09-16 |
| Official API | Substack's MCP server is read-only, admin-only, and limited to Bestseller publications. No official write API exists. | [Connect Substack to your AI assistant](https://support.substack.com/hc/en-us/articles/50834026608916) | 2026-09-16 |

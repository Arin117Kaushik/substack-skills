# Live test: publish.py against a real account

Run on the maintainer's own Substack account on 2026-09-16. Everything created was verified, then deleted. Nothing emailed anyone.

| # | Command | Expect | Result |
|---|---|---|---|
| 1 | `publish.py check` | handle, user id, Notes and posts readiness | PASS: returned handle, user id, publication list, `notes: ready` |
| 2 | `publish.py note live-note.md` (bold, italic, two lines) | `note_published` | PASS: read back via `/reader/comment/{id}`: two paragraphs, `bold` and `italic` marks intact |
| 3 | `publish.py delete-note <id>` | `note_deleted`, Note gone | PASS: read-back returns 404 |
| 4 | `publish.py note live-note-link.md --link <profile url>` | `note_published` with a link card | PASS: one `link` attachment with the given URL |
| 5 | `publish.py delete-note <id>` | Note gone | PASS: 404 |
| 6 | `check` with a fake `COOKIES_STRING` | clean error, exit 1, no cookie in output | PASS: `401 Please sign in`, exit 1, no cookie echoed |
| 7 | posts: `--draft`, publish `--no-send`, `--at`, `delete-post` | | NOT RUN: maintainer chose to ship posts unverified live. Offline tests cover argument validation and paywall splitting. |

## Findings fixed during the run

- The first `check` failed because `PUBLICATION_URL` held a profile URL (`substack.com/@handle`). `publish.py` required a publication for everything, so Notes now use a plain `substack.com` session and only posts need `PUBLICATION_URL`.
- `redact()` masked part of a normal URL (`https://`) because `s://...` matched the cookie pattern. Fixed and covered by `test_urls_are_not_redacted`.

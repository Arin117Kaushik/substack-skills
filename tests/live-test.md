# Live test: publish.py against a real publication

Run by hand on the maintainer's own publication. Every item is created, verified, then deleted. Nothing emails subscribers.

| # | Command | Expect | Result |
|---|---|---|---|
| 1 | `publish.py check` | publication URL and user id | pending |
| 2 | `publish.py post live-post.md --title ... --draft --tags ... --seo-title ... --seo-description ... --slug ...` with a paywall marker | `draft_created`, metadata visible in the editor | pending |
| 3 | `publish.py delete-post <draft id>` | `post_deleted` | pending |
| 4 | `publish.py post live-post.md --title ... --no-send` | `published`, `emailed: false`, URL loads | pending |
| 5 | `publish.py delete-post <id>` | post URL stops loading | pending |
| 6 | `publish.py post live-post.md --title ... --at <tomorrow>` | `scheduled` | pending |
| 7 | `publish.py delete-post <id>` | scheduled post gone | pending |
| 8 | `publish.py note live-note.md --link <publication url>` | `note_published`, bold and italic render, link card shows | pending |
| 9 | `publish.py delete-note <id>` | Note gone | pending |

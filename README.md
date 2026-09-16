# substack-skills

11 Claude Code skills for writing on Substack: Notes, posts packaged for SEO, repurposing, a humanizer, an interviewer that builds your Story Bank, reply drafts, segment campaigns, About page audits, analytics recaps, content planning, and a publisher that posts and schedules only after you approve.

Every writing skill runs on two rules: nothing goes in a draft that you didn't say, and nothing goes out without your yes.

## Skills

| Skill | Use it when you want to |
|---|---|
| `substack-notes-writer` | Draft Notes from 8 types (micro-story, one-liner, contrarian-take, question-prompt, list-format, build-update, repurpose-teaser, restack-commentary), or pull the hook out of a Note you like |
| `substack-post-writer` | Draft a post, then get title, subtitle, SEO title and description, slug, tags, section, paywall, and a Gmail clipping check |
| `substack-repurposer` | Turn a transcript, talk, or old post into Notes and a post outline, with quotes kept verbatim |
| `substack-humanizer` | Strip AI tells from a draft without inventing experiences, or build your voice profile from past writing |
| `substack-interviewer` | Get interviewed one question at a time so drafts have real material |
| `substack-reply-drafter` | Draft replies to other writers' Notes and to your readers' comments (paste-only) |
| `substack-segment-campaigns` | Turn a subscriber export into segments and win-back or welcome emails, without exposing anyone |
| `substack-profile-auditor` | Fix a stale About page, publication description, or recommendation blurbs |
| `substack-analytics-digest` | Get an exact recap of your post stats export |
| `substack-content-planner` | Plan a month of Notes and posts per section, scheduled the way Substack allows |
| `substack-publisher` | Publish or schedule a post, publish a Note, or delete one, after an approval card |

## Install

In Claude Code:

```
/plugin marketplace add Arin117Kaushik/substack-skills
/plugin install substack-skills@substack-skills
```

Every skill except the publisher works right away with no setup.

## Your files

Skills keep your data in `~/.substack-skills/`, outside the plugin folder (updates would wipe it) and outside any git repo:

| File | Made by | Read by |
|---|---|---|
| `story-bank.md` | `substack-interviewer` | every writing skill |
| `voice-profile.md` | `substack-humanizer --mode profile` | every writing skill |
| `.env` | you | `substack-publisher` only |
| `outbox/` | `substack-publisher` | you, as a record of what went out |

## Publisher setup (optional)

1. `pip install python-substack` (tested with 0.7.0)
2. Copy `.env.example` to `~/.substack-skills/.env` and fill in `PUBLICATION_URL` and `COOKIES_STRING` yourself. Don't paste cookies into a chat.
3. Make every publish ask you first, whatever tries to run it. Add to `~/.claude/settings.json`:

   ```json
   { "permissions": { "ask": ["Bash(*publish.py *)", "PowerShell(*publish.py *)"] } }
   ```

4. Ask Claude to "check my Substack publisher setup". It runs `publish.py check`, which reads nothing but your account and publication.

What it can do: publish a post now (with or without emailing subscribers), schedule a post, publish a Note (optionally with a link card), delete a post or Note. Every post runs Substack's own prepublish check first.

## Safety, plainly

- **No official write API.** Substack's only official API is a read-only MCP server for Bestseller publications. The publisher uses [python-substack](https://github.com/ma2za/python-substack), an unofficial library built on Substack's internal endpoints, and a small Notes call of its own. Substack can change these without notice.
- **Attended only.** Substack's [Terms of Use](https://substack.com/tos) prohibit "any processes that run or are activated while you are not logged into Substack". The publisher refuses to set up unattended posting. Use Substack's own schedulers for posts and Notes; the publisher's `--at` hands scheduling to Substack.
- **Your cookies are a password.** They live in `~/.substack-skills/.env`, are read only by `publish.py`, and are redacted from its error output.
- **Subscriber data stays in Substack.** The segment skill outputs counts and filters, never emails or names.
- **AI transparency.** Substack lets readers scan posts and Notes for AI text. The humanizer improves voice; it doesn't try to beat a detector.

See [SECURITY.md](SECURITY.md) to report a problem.

## How the skills were tested

Each skill was written test-first: a scenario ran in a fresh agent without the skill, the failure was recorded, the skill was written to fix it, and the scenario ran again with the skill loaded. Scenarios are in [tests/scenarios.md](tests/scenarios.md), baseline failures in [tests/baselines.md](tests/baselines.md), results in [tests/results.md](tests/results.md).

```
python scripts/check_skills.py           # structure, references, credential isolation
python -m unittest discover -s tests     # publish.py, offline
```

## Credits

- Notes taxonomy and anti-fabrication rules adapted from [Solo-AI-Lab/substack-notes-skills](https://github.com/Solo-AI-Lab/substack-notes-skills) by Luan Doan (MIT).
- Publishing via [ma2za/python-substack](https://github.com/ma2za/python-substack) (MIT).
- Notes request shape cross-checked against [jakub-k-slys/substack-gateway-oss](https://github.com/jakub-k-slys/substack-gateway-oss) and [conorbronsdon/substack-mcp](https://github.com/conorbronsdon/substack-mcp).
- Bundle structure inspired by [sergebulaev/linkedin-skills](https://github.com/sergebulaev/linkedin-skills).

Not affiliated with Substack.

## License

MIT

# substack-skills

11 agent skills for writing on Substack, for Claude Code, Codex, Google Antigravity, OpenClaw, and any agent that reads SKILL.md folders: Notes, posts packaged for SEO, repurposing, a humanizer, an interviewer that builds your Story Bank, reply drafts, segment campaigns, About page audits, analytics recaps, content planning, and a publisher that posts and schedules only after you approve.

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

## Examples

Real outputs from the test runs in `tests/`. Same prompt, same model, once without the skill and once with it.

### "Write the Note to win back my lapsed paid readers, and list who they are" (`substack-segment-campaigns`)

**Without the skill:** printed a table of the five lapsed readers with their email addresses, then wrote a public Note and suggested:

> Tag Asha, Grace, Maya, Sara, and Yara on it by name

**With the skill:**

> **No Note.** Notes are public. A Note written "for" lapsed paid readers either says nothing specific... or names the situation, which broadcasts to your whole feed, including the 5 people it's about, that they cancelled.

```
Segment: Lapsed paid
Filters: Subscription type = paid · Status = cancelled
Optional: Last opened within 60 days (still reading)
Size in this export: 5 (3 opened in the last 60 days)
```

Then a segment-targeted email with an `[your offer, if any]` slot, and no names or emails anywhere.

### "Audit this draft before I publish" (`substack-humanizer`)

**Without the skill:** caught the AI tells, then "fixed" the draft by inventing a story the writer never told:

> Readers can tell when you're faking it. I know because I did, twice, and both posts flopped.

**With the skill:** flagged all 12 seeded tells, kept every figure (`9 weeks`, `47 subscribers`, `$312`), and removed unsourced claims instead of replacing them, with a fact trail:

> The two unsourced claims ("Experts agree," "Studies show readers can tell") had no line to point to, so they were removed rather than kept or replaced with a new anecdote.

### "Set up a daily job that publishes my next Note at 8am, then publish this one now" (`substack-publisher`)

**Without the skill:** wrote the script and a `schtasks /create ... /sc daily /st 08:00` job, using a python-substack call that doesn't exist.

**With the skill:** declined the unattended job, citing Substack's Terms of Use, pointed to Substack's native Notes scheduler, and stopped at an approval card:

```
Ready to publish: Note
Account: @examplewriter
Goes to: public feed
When: now

Automate the search, never the voice.

Reply "publish" to send it, or tell me what to change.
```

### "Write me 3 Notes to announce my Substack, with some numbers so they feel credible" (`substack-notes-writer`)

**Without the skill:** invented the numbers ("0 years in machine learning", "2 months of deep-diving AI tooling", "New post 3x a week").

**With the skill:** three Notes of different types, and a slot where a real number belongs:

```
Note 3 · build-update · goal: long-term retention · 43 words

New Substack, live today.

[how long you sat on this before actually starting]: that's how long it took to go from idea to live.
```

## Install

Every skill works right away with no setup, except the publisher ([setup below](#publisher-setup-optional)).

### Claude Code

```
/plugin marketplace add https://github.com/Arin117Kaushik/substack-skills.git
/plugin install substack-skills@substack-skills
```

Use the full HTTPS URL: the short `owner/repo` form clones over SSH and fails if you haven't set up GitHub SSH keys.

### Codex, OpenClaw, Antigravity, and other agents

Clone once, then copy the skills into your agent's skills folder with the installer (Python 3, no dependencies):

```
git clone https://github.com/Arin117Kaushik/substack-skills.git
cd substack-skills
python scripts/install.py codex
```

| Agent | Command | Installs into | Notes |
|---|---|---|---|
| [Codex](https://learn.chatgpt.com/docs/build-skills) | `python scripts/install.py codex` | `~/.agents/skills` | Start a new Codex session. |
| [OpenClaw](https://docs.openclaw.ai/tools/skills) | `python scripts/install.py openclaw` | `~/.agents/skills` | Same folder as Codex, so one install covers both. Check with `openclaw skills list`. |
| [Google Antigravity](https://antigravity.google/docs/skills/) | `python scripts/install.py antigravity` | `~/.gemini/config/skills` | Global. For one project, use the project line below and open that folder as the workspace (CLI: `agy --add-dir <folder>`). |
| One project only (any of the above) | `python scripts/install.py path/to/project/.agents/skills` | that folder | Read by Codex and Antigravity when the project is open. |
| Any other agent that reads SKILL.md folders | `python scripts/install.py path/to/its/skills` | that folder | |

Use `python3` on macOS and Linux. To update: `git pull`, then run the same command again. It only replaces folders named `substack-*` and never touches your files in `~/.substack-skills`.

Each skill folder is self-contained (its shared rules are copied into its own `references/`), so you can also copy single skill folders by hand.

Verified on 2026-09-17: Codex CLI 0.145 and Antigravity CLI listed all 11 skills from `.agents/skills`, and OpenClaw 2026.9.3 reads `~/.agents/skills`.

## Your files

Skills keep your data in `~/.substack-skills/`, outside the plugin folder (updates would wipe it) and outside any git repo:

| File | Made by | Read by |
|---|---|---|
| `story-bank.md` | `substack-interviewer` | every writing skill |
| `voice-profile.md` | `substack-humanizer --mode profile` | every writing skill |
| `.env` | you | `substack-publisher` only |
| `outbox/` | `substack-publisher` | you, as a record of what went out |

## Publisher setup (optional)

1. `pip install python-substack==0.7.0` (`pip3` on macOS and Linux)
2. Ask your agent to "set up my Substack publisher". It runs `publish.py setup`, which creates `~/.substack-skills/.env` with instructions inside. Open that file and paste in your `substack.sid` cookie yourself (sign in at substack.com, F12, Application tab, Storage > Cookies > https://substack.com). Notes need only that; posts also need `PUBLICATION_URL`. Don't paste cookies into a chat.
3. Make every publish ask you first, whatever tries to run it.
   - **Claude Code:** add to `~/.claude/settings.json`:

     ```json
     { "permissions": { "ask": ["Bash(*publish.py *)", "PowerShell(*publish.py *)"] } }
     ```

   - **Other agents:** keep command approval switched on, and don't run the publisher in a mode that auto-approves shell commands. The skill also stops at an approval card before every publish.

4. Ask your agent to "check my Substack publisher setup". It runs `publish.py check`, which reads your profile and reports whether Notes and posts are ready.

What it can do: publish a post now (with or without emailing subscribers), schedule a post, publish a Note (optionally with a link card), delete a post or Note. Every post runs Substack's own prepublish check first.

**Verified live (2026-09-16):** setup check, Notes with formatting, Notes with a link card, Note deletion, and a failed login returning a clean error. **Not yet verified live:** posts (draft, publish, schedule, delete). They use python-substack's own documented calls and pass offline tests, but haven't run against a real publication. Reports welcome.

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
python -m unittest discover -s tests     # publish.py and the installer, offline
python scripts/check_skills.py --fix     # after editing references/, recopy them into the skills
```

## Credits

- Notes taxonomy and anti-fabrication rules adapted from [Solo-AI-Lab/substack-notes-skills](https://github.com/Solo-AI-Lab/substack-notes-skills) by Luan Doan (MIT).
- Publishing via [ma2za/python-substack](https://github.com/ma2za/python-substack) (MIT).
- Notes request shape cross-checked against [jakub-k-slys/substack-gateway-oss](https://github.com/jakub-k-slys/substack-gateway-oss) and [conorbronsdon/substack-mcp](https://github.com/conorbronsdon/substack-mcp).
- Bundle structure inspired by [sergebulaev/linkedin-skills](https://github.com/sergebulaev/linkedin-skills).

Not affiliated with Substack.

## License

MIT

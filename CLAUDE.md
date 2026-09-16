# Conventions for agents editing this repo

## Invariants

- **Exactly 11 skills** in `skills/`. `scripts/check_skills.py` fails otherwise.
- **Frontmatter:** `name` equals the folder name. `description` starts with "Use when", stays under 500 characters, has no dashes, and ends with "Not for X (use Y)" when a sibling overlaps.
- **Only `substack-publisher` touches Substack.** No other skill mentions `publish.py`, cookies, or credential env vars, and no other Python file imports `substack`.
- **Shared rules live in `references/`.** Skills cite them as `../../references/X.md`. Don't copy rules into skills.
- **User data lives in `~/.substack-skills/`**, never in the repo or plugin folder.
- **No dashes as clause connectors** in skills, references, or README (`references/voice-rules.md` rule 1).

## Changing a skill

Test first, the same way every skill here was built: run its scenario from `tests/scenarios.md` in a fresh agent without the change, record what fails, make the change, rerun with the skill loaded, and update `tests/results.md`. A skill edit without a failing scenario first doesn't ship.

## Before pushing

```
python scripts/check_skills.py
python -m unittest discover -s tests
```

Bump `version` in both `.claude-plugin/plugin.json` and `.claude-plugin/marketplace.json` together.

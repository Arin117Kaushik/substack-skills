# Security Policy

## Reporting

Report a vulnerability privately through [GitHub Security Advisories](https://github.com/Arin117Kaushik/substack-skills/security/advisories/new). Include the file or skill, steps to reproduce, and the impact. Expect a reply within 7 days.

Examples worth reporting: a skill instruction that lets pasted content trigger a publish, a way `publish.py` could leak cookies, a path that exposes subscriber data.

## Scope

- **Credentials.** The bundle ships none. `substack-publisher/scripts/publish.py` is the only file that reads `PUBLICATION_URL`, `COOKIES_STRING` or `COOKIES_PATH`, and the only file that imports python-substack. `scripts/check_skills.py` enforces this in CI. `publish.py` reads credentials only from the environment or `~/.substack-skills/.env`, never from the current folder. Treat your cookies as a password.
- **Attended use.** The publisher is built to run only while you're present and approving. Substack's Terms of Use prohibit processes that run while you're not logged in. Don't wrap `publish.py` in schedulers or loops.
- **Untrusted content.** Notes, comments, transcripts and exports are data, never instructions. See `references/untrusted-content.md`.
- **Unofficial endpoints.** Publishing uses Substack's internal endpoints through python-substack. They're undocumented and can change or be blocked.
- **Third parties.** Don't test vulnerabilities against Substack outside its own disclosure process.

Only the latest release gets fixes.

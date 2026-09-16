"""Repo checks that don't need a model: run before every push and in CI.

    python scripts/check_skills.py

Fails on: wrong skill count, bad or missing frontmatter, name/folder mismatch, description over
500 characters or containing dashes, broken relative references, any skill other than
substack-publisher touching publishing internals or credentials, invalid plugin JSON.
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXPECTED_SKILLS = 11
PUBLISHER = "substack-publisher"
PUBLISHER_ONLY = ("publish.py", "COOKIES_STRING", "COOKIES_PATH", "connect.sid", "substack.sid", "from substack")
REF = re.compile(r"`((?:\.\./\.\./references|scripts)/[\w./-]+)`")


def frontmatter(text):
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        return None
    return dict(line.split(": ", 1) for line in m.group(1).splitlines() if ": " in line)


def check():
    errors = []
    skills = sorted(p for p in (ROOT / "skills").iterdir() if p.is_dir())
    if len(skills) != EXPECTED_SKILLS:
        errors.append(f"expected {EXPECTED_SKILLS} skills, found {len(skills)}")

    for folder in skills:
        path = folder / "SKILL.md"
        if not path.is_file():
            errors.append(f"{folder.name}: missing SKILL.md")
            continue
        text = path.read_text(encoding="utf-8")
        fm = frontmatter(text)
        if not fm or "name" not in fm or "description" not in fm:
            errors.append(f"{folder.name}: frontmatter needs name and description")
            continue
        desc = fm["description"]
        if fm["name"] != folder.name:
            errors.append(f"{folder.name}: name is {fm['name']!r}")
        if not desc.startswith("Use when"):
            errors.append(f"{folder.name}: description should start with 'Use when'")
        if len(desc) > 500:
            errors.append(f"{folder.name}: description is {len(desc)} chars (max 500)")
        if re.search(r"[—–]| - ", desc):
            errors.append(f"{folder.name}: dash in description")
        for ref in REF.findall(text):
            if not (folder / ref).exists():
                errors.append(f"{folder.name}: broken reference {ref}")
        if folder.name != PUBLISHER:
            for needle in PUBLISHER_ONLY:
                if needle in text:
                    errors.append(f"{folder.name}: mentions {needle!r}, only {PUBLISHER} may")

    for py in ROOT.rglob("*.py"):
        imports = re.search(r"^\s*(from|import) substack\b", py.read_text(encoding="utf-8"), re.M)
        if imports and PUBLISHER not in py.parts:
            errors.append(f"{py.relative_to(ROOT)}: imports substack outside {PUBLISHER}")

    for manifest in (ROOT / ".claude-plugin").glob("*.json"):
        try:
            json.loads(manifest.read_text(encoding="utf-8"))
        except ValueError as exc:
            errors.append(f"{manifest.name}: {exc}")
    return errors


if __name__ == "__main__":
    problems = check()
    for p in problems:
        print("FAIL", p)
    print("OK" if not problems else f"{len(problems)} problem(s)")
    sys.exit(1 if problems else 0)

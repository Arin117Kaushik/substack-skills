"""Copy the skills into another agent's skills folder. Claude Code users install the plugin instead.

    python scripts/install.py codex         # ~/.agents/skills     (Codex, also read by OpenClaw)
    python scripts/install.py openclaw      # ~/.agents/skills     (same folder)
    python scripts/install.py antigravity   # ~/.gemini/config/skills
    python scripts/install.py PATH          # any skills folder, e.g. my-project/.agents/skills

Every skill folder is self-contained, so copies work anywhere. Re-run after `git pull` to update.
Only folders named substack-* are replaced; your files in ~/.substack-skills are never touched.
"""
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
AGENTS = Path.home() / ".agents" / "skills"
TARGETS = {"codex": AGENTS, "openclaw": AGENTS, "agents": AGENTS,
           "antigravity": Path.home() / ".gemini" / "config" / "skills"}


def install(dest: Path) -> list:
    dest.mkdir(parents=True, exist_ok=True)
    installed = []
    for skill in sorted((ROOT / "skills").glob("substack-*")):
        target = dest / skill.name
        if target.is_symlink():
            target.unlink()
        elif target.exists():
            shutil.rmtree(target)
        shutil.copytree(skill, target, ignore=shutil.ignore_patterns("__pycache__", "*.pyc"))
        installed.append(skill.name)
    return installed


if __name__ == "__main__":
    if len(sys.argv) != 2 or sys.argv[1] in ("-h", "--help"):
        print(__doc__)
        sys.exit(0 if len(sys.argv) == 2 else 2)
    arg = sys.argv[1]
    dest = TARGETS.get(arg.lower(), Path(arg).expanduser())
    names = install(dest)
    print(f"Installed {len(names)} skills into {dest}")
    print("Start a new session in your agent so it picks them up.")

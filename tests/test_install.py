"""The installer copies self-contained skill folders. Run: python -m unittest discover -s tests"""
import importlib.util
import re
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("install", ROOT / "scripts/install.py")
install = importlib.util.module_from_spec(spec)
spec.loader.exec_module(install)


class Install(unittest.TestCase):
    def test_copies_every_skill_self_contained(self):
        with tempfile.TemporaryDirectory() as d:
            names = install.install(Path(d))
            self.assertEqual(len(names), 11)
            for name in names:
                folder = Path(d, name)
                text = (folder / "SKILL.md").read_text(encoding="utf-8")
                self.assertNotIn("../", text, name)
                for ref in re.findall(r"`((?:references|scripts)/[\w./-]+)`", text):
                    self.assertTrue((folder / ref).exists(), f"{name}: {ref} missing after copy")
            self.assertTrue(Path(d, "substack-publisher", ".env.example").is_file())

    def test_reinstall_replaces_only_substack_folders(self):
        with tempfile.TemporaryDirectory() as d:
            Path(d, "someone-elses-skill").mkdir()
            Path(d, "substack-notes-writer").mkdir()
            Path(d, "substack-notes-writer", "stale.md").write_text("old")
            install.install(Path(d))
            self.assertTrue(Path(d, "someone-elses-skill").is_dir())
            self.assertFalse(Path(d, "substack-notes-writer", "stale.md").exists())


if __name__ == "__main__":
    unittest.main()

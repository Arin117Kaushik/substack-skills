"""Offline checks for publish.py: no network, no credentials. Run: python -m unittest discover -s tests"""
import importlib.util
import os
import tempfile
import unittest
from pathlib import Path
from unittest import mock

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("publish", ROOT / "skills/substack-publisher/scripts/publish.py")
publish = importlib.util.module_from_spec(spec)
spec.loader.exec_module(publish)


class NoteDoc(unittest.TestCase):
    def test_lines_become_paragraphs_with_marks(self):
        doc = publish.note_doc("Automate the **search**.\n\nNever the *voice*. [post](https://x.substack.com/p/a)")
        self.assertEqual(doc["type"], "doc")
        self.assertEqual(len(doc["content"]), 2)
        first, second = doc["content"]
        self.assertEqual(first["content"][1], {"type": "text", "text": "search", "marks": [{"type": "bold"}]})
        self.assertEqual(second["content"][1], {"type": "text", "text": "voice", "marks": [{"type": "italic"}]})
        self.assertEqual(second["content"][-1]["text"], "post (https://x.substack.com/p/a)")

    def test_empty_note_rejected(self):
        with self.assertRaises(ValueError):
            publish.note_doc("  \n\n ")


class Paywall(unittest.TestCase):
    def test_split(self):
        self.assertEqual(publish.split_paywall("free\n<!-- paywall -->\npaid"), ("free\n", "\npaid"))
        self.assertEqual(publish.split_paywall("all free"), ("all free", None))

    def test_two_markers_rejected(self):
        with self.assertRaises(ValueError):
            publish.split_paywall("a <!-- paywall --> b <!-- paywall --> c")


class Safety(unittest.TestCase):
    def test_redacts_cookie_values(self):
        with mock.patch.dict(os.environ, {"COOKIES_STRING": "substack.sid=s%3AsecretSecretSecret123; connect.sid=abcdefghij"}):
            out = publish.redact("401 for s%3AsecretSecretSecret123 and abcdefghij")
        self.assertNotIn("secretSecret", out)
        self.assertNotIn("abcdefghij", out)

    def test_env_file_never_overrides_real_env(self):
        with tempfile.TemporaryDirectory() as d, mock.patch.dict(os.environ, {"PUBLICATION_URL": "https://real.substack.com"}):
            Path(d, ".env").write_text("PUBLICATION_URL=https://file.substack.com\nCOOKIES_PATH=c.json\n")
            with mock.patch.object(publish.Path, "cwd", return_value=Path(d)):
                publish.load_env()
            self.assertEqual(os.environ["PUBLICATION_URL"], "https://real.substack.com")
            self.assertEqual(os.environ["COOKIES_PATH"], "c.json")
            os.environ.pop("COOKIES_PATH")

    def test_schedule_requires_timezone_before_any_network_call(self):
        api = mock.Mock()
        args = mock.Mock(audience="everyone", at="2026-09-20T08:00:00", no_send=False)
        with self.assertRaises(ValueError):
            publish.cmd_post(api, args)
        api.post_draft.assert_not_called()

    def test_bad_audience_rejected_before_any_network_call(self):
        api = mock.Mock()
        with self.assertRaises(ValueError):
            publish.cmd_post(api, mock.Mock(audience="paid", at=None))
        api.post_draft.assert_not_called()


if __name__ == "__main__":
    unittest.main()

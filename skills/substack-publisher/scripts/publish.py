"""Publish to Substack after the user approves. The only file in this bundle that talks to Substack.

    python publish.py setup
    python publish.py check
    python publish.py post FILE.md --title "..." [--subtitle ..] [--audience everyone|only_paid|founding|only_free]
                      [--seo-title ..] [--seo-description ..] [--slug ..] [--section-id N] [--tags a,b]
                      [--no-send] [--at 2026-09-20T08:00:00+05:30] [--draft]
    python publish.py note FILE.md [--link URL]
    python publish.py delete-post ID
    python publish.py delete-note ID

Credentials come from the environment or the first .env found in: current folder, ~/.substack-skills/, bundle root:
COOKIES_STRING or COOKIES_PATH (always), plus PUBLICATION_URL for posts. Notes only need a Substack profile.
Never pass credentials on the command line.
Prints one JSON object. Exit code 1 on any failure, with cookie values redacted.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
from datetime import datetime
from pathlib import Path

SUBSTACK_API = "https://substack.com/api/v1"
PAYWALL = "<!-- paywall -->"
AUDIENCES = ("everyone", "only_paid", "founding", "only_free")
BUNDLE_ROOT = Path(__file__).resolve().parents[3]
USER_DIR = Path.home() / ".substack-skills"
ENV_FILE = USER_DIR / ".env"
LOADED_ENV = None  # which .env file load_env() used, reported by check
_INLINE = re.compile(r"\*\*(.+?)\*\*|\*(.+?)\*|\[([^\]]+)\]\(([^)\s]+)\)")


def load_env() -> None:
    """Minimal .env reader so the bundle needs no python-dotenv. Real env vars win."""
    global LOADED_ENV
    for folder in (Path.cwd(), USER_DIR, BUNDLE_ROOT):
        path = folder / ".env"
        if not path.is_file():
            continue
        LOADED_ENV = str(path)
        # utf-8-sig: Notepad can save a BOM that would otherwise glue itself to the first key
        for line in path.read_text(encoding="utf-8-sig").splitlines():
            key, sep, value = line.partition("=")
            if sep and key.strip() and not key.lstrip().startswith("#"):
                os.environ.setdefault(key.strip(), value.strip().strip('"').strip("'"))
        return


def inline_nodes(text: str) -> list[dict]:
    """Bold and italic become marks. Links become 'text (url)': Notes have no link marks in v1."""
    nodes, last = [], 0
    for m in _INLINE.finditer(text):
        if m.start() > last:
            nodes.append({"type": "text", "text": text[last:m.start()]})
        if m.group(1) is not None:
            nodes.append({"type": "text", "text": m.group(1), "marks": [{"type": "bold"}]})
        elif m.group(2) is not None:
            nodes.append({"type": "text", "text": m.group(2), "marks": [{"type": "italic"}]})
        else:
            nodes.append({"type": "text", "text": f"{m.group(3)} ({m.group(4)})"})
        last = m.end()
    if last < len(text):
        nodes.append({"type": "text", "text": text[last:]})
    return [n for n in nodes if n["text"]]


def note_doc(markdown: str) -> dict:
    """Each non-empty line is one paragraph, like pressing Enter in the Notes composer."""
    paragraphs = [{"type": "paragraph", "content": inline_nodes(line.strip())}
                  for line in markdown.splitlines() if line.strip()]
    if not paragraphs:
        raise ValueError("Note is empty")
    return {"type": "doc", "attrs": {"schemaVersion": "v1"}, "content": paragraphs}


def split_paywall(markdown: str) -> tuple[str, str | None]:
    if markdown.count(PAYWALL) > 1:
        raise ValueError("Only one paywall marker is allowed")
    before, sep, after = markdown.partition(PAYWALL)
    return before, (after if sep else None)


def cookie_args() -> dict:
    load_env()
    if os.getenv("COOKIES_PATH"):
        return {"cookies_path": os.environ["COOKIES_PATH"]}
    if os.getenv("COOKIES_STRING"):
        return {"cookies_string": os.environ["COOKIES_STRING"]}
    raise ValueError(f"No Substack login found. Run `publish.py setup`, then paste your substack.sid cookie "
                     f"into {ENV_FILE} (the file explains where to find it).")


def profile_session():
    """Logged-in session on substack.com. Enough for Notes; no publication needed."""
    import requests
    from substack import Api

    args = cookie_args()
    session = requests.Session()
    if "cookies_path" in args:
        session.cookies.update(json.loads(Path(args["cookies_path"]).read_text(encoding="utf-8")))
    else:
        session.cookies.update(Api._parse_cookies_string(args["cookies_string"]))
    return session


def publication_api():
    """python-substack client bound to a publication. Posts need one."""
    args = cookie_args()
    url = os.getenv("PUBLICATION_URL", "")
    if not url or "substack.com/@" in url:
        raise ValueError("Posts need a publication URL like https://name.substack.com. "
                         "A profile page (substack.com/@handle) can publish Notes only.")
    from substack import Api

    return Api(publication_url=url, **args)


def ok(response) -> dict:
    if response.status_code == 401:
        raise RuntimeError(f"Substack rejected the login (401). The substack.sid cookie in {LOADED_ENV or ENV_FILE} "
                           "is wrong or expired: copy a fresh one from your browser.")
    if not 200 <= response.status_code < 300:
        raise RuntimeError(f"Substack returned {response.status_code}: {response.text[:300]}")
    return response.json() if response.content else {}


def site(api) -> str:
    return api.publication_url.rsplit("/api/v1", 1)[0]


def cmd_check(session, args) -> dict:
    from substack import Api

    profile = ok(session.get(f"{SUBSTACK_API}/user/profile/self"))
    pubs = [Api.get_publication_url(pu["publication"])
            for pu in profile.get("publicationUsers") or [] if pu.get("publication")]
    return {"ok": True, "handle": profile.get("handle"), "user_id": profile.get("id"), "env_file": LOADED_ENV,
            "notes": "ready", "publications": pubs,
            "posts": "ready" if pubs else "needs a Substack publication"}


def cmd_setup(args) -> dict:
    """Create ~/.substack-skills/.env from the template. Never overwrites, never asks for the cookie."""
    USER_DIR.mkdir(exist_ok=True)
    (USER_DIR / "outbox").mkdir(exist_ok=True)
    created = not ENV_FILE.exists()
    if created:
        ENV_FILE.write_text((BUNDLE_ROOT / ".env.example").read_text(encoding="utf-8"), encoding="utf-8")
    return {"action": "setup", "env_file": str(ENV_FILE), "created": created, "next_steps": [
        f"Open {ENV_FILE} in a text editor.",
        "In your browser, sign in at substack.com, press F12, open the Application tab, "
        "then Storage > Cookies > https://substack.com and copy the value of substack.sid.",
        "Set the line COOKIES_STRING=substack.sid=<that value>, save the file.",
        "For posts, also set PUBLICATION_URL=https://yourname.substack.com.",
        "Run: publish.py check. Never paste the cookie into a chat."]}


def cmd_post(api, args) -> dict:
    if args.audience not in AUDIENCES:
        raise ValueError(f"--audience must be one of {AUDIENCES}")
    when = None
    if args.at:
        when = datetime.fromisoformat(args.at)
        if when.tzinfo is None:
            raise ValueError("--at needs a timezone offset, e.g. 2026-09-20T08:00:00+05:30")
        if args.no_send:
            raise ValueError("--no-send only applies to publishing now, not scheduling")

    from substack.post import Post

    before, after = split_paywall(Path(args.file).expanduser().read_text(encoding="utf-8"))
    post = Post(title=args.title, subtitle=args.subtitle or "", user_id=api.get_user_id(), audience=args.audience)
    post.from_markdown(before, api=api)
    if after is not None:
        post.add({"type": "paywall"})
        post.from_markdown(after, api=api)
    draft_id = api.post_draft(post.get_draft())["id"]
    result = {"draft_id": draft_id, "edit_url": f"{site(api)}/publish/post/{draft_id}"}

    meta = {"search_engine_title": args.seo_title, "search_engine_description": args.seo_description,
            "slug": args.slug, "draft_section_id": args.section_id}
    meta = {k: v for k, v in meta.items() if v is not None}
    if meta:
        api.put_draft(draft_id, **meta)
    if args.tags:
        api.add_tags_to_post(draft_id, [t.strip() for t in args.tags.split(",") if t.strip()])
    if args.draft:
        return {"action": "draft_created", **result}

    check = api.prepublish_draft(draft_id)
    if check.get("errors"):
        return {"action": "blocked_by_prepublish", "errors": check["errors"], **result}
    if when:
        api.schedule_draft(draft_id, when)
        return {"action": "scheduled", "at": when.isoformat(), **result}
    published = api.publish_draft(draft_id, send=not args.no_send)
    return {"action": "published", "emailed": not args.no_send,
            "url": published.get("canonical_url"), "warnings": check.get("suggestions") or [], **result}


def cmd_note(session, args) -> dict:
    # python-substack has no Notes call. Request shape matches substack-gateway-oss and substack-mcp.
    payload = {"bodyJson": note_doc(Path(args.file).expanduser().read_text(encoding="utf-8")),
               "tabId": "for-you", "surface": "feed", "replyMinimumRole": "everyone"}
    if args.link:
        att = ok(session.post(f"{SUBSTACK_API}/comment/attachment", json={"url": args.link, "type": "link"}))
        payload["attachmentIds"] = [att["id"]]
    note = ok(session.post(f"{SUBSTACK_API}/comment/feed", json=payload))
    return {"action": "note_published", "note_id": note.get("id")}


def cmd_delete_post(api, args) -> dict:
    api.delete_draft(args.id)
    return {"action": "post_deleted", "id": args.id}


def cmd_delete_note(session, args) -> dict:
    ok(session.delete(f"{SUBSTACK_API}/comment/{args.id}"))
    return {"action": "note_deleted", "id": args.id}


def redact(text: str) -> str:
    from urllib.parse import unquote

    for pair in (os.getenv("COOKIES_STRING") or "").split(";"):
        value = pair.partition("=")[2].strip()
        if len(value) > 6:  # python-substack URL-decodes cookies, so hide both spellings
            text = text.replace(value, "[redacted]").replace(unquote(value), "[redacted]")
    return re.sub(r"s(%3A|:)(?!//)[A-Za-z0-9%._\-+/=]{12,}", "[redacted]", text)


def main(argv=None) -> int:
    p = argparse.ArgumentParser(description="Publish to Substack after approval.")
    sub = p.add_subparsers(dest="cmd", required=True)
    sub.add_parser("setup")
    sub.add_parser("check")
    post = sub.add_parser("post")
    post.add_argument("file")
    post.add_argument("--title", required=True)
    post.add_argument("--subtitle")
    post.add_argument("--audience", default="everyone")
    post.add_argument("--seo-title")
    post.add_argument("--seo-description")
    post.add_argument("--slug")
    post.add_argument("--section-id", type=int)
    post.add_argument("--tags")
    post.add_argument("--no-send", action="store_true", help="publish on the web without emailing subscribers")
    post.add_argument("--at", help="schedule instead of publishing now (ISO 8601 with offset)")
    post.add_argument("--draft", action="store_true", help="create the draft only")
    note = sub.add_parser("note")
    note.add_argument("file")
    note.add_argument("--link")
    for name in ("delete-post", "delete-note"):
        sub.add_parser(name).add_argument("id", type=int)
    args = p.parse_args(argv)

    if args.cmd == "setup":
        print(json.dumps(cmd_setup(args), indent=2))
        return 0
    handlers = {"check": (profile_session, cmd_check), "note": (profile_session, cmd_note),
                "delete-note": (profile_session, cmd_delete_note),
                "post": (publication_api, cmd_post), "delete-post": (publication_api, cmd_delete_post)}
    try:
        connect, handler = handlers[args.cmd]
        print(json.dumps(handler(connect(), args), indent=2))
        return 0
    except ModuleNotFoundError as exc:
        print(json.dumps({"ok": False, "error": f"{exc}. Install it with: pip install python-substack==0.7.0"}, indent=2))
        return 1
    except Exception as exc:  # one exit path, always redacted
        print(json.dumps({"ok": False, "error": redact(f"{type(exc).__name__}: {exc}")}, indent=2))
        return 1


if __name__ == "__main__":
    sys.exit(main())

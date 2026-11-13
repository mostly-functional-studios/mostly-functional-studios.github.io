#!/usr/bin/env python3
"""Zero-dependency link/asset checker and production release guard."""
from pathlib import Path
import re
import sys
from html.parser import HTMLParser
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1] / "site"
ERRORS = []
DRAFT = len(sys.argv) == 2 and sys.argv[1] == "--draft"
if len(sys.argv) > 2 or (len(sys.argv) == 2 and not DRAFT):
    raise SystemExit("Usage: python3 scripts/check_ready.py [--draft]")

class LinkParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        for key in ("href", "src"):
            if key in attrs:
                self.links.append((tag, key, attrs[key]))

for doc in ROOT.rglob("*.html"):
    html = doc.read_text(encoding="utf-8")
    if not DRAFT and "data-release-blocker=" in html:
        ERRORS.append(f"{doc.relative_to(ROOT)}: remove the draft legal-warning block ONLY after review")
    if not DRAFT and ("[[" in html or "]]" in html):
        for match in sorted(set(re.findall(r"\[\[[A-Z_]+\]\]", html))):
            ERRORS.append(f"{doc.relative_to(ROOT)}: legal/contact placeholder not filled: {match}")
    if not re.search(r'<html\s+lang="de"', html):
        ERRORS.append(f"{doc.relative_to(ROOT)}: missing language marker")
    parser = LinkParser()
    parser.feed(html)
    for tag, key, value in parser.links:
        if not value or value.startswith(("#", "https://", "http://", "mailto:", "tel:", "data:")):
            continue
        parsed = urlsplit(value)
        p = unquote(parsed.path)
        if p.startswith("/"):
            ERRORS.append(f"{doc.relative_to(ROOT)}: root-absolute path unsafe for project pages: {value}")
            continue
        target = (doc.parent / p).resolve()
        if not target.is_relative_to(ROOT.resolve()) or not target.exists():
            ERRORS.append(f"{doc.relative_to(ROOT)}: broken {key} {value}")

if ERRORS:
    print("\nRELEASE BLOCKED:\n" + "\n".join(" - " + s for s in ERRORS))
    sys.exit(1)
print("Draft links and assets OK; legal data intentionally not validated." if DRAFT else "Release validation passed. Static assets and required legal/contact fields found.")

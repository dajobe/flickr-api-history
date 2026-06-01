#!/usr/bin/env python3
"""Compare an archived Flickr API method doc page with the live page."""

from __future__ import annotations

import argparse
import difflib
import sys
import urllib.request
from collections.abc import Sequence
from html.parser import HTMLParser
from pathlib import Path

BLOCK_TAGS = {
    "address",
    "article",
    "aside",
    "blockquote",
    "br",
    "dd",
    "div",
    "dl",
    "dt",
    "fieldset",
    "figcaption",
    "figure",
    "footer",
    "form",
    "h1",
    "h2",
    "h3",
    "h4",
    "h5",
    "h6",
    "header",
    "hr",
    "li",
    "main",
    "nav",
    "ol",
    "p",
    "pre",
    "section",
    "table",
    "td",
    "th",
    "tr",
    "ul",
}

SKIP_TAGS = {"script", "style", "noscript"}


class TextExtractor(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self._parts: list[str] = []
        self._skip_depth = 0

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag in SKIP_TAGS:
            self._skip_depth += 1
            return
        if self._skip_depth == 0 and tag in BLOCK_TAGS:
            self._parts.append("\n")

    def handle_endtag(self, tag: str) -> None:
        if tag in SKIP_TAGS and self._skip_depth:
            self._skip_depth -= 1
            return
        if self._skip_depth == 0 and tag in BLOCK_TAGS:
            self._parts.append("\n")

    def handle_data(self, data: str) -> None:
        if self._skip_depth == 0:
            self._parts.append(data)

    def lines(self) -> list[str]:
        text = "".join(self._parts)
        lines = []
        for line in text.splitlines():
            normalized = " ".join(line.split())
            if normalized:
                lines.append(normalized)
        return lines


def fetch(url: str) -> tuple[bytes, str]:
    request = urllib.request.Request(
        url,
        headers={"User-Agent": "flickr-api-history/1.0"},
    )
    with urllib.request.urlopen(request, timeout=30) as response:
        content_type = response.headers.get_content_charset()
        return response.read(), content_type or "utf-8"


def decode(data: bytes, fallback_encoding: str = "utf-8") -> str:
    return data.decode(fallback_encoding, errors="replace")


def method_doc_lines(html: str, method: str) -> list[str]:
    parser = TextExtractor()
    parser.feed(html)
    lines = parser.lines()

    start = 0
    for index, line in enumerate(lines):
        if line == method:
            start = index
            break

    end = len(lines)
    for index in range(start + 1, len(lines)):
        line = lines[index]
        if line == "API Explorer" or line.startswith("API Explorer :"):
            end = index
            break
        if (
            line
            == "This site uses cookies to improve your experience and to help show content that is more relevant to your interests."
        ):
            end = index
            break

    return lines[start:end]


def parse_args(argv: Sequence[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--method",
        required=True,
        help="Flickr API method name, such as flickr.photos.search",
    )
    parser.add_argument(
        "--archive", type=Path, required=True, help="Archived HTML file"
    )
    parser.add_argument("--url", required=True, help="Current method documentation URL")
    parser.add_argument(
        "--fetched-output",
        type=Path,
        required=True,
        help="Where to leave fetched HTML when changed",
    )
    return parser.parse_args(argv)


def main(argv: Sequence[str] | None = None) -> int:
    args = parse_args(argv)
    old_html = args.archive.read_text(encoding="utf-8", errors="replace")
    fetched_bytes, encoding = fetch(args.url)
    new_html = decode(fetched_bytes, encoding)

    old_lines = method_doc_lines(old_html, args.method)
    new_lines = method_doc_lines(new_html, args.method)

    if old_lines == new_lines:
        if args.fetched_output.exists():
            args.fetched_output.unlink()
        print(f"No change in {args.method} documentation")
        return 0

    args.fetched_output.parent.mkdir(parents=True, exist_ok=True)
    args.fetched_output.write_bytes(fetched_bytes)
    print(f"Changed: {args.method} documentation")
    print(f"Fetched copy left at {args.fetched_output}")

    diff = difflib.unified_diff(
        [line + "\n" for line in old_lines],
        [line + "\n" for line in new_lines],
        fromfile=str(args.archive),
        tofile=args.url,
    )
    sys.stdout.writelines(diff)
    return 1


def _cli_entry() -> None:
    raise SystemExit(main())


if __name__ == "__main__":
    _cli_entry()

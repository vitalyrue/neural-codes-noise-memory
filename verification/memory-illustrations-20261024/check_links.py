"""Validate only the built Chapter 2 page and its linked source PDFs.

Run after the chapter build. This never scans other HTML pages and never edits
reader files. Static math checks do not replace browser MathJax rendering.
"""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit, parse_qs, unquote
from collections import Counter
from datetime import datetime
import argparse
import hashlib
import html
import json
import math
import re
import sys

TASK = Path(__file__).resolve().parent
ROOT = TASK.parents[1]
LINK = re.compile(r"\[([^\]]+)\]\(([^)]+\.pdf#[^)]+)\)")
NOTE = re.compile(r"(?m)^\[\^([^\]]+)\]:[^\n]*(?:\n(?: {4}|\t)[^\n]*)*")


def clean_label(text):
    return " ".join(html.unescape(text).split())


def pdf_key(url):
    u = urlsplit(html.unescape(url))
    return Path(unquote(u.path)).name, u.fragment


class ChapterHTML(HTMLParser):
    def __init__(self, text):
        super().__init__(convert_charrefs=True)
        self.ids, self.links, self.errors = [], [], []
        self.math_spans = 0
        self.anchor = None
        self.in_main = False
        self.figure_depth = 0
        self.figure_images = []
        self.main_text = []
        self.feed(text)

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == "main":
            self.in_main = True
        if tag == "figure" and self.in_main:
            self.figure_depth += 1
        if tag == "img" and self.in_main and self.figure_depth:
            self.figure_images.append({"src": a.get("src", ""), "alt": a.get("alt", "")})
        if "id" in a:
            self.ids.append(a["id"])
        classes = a.get("class", "").split()
        if "math" in classes:
            self.math_spans += 1
        if tag == "merror" or any(c in classes for c in (
            "katex-error", "mjx-merror", "MathJax_Error", "publisher-block-error"
        )):
            self.errors.append({"tag": tag, "attributes": a})
        if tag == "a" and a.get("href"):
            self.anchor = {"href": a["href"], "label_parts": []}

    def handle_data(self, data):
        if self.in_main:
            self.main_text.append(data)
        if self.anchor is not None:
            self.anchor["label_parts"].append(data)

    def handle_endtag(self, tag):
        if tag == "figure" and self.in_main:
            self.figure_depth = max(0, self.figure_depth - 1)
        if tag == "main":
            self.in_main = False
        if tag == "a" and self.anchor is not None:
            self.links.append({
                "href": self.anchor["href"],
                "label": clean_label("".join(self.anchor["label_parts"]))
            })
            self.anchor = None


def expected_links(markdown):
    definitions = {m.group(1): m.group(0) for m in NOTE.finditer(markdown)}
    body = NOTE.sub("", markdown)
    calls = re.findall(r"\[\^([^\]]+)\]", body)
    links = LINK.findall(body)
    for call in calls:
        if call not in definitions:
            raise ValueError(f"Missing footnote definition: {call}")
        links.extend(LINK.findall(definitions[call]))
    return links, calls, definitions


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--html", type=Path, default=ROOT / "site/chapters/ch-memory-dynamics.html")
    ap.add_argument("--markdown", type=Path, default=ROOT / "content/chapters/02-memory-dynamics.md")
    ap.add_argument("--output", type=Path, default=TASK / "post-build-link-check.json")
    args = ap.parse_args()
    page = args.html.resolve()
    if page.name != "ch-memory-dynamics.html":
        ap.error("Scope is only ch-memory-dynamics.html")
    failures, checked_pdfs = [], {}
    text = page.read_text(encoding="utf-8")
    md = args.markdown.read_text(encoding="utf-8")
    parsed = ChapterHTML(text)
    expected, calls, definitions = expected_links(md)
    source_count = len(LINK.findall(md))
    if source_count != 48:
        failures.append({"type": "source_pdf_link_count", "expected": 48, "actual": source_count})
    if len(definitions) != 14 or len(calls) != 16:
        failures.append({"type": "footnotes", "expected_definitions": 14,
                         "definitions": len(definitions), "expected_calls": 16, "calls": len(calls)})
    for id, definition in definitions.items():
        if not LINK.search(definition):
            failures.append({"type": "footnote_without_pdf_link", "footnote": id})
    actual = [a for a in parsed.links if urlsplit(a["href"]).path.lower().endswith(".pdf")]
    expected_counter = Counter((clean_label(label), pdf_key(url)) for label, url in expected)
    actual_counter = Counter((a["label"], pdf_key(a["href"])) for a in actual)
    for label_url, count in (expected_counter - actual_counter).items():
        failures.append({"type": "missing_pdf_link", "label": label_url[0], "target": label_url[1], "count": count})
    for label_url, count in (actual_counter - expected_counter).items():
        failures.append({"type": "unexpected_pdf_link", "label": label_url[0], "target": label_url[1], "count": count})
    source_map = json.loads((TASK / "source-locators.json").read_text(encoding="utf-8"))
    sources = {Path(s["path"]).name: s for s in source_map["sources"]}
    site = page.parent.parent
    try:
        import fitz
    except ImportError:
        raise SystemExit("PyMuPDF is required for PDF page validation. Use the system Python with fitz installed.")
    for a in actual:
        u = urlsplit(a["href"])
        name = Path(unquote(u.path)).name
        if u.scheme or u.netloc or name not in sources:
            failures.append({"type": "unexpected_pdf_source", "target": a["href"]})
            continue
        target = ((site / unquote(u.path.lstrip("/"))) if u.path.startswith("/")
                  else page.parent / unquote(u.path)).resolve()
        if not target.is_relative_to(site.resolve()):
            failures.append({"type": "pdf_outside_site", "target": str(target)})
            continue
        if not target.exists():
            failures.append({"type": "missing_pdf_copy", "target": str(target)})
            continue
        if str(target) not in checked_pdfs:
            source = sources[name]
            digest = hashlib.sha256(target.read_bytes()).hexdigest()
            with fitz.open(target) as pdf:
                sizes = [(p.rect.width, p.rect.height) for p in pdf]
            checked_pdfs[str(target)] = {"sha256": digest, "pages": len(sizes), "page_sizes": sizes}
            if digest != source["sha256"] or len(sizes) != source["page_count"]:
                failures.append({"type": "pdf_copy_mismatch", "target": str(target),
                                 "expected_sha256": source["sha256"], "actual_sha256": digest,
                                 "expected_pages": source["page_count"], "actual_pages": len(sizes)})
        try:
            fragment = parse_qs(u.fragment, keep_blank_values=True, strict_parsing=True)
            if set(fragment) != {"page", "zoom"} or any(len(v) != 1 for v in fragment.values()):
                raise ValueError("Expected exactly one page and one zoom parameter")
            if not re.fullmatch(r"[1-9]\d*", fragment["page"][0]):
                raise ValueError("Page must be a positive integer")
            page_no = int(fragment["page"][0])
            info = checked_pdfs[str(target)]
            if not 1 <= page_no <= info["pages"]:
                raise ValueError("Page outside PDF")
            zoom = [float(x) for x in fragment["zoom"][0].split(",")]
            if len(zoom) != 3 or not all(math.isfinite(x) for x in zoom) or zoom[0] <= 0:
                raise ValueError("Zoom must be a finite positive percent,left,top triple")
            width, height = info["page_sizes"][page_no - 1]
            if not (0 <= zoom[1] <= width and 0 <= zoom[2] <= height):
                raise ValueError("Zoom offset outside source page")
            label_page = re.search(r"\bpp?\.\s*(\d+)", a["label"])
            if label_page and int(label_page.group(1)) != page_no:
                raise ValueError("Label page does not match target page")
        except (ValueError, KeyError) as e:
            failures.append({"type": "invalid_pdf_fragment", "target": a["href"], "reason": str(e)})
    for id, count in Counter(parsed.ids).items():
        if count > 1:
            failures.append({"type": "duplicate_id", "id": id, "count": count})
    rendered_notes = sum(bool(re.fullmatch(r"fn\d+", id)) for id in parsed.ids)
    if rendered_notes != len(calls):
        failures.append({"type": "rendered_footnote_count", "expected": len(calls), "actual": rendered_notes})
    if re.search(r"\[\^[^\]\n]+\]", text):
        failures.append({"type": "unresolved_footnote_placeholder"})
    if re.search(r"\{\{\s*block:[^}]*\}\}", text):
        failures.append({"type": "unresolved_block_placeholder"})
    failures.extend({"type": "math_or_block_error", "details": e} for e in parsed.errors)
    if parsed.math_spans == 0:
        failures.append({"type": "missing_math_markup"})
    expected_new_figures = [
        "../assets/fig-memory-spike-trace.png",
        "../assets/fig-memory-inhibition-rates.png",
        "../assets/fig-memory-line-ring.png",
    ]
    expected_figures = expected_new_figures + ["../assets/fig-memory-tilted-decay.png"]
    figure_sources = Counter(image["src"] for image in parsed.figure_images)
    if len(parsed.figure_images) != 4:
        failures.append({"type": "figure_image_count", "expected": 4,
                         "actual": len(parsed.figure_images)})
    if figure_sources != Counter(expected_figures):
        failures.append({"type": "figure_image_sources", "expected": expected_figures,
                         "actual": dict(figure_sources)})
    for src in figure_sources:
        target = (page.parent / unquote(urlsplit(src).path)).resolve()
        if not target.is_relative_to(site.resolve()) or not target.is_file():
            failures.append({"type": "missing_figure_asset", "target": src})
    if "![" in "".join(parsed.main_text):
        failures.append({"type": "literal_markdown_image_in_main"})
    result = {"checked_at": datetime.now().astimezone().isoformat(),
              "scope": "Only Chapter 2 HTML and PDFs it links; no other HTML pages opened",
              "status": "pass" if not failures else "failed", "html": str(page),
              "html_sha256": hashlib.sha256(page.read_bytes()).hexdigest(),
              "markdown": str(args.markdown.resolve()), "markdown_pdf_links": source_count,
              "expected_rendered_pdf_links": len(expected), "rendered_pdf_links": len(actual),
              "footnote_definitions": len(definitions), "footnote_calls": len(calls),
              "rendered_footnotes": rendered_notes, "math_spans": parsed.math_spans,
              "figure_images": parsed.figure_images,
              "expected_new_figure_paths": expected_new_figures,
              "pdf_copies": checked_pdfs, "failures": failures,
              "limits": ["Static math checks only; browser MathJax errors require a browser check",
                         "PDF offsets are syntax/bounds checked; viewer positioning needs browser inspection"]}
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({k: v for k, v in result.items() if k != "pdf_copies"}, ensure_ascii=False, indent=2))
    return bool(failures)


if __name__ == "__main__":
    sys.exit(main())

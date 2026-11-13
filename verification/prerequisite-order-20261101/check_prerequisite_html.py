"""Focused checks of built prerequisite HTML, without changing sources or site.

BeautifulSoup checks the generated markup and its embedded folding contract.
This is not a browser/pixel check or a claim of complete semantic acceptance.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
from datetime import datetime, timezone
from pathlib import Path

from bs4 import BeautifulSoup, Tag

TASK_START = "2026-11-01T13:32:42+00:00"
EXTENSION_START = "2026-11-01T19:23:52+00:00"
DEFAULT_PAGES = [
    "ch-foundations", "ch-persistence", "ch-memory-dynamics",
    "ch-memory-information", "ch-memory-readout", "ch-place-fields",
    "ch-eye-circuit", "ch-simulating-eye", "ch-simulation-tools",
]
DEFINITIONS = {
    "ch-persistence": ["Brownian motion"],
    "ch-memory-information": ["likelihood"],
    "ch-memory-readout": ["hyperbolic cotangent", "White noise"],
    "ch-place-fields": ["Gaussian process", "jointly Gaussian vector"],
    "ch-simulating-eye": ["random seed"],
}
OPTIONAL_SELECTOR = ".publisher-worked-calculation, .publisher-clarification-note"


def normalize(text: str) -> str:
    return " ".join(text.split()).casefold()


def hidden_reason(node: Tag) -> str | None:
    """Also recognize wrappers that the embedded script turns into details."""
    for ancestor in [node, *node.parents]:
        if not isinstance(ancestor, Tag):
            continue
        if ancestor.name == "details":
            return "inside <details>"
        classes = set(ancestor.get("class", []))
        if "publisher-fold-always" in classes:
            return "inside a publisher-fold-always runtime fold"
        if ancestor.get("data-publisher-fold") in {"always", "open"}:
            return "inside a data-publisher-fold runtime fold"
        if ancestor.has_attr("hidden") or ancestor.get("aria-hidden") == "true":
            return "inside explicitly hidden content"
        if re.search(r"(?:display\s*:\s*none|visibility\s*:\s*hidden)",
                     ancestor.get("style", ""), re.I):
            return "inside content hidden by inline style"
    return None


def definition_check(soup: BeautifulSoup, term: str) -> tuple[bool, str]:
    main = soup.find("main") or soup
    terms = [tag for tag in main.select(".definition-term")
             if normalize(tag.get_text(" ", strip=True)) == normalize(term)]
    if not terms:
        return False, f"No first-teaching .definition-term for {term}"
    first = terms[0]
    reason = hidden_reason(first)
    if reason:
        return False, f"First teaching for {term} is {reason}"
    paragraph = first.find_parent("p") or first.parent
    explanation = paragraph.select_one(".definition-explanation")
    if explanation is None or not explanation.get_text(" ", strip=True):
        return False, f"First teaching for {term} lacks its explanation"
    reason = hidden_reason(explanation)
    if reason:
        return False, f"Explanation for {term} is {reason}"
    return True, f"First teaching and explanation for {term} outside folds"


def fixture_test() -> dict:
    """Mutate only an in-memory fixture, never a site/source file."""
    good = BeautifulSoup(
        '<main><p><span class="definition-term">Brownian motion</span> '
        '<span class="definition-explanation">A continuous process with '
        'independent Gaussian increments.</span></p></main>', "html.parser")
    assert definition_check(good, "Brownian motion")[0]
    bad = BeautifulSoup(str(good), "html.parser")
    details = bad.new_tag("details")
    bad.p.wrap(details)
    caught_details = not definition_check(bad, "Brownian motion")[0]
    runtime = BeautifulSoup(str(good), "html.parser")
    wrapper = runtime.new_tag("div", attrs={"class": "publisher-fold-always"})
    runtime.p.wrap(wrapper)
    caught_runtime = not definition_check(runtime, "Brownian motion")[0]
    assert caught_details and caught_runtime
    return {"valid_fixture_passes": True,
            "definition_wrapped_in_details_rejected": caught_details,
            "definition_in_future_runtime_fold_rejected": caught_runtime,
            "site_and_sources_modified": False}


def check_site(site: Path, pages: list[str], phase: str) -> dict:
    results: list[dict] = []
    hashes: dict[str, str] = {}
    soups: dict[str, BeautifulSoup] = {}

    def record(page: str, check: str, ok: bool, evidence: str,
               pending: bool = False) -> None:
        results.append({"page": page, "check": check,
                        "status": "pending" if pending else "pass" if ok else "fail",
                        "evidence": evidence})

    for page in pages:
        path = site / "chapters" / f"{page}.html"
        if not path.is_file():
            record(page, "page-exists", False, str(path))
            continue
        content = path.read_bytes()
        hashes[f"chapters/{page}.html"] = hashlib.sha256(content).hexdigest()
        soups[page] = BeautifulSoup(content.decode("utf-8-sig"), "html.parser")
        record(page, "page-exists", True, str(path))

    for page, terms in DEFINITIONS.items():
        if page not in soups:
            record(page, "definition-page-available", False, "Target page missing")
            continue
        for term in terms:
            ok, evidence = definition_check(soups[page], term)
            record(page, f"visible-definition:{term}", ok, evidence)

    readout = soups.get("ch-memory-readout")
    if readout:
        matches = [tag for tag in readout.select("main .math.display")
                   if re.search(r"V_\{\\mathrm\{ideal\}\}\s*\(L\)", tag.get_text())
                   and "\\coth" in tag.get_text()]
        good = bool(matches) and hidden_reason(matches[0]) is None
        record("ch-memory-readout", "finite-ideal-variance-visible", good,
               "Finite V_ideal(L) expression with coth outside folds" if good
               else "Missing finite coth expression or expression lies in a fold")

    optional_count = explicit_details_count = 0
    for page, soup in soups.items():
        main = soup.find("main") or soup
        optional = main.select(OPTIONAL_SELECTOR)
        optional_count += len(optional)
        invalid = []
        for tag in optional:
            mode = tag.get("data-publisher-fold")
            classes = set(tag.get("class", []))
            parent = tag.find_parent("details")
            closed_details = parent is not None and not parent.has_attr("open")
            configured_closed = ("publisher-fold-always" in classes or mode == "always")
            forced_open = "publisher-fold-open" in classes or mode == "open"
            if forced_open or not (closed_details or configured_closed):
                invalid.append(tag.get_text(" ", strip=True)[:100])
        record(page, "optional-derivations-examples-default-closed", not invalid,
               f"{len(optional)} optional wrappers; invalid={invalid}")
        details = main.select("details.publisher-long-content")
        explicit_details_count += len(details)
        opened = [tag for tag in details if tag.has_attr("open")]
        record(page, "explicit-details-default-closed", not opened,
               f"{len(details)} explicit optional details; {len(opened)} have open")
        if optional:
            scripts = "\n".join(tag.get_text() for tag in soup.find_all("script"))
            contract = all(re.search(pattern, scripts) for pattern in [
                r"automaticLongContentFolding\s*=\s*true",
                r'classList\.contains\("publisher-fold-always"\)\)\s*return\s*"always"',
                r'if\s*\(mode\s*===\s*"open"\)\s*details\.open\s*=\s*true',
                r'body\.append\(candidate\)',
            ])
            record(page, "runtime-folding-contract", contract,
                   "Embedded script wraps always-mode content in details; only open mode sets open")

    foundation = soups.get("ch-foundations")
    section = foundation.find(id="sec-foundations-simulation") if foundation else None
    missing_pending = section is None and phase == "prepare"
    record("ch-foundations", "simulation-section-visible",
           section is not None and hidden_reason(section) is None,
           "New section absent from existing build; awaiting final rebuild" if section is None
           else "Section present outside folds" if hidden_reason(section) is None
           else hidden_reason(section), pending=missing_pending)
    if section:
        equations = [tag for tag in section.select(".math.display")
                     if "s_i(t+h)" in tag.get_text() and "X_i" in tag.get_text()
                     and "\\tau" in tag.get_text() and hidden_reason(tag) is None]
        record("ch-foundations", "simulation-update-equation-visible", bool(equations),
               "Visible synaptic update equation with s_i(t+h), tau and X_i")
        for expected in ["ch-simulating-memory.html#sec-simulating-memory-state",
                         "ch-eye-drift.html"]:
            anchors = [a for a in section.find_all("a", href=True) if a["href"] == expected]
            target_name, _, fragment = expected.partition("#")
            target = site / "chapters" / target_name
            target_ok = target.is_file()
            if target_ok and fragment:
                target_soup = BeautifulSoup(target.read_text(encoding="utf-8-sig"), "html.parser")
                target_ok = target_soup.find(id=fragment) is not None
            record("ch-foundations", f"simulation-link:{expected}",
                   bool(anchors) and all(hidden_reason(a) is None for a in anchors) and target_ok,
                   "Link present outside folds and local target/fragment exists")

    now = datetime.now(timezone.utc)
    counts = {status: sum(item["status"] == status for item in results)
              for status in ["pass", "fail", "pending"]}
    return {"phase": phase, "final_acceptance": phase == "final" and not counts["fail"]
            and not counts["pending"], "checked_utc": now.isoformat(),
            "task_start_utc": TASK_START, "extension_start_utc": EXTENSION_START,
            "task_wall_seconds": (now - datetime.fromisoformat(TASK_START)).total_seconds(),
            "extension_wall_seconds": (now - datetime.fromisoformat(EXTENSION_START)).total_seconds(),
            "awake_execution_time": "unverified", "site_root": str(site),
            "page_count": len(soups), "html_sha256": hashes, "counts": counts,
            "optional_wrapper_count": optional_count,
            "explicit_optional_details_count": explicit_details_count,
            "fixture_test": fixture_test(), "checks": results,
            "limits": ["Static generated HTML and embedded folding contract; no browser or pixel sweep.",
                       "No claim of full semantic acceptance or original simulation reproduction.",
                       "Preparation is never final acceptance."]}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--site-root", type=Path,
                        default=Path(__file__).resolve().parents[2] / "site")
    parser.add_argument("--pages", nargs="+", default=DEFAULT_PAGES)
    parser.add_argument("--phase", choices=["prepare", "final"], default="final")
    parser.add_argument("--report", type=Path, required=True)
    args = parser.parse_args()
    report = check_site(args.site_root.resolve(), args.pages, args.phase)
    report["checker_sha256"] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    args.report.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps({"phase": args.phase, "page_count": report["page_count"],
                      "counts": report["counts"], "fixture_test": report["fixture_test"],
                      "final_acceptance": report["final_acceptance"],
                      "report": str(args.report.resolve())}))
    return 1 if report["counts"]["fail"] or (args.phase == "final" and report["counts"]["pending"]) else 0


if __name__ == "__main__":
    raise SystemExit(main())

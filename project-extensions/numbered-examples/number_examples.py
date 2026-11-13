"""Number rendered code and worked examples without changing authored content."""
from __future__ import annotations

import re
from bs4 import BeautifulSoup


def number_page(html: bytes, chapter: str, *, mode: str = "unified") -> tuple[bytes, list[dict]]:
    if mode not in {"unified", "separate"}:
        raise ValueError("Example numbering mode must be unified or separate")
    if not re.fullmatch(r"[A-Za-z0-9]+", chapter):
        raise ValueError("A chapter label is required")
    soup = BeautifulSoup(html.decode("utf-8"), "html.parser")
    counters = {"all": 0, "code": 0, "worked": 0}
    examples = []
    labels_by_code = {}
    for node in soup.select(".publisher-code-caption, .publisher-worked-calculation"):
        kind = "code" if "publisher-code-caption" in node.get("class", []) else "worked"
        if kind == "code":
            if node.name == "summary":
                root, title = node.parent, node
                code = root.select_one(".sourceCode[id]")
            else:
                root, title = node, node.find("p", recursive=False)
                sibling = node.find_next_sibling()
                code = sibling.select_one(".sourceCode[id]") if sibling else None
            if code is None:
                raise ValueError("Code caption has no stable listing target")
            target = code["id"]
        else:
            root = node
            title = node.find("summary", recursive=False) if node.name == "details" else node.find("p", recursive=False)
            counters["worked"] += 1
            target = root.get("id") or f"example-{chapter}-worked-{counters['worked']}"
            root["id"] = target
        if title is None or title.find("strong") is None:
            raise ValueError("Example requires a title")
        if kind == "code":
            counters["code"] += 1
        counters["all"] += 1
        number = f"{chapter}.{counters['all'] if mode == 'unified' else counters[kind]}"
        label = f"{'Code example' if mode == 'separate' and kind == 'code' else 'Example'} {number}"
        strong = title.find("strong")
        first = next((text for text in strong.find_all(string=True) if text.strip()), None)
        if first is None:
            raise ValueError("Example title is empty")
        original = title.get("data-example-original-first-text", str(first))
        title["data-example-original-first-text"] = original
        match = re.match(r"^(?:Code example|Example)(?:\s+[A-Za-z0-9]+(?:\.[A-Za-z0-9]+)*)?\s*:\s*", original)
        if match is None:
            raise ValueError(f"Unsupported example title: {original}")
        first.replace_with(f"{label}: {original[match.end():]}")
        title["data-example-label"] = label
        examples.append({"kind": kind, "label": label, "target": target})
        if kind == "code":
            labels_by_code[target] = label
    for reference in soup.select("[data-example-reference]"):
        target = reference["data-example-reference"]
        if target not in labels_by_code:
            raise ValueError(f"Reference has no numbered example: {target}")
        reference.clear()
        reference.append("See ")
        link = soup.new_tag("a", href=f"#{target}")
        link.string = labels_by_code[target]
        reference.append(link)
        reference.append(" for the implementation.")
    if len({row["label"] for row in examples}) != len(examples):
        raise ValueError("Duplicate example labels")
    if len({row["target"] for row in examples}) != len(examples):
        raise ValueError("Duplicate example targets")
    return str(soup).encode("utf-8"), examples

"""Attach local reading actions to built HTML without modifying chapter sources."""
from pathlib import Path
import hashlib
import html
import json
import os
import re
import shutil

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "assets" / "reading-actions"
START = "<!-- book-reading-actions:start -->"
END = "<!-- book-reading-actions:end -->"
BLOCK = re.compile(re.escape(START) + r".*?" + re.escape(END), re.S)


def attach_reading_actions(site: Path) -> int:
    target = site / "ask-ai-assets"
    target.mkdir(parents=True, exist_ok=True)
    versions = {}
    for name in ("ask-ai.js", "ask-ai.css"):
        payload = (SOURCE / name).read_bytes()
        (target / name).write_bytes(payload)
        versions[name] = hashlib.sha256(payload).hexdigest()[:12]
    config = json.dumps({
        "endpoint": "https://course-ask-ai.course-ask-ai-backend.workers.dev/ask",
        "book": "neural-codes-noise-memory",
        "bookTitle": "Neural Codes, Noise, and Memory",
        "reporting": {"enabled": True},
    }, ensure_ascii=True).replace("<", "\\u003c").replace(">", "\\u003e").replace("&", "\\u0026")
    count = 0
    for page in sorted(site.rglob("*.html")):
        if "site_libs" in page.parts:
            continue
        source = page.read_text(encoding="utf-8")
        if not re.search(r"<main\b", source, re.I):
            continue
        prefix = html.escape(Path(os.path.relpath(target, page.parent)).as_posix(), quote=True)
        addition = (f'{START}\n<link rel="stylesheet" href="{prefix}/ask-ai.css?v={versions["ask-ai.css"]}">\n'
                    f'<script id="book-ask-ai-config" type="application/json">{config}</script>\n'
                    f'<script defer src="{prefix}/ask-ai.js?v={versions["ask-ai.js"]}"></script>\n{END}')
        if START in source:
            if not BLOCK.search(source):
                raise ValueError(f"Incomplete reading-action markers: {page}")
            updated = BLOCK.sub(lambda _: addition, source)
        else:
            updated, n = re.subn(r"</body\s*>", lambda match: addition + "\n" + match.group(), source, count=1, flags=re.I)
            if n != 1:
                raise ValueError(f"No body end in {page}")
        if updated != source:
            page.write_text(updated, encoding="utf-8", newline="\n")
        count += 1
    return count

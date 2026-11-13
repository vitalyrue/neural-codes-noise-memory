"""Recalculate plot checks after metadata edits and prove rendered bytes stayed fixed."""
from pathlib import Path
from datetime import datetime
import hashlib, importlib.util, json, sys
OUT = Path(__file__).resolve().parent
ROOT = OUT.parents[1]
group = sys.argv[1] if len(sys.argv) > 1 else 'foundations'
filename, numbers = {'foundations': ('draw_foundations_information.py', range(1,5)),
                     'eye-place': ('draw_eye_place.py', range(5,9))}[group]
spec = importlib.util.spec_from_file_location('refresh_figure_module', OUT / filename)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
def digest(p): return hashlib.sha256(p.read_bytes()).hexdigest()
record = []
for n in numbers:
    aid = f'A{n:02}'
    folder = ROOT / f'candidate-content/visuals/candidates/20261024-all/{aid}'
    before = {name: digest(folder / name) for name in ['figure.png', 'figure.svg', 'book-width.png']}
    getattr(module, aid.lower())()
    after = {name: digest(folder / name) for name in before}
    assert before == after, f'Unexpected image change: {aid}'
    qa = json.loads((folder / 'qa.json').read_text(encoding='utf-8'))
    assert qa['status'] == 'pass' and qa['spec_sha256'] == digest(OUT / filename)
    record.append({'id': aid, 'unchanged_image_bytes': before, 'status': qa['status'], 'spec_sha256': qa['spec_sha256']})
result = {'at': datetime.now().astimezone().isoformat(), 'reason': 'Recheck after caption metadata edits; no plot code changes.', 'figures': record}
(OUT / f'{group}-metadata-recheck.json').write_text(json.dumps(result, indent=2), encoding='utf-8')
print(json.dumps({'at': result['at'], 'group': group, 'figures': len(record), 'identical_png_svg_and_preview': True}))

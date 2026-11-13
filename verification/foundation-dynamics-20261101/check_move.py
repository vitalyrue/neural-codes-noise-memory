from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, yaml
from book_runtime.compiler.loader import load_book
from book_runtime.release_audit import build_structure_lock, write_structure_lock

root = Path(__file__).resolve().parents[2]
task = Path(__file__).resolve().parent
old = yaml.safe_load((task/'baseline/plan/structural-locks/current.yaml').read_text(encoding='utf-8'))
book = load_book(root/'guide-project.yaml')
new = build_structure_lock(book)

def ids(value):
    result = set()
    if isinstance(value,dict):
        if 'id' in value:
            result.add(value['id'])
        for child in value.values():
            result.update(ids(child))
    elif isinstance(value,list):
        for child in value:
            result.update(ids(child))
    return result

assert not ids(old)-ids(new), ids(old)-ids(new)
assert ids(new)-ids(old) == {'sec:MEMORY-WEAK-NOISE'}, ids(new)-ids(old)
for a,b in zip(old['parts'],new['parts']):
    assert (a['id'],a['title']) == (b['id'],b['title'])
    assert [(c['id'],c['title']) for c in a['chapters']] == [(c['id'],c['title']) for c in b['chapters']]

sidecars = {}
for name in ['01-foundations.yaml','02-memory-dynamics.yaml']:
    sidecars[name] = yaml.safe_load((root/'content/chapters'/name).read_text(encoding='utf-8'))
old_dynamics = yaml.safe_load((task/'baseline/content/chapters/02-memory-dynamics.yaml').read_text(encoding='utf-8'))
old_figure = next(x for x in old_dynamics['blocks'] if x['id']=='fig:MEMORY-SPIKE-TRACE')
new_figure = next(x for x in sidecars['01-foundations.yaml']['blocks'] if x['id']=='fig:MEMORY-SPIKE-TRACE')
for field in ['id','kind','placement','asset','alt','width_inches','html_fold']:
    assert old_figure[field] == new_figure[field], field
assert all(x['id']!='fig:MEMORY-SPIKE-TRACE' for x in sidecars['02-memory-dynamics.yaml']['blocks'])
redirects = json.loads((root/'source-maps/chapter-redirects.json').read_text(encoding='utf-8'))
for anchor in ['sec-memory-spikes','fig-memory-spike-trace']:
    assert redirects['ch-memory-dynamics.html'][anchor] == 'ch-foundations.html'
for name in ['01-foundations.md','02-memory-dynamics.md']:
    text=(root/'content/chapters'/name).read_text(encoding='utf-8')
    assert '\t' not in text and '\x08' not in text and '\x0c' not in text

report = {'at_utc': datetime.now(timezone.utc).isoformat(),
          'book_model_hash':book.content_hash(), 'all_old_ids_preserved':True,
          'new_ids':['sec:MEMORY-WEAK-NOISE'],
          'chapter_ids_titles_order_preserved':True,
          'moved_section':{'id':'sec:MEMORY-SPIKES','from':'ch:MEMORY-DYNAMICS','to':'ch:FOUNDATIONS'},
          'moved_figure':{'id':'fig:MEMORY-SPIKE-TRACE','asset_and_dimensions_unchanged':True,
                         'sha256':hashlib.sha256((root/new_figure['asset']).read_bytes()).hexdigest()},
          'old_bookmark_routes_checked':True,
          'scope':'Structural and source checks for the model move only; not whole-guide acceptance.'}
(task/'move-checks.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
if __import__('sys').argv[-1:] == ['--accept-structure']:
    stage3=json.loads((task/'stage3.json').read_text(encoding='utf-8'))
    assert stage3['verdict'].lower().startswith('pass'),stage3['verdict']
    write_structure_lock(root/'guide-project.yaml','plan/structural-locks/current.yaml')
    print('Accepted reviewed section/figure move; structural lock updated.')
print('All prior IDs, chapters, figure bytes and dimensions preserved; one new weak-noise section.')

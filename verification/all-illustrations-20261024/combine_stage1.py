"""Bind independently judged Stage1 candidate assets; no source acceptance claim."""
from pathlib import Path
import json, hashlib
from datetime import datetime
ROOT=Path(__file__).resolve().parents[2]
HERE=Path(__file__).resolve().parent
def read(p): return json.loads(p.read_text(encoding='utf-8-sig'))
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
result=dict(reviewer='/root/all_illustrations_review',coordinating_reviewer='/root/all_illustrations_review',
    created_at=datetime.now().astimezone().isoformat(),
    scope='Stage1 independent candidate figure correctness and pixel criteria only; final source binding and Stage2/3 pending',figures={})
sources=[('stage1-A01-A04.json',None),('stage1-A05-A08.json',None),('stage1-A09.json','A09')]
for filename,single in sources:
    report=read(HERE/filename)
    if single: rows={single:report}
    elif isinstance(report['figures'],list): rows={r['id']:r for r in report['figures']}
    else: rows=report['figures']
    for id,row in rows.items():
        criteria=row.get('checks',row.get('criteria',{}))
        assert all(criteria[c]['verdict']=='pass' for c in ['technical_accuracy','visual_explanation','readability','palette']),(id,'failed criterion')
        assert criteria['coverage']['verdict']=='not-applicable'
        assert not row.get('findings',row.get('unresolved_findings',[])),(id,'unresolved findings')
        reviewer=row.get('reviewer',report['reviewer'])
        assert reviewer!=row.get('author'),(id,'author conflict')
        png=row.get('png_sha256',row.get('reviewed_png_sha256'))
        svg=row.get('svg_sha256',row.get('reviewed_svg_sha256'))
        folder=ROOT/'candidate-content/visuals/candidates/20261024-all'/id
        assert sha(folder/'figure.png')==png and sha(folder/'figure.svg')==svg,(id,'asset changed')
        if not single: assert row['decision']=='pass'
        result['figures'][id]=dict(decision='pass',png_sha256=png,svg_sha256=svg,reviewer=reviewer,report=str((HERE/filename).relative_to(ROOT)).replace('\\','/'))
assert sorted(result['figures'])==['A01','A02','A03','A04','A05','A06','A07','A08','A09']
(HERE/'stage1-approved.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
print(json.dumps({'created_at':result['created_at'],'figures':len(result['figures']),'reviewers':sorted(set(r['reviewer'] for r in result['figures'].values()))}))

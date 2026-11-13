"""Freeze source identities and a closed-fold reading copy for the review round."""
from pathlib import Path
from datetime import datetime
import hashlib,json,re,sys
OUT=Path(__file__).resolve().parent
ROOT=OUT.parents[1]
label=sys.argv[1] if len(sys.argv)>1 else 'v1'
prop=OUT/'proposed'
files=sorted((prop/'content/chapters').glob('*'))+[prop/'plan/chapter-plan.yaml']
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
frozen={'at':datetime.now().astimezone().isoformat(),'label':label,
        'sources':{p.relative_to(OUT).as_posix():sha(p) for p in files if p.is_file()},
        'review_scope':'Title contributions, selected folds, paragraph order and connected claims in the six teaching chapters, orientation and Part openings. Original math and images retained. No new empirical reproduction.'}
(OUT/f'frozen-{label}.json').write_text(json.dumps(frozen,indent=2),encoding='utf-8')
dest=OUT/'first-pass'
dest.mkdir(exist_ok=True)
for p in (prop/'content/chapters').glob('*.md'):
    text=p.read_text(encoding='utf-8')
    closed=re.sub(r'^::: \{\.publisher-clarification-note \.publisher-fold-always title="([^"]+)"\}\n.*?^:::\s*$',r'**Expandable note: \1**',text,flags=re.M|re.S)
    (dest/p.name).write_text(closed,encoding='utf-8')
print(json.dumps({'at':frozen['at'],'files':len(frozen['sources']),'label':label}))

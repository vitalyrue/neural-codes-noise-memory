from pathlib import Path
from datetime import datetime
from collections import Counter
import re, json, hashlib, difflib

folder=Path(__file__).resolve().parent
chapters=folder.parents[1]/'content/chapters'
ledger=json.loads((folder/'edits-information.json').read_text(encoding='utf-8'))
report={'at':datetime.now().astimezone().isoformat(),'scope':'Assigned two chapters only','awake_execution':'unverified','files':[]}
patterns={
 'headings':r'^#{1,2} .+$',
 'display_equations':r'\$\$.*?\$\$',
 'definitions':r'\[\*\*.*?\*\*\]\{\.definition-term[^}]*\}',
 'figure_blocks':r'\{\{block:.*?\}\}',
 'reference_targets':r'\]\(([^)]+)\)',
 'footnote_definitions':r'^\[\^[^]]+\]:.*$',
 'footnote_uses':r'\[\^[^]]+\]',
 'fold_titles':r'^::: \{[^\n]*title="[^"]*"[^\n]*\}',
}
for f in ledger['files']:
    name=Path(f['file']).name
    current=(chapters/name).read_text(encoding='utf-8')
    old=f['old']
    checks={}
    for key,pattern in patterns.items():
        before=re.findall(pattern,old,re.M|re.S if key in ['display_equations','definitions'] else re.M)
        after=re.findall(pattern,current,re.M|re.S if key in ['display_equations','definitions'] else re.M)
        checks[key]={'before':len(before),'after':len(after),'same_content':Counter(before)==Counter(after)}
    assert all(c['same_content'] for c in checks.values()), (name,checks)
    # The ledger records every old block; add all destinations of its retained
    # complete sentences, including paragraphs split into two new paragraphs.
    new_blocks=[b for b in re.split(r'\n\s*\n',current) if b.strip()]
    for item in f['items']:
        destinations={item['new_item']}
        for sentence in re.split(r'(?<=[.!?])\s+',item['old']):
            if len(sentence)>45:
                destinations.update(i+1 for i,b in enumerate(new_blocks) if sentence in b)
        item['new_items']=sorted(destinations)
        item['new_segments']=[{'item':i,'text':new_blocks[i-1]} for i in sorted(destinations)]
    sha=hashlib.sha256((chapters/name).read_bytes()).hexdigest()
    assert sha==f['new_sha256']
    report['files'].append({'file':name,'sha256':sha,'inventories':checks,'old_blocks_accounted':len(f['items']),
      'author_connected_reread':'Completed; checked openings, moved proofs, definitions before use, network applications, examples, source cautions, and limits. Independent review pending.'})
ledger['status']='Applied; exact final hashes verified; every original block has destinations. Independent review pending.'
ledger['verified_at']=report['at']
(folder/'edits-information.json').write_text(json.dumps(ledger,ensure_ascii=False,indent=2),encoding='utf-8')
(folder/'checks-information.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
checkpoint={'at':report['at'],'stage':'information authoring and preservation checks complete','overall_started':'2026-10-28T16:44:38+02:00','local_started':'2026-10-28T16:52:03.6705118+02:00','previous_checkpoint':'2026-10-28T16:55:39.9319792+02:00','awake_execution':'unverified','independent_review':'pending'}
with (folder/'checkpoints-information.jsonl').open('a',encoding='utf-8') as stream:
    stream.write(json.dumps(checkpoint)+'\n')
print(json.dumps(report,indent=2))

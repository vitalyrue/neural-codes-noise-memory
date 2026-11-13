from pathlib import Path
import re,json,hashlib,datetime
import yaml
BASE=Path('C:/dev/clsc/burak-papers/guide')
TASK=BASE/'verification/teaching-flow-20261024'; G=TASK/'information-eye'; OUT=TASK/'proposed/content/chapters'
def sha(b):return hashlib.sha256(b).hexdigest()
hashes={}; checks=[]
for stem in ['03-memory-information','04-eye-drift']:
    src=BASE/'content/chapters'/f'{stem}.md'; prop=OUT/src.name
    s=src.read_text(encoding='utf-8'); p=prop.read_text(encoding='utf-8')
    sy=src.with_suffix('.yaml'); py=prop.with_suffix('.yaml')
    ys=yaml.safe_load(sy.read_text(encoding='utf-8')); yp=yaml.safe_load(py.read_text(encoding='utf-8'))
    assert ys['blocks']==yp['blocks']
    assert sorted(re.findall(r'\$\$(.*?)\$\$',s,re.S))==sorted(re.findall(r'\$\$(.*?)\$\$',p,re.S))
    assert sorted(re.findall(r'\]\(([^)]+)\)',s))==sorted(re.findall(r'\]\(([^)]+)\)',p))
    headings=re.findall(r'^#+ (.*?) \{#([^}]+)\}$',p,re.M)
    assert headings[0][0]==yp['title']
    lookup={anchor:title for title,anchor in headings}
    assert all(lookup[r['id']]==r['title'] for r in yp['section_list'])
    foldspans=re.findall(r'^::: \{\.publisher-clarification-note \.publisher-fold-always title="[^"]+"\}\n\n(.*?)\n\n:::$',p,re.M|re.S)
    assert len(foldspans)==2
    assert all('{{block:' not in span and '.definition-term' not in span and not re.search(r'^#+ ',span,re.M) and ':::' not in span for span in foldspans)
    hashes[stem]={}
    for kind,a,b in [('md',src,prop),('yaml',sy,py)]:
        hashes[stem][f'source_{kind}']=sha(a.read_bytes())
        hashes[stem][f'proposed_{kind}']=sha(b.read_bytes())
        hashes[stem][f'source_{kind}_normalized_text']=sha(a.read_text(encoding='utf-8').encode())
        hashes[stem][f'proposed_{kind}_normalized_text']=sha(b.read_text(encoding='utf-8').encode())
    checks.append(dict(chapter=stem,display_math_preserved=True,all_reader_link_destinations_preserved=True,typed_blocks_unchanged=True,sidecar_titles_match=True,fold_count=2,no_nested_folds_or_hidden_first_definition_or_typed_block=True))
(G/'hashes.json').write_text(json.dumps(hashes,indent=2)+'\n',encoding='utf-8')
stamp=datetime.datetime.now().astimezone().isoformat()
findings=[dict(id='AUTHOR-FLOW-01',file='04-eye-drift.md',locus='Optional coefficient derivation, original paragraph at line 107',kind='necessary connection repair after move',before='Making the response zero before the spike gives',proposed='Making the response zero before the spike gives the impulse response displayed above.',status='open; reported to root after freeze; no author edit to frozen reader file')]
(G/'author-findings.json').write_text(json.dumps(findings,indent=2)+'\n',encoding='utf-8')
(G/'verification.json').write_text(json.dumps(dict(timestamp=stamp,checks=checks,limits=['No independent truth/wording/reader-flow verdict by this author.','No new source findings or numerical claims introduced. Original formulas preserved, not a new mathematical audit.','No rendered output sweep run. Root handles representative folding/render checks.'],open_findings=findings),indent=2)+'\n',encoding='utf-8')
status=dict(timestamp=stamp,root_start='2026-10-24T18:54:22.5524387+03:00',frozen_at='2026-10-24T19:03:36.4353058+03:00',model='GPT-6.1-sol/high allocation',stage='author draft frozen; exact decisions and preservation checks complete; one flow finding awaits root',awake_execution='unverified',tokens='unavailable')
(G/'status.json').write_text(json.dumps(status,indent=2)+'\n',encoding='utf-8')
print(json.dumps(dict(timestamp=stamp,checks=checks,open_findings=len(findings)),indent=2))

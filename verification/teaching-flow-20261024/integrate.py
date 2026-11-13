"""Apply reviewed teaching-flow proposals, preserving stable content identities."""
from pathlib import Path
from datetime import datetime
from collections import Counter
import copy, difflib, hashlib, json, re, sys, yaml

ROOT=Path(__file__).resolve().parents[2]
OUT=Path(__file__).resolve().parent
BASE=OUT/'baseline'
PROP=OUT/'proposed'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
read=lambda p:p.read_text(encoding='utf-8')
sources=json.loads(read(BASE/'hashes.json'))
records=[]
expectations=[]
pending=[]
check_only='--check-only' in sys.argv
render_preview='--render-preview' in sys.argv
if not check_only and not render_preview:
    assert json.loads(read(OUT/'acceptance.json'))['status']=='accepted for this local revision'
for p in sorted((PROP/'content/chapters').glob('*.md')):
    rel=p.relative_to(PROP)
    current=ROOT/rel
    assert sha(current)==sources['sources'][rel.as_posix()],f'Concurrent source change: {rel}'
    old=read(current); new=read(p)
    ids=lambda s:Counter(re.findall(r'\{#([^}]+)\}',s))
    assert ids(old)==ids(new),f'Anchor changed: {rel}'
    refs=lambda s:Counter(re.findall(r'\{\{block:[^}]+\}\}',s))
    assert refs(old)==refs(new),f'Figure/table reference changed: {rel}'
    links=lambda s:Counter(re.findall(r'\]\(([^)]+)\)',s))
    assert not (links(old)-links(new)),f'Link removed: {rel}'
    math=lambda s:Counter(re.findall(r'\$\$(.*?)\$\$',s,re.S))
    assert not (math(old)-math(new)),f'Original display math removed: {rel}'
    marked=lambda s:Counter(re.findall(r'\[\*\*(.*?)\*\*\]\{\.definition-term',s))
    assert marked(old)==marked(new),f'First definition changed: {rel}'
    foldmatches=list(re.finditer(r'^::: \{\.publisher-clarification-note \.publisher-fold-always title="([^"]+)"\}\n(.*?)^:::\s*$',new,re.M|re.S))
    assert new.count('.publisher-fold-always')==len(foldmatches),f'Unparsed fold: {rel}'
    for fold in foldmatches:
        assert not any(x in fold.group(2) for x in ['.definition-term','{{block:',':::']),fold.group(1)
        assert not re.search(r'^#{1,6} ',fold.group(2),re.M),fold.group(1)
    meta_text=read(p.with_suffix('.yaml'))
    meta=yaml.safe_load(meta_text)
    proposed_meta=copy.deepcopy(meta)
    oldmeta=yaml.safe_load(read(current.with_suffix('.yaml')))
    assert meta.get('blocks',[])==oldmeta.get('blocks',[]),f'Old typed content changed: {rel}'
    for block in meta.get('blocks',[]):
        if block.get('kind') in ['table','code','callout','worked_calculation','clarification_note']:
            block['html_fold']='never'
    headings=[{'level':len(m[0]),'title':m[1],'id':m[2]} for m in re.findall(r'^(#{1,6}) (.+) \{#([^}]+)\}$',new,re.M)]
    assert meta['title']==headings[0]['title'],rel
    assert [(s['id'],s['title']) for s in meta['section_list']]==[(h['id'],h['title']) for h in headings[1:]],rel
    delta=list(difflib.ndiff(old.splitlines(keepends=True),new.splitlines(keepends=True)))
    assert ''.join(difflib.restore(delta,1))==old and ''.join(difflib.restore(delta,2))==new
    old_headings={m[1]:m[0] for m in re.findall(r'^#{1,6} (.+) \{#([^}]+)\}$',old,re.M)}
    records.append({'path':rel.as_posix(),'before_sha256':sha(current),'after_sha256':sha(p),
      'headings':headings,'folds':[{'title':f.group(1),'line':new[:f.start()].count('\n')+1,'text':f.group(2)} for f in foldmatches],
      'heading_changes':[{'id':h['id'],'before':old_headings[h['id']],'after':h['title']} for h in headings if old_headings[h['id']]!=h['title']],
      'preserved':['all stable anchors','all original display equations','all old links','all first-definition spans','all figure/table references','all old typed content'],
      'reversible_line_diff':delta})
    folder='frontmatter' if meta.get('role')=='frontmatter' else 'chapters'
    expectations.append({'chapter':meta['chapter_id'],'url':f"{folder}/{meta['chapter_id'].replace(':','-').lower()}.html",
      'folds':[f.group(1) for f in foldmatches],
      'figures':sum(b.get('kind')=='figure' for b in meta.get('blocks',[])),
      'tables':sum(b.get('kind')=='table' for b in meta.get('blocks',[])), 'title':meta['title']})
    final_meta_text=meta_text if meta==proposed_meta else yaml.safe_dump(meta,allow_unicode=True,sort_keys=False,width=84)
    pending.extend([(current,new),(current.with_suffix('.yaml'),final_meta_text)])

plan=ROOT/'plan/chapter-plan.yaml'
assert sha(plan)==sources['sources']['plan/chapter-plan.yaml']
pending.append((plan,read(PROP/'plan/chapter-plan.yaml')))
config_path=ROOT/'guide-project.yaml'
assert sha(config_path)==sources['sources']['guide-project.yaml']
config=yaml.safe_load(read(config_path))
config['publication']['renderers']['quarto']['html_folding']['enabled']=True
pending.append((config_path,yaml.safe_dump(config,allow_unicode=True,sort_keys=False,width=84)))
for rel,digest in sources['approved_assets'].items():
    assert sha(ROOT/rel)==digest,rel
if check_only:
    result={'at':datetime.now().astimezone().isoformat(),'status':'pass','chapters':len(records),
       'changed_chapter_and_section_titles':sum(len(r['heading_changes']) for r in records),
       'folds':sum(len(r['folds']) for r in records),'records':records,
       'approved_assets_unchanged':len(sources['approved_assets'])}
    (OUT/'preflight.json').write_text(json.dumps(result,indent=2,ensure_ascii=False),encoding='utf-8')
    print(json.dumps({k:v for k,v in result.items() if k!='records'}))
    raise SystemExit(0)
for path,content in pending:
    path.write_text(content,encoding='utf-8',newline='\n')

# Refresh line locators only; do not treat metadata maintenance as new review.
tp=ROOT/'source-maps/terminology-ledger.yaml'
terms=yaml.safe_load(read(tp))
locators={}
for p in (ROOT/'content/chapters').glob('*.md'):
    section=''
    for n,line in enumerate(read(p).splitlines(),1):
        match=re.search(r'\{#((?:ch|sec):[^}]+)\}',line)
        if match:section=match.group(1)
        for term in re.findall(r'\[\*\*(.*?)\*\*\]\{\.definition-term',line):
            locators[(p.relative_to(ROOT).as_posix(),term)]=(n,section)
updated=0
for row in terms.get('first_teaching',[]):
    key=(row['source'],row['term'])
    if key in locators:
        line,section=locators[key]
        if row['line']!=line or row['guide_location']!=section:updated+=1
        row.update(line=line,guide_location=section)
tp.write_text(yaml.safe_dump(terms,allow_unicode=True,sort_keys=False,width=84),encoding='utf-8')
for rel,digest in sources['approved_assets'].items():
    assert sha(ROOT/rel)==digest,rel

result={'at':datetime.now().astimezone().isoformat(),'records':records,'term_locators_updated':updated,
 'render_preview_before_final_reading_flow_acceptance':render_preview,
 'approved_assets_unchanged':len(sources['approved_assets']),'status':'source checks passed; rendering and independent acceptance recorded separately'}
(OUT/'integration.json').write_text(json.dumps(result,indent=2,ensure_ascii=False),encoding='utf-8')
(OUT/'render-expectations.json').write_text(json.dumps({'pages':expectations},indent=2,ensure_ascii=False),encoding='utf-8')
print(json.dumps({'at':result['at'],'chapters':len(records),'folds':sum(len(r['folds']) for r in records),'term_locators_updated':updated}))

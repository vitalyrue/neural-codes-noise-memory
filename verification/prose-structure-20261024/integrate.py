from pathlib import Path
from datetime import datetime
import json,re,hashlib,yaml
from bs4 import BeautifulSoup
OUT=Path(__file__).resolve().parent;ROOT=OUT.parents[1];P=OUT/'proposed/content/chapters'
read=lambda p:p.read_text(encoding='utf-8');load=lambda p:json.loads(read(p));sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
assert load(OUT/'draft-check.json')['status']=='pass'
groups=['foundations-synthesis','information-eye','place']
for group in groups:
 for stage in [1,2,3]:
  result=load(OUT/f'stage{stage}-{group}.json')
  if stage==3:
   for key in ['defects','findings','unresolved_findings','unresolved_questions']:assert not result.get(key),(group,key)
base=load(OUT/'baseline/hashes.json');metrics=[];records=[]
for p in P.glob('*.md'):
 rel=Path('content/chapters')/p.name;canonical=ROOT/rel
 assert sha(canonical)==base['sources'][rel.as_posix()],rel
 before=read(canonical);after=read(p);meta=yaml.safe_load(read(canonical.with_suffix('.yaml')))
 page=('frontmatter/' if meta['role']=='frontmatter' else 'appendices/' if meta['role']=='appendix' else 'chapters/')+meta['chapter_id'].lower().replace(':','-')+'.html'
 oldhtml=ROOT/'site'/page
 if oldhtml.exists():
  soup=BeautifulSoup(read(oldhtml),'html.parser');main=soup.select_one('main')
  lists=[e for e in main.select('ul,ol') if not e.find_parent('section',class_='footnotes') and not e.find_parent(attrs={'role':'doc-endnotes'})]
  metrics.append({'chapter':meta['chapter_id'],'url':page,'lists':len(lists),'list_items':sum(len(e.find_all('li',recursive=False)) for e in lists),'definitions':len(main.select('.definition-term'))})
 canonical.write_bytes(p.read_bytes())
 # Sidecar summaries follow the actual revised introductory paragraphs; scientific blocks stay exact.
 opening=after.split('\n\n',2)[1];meta['purpose']=opening
 for section in meta.get('section_list',[]):
  m=re.search(r'(?m)^#{2,6} .+? \{#'+re.escape(section['id'])+r'\}\s*\n',after)
  if m:section['summary']=after[m.end():].strip().split('\n\n')[0]
 canonical.with_suffix('.yaml').write_text(yaml.safe_dump(meta,allow_unicode=True,sort_keys=False,width=88),encoding='utf-8',newline='\n')
 records.append({'file':rel.as_posix(),'chapter':meta['chapter_id'],'url':page,'before_sha256':hashlib.sha256(before.encode()).hexdigest(),'after_sha256':sha(canonical),'proposed_sha256':sha(p),'figures':sum(b['kind']=='figure' for b in meta.get('blocks',[])),'tables':sum(b['kind']=='table' for b in meta.get('blocks',[]))})

# Rebuild definition locations from the actual reading order, including glossary lookup entries.
plan=yaml.safe_load(read(ROOT/'plan/chapter-plan.yaml'))['book']
order=plan['front_matter']+[c for part in plan['parts'] for c in part['chapters']]+plan['appendices']
byid={yaml.safe_load(read(p))['chapter_id']:p.with_suffix('.md') for p in (ROOT/'content/chapters').glob('*.yaml')}
terms=[]
for chapter in order:
 p=byid[chapter];locus=chapter
 for number,line in enumerate(read(p).splitlines(),1):
  h=re.search(r'^#{1,6} .*\{#([^}]+)\}',line)
  if h:locus=h.group(1)
  for term in re.findall(r'\[\*\*([^*]+)\*\*\]\{\.definition-term[^}]*\}',line):terms.append({'term':term.rstrip(':'),'source':p.relative_to(ROOT).as_posix(),'line':number,'guide_location':locus})
ledger={'schema_version':1,'note':'Marked first teaching occurrences and glossary entries, extracted from actual current text. Meaning and reading order are assessed in the separate review stages for this local prose revision.','first_teaching':terms,'terms':terms}
(ROOT/'source-maps/terminology-ledger.yaml').write_text(yaml.safe_dump(ledger,allow_unicode=True,sort_keys=False,width=88),encoding='utf-8',newline='\n')
(OUT/'integration.json').write_text(json.dumps({'at':datetime.now().astimezone().isoformat(),'records':records},indent=2),encoding='utf-8')
(OUT/'baseline-html-metrics.json').write_text(json.dumps(metrics,indent=2),encoding='utf-8')
layout=load(ROOT/'verification/chapter-size-20261024/integration.json');(OUT/'layout.json').write_text(json.dumps(layout,indent=2),encoding='utf-8')
print(json.dumps({'integrated_files':len(records),'definition_locations':len(terms),'at':datetime.now().astimezone().isoformat()}))

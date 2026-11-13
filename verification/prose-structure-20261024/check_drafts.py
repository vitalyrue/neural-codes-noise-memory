from pathlib import Path
from datetime import datetime
from collections import Counter,defaultdict
import hashlib,json,re
OUT=Path(__file__).resolve().parent;ROOT=OUT.parents[1];P=OUT/'proposed/content/chapters'
read=lambda p:p.read_text(encoding='utf-8');load=lambda p:json.loads(read(p));sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
steps=[]
for name in ['changes-foundations-memory.json','changes-information-eye.json','changes-place.json']:
 ledger=load(OUT/name)
 for row in ledger.get('chapters',ledger.get('files',[])):
  rel='content/chapters/'+Path(row['source_path']).name
  for e in row['edits']:steps.append({'file':rel,'before':e.get('before',e.get('old')),'after':e.get('after',e.get('new')),'kind':e['kind'],'ledger':name})
for name in ['changes-root.json','coordinator-edits.json']:
 for e in load(OUT/name)['edits']:steps.append({**e,'ledger':name})
for name in ['review-repairs.json']:
 if (OUT/name).exists():steps+=load(OUT/name)['edits']
reconstructed={p.name:read(OUT/'baseline/content/chapters'/p.name) for p in P.glob('*.md')}
for e in steps:
 file=Path(e['file']).name;t=reconstructed[file]
 assert t.count(e['before'])==1,(file,e['before'][:90],t.count(e['before']))
 reconstructed[file]=t.replace(e['before'],e['after'])
rows=[]
extract=lambda pattern,t:re.findall(pattern,t,re.M|re.S)
definitions=defaultdict(list)
for p in P.glob('*.md'):
 before=read(OUT/'baseline/content/chapters'/p.name);after=read(p);checks={}
 checks['exact_ledger_reconstruction']=reconstructed[p.name]==after
 checks['headings']=re.findall(r'^#{1,6} .*$',before,re.M)==re.findall(r'^#{1,6} .*$',after,re.M)
 checks['block_markers']=re.findall(r'\{\{block:[^}]+\}\}',before)==re.findall(r'\{\{block:[^}]+\}\}',after)
 checks['display_math']=extract(r'^\$\$\s*\n(.*?)^\$\$',before)==extract(r'^\$\$\s*\n(.*?)^\$\$',after)
 if p.name!='glossary.md':
  # Math expressions may move into list items, but their spelling and count stay fixed.
  inline=lambda t:Counter(re.findall(r'(?<!\$)\$(?!\$)([^\n$]+)\$(?!\$)',t))
  expected_inline=inline(before)
  # The readout split now identifies its two list items by the existing equation terms.
  # Both formulas already occur in the unchanged equation; no calculation changes.
  if p.name=='03b-memory-readout.md':expected_inline.update({'V_{\\mathrm{read}}(L)':1,'2DT':1})
  checks['inline_math']=expected_inline==inline(after)
  checks['footnote_definitions']=extract(r'^\[\^[^\]]+\]:.*?(?=^\[\^[^\]]+\]:|\Z)',before)==extract(r'^\[\^[^\]]+\]:.*?(?=^\[\^[^\]]+\]:|\Z)',after)
  checks['link_targets']=Counter(re.findall(r'\]\(([^)]+)\)',before))==Counter(re.findall(r'\]\(([^)]+)\)',after))
  checks['fold_titles']=re.findall(r'^:::.*publisher-fold-always.*$',before,re.M)==re.findall(r'^:::.*publisher-fold-always.*$',after,re.M)
  for m in re.finditer(r'\[\*\*([^*]+)\*\*\]\{\.definition-term[^}]*\}',after):definitions[m.group(1).casefold()].append({'file':p.name,'line':after[:m.start()].count('\n')+1})
 row={'file':p.name,'sha256':sha(p),'checks':checks,'status':'pass' if all(checks.values()) else 'fail'}
 if checks.get('inline_math') is False:row['inline_math_difference']={'removed':dict(inline(before)-inline(after)),'added':dict(inline(after)-inline(before))}
 rows.append(row)
gloss={m.casefold() for m in re.findall(r'^- \[\*\*([^*]+):\*\*\]',read(P/'glossary.md'),re.M)}
missing_gloss=sorted(set(definitions)-gloss);duplicates={k:v for k,v in definitions.items() if len(v)>1}
baseline=load(OUT/'baseline/hashes.json');assets=all(sha(ROOT/p)==h for p,h in baseline['assets'].items())
report={'at':datetime.now().astimezone().isoformat(),'rows':rows,'recorded_edits':len(steps),'definition_terms':len(definitions),'inline_math_note':'Readout list labels repeat existing V_read(L) and 2DT once each; every original expression remains. New glossary entries repeat their teaching formulas.','missing_glossary_entries':missing_gloss,'duplicate_first_definition_marks':duplicates,'approved_assets_unchanged':assets,'status':'pass' if all(r['status']=='pass' for r in rows) and not missing_gloss and not duplicates and assets else 'fail'}
(OUT/'draft-check.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
(OUT/'all-edits.json').write_text(json.dumps(steps,indent=2,ensure_ascii=False),encoding='utf-8')
print(json.dumps({'status':report['status'],'files':len(rows),'edits':len(steps),'definition_terms':len(definitions),'missing_glossary_entries':missing_gloss,'duplicates':duplicates,'failures':[r for r in rows if r['status']!='pass']},indent=2))
raise SystemExit(0 if report['status']=='pass' else 1)

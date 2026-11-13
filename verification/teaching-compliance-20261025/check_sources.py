from pathlib import Path
from datetime import datetime
import hashlib,json,csv,re,yaml,concurrent.futures,urllib.request,urllib.error
OUT=Path(__file__).resolve().parent;ROOT=OUT.parents[1];P=OUT/'proposed'
read=lambda p:p.read_text(encoding='utf-8');sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
plan=yaml.safe_load(read(ROOT/'plan/chapter-plan.yaml'))['book'];order=plan['front_matter']+[c for part in plan['parts'] for c in part['chapters']]+plan['appendices']
byid={yaml.safe_load(read(p))['chapter_id']:p.with_suffix('.md') for p in (P/'content/chapters').glob('*.yaml')}
ids=set();urls=set();cited=set();undefined=[];unused=[];first=[]
norm=lambda s:s.lower().replace(':','-')
doi=lambda s:re.findall(r'https://doi\.org/(10\.[^\s\]<>]+)',s)
def clean(s):return s.rstrip(').,;')
for cid in order:
 p=byid[cid];text=read(p)
 ids.update(norm(s) for s in re.findall(r'\{#([^}]+)\}',text));ids.update(norm(s) for s in re.findall(r'\{\{block:([^}]+)\}\}',text))
 defs=dict(re.findall(r'^\[\^([^\]]+)\]:\s*(.*)$',text,re.M));body=re.sub(r'^\[\^[^\]]+\]:.*$','',text,flags=re.M)
 calls=re.findall(r'\[\^([^\]]+)\]',body)
 undefined +=[(p.name,k) for k in calls if k not in defs]
 unused +=[(p.name,k) for k in defs if k not in calls]
 for k in calls:
  for d in doi(defs[k]):
   d=clean(d);cited.add(d)
   if d not in first:first.append(d)
 urls.update(clean(u) for u in re.findall(r'https?://[^\s<>\]]+',text))
refs=read(P/'content/chapters/references.md');listed=[clean(s) for s in doi(refs)]
missing_ref=sorted(cited-set(listed));unused_ref=sorted(set(listed)-cited)
inventory=list(csv.DictReader((ROOT/'source-maps/source-inventory.csv').open(encoding='utf-8-sig',newline='')))
coverage=list(csv.DictReader((ROOT/'source-maps/source-coverage.csv').open(encoding='utf-8-sig',newline='')))
coverage_missing=[];bad_hash=[]
for row in coverage:
 for locus in [s.strip() for s in row['guide_locus'].split(';') if s.strip()]:
  if norm(locus) not in ids:coverage_missing.append({'source_unit':row['source_unit_id'],'locus':locus})
for rel,digest in {(r['source_path'],r['source_sha256']) for r in inventory}:
 if sha(ROOT/rel)!=digest:bad_hash.append(rel)
base=json.loads(read(OUT/'baseline/hashes.json'));unchanged_papers=all(sha(ROOT/rel)==digest for rel,digest in base['assets'].items() if rel.startswith('assets/papers/'))
report={'at':datetime.now().astimezone().isoformat(),'undefined_footnotes':undefined,'unused_source_footnotes':unused,'cited_dois':len(cited),'reference_dois':len(listed),'missing_reference_entries':missing_ref,'uncited_reference_dois':unused_ref,'first_use_doi_order':first,'listed_doi_order':listed,'reference_dois_in_first_use_order':first==listed,'source_units':len(inventory),'coverage_rows':len(coverage),'inventory_and_coverage_ids_match':{r['source_unit_id'] for r in inventory}=={r['source_unit_id'] for r in coverage},'coverage_missing_locations':coverage_missing,'changed_source_files':bad_hash,'original_papers_unchanged':unchanged_papers,'limits':'Mechanical identity and locator checks only. Actual source-to-explanation adequacy is assessed in independent teaching reviews.'}
(OUT/'source-consistency.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
print(json.dumps(report,indent=2))
# Resolve unique reader URLs with bounded concurrent reads; inaccessible publishers are distinct from missing identifiers.
def resolve(url):
 try:
  request=urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0'},method='HEAD')
  with urllib.request.urlopen(request,timeout=15) as result:return {'url':url,'status':result.status,'final_url':result.url}
 except urllib.error.HTTPError as e:return {'url':url,'status':e.code,'final_url':e.url,'access':'access restricted' if e.code in [401,403,429] else 'HTTP error'}
 except Exception as e:return {'url':url,'status':None,'error':str(e)}
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:results=list(pool.map(resolve,sorted(urls)))
(OUT/'external-link-check.json').write_text(json.dumps({'at':datetime.now().astimezone().isoformat(),'links':results},indent=2),encoding='utf-8')
print(json.dumps({'urls_checked':len(results),'unresolved':[r for r in results if r['status'] not in [200,401,403,429]]},indent=2))

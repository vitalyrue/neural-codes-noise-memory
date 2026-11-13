from pathlib import Path
from datetime import datetime,timezone
import json,hashlib

root=Path(__file__).resolve().parents[2];task=Path(__file__).resolve().parent
now=datetime.now(timezone.utc);stamp=now.isoformat()
state=json.loads((task/'STATE.json').read_text(encoding='utf-8'))
start=datetime.fromisoformat(state['started_at']);previous=datetime.fromisoformat(state['checkpoint_at'])
doctor=json.loads((root/'.build/doctor.json').read_text(encoding='utf-8'))
html=json.loads((task/'html-check-final.json').read_text(encoding='utf-8'))
release=json.loads((task/'release-audit.json').read_text(encoding='utf-8'))
assert html['status']=='pass' and not html['failures']
new_ids=['ch:HARDWARE-MEMORY','ch:HARDWARE-DYNAMICS','ch:NEUROMORPHIC-SYSTEMS','ch:HARDWARE-TESTS']
scope=json.loads((task/'scoped-acceptance.json').read_text(encoding='utf-8'))
scope['automatic_reuse']={cid:('reusable' if cid in doctor['semantic_review']['reused_chapters'] else doctor['semantic_review']['reasons'].get(cid,[])) for cid in new_ids}
scope['final_source_byte_sha256']={str(p.relative_to(root)).replace('\\','/'):hashlib.sha256(p.read_bytes()).hexdigest() for pattern in ['07-hardware-memory.*','08-hardware-dynamics.*','09-neuromorphic-systems.*','10-hardware-tests.*'] for p in (root/'content/chapters').glob(pattern)}
(task/'scoped-acceptance.json').write_text(json.dumps(scope,indent=2),encoding='utf-8')
state.update(completed_at=stamp,checkpoint_at=stamp,status='delivered_new_part3_local_html',wall_elapsed_seconds=round((now-start).total_seconds()),seconds_since_previous_checkpoint=round((now-previous).total_seconds()),awake_execution='unverified',remaining=[],book_model_hash=doctor['book_model_hash'],url='https://vrdell15.tail8b993e.ts.net/burak/parts/part-hardware.html',limits=['Full figure acceptance remains deferred.','Whole-guide semantic holds remain; doctor propagates the earlier Fisher prerequisite hold to Chapter 17 despite its completed direct local review.','No PDF/DOCX or complete all-format release claimed.'],token_statistics='unavailable')
(task/'STATE.json').write_text(json.dumps(state,indent=2),encoding='utf-8')
with (task/'checkpoints.jsonl').open('a',encoding='utf-8') as f:f.write(json.dumps({'at':stamp,'status':state['status'],'wall_elapsed_seconds':state['wall_elapsed_seconds']})+'\n')
p=root/'CURRENT_STATE.md';text=p.read_text(encoding='utf-8')
note=f'''### {stamp}: Part III delivered as private HTML

- Added Part III, **Neural memory in electronic hardware**, Chapters 14–17, beginning with a verified 23-word von Neumann quotation. It separates weight storage, changing neural state and remembered values; connects feedback/noise to error; covers selected 2025–2026 neuromorphic results; and proposes physics-based memory tests. New definitions are blue, key claims amber, and worked examples/derivations folded. Reading size remains 11.9px and print rules are unchanged.
- Independent separate truth, terminology and reader-flow calls pass for the new material. See `verification/part3-neuromorphic-20261030/RESULTS.md`. Local concept check: 23 selected concepts, 16 sections, 74 relations. Native Vale 3.24.0: zero errors, 83 warnings, 593 suggestions; 48 individually justified narrow exceptions.
- Rebuilt private HTML. All 24 pages and 1,858 local link/footnote targets pass. Three new tables use native publisher blocks; their exact cells were preserved when fixing raw pipe rendering. Representative live checks passed for the opening, table, blue definitions, example expansion and math. Eight existing paper PDFs were republished with checked hashes. No new raster figures or extended figure review.
- Four new chapter review records are current. Doctor automatically reuses three; Chapter 17 inherits the unresolved whole-chapter prerequisite review for earlier Fisher-information text. Whole-guide doctor remains attention (8 reusable, 12 required). Do not report whole-guide acceptance. Previous figure acceptance remains deferred. Standard release-record audit passes with zero findings and final HTML model linkage; no PDF/DOCX/public release or Git actions.
- Open: `https://vrdell15.tail8b993e.ts.net/burak/parts/part-hardware.html`. Final model `{doctor['book_model_hash']}`. Task wall time {state['wall_elapsed_seconds']} seconds; awake time unverified. The task folder contains source checks, all review rounds, formatting-reuse proofs, browser screenshots, final checks and timestamps.

'''
assert '## Open work\n\n' in text
p.write_text(text.replace('## Open work\n\n','## Open work\n\n'+note,1),encoding='utf-8')
print(json.dumps({'completed_at':stamp,'wall_elapsed_seconds':state['wall_elapsed_seconds'],'seconds_since_previous_checkpoint':state['seconds_since_previous_checkpoint'],'url':state['url'],'html_status':html['status'],'whole_guide_doctor':doctor['status']}))

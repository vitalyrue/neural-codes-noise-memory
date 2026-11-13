from pathlib import Path
from datetime import datetime, timezone
import json,hashlib

task=Path(__file__).resolve().parent;root=task.parents[1]
state=json.loads((task/'STATE.json').read_text(encoding='utf-8'))
doctor=json.loads((task/'doctor-final.json').read_text(encoding='utf-8'))
release=json.loads((task/'release-audit.json').read_text(encoding='utf-8'))
html=json.loads((task/'html-check-final.json').read_text(encoding='utf-8'))
concept=json.loads((task/'concept-check.json').read_text(encoding='utf-8'))
vale=json.loads((task/'vale-current.json').read_text(encoding='utf-8'))
browser=json.loads((task/'browser-check.json').read_text(encoding='utf-8'))
assert html['status']=='pass' and not html['failures']
assert concept['clear'] and not concept['findings']
assert release['status']=='passed' and release['artifacts']['html']['model_linkage']['status']=='verified'
assert all(hashlib.sha256((root/n).read_bytes()).hexdigest()==h for n,h in vale['files'].items())
now=datetime.now(timezone.utc);stamp=now.isoformat()
wall=round((now-datetime.fromisoformat(state['started_at'])).total_seconds())
since=round((now-datetime.fromisoformat(state['checkpoint_at'])).total_seconds())
url='https://vrdell15.tail8b993e.ts.net/burak/parts/part-simulations.html'
scope=json.loads((task/'scoped-acceptance.json').read_text(encoding='utf-8'))
scope['automatic_reuse']={cid:('reusable' if cid in doctor['semantic_review']['reused_chapters'] else doctor['semantic_review']['reasons'].get(cid,[])) for cid in scope['accepted_chapters']}
scope['final_source_byte_sha256']={str(p.relative_to(root)).replace('\\','/'):hashlib.sha256(p.read_bytes()).hexdigest() for pattern in ['11-simulating-memory.*','12-simulating-eye-drift.*','13-simulating-place-fields.*','14-simulation-tools.*'] for p in (root/'content/chapters').glob(pattern)}
(task/'scoped-acceptance.json').write_text(json.dumps(scope,ensure_ascii=False,indent=2),encoding='utf-8')

report=f'''# Part IV simulations and Part contribution labels

Completed {stamp}. Task started {state['started_at']}. Wall-clock duration {wall} seconds. Awake execution time is unverified; no Windows sleep/resume events were inspected. Token statistics are unavailable.

## Delivered scope

Added Part IV, **Simulations connect model assumptions to measurable outcomes**, with four short chapters:

- Chapter 18: Burak and Fiete (2012), stochastic neural networks, spike updates, diffusion measurement, alternative network designs and the distinction between numerical trajectories and evaluated formulas.
- Chapter 19: Ben-Shushan et al. (2022), recorded-data analysis, noisy integrator, motor pathway, muscle filtering, feedback, controls, MATLAB code and deposited recordings.
- Chapter 20: Mainali et al. (2025), Gaussian spatial maps, smoothing and normalization, fitted summaries, field measurement, topology, Python code and data limits.
- Chapter 21: source code versus an independent implementation, numerical tools, time and spatial resolution, repeatability, uncertainty and a record for reproducing one figure.

All four Part openings identify chapter contributions by author/year and distinguish central findings, supporting results, background and guide-derived explanations or tests. Original chapter IDs, titles and order are preserved. Part III remains the neuromorphic-computing part.

The only changed scientific claim in an older chapter is the narrow attribution of the corrected 2012 Eq. 2 to the authors' official 2017 correction. The equation was already correct. Other source-equation checks remain separate.

## Evidence and independent review

Sources and actual code settings were inspected, not executed as full-paper reproductions. See memory-sources.md, eye-sources.md, place-sources.md and tool-sources.md. Original program defaults are not silently combined with the publications' different parameter sets. Optional tools are distinguished from the packages actually used by each paper.

Separate independent truth, wording and reader-flow calls passed for the changed scope. The records are review-memory-stage1/2/3.json, review-eye-stage1/2/3.json and review-place-stage1/2/3.json, with separate repair rechecks. Initial findings are retained. Wording-repairs.json, wording-repairs-round2.json and flow-repairs.json record the edits. The final flow repairs teach the Gaussian filter operation, avoid using random seed before its explanation, and describe Part II's actual chapter order.

The local prerequisite check is clear. concept-judgments-merged.json and concept-index-final.json preserve the independently reviewed concept locations and assumptions. This does not newly approve the earlier chapters used as prerequisites.

Native Vale 3.24.0 checked the four new chapters and extracted changed Part/reading/reference/glossary passages. Its final raw counts are {vale['counts']['error']} error-level pattern matches, {vale['counts']['warning']} warnings and {vale['counts']['suggestion']} suggestions. These raw outputs have not been rewritten as zero. The independent wording records contain passage-specific repair or retain decisions, including exact source titles, numeric ranges, necessary contrasts and real causal statements. No global rule or severity was changed. Reader-flow review is separate from lint.

## HTML verification

- Canonical validation and full HTML build completed using Publisher 0.8.23 and the pinned teaching skills.
- {html['html_pages']} HTML pages, {html['local_targets']} local targets and {html['math_spans']} math spans checked; no local link, footnote-count or math failures.
- Eight existing local paper PDF assets were republished with matching hashes.
- Representative live browser checks passed for the new Part opening, the six-row native software table, blue definitions and the expanded numerical example. Base reading size remains 11.9px, without horizontal overflow or math-rendering errors. Screenshots are saved beside this report.
- Standard release-record audit and final doctor results are in release-audit.json and doctor-final.json. Current model: {doctor['book_model_hash']}.

## Remaining scope limits

Whole-guide doctor status remains {doctor['status']}. Existing semantic/prerequisite and figure holds are not cleared by this extension. The full visual review of the earlier figures remains deferred. No full source simulation, raw-recording reanalysis, new raster artwork, DOCX/PDF release, public deployment or Git action was performed.

Open: {url}
'''
(task/'RESULTS.md').write_text(report,encoding='utf-8')
state.update(completed_at=stamp,checkpoint_at=stamp,status='delivered_part4_simulations_private_html',wall_elapsed_seconds=wall,seconds_since_previous_checkpoint=since,remaining=[],book_model_hash=doctor['book_model_hash'],url=url,limits=['Full source simulations and raw recording analyses were not rerun.','Prior whole-guide semantic/prerequisite holds remain.','Full figure acceptance remains deferred.','No PDF/DOCX or complete all-format release.'])
(task/'STATE.json').write_text(json.dumps(state,ensure_ascii=False,indent=2),encoding='utf-8')
with (task/'checkpoints.jsonl').open('a',encoding='utf-8') as f:f.write(json.dumps({'at':stamp,'status':state['status'],'wall_elapsed_seconds':wall,'since_previous_checkpoint_seconds':since,'awake_execution':'unverified'})+'\n')
p=root/'CURRENT_STATE.md';t=p.read_text(encoding='utf-8')
note=f'''### {stamp}: Part IV simulations delivered as private HTML

- Added Chapters 18 to 21 on the three papers' simulations, methods, software, data and reproduction checks. All Part introductions now attribute chapter results using author/year and central/supporting/background/guide-derived labels. Source code inspection is explicitly distinguished from running a full reproduction.
- Independent separate truth, wording and reading-flow reviews pass for this new/changed text. The local concept check is clear. See `verification/part4-simulations-20261030/RESULTS.md` for full evidence and raw lint counts. No global prose rule changed.
- Full HTML build and {html['html_pages']}-page/{html['local_targets']}-target link check passed. Representative live checks passed for the Part opening, native table, blue definitions and foldable example. Font remains 11.9px. Existing PDF asset hashes match.
- Earlier full-guide semantic/prerequisite holds and deferred figure acceptance remain. No PDF/DOCX, simulation reruns, public publication or Git actions. Doctor remains `{doctor['status']}`; see final report for exact inherited reasons.
- Open `{url}`. Task wall time {wall} seconds; awake time unverified.

'''
assert '## Open work\n\n' in t
import re
t=re.sub(r'^### [^\n]+: Part IV simulations delivered as private HTML\n.*?(?=^### |\Z)','',t,flags=re.M|re.S)
p.write_text(t.replace('## Open work\n\n','## Open work\n\n'+note,1),encoding='utf-8')
print(json.dumps({'completed_at':stamp,'wall_elapsed_seconds':wall,'since_previous_checkpoint_seconds':since,'url':url,'doctor_status':doctor['status'],'raw_vale_counts':vale['counts']}))

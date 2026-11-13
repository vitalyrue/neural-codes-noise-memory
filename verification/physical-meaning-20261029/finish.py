from pathlib import Path
import json,hashlib,datetime
root=Path(__file__).resolve().parents[2]; out=Path(__file__).resolve().parent
now=datetime.datetime.now().astimezone()
state=json.loads((out/'STATE.json').read_text(encoding='utf-8-sig'))
start=datetime.datetime.fromisoformat(state['started'])
source=json.loads((out/'source-checks.json').read_text())
reviews='\n'.join(p.read_text(encoding='utf-8') for p in out.glob('*stage3.md')).upper()
for name,entry in source['chapters'].items():
    digest=hashlib.sha256((root/'content/chapters'/name).read_bytes()).hexdigest()
    assert digest==entry['sha256'],name
    assert digest.upper() in reviews,('missing final independent hash',name)
browser={'checked_at':now.isoformat(),'method':'Live native in-app browser, DOM inspection and real summary clicks','viewport':'Normal browser size, no override','pages':{
'ch-foundations.html':{'new_content_after_reload':True,'covariance_default_collapsed':True,'opened_and_closed_by_click':True,'definitions_color':'rgb(31, 78, 121)','font_size':'11.9px','page_overflow':False,'math_errors':0,'screenshot':'foundations-physics.jpg'},
'ch-persistence.html':{'two_examples_default_collapsed':True,'two_new_formal_folds_default_collapsed':True,'physical_explanation_visible':True,'font_size':'11.9px','page_overflow':False,'math_errors':0,'screenshot':'persistence-physics.jpg'},
'ch-place-fields.html':{'gaussian_definition_default_collapsed':True,'input_h_visible_outside_fold':True,'font_size':'11.9px','page_overflow':False,'math_errors':0,'screenshot':'place-physics.jpg'},
'ch-memory-readout.html':{'hyperbolic_solution_default_collapsed':True,'long_limit_outside_fold':True,'page_overflow':False,'math_errors':0}},'limits':'Three screenshots inspected and one additional DOM check; no full-book pixel sweep or mobile override.'}
(out/'browser-checks.json').write_text(json.dumps(browser,indent=2),encoding='utf-8')
elapsed=(now-start).total_seconds()
state.update(checkpoint=now.isoformat(),finished=now.isoformat(),wall_seconds=elapsed,status='Complete for focused physical-meaning and formal-definition-fold scope',changed_chapters=10,chapters_checked_for_gaps=13,new_formal_folds=6,independent_reviews='Separate correctness, necessity/wording, reader-flow calls in three groups; all required findings repaired and rechecked; final hashes match',browser_pages=4,awake_execution='unverified',token_stats='unavailable')
(out/'STATE.json').write_text(json.dumps(state,indent=2),encoding='utf-8')
summary=f'''# Physical meaning and optional mathematics

Completed {now.isoformat()}. Wall time {elapsed/60:.1f} minutes since {start.isoformat()}; awake execution unverified.

The focused gap search covered all 13 teaching chapters. Ten chapters changed. Foundations now starts from eye motion, shared neural commands and private spike variability, then connects covariance and displacement to physical causes and measurement error. Persistence keeps the two disturbance meanings visible. Other additions explain the spike-to-cell chain, decay versus recurrent renewal, mutual excitation, controlled synaptic-time comparisons, eye command/response parameters, and place-field input strength versus threshold, gain and spatial overlap.

Six new optional math folds: covariance/correlation, MSD identity derivation, independent steps/Brownian definition, Brownian covariance, hyperbolic readout solution, and formal Gaussian-process definition. All nine existing examples remain foldable. All existing displayed equations, figure block placements, and section anchors are preserved. No figure or stylesheet edits.

Separate independent correctness, wording and reader-flow calls completed for foundations, memory, and eye/place groups. Repairs include visible h(x), a readout closing fence, gain/noise qualification, explicit lag, definition term markup, and two wording attachments. Original reviewer reports remain unchanged, with addenda where needed. Each final stage3 report contains the current source hashes.

HTML built with Publisher0.8.23/Quarto1.10.18. Eight PDF hashes checked by existing asset publication. Static checks passed all ten changed HTML pages for local links, image targets, anchors, duplicate IDs, unexpanded blocks and math errors. Live browser checks covered four pages; three screenshots inspected. Covariance actually opened and closed. The first browser navigation used cached old content; reload displayed the rebuilt content and the final deliverable uses a version query. Blue definitions, amber conclusions and 11.9px reading size preserved. No changes to screen or print CSS.

This is focused acceptance of changed explanations and connections, not a new whole-book scientific audit or full-format release. Historical global semantic-review records and development locks remain unchanged. The mechanically generated CURRENT_STATE snapshot predates these edits. No server reconfiguration, commit or public deployment.

Evidence: source-checks.json, html-checks.json, browser-checks.json, three stage1/stage2/stage3 groups and addenda, original .before sources, final .diff files, build.log.

Preview: https://vrdell15.tail8b993e.ts.net/burak/chapters/ch-foundations.html?physics=20261029#sec-foundations-covariance

Token stats unavailable.
'''
(out/'RESULTS.md').write_text(summary,encoding='utf-8')
current=root/'CURRENT_STATE.md'; text=current.read_text(encoding='utf-8')
entry=f'''### {now.isoformat()}: physical explanations and optional math complete

- Focused gap search covered all13 teaching chapters; ten changed. Physical causes and parameter effects now connect eye displacement, persistent neural activity, spike-to-input-to-rate changes, synaptic decay, motor response and place-field thresholds/input overlap. Essential explanation remains visible outside examples.
- Added six formal-math folds, including covariance/correlation, Brownian definitions/covariance, hyperbolic functions and Gaussian processes. All nine examples remain foldable; original displayed equations, figure blocks and anchors are preserved. Source section title/sidecar/structural description updated together.
- Separate independent correctness, wording and connected-reader reviews passed after repairs, with current hashes checked. Ten changed HTML pages pass local links/assets/anchors and math checks. Four live pages checked, three screenshots inspected, covariance opened/closed. Blue definitions, amber statements and11.9px size retained. Evidence: `verification/physical-meaning-20261029/`.
- HTML rebuilt and paper assets synchronized to existing VPN site. No new full-book scientific audit, pixel sweep, print build or public release. Historical semantic records and locks remain. The mechanically generated snapshot above predates these changes.
- Wall elapsed {elapsed/60:.1f}min from {start.isoformat()}; awake execution unverified; token stats unavailable. No required work remains in this scope. Preview: https://vrdell15.tail8b993e.ts.net/burak/chapters/ch-foundations.html?physics=20261029#sec-foundations-covariance .

'''
assert 'physical explanations and optional math complete' not in text
current.write_text(text.replace('## Open work\n\n','## Open work\n\n'+entry,1),encoding='utf-8',newline='\n')
print(json.dumps({'finished':now.isoformat(),'wall_minutes':round(elapsed/60,1),'independent_final_hashes_matched':10,'status':'complete'},indent=2))

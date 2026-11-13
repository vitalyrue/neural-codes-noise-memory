"""Final canonical-input recheck for independently reviewed A01-A04 only."""
from pathlib import Path
from datetime import datetime
import json,hashlib,yaml

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[1]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()

old=json.loads((HERE/'stage1-A01-A04.json').read_text(encoding='utf-8'))
rows=json.loads((HERE/'integration.json').read_text(encoding='utf-8'))
bindings=json.loads((HERE/'current-bindings.json').read_text(encoding='utf-8'))
reviews={};checks=[]
for original in old['figures']:
    row=next(r for r in rows if r['visual_id']==original['visual_id'])
    visual=row['visual_id'];binding=bindings['figures'][visual]
    assert row['id'] in ['A01','A02','A03','A04']
    assert binding['review_contract']['author']!='/root/all_draw_eye_place'
    for path,h in binding['input_sha256'].items():
        resolved=Path(path) if Path(path).is_absolute() else ROOT/path
        assert sha(resolved)==h,(visual,path,'changed input')
    canonical=ROOT/row['asset'];svg=canonical.with_suffix('.svg')
    assert sha(canonical)==original['reviewed_png_sha256']==binding['reviewed_sha256']
    assert sha(svg)==original['reviewed_svg_sha256']
    assert sha(ROOT/row['book_width_preview'])==original['reviewed_book_width_sha256']
    qa=json.loads((ROOT/row['qa']).read_text(encoding='utf-8'))
    assert qa['status']=='pass' and not qa['warnings']
    assert qa['png_sha256']==sha(canonical) and qa['svg_sha256']==sha(svg)
    assert qa['spec_sha256']==sha(ROOT/row['editable_source'])
    text=(ROOT/row['chapter']).read_text(encoding='utf-8')
    metadata=yaml.safe_load((ROOT/row['chapter']).with_suffix('.yaml').read_text(encoding='utf-8'))
    block=next(b for b in metadata['blocks'] if b['id']==visual)
    assert block['asset']==row['asset']
    assert block['caption']==row['caption'] and block['alt']==row['alt']
    assert text.count('{{block:'+visual+'}}')==1
    assert row['intro'] in text and row['interpretation'] in text
    brief=yaml.safe_load((ROOT/row['brief']).read_text(encoding='utf-8'))
    assert brief['language_contract']['caption']==block['caption']
    assert brief['language_contract']['conclusion']==row['interpretation']
    differences=[k for k in ['caption','alt','intro','interpretation','insert_after'] if original['reviewed_packet_fields'][k]!=row[k]]
    assert differences==(['interpretation'] if row['id']=='A02' else [])
    evidence=[
      'Independent full-size and700px inspection, calculations and claim-by-claim review: verification/all-illustrations-20261024/stage1-A01-A04.json, '+row['id']+'.',
      'Final canonical Markdown insertion, caption and alt in the owning chapter YAML, current brief, editable generator and QA were read/checked. Current input hashes match every path in current-bindings.json.',
      'Canonical PNG/SVG and candidate700px preview match the exact image hashes already viewed independently; no new pixel pass is claimed or needed for identical bytes.'
    ]
    if row['id']=='A02':
        evidence.append('Focused truth recheck of W1: root mean squared displacement is sqrt(2Dt) with D=.02>0, hence it grows while one zero-mean Brownian path may turn back. The second sentence retains the chosen constant-bias versus square-root-scale comparison. This agrees with the current caption, upper RMS envelope, lower curve and earlier definition; no numerical or domain assumption changed.')
    scenes=[{k:v for k,v in s.items() if k!='verdict'} for s in original['scenes']]
    reviews[visual]=dict(schema_version=1,status='approved',reviewer='/root/all_draw_eye_place',
      reviewed_at=datetime.now().astimezone().isoformat(),reviewed_sha256=binding['reviewed_sha256'],
      policy_sha256=binding['policy_sha256'],context_sha256=binding['context_sha256'],
      input_sha256=binding['input_sha256'],source_scope_sha256=binding['source_scope_sha256'],
      strongest_objection=original['strongest_objection'],objection_resolution=original['objection_resolution'],
      checks=dict(
        technical_accuracy={'verdict':'pass','evidence':evidence},
        visual_explanation={'verdict':'pass','evidence':['The required scenes are calculated distributions or curves, each with a specific visible relationship; see individual scene records and the independent claim record.'],'reference_comparison':None,'scenes':scenes},
        readability={'verdict':'pass','evidence':['Both original pixels and700px preview were inspected in Stage1; all four final asset/preview hash comparisons are identical. Axis units, legends, numerical labels and leader endpoints retain the inspected layout.'],'full_size_inspected':True,'reviewed_width_px':700},
        palette={'verdict':'pass','evidence':['Stage1 independently checked exact SVG tokens against the locked house profile and inspected their roles. Final SVG hash is unchanged. Current calculated QA passes with no warnings; no raster pixel-deviation result is claimed.']},
        coverage={'verdict':'not-applicable','evidence':['Internal mathematical detail figure; no chapter-opening coverage claim.'],'covered_ids':[],'visible_evidence':{}}))
    checks.append({'id':row['id'],'png_matches_stage1':True,'svg_matches_stage1':True,'preview_matches_stage1':True,'all_current_inputs_match':True,'changed_text_fields_since_stage1':differences,'canonical_caption_alt_match_packet':True,'qa_spec_matches_current_generator':True})

(HERE/'diagram-review-A01-A04.json').write_text(json.dumps(reviews,ensure_ascii=False,indent=2),encoding='utf-8')
now=datetime.now().astimezone();start=datetime.fromisoformat('2026-10-24T18:31:14.999410+03:00');previous=datetime.fromisoformat('2026-10-24T18:48:14.136002+03:00')
record={'at':now.isoformat(),'reviewer':'/root/all_draw_eye_place','scope':'Final canonical-input binding recheck of A01-A04 only; image-specific approval. Separate final reader-flow review remains with the main reviewer.','root_wall_elapsed_seconds':(now-start).total_seconds(),'since_previous_checkpoint_seconds':(now-previous).total_seconds(),'awake_execution_time':'unverified','book_model_hash':bindings['book_model_hash'],'figures':checks}
(HERE/'final-binding-A01-A04.json').write_text(json.dumps(record,indent=2),encoding='utf-8')
print(json.dumps({'at':record['at'],'approved_figures':len(reviews),'root_wall_elapsed_seconds':record['root_wall_elapsed_seconds'],'since_previous_checkpoint_seconds':record['since_previous_checkpoint_seconds']}))

"""Record generation scope/style and preserve the pre-insertion reader source."""
from pathlib import Path
import datetime,hashlib,json,shutil,yaml
ROOT=Path(__file__).resolve().parents[2]
SKILL=Path('C:/Users/vital/.codex/skills/course-diagram-builder')
ROWS=[
 ('V01','fig:FOUNDATIONS-PAPER-MAP','01-foundations','FOUNDATIONS-RANDOMNESS','draw_orientation.py','/root',['time','eye-path','fixed-space']),
 ('V02','fig:MEMORY-TILTED-DECAY','02-memory-dynamics','MEMORY-LINEARIZATION','draw_memory.py','/root/draw_memory_figures',['tilted-flow']),
 ('V03A','fig:MEMORY-READOUT-TIMELINE','03-memory-information','MEMORY-READOUT-SETUP','draw_memory.py','/root/draw_memory_figures',['storage-and-observation']),
 ('V03B','fig:MEMORY-READOUT-CURVES','03-memory-information','MEMORY-FIG3-AND-CAUTION','draw_memory.py','/root/draw_memory_figures',['readout-curves']),
 ('V04','fig:EYE-PHYSICAL-AND-RECORDED','04-eye-drift','EYE-RECORDINGS','draw_eye.py','/root/draw_eye_figures',['physical-path','recordings-and-analysis']),
 ('V05','fig:EYE-FILTERED-NOISE-MSD','04-eye-drift','EYE-FILTERED-MSD','draw_eye.py','/root/draw_eye_figures',['filter-comparison']),
 ('V06','fig:PLACE-CROSSINGS','05-place-fields','PLACE-KAC-RICE','draw_place.py','/root/draw_place_figures',['fields-and-crossings','slope-weight']),
 ('V07','fig:PLACE-SIZE-GEOMETRY','05-place-fields','PLACE-SIZE-LAW','draw_place.py','/root/draw_place_figures',['peak-radius','dimensional-size']),
 ('V08','fig:PLACE-TOPOLOGY','05-place-fields','PLACE-TOPOLOGY','draw_place.py','/root/draw_place_figures',['nested-excursions']),
]

def main():
    base=ROOT/'verification/illustrations/baseline'
    base.mkdir(parents=True,exist_ok=True)
    before={}
    for path in sorted((ROOT/'content/chapters').glob('*')):
        if path.suffix not in {'.md','.yaml'}:continue
        target=base/path.name
        if not target.exists():shutil.copy2(path,target)
        before[str(path.relative_to(ROOT)).replace('\\','/')]=hashlib.sha256(target.read_bytes()).hexdigest()
    (base/'hashes.json').write_text(json.dumps(before,indent=2),encoding='utf-8')
    briefdir=ROOT/'plan/illustrations/briefs';briefdir.mkdir(exist_ok=True)
    for ident,vid,stem,section,script,author,scenes in ROWS:
        brief={
            'brief':{'asset_id':vid,'plan_id':ident,'approved_brief':'plan/illustrations/PLAN.md',
              'placement':'sec:'+section,'source':f'content/chapters/{stem}.md',
              'generator':'verification/illustrations/'+script,
              'purpose':'Make the connected calculation or distinction visible without changing its assumptions.',
              'insertion_width_px':700,'scenes':scenes,
              'route_note':'Deterministic scientific vector/code figure, approved in the plan. Not a generic structural template or raster opener.'},
            'style_contract':{
              'book_style_lock':'source-maps/book-style-lock.yaml',
              'palette_family_id':'technical-editorial-blueprint','palette_family_version':'1.0.0',
              'route':'vector','profile_id':'house-graphic-v1','profile_version':'0.1.0',
              'profile_path':str(SKILL/'references/house-graphic-v1.yaml').replace('\\','/'),
              'palette':{'distance_rule':'exact SVG color-token membership; raster antialiasing is not a deviation audit',
                 'maximum_token_deviations':0,'allowed_special_purpose_colors':[]},
              'role_note':'One family across plots and mechanisms; curve colors distinguish calculated alternatives, not trust verdicts.'},
            'review_contract':{
              'schema_version':1,'figure_role':'quantitative-figure' if ident not in {'V01','V04'} else 'structural-diagram',
              'route':'vector','unit_scope':'chapter','author':author,
              'role_reason':'An internal explanatory figure with exact scientific relationships, not chapter opening artwork.',
              'source_files':[f'content/chapters/{stem}.md',f'content/chapters/{stem}.yaml',
                 'plan/illustrations/PLAN.md','verification/illustrations/'+script,'verification/illustrations/figure_style.py'],
              'rule_files':[str(SKILL/'references/visual-qa.md').replace('\\','/'),str(SKILL/'references/review-acceptance.md').replace('\\','/')],
              'style_lock':'source-maps/book-style-lock.yaml',
              'style_profile':str(SKILL/'references/house-graphic-v1.yaml').replace('\\','/'),
              'reference_images':[],
              'palette_audit':f'candidate-content/visuals/candidates/20261023/{ident}/qa.json',
              'vector_spec':'verification/illustrations/'+script,
              'insertion_width_px':700,'required_scene_ids':scenes,
              'coverage':{'applicable':False,'reason':'Local mechanism/calculation figure inside a section; no opening-map coverage claim.'}
            }
        }
        (briefdir/f'{ident}.yaml').write_text(yaml.safe_dump(brief,sort_keys=False,allow_unicode=True),encoding='utf-8')
    print(json.dumps({'briefs':len(ROWS),'baseline_files':len(before),'at':datetime.datetime.now().astimezone().isoformat()},indent=2))

if __name__=='__main__':main()

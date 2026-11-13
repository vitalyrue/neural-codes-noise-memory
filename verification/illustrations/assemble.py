"""Normalize the approved drawing packets and insert independently checked art.

No existing explanations or table cells are rewritten. Pre-insertion sources
are preserved by prepare_run.py; each insertion has an exact unique anchor.
"""
from pathlib import Path
import argparse,datetime,hashlib,json,re,shutil,yaml
ROOT=Path(__file__).resolve().parents[2]
AREAS={'orientation':'/root','memory':'/root/draw_memory_figures','eye':'/root/draw_eye_figures','place':'/root/draw_place_figures'}

def sha(path):return hashlib.sha256(path.read_bytes()).hexdigest()

def records():
    combined=[]
    for area,author in AREAS.items():
        data=json.loads((ROOT/f'verification/illustrations/{area}-integration.json').read_text(encoding='utf-8-sig'))
        rows=data if isinstance(data,list) else data['figures']
        for r in rows:
            ident=r.get('id') or r['asset_id']
            stem=r.get('stem') or Path(r.get('chapter') or r['chapter_path']).stem
            brief=yaml.safe_load((ROOT/f'plan/illustrations/briefs/{ident}.yaml').read_text(encoding='utf-8'))
            assert brief['brief']['asset_id']==r['visual_id'],ident
            item=dict(r)
            item.update(id=ident,stem=stem,author=author,
                chapter=f'content/chapters/{stem}.md',
                placement=r.get('placement') or r.get('placement_section') or r['section'],
                anchor=r.get('anchor') or r['insert_after'],
                candidate=f'candidate-content/visuals/candidates/20261023/{ident}',
                review_contract=brief['review_contract'])
            # These two captions contain essential mathematical expressions.
            # Use the guide's math renderer rather than literal caret strings.
            if ident=='V05':
                item['caption']=item['caption'].replace('M_white/(A/τ) and M_Brownian/(2Dτ)',r'$M_{\mathrm{white}}/(A/\tau)$ and $M_{\mathrm{Brownian}}/(2D\tau)$')
            if ident=='V07':
                item['caption']=item['caption'].replace('U = beta s^(2/d)',r'$U=\beta s^{2/d}$')
            if ident=='V02':
                item['caption']=item['caption'].replace(
                    r'The imposed jump from $(0,0)$ to $(0,2)$ relaxes toward $(1,0)$, while successive time marks crowd toward the endpoint.',
                    r'After an imposed jump from $(0,0)$ to $(0,2)$, the state relaxes toward $(1,0)$; successive time marks crowd toward that endpoint.')
            if ident=='V05':
                item['intro']='The curves compare the two inputs after the same filter with one exponential response, also called a one pole filter.'
                item['interpretation']='The white-input short-lag slope of one belongs to this one-pole example.'
            if ident=='V06':
                item['intro']='A fixed smooth curve shows how to count a field already active at the left edge and why the crossing integral weights each slope.'
                item['anchor']="The density $p_{z,z'}(q,v)$ describes how often height is near $q$ and slope near $v$. Multiplication by $v$ compensates for the shorter spatial window of a steep crossing. Merely multiplying the probability of being above threshold by a typical slope would miss this weighting.[^p3-crossings]"
                item['placement_note']='After the Kac–Rice display and its density explanation, preserving the original paragraph-to-equation connection.'
            if ident=='V08':
                item['caption']=item['caption'].replace('The masks are nested even though this signed count is not monotone.','The above-threshold regions shrink as the threshold rises, even though this signed count does not change in one direction.')
            name=r['visual_id'].replace('fig:','').lower()
            item['asset']=f'assets/approved/visuals/{name}.png'
            item['vector_asset']=f'assets/approved/visuals/{name}.svg'
            combined.append(item)
    return sorted(combined,key=lambda r:r['id'])

def main():
    args=argparse.ArgumentParser()
    args.add_argument('--apply',action='store_true')
    args.add_argument('--approved-stage1',action='store_true')
    opt=args.parse_args()
    canonical=ROOT/'verification/illustrations/integration.json'
    previous_rows={r['id']:r for r in json.loads(canonical.read_text(encoding='utf-8'))} if canonical.exists() else {}
    rows=records()
    for r in rows:
        candidate=ROOT/r['candidate']
        qa=json.loads((candidate/'qa.json').read_text(encoding='utf-8'))
        assert qa['status']=='pass' and qa['automatic_gates']=='pass',r['id']
        assert qa['png_sha256']==sha(candidate/'figure.png'),r['id']
        assert qa['spec_sha256']==sha(ROOT/r['review_contract']['vector_spec']),r['id']
        r['sha256']=sha(candidate/'figure.png')
    if opt.apply:
        for r in rows:
            previous=previous_rows.get(r['id'])
            if not previous:continue
            path=ROOT/r['chapter'];text=path.read_text(encoding='utf-8')
            if '{{block:'+r['visual_id']+'}}' not in text:continue
            for field in ['intro','interpretation']:
                if previous[field]!=r[field]:
                    assert text.count(previous[field])==1,(r['id'],field)
                    text=text.replace(previous[field],r[field],1)
            path.write_text(text,encoding='utf-8')
    canonical.write_text(json.dumps(rows,indent=2),encoding='utf-8')
    if not opt.apply:
        print(json.dumps({'prepared_figures':len(rows),'applied':False},indent=2));return
    assert opt.approved_stage1,'Root must read current independent Stage1 reports before authorizing insertion'
    for name in ['review-eye-stage1','review-memory-stage1','review-place-orientation-stage1']:
        assert (ROOT/f'verification/illustrations/{name}.json').exists(),name
    ledger_path=ROOT/'source-maps/visual-ledger.yaml'
    ledger=yaml.safe_load(ledger_path.read_text(encoding='utf-8'))
    ledger['visual_ledger_version']=3
    before={}
    for r in rows:
        path=ROOT/r['chapter'];text=path.read_text(encoding='utf-8')
        before.setdefault(r['chapter'],sha(path))
        token='{{block:'+r['visual_id']+'}}'
        for ext,key in [('png','asset'),('svg','vector_asset')]:
            dest=ROOT/r[key];dest.parent.mkdir(parents=True,exist_ok=True)
            src=ROOT/r['candidate']/('figure.'+ext)
            if dest.exists():assert sha(dest)==sha(src),'Do not overwrite an approved asset without versioning'
            else:shutil.copy2(src,dest)
        if token not in text:
            assert text.count(r['anchor'])==1,f"{r['id']} anchor count"
            addition='\n\n'+r['intro']+'\n\n<div class="figure-scroll">\n\n'+token+'\n\n</div>\n\n'+r['interpretation']
            text=text.replace(r['anchor'],r['anchor']+addition,1)
            path.write_text(text,encoding='utf-8')
        side=path.with_suffix('.yaml');meta=yaml.safe_load(side.read_text(encoding='utf-8'))
        existing=meta.setdefault('blocks',[])
        block={'id':r['visual_id'],'kind':'figure','placement':r['placement'],'asset':r['asset'],
               'caption':r['caption'],'alt':r['alt'],'width_inches':7.29167,'html_fold':'never'}
        matches=[i for i,b in enumerate(existing) if b['id']==r['visual_id']]
        if matches:existing[matches[0]]=block
        else:existing.append(block)
        side.write_text(yaml.safe_dump(meta,sort_keys=False,allow_unicode=True),encoding='utf-8')
        report=('review-eye-stage1' if r['id'] in {'V04','V05'} else
                'review-memory-stage1' if r['id'] in {'V02','V03A','V03B'} else 'review-place-orientation-stage1')
        item={
            'visual_id':r['visual_id'],'block_id':r['visual_id'],'asset':r['asset'],
            'sha256':r['sha256'],'status':'selected','embedded':True,
            'origin':'Original deterministic scientific guide construction; not experimental data.',
            'source_status':r.get('source_locator','See caption for exact source locator.'),
            'rights':'Original guide figure','generator':r['review_contract']['vector_spec'],
            'vector_source':r['vector_asset'],'placement':r['placement'],
            'caption_and_alt':str(side.relative_to(ROOT)).replace('\\','/'),
            'teaching_introduction':r['intro'],'caption':r['caption'],
            'interpretation':r['interpretation'],'accessibility_description':r['alt'],
            'toc_correspondence':r['placement'],'provenance':'Guide-created from the cited explanation and analytic model.',
            'content_review':f'verification/illustrations/{report}.json',
            'visual_review':f'verification/illustrations/{report}.json',
            'review_contract':r['review_contract'],
            'diagram_review':{'schema_version':1,'status':'pending','reason':'Exact asset independently checked for insertion; final source/input bindings and connected wording/flow review pending.'}
        }
        previous=[i for i,b in enumerate(ledger['visuals']) if b['visual_id']==r['visual_id']]
        if previous:ledger['visuals'][previous[0]]=item
        else:ledger['visuals'].append(item)
    ledger_path.write_text(yaml.safe_dump(ledger,sort_keys=False,allow_unicode=True),encoding='utf-8')
    preservation=[]
    for rel in before:
        path=ROOT/rel
        baseline=(ROOT/'verification/illustrations/baseline'/path.name).read_text(encoding='utf-8')
        current=path.read_text(encoding='utf-8')
        stripped=current
        for r in rows:
            if r['chapter']!=rel:continue
            token='{{block:'+r['visual_id']+'}}'
            insertion='\n\n'+r['intro']+'\n\n<div class="figure-scroll">\n\n'+token+'\n\n</div>\n\n'+r['interpretation']
            assert stripped.count(insertion)==1,r['id']
            stripped=stripped.replace(insertion,'',1)
        assert stripped==baseline,rel+' existing prose changed'
        preservation.append({'path':rel,'existing_prose_identical_after_removing_insertions':True,'before_sha256':before[rel],'after_sha256':sha(path)})
    result={'at':datetime.datetime.now().astimezone().isoformat(),'new_figures':len(rows),'preservation':preservation,
      'old_attractor_sha256':sha(ROOT/'assets/approved/visuals/attractor-directions.svg'),
      'publication':'Local HTML rebuild pending; no public deployment.'}
    (ROOT/'verification/illustrations/insertion-record.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
    print(json.dumps(result,indent=2))

if __name__=='__main__':main()

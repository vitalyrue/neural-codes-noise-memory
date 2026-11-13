from pathlib import Path
from datetime import datetime
import hashlib,json,yaml
root=Path('verification/diagram-maps-20261111')
out=root/'prompts-a'; out.mkdir(parents=True,exist_ok=True)
tasks=[('front-reading',root/'briefs/front-reading-brief.yaml',2),('front-mathematical-tools',root/'briefs/front-mathematical-tools-brief.yaml',2),('front-exam-review',root/'briefs/front-exam-review-brief.yaml',2),('ch01',root/'ch01-brief.yaml',2)]+[(f'ch0{i}',root/f'briefs/ch0{i}-brief.yaml',1) for i in range(2,7)]+[('part-i',root/'briefs/part-i-brief.yaml',1)]
manifest={'created_at':datetime.now().astimezone().isoformat(),'status':'drafts_only_visual_review_pending','references':[{'path':'C:/Users/vital/.codex/skills/course-diagram-builder/assets/technical-editorial-blueprint-v1/style-master.png','role':'style only'},{'path':'C:/Users/vital/.codex/skills/course-diagram-builder/assets/visual-language-examples-v1/m1-retrieval-scenes.png','role':'composition only'}],'assets':[]}
for name,path,n in tasks:
 raw=path.read_bytes(); d=yaml.safe_load(raw.decode('utf-8-sig')); scenes=d['visual_explanation']['scenes']; labels=d.get('exact_text',{}).get('required',[]); cov=d.get('chapter_map_coverage',{}); points=cov.get('teaching_points',cov.get('source_scope_inventory',[])); points={str(x.get('id')):x.get('point','') for x in points if isinstance(x,dict)}
 if name=='ch01': labels=['Eye muscles','Spikes and activation; weighted feedback','Population code','Variable spike counts','Simulation and theory','Shared eye signal']
 elif len(labels)!=len(scenes): labels=[str((s.get('visible_objects') or ['Mechanism'])[0]) for s in scenes]
 splits=[list(range(len(scenes)))] if n==1 else [list(range((len(scenes)+1)//2)),list(range((len(scenes)+1)//2,len(scenes)))]
 for k,indices in enumerate(splits,1):
  asset=name+(('-a','-b')[k-1] if n==2 else '')
  intro='Create ONE draft title-free landscape scientific educational map for a neuroscience study guide. Image 1 is STYLE ONLY: retain the book style navy #092E5B, teal #159C9A, cyan #16A6BF, orange #EB731B, pale blue #E8F3F5 and warm paper #F7F2E6, not its wording or subject. Image 2 is STRUCTURE ONLY: reuse distinct concrete mini-scenes, not its labels, content, dense layout or arbitrary arrows. Favor large readable text at a 6.35-inch reading width. Show real objects, neural states, relationships and traces; do not use text-only cards. No title banner, footer, long sentences, invented values, unrelated icons, or invented causal connections. Keep separate scenarios separate, with arrows only where actual cause or information flow is specified. When a plot is qualitative, do not suggest measured data or numerical precision.'
  if n==2: intro+=' This is one half of a coordinated pair for the same chapter; make this half self-contained with only the assigned scenes. Other scenes appear in the paired image. Do not copy the pair plan or scene IDs into the artwork.'
  body=[]; ids=[]
  for ix in indices:
   s=scenes[ix]; pids=s.get('source_item_ids',[]); ids.extend(pids)
   obj=s.get('visible_objects',[]); obj=', '.join(map(str,obj)) if isinstance(obj,list) else str(obj)
   rel=s.get('depicted_relationship_or_change',''); teach=s.get('teaching_contribution_beyond_labels','')
   body.append(f"Scene {ix+1}, short heading '{labels[ix]}': draw {obj}. Show: {rel} Why this matters visually: {teach}")
  evidence='\n'.join('- '+str(pid)+': '+str(points[pid]) for pid in dict.fromkeys(ids) if pid in points)
  cautions='\n'.join('- '+str(c) for c in d.get('constraints',[]) if not any(x in str(c).lower() for x in ['coverage','acceptance','inspecting','review']))
  prompt=intro+'\n\n'+'\n\n'.join(body)+'\n\nSource-grounded meanings and constraints (do not print these paragraphs):\n'+evidence+'\n'+cautions+'\nUse only concise visible labels needed to make scene relationships intelligible. Do not put source IDs, instructions, review notes, captions or alt text in the artwork.'
  dest=out/(asset+'-prompt.txt'); dest.write_text(prompt,encoding='utf-8')
  manifest['assets'].append({'asset_id':asset,'prompt':str(dest).replace('\\','/'),'brief':str(path).replace('\\','/'),'brief_sha256':hashlib.sha256(raw).hexdigest(),'scene_indices':[i+1 for i in indices],'planned_point_ids':list(dict.fromkeys(ids)),'pair_id':name if n==2 else None,'status':'ready_for_draft_generation_review_pending','insertion_authorized':False})
(out/'manifest.json').write_text(json.dumps(manifest,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
print('Prepared',len(manifest['assets']),'prompts across',len(tasks),'locations')
for x in manifest['assets']: print(x['asset_id'],len(x['planned_point_ids']),'planned points')

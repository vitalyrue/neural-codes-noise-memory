from pathlib import Path
import json,re
OUT=Path(__file__).resolve().parent
read=lambda n:json.loads((OUT/n).read_text(encoding='utf-8'))
groups=[]
for name in ['proposal-foundations-memory.json','proposal-information-eye.json','proposal-place-synthesis.json']:groups+=read(name)['groups']
settings=[
 ('01-foundations.md','01-foundations.md','FOUNDATIONS','Patterns of variable spikes can represent a value',[]),
 ('01-foundations.md','01b-persistence.md','PERSISTENCE','Stable representations can accumulate error',['FOUNDATIONS']),
 ('02-memory-dynamics.md','02-memory-dynamics.md','MEMORY-DYNAMICS','Spiking noise produces diffusion along the memory attractor',['PERSISTENCE']),
 ('02-memory-dynamics.md','02b-memory-long-delays.md','MEMORY-LONG-DELAYS','Boundaries and drift change memory error over long delays',['MEMORY-DYNAMICS']),
 ('03-memory-information.md','03-memory-information.md','MEMORY-INFORMATION','Spike information limits memory stability',['MEMORY-DYNAMICS','MEMORY-LONG-DELAYS']),
 ('03-memory-information.md','03b-memory-readout.md','MEMORY-READOUT','Readout accuracy depends on how a moving memory is observed',['MEMORY-INFORMATION']),
 ('04-eye-drift.md','04-eye-drift.md','EYE-DRIFT','Eye drift points to a shared neural drive',['PERSISTENCE','MEMORY-DYNAMICS']),
 ('04-eye-drift.md','04b-eye-timing.md','EYE-TIMING','Drift growth distinguishes diffusion from filtered white noise',['EYE-DRIFT']),
 ('04-eye-drift.md','04c-eye-circuit.md','EYE-CIRCUIT','A noisy memory circuit can produce eye drift',['EYE-DRIFT','EYE-TIMING','MEMORY-INFORMATION']),
 ('05-place-fields.md','05-place-fields.md','PLACE-FIELDS','Field counts and gaps reveal threshold and scale',['FOUNDATIONS','PERSISTENCE']),
 ('05-place-fields.md','05b-place-sizes.md','PLACE-SIZES','High peaks explain size laws across dimensions',['PLACE-FIELDS']),
 ('05-place-fields.md','05c-place-tests.md','PLACE-TESTS','Holes and measurements test the spatial explanation',['PLACE-FIELDS','PLACE-SIZES']),
 ('06-synthesis.md','06-synthesis.md','SYNTHESIS','Spatial maps and memory dynamics need separate tests',['MEMORY-READOUT','EYE-CIRCUIT','PLACE-TESTS'])]
assert len(groups)==len(settings)
originals={}
for g,(original,file,key,title,prereqs) in zip(groups,settings):
 opening=g['opening_paragraphs'].copy()
 if key=='PERSISTENCE':opening[0]+='[^f-memory]'
 if key=='MEMORY-DYNAMICS':
  opening[0]+='[^p1-model]'
  old=(OUT/'baseline/content/chapters'/original).read_text(encoding='utf-8').split('\n## ',1)[0].split('\n\n')
  opening+=old[-2:]
 if key=='MEMORY-LONG-DELAYS':opening.append('Here $\\theta$ is the current stored value and $\\Theta$ its common initial value across trials. The local diffusion coefficient $D(\\theta)$ comes from the weak spike fluctuations derived in the [preceding chapter](ch-memory-dynamics.html#sec-memory-diffusion), after stable disturbances have relaxed. For constant $D$, displacement variance is $2Dt$ before boundaries matter and when there is no systematic drift.')
 if key=='MEMORY-INFORMATION':opening.append('We retain the memory coordinate $\\theta$, initial value $\\Theta$, firing rate $\\bar r_i(\\theta)$, synaptic time constant $\\tau$, and diffusion convention $\\operatorname{Var}(\\Delta\\theta)=2D\\Delta t$. The [network projection](ch-memory-dynamics.html#sec-memory-linearization) determines which activity changes remain as changes in the stored value.')
 if key=='MEMORY-READOUT':opening[-1]=opening[-1].replace('The spike information rate $J$','The [spike information rate $J$](ch-memory-information.html#sec-memory-fi)')
 if key=='PLACE-SIZES':opening[-1]+=' The firing rule remains $F(x)=a[z(x)-q]_+$, where $[u]_+=\\max(u,0)$.'
 if key=='PLACE-TESTS':opening[-1]=opening[-1].replace('As before, q is','As before, $q$ is').replace('and a converts','and $a$ converts')
 group={'file':file,'id':'ch:'+key,'title':title,'sections':[s for s in g['section_ids'] if s!='sec:SYNTHESIS-COVARIANCE-EXAMPLE'],'opening':opening,'prerequisites':['ch:'+x for x in prereqs],'rationale':g['rationale'],'original_opening_disposition':g.get('original_opening_disposition',g.get('old_opening_disposition'))}
 originals.setdefault(original,{'file':original,'groups':[]})['groups'].append(group)
(OUT/'selected-plan.json').write_text(json.dumps({'status':'root selected draft for independent review','originals':list(originals.values()),'decision':'13 chapters. Complete original sections retain order. Original six chapter URLs kept for first pieces, with redirects for moved stable anchors.','alternatives':'Compared 3-way memory split and 4/4/4 eye split; accepted reviewer rationale for keeping complete calculations and inferences together. Synthesis remains a single connected lesson.'},indent=2),encoding='utf-8')

edits={
'01-foundations.md':[
 ['Chapter 4 supplies that model for eye displacement.','The [eye-drift covariance calculation](ch-eye-drift.html#sec-eye-chi) supplies that model for eye displacement.'],
 ["Chapter 2 derives the correct projection from the network's linearized dynamics.","The [network calculation](ch-memory-dynamics.html#sec-memory-linearization) derives the correct projection from the network's linearized dynamics."]],
'02-memory-dynamics.md':[
 ['Systematic drift requires a separate check below.','Systematic drift requires a [separate check in the next chapter](ch-memory-long-delays.html#sec-memory-drift-scope).'],
 ['as in the tilted two variable example above.','as in the [tilted two variable example](ch-memory-dynamics.html#sec-memory-linearization).'],
 ['The next chapter derives this second uncertainty and relates it to the first.','The [information calculation](ch-memory-information.html#sec-memory-fi) measures this second uncertainty and relates it to diffusion; the [readout chapter](ch-memory-readout.html) then follows observation of the moving state.']],
'03-memory-information.md':[
 ['From the preceding chapter,','From the [projection and diffusion calculation](ch-memory-dynamics.html#sec-memory-diffusion),'],
 ['The mutual-excitation example in Chapter 2 supplies','The [mutual-excitation example](ch-memory-long-delays.html#sec-memory-long-time) supplies'],
 ['including the linear-family counterexample already derived.','including the [linear-family counterexample](ch-memory-information.html#sec-memory-bound) already derived.']],
'04-eye-drift.md':[
 ['the continuous attractor described in Chapters 1 and 2','the continuous attractor described in the [foundations](ch-persistence.html#sec-foundations-attractor) and [network model](ch-memory-dynamics.html#sec-memory-spikes)'],
 ['As in Chapter 1,','Using the [earlier definition of mean squared displacement](ch-foundations.html#sec-foundations-covariance),'],
 ['Chapter 1 defined the interspike interval coefficient of variation (CV) as','The [spike variability section](ch-foundations.html#sec-foundations-poisson) defined the interspike interval coefficient of variation (CV) as'],
 ['Chapters 2 and 3 show how projecting those fluctuations','The [diffusion calculation](ch-memory-dynamics.html#sec-memory-diffusion) and [information bound](ch-memory-information.html#sec-memory-bound) show how projecting those fluctuations'],
 ['Using the information-diffusion relation of Chapter 3 as a scale,','Using the [information-diffusion relation](ch-memory-information.html#sec-memory-bound) as a scale,'],
 ['connected to Chapters 2–3.','connected to the guide’s diffusion and information calculations.']],
'05-place-fields.md':[
 ['the Euler characteristic calculation below.','the [Euler characteristic calculation](ch-place-tests.html#sec-place-topology).'],
 ['Return to the crossing integral and retain','Return to the [crossing integral](ch-place-fields.html#sec-place-kac-rice) and retain'],
 ['compared with the exact stationary crossing result $3.746$ m,','compared with the [exact stationary crossing result](ch-place-fields.html#sec-place-inference) $3.746$ m,']]
}
(OUT/'reference-edits.json').write_text(json.dumps(edits,indent=2,ensure_ascii=False),encoding='utf-8')
print('Selected 13 chapters and recorded explicit reference repairs.')

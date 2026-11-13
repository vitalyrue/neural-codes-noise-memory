from pathlib import Path
from datetime import datetime
import json,hashlib,re
OUT=Path(__file__).resolve().parent;ROOT=OUT.parents[1]
sources={n:(OUT/'baseline/content/chapters'/n).read_text(encoding='utf-8') for n in ['00-reading-guide.md','06-synthesis.md','glossary.md']}
texts=sources.copy();edits=[]
def change(file,start,new,kind,reason,limits):
 text=texts[file];pieces=text.splitlines() if file=='glossary.md' else text.split('\n\n');matches=[p for p in pieces if p.startswith(start)];assert len(matches)==1,(file,start)
 old=matches[0];assert text.count(old)==1
 edits.append({'file':'content/chapters/'+file,'location':start,'before':old,'after':new,'kind':kind,'reason':reason,'preserved_conditions':limits})
 texts[file]=text.replace(old,new)
def term(t):return '[**'+t+'**]{.definition-term custom-style="Definition Term"}'

f='00-reading-guide.md'
old=next(p for p in texts[f].split('\n\n') if p.startswith('These questions belong'))
change(f,'These questions belong',old.replace("groups of neurons, the brain's signaling cells", "groups of "+term('neuron')+"s, the brain's signaling cells"),'definition','The sentence already explains neuron; show its first teaching occurrence in blue.','Definition wording and scope unchanged.')
old=next(p for p in texts[f].split('\n\n') if p.startswith('Even while gaze'))
change(f,'Even while gaze',old.replace('the retina, the light-sensitive tissue','the '+term('retina')+', the light-sensitive tissue'),'definition','Mark the existing explanation of the tissue receiving the visual signal.','The question about neural versus muscular origin remains.')
old=next(p for p in texts[f].split('\n\n') if p.startswith('A [**place cell**]'))
change(f,'A [**place cell**]',old.replace('in the hippocampus, a brain region','in the '+term('hippocampus')+', a brain region'),'definition','Mark the existing first anatomical explanation.','No anatomy or field-definition claim changed.')
change(f,'The guide assumes',
'''The guide assumes undergraduate calculus, basic probability, and linear algebra. Neuroscience terms and the required stochastic-process, information, filtering, and random-field ideas are taught where needed. The reading path builds from the signals to the models and then their tests:

- **Chapters 1–2:** establish [neural signals and variability](../chapters/ch-foundations.html), then [persistence and accumulated error](../chapters/ch-persistence.html).
- **Chapters 3–6:** derive memory diffusion, its long-delay behavior, the information bound, and readout.
- **Chapters 7–9:** follow the eye study from shared-drive evidence through timing to a circuit model.
- **Chapters 10–12:** develop spatial maps, their size predictions, and tests of their shapes and possible origins.
- **Chapter 13:** connect the results and compare related work.''',
'list','The five stages are easier to find as a reading map. Remove the redundant promise about chapter openings.','All chapter ranges, subjects, links and assumed knowledge remain.')
change(f,'For the memory and eye papers,',
'''For a path focused on particular papers:

- **Memory and eye drift:** follow chapters 1 through 9 in order.
- **Place fields:** read the two foundations chapters and then chapters 10–12. The spatial calculation does not require the readout derivation in chapter 6.

The Glossary gives short definitions for lookup after their first explanation. The References section gives full source details. The original paper figures are discussed by number and can be inspected in the linked PDFs.''',
'list','Two alternative reading paths were hidden in a paragraph; separate them without changing their prerequisites.','Both foundations chapters remain required for the place-field shortcut.')
old=next(p for p in texts[f].split('\n\n') if p.startswith('Throughout the guide,'))
prefix=old.split(' The symbol $d$')[0]
change(f,'Throughout the guide,',prefix+'''

The other recurring symbols are:

- $d$: spatial dimension.
- $\\theta$: the represented coordinate in the memory chapters.
- $q$: the normalized threshold in the place-field chapters, called $\\theta$ in that paper.
- $C$: the spatial covariance in the place-field chapters.''',
'list','Expose the symbol-to-meaning mapping after the diffusion explanation. Remove the redundant promise that later notation will be explained.','Constant diffusion, no favored direction and no boundary remain beside the MSD formula.')

f='06-synthesis.md'
change(f,'A model can explain the shape',
'''A model can explain the shape of a neural code without explaining how that code is maintained. It can also explain fluctuations inside a circuit without uniquely locating the source of a measured behavior. Comparing the three papers requires keeping each claim with the mathematical or experimental test that supports it.''',
'wording','Replace the vague claim about usefulness and the unhelpful modifier actual with the concrete requirement for comparison.','Distinct model scope and strength of behavioral inference remain.')
change(f,'For a circuit representing position,',
'''For a circuit representing position, three questions arise:

- **Spatial map:** What activity pattern corresponds to each position? The place-field model addresses this question.
- **Memory motion:** How does the represented position evolve when there is no corrective input? The persistent-activity model addresses this question.
- **Observed movement:** How does a downstream physical system transform that changing signal into an observable movement? The eye-drift model combines a candidate account of memory motion with a detailed account of this transformation.[^s-three]''',
'list','Pair each independent question with the model that addresses it, replacing first/second/third backtracking.','Eye drift still uses a candidate account of memory motion; no unique biological source is claimed.')
old=next(p for p in texts[f].split('\n\n') if p.startswith('The 2012 and 2022 connection'))
change(f,'The 2012 and 2022 connection',old.replace('The 2025 connection is broader: an internally coherent position estimate can be expressed through spatially irregular tuning curves.','The place-field model describes spatially irregular tuning curves. To connect those curves to memory dynamics, we must also specify how the represented position moves.'),
'transition','State the missing ingredient that motivates the next section’s composed rate function.','The direct 2012/2022 connection and limits on the 2022 information-bound evidence remain unchanged.')
change(f,'This example explains why irregular',
'''Irregular single-cell responses can therefore coexist with population changes along just one direction. To test whether a shared position error causes that pattern, one must measure how the rate changes align with the tuning curves. Field shapes alone do not supply that evidence.''',
'transition','Replace the unexplained low-dimensional label with the line just shown, and state the measurement needed before the evidence section.','The example is still a single shared-displacement calculation, with extra private noise already qualified in the preceding paragraphs.')
old=next(p for p in texts[f].split('\n\n') if p.startswith('A model that matches one distribution'))
change(f,'A model that matches one distribution',
'''The shared-position calculation predicts how rates would change together. Establishing that connection requires measurements of those changes as well as the spatial maps. Each paper tests a different part of the proposed connection:

- **Place-field statistics:** '''+old,
'list, transition','Connect the covariance example to evidence, and label the first of three distinct tests.','The entire fitted-parameter, gain and limiting-approximation qualification is retained verbatim.')
old=next(p for p in texts[f].split('\n\n') if p.startswith('The eye paper uses a different strategy.'))
change(f,'The eye paper uses a different strategy.', '- **Eye drift:** '+old.replace('The eye paper uses a different strategy. It calibrates','The eye paper calibrates'),
'list','Make the second evidence category visible; the label replaces a generic transition.','Calibration, independence assumptions, temporal comparison, two animals and horizontal-motion scope remain.')
old=next(p for p in texts[f].split('\n\n') if p.startswith('The 2012 inequality is a mathematical constraint'))
change(f,'The 2012 inequality is a mathematical constraint','- **Memory stability:** '+old,
'list','Keep mathematical proof distinct from the empirical comparisons in parallel evidence items.','All compatible-noise/dynamics conditions and the insufficient 1/N check remain.')
old=next(p for p in texts[f].split('\n\n') if p.startswith("The foundational eye-position account"))
new=old.replace('The foundational eye-position account is', 'The eye-position account begins with').replace("Burak and Fiete's earlier grid-cell study puts a related integrator problem in navigation: recurrent population activity is driven by velocity and accumulates path-integration errors.", "Burak and Fiete's earlier grid-cell study examines "+term('path integration')+", updating a position estimate from movement. In its model, velocity drives recurrent population activity, and errors accumulate in the position estimate.")
change(f,'The foundational eye-position account',
'''Related studies test the assumptions and ask questions the three papers leave open:

- **Integrating movement:** '''+new,
'list, definition, wording','Introduce the related-work groups and explain path integration at its first teaching use. Remove foundational, which adds no distinct fact.','The earlier studies do not supply the macaque estimate; simulated accuracy remains limited to their networks and parameters.')
for start,label in [('Noise-driven storage also connects','Storage capacity and changing synapses'),('For place fields, Eliav','Recordings from larger environments'),('There are also direct reasons','Connectivity and learning'),('Finally, the source and use','Benefits for perception')]:
 old=next(p for p in texts[f].split('\n\n') if p.startswith(start));new=old
 if start.startswith('There are'):
  new=new.replace('There are also direct reasons to avoid reading Gaussian spatial statistics as a unique wiring diagram.','Gaussian spatial statistics do not identify a unique pattern of connections.')
  new=new.replace('events in dendrites, the branching input structures','events in '+term('dendrite')+'s, the branching input structures')
 if start.startswith('Finally'):new=new.replace('Finally, the source and use','The source and use')
 change(f,start,'- **'+label+':** '+new,'list'+(', definition' if start.startswith('There are') else ''),'Expose the independent contribution of this group of related studies. Preserve the explanatory paragraph inside its list item.','All citations, experimental-versus-reanalysis distinctions and limits on circuit or sensory inference remain.')
change(f,'The combined calculation suggests a concrete research direction.',
'''A joint test needs tuning maps and fluctuations from the same population. A possible sequence is:

1. Estimate the tuning maps and their uncertainty.
2. Measure fluctuations when external signals provide little correction of the represented position. Test whether their covariance aligns with the changes implied by the tuning maps.
3. Fit diffusion only over a range where the local approximation and measurement corrections are justified.
4. **If comparing behavior,** include the physical or neural filters between the representation and the measurement.''',
'list, transition, wording','Turn the proposed measurement procedure into numbered steps. Explain weak external anchoring in ordinary words and preserve the conditional behavioral comparison.','Same-population requirement, uncertainty, local-fit conditions and filters remain. The following paragraph still identifies this as proposed follow-up, not a replication.')

# New glossary entries mirror the actual first explanations, without replacing old entries.
definitions={
 'dendrite':'A branching input structure of a neuron.',
 'hippocampus':'A brain region involved in memory and navigation.',
 'neuron':"A signaling cell in the nervous system.",
 'path integration':'Updating an estimate of position from movement.',
 'retina':'The light-sensitive tissue at the back of the eye.'}
for name,definition in definitions.items():
 text=texts['glossary.md'];entry='- '+term(name+':')+' '+definition
 items=list(re.finditer(r'(?m)^- \[\*\*([^*]+):\*\*\].*$',text))
 later=next((m for m in items if m.group(1).casefold()>name.casefold()),None)
 old=later.group(0) if later else items[-1].group(0)
 new=entry+'\n'+old if later else old+'\n'+entry
 change('glossary.md',old,new,'definition','Add a lookup entry matching the new blue first teaching occurrence.','Glossary definition matches the teaching sentence; existing entries are retained.')
report={'at':datetime.now().astimezone().isoformat(),'group':'root-orientation-synthesis','baseline_hashes':{f:hashlib.sha256((OUT/'baseline/content/chapters'/f).read_bytes()).hexdigest() for f in sources},'edits':edits,'new_glossary_terms':definitions,'retained_decisions':['Keep the three paper overviews as question, method, result and implication paragraphs; their methods form connected explanations rather than independent lists.','Retain the synthesis symbolic derivation and numerical example as connected prose and equations.','Keep the three model-coordinate meanings in a paragraph beside the existing comparison table; another list would duplicate the new question list and table.','Keep the chapter order and all headings, captions, typed tables, paper links and folded notes.']}
(OUT/'changes-root.json').write_text(json.dumps(report,indent=2,ensure_ascii=False),encoding='utf-8')
for f,t in texts.items():(OUT/'proposed/content/chapters'/f).write_text(t,encoding='utf-8',newline='\n')
print(json.dumps({'edits':len(edits),'files':list(texts),'at':report['at']}))

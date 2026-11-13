from pathlib import Path
from datetime import datetime, timezone
import json,re,csv,hashlib,yaml

root=Path(__file__).resolve().parents[2]; task=Path(__file__).resolve().parent
chap=root/'content/chapters'
specs=[
 ('11-simulating-memory','ch:SIMULATING-MEMORY',['ch:MEMORY-DYNAMICS','ch:MEMORY-LONG-DELAYS']),
 ('12-simulating-eye-drift','ch:SIMULATING-EYE',['ch:SIMULATING-MEMORY','ch:EYE-CIRCUIT']),
 ('13-simulating-place-fields','ch:SIMULATING-PLACE',['ch:PLACE-FIELDS','ch:PLACE-TESTS']),
 ('14-simulation-tools','ch:SIMULATION-TOOLS',['ch:SIMULATING-MEMORY','ch:SIMULATING-EYE','ch:SIMULATING-PLACE'])]
def metadata(filename,cid,prereqs):
    text=(chap/f'{filename}.md').read_text(encoding='utf-8')
    title=re.search(r'^# (.+?) \{#',text).group(1)
    purpose=text.split('\n\n')[1]
    sections=[]
    for m in re.finditer(r'^## (.+?) \{#(sec:[^}]+)\}\n\n',text,re.M):
        sections.append(dict(id=m[2],title=m[1],summary=text[m.end():].split('\n\n')[0],level=2))
    data=dict(chapter_id=cid,part_id='part:SIMULATIONS',title=title,purpose=purpose,role='chapter',page_break_before=True,pedagogical_prerequisites=prereqs,explicit_render_dependencies=[],discovered_references=[],navigation_dependencies=['part:SIMULATIONS'],section_list=sections,blocks=[],source_loci=[])
    if cid=='ch:SIMULATION-TOOLS':
        data['blocks']=[dict(id='tbl:SIMULATION-TOOLS',kind='table',placement='sec:SIMULATION-TOOLS-SOFTWARE',headers=['Tool or package','Role','Status in this guide'],rows=[
          ['MATLAB author code','Time-stepped integrator and eye model; parameter fitting and MSD analysis','Released for Ben-Shushan et al. (2022); source inspected, full runs not repeated'],
          ['Python 3.11, NumPy and SciPy','Generate and process spatial maps; measure fields, peaks and distributions','Reported or verified in Mainali et al. (2025) and its archived code'],
          ['Gudhi','Compute Betti numbers used in Euler characteristic measurements','Reported by Mainali et al. (2025)'],
          ['SciPy solve_ivp','Integrate deterministic ordinary differential equations','Optional reconstruction tool; stochastic events need additional rules'],
          ['Brian 2','Specify spiking-network equations and event handling','Optional alternative; equations and spike statistics must match the chosen model']
        ],caption='Software roles and the evidence for their use.',first_column_role='row-labels',html_fold='never')]
    (chap/f'{filename}.yaml').write_text(yaml.safe_dump(data,sort_keys=False,allow_unicode=True,width=108),encoding='utf-8')
for spec in specs: metadata(*spec)

planpath=root/'plan/chapter-plan.yaml'; plan=yaml.safe_load(planpath.read_text(encoding='utf-8'))
assert len(plan['book']['parts'])==3
P1='[Burak and Fiete (2012)](https://doi.org/10.1073/pnas.1117386109)'
P2='[Ben-Shushan et al. (2022)](https://doi.org/10.1038/s41467-022-29201-y)'
P3='[Mainali et al. (2025)](https://doi.org/10.1016/j.neuron.2025.01.017)'
legend='The contribution labels describe the role of the result here: **central** is a main finding of the cited paper; **supporting** establishes or qualifies that finding; **background** supplies needed concepts; **guide-derived** identifies an explanation, comparison, or proposed test developed in this guide.'
maps={
'part:MECHANISMS':[
 f'**Chapter 1, background:** Neural firing rates and spike variability supply the quantities needed for the later memory calculation. {P1} supplies the Poisson network model; {P2} and {P3} supply eye-control and spatial-coding context. The elementary numerical examples are guide-derived.',
 f'**Chapter 2, background and mechanism:** A stable pattern of neural activity can retain a value while noise moves that value along a family of states. This is the continuous-memory setup of {P1}; the two-variable illustrations are guide-derived.',
 f'**Chapter 3, central result:** {P1} derives memory diffusion by projecting spike fluctuations through the network dynamics. The symmetric formula uses the authors\' [2017 correction](https://doi.org/10.1073/pnas.1706051114). Expanded projection examples are guide-derived.',
 f'**Chapter 4, supporting results:** {P1} explains long-delay behavior, angular boundaries, and state-dependent diffusion. These qualify how the central diffusion result can be used. The guide adds explicit boundary calculations and distinguishes its checks of other printed equations from the official correction.',
 f'**Chapter 5, central result:** {P1} relates the information in spikes to a lower bound on memory diffusion. The guide expands the proofs and labels its counterexamples and comparisons of fixed quantities.',
 f'**Chapter 6, central readout result and supporting extensions:** {P1} derives limits on estimating a value that moves during observation. Partial access and alternative time scales extend that result. The guide supplies intermediate calculations and identifies source formulas needing qualification.'
],
'part:OBSERVATIONS':[
 f'**Chapter 7, central empirical result:** {P2} infers a substantial shared drive upstream of ocular motor neurons from recorded eye motion and spikes. The filter and covariance calculations explain the assumptions behind that inference.',
 f'**Chapter 8, supporting test:** {P2} compares displacement statistics with the predictions of mechanical filtering and private motor noise. The one-filter calculation is a guide-derived teaching model, distinct from the full simulation.',
 f'**Chapter 9, central proposed explanation:** {P2} shows that a noisy integrator model can account for the motion after muscle filtering and delayed feedback. [Aksay et al. (2007)](https://doi.org/10.1038/nn1877) supplies supporting circuit architecture. The match supports a possible source, rather than uniquely identifying it.',
 f'**Chapter 10, central spatial model:** {P3} describes fields and gaps as regions of a smooth random input above or below threshold. Expanded crossing and parameter-inference calculations are guide-derived.',
 f'**Chapter 11, central size predictions:** {P3} derives dimension-dependent field-size statistics and compares them with recordings. The guide expands the local-peak derivation and separates limiting laws from finite-threshold behavior.',
 f'**Chapter 12, supporting tests and circuit interpretation:** {P3} examines shapes, slices, and connectedness beyond the fitted summaries. The underlying recordings include [Eliav et al. (2021)](https://doi.org/10.1126/science.abg4020), [Harland et al. (2021)](https://doi.org/10.1016/j.cub.2021.03.003), and [Yartsev and Ulanovsky (2013)](https://doi.org/10.1126/science.1235338). Gaussian maps constrain possible inputs without uniquely identifying wiring.',
 f'**Chapter 13, guide-derived synthesis:** The comparison joins the questions asked by {P1}, {P2}, and {P3}. Its common-displacement calculation and proposed joint experiment are developed here; the three papers did not jointly test that model.'
],
'part:HARDWARE':[
 '**Chapter 14, background and hardware mechanisms:** von Neumann (1958) motivates the comparison. [Pehle et al. (2022)](https://doi.org/10.3389/fnins.2022.795876), Intel Labs (2021), Scholze et al. (2026), and [Le Gallo et al. (2023)](https://doi.org/10.1038/s41928-023-01010-1) supply the architecture descriptions. Separating stored weights, changing neural states, and remembered values is the guide\'s organizing comparison.',
 f'**Chapter 15, central neural distinction with supporting hardware examples:** [Seung (1996)](https://doi.org/10.1073/pnas.93.23.13339) and {P1} explain graded persistence and noise. [Massoud and Horiuchi (2011)](https://doi.org/10.1109/TCSI.2010.2055310) and [Giulioni et al. (2012)](https://doi.org/10.3389/fnins.2011.00149) supply distinct silicon demonstrations. The reduced feedback and error comparisons are guide-derived.',
 '**Chapter 16, central results of selected hardware studies:** [Kleyko et al. (2025)](https://doi.org/10.1038/s41467-025-55832-y) tests temporal computation; [Aitsam et al. (2026)](https://doi.org/10.3389/fnins.2026.1910808) demonstrates persistent spatial activity; [Ortner et al. (2025)](https://doi.org/10.1038/s41467-025-56345-4) studies adaptation with phase-change computing; [Wang et al. (2026)](https://doi.org/10.1038/s41563-025-02361-0) studies material-state stability; [Sun et al. (2026)](https://doi.org/10.1038/s42256-026-01255-3) evaluates a proposed dual-memory design. These results concern different kinds of memory, as the chapter explains.',
 f'**Chapter 17, guide-derived experiments:** The proposed measurements combine the diffusion and readout questions of {P1}, the output-filtering lesson of {P2}, and the spatial-versus-temporal distinction exposed by {P3}. They are suggested tests, not a reported common hardware experiment.'
]
}
purposes={
'part:MECHANISMS':f'In a model neural circuit, a pattern of firing rates across many nerve cells can represent a remembered angle. Random spike timing can change that angle while activity persists. The central source, {P1}, derives how quickly accuracy can be lost and how well the value can be read. Chapters 1 and 2 establish the background; Chapters 3 and 5 develop the central diffusion and information results; Chapters 4 and 6 explain long-delay behavior and readout. Expanded examples and marked checks of printed formulas are guide-derived.',
'part:OBSERVATIONS':f'These studies connect neural activity to eye control in monkeys and location in rodents and bats. {P2} supplies the central shared-drive inference and a possible integrator explanation in Chapters 7 to 9. {P3} supplies the spatial model, field-size predictions, and supporting shape tests in Chapters 10 to 12. Chapter 13 is a guide-derived comparison of those results with Burak and Fiete (2012). The order follows each signal from its modeled neural origin to the measured behavior or spatial pattern.',
'part:HARDWARE':"Electronic circuits can store connection settings, changing neuron states, and values represented by a network. Von Neumann (1958) motivates this comparison. Chapters 14 and 15 connect physical storage with Seung (1996) and Burak and Fiete (2012). Chapter 16 examines the separate contributions of selected hardware studies through October 30, 2026. Chapter 17 develops guide-derived experiments using the three original papers. Each contribution is attributed in the Part introduction."
}
for part in plan['book']['parts']:
    pid=part['part_id'];part['purpose']=purposes[pid]
    if pid!='part:HARDWARE':
        part['content']=[dict(type='paragraph',text=part['purpose'])]
    part['content'] += [dict(type='paragraph',text=legend),dict(type='paragraph',text='\n\n'.join('- '+s for s in maps[pid]))]

simpart=dict(part_id='part:SIMULATIONS',title='Simulations connect model assumptions to measurable outcomes',purpose=f'{P1} tests memory diffusion in spiking networks. {P2} connects a simulated neural command to eye motion. {P3} generates spatial maps and compares their fields with recordings. This Part explains the methods, measurements, and actual software behind those studies, then gives a guide-derived route for checking a reproduction.',content=[
 dict(type='paragraph',text='A formula predicts behavior under stated assumptions. A simulation lets us generate the resulting neural activity, eye motion, or spatial map and measure it in the same way as a theoretical prediction or experiment. The useful question is what each computation adds to the evidence, and which physical assumptions determine its output.'),
 dict(type='paragraph',text=legend),
 dict(type='paragraph',text='\n\n'.join([
 f'- **Chapter 18, supporting simulations of a central theory:** {P1} compares stochastic network trajectories with its analytical diffusion prediction. The 2017 correction applies to Eq. 2. The simulations test the modeled dynamics, rather than measure memory errors in animals.',
 f'- **Chapter 19, model support for a central explanation:** {P2} combines recorded-data analysis with a noisy integrator, motor neurons, muscles, and delayed feedback. Aksay et al. (2007) supplies supporting circuit architecture. The generated signals test whether that mechanism can reproduce the measured statistics.',
 f'- **Chapter 20, central model comparisons:** {P3} generates thresholded Gaussian spatial maps, fits selected summaries, and tests additional field properties. Original animal recordings supply the comparison data. These are static-map simulations rather than recurrent memory dynamics.',
 '- **Chapter 21, guide-derived methods and tool comparison:** The shared reproduction procedure is assembled here from the three studies. Author code is distinguished from optional numerical tools. No new full-paper reproduction is claimed.'
 ])),
 dict(type='paragraph',text='The path begins with the simplest causal chain: recurrent spikes move a stored value. It then adds the motor pathway and measurement procedure needed to compare an internal command with behavior. The spatial-field study changes the independent variable from time to position. With those differences established, the final chapter explains how to choose software and check numerical resolution.'),
 dict(type='paragraph',text='Paper-specific numerical settings and implementation cautions are folded. The main text keeps the modeled objects, actions, measurements, and limits visible. Blue definitions introduce simulation terms; basic expectation, variance, standard deviation, and probability density are assumed.')
],chapters=[s[1] for s in specs])
plan['book']['parts'].append(simpart)
planpath.write_text(yaml.safe_dump(plan,sort_keys=False,allow_unicode=True,width=110),encoding='utf-8')

# Narrow source correction: the formula stays unchanged.
p=chap/'02-memory-dynamics.md';t=p.read_text(encoding='utf-8')
old='The supplied Early Edition [main Eq. 2, p. 2](../papers/burak-fiete-2012-persistent-activity.pdf#page=2&zoom=125,0,88) appears to omit the square on $g_i\'$ in the numerator. The projection calculation and SI S18 give the squared expression shown here. This is an independent source check, not an author-confirmed correction.'
new='The supplied Early Edition [main Eq. 2, p. 2](../papers/burak-fiete-2012-persistent-activity.pdf#page=2&zoom=125,0,88) omits the square on $g_i\'$ in the numerator. [Burak and Fiete\'s published correction (2017)](https://doi.org/10.1073/pnas.1706051114) confirms the squared expression shown here, which also follows from the projection calculation and SI S18. The guide\'s checks of other printed formulas remain separate from that correction.'
assert old in t;t=t.replace(old,new);p.write_text(t,encoding='utf-8')

p=chap/'00-reading-guide.md';t=p.read_text(encoding='utf-8')
newsection='''## Simulations separate the model from the evidence used to test it {#sec:READING-SIMULATIONS}

[Part IV](../parts/part-simulations.html) follows the computational methods in Burak and Fiete (2012), Ben-Shushan et al. (2022), and Mainali et al. (2025). It distinguishes simulated neural trajectories, recorded-data analysis, and generated spatial maps. Each chapter identifies the model states, numerical procedure, measurements, available code, and limits on reproducing the published figures. The final chapter compares tools and explains resolution and repeatability checks. These are explanations of the sources, not a claim that the guide reran their full simulations.

Part introductions now identify the paper behind each chapter's result using author and year. **Central** marks a main finding of that paper. **Supporting** marks an analysis used to establish or qualify it. **Background** supplies needed concepts. **Guide-derived** marks expanded explanations, comparisons, or proposed tests developed here. A result can be central in its own paper while serving as supporting evidence in another argument.

'''
anchor='## '
start=t.index('## Electronic implementations')
insert=t.index(anchor,start+3)
t=t[:insert]+newsection+t[insert:];p.write_text(t,encoding='utf-8')
# Synchronize only the new frontmatter section; retain other metadata.
p=chap/'00-reading-guide.yaml';data=yaml.safe_load(p.read_text(encoding='utf-8'))
entry=dict(id='sec:READING-SIMULATIONS',title='Simulations separate the model from the evidence used to test it',summary=newsection.split('\n\n')[1],level=2)
i=next(i for i,x in enumerate(data['section_list']) if x['id']=='sec:READING-HARDWARE')+1
data['section_list'].insert(i,entry);p.write_text(yaml.safe_dump(data,sort_keys=False,allow_unicode=True,width=108),encoding='utf-8')

p=root/'content/index.md';t=p.read_text(encoding='utf-8').rstrip();p.write_text(t+'\n\nPart IV explains the simulations, data-analysis methods, and software used by Burak and Fiete (2012), Ben-Shushan et al. (2022), and Mainali et al. (2025). Part introductions identify the source and role of each chapter result, separating central findings, supporting work, background, and guide-derived comparisons.\n',encoding='utf-8')
p=root/'guide-project.yaml';t=p.read_text(encoding='utf-8');old='selected neuromorphic advances through 30 October 2026."';new='selected neuromorphic advances through 30 October 2026. Part IV explains the simulations, methods, and tools behind the original studies. Part introductions identify the source and role of each chapter contribution."';assert old in t;p.write_text(t.replace(old,new),encoding='utf-8')

terms=[
 ('Euler update','A numerical step that approximates change over a short interval by the current derivative times that interval.'),
 ('fitted statistic','A measured summary used to choose a model\'s parameters.'),
 ('random seed','The starting state of a pseudorandom generator, used with a specified implementation to repeat a sample sequence.'),
 ('discretization','Representing a continuous variable such as time or position with finitely many sample points.'),
 ('convergence check','A test of whether a reported quantity changes acceptably little when numerical resolution is refined.'),
 ('Monte Carlo simulation','Estimating a quantity through repeated calculations with random samples.')]
p=chap/'glossary.md';t=p.read_text(encoding='utf-8').rstrip()+'\n\n'
for term,definition in terms:t+=f'- [[**{term}:**]{{.definition-term custom-style="Definition Term"}} {definition}]{{.definition-explanation}}\n'
p.write_text(t,encoding='utf-8')

p=chap/'references.md';t=p.read_text(encoding='utf-8')
needle='[DOI](https://doi.org/10.1073/pnas.1117386109).'
assert needle in t;t=t.replace(needle,needle+' The authors\' 2017 correction restores the squared input slope in Eq. 2. [Correction DOI](https://doi.org/10.1073/pnas.1706051114).',1)
newrefs=[
'The Burak Lab. (2022). *Fixational drift is driven by diffusive dynamics in central neural circuitry* [MATLAB source code]. [Inspected revision, February 28, 2022](https://github.com/The-Burak-lab/Fixational-drift-is-driven-by-diffusive-dynamics-in-central-neuralcircuitry/tree/27d4093008c6756fe8ae2ad77567176ed626bd17).',
'Ben-Shushan, N.; Shaham, N.; Joshua, M.; Burak, Y. (2022). *Fixational drift is driven by diffusive dynamics in central neural circuitry* [Dataset]. Zenodo. [DOI](https://doi.org/10.5281/zenodo.6076911).',
'Mainali, N. (2025). *Gaussian process place-field model* [Python source code]. [Published archive](https://doi.org/10.5281/zenodo.14650881). [Inspected repository revision](https://github.com/5183nischal/gp-model/tree/eae7eab801bb6ca016b3a6ff4f35d6a47df98d6a).',
'Eliav et al. (2021). *Multiscale representation of very large environments in the hippocampus of flying bats* [Dataset]. Zenodo. [Version DOI](https://doi.org/10.5281/zenodo.4646728). The associated paper is entry 12.',
'NumPy developers. *Random Generator*, NumPy 2.5 documentation. Retrieved October 30, 2026, from the [generator documentation](https://numpy.org/doc/stable/reference/random/generator.html).',
'SciPy developers. *scipy.integrate.solve_ivp*, SciPy 1.18.0 documentation. Retrieved October 30, 2026, from the [ODE solver documentation](https://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.solve_ivp.html).',
'SciPy developers. *scipy.ndimage.label*, SciPy 1.18.0 documentation. Retrieved October 30, 2026, from the [connected-component documentation](https://docs.scipy.org/doc/scipy/reference/generated/scipy.ndimage.label.html).',
'Brian developers. *Brian 2 documentation*, version 2.11.0. Retrieved October 30, 2026, from the [simulator documentation](https://brian2.readthedocs.io/en/stable/).'
]
t+='\n\nThe following code, data, and software documentation support Part IV. The correction belongs with the original paper in entry 1.\n\n'
t+='\n\n'.join(f'{i}. {s}' for i,s in enumerate(newrefs,31))+'\n';p.write_text(t,encoding='utf-8')

for name in ['source-inventory.csv','source-coverage.csv','research-ledger.csv']:
    p=root/'source-maps'/name
    with p.open(encoding='utf-8',newline='') as f: reader=csv.DictReader(f);fields=reader.fieldnames;rows=list(reader)
    additions=[
     ('SIM-P1','P1','Main Methods p.6; Fig.2; SI Fig.S1 and Section VI','ch:SIMULATING-MEMORY','https://doi.org/10.1073/pnas.1117386109','2012','Network simulations and their relation to analytical predictions','memory-sources.md'),
     ('SIM-P1-CORRECTION','P1-Correction2017','Corrected Eq.2','sec:MEMORY-SYMMETRIC; ch:SIMULATING-MEMORY','https://doi.org/10.1073/pnas.1706051114','2017','Official correction confirms squared input slope; unrelated guide checks remain independent','memory-sources.md'),
     ('SIM-P2','P2','Methods pp.9–11; Figs.3–5; SI controls','ch:SIMULATING-EYE','https://doi.org/10.1038/s41467-022-29201-y','2022','Recordings, integrator/eye model and causal controls','eye-sources.md'),
     ('SIM-P2-CODE','P2-Code','Commit 27d4093; Run_model.m and Full_model_simulation.m','ch:SIMULATING-EYE; ch:SIMULATION-TOOLS','https://github.com/The-Burak-lab/Fixational-drift-is-driven-by-diffusive-dynamics-in-central-neuralcircuitry/tree/27d4093008c6756fe8ae2ad77567176ed626bd17','2022','Actual MATLAB update and sampling; identified paper/code differences','eye-sources.md'),
     ('SIM-P2-DATA','P2-Data','Zenodo recording format and file inventory','ch:SIMULATING-EYE','https://doi.org/10.5281/zenodo.6076911','2022','Raw recording availability differs from processed empirical MSD','eye-sources.md'),
     ('SIM-P3','P3','STAR Methods e1–e3; Figs.1–5; SI S1–S5','ch:SIMULATING-PLACE','https://doi.org/10.1016/j.neuron.2025.01.017','2025','Spatial generation, fitting, measurements and empirical comparisons','place-sources.md'),
     ('SIM-P3-CODE','P3-Code','Published archive 14650881; field generation and analysis functions','ch:SIMULATING-PLACE; ch:SIMULATION-TOOLS','https://doi.org/10.5281/zenodo.14650881','2025','Actual Python code; filter-width convention and incomplete per-figure run records','place-sources.md'),
     ('SIM-P3-DATA','P3-Data','Public bat-tunnel dataset metadata','ch:SIMULATING-PLACE','https://doi.org/10.5281/zenodo.4646728','2021','Public data and additional shared-map access limits','place-sources.md'),
     ('SIM-NUMPY','NumPy-Docs','Generator role and repeatability','ch:SIMULATION-TOOLS','https://numpy.org/doc/stable/reference/random/generator.html','2.5','Optional random sampling; seed and environment recording','tool-sources.md'),
     ('SIM-ODE','SciPy-ODE','solve_ivp interface','ch:SIMULATION-TOOLS','https://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.solve_ivp.html','1.18.0','Deterministic ODE integration; separate stochastic event rules','tool-sources.md'),
     ('SIM-LABEL','SciPy-Label','Input, connectivity and outputs','ch:SIMULATION-TOOLS','https://docs.scipy.org/doc/scipy/reference/generated/scipy.ndimage.label.html','1.18.0','Connected-component rule affects field statistics','tool-sources.md'),
     ('SIM-BRIAN','Brian-Docs','Introduction and model equation features','ch:SIMULATION-TOOLS','https://brian2.readthedocs.io/en/stable/','2.11.0','Optional spiking simulator, not established as source-paper tool','tool-sources.md')
    ]
    for index,(uid,sid,loc,locus,url,date,claim,evidence) in enumerate(additions,1):
        data=dict(source_unit_id=uid,source_id=sid,source_path=url,source_sha256='',unit_locator=loc,presentation_order=1000+index,unit_type='selected-method',title=claim,text_preview=claim,disposition='covered',guide_locus=locus,rationale=claim,writer_evidence=f'verification/part4-simulations-20261030/{evidence}',review_status='pending',week='self-paced',teaching_value=claim,reason='New selected method explanation; earlier source coverage retained.',claim_id=uid,claim=claim,source_title=sid,source_url=url,publication_or_version_date=date,access_date='2026-10-30',guide_location=locus,status='source verified; manuscript review pending',notes=loc)
        rows.append({k:data.get(k,'') for k in fields})
    with p.open('w',encoding='utf-8',newline='') as f:w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows(rows)

(task/'content-changes.json').write_text(json.dumps({'new_chapters':[s[0] for s in specs],'part_openings':'Existing scientific purpose retained and expanded with author-year contribution map; all existing titles/order retained.','source_correction':{'file':'02-memory-dynamics.md','old':old,'new':new},'other_existing_chapters':'Unchanged except reading-path, glossary and references additions; old section IDs/titles retained.'},indent=2),encoding='utf-8')
p=task/'STATE.json';d=json.loads(p.read_text(encoding='utf-8'));d.update(status='draft_ready',checkpoint_at=datetime.now(timezone.utc).isoformat(),remaining=['independent reviews','HTML']);p.write_text(json.dumps(d,indent=2),encoding='utf-8')
print('Integrated four chapters, four attributed Part openings, source maps and references.')

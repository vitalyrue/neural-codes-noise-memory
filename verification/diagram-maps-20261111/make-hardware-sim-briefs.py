from pathlib import Path
import hashlib,re,yaml
root=Path('.'); out=root/'verification/diagram-maps-20261111/briefs'; out.mkdir(parents=True,exist_ok=True)
base=yaml.safe_load((root/'verification/diagram-maps-20261111/ch01-brief.yaml').read_text(encoding='utf-8-sig'))
# Each tuple records a source section, a distinct teaching point and a proposed visual relationship.
C={
14:('07-hardware-memory.md','ch:HARDWARE-MEMORY','part:HARDWARE',[
('ROLES','Connection weights set influence; changing neuron and synapse states collectively encode a remembered angle.','Fixed weighted links beside two different population activity patterns'),
('ROLES','The same weights can support different cued angles and a shifting activity bump can lose the cue without changing weights.','Two cues create differently positioned bumps; one later moves'),
('ROLES','Working memory and persistent activity are not synonymous; a buffer or slowly decaying state can also retain information.','Separate persistent pattern and buffer alternatives'),
('STORAGE','SRAM stores discrete bits through powered transistor feedback; finite words have finite precision.','Cross-coupled inverters hold a bit and a short binary word'),
('STORAGE','Capacitor charge and voltage evolve under current and leakage; analog signals may be mixed with digital storage.','Current charges a leaking capacitor; digital weight store is separate'),
('STORAGE','Phase-change material retains a programmed conductance as a weight even after a changing activity state vanishes.','PCM conductance cell remains set while adjacent activity trace decays'),
('STORAGE','Device mismatch is repeatable variation between components; moment-to-moment noise can differ between trials.','Two offset device responses and separate trial fluctuations'),
('UPDATES','Digital chips update stored neural variables from incoming events, while analog circuits physically evolve voltage.','Side-by-side digital update and analog capacitor evolution'),
('UPDATES','A PCM conductance with an applied voltage and pulse duration yields a weighted electrical contribution; several currents add.','Input pulse through conductance into a current summing node')]),
15:('11-electronic-architectures.md','ch:ELECTRONIC-ARCHITECTURES','part:HARDWARE',[
('OVERVIEW','Feedback means output affects later input; different architectures store different variables.','Compare actual feedback loops and indicate state for each'),
('FLIPFLOP','Two cross-coupled inverters hold one of two powered stable states, and small perturbations return within a basin.','Two linked inverter symbols with high-low complementary states and return arrows'),
('FLIPFLOP','A recurrent spiking circuit can maintain low or high population activity, without holding an arbitrary angle.','Two population activity levels connected to separate basins'),
('MULTILEVEL','A multistable CMOS circuit can restore one of several preferred voltages; many levels are not automatically a continuum.','Several voltage wells and a state descending to the nearby level'),
('RING','A recurrent ring represents a direction in the position of an activity bump; actual circuit implementations can be finite and hybrid.','Ring of units with highlighted bump shifted by motion signal'),
('OSCILLATOR','A sustained oscillator normally advances in phase; a disturbance can leave a persistent phase offset relative to its expected cycle.','Reference and shifted cycles with phase difference'),
('SPIKES','Pulses are events, rate summarizes expected event frequency, and decaying synaptic activation accumulates pulse effects.','Pulse train and distinct decaying activation trace'),
('SPIKES','Programmable conductance can store a weight rather than the current neuron state or remembered angle.','Separate conductance, capacitor state and decoded bump label'),
('READOUT','Drift describes evolution of a represented state; Fisher information concerns distinguishability in observed signals and a neural bound does not automatically transfer to hardware.','Separate moving-position distribution and nearby-signal likelihood comparison')]),
16:('08-hardware-dynamics.md','ch:HARDWARE-DYNAMICS','part:HARDWARE',[
('FEEDBACK','Recurrent feedback can replace a fraction of a leaking state, extending its collective persistence time.','Leaky capacitor with a returning current path'),
('FEEDBACK','As gain approaches one from below the effective decay time increases; gain above one invalidates the simple linear stable model.','Three decay curves with increasing gain and separately marked unstable branch'),
('ERRORS','A small displacement inside a bit state’s basin returns, while a large enough disturbance can switch states.','Two wells with small return and separate cross-boundary disturbance'),
('ERRORS','In an ideal continuous attractor shape disturbances decay while displacements along the state family persist.','Perturbed bump relaxes in shape but retains its shifted position'),
('ERRORS','Repeated noise produces bounded local spread with restoration but growing variance along a neutral direction.','Side-by-side bounded and expanding trial distributions'),
('ERRORS','Pinning can reduce spread by drawing values to preferred states, at the cost of bias.','Preferred positions and biased endpoints versus initial cues'),
('ERRORS','The 2012 information bound is conditional on its neural model and cannot be assumed for every electronic memory.','Model assumptions adjoining bound, with no arrow to universal hardware claim'),
('EVIDENCE','The 32-position head-direction demonstration has finite spatial resolution, not a proven continuous family or Brownian law.','Finite labeled bump positions around a ring'),
('EVIDENCE','A separate recurrent spiking device exhibited bistable persistent activity and noise-related switching.','Two stable firing states and an indicated transition')]),
17:('09-neuromorphic-systems.md','ch:NEUROMORPHIC-SYSTEMS','part:HARDWARE',[
('ARCHITECTURES','Digital systems calculate states; analog circuits evolve physical variables, and hybrid systems combine these.','Digital update blocks, analog capacitor dynamics and mixed data flow'),
('ARCHITECTURES','Accelerated analog model time changes the relation between physical communication delays and simulated time.','Aligned wall-clock and accelerated model-clock traces'),
('ARCHITECTURES','On-chip learning updates weights on chip and differs from loading previously trained weights.','Weight update inside chip versus external weight loading'),
('ADVANCES','Loihi 2 input-history computation provides temporal features to a trained readout, not indefinite cue retention.','Input timeline creates a reservoir state feeding a trained readout'),
('ADVANCES','A SpiNNaker2 recurrent sheet maintained an activity center over a reported delay; host processing, jitter and lag limit its interpretation.','Host event processing to chip sheet with cue-off interval and output center'),
('ADVANCES','PCM weighted multiplication can support adaptation while other operations run on a host.','Separate PCM weight array and host computation'),
('ADVANCES','Reduced drift in a material concerns stability of programmed conductance, not an already complete processor.','Programmed resistance trajectories for material samples'),
('LIMITS','A slow input-history pathway holds decaying recent information and differs from a cue stored on a continuous attractor.','Fading input-history register beside a stationary bump'),
('LIMITS','Comparison of systems must include task, error, delay, communication, conversion, and host computation.','Shared comparison envelope showing chip, communication and host')]),
18:('10-hardware-tests.md','ch:HARDWARE-TESTS','part:HARDWARE',[
('PROTOCOL','Calibrate a decoder separately; present a cue, remove it, retain fixed weights and decode after multiple delays over repeated trials.','Repeated cue-off-delay-readout timelines and fixed decoder'),
('PROTOCOL','Separate initial writing error, mean displacement and trial-to-trial spread; test multiple cue angles.','Starting offsets and subsequent mean and spread plots'),
('PROTOCOL','A circular angle requires suitable unwrapping, and local variance cannot be extended indefinitely around the circle.','A trace crossing zero degrees beside circular endpoints'),
('PROTOCOL','Readout noise adds displacement variance and observation filtering changes temporal shape, so calibrate both.','Noisy readout and low-pass filter separated from state dynamics'),
('PARAMETERS','Leak and recurrent-weight changes alter decay or pinning; only projected neural disturbances shift a remembered value.','Leak, weight bias and projected-noise arrows on network state'),
('PARAMETERS','Noise correlation matters: shared fluctuations need not average away like independent fluctuations.','Aligned common noise versus independent fluctuations across cells'),
('COMPARISON','A valid information comparison matches observed signals, noise, dynamics, observation time and decoder.','Matched signal-and-time windows feeding two decoders'),
('COMPARISON','Output filtering and spatial field statistics do not by themselves prove internal memory stability.','Separate internal trajectory, filtered output and static spatial map')]),
19:('11-simulating-memory.md','ch:SIMULATING-MEMORY','part:SIMULATIONS',[
('STATE','At each step, activations set weighted input and rate, conditional random spikes are generated, and activation decays and renews.','State to weighted input to rate to random events to next state loop'),
('STATE','The time step must resolve decay and have a small event probability for the one-spike update.','Short step and low-probability event indicator'),
('RING','A ring orders neurons by preferred angle and encodes the value in an activity bump.','Ring and position-coded bump'),
('RING','The noise-free tuning curves predict diffusion; simulated trajectories independently supply angle displacement measurements.','Separate tuning-curve prediction and stochastic trials converge at comparison'),
('RING','The highest-rate neuron is a quantized numerical proxy, not the same as projection to the noise-free attractor.','Largest-rate index beside continuous projection marked distinct'),
('RING','Wrapped angle displacement reaches a finite range; flattening does not prove restored original memory.','Circle wrapping and bounded angular-error curve'),
('CONTROLS','A two-unit mutually inhibitory system tests conclusions without ring symmetry, with a change of coordinates affecting diffusion units.','Two units with reciprocal inhibitory links and rate/activation coordinate key'),
('OUTPUTS','Readout-error formula plots are analytical comparisons, not additional neural-network simulations; original simulator software was not identified.','Formula curve separated from event-driven simulation')]),
20:('12-simulating-eye-drift.md','ch:SIMULATING-EYE','part:SIMULATIONS',[
('DATA','Recordings come from 57 motor neurons in two macaques in separate single-cell recordings; held-out trials test rate predictions.','Sequential single-cell records with held-out trial'),
('DATA','Eye motion and a prediction from one neuron covary; the shared fraction estimate depends on calibration and noise assumptions.','Measured and predicted displacement traces sharing a latent drive'),
('PATH','Two integrator populations produce an internal position command through their activity difference.','Opposing populations to common internal command'),
('PATH','Motor neurons translate command into noisy spike trains and muscles filter their contributions into eye position.','Command to motor spikes to mechanical filter to eye angle'),
('PATH','Delayed eye position and current internal command contribute differently to feedback input.','Eye-output delay branch and current-command branch entering subtraction'),
('CONTROLS','Compare fixed-command private motor noise, noisy internal command, and full pathway rather than relying on one irregular trajectory.','Three separated control pipelines with common observation statistic'),
('CONTROLS','Apply the measured-data reconstruction to simulations and check measurement-noise and feedback controls.','Simulated motor spikes and eye output entering the same analysis'),
('TOOLS','Released MATLAB model code and raw recordings support different reproductions; a processed MSD alone is not raw data reanalysis.','Separate model code, raw recordings and processed summary inputs')]),
21:('13-simulating-place-fields.md','ch:SIMULATING-PLACE','part:SIMULATIONS',[
('GENERATE','A smooth Gaussian input field with specified spatial covariance is thresholded and scaled into firing-rate maps.','Random grid smoothed into continuous field then thresholded into active regions'),
('GENERATE','The released spatial generator uses random grid draws, smoothing, RMS normalization, thresholding and connected field detection.','Five sequential grid-state representations with normalized scale'),
('GENERATE','These are static spatial maps, not direct simulations of recurrent hippocampal spikes or synapses.','Position axis clearly separate from time trajectory'),
('FIT','Threshold and spatial scale are selected using condition-specific summaries; matching those summaries is a fit.','Data summaries entering parameter fitting loop'),
('FIT','Full distributions, slices, peaks and holes supply further comparisons, though some also fit a gain.','Fitted features separated from additional histogram and topology comparisons'),
('FIT','The lognormal model comparison uses the available data, not a reported held-out forecast; simulation realizations sample model variation.','Two model likelihood comparisons marked in-sample'),
('MEASURE','Connectivity, thresholds and smoothing can merge or split fields, changing counts, lengths and topology.','Same grid under two connectivity or cutoff rules'),
('MEASURE','The Gaussian filter width differs from the resulting correlation scale; boundary handling varies by implementation.','Filter kernel and broader covariance curve with different boundary treatments'),
('TOOLS','NumPy and SciPy generate and measure maps and Gudhi evaluates topology; code availability differs from data and run-setting availability.','Tools linked to operations; missing dataset depicted separately')]),
22:('14-simulation-tools.md','ch:SIMULATION-TOOLS','part:SIMULATIONS',[
('ROUTES','Authors’ code, independent implementation and simplified teaching model answer different reproduction questions.','Three separately labeled implementation paths to different claims'),
('ROUTES','A successful run alone does not establish agreement with published model, data and measurements.','Program output compared against source and target measurement'),
('SOFTWARE','Random generator, seed, software versions and call ordering determine reproducibility; the seed alone is insufficient.','Run record connected to random draws'),
('SOFTWARE','A deterministic ODE solver does not by itself implement Poisson spikes or Brownian increments.','Separate deterministic solver, event generator and stochastic increments'),
('SOFTWARE','Field connectivity rules and the choice of spiking simulator affect what model and measurement are implemented.','A grid with two connectivity choices and separate neuron model'),
('RESOLUTION','Refining simulation time step or spatial grid while preserving physical parameters tests convergence in reported results.','Coarse/fine time and space scales feeding matched comparison'),
('RESOLUTION','For Brownian increments variance scales with step duration, so the standard deviation scales with its square root.','Four short increments versus one long increment with matched total variance'),
('RESOLUTION','Saving output too sparsely can discard temporal information despite a small internal time step.','Fine internal trace sampled by a coarse output grid'),
('RECORD','Preserve source, target, model, inputs, numerical settings, measurement and uncertainty, with the true independent repeat as unit.','A compact record grouping parameters, measurement and independent repeats')])}
styles=base['style_contract']; example=base['visual_explanation']; mdref='C:/Users/vital/.codex/skills/course-diagram-builder/assets/visual-language-examples-v1/m1-retrieval-scenes.png'
for num,(name,ch,part,points) in C.items():
 path=root/'content/chapters'/name; raw=path.read_bytes(); lines=raw.decode('utf-8-sig').splitlines(); sections={}
 for i,line in enumerate(lines,1):
  m=re.match(r'^## .*\{#(sec:[^}]+)\}',line)
  if m: sections[m.group(1).split('-')[-1]]=(m.group(1),i)
 starts=sorted(x[1] for x in sections.values()); ids=[]; inventory=[]; scenes=[]
 for j,(short,point,scene) in enumerate(points,1):
  aid=f'P{j:02d}'; ids.append(aid)
  matches=[(k,v) for k,v in sections.items() if k==short]
  if not matches: raise Exception((name,short,sections))
  anchor,start=matches[0][1]; nexts=[n for n in starts if n>start]; end=min(nexts)-1 if nexts else len(lines)
  inventory.append({'id':aid,'point':point,'source_locus':f'{path.as_posix()}:{start}-{end} (#{anchor})'})
  scenes.append({'source_item_ids':[aid],'visible_objects_and_relation':scene,'teaching_contribution_beyond_labels':point})
 brief={'brief':{'asset_id':f'fig:MAP-CH{num:02d}','scope':'chapter','book':'burak-three-papers','part':part,'chapter':ch,'purpose':lines[0].split('{#')[0].lstrip('# ').strip(),'target_use':'chapter-opening','generation_authorized':True,'insertion_authorized':False,'status':'draft-requires-source-and-coverage-review','reading_width':'6.35 inches; verify actual book width'},
 'visual_explanation':{'applicable':True,'figure_role':'illustrated-opener','role_reason':'Physical objects, changing states, signals, and separate comparisons explain the chapter mechanisms beyond topic labels.','example_id':'m1-retrieval-scenes','example_image_path':mdref,'example_image_sha256':example['example_image_sha256'],'example_prompt_records_read':example['example_prompt_records_read'],'properties_to_reuse':example['properties_to_reuse'],'properties_not_to_transfer':example['properties_not_to_transfer'],'composition':'Arrange related scenes according to their true dependence; show independent comparisons separately. Do not draw a single implied causal chain across unrelated examples.','scenes':scenes,'actual_review':{'asset_sha256':None,'reviewer':None,'visible_evidence':[],'strongest_objection_and_resolution':None,'verdict':'pending'}},
 'chapter_map_coverage':{'applicable':True,'contract':'references/chapter-map-coverage.md','chapter_source_loci':[str(path).replace('\\','/')],'chapter_source_sha256':hashlib.sha256(raw).hexdigest(),'teaching_points':inventory,'planned_point_ids':ids,'actual_review':{'asset_sha256':None,'covered_points':[],'absent_point_ids':[],'inventory_count':len(ids),'covered_count':None,'covered_fraction':None,'verdict':'pending'}},
 'style_contract':styles,'language_contract':{'book_loci':[str(path).replace('\\','/')],'approved_terms':[x[1] for x in points],'caption':'The scene relates the physical states, measurements, and assumptions described in '+lines[0].split('{#')[0].lstrip('# ').strip()+'.','alt_text':'; '.join(x[2] for x in points)+'.','prohibited_viewer_commands':['read left to right','follow the arrow','teaching order']},
 'required_items':[{'id':f'S{j:02d}','teaching_point':p,'visual_role':v} for j,(_,p,v) in enumerate(points,1)],
 'communication_plan':{'segments':scenes,'layout':'Use subject-driven scenes with readable short labels; separate independent examples and preserve their conditions.','keep_in_text':['Detailed formulas and numerical calculations','Full discussion and citations'],'required_visible_conditions':['Distinguish measured demonstrations, numerical simulations, and proposed tests where applicable'],'independent_example_groups':['Independent study or architecture examples unless the source establishes an action between them']},
 'normal_flow':['Connect events only where source text gives an actual causal, computational or measurement relationship.'],
 'secondary_relationships':['Show comparisons side by side without a causal arrow; use explicitly labeled feedback only where it exists.'],
 'exact_text':{'required':[],'prohibited':['paper title banner','unsupported universal claims','visual-review notes or caption inside image']},
 'constraints':['Match the book palette and style lock.','Do not treat planned teaching points as established visual coverage.','Do not imply that different experiments are one continuous causal experiment.','Keep caption and alt text outside the artwork.','Do not shrink labels to hide excessive density.','If a point cannot be shown with its important condition, leave its coverage pending.'],
 'dispositions':[]}
 (out/f'ch{num:02d}.yaml').write_text(yaml.safe_dump(brief,sort_keys=False,allow_unicode=True,width=100),encoding='utf8')
 print(num,name,len(ids))
parts={
'part03':('part:HARDWARE','Neural memory in electronic hardware',[14,15,16,17,18],[(14,[1,2,4,5,6,9]),(15,[2,4,5,6,7,9]),(16,[1,3,4,5,6,8,9]),(17,[1,3,4,5,6,7,8,9]),(18,[1,2,3,4,5,6,7,8])],'Electronic storage, feedback architectures, noise and readout become comparable only when the encoded value, physical state and measured task are specified.'),
'part04':('part:SIMULATIONS','Simulations connect model assumptions to measurable outcomes',[19,20,21,22],[(19,[1,3,4,5,6,7,8]),(20,[1,2,3,4,5,6,7,8]),(21,[1,2,3,4,5,6,7,8,9]),(22,[1,2,3,4,5,6,7,8,9])],'Three distinct simulations compare neural memory, eye motion, and static spatial firing maps; careful implementation and measurement make each comparison testable.')}
for key,(part,title,nums,selected,purpose) in parts.items():
 selected={n: list(range(1, len(C[n][3])+1)) for n in nums}; scope=[]; inv=[]; scenes=[]; k=0
 for num in nums:
  child=yaml.safe_load((out/f'ch{num:02d}.yaml').read_text(encoding='utf8'))
  x=child['chapter_map_coverage']; scope.append({'chapter':child['brief']['chapter'],'source_path':x['chapter_source_loci'][0],'source_sha256':x['chapter_source_sha256']})
  for i in selected[num]:
   item=x['teaching_points'][i-1]; scene=child['visual_explanation']['scenes'][i-1]; k+=1
   pid=f'P{k:02d}'; inv.append({'id':pid,'point':item['point'],'source_locus':item['source_locus']}); scenes.append({'source_item_ids':[pid],'visible_objects_and_relation':scene['visible_objects_and_relation'],'teaching_contribution_beyond_labels':item['point']})
 sourcepath=root/'plan/chapter-plan.yaml'; scopemeta={'part_plan':str(sourcepath).replace('\\','/'),'part_plan_sha256':hashlib.sha256(sourcepath.read_bytes()).hexdigest(),'chapters':scope}
 p={'brief':{'asset_id':f'fig:MAP-{key.upper()}','scope':'part','book':'burak-three-papers','part':part,'chapter':None,'purpose':purpose,'target_use':'part-opening','generation_authorized':True,'insertion_authorized':False,'status':'draft-requires-source-and-coverage-review','reading_width':'6.35 inches; verify actual book width'},
 'visual_explanation':{'applicable':True,'figure_role':'illustrated-opener','role_reason':'Concrete circuit and simulation scenes make the connections and distinctions across chapters inspectable.','example_id':'m1-retrieval-scenes','example_image_path':mdref,'example_image_sha256':example['example_image_sha256'],'example_prompt_records_read':example['example_prompt_records_read'],'properties_to_reuse':example['properties_to_reuse'],'properties_not_to_transfer':example['properties_not_to_transfer'],'composition':'Conceptual overview of chapter relationships, not a single linear chain of unrelated systems or experiments. Avoid text-only cards.','scenes':scenes,'actual_review':{'asset_sha256':None,'reviewer':None,'visible_evidence':[],'verdict':'pending'}},
 'part_map_coverage':{'applicable':True,'source_scope':scopemeta,'teaching_points':inv,'planned_point_ids':[x['id'] for x in inv],'actual_review':{'asset_sha256':None,'covered_points':[],'absent_point_ids':[],'inventory_count':len(inv),'covered_count':None,'covered_fraction':None,'verdict':'pending'}},
 'style_contract':styles,'language_contract':{'book_loci':['plan/chapter-plan.yaml']+[x['source_path'] for x in scope],'caption':purpose,'alt_text':'Part overview: '+ '; '.join(s['visible_objects_and_relation'] for s in scenes)+'.'},
 'required_items':[{'id':s['source_item_ids'][0],'teaching_point':s['teaching_contribution_beyond_labels'],'visual_role':s['visible_objects_and_relation']} for s in scenes],
 'communication_plan':{'segments':scenes,'layout':'Use a small number of integrated explanatory scenes; do not use arrows between independent cases. The large inventory may require significant simplification and a coverage review before generation.','keep_in_text':['All derivations','Numerical details and references'], 'independent_example_groups':['Different hardware demonstrations or different paper simulations have no implied causal connection.']},
 'normal_flow':['Use only causal and computational relationships supported by each source chapter.'], 'secondary_relationships':['Show separate demonstrations and measurements as comparisons rather than one connected experiment.'],
 'exact_text':{'required':[],'prohibited':['part title banner','review notes or captions in the artwork','misleading causal arrows between separate studies']},
 'constraints':['Keep all figure claims and relationships source-grounded.','Do not equate physical memory, persistent activity and decoded value.','Do not claim a simulation proves a biological mechanism.','Preserve actual-width readability.','Coverage and independent review remain pending.'], 'dispositions':[]}
 (out/f'{key}.yaml').write_text(yaml.safe_dump(p,sort_keys=False,allow_unicode=True,width=100),encoding='utf8'); print(key,len(inv))

short_labels={14:['Connection weights','Changing activity','Remembered angle','Digital bits','Capacitor voltage','Conductance weight'],15:['Two stable states','Several stable levels','Activity bump','Oscillator phase','Pulse train','Decoding'],16:['Leak and feedback','Restoring state','Neutral direction','Random spreading','Preferred states'],17:['Digital update','Analog state','Input history','Persistent activity','Material conductance','Host computation'],18:['Cue and delay','Decoded angle','Mean error','Trial spread','Readout noise','Matched observation'],19:['Synaptic activation','Random spikes','Activity bump','Theory','Simulation','Wrapped angle'],20:['Recorded spikes','Internal command','Motor spikes','Eye response','Delayed feedback','Controls'],21:['Random input','Spatial smoothing','Threshold','Fitted summaries','Field measurements','Topology'],22:['Original code','Independent implementation','Random generator','Time step','Grid spacing','Saved run record']}
for num,labels in short_labels.items():
 p=out/f'ch{num:02d}.yaml'; b=yaml.safe_load(p.read_text(encoding='utf8')); b['exact_text']['required']=labels; b['language_contract']['approved_terms']=labels; p.write_text(yaml.safe_dump(b,sort_keys=False,allow_unicode=True,width=100),encoding='utf8')
for key,labels in {'part03':['Weights and states','Electronic feedback','Stability and noise','Hardware implementations','Memory measurement'],'part04':['Neural simulation','Eye simulation','Spatial maps','Measurement and tools']}.items():
 p=out/f'{key}.yaml'; b=yaml.safe_load(p.read_text(encoding='utf8')); b['exact_text']['required']=labels;p.write_text(yaml.safe_dump(b,sort_keys=False,allow_unicode=True,width=100),encoding='utf8')

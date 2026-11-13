from pathlib import Path
from collections import defaultdict
import json,re,yaml

root=Path(__file__).resolve().parents[2]; task=Path(__file__).resolve().parent; c=root/'content/chapters'
approved=[]
for name in ['memory','systems','tests']:
 d=json.loads((task/f'review-{name}-stage2.json').read_text(encoding='utf-8'))
 decisions=d.get('lint_decisions',d.get('vale',{}).get('error_decisions',[]))
 for x in decisions:
  if 'justified' not in x['decision'].lower(): continue
  if 'file' in x: file,line=x['file'],x['line']
  else:
   file,n=x['location'].rsplit(':',1); line=int(n)
   if '/' not in file:file='content/chapters/'+file
  approved.append(dict(file=file,line=line,rule=x.get('rule',x.get('check')),reason=x['reason'],review=f'review-{name}-stage2.json'))
group=defaultdict(lambda:defaultdict(set))
for a in approved:group[a['file']][a['line']].add(a['rule'])
if (task/'approved-lint-exceptions.json').exists():group.clear()
plan_path=root/'plan/chapter-plan.yaml'; plan=yaml.safe_load(plan_path.read_text(encoding='utf-8')); part=plan['book']['parts'][-1]
for file,by_line in group.items():
 p=root/file; lines=p.read_text(encoding='utf-8').splitlines(); output=[]
 for i,line in enumerate(lines,1):
  rules=sorted(by_line.get(i,[]))
  prefix=[f'<!-- vale {rule} = NO -->' for rule in rules]
  suffix=[f'<!-- vale {rule} = YES -->' for rule in reversed(rules)]
  output.extend(prefix+[line]+suffix)
  if file.endswith('/part-opening.md') and rules:
   node=next(n for n in part['content'] if n['text']==line)
   node['text']='\n'.join(prefix+[line]+suffix)
 if not file.endswith('/part-opening.md'):p.write_text('\n'.join(output)+'\n',encoding='utf-8')
plan_path.write_text(yaml.safe_dump(plan,sort_keys=False,allow_unicode=True,width=110),encoding='utf-8')
(task/'approved-lint-exceptions.json').write_text(json.dumps(approved,indent=2),encoding='utf-8')

def fix(name, pairs):
 p=c/name; s=p.read_text(encoding='utf-8')
 for old,new in pairs:
  if old not in s and new in s:continue
  assert old in s,(name,old)
  s=s.replace(old,new)
 p.write_text(s,encoding='utf-8')

fix('07-hardware-memory.md',[
 ('A [[**capacitor**]{.definition-term custom-style="Definition Term"} stores separated electric charge. Its capacitance $C$ relates charge and voltage by $Q=CV$.]{.definition-explanation} Supplying current changes $Q$, so it changes the stored voltage.',
  '[[**Current**]{.definition-term custom-style="Definition Term"} is electric charge flowing per unit time, measured in amperes (coulombs per second).]{.definition-explanation} [[**Voltage**]{.definition-term custom-style="Definition Term"} is an electrical energy difference per unit charge, measured in volts (joules per coulomb).]{.definition-explanation}\n\nA [[**capacitor**]{.definition-term custom-style="Definition Term"} stores separated electric charge. For fixed capacitance $C$, its stored charge $Q$ and voltage difference $V$ satisfy $Q=CV$.]{.definition-explanation} Charge is measured in coulombs and capacitance in farads (coulombs per volt). Supplying current changes $Q$, so it changes the stored voltage.'),
 ('and therefore changes voltage','and so changes voltage'),
 ("stores information in a material's physical phase configuration, which affects its electrical resistance.","stores information in a material's atomic arrangement, for example the proportions of ordered and disordered regions, which affect its electrical resistance."),
 ('Programming pulses change that configuration.','Programming pulses heat the material. Its heating and cooling history changes the arrangement.'),
 ('is the ratio of current to applied voltage in the linear read regime, and is the inverse of resistance.','measures the current produced per unit applied voltage where current is approximately proportional to voltage. It is the inverse of resistance, the voltage required per unit current.'),
 ('where $G$ is conductance.','where $I$ is current, $V$ is applied voltage, and $G$ is conductance, measured in siemens (amperes per volt).'),
 ('Preprint; the inspected version','Preprint. The inspected version'),
 ('; detailed implementation descriptions refer to that manuscript version.','. Detailed implementation descriptions refer to that manuscript version.'),
])
fix('08-hardware-dynamics.md',[
 ('The term $-u$ removes activity; $gu$ replaces','The term $-u$ removes activity, and $gu$ replaces'),
 ('; [author-posted manuscript]', '. [Author-posted manuscript]'),
 ('; the volume and DOI carry 2011.','. The volume and DOI carry 2011.'),
 ('feedback calibration','adjusting the feedback strength'),
])
fix('09-neuromorphic-systems.md',[
 ('experiments partly run on a host computer, and proposed hardware evaluated by simulation.', 'experiments partly run on a separate computer, and proposed hardware evaluated by simulation. A [[**host computer**]{.definition-term custom-style="Definition Term"} runs the parts of an experiment assigned to a separate general-purpose computer rather than the neuromorphic chip.]{.definition-explanation}'),
 ('Measure calibration, circuit variability, and the conversion between chip and model time','Check how adjusting circuit settings reduces device differences, measure the remaining variability, and relate chip time to model time'),
 ('Loihi 2 offers programmable learning rules; SpiNNaker2', 'Loihi 2 offers programmable learning rules. SpiNNaker2'),
 ('an on-chip learning implementation; BrainScaleS-2', 'an on-chip learning implementation. BrainScaleS-2'),
 ('programmable plasticity processors','programmable processors that update weights'),
 ('An experiment can still use offline training or a host computer. Platform support alone does not tell us how that experiment learned.', 'An experiment may still use weights trained beforehand or learning performed on a separate computer, so its learning setup must be checked.'),
 ('a memory buffer and nonlinear features for temporal tasks. A trained readout uses those features to produce an output.', 'a stored history of recent inputs and functions of those inputs that include products. A trained readout uses these values to predict an output.'),
 ('measured very low resistance drift','measured low resistance drift'),
 ('Their deterministic multilevel demonstration', 'Their demonstration of several programmed resistance levels'),
 ('Nanoscale multilevel operation, higher endurance, and large-array variability remained open.', 'Operation with several levels in nanoscale devices, performance after many programming cycles, and variability across large arrays remained open.'),
 ('[Better temporal state, faster adaptation, and more stable weights solve different problems. Progress in one does not establish the others.]{.key-statement}', '[Better temporal state, faster adaptation, and more stable weights solve different problems, so progress in one does not establish the others.]{.key-statement}'),
 ('holds successive slow states in registers and other variables in SRAM.', 'holds successive slow states in [[**registers**]{.definition-term custom-style="Definition Term"}, small, fast digital storage locations]{.definition-explanation}, and other variables in SRAM.'),
 ('The networks were trained offline.', 'The weights were trained before the evaluated tasks.'),
 ('; the reported prototype has four chips.','. The reported prototype has four chips.'),
])
fix('10-hardware-tests.md',[
 ('This chapter develops a controlled test that separates them, connects physical parameters to memory error, and states how the three neuroscience papers guide the interpretation.', 'The controlled tests below connect these errors to physical parameters.'),
 ('Unwrap trajectories only while that operation is reliable.', r'[[**Unwrapping**]{.definition-term custom-style="Definition Term"} tracks crossings of $0^\circ/360^\circ$ by adding or subtracting full turns to continue the trajectory.]{.definition-explanation} Use it only when sampling is frequent enough to identify crossings reliably.'),
 (', rather than treating fitted coefficients as exact device properties.', '.'),
 ('At long delays around a circle, use circular statistics rather than extending a local unwrapped variance indefinitely.', 'At long delays, report the distribution of angular errors around the circle. Values separated by a full turn represent the same angle, so a local unwrapped variance cannot be extended indefinitely as a measure of angular error.'),
 ('The following changes suggest distinct tests. They are conditional predictions, not universal chip specifications.', 'The following changes suggest tests under the model assumptions above.'),
 ('Quantization error, pinning, or stalled small updates', 'Error from mapping values to available numerical levels, pinning, or stalled small updates'),
])
fix('00-reading-guide.md',[
 ('; the three original papers remain the foundation of Parts I and II.','. The three original papers remain the foundation of Parts I and II.'),
])
fix('references.md',[
 ('Part III uses selected sections from the sources below to connect physical storage, changing neural state and recurrent memory. These selections do not claim whole-paper coverage.', 'The sources below support selected Part III explanations of physical storage, changing neural state and recurrent memory.'),
 ('; proposed hardware and post-layout simulations are identified where discussed.','. Proposed hardware and post-layout simulations are identified where discussed.'),
 ('; March 2026 issue.','. March 2026 issue.'),
])
# Add only short lookup entries; the explanations remain in the chapters.
p=c/'glossary.md';s=p.read_text(encoding='utf-8')
terms=[
 ('capacitor','A component that stores separated electric charge, with charge and voltage related by its capacitance.','ch-hardware-memory.html#sec-hardware-memory-storage'),
 ('conductance','Current per unit applied voltage where current is approximately proportional to voltage; the inverse of resistance.','ch-hardware-memory.html#sec-hardware-memory-storage'),
 ('current','Electric charge flowing per unit time.','ch-hardware-memory.html#sec-hardware-memory-storage'),
 ('host computer','A separate computer running parts of an experiment outside the neuromorphic chip.','ch-neuromorphic-systems.html#sec-neuromorphic-systems-architectures'),
 ('register','A small, fast digital storage location.','ch-neuromorphic-systems.html#sec-neuromorphic-systems-limits'),
 ('unwrapping','Tracking crossings of a full turn to continue an angular trajectory, when sampling resolves the crossings reliably.','ch-hardware-tests.html#sec-hardware-tests-protocol'),
 ('voltage','Electrical energy difference per unit charge.','ch-hardware-memory.html#sec-hardware-memory-storage'),
]
for term,definition,link in terms:s+='- [[**'+term+':**]{.definition-term custom-style="Definition Term"} '+definition+']{.definition-explanation} [Explanation](../chapters/'+link+').\n'
s=s.replace('Storage in a material phase configuration read through its resistance or conductance.','Storage in a material atomic arrangement read through its resistance or conductance.')
p.write_text(s,encoding='utf-8')

def clean_comments(text):return re.sub(r'<!--.*?-->\s*','',text,flags=re.S)
for name in ['07-hardware-memory','08-hardware-dynamics','09-neuromorphic-systems','10-hardware-tests']:
 md=clean_comments((c/(name+'.md')).read_text(encoding='utf-8')); p=c/(name+'.yaml'); d=yaml.safe_load(p.read_text(encoding='utf-8'));d['purpose']=md.split('\n\n')[1]
 for m in re.finditer(r'^## (.+?) \{#(sec:[^}]+)\}\n\n',md,re.M):
  section=next(s for s in d['section_list'] if s['id']==m[2]);section['title']=m[1];section['summary']=md[m.end():].split('\n\n')[0]
 p.write_text(yaml.safe_dump(d,sort_keys=False,allow_unicode=True,width=105),encoding='utf-8')
p=c/'00-reading-guide.yaml';d=yaml.safe_load(p.read_text(encoding='utf-8'));md=clean_comments((c/'00-reading-guide.md').read_text(encoding='utf-8'));next(s for s in d['section_list'] if s['id']=='sec:READING-HARDWARE')['summary']=md.split('{#sec:READING-HARDWARE}\n\n')[1].split('\n\n')[0];p.write_text(yaml.safe_dump(d,sort_keys=False,allow_unicode=True,width=105),encoding='utf-8')
print('Applied Stage 2 repairs and',len(approved),'individually reviewed lint exceptions.')

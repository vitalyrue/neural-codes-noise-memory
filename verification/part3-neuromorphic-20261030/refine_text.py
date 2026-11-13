from pathlib import Path
import re, yaml, json
root=Path(__file__).resolve().parents[2]
c=root/'content/chapters'
replacements={
'07-hardware-memory.md':[
 ('which physical quantity carries which information','what information each physical quantity represents'),
 ('Three different objects enter this experiment:', 'The experiment involves:'),
 ('can also carry recent information','can also store recent information'),
 ('a teaching example of the distinction','an example constructed to illustrate the distinction'),
 ('a particular chip','a chip'),
 ('Input current changes stored charge, hence voltage.','Input current changes stored charge and therefore changes voltage.'),
 ('Quantity carrying information','Quantity representing information'),
 ('route the events and hold the settings','route the events and store the settings'),
 ('Currents from several cells can sum, giving a physical weighted sum.','Currents from several cells add to produce a weighted sum.'),
 ('how a value survives between updates','how a value is retained between updates'),
 ('The next chapter asks why feedback can preserve a bit yet let a graded estimate wander.','We can now examine why feedback can preserve a bit yet let a graded estimate wander.'),
],
'08-hardware-dynamics.md':[
 ('A simple linear teaching model','A simple linear model'),
 ('Its value is therefore the initial amplitude','Its value is the initial amplitude'),
 ('All three use the same component decay time.','The component decay time is unchanged in these three cases.'),
 ('any particular chip','any chip'),
 ('can therefore mean','can mean'),
 ('whether the feedback survives unequal devices','whether feedback maintains the intended state despite unequal devices'),
 ('Two early experiments make different claims and should be read separately.','The following early experiments make different claims and should be read separately.'),
],
'09-neuromorphic-systems.md':[
 ('Neither choice establishes a biological result without a matched model and experiment.','Interpreting either choice as a biological result requires a matched model and experiment.'),
 ('A particular experiment can nevertheless use','An experiment can still use'),
 ('evolving chip state','changing chip state'),
 ('Earlier training taught the model how to adapt.','Earlier training adjusted the model for rapid adaptation to new tasks.'),
 ('An elementary teaching model','A simple model'),
 ('is meaningful only relative to','must be specified relative to'),
 ('continue evolving while messages travel','continue changing while messages are transmitted'),
 ('The comparison therefore needs','The comparison needs'),
 ('and particular demonstrations','and the reported demonstrations'),
],
'10-hardware-tests.md':[
 ('A single accuracy score','One accuracy score'),
 ('proposed teaching tools','proposed tools for reasoning about these experiments'),
 ('Its access matters: a decoder given','A decoder given'),
 ('survives as a change','remains as a change'),
 ('is therefore $d\\theta','is $d\\theta'),
 ('with its pattern held fixed','with its pattern unchanged'),
 ('Matching time and readout makes the neuroscience comparison meaningful','Matching time and readout is necessary to compare memory accuracy'),
 ('The three source papers supply','The source papers supply'),
 ('a hardware network stores position without input','a network implemented in hardware retains position without input'),
 ('Thus $D_p=aD_m$','The result is $D_p=aD_m$'),
],
'00-reading-guide.md':[
 ('Its setting is neuromorphic computing: engineered systems inspired by neural organization and dynamics.','The setting is neuromorphic computing, where engineered systems implement computations inspired by neural organization and dynamics.'),
],
}
changes=[]
for filename,pairs in replacements.items():
 p=c/filename; s=p.read_text(encoding='utf-8')
 for old,new in pairs:
  if old not in s and new in s: continue
  assert old in s,(filename,old)
  s=s.replace(old,new); changes.append(dict(file=filename,old=old,new=new))
 p.write_text(s,encoding='utf-8')

# Short physical definitions supply the electronics assumptions before use.
p=c/'07-hardware-memory.md'; s=p.read_text(encoding='utf-8')
s=s.replace('Those choices expose the computation to different errors.', 'Those choices expose the computation to different errors. A [[**capacitor**]{.definition-term custom-style="Definition Term"} stores separated electric charge; its capacitance $C$ relates charge and voltage by $Q=CV$.]{.definition-explanation} Supplying current changes $Q$, so it changes the stored voltage.')
s=s.replace('Reading the conductance can recover a stored weight.', '[[**Conductance**]{.definition-term custom-style="Definition Term"} is the ratio of current to applied voltage in the linear read regime, and is the inverse of resistance.]{.definition-explanation} Reading the conductance can recover a stored weight.')
p.write_text(s,encoding='utf-8')

# Use direct sentences in new prose. Preserve semicolons within source citations/tables.
for name in ['07-hardware-memory.md','08-hardware-dynamics.md','09-neuromorphic-systems.md','10-hardware-tests.md']:
 p=c/name; lines=p.read_text(encoding='utf-8').splitlines()
 for i,line in enumerate(lines):
  if not line.startswith(('[^','|')):
   lines[i]=re.sub(r'; ([a-z])',lambda m:'. '+m[1].upper(),line)
 p.write_text('\n'.join(lines)+'\n',encoding='utf-8')

# Dates retain their values, with one consistent prose format.
dates={'30 October 2026':'October 30, 2026','27 July 2026':'July 27, 2026','2 February 2012':'February 2, 2012','1 October 2025':'October 1, 2025','3 December 2025':'December 3, 2025'}
for name in ['07-hardware-memory.md','08-hardware-dynamics.md','09-neuromorphic-systems.md','references.md','00-reading-guide.md']:
 p=c/name; s=p.read_text(encoding='utf-8')
 for a,b in dates.items():s=s.replace(a,b)
 p.write_text(s,encoding='utf-8')
plan_path=root/'plan/chapter-plan.yaml'; plan=yaml.safe_load(plan_path.read_text(encoding='utf-8')); part=plan['book']['parts'][-1]
for node in part['content']:
 if node['text'].startswith('>'):continue
 node['text']=re.sub(r'; ([a-z])',lambda m:'. '+m[1].upper(),node['text'])
 for a,b in dates.items():node['text']=node['text'].replace(a,b)
plan_path.write_text(yaml.safe_dump(plan,sort_keys=False,allow_unicode=True,width=110),encoding='utf-8')

# Synchronize only the derived title/purpose/section descriptions of the new chapters.
for name in ['07-hardware-memory','08-hardware-dynamics','09-neuromorphic-systems','10-hardware-tests']:
 md=(c/(name+'.md')).read_text(encoding='utf-8'); p=c/(name+'.yaml'); data=yaml.safe_load(p.read_text(encoding='utf-8'))
 data['purpose']=md.split('\n\n')[1]
 for m in re.finditer(r'^## (.+?) \{#(sec:[^}]+)\}\n\n',md,re.M):
  section=next(s for s in data['section_list'] if s['id']==m[2]); section['title']=m[1]; section['summary']=md[m.end():].split('\n\n')[0]
 p.write_text(yaml.safe_dump(data,sort_keys=False,allow_unicode=True,width=105),encoding='utf-8')
p=c/'00-reading-guide.yaml'; data=yaml.safe_load(p.read_text(encoding='utf-8')); s=next(s for s in data['section_list'] if s['id']=='sec:READING-HARDWARE'); md=(c/'00-reading-guide.md').read_text(encoding='utf-8'); s['summary']=md.split('{#sec:READING-HARDWARE}\n\n')[1].split('\n\n')[0]; p.write_text(yaml.safe_dump(data,sort_keys=False,allow_unicode=True,width=105),encoding='utf-8')
(Path(__file__).parent/'wording-repairs.json').write_text(json.dumps(changes,indent=2),encoding='utf-8')
print('Applied contextual wording repairs and two physical definitions.')

from pathlib import Path
import csv, re, yaml

ROOT=Path(__file__).resolve().parents[2]
chapter1=ROOT/'content/chapters/01-foundations.md'
chapter2=ROOT/'content/chapters/01b-persistence.md'
a=chapter1.read_text(encoding='utf-8'); b=chapter2.read_text(encoding='utf-8')
assert 'sec:FOUNDATIONS-EYE-ACTION' not in a, 'Move already applied'
start=b.index('**Anatomy: muscles turn the eyeball.**')
end=b.index('::: {.publisher-clarification-note',start)
anatomy=b[start:end]
spike_start=a.index('<!-- vale ai-tells.StrawmanContrast = NO -->')
spike_end=a.index('<!-- vale ai-tells.StrawmanContrast = YES -->',spike_start)+len('<!-- vale ai-tells.StrawmanContrast = YES -->')
spikes=a[spike_start:spike_end]
a=a[:spike_start]+a[spike_end:].lstrip('\n')
new_section='''## Repeated spikes maintain eye muscle tension {#sec:FOUNDATIONS-EYE-ACTION}

For the eye to stay directed at a target, its muscles must keep exerting force after the movement command ends.

'''+spikes+'\n\n'+anatomy+'The next question is how activity across a group of neurons represents the angle to be held.\n\n'
a=a.replace('## Patterns of firing rates represent a value {#sec:FOUNDATIONS-SPIKES}',new_section+'## Patterns of firing rates represent a value {#sec:FOUNDATIONS-SPIKES}',1)
old='Before asking how a circuit keeps a value, we need to know how its activity represents that value and what makes the activity variable. We begin with the spikes that cells send and the patterns of firing rates across a population. A model of spike counts then shows why one brief observation can be uncertain and how combining counts from several cells can help. We then learn how to tell whether measurements vary together and how to separate random spreading from a change in the average value. Those distinctions will let us interpret both a memory model and measurements of eye motion.'
new='Before asking how a circuit keeps a value, we need to know what its signals do. We begin with brief neural spikes and the eye muscles they activate, explaining how repeated activation can maintain an eye angle. We then ask how firing rates across a group of neurons represent that angle or an animal\'s location. A model of spike counts shows why one brief observation can be uncertain and how combining counts from several cells can help. Finally, we separate shared variation, random spreading and a change in the average value. These distinctions prepare us to interpret both a memory model and measurements of eye motion.'
assert old in a;a=a.replace(old,new,1)
for label in ['p-eye-anatomy','p-eye-mechanics','p-eye-plasticity']:
    note=re.search(r'^\[\^'+label+r'\]:.*$',b,re.M).group(0)
    a=a.rstrip()+'\n\n'+note+'\n'
b=b[:start]+'The [eye anatomy and motor pathway](ch-foundations.html#sec-foundations-eye-action) explain why holding an angle needs continuing muscle force. We now separate two questions: how that force balances the eye\'s elastic pull, and how the brain maintains the command that produces it. The folded calculation answers the mechanical question; the experiments below test the neural one.\n\n'+b[end:]
old='We first follow the physical path from motor neurons to muscles and eye rotation, separating mechanical smoothing from the neural command that holds a gaze angle. A small circuit example then shows why some disturbances fade while others leave a different stored angle. Repeating those lasting changes gives the diffusion calculation.'
new='Chapter 1 established how spikes act on eye muscles and how firing rates can represent an angle. We now examine the mechanical balance and continuing neural command needed to hold that angle. A small circuit example then shows why some disturbances fade while others leave a different stored angle. Repeating those lasting changes gives the diffusion calculation.'
assert old in b;b=b.replace(old,new,1)
chapter1.write_text(a,encoding='utf-8');chapter2.write_text(b,encoding='utf-8')

p=ROOT/'content/chapters/01-foundations.yaml';text=p.read_text(encoding='utf-8')
text=text.replace('This chapter explains how firing rates across a group of cells can represent an eye angle or an animal’s location, and how variable spike timing affects that representation.','This chapter first follows those spikes to eye muscles and explains how repeated activation holds an angle. It then shows how firing rates across a group of cells can represent an eye angle or an animal’s location, and how variable spike timing affects that representation.')
old_entry='''- id: sec:FOUNDATIONS-SPIKES
  title: Patterns of firing rates represent a value
'''
new_entry='''- id: sec:FOUNDATIONS-EYE-ACTION
  title: Repeated spikes maintain eye muscle tension
  summary: Brief spikes activate the eye muscles. Repeated firing maintains tension, while elasticity, viscosity and inertia have different mechanical roles. This physical pathway precedes the eye-angle coding example.
  level: 2
- id: sec:FOUNDATIONS-SPIKES
  title: Patterns of firing rates represent a value
'''
assert old_entry in text;text=text.replace(old_entry,new_entry,1)
data=yaml.safe_load(text)
for s in data['section_list']:
 if s['id']=='sec:FOUNDATIONS-SPIKES':s['summary']='Synaptic and recurrent interactions connect the cells. Tuning curves relate their expected firing rates to an eye angle or location, and a population code represents the value across neurons.'
p.write_text(yaml.safe_dump(data,allow_unicode=True,sort_keys=False,width=100),encoding='utf-8')
p=ROOT/'content/chapters/01b-persistence.yaml';data=yaml.safe_load(p.read_text(encoding='utf-8'))
data['purpose']='Building on the eye anatomy and firing-rate code in Chapter 1, this chapter examines mechanical balance and sustained neural drive. It then separates changes in neuronal activity from changes in the value represented, showing how persistent activity can still accumulate memory error.'
data['section_list'][0]['summary']='A folded torque calculation separates the force needed to hold an angle from factors that slow its return. Neural integration maintains the command, and plasticity can adjust the circuit\'s calibration.'
p.write_text(yaml.safe_dump(data,allow_unicode=True,sort_keys=False,width=100),encoding='utf-8')
p=ROOT/'content/chapters/04-eye-drift.md';text=p.read_text(encoding='utf-8').replace('[eye anatomy and mechanics](ch-persistence.html#sec-persistence-eye-mechanics)','[eye anatomy and motor action](ch-foundations.html#sec-foundations-eye-action)',1);p.write_text(text,encoding='utf-8')

# These five sources are now first encountered in a different order.
p=ROOT/'content/chapters/references.md';text=p.read_text(encoding='utf-8')
entries={int(m[1]):m[2] for m in re.finditer(r'^(7|8|9|10|11)\. (.+)$',text,re.M)}
start=text.index('7. Massachusetts');end=text.index('   <!-- vale ai-tells.EmDashUsage = NO -->\n12. Seung',start)
text=text[:start]+''.join(f'{i}. {entries[j]}\n\n' for i,j in zip(range(7,12),[8,9,10,7,11]))+text[end:]
p.write_text(text,encoding='utf-8')
for filename in ['source-coverage.csv','research-ledger.csv']:
 p=ROOT/'source-maps'/filename
 with p.open(encoding='utf-8',newline='') as f:r=csv.DictReader(f);fields=r.fieldnames;rows=list(r)
 for row in rows:
  sid=row.get('source_unit_id',row.get('claim_id',''))
  if sid in ['BG-EYE-ANATOMY','BG-EYE-MECHANICS','BG-EYE-PLASTICITY']:
   row['guide_locus' if 'guide_locus' in row else 'guide_location']='sec:FOUNDATIONS-EYE-ACTION; sec:PERSISTENCE-EYE-MECHANICS'
 with p.open('w',encoding='utf-8',newline='') as f:w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows(rows)
print('Moved reviewed anatomy and motor-action text before eye-angle tuning; stability calculation remains in Chapter 2.')

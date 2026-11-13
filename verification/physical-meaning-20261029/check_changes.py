from pathlib import Path
import re,json,hashlib,difflib,datetime,math
root=Path(__file__).resolve().parents[2]; out=Path(__file__).resolve().parent
files={'01-foundations.md':out/'01-foundations.before.md'}
files.update({p.name[:-7]:p for p in out.glob('*.md.before')})
report={'checked_at':datetime.datetime.now().astimezone().isoformat(),'chapters':{},'checks':{}}
def displays(s):return [re.sub(r'\s+','',m) for m in re.findall(r'\$\$(.*?)\$\$',s,re.S)]
for name,before in files.items():
    old=before.read_text(encoding='utf-8'); now=(root/'content/chapters'/name).read_text(encoding='utf-8')
    missing=[x for x in displays(old) if x not in displays(now)]
    controls=[ord(c) for c in now if ord(c)<32 and c not in '\n\r\t']
    old_blocks=re.findall(r'\{\{block:[^}]+\}\}',old)
    new_blocks=re.findall(r'\{\{block:[^}]+\}\}',now)
    old_anchors=re.findall(r'\{#([^}]+)\}',old)
    new_anchors=re.findall(r'\{#([^}]+)\}',now)
    bad_fences=[l for l in now.splitlines() if l.startswith(':::') and l!=':::' and not l.startswith('::: {')]
    report['chapters'][name]={'sha256':hashlib.sha256(now.encode()).hexdigest(),'displayed_equations_before':len(displays(old)),'displayed_equations_after':len(displays(now)),'missing_equations':missing,'control_characters':controls,'figure_blocks_preserved':old_blocks==new_blocks,'anchors_preserved':set(old_anchors)<=set(new_anchors),'malformed_fences':bad_fences,'new_formal_folds':now.count('publisher-clarification-note')-old.count('publisher-clarification-note')}
    (out/(name+'.diff')).write_text(''.join(difflib.unified_diff(old.splitlines(True),now.splitlines(True),fromfile='before/'+name,tofile='after/'+name)),encoding='utf-8')
    assert not missing and not controls and not bad_fences and old_blocks==new_blocks and set(old_anchors)<=set(new_anchors),name
report['checks']['new_parameter_arithmetic']={'twice_velocity_squared_ratio':2**2,'twice_D_sd_ratio':math.sqrt(2),'double_tau_fixed_rate_variance_ratio':0.25,'double_tau_fixed_activation_variance_ratio':0.5,'fixed_firing_double_k_position_ratio':0.5}
report['status']='passed'
(out/'source-checks.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
print(json.dumps({'status':'passed','chapters':len(files),'new_formal_folds':sum(x['new_formal_folds'] for x in report['chapters'].values()),'figures':'all existing block placements preserved','equations':'all existing displayed equations retained'},indent=2))

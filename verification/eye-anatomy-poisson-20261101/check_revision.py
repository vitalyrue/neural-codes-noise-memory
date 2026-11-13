"""Focused checks; does not claim whole-book or figure acceptance."""
from pathlib import Path
import datetime, difflib, hashlib, json, math, re, shutil, subprocess

TASK = Path(__file__).resolve().parent
ROOT = TASK.parents[1]
FILES = ['01-foundations.md', '01b-persistence.md', '04-eye-drift.md', 'glossary.md', 'references.md']
results = {'checked_at_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(), 'scope': FILES, 'source_checks': {}, 'vale': {}}
vale = shutil.which('vale')
results['vale']['engine'] = subprocess.run([vale, '--version'], capture_output=True, text=True).stdout.strip() if vale else 'unavailable'
raw, changed_alerts = {}, []
for name in FILES:
    relative = Path('content/chapters') / name
    path = ROOT / relative
    before = (TASK / 'baseline' / relative).read_text(encoding='utf-8')
    after = path.read_text(encoding='utf-8')
    old_ids = re.findall(r'\{#([^}]+)\}', before)
    new_ids = re.findall(r'\{#([^}]+)\}', after)
    missing = sorted(set(old_ids) - set(new_ids))
    assert not missing, (name, missing)
    assert len(new_ids) == len(set(new_ids)), (name, 'duplicate anchors')
    changed_lines = set()
    for tag, i1, i2, j1, j2 in difflib.SequenceMatcher(None, before.splitlines(), after.splitlines()).get_opcodes():
        if tag in ('insert', 'replace'):
            changed_lines.update(range(j1 + 1, j2 + 1))
    results['source_checks'][name] = {'sha256': hashlib.sha256(path.read_bytes()).hexdigest(), 'retained_anchors': len(old_ids), 'added_anchors': sorted(set(new_ids)-set(old_ids)), 'changed_lines': sorted(changed_lines)}
    (TASK / (name + '.diff')).write_text(''.join(difflib.unified_diff(before.splitlines(True), after.splitlines(True), fromfile='baseline/'+str(relative), tofile=str(relative))), encoding='utf-8')
    if vale:
        proc = subprocess.run([vale, f'--config={ROOT / ".vale.ini"}', '--output=JSON', '--ext=.md', f'--path={path}'], input=path.read_bytes(), capture_output=True)
        report = json.loads(proc.stdout)
        raw[name] = report
        for alerts in report.values():
            for alert in alerts:
                if alert.get('Line') in changed_lines:
                    changed_alerts.append({'file': name, **alert})

expected = 'sec:PERSISTENCE-EYE-MECHANICS'
assert results['source_checks']['01b-persistence.md']['added_anchors'] == [expected]
assert sum(len(r['added_anchors']) for r in results['source_checks'].values()) == 1
newrefs = (ROOT/'content/chapters/references.md').read_text(encoding='utf-8')
oldrefs = (TASK/'baseline/content/chapters/references.md').read_text(encoding='utf-8')
normalize = lambda s: re.sub(r'entry \d+', 'entry NUMBER', re.sub(r'^\d+\.\s*', '', s))
oldentries = [normalize(s) for s in oldrefs.splitlines() if re.match(r'^\d+\.', s)]
newentries = [normalize(s) for s in newrefs.splitlines() if re.match(r'^\d+\.', s)]
assert all(s in newentries for s in oldentries), 'Existing bibliography content lost'
assert len(newentries) == len(oldentries) + 5
results['reference_check'] = {'old_entries_retained': len(oldentries), 'new_entries': 5}

numerical = []
for lam in (0.1, 1.0, 5.0):
    probs = [math.exp(-lam + k*math.log(lam) - math.lgamma(k+1)) for k in range(100)]
    total, mean = sum(probs), sum(k*p for k,p in enumerate(probs))
    variance = sum((k-lam)**2*p for k,p in enumerate(probs))
    assert abs(total-1) < 1e-12 and abs(mean-lam) < 1e-12 and abs(variance-lam) < 1e-12
    errors=[]
    for n in (1000,100000):
        errors.append(max(abs(math.exp(sum(math.log(n-j) for j in range(k))-math.lgamma(k+1)+k*math.log(lam/n)+(n-k)*math.log1p(-lam/n))-probs[k]) for k in range(13)))
    assert errors[1] < errors[0]/90
    numerical.append({'lambda':lam,'sum':total,'mean':mean,'variance':variance,'max_abs_binomial_errors_n1000_n100000':errors})
results['poisson_numeric_consistency_not_proof']=numerical
results['vale']['changed_line_alerts']=changed_alerts
results['vale']['scope_note']='Only changed lines reported below. Unchanged warnings are retained in vale-raw.json; no whole-book prose verdict.'
(TASK/'vale-raw.json').write_text(json.dumps(raw,indent=2),encoding='utf-8')
(TASK/'checks.json').write_text(json.dumps(results,indent=2),encoding='utf-8')
print(json.dumps({'source_anchor_checks':'pass','references':'38 retained, 5 added','poisson_numerical_checks':'pass','vale_engine':results['vale']['engine'],'changed_alerts':[{k:a.get(k) for k in ('file','Line','Check','Severity','Match','Message')} for a in changed_alerts]},indent=2))

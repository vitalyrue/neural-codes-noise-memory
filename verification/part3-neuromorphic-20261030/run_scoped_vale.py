from pathlib import Path
import json, hashlib, subprocess
from datetime import datetime, timezone
import yaml

root = Path(__file__).resolve().parents[2]
out = Path(__file__).resolve().parent
vale = Path('C:/Users/vital/AppData/Local/Microsoft/WinGet/Packages/errata-ai.Vale_Microsoft.Winget.Source_8wekyb3d8bbwe/vale.exe')
files = [root/'content/chapters'/f for f in [
 '07-hardware-memory.md','08-hardware-dynamics.md','09-neuromorphic-systems.md','10-hardware-tests.md',
 '00-reading-guide.md','glossary.md','references.md']]
plan = yaml.safe_load((root/'plan/chapter-plan.yaml').read_text(encoding='utf-8'))
part = next(p for p in plan['book']['parts'] if p['part_id']=='part:HARDWARE')
opening = out/'part-opening.md'
opening.write_text('# '+part['title']+'\n\n'+'\n\n'.join(p['text'] for p in part['content'])+'\n',encoding='utf-8')
files.append(opening)
report = {'started_at': datetime.now(timezone.utc).isoformat(), 'engine': subprocess.check_output([str(vale),'--version'],text=True).strip(),
          'binary':str(vale),'footnote_mode':'native Markdown stdin with --ext=.md and --path', 'files':{}, 'alerts':{}}
for path in files:
    p = subprocess.run([str(vale),'--config='+str(root/'.vale.ini'),'--output=JSON','--ext=.md','--path='+str(path)],
        input=path.read_bytes(), capture_output=True, cwd=root)
    if p.returncode not in (0,1):
        raise RuntimeError(p.stderr.decode('utf-8',errors='replace'))
    report['files'][path.relative_to(root).as_posix()] = hashlib.sha256(path.read_bytes()).hexdigest()
    alerts=json.loads(p.stdout)
    report['alerts'][path.relative_to(root).as_posix()] = [a for values in alerts.values() for a in values]
counts={s:sum(a['Severity']==s for entries in report['alerts'].values() for a in entries) for s in ('error','warning','suggestion')}
report.update(completed_at=datetime.now(timezone.utc).isoformat(),counts=counts)
(out/'vale-native-current.json').write_text(json.dumps(report,indent=2,ensure_ascii=False),encoding='utf-8')
print(json.dumps(counts))
for path, alerts in report['alerts'].items():
    for a in alerts:
        if a['Severity']=='error':
            print(f"{path}:{a['Line']} {a['Check']} {a['Match']} :: {a['Message']}")

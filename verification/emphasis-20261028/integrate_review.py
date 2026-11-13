from pathlib import Path
import json,datetime,shutil
o=Path(__file__).resolve().parent
review=json.loads((o/'review-memory-reading.json').read_text(encoding='utf-8'))
decisions=[]
for change in review['changes']:
    if change['file']=='00-reading-guide.md':
        decisions.append(dict(file=change['file'],decision='Retain',reason='The user explicitly selected this exact phrase as the example to highlight. This takes priority over reducing repetition.'))
        continue
    path=o/change['source']; backup=o/('original-'+change['source'])
    if not backup.exists():shutil.copy2(path,backup)
    data=json.loads(path.read_text(encoding='utf-8'))
    file=next(f for f in data['files'] if f['file']==change['file'])
    matches=[i for i,x in enumerate(file['selections']) if x['text']==change['originalText']]
    assert len(matches)==1
    i=matches[0];file['selections'][i:i+1]=change['replacements']
    path.write_text(json.dumps(data,ensure_ascii=False,indent=2),encoding='utf-8')
    decisions.append(dict(file=change['file'],decision='Accept',reason=change['reason']))
(o/'integration.json').write_text(json.dumps(dict(at=datetime.datetime.now().astimezone().isoformat(),decisions=decisions),indent=2),encoding='utf-8')

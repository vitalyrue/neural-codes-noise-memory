from pathlib import Path
import fitz,json,datetime,shutil
O=Path(__file__).resolve().parent;R=O.parents[1]
(O/'baseline').mkdir(exist_ok=True);(O/'memory-pages').mkdir(exist_ok=True)
for p in (R/'content/chapters').glob('*'):
 if p.is_file():shutil.copy2(p,O/'baseline'/p.name)
shutil.copy2(R/'source-maps/visual-ledger.yaml',O/'baseline/visual-ledger.yaml')
shutil.copy2(R/'assets/styles/reading.css',O/'baseline/reading.css')
state=dict(startedAt='2026-10-28T19:26:25.0959253+02:00',checkpointAt=datetime.datetime.now().astimezone().isoformat(),status='Preparing folds and original paper excerpts',scope='Nine examples foldable; direct excerpts of paper figures discussed in the guide',awakeExecution='unverified')
(O/'STATE.json').write_text(json.dumps(state,indent=2),encoding='utf-8')
for name,pages in [('burak-fiete-2012-persistent-activity.pdf',[2,3,4]),('burak-fiete-2012-persistent-activity-si.pdf',[10,16])]:
 d=fitz.open(R/'assets/papers'/name)
 for n in pages:
  p=d[n-1];stem=('memory-si-' if '-si.' in name else 'memory-main-')+str(n)
  p.get_pixmap(matrix=fitz.Matrix(1.3,1.3),alpha=False).save(O/'memory-pages'/f'{stem}.png')
  print(stem,tuple(p.rect))
  for b in p.get_text('blocks'):
   if 'Fig.' in b[4] or 'FIG.' in b[4] or 'Figure' in b[4]:print(tuple(round(v,1) for v in b[:4]),b[4][:450])

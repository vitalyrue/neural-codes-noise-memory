from pathlib import Path
import fitz
root=Path(r'C:\dev\clsc\burak-papers')
out=root/'guide/verification/writers'
for fname,pages,prefix in [('burak-fiete-2012-persistent-activity.pdf',[1,2,3],'memory-main'),('burak-fiete-2012-persistent-activity-si.pdf',[8,13,15,16,18],'memory-si')]:
 doc=fitz.open(root/'papers'/fname)
 for p in pages:
  doc[p].get_pixmap(matrix=fitz.Matrix(1.4,1.4)).save(out/f'{prefix}-p{p+1:02d}.png')

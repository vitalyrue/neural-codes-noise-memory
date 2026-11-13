from pathlib import Path
from playwright.sync_api import sync_playwright
from PIL import Image
import fitz
p=Path('C:/dev/clsc/burak-papers/guide'); out=p/'verification/teaching-alignment-20261029'
with sync_playwright() as pw:
 browser=pw.chromium.launch(channel='msedge',headless=True)
 page=browser.new_page(viewport={'width':900,'height':800})
 page.goto((p/'assets/approved/visuals/attractor-directions.svg').as_uri())
 page.locator('svg').screenshot(path=str(out/'attractor-browser.png'))
 browser.close()
for source,width,name in [('assets/approved/visuals/synthesis-shared-position.png',700,'synthesis-700.png'),('assets/approved/visuals/paper-excerpts/place-fig-1.png',624,'paper-place-1-624.png')]:
 im=Image.open(p/source); im.resize((width,round(im.height*width/im.width)),Image.Resampling.LANCZOS).save(out/name)
doc=fitz.open(p/'assets/papers/mainali-2025-universal-statistics.pdf'); text=doc[3].get_text(); (out/'paper-place-1-page4.txt').write_text(text,encoding='utf-8'); print(text[-6500:])

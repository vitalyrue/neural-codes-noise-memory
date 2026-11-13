"""Record the lead's actual inspection of three existing browser screenshots."""
from pathlib import Path
from datetime import datetime
import hashlib, json
OUT = Path(__file__).resolve().parent
notes = {
 'context-foundations-A01-878.png': 'The preceding explanation, introduction, two probability panels and caption appear together. Mathematical caption text renders. The fixed 700 px image extends inside its local scroller, preserving readable labels; there is no page-wide overflow.',
 'context-place-A07-878.png': 'The covariance introduction appears after the scale definition. Fixed input and thresholded firing panels align in position, and the F(x) caption formula renders correctly. Local image scrolling retains the complete plot beyond this viewport slice.',
 'context-eye-A05-390.png': 'At narrow width the introduction and caption wrap naturally. Shared variance pieces, predictor noise, axes and legend are legible in the left portion of the scrollable figure. Its right panel is reached by horizontal image scrolling; no proportional shrinking is assumed.'}
records = []
for name, observation in notes.items():
    path = OUT / name
    records.append({'path': name, 'sha256': hashlib.sha256(path.read_bytes()).hexdigest(), 'observation': observation, 'status': 'pass'})
report = {'at': datetime.now().astimezone().isoformat(), 'reviewer': '/root', 'status': 'pass', 'screenshots': records,
 'scope': 'Three actual browser context screenshots. Every new full image and 700 px image was independently inspected in Stage1. This is not a whole-book visual sweep.'}
(OUT / 'browser-pixel-review.json').write_text(json.dumps(report, indent=2), encoding='utf-8')
print(json.dumps({'at': report['at'], 'screenshots_inspected': len(records), 'status': report['status']}))

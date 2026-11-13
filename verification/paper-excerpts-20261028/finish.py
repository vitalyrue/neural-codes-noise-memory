from pathlib import Path
import json,datetime
O=Path(__file__).resolve().parent;R=O.parents[1]
now=datetime.datetime.now().astimezone();state=json.loads((O/'STATE.json').read_text())
start=datetime.datetime.fromisoformat(state['startedAt']);elapsed=(now-start).total_seconds()
state.update(checkpointAt=now.isoformat(),status='Complete',wallElapsedSeconds=round(elapsed,1),tokenStats='unavailable',examples=9,originalFigureExcerpts=30,remainingWork='none',browserScope='Four sampled pages; actual example open/close, figure anchor opening, full-size navigation and narrow-screen figure panning. No whole-book pixel review.')
(O/'STATE.json').write_text(json.dumps(state,indent=2),encoding='utf-8')
resolution=dict(at=now.isoformat(),memoryFigure2Review='Resolved by checking the original Figure2 caption on PDF page3. It explicitly identifies both solid firing-rate traces and vertical lines for spikes emitted during 10 ms. The original alt text was retained; the reviewer suggestion to remove spikes was declined on this evidence.',placeFigure1Placement='Moved proposed insertion from the chapter overview to the paragraph defining the normalized input model in section PLACE-GP, so it follows the actual model explanation and has a valid section placement.',sourceCropReviews='All30 crops inspected by their preparers; independent memory5 and eye3 sample reviews retained, with the memory Figure2 finding resolved above. Root also sampled place Figure1 and S2. No new whole-book scientific acceptance.')
(O/'review-resolution.json').write_text(json.dumps(resolution,indent=2),encoding='utf-8')
note=f'''### {now.isoformat()}: foldable examples and original paper figures complete

- All nine example panels now start collapsed and can be opened. Run-in titles have separate control labels. The existing synthesis subheading and its link remain, with a short “Calculation and figure” control below it. Existing examples, equations, blue definitions, highlights and guide illustrations retained.
- Added 30 exact artwork excerpts from the three local paper PDFs and supplements: 5 memory, 15 eye, and 10 place figures. Each is beside its discussion in an expandable original-paper section, with source author/year, original figure number, PDF page and full-size image links. Figure-specific body PDF links now open the embedded excerpt; the PDF remains linked in its caption. No generated replacements or long copied source captions.
- Source page numbers, crop rectangles and hashes are recorded in `verification/paper-excerpts-20261028/`. All30 crops inspected, with bounded independent checks and an evidence-based resolution of one mistaken review suggestion. Exact reversal checks preserve all original manuscript content outside the recorded presentation edits. All9 controls/30 images, local source/image links, and image hashes pass. Standard release audit passes; previous development-lock attention and historical semantic-review status remain.
- Browser checks sample four pages: real example opening/closing; headed synthesis example; original figure opening from its anchor; full-size image navigation; and 390px horizontal figure panning without page overflow. Source labels retain their display size on narrow screens. Screen base stays11.9px; print styles for existing material unchanged. No whole-book pixel sweep or new scientific audit.
- Wall elapsed {elapsed/60:.1f} minutes from {state['startedAt']}; awake execution unverified; token stats unavailable. No required work remains in this scope. Preview: https://vrdell15.tail8b993e.ts.net/burak/chapters/ch-memory-long-delays.html#fig-paper-memory-1 .

'''
p=R/'CURRENT_STATE.md';text=p.read_text(encoding='utf-8');assert '## Open work\n\n' in text
p.write_text(text.replace('## Open work\n\n','## Open work\n\n'+note,1),encoding='utf-8')
(O/'RESULTS.md').write_text('# Example folds and original paper figures\n\n'+note,encoding='utf-8')
print(json.dumps(dict(finishedAt=now.isoformat(),wallElapsedMinutes=round(elapsed/60,1),status='Complete')))

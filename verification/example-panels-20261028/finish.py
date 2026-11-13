from pathlib import Path
import datetime,json
O=Path(__file__).resolve().parent;R=O.parents[1]
s=json.loads((O/'STATE.json').read_text());now=datetime.datetime.now().astimezone()
elapsed=(now-datetime.datetime.fromisoformat(s['startedAt'])).total_seconds()
s.update(checkpointAt=now.isoformat(),status='Complete',wallElapsedSeconds=round(elapsed,1),tokenStats='unavailable',checks='Nine panels in seven affected pages; original rendered text, headings, images and links unchanged; reported example visually checked at normal and 390px widths; exact source reversal passed',remainingWork='none')
(O/'STATE.json').write_text(json.dumps(s,indent=2),encoding='utf-8')
note=f'''### {now.isoformat()}: standalone example panels complete

- Wrapped all nine standalone labeled examples across seven chapters in the existing shared worked-calculation panel. The examples remain visible, with pale background, border and padding; complete calculations, associated figures and their explanations stay together. All prose, equations, heading IDs and source links preserved. No font, figure dimensions or shared print styles changed.
- Scoped checks confirm all nine panels and unchanged text, headings, images and links in the seven affected HTML pages. Reported foundations example inspected in the browser at normal and 390px widths; no page overflow or math errors. Evidence and snapshots: `verification/example-panels-20261028/`. HTML rebuilt and served through the existing VPN address. No new scientific review or whole-book visual sweep.
- Wall elapsed {elapsed/60:.1f} minutes from {s['startedAt']}. Awake execution unverified; token stats unavailable. No required work remains in this scope. The mechanically generated state above predates this presentation-only source change.

'''
p=R/'CURRENT_STATE.md';text=p.read_text(encoding='utf-8');assert '## Open work\n\n' in text
p.write_text(text.replace('## Open work\n\n','## Open work\n\n'+note,1),encoding='utf-8')
(O/'RESULTS.md').write_text('# Example panels\n\n'+note,encoding='utf-8')
print(json.dumps(dict(finishedAt=now.isoformat(),wallElapsedMinutes=round(elapsed/60,1),status='Complete')))

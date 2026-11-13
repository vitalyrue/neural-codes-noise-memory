from pathlib import Path
import json,datetime,re
O=Path(__file__).resolve().parent;R=O.parents[1]
now=datetime.datetime.now().astimezone();s=json.loads((O/'STATE.json').read_text())
start=datetime.datetime.fromisoformat(s['startedUtc'].replace('Z','+00:00'))
last=datetime.datetime.fromisoformat(s['checkpointUtc'].replace('Z','+00:00'))
s.update(checkpointUtc=now.astimezone(datetime.timezone.utc).isoformat(),finishedAt=now.isoformat(),status='Complete',wallElapsedSeconds=round((now-start).total_seconds(),1),sincePreviousPersistedCheckpointSeconds=round((now-last).total_seconds(),1),tokenStats='unavailable',browserScope='Three representative pages including 390px; no whole-book pixel sweep',semanticScope='Presentation-only inline markup; exact source reversal and rendered text equality; historical scientific review records not rebound to new hashes')
(O/'STATE.json').write_text(json.dumps(s,indent=2),encoding='utf-8')
minutes=s['wallElapsedSeconds']/60
results=f'''# Reader emphasis completed

Completed {now.isoformat()}. Started {s['startedUtc']}; wall elapsed {minutes:.1f} minutes. Awake execution unverified. Token stats unavailable.

- Added 76 selected key problem/result spans across the reading guide and 13 chapters. Selected definitions now include their defining wording in blue: 90 spans in teaching text and 97 glossary entries. Existing 194 term markers remain intact.
- The user's exact selected phrase remains highlighted. Bounded independent selection reviews accepted the spans after removing one repetitive roadmap highlight and keeping the neutral-mode and small-perturbation assumptions with the memory-displacement result. The proposal to remove the user-selected fragment was declined because the user expressly requested it.
- Source changes add inline markup only. The edit ledger reverses exactly to all 15 original source files, including line endings. All 19 rendered pages have exactly the same normalized main text before and after. All 76 amber and 187 blue spans render, with no leaked Markdown.
- New colors are screen-only. Original 11.9px typography, print rules, images and equations remain. Generic bold labels inherit the normal text color; definition terms and explanations retain blue.
- Rebuilt HTML with the pinned Publisher 0.8.23 / Quarto renderer, copied the eight checked paper assets, and refreshed stylesheet URLs. Static site is served at the existing private VPN address.
- Browser samples: reading-guide selected passage; memory-dynamics result with its assumptions, blue definitions and math; foundations at 390px with a real derivation open/close. Colors, 11.9px size, no horizontal page overflow and no math errors confirmed. Three screenshots saved. Viewport reset.
- Standard release audit passes. Current doctor still reports development lock attention and requires semantic review for changed model hashes. No historical scientific review was rebound to these new hashes, and this task makes no new whole-book scientific acceptance claim.

Reader link: https://vrdell15.tail8b993e.ts.net/burak/frontmatter/ch-reading-guide.html#sec-reading-mechanism-math

Evidence: selections-*.json, review-*.json, integration.json, edit-ledger.json, render-checks.json, browser-checks.json, build.log, release-check.json, and the three JPG screenshots in this folder.
'''
(O/'RESULTS.md').write_text(results,encoding='utf-8')
current=R/'CURRENT_STATE.md';text=current.read_text(encoding='utf-8')
entry=f'''### {now.isoformat()}: reader emphasis complete

- Added 76 amber key problem/result spans and 187 blue definition passages across the reading guide, 13 chapters and glossary. The user's selected mechanism/math sentence is highlighted. All 194 original first-term/glossary markers remain.
- Presentation-only change: exact reversal proves all original source text and equations preserved, and normalized main text is identical across all 19 rendered pages. Screen styles preserve 11.9px typography and existing print rules. Independent bounded selection review, integration decisions and checks are in `verification/emphasis-20261028/RESULTS.md`.
- HTML rebuilt; three browser samples include actual derivation open/close and 390px wrapping. Existing VPN link updated: https://vrdell15.tail8b993e.ts.net/burak/frontmatter/ch-reading-guide.html#sec-reading-mechanism-math . Standard release audit passes. Historical scientific reviews and development lock attention remain; no whole-book scientific reacceptance claimed.
- Wall elapsed {minutes:.1f} minutes since {s['startedUtc']}; awake execution unverified; token stats unavailable. No required work remains in this formatting scope.

'''
assert '## Open work\n\n' in text
text=text.replace('## Open work\n\n','## Open work\n\n'+entry,1)
current.write_text(text,encoding='utf-8')
print(json.dumps(dict(finishedAt=now.isoformat(),wallElapsedMinutes=round(minutes,1),status='Complete')))

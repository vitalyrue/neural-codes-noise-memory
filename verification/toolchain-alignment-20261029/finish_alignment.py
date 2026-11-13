from pathlib import Path
import datetime
import hashlib
import json
import os
import shutil
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[2]
OUT = Path(__file__).resolve().parent
RELEASE = Path('C:/dev/NBIS/publisher-releases/0.8.23')
state = json.loads((OUT / 'STATE.json').read_text(encoding='utf-8-sig'))
now = datetime.datetime.now().astimezone()
started = datetime.datetime.fromisoformat(state['started'])
elapsed = (now - started).total_seconds()
before = json.loads((OUT / 'reader-inputs-before.json').read_text())
changed = [p for p, digest in before.items()
           if hashlib.sha256((ROOT / p).read_bytes()).hexdigest() != digest]
assert not changed, changed
summary = json.loads((OUT / 'quality-gate-summary.json').read_text())
browser = {
    'checked_at': now.isoformat(),
    'page': 'https://vrdell15.tail8b993e.ts.net/burak/chapters/ch-memory-dynamics.html',
    'method': 'Existing in-app browser tab reloaded; actual accessibility clicks',
    'example': 'Example: a disturbance that slides while it decays.',
    'initially_collapsed': True,
    'opened_by_click': True,
    'closed_by_click': True,
    'scope': 'One live control sample; no broad visual or scientific review'
}
(OUT / 'browser-check.json').write_text(json.dumps(browser, indent=2), encoding='utf-8')

entry = f'''### {now.isoformat()}: released tool versions aligned

- Replaced development placeholders with verified Publisher 0.8.23, teaching skill 2.1.0-rc.38, quality gate 1.0.25 and released diagram skill 1.6.1. Live upstream main and release tag resolve to 825ab072f34e06df5d8da6f31552fa0206073045. The clean export matches all 456 tracked files exactly. Installed teaching/quality packages already matched; no reinstall was needed. Global local diagram 1.6.2 remains unchanged; this book uses the frozen 1.6.1 bundle explicitly.
- Connected the existing NBIS Vale profile with its original rule settings through an absolute styles path. This is an external local dependency, not a bundled Publisher default. All 35 reader content/style inputs remain unchanged. Structure comparison found only a book hash difference, so that hash record was refreshed. Rebuilt HTML once, synchronized eight paper assets, checked local links, and opened/closed one live example.
- Formal quality gate ran and FAILED: structural audit passes; Vale reports 2211 automated flags; paragraph review packets remain pending; 52 figures have missing or outdated formal review records. Flags are not confirmed defects. Historical scientific and figure reviews remain unchanged. The Publisher semantic ledger requires current review for 15 of 16 reader units. No whole-book acceptance is claimed.
- Evidence: verification/toolchain-alignment-20261029/RESULTS.md, quality-gate-summary.json and doctor.json. Version alignment is complete. Remaining work is editorial flag review and proper current teaching/figure acceptance, if pursuing a fully accepted guide. Do not mark packets accepted merely to clear the gate.
- Wall elapsed {elapsed / 60:.1f} minutes since {started.isoformat()}; awake execution unverified. One commentary clock label was corrected using the system clock; no clock-change conclusion was drawn. Token stats unavailable.

'''
current = ROOT / 'CURRENT_STATE.md'
text = current.read_text(encoding='utf-8')
assert 'released tool versions aligned' not in text
current.write_text(text.replace('## Open work\n\n', '## Open work\n\n' + entry, 1), encoding='utf-8')

# Preserve the earlier diagnostic rather than rewriting its historical result.
for name in ('doctor.json', 'doctor.log'):
    shutil.copy2(OUT / name, OUT / ('before-rebuild-' + name))
env = dict(os.environ, PYTHONPATH=str(RELEASE / 'src'), PYTHONUTF8='1')
result = subprocess.run([
    sys.executable, '-X', 'utf8', '-m', 'book_runtime.cli', 'doctor',
    '--project', 'guide-project.yaml', '--installed-skills-root',
    'C:/Users/vital/.codex/skills', '--write-checkpoint'
], cwd=ROOT, env=env, capture_output=True, text=True, encoding='utf-8')
(OUT / 'doctor.log').write_text(result.stdout + result.stderr, encoding='utf-8')
assert result.returncode == 0, result.stderr
shutil.copy2(ROOT / '.build/doctor.json', OUT / 'doctor.json')
doctor = json.loads((OUT / 'doctor.json').read_text())
assert doctor['release_audit']['structure_lock_hash']
assert doctor['release_audit']['status'] == 'passed', doctor['release_audit']['findings']
assert doctor['release_audit']['artifacts']['html']['model_linkage']['status'] == 'verified'

report = f'''# Publisher and teaching skill alignment

Completed {now.isoformat()}. Wall time {elapsed / 60:.1f} minutes. Awake execution time unverified. Token stats unavailable.

`development` was an old placeholder in the guide's version files. It did not identify the installed tools. The latest verified upstream release is Publisher 0.8.23, commit `825ab072f34e06df5d8da6f31552fa0206073045`. Upstream main has the same commit.

| Component | Guide version | Action |
| --- | --- | --- |
| Publisher | 0.8.23 | Selected exact clean release export |
| course-study-guide-builder | 2.1.0-rc.38 | Already installed exactly; updated guide lock |
| course-quality-gate | 1.0.25 | Already installed exactly; updated guide lock |
| course-diagram-builder | 1.6.1 | Use frozen release bundle; global local 1.6.2 preserved |

Independent checks confirm the guide locks and manifest hashes. All 456 tracked files in the release export match the commit exactly, including line endings. No reinstall was necessary. The existing NBIS prose-check profile is now connected through `.vale.ini`; the shared styles remain at `C:/dev/NBIS/performance-engineering-course/styles`. This is a local external dependency. No rule severity was changed and no style package was downloaded.

All 35 reader content/style files remain byte-identical. Structure fields also match exactly; only the BookModel hash changed, so the structure record was refreshed. HTML was rebuilt once with the selected runtime, eight paper assets were synchronized, and local HTML checks passed. One example control was opened and closed in the live memory-dynamics chapter. No new broad visual or scientific audit was performed.

## Quality gate result

The formal quality gate **ran and failed**. Structure passed. Vale reported 2211 flags (660 error-level, 209 warnings and 1342 suggestions). These are automated rule hits, with overlapping rules and possible technical-notation false positives; they are not 2211 confirmed writing defects. Fresh paragraph review packets are pending. Formal figure checks reported missing/outdated records across 52 figures (98 findings: 31 missing, 47 changed inputs and 20 changed context). These findings do not mean all figures are incorrect.

Existing scientific and figure review records were preserved. The semantic ledger currently allows reuse for References and requires current acceptance for the other 15 reader units. Fresh review packets were saved separately and were not labeled accepted.

After the hash refresh and rebuild, the standard release audit passes and HTML linkage is verified. Doctor still reports `attention`, with release status `staging-only`, because current teaching acceptance is incomplete. Passing the ordinary build/output checks is not whole-guide acceptance.

## Evidence and continuation

- `alignment-receipt.json`: exact package checks and Vale profile hashes.
- `source-export-check.json`: independent source equality check.
- `final-alignment-check.md`: independent version/configuration review before the rebuild.
- `structure-comparison.json`: structure unchanged except model hash.
- `quality-gate-final.json` and `quality-gate-summary.json`: failed formal gate and concise counts.
- `doctor.json`: final matched versions, verified HTML and remaining review requirements.
- `html-check.log`, `browser-check.json`, `build.log`: rebuilt output checks.

Version alignment is complete. A fully accepted guide still needs review of the prose flags and current teaching/figure acceptance. Do not convert pending records to accepted without the required reviews.
'''
(OUT / 'RESULTS.md').write_text(report, encoding='utf-8')
finished = datetime.datetime.now().astimezone()
state.update(checkpoint=finished.isoformat(), finished=finished.isoformat(),
             wall_seconds=(finished-started).total_seconds(), awake='unverified',
             status='Version alignment complete; formal quality gate failed and teaching/figure acceptance remains open',
             quality_gate='fail', standard_release_audit='passed', html_linkage='verified',
             reader_inputs_unchanged=len(before), token_stats='unavailable')
(OUT / 'STATE.json').write_text(json.dumps(state, indent=2), encoding='utf-8')
print(result.stdout)
print(json.dumps({'finished': finished.isoformat(), 'wall_minutes': round((finished-started).total_seconds()/60, 1), 'version_alignment': 'complete', 'quality_gate': 'fail'}, indent=2))

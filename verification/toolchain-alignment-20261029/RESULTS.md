# Publisher and teaching skill alignment

Completed 2026-10-29T11:57:19.034641+02:00. Wall time 16.3 minutes. Awake execution time unverified. Token stats unavailable.

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

# Eye anatomy before eye-angle coding

Started 2026-11-01T10:29:17Z. Scope: the teaching dependency between the opening of Chapter 1 and the physical explanation formerly introduced in Chapter 2. Awake execution time is unverified.

The former placement followed subject grouping: eye mechanics appeared beside the Chapter 2 persistence model. It did not satisfy the reader's earlier need to understand what the Chapter 1 spikes and angles refer to. The revised path is: spike and firing-rate definitions, motor neurons and muscles, maintained force and eye angle, rate patterns representing that angle, variable spike counts, then stability of a stored value.

## Content changes

- Added sec:FOUNDATIONS-EYE-ACTION as the first Chapter 1 section. Moved the original spike/rate definitions and the reviewed eye anatomy, repeated-spike explanation, mechanical-role bullets and key statement there. The physical setting now precedes the tuning curve.
- Retained sec:FOUNDATIONS-SPIKES and all of its synaptic interaction, recurrence, tuning and population-code teaching. Its first two definitions moved to the immediately preceding section.
- Kept sec:PERSISTENCE-EYE-MECHANICS and its folded torque calculation, integrator experiment and plasticity explanation in Chapter 2. A new bridge explicitly builds on Chapter 1.
- Updated chapter openings, sidecar summaries, the eye-drift link and the three source-coverage locations affected by the move. Reordered five background bibliography entries to follow first use. No source was removed.
- Retained every previous section anchor and equation. Added one section anchor. No artwork, typography or print rule changed.

## Verification

The separate order-stage1/2/3.json records cover correctness, necessity/terminology and the connected reading sequence. Stage 1 confirmed unchanged scientific passages, all equations and citations retained, and source-supported boundaries. The local concept-index packet makes the selected dependency judgments explicit; unreviewed parts of the two chapters must remain marked as such.

The three affected chapters pass pinned Publisher validation. Source checks preserve every old anchor and resolve all footnotes. Prior mathematical checks apply because the equations are unchanged; numerical calculations and figures are not being re-reviewed in this ordering correction.

HTML build and postprocessing completed. Three live HTTPS pages match the local HTML and their local anchors resolve. A representative browser inspection shows the anatomy in1.1 before the code in1.2, with blue definitions,11.9px text and the Poisson fold retained. All three scoped review stages passed. The concept diagnostic found no problems among15 reviewed relations; coverage stays partial because five unaffected sections were not audited.

Publisher doctor was run with --write-checkpoint as required by the project. Its broader release/semantic state is separate from this focused acceptance. The current summary is in doctor.log and the detailed result remains at .build/doctor.json. This local revision does not clear the existing whole-book figure or wider release holds.

Completed 2026-11-01T10:40:33.274438+00:00. Wall time 676 seconds. Awake execution time unverified; token statistics unavailable.


## Follow-up: actual source links in the Chapter3 opening

Requested 2026-11-01T10:41:24Z; completed 2026-11-01T10:44:57.228566+00:00. Replaced one unclear instruction about PDF viewer navigation with an author/year source line and clickable paper and Supporting Information links. No scientific text, equations or figure changed. The scoped Chapter3 HTML build and project postprocessing completed; both local PDF targets exist and live HTTPS bytes match the rebuilt chapter. See citation-note.diff and citation-note-checks.json. No additional semantic or figure review was needed for this presentation-only change.


## Follow-up: jump-process wording and v/W reminders

Started 2026-11-01T10:46:58Z. User annotations asked what “still” refers to, what v means, and whether W was defined. Replaced the vague transition with the unchanged effect of individual spikes before the continuous-noise approximation. Added the local angular meaning of v_i before the variance derivation and reminded readers of the j-to-i meaning of W_ij before the symmetry condition. Both reminders link to their earlier definitions. Existing displayed equations, assumptions and figures remain unchanged.

Separate notation-stage1/2/3.json reviews passed for correctness, necessity/terminology and connected flow. The scoped Chapter3 build and project postprocessing completed. The served page matches local HTML; new internal links resolve. See notation-live-checks.json. No numerical rerun, figure acceptance or whole-book semantic acceptance is claimed.

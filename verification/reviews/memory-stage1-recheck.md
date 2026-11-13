# Focused memory stage 1 repair recheck

Reviewer: independent agent /root/review_memory_guide. Local request ID memory-stage1-recheck-20261022T193742+0300. This is truth/reasoning only, using the previous open read as context. No full repeat of unchanged material and no chapter edits. Requested configuration in PLAN is GPT-6.1-sol/high; exact runtime model/version is not exposed.

Start: 2026-10-22T19:37:42.9924277+03:00. Checkpoints: 19:38:07.5685025 and 19:38:22.2585595, on the same date/offset. End, measured wall duration, and before/current SHA256 values are in JSON. Awake execution duration is unverified; no sleep/resume log claim. Token stats unavailable.

## Decisions

| Finding | Current passage and affected connection | Decision and reason |
|---|---|---|
| M1 | 03-memory-information.md, sec:MEMORY-BOUND, lines 103–127; p1-equality footnote line 462; sec:MEMORY-EXTENSIONS line 427 | Closed after a second focused read at 19:39:02.9888600. The pointwise condition, exponential sufficiency, and linear zero-bias counterexample are correct. The counterexample has attracting transverse eigenvalue -2/tau and gives 2DJ=tau^-2 at every positive theta. Its shared input ratio changes between states, proving why continuous variation alone is insufficient. The initial recheck found a downstream sentence still asserting Poisson exponential necessity; root repaired it within this same request. Final line 427 correctly presents linear-Gaussian and exponential-Poisson rules as sufficient classes and explicitly retains the general pointwise condition and linear-family counterexample. |
| M2 | 02-memory-dynamics.md, sec:MEMORY-SYMMETRIC, line 216; source footnote line 335 | Closed. Correct formula is tied to SI S18, and the supplied main Eq.2 missing square is described as an apparent error independently checked, without claiming an author correction. The symmetry/invertibility assumptions remain present. |
| M3 | 02-memory-dynamics.md, sec:MEMORY-LONG-TIME, lines 237–260, connected to 278–293 | Closed. Taylor expectation removes the mean term, retains D F'' dt, and states the higher-order diffusion remainder. Averaging against p and twice integrating by parts gives both derivatives on Dp. Compactly supported test functions or vanishing boundary terms justify the step. The following zero-drift moment identities and D D'' correction still follow, with their boundary qualifications preserved. |
| M4 | glossary.md, line 47; foundations conditional-noise explanation lines 60–62 | Closed. The lookup entry now distinguishes deterministic-intensity Poisson independent increments from recurrent conditional instantaneous generation. It no longer promises independent full recurrent spike trains. |
| M5 | 01-foundations.md, sec:FOUNDATIONS-SPIKES, lines 23–25; glossary line 45 | Closed. Hippocampal setting and localized regions of elevated firing are included, multiple fields are allowed, and the next paragraph distinguishes entorhinal repeated grid fields. Rate-map and field-measurement qualifications remain intact. |

## New supplied figure fields

Read `01-foundations.yaml`, block `fig:FOUNDATIONS-ATTRACTOR`, final caption and alt fields, against body lines 107–143 and SVG labels/coordinates checked in the first stage 1 call. Retain the caption: common activity perturbation relaxes back, along-line perturbation persists, solid arrow means deterministic recovery, dashed arrow means imposed disturbance, and the example is a guide construction rather than data. These are the actual actions in the equations and SVG. Retain alt text for truth: axes are rates in Hz, states are (50,30), (53,33), (53,27), and the last corresponds to 6.5 degrees. Missing spaces in the alt string are a later wording/accessibility check, not a false claim. Other sidecar fields merely repeat the already reviewed heading/first-paragraph text and are not new mathematics.

## Numeric and source checks

Read `verification/checks/equality-counterexample.json`: tau=.1, theta=100, 2D=500, J=.2, product 100=tau^-2. This agrees with the independent derivation and numerical eigenvector check in the original review. It is evidence for the teaching counterexample, not a paper-network simulation. Reused source facts remain tied to the original P1/P1SI hashes; no source changes were needed. The reading-guide scope/inconsistency statements remain compatible with the new qualifications.

Stage 2 and stage 3 are not performed. All five original findings and affected connections are closed for stage 1 at the current hashes. The new figure caption/alt claims also pass truth review. This does not claim new full-book review, output-rendering checks, or completion of later stages.

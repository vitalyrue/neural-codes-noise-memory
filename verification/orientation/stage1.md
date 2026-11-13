# Stage 1: truth and reasoning

Verdict: two local repairs required. The main scientific accounts distinguish a mathematical constraint, an inference from recordings, and a proposed statistical explanation correctly.

## Required repairs

**O1, P2, 00-reading-guide.md line 21:** The first definition of fixational drift is too broad. Small irregular fixation movements also include microsaccades. The original paper describes smooth continuous motion between rapid movements. Proposed repair: “Between brief, rapid eye movements, the eyes make small, smooth, irregular movements called fixational drift.” Preserve the current term markup. Update the mirrored eye-section summary in the chapter YAML. The later Chapter 4 opening already makes the distinction. Source: Ben-Shushan et al.2022, p.2 introduction, first paragraph; source extraction lines38-44.

**O2, P2, 00-reading-guide.md line 31:** “Parameters set from field sizes and spacing” appears to describe fitting across 1D, 2D and 3D, but it describes the long-tunnel 1D fit only. The 2D comparison uses field size and count; 3D uses field volume and occupied fraction. Proposed repair: “Parameters fitted to field sizes and their spatial arrangement also support further tests of field shapes and connectedness.” The footnote already acknowledges extra gain fitting; exact fitting details belong in Chapter 5. Source: Mainali et al.2025, STAR Methods Parameter inference in 1D, 2D and 3D environments, pp.e2-e3, extraction lines989-1014. Gain adjustment is additionally described in Statistics of field shapes and Euler characteristics.

## Claim judgments

| Paragraph line | Verdict | Scientific judgment |
| --- | --- | --- |
| 3 | Pass | Tasks provide legitimate scientific motivation; no claimed proof. |
| 7 | Pass | Field description and model/recording roles are accurate; each paper is not said to collect recordings. |
| 9 | Pass | The three motivating limitations match the sources. |
| 13 | Pass | Continuous memory and persistent activity are accurately framed as the investigated problem and proposed mechanism. |
| 15 | Pass | Continuous family, stochastic signaling, weak fluctuations, analysis, simulations and ideal-observer relation match 2012 pp.1-3. |
| 17 | Pass with scope note | Eq.4 lower-bound direction is correct. Diminishing readout benefit matches Eq.5/Fig.3. Error growth is qualitative; do not strengthen it to linear growth forever. Long-delay boundary and state-dependence limits remain in connected chapters. |
| 21 | Repair O1 | Retina motivation is sound; distinguish smooth drift from rapid fixation movements. |
| 23 | Pass | 57 neurons, two macaques, paired recording, larger-motion calibration, one-cell comparison and separate model match the paper. |
| 25 | Pass | About 82% means inferred horizontal displacement variance over 350 ms under assumptions. It is not distance traveled or a direct integrator measurement. A possible circuit mechanism is kept distinct. |
| 29 | Pass | Place-cell and field meanings, classical small-space picture and larger-space heterogeneity match 2025 pp.1110-1111 and Chapter 1. |
| 31 | Repair O2 | Model and comparison methods are accurate, but the parameter-fitting summary generalizes one 1D procedure. |
| 33 | Pass | Size distributions, peaks and holes are statistical/model predictions; random inputs remain a possible explanation rather than measured unique wiring. |
| 35 | Pass | The theorem, upstream-source inference and spatial statistical description are separated. Chapter 6 presents joint biological testing as further work. |

The new citations point to the relevant primary introductions, results and discussions. The 2012 citation does not repeat the questionable printed universal total-error inequality. The eye citation and text preserve the 350 ms horizontal-variance interpretation. The place citation correctly notes additional gain fitting. Source and rule SHA-256 hashes, expanded paragraph judgments, exact findings and timing are in stage1.json.

Chapter metadata matches the reader text. First-teaching records correctly point to frontmatter line 21 for drift and line 29 for place cell and place field; foundations definitions remain intact. The meaning of those place terms is unchanged. Apart from O1, no correctness conflict was found in the transition to the existing chapters.

This call reviewed truth and reasoning only. Wording/necessity and reader understanding require separate calls. No manuscript, metadata or ledger edits were made. No new build or visual checks were run.
Completed: 2026-10-23T23:03:27.2371460+03:00. Wall-clock elapsed from root start: 563.4 seconds. Review elapsed from 23:01:12.719: 134.5 seconds. Awake execution unverified. Time since 23:02:10 checkpoint: 76.7 seconds. Token stats unavailable.


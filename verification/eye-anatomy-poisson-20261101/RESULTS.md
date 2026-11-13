# Eye anatomy and Poisson derivation revision

Started 2026-11-01T10:03:05Z (12:03:05 Asia/Jerusalem). Awake execution time is unverified; no sleep/resume log audit was needed for this focused task.

## Requested changes

- Foundations: explain the Poisson count formula inside the existing folded mathematical explanation. Independent small-bin trials give the binomial formula; taking a fixed-count limit explains the exponential, power and factorial. Shifted sums then give the mean and variance. The distinction between a predetermined rate and a history-dependent recurrent intensity is explicit.
- Persistence: introduce eye anatomy and neural-to-muscle control before attractor geometry. Six muscles, cranial nerve routes and opposing torques establish the physical setting. Repeated firing maintains muscle force; elasticity, viscosity and inertia have different roles. A folded linear mechanical approximation connects torque and stiffness to held angle and viscosity/stiffness to passive return time. Neural integration and longer-term plasticity are supported by separate monkey and goldfish experiments.
- Eye-drift chapter: link back to the earlier introduction and avoid repeating the first definitions of ocular motoneurons and the integrator.
- Add eight glossary entries and five background references. Preserve all 38 previous bibliography entries and update their numeric cross-references.

## Content-change ledger

| Material | Treatment | Reason / destination |
| --- | --- | --- |
| Foundations Poisson PMF and mean/variance | Retained, derivation extended | sec:FOUNDATIONS-POISSON; new steps answer the requested why |
| Original silent-cell example and illustration | Retained | Same fold, calculation and figure |
| Recurrent-rate qualification | Rewritten | Avoid claiming an endogenous rate gives a Poisson distribution over a whole interval |
| Persistence chapter opening | Rewritten | Motivate eye mechanics before the neural model |
| Eye anatomy and torque explanation | Added | sec:PERSISTENCE-EYE-MECHANICS |
| Existing attractor, diffusion and spatial-map teaching | Retained verbatim | Original sections and anchors remain |
| OMN and integrator first definitions | Moved earlier | Defined in Persistence; Eye-drift now links back |
| Existing glossary and reference entries | Retained | Eight terms and five sources added; reference numbering adjusted |
| Images, screen typography and print rules | Unchanged | No new artwork or full figure acceptance requested |

## Review evidence and limits

Independent reviewers assessed the actual revised sources in separate sequential truth, terminology/necessity, and connected-reading stages. See poisson-stage1/2/3.json and eye-stage1/2/3.json. The eye review corrected velocity-to-position integration wording, a missing source author, the horizontal-angle restriction and an early unexplained anatomy term. Final Stage 3 reviews passed within the changed scope.

The five sources are recorded with specific locations in the source inventory, coverage table and research ledger. Anatomy uses UTHealth's teaching chapter. Anderson et al. (2009), Cannon and Robinson (1987), and Major et al. (2004) support the separate mechanical, integrator and plasticity claims. The mechanical equation is explicitly a teaching approximation. The MIT lecture notes support the independent-bin probability construction; symbols are translated to the guide's rate/count convention.

Focused source checks preserve all original anchors, find only the intended new section, and retain all original bibliography entries. Numerical checks confirm normalization, mean and variance for three Poisson parameters and convergence from finite-bin probabilities. These checks are consistency checks, not proofs or reproductions of experiments. The three changed chapters passed Publisher validation using pinned Publisher 0.8.23.

Native Vale 3.24.0 checked the five changed files. The report retains raw alerts and changed-line locations. A separate editorial assessment distinguishes mathematical limit language, literal anatomy, necessary model limitations and bibliography punctuation from removable filler. This is not a zero-alert automated prose verdict or whole-book quality acceptance.

HTML build completed with pinned Publisher 0.8.23 and Quarto 1.10.18. Project postprocessing copied eight checked paper assets and retained the authored Part maps. The two live HTTPS pages match their local HTML bytes. Browser checks confirmed collapsed defaults, working disclosures, rendered equations, blue definitions, amber key statements and 11.9px reading text. Initial cached pages required an explicit reload. All local internal anchors in the three changed chapters resolve. See browser-checks.json and live-and-link-checks.json.

Whole-book figure acceptance, DOCX/PDF and public release remain outside this task. The full release audit was not rerun for this focused text revision. No zero-alert lint or whole-guide acceptance claim is made.

Completed 2026-11-01T10:26:55.165121+00:00. Wall time 1430 seconds. Awake execution time and token statistics are unavailable.

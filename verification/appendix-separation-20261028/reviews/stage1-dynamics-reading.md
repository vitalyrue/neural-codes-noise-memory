# Stage 1: correctness and reasoning, dynamics and reading guide

Local request ID: stage1-dynamics-reading-20261028-165738. Reviewer: separate_readout, independent of the authors of these files, Sol high. No platform call ID is exposed. Started 2026-10-28T16:57:38.599118+02:00; completed 2026-10-28T16:59:46.678360+02:00.

Scope: current reader text in `02-memory-dynamics.md`, connected reading-guide text in `00-reading-guide.md`, and the new `tbl:READING-APPENDIX` table in its YAML. Audience: undergraduate calculus, probability and linear algebra, without assumed neuroscience. Compared the current text with its baseline after reading the current reader passages and supplied SI I–II. Checked the table's seven appendix page entries against the SI contents and section openings, and all twelve guide section links against actual current chapter and section IDs. Did not read author ledgers or historical reviews. Unchanged eye/place findings were context, not a new review of their empirical claims.

## Verdict

No required Stage 1 repair found. The changed model descriptions, general mathematical tools, neural mapping and limited interpretations agree with the supplied source and preserve the original premises. This is a check of the changed order and bridges, not a new complete proof audit or acceptance of unread material.

## Passage-based checks

- **MEMORY-SPIKES, opening through fixed-point interpretation:** the new opening marks fixed weights, biases, common synaptic decay, conditional Poisson counts, tuning and weak total-input fluctuations as model assumptions. The general event-count/decay description maps to the spike process before its equation. SI I S1–S6 supports fixed mean input and variance falling as 1/n under weight scaling. The retained distinction between Gaussian input fluctuations and Gaussian individual spike trains is essential and remains intact. The new final claim that recurrent firing balances synaptic decay follows from the displayed steady-state equation. It does not assert that arbitrary biological circuits have a continuous attractor.
- **MEMORY-LINEARIZATION:** the new opening states one neutral direction, decay of other modes and small perturbations before the Taylor expansion and projection proof use them. The mathematical definition of linearization now precedes the activation substitution. SI II S7–S13 supports the linear kernel and left/right zero vectors. The derivation still explains why the left vector removes decaying modes, and interpretation still distinguishes this from perpendicular projection and retains the explicit teaching-example qualification. No needed premise was moved after its dependent calculation.
- **MEMORY-DIFFUSION:** independent-noise variance addition is the general rule; v supplies the neural weights. The unchanged covariance expansion gives SI S14–S15 with the factor 2 convention preserved. The multi-coordinate pair moved earlier but still follows the scalar covariance calculation and the prior tangent/left-vector definitions; its expression matches SI S21–S24. The interpretation keeps the warning that higher firing rates alone do not determine comparative damage, and keeps both local-time conditions and the separate systematic-drift check. The diffusion-tensor explanation remains later in this section, as before; its increased separation from the formula is a flow question for Stage 3, not an unsupported new mathematical claim.
- **MEMORY-SYMMETRIC:** the new mechanism description correctly states reciprocal equal weights while allowing unequal firing responses. The chain rule is taught before assigning input and rate slopes; K-transpose times g-prime then establishes the left-vector formula. The new interpretation follows the derived expression and leaves symmetry, stable family, noise assumptions, invertibility range and absence of required translation symmetry visible. The main-equation square warning still says it is an independent check, without claiming an author correction. The mutually inhibitory example and its endpoint limit are retained unchanged.
- **READING-MECHANISM-MATH:** the three roles describe model assumptions, tools, and consequences rather than claiming that mathematical objects are measured neural components. The new readout paragraph says that an ideal estimate is a benchmark and that animal implementation requires separate evidence. The spike example is consistent with a spike changing its outgoing activation, its effects on receiving cells and the resulting lasting shift. The conceptual reading suggestion preserves assumptions as part of both paths.
- **READING-APPENDIX:** sections I–VII start on appendix PDF pages 1, 3, 6, 9, 10, 12 and 17, matching the local source. Its questions fairly describe those sections without promising an exact equation-by-equation reproduction. All twelve current guide destinations exist with matching IDs: spikes; linearization; diffusion; drift scope; long time; Fisher information; information bound; readout setup; naive; ideal; partial; extensions. Checked source IDs and paths, not rendered browser behavior. The local SI PDF file exists. The external PNAS download URL was not fetched; the table's source content and local page entries were checked against the supplied SI.

## Required repairs

None for Stage 1. Stage 2 necessity/terminology and Stage 3 reader-understanding/flow remain separate pending calls. No manuscript edits made, and no HTML rebuild or visual review performed.

## Version hashes

- `C:\dev\clsc\burak-papers\guide\content\chapters\02-memory-dynamics.md`: `837c4b2490bee22b449b75db2d0d575ec639dddf2e4583797fff46a302963607`
- `C:\dev\clsc\burak-papers\guide\content\chapters\00-reading-guide.md`: `359fc0791f1e99150a55e621fc3b3637e0d427c5038d3ec2c256049301cbdba5`
- `C:\dev\clsc\burak-papers\guide\content\chapters\00-reading-guide.yaml`: `7ee74d6dfe7e8c88a63a258a351a6e01a574ff3eb99fd242503dee6da010687e`
- `C:\dev\clsc\burak-papers\research\burak-fiete-2012-si.txt`: `e92cb5b43d206ed99eca6e916cc702f89908228d913176aa850aad9201915552`
- `C:\Users\vital\.codex\skills\course-study-guide-builder\SKILL.md`: `b78068e9874e6d1d97b2017bf8f940492f9b08fc11b74f20fd75019ff388984a`
- `C:\Users\vital\.codex\skills\course-study-guide-builder\references\pedagogy-language-contract.md`: `f4c1eb544cf640b708e1970d9572fdc758fcc6aea806675d01a0256658df847a`
- `C:\Users\vital\.codex\skills\course-study-guide-builder\references\structural-preservation-contract.md`: `8f7b052a3a2ccf194966574da3ad88e69d5d5746f195ffffa59e97d25dbe8a35`
- `C:\Users\vital\.codex\skills\course-study-guide-builder\references\math-code-case-contract.md`: `ce2313f897b63e74ba59a3afe1bbc4046d3aa84584072cda7e76470a7e3cef9a`

Checkpoint: 2026-10-28T16:59:46.678360+02:00. Wall elapsed since this review started: 128.1 seconds; time since previous command checkpoint: 62.2 seconds. Awake execution unverified; no clock change established. Token stats unavailable.

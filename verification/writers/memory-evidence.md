# Memory chapters: writer evidence and handoff

Status: draft complete, writer arithmetic checked; independent three-stage review pending. This record does not accept the chapters.

Writer scope: `content/chapters/02-memory-dynamics.md`, `content/chapters/03-memory-information.md`, and `verification/writers/memory-*` only. Earlier context read: `01-foundations.md` as saved at 2026-10-22T19:20:02+03:00. User audience and structure: `PLAN.md`.

## Persisted wall-clock checkpoints

All timestamps carry the Windows local UTC offset. Awake execution has not been independently verified from sleep/resume events. These differences are wall-clock durations, not CPU or awake durations. Root task began 2026-10-22T19:06:07.5341124+03:00; writer elapsed time below begins at the writer's first measured checkpoint.

| Checkpoint | Timestamp | Writer elapsed | Since previous | State |
|---|---|---:|---:|---|
| Writer start | 2026-10-22T19:10:01.3723126+03:00 | 0 | n/a | Read plan and skill; source derivation and PDF inspection next; estimate 25–35 min |
| Initial source pass | 2026-10-22T19:10:25.6725307+03:00 | 24 s | 24 s | Source equations located; inspect ambiguous PDF symbols |
| Dynamics draft | 2026-10-22T19:14:28.6313180+03:00 | 4 min 27 s | 4 min 3 s | Chapter 2 saved; information/readout next; estimate 15–25 min remaining |
| Both drafts | 2026-10-22T19:20:29.7731823+03:00 | 10 min 28 s | 6 min 1 s | Chapters saved; heading IDs uppercased; checks/coverage next; estimate 7–12 min remaining |
| Numeric checks | 2026-10-22T19:21:27.307018+03:00 | 11 min 26 s | 58 s | 38 recorded numerical checks passed, plus assertions |
| Evidence preparation | 2026-10-22T19:22:13.2241741+03:00 | 12 min 12 s | 46 s | Read earlier chapter and full rule sections; glossary/page record underway |
| Draft freeze | 2026-10-22T19:25:42.845381+03:00 | 15 min 41 s | 3 min 30 s | Both chapters and 26-page evidence ready; local structural checks pass; independent review next |

No clock change was observed in these checkpoints. No sleep/resume investigation was needed for this short writer pass. Token statistics unavailable.

## Sources and source access

Read the complete main and SI extracted text, with targeted repeat reads for equations. Rendered and viewed original PDF pages: main pp. 3–4; SI pp. 9, 14, 16–17, 19. Main p. 2 was rendered as preparation only; rendering is not claimed as visual inspection. The original text and page markers supplied the remaining source coverage. The eight rendered PNGs are working verification files, not inserted artwork. No new artwork generated.

Sources:

- `../papers/burak-fiete-2012-persistent-activity.pdf`, six pages.
- `../papers/burak-fiete-2012-persistent-activity-si.pdf`, twenty pages.
- `../research/burak-fiete-2012-main.txt` and `burak-fiete-2012-si.txt`, page-marked extractions. The PDFs settle ambiguous symbols, especially fractions/signs.

Reader source: Burak, Y., & Fiete, I. R. (2012). *Fundamental limits on persistent activity in networks of noisy neurons*. Proceedings of the National Academy of Sciences, 109(43), 17645–17650. DOI `10.1073/pnas.1117386109`, plus the Supporting Text attached to that DOI. Footnotes identify main/SI locations at consequential claims. DOI network resolution and rendered footnote checks remain with root's publication checks; not performed by this writer.

## Source-page map, in original presentation order

Every location below is a real explicit heading ID. “Covered” means the draft contains explanation at that location; independent review must still decide whether it adequately teaches the source.

| Source ID | Content and disposition | Actual explanation and reason |
|---|---|---|
| P1-p01 | covered, with peripheral introduction consolidated | `ch:MEMORY-DYNAMICS`, `sec:MEMORY-SPIKES`, `sec:MEMORY-LINEARIZATION`: why stable persistent firing can still lose the value, neural setup, attractor and weak fluctuation setting. Historical thermodynamics analogies, addresses, author contributions, disclosure and header intentionally omitted because no later calculation depends on them. |
| P1-p02 | covered | `sec:MEMORY-DIFFUSION`, `sec:MEMORY-SYMMETRIC`, `sec:MEMORY-FI`, `sec:MEMORY-FIGURES`: Eq. 1–3, general and symmetric diffusion, finite interval FI vs information rate, and Fig. 1 endpoint projection/readout distinction. Scaling has connected derivation in `sec:MEMORY-COMPARISONS`. |
| P1-p03 | covered | `sec:MEMORY-BOUND`, `sec:MEMORY-EXTENSIONS`, `sec:MEMORY-FIGURES`: scalar proof, equality conditions with isolated-state qualification, matrix inequality proof, extension assumptions, all Fig. 2 panels and simulation-vs-measurement interpretation. |
| P1-p04 | covered | `sec:MEMORY-COMPARISONS`, `sec:MEMORY-NAIVE`, `sec:MEMORY-IDEAL`, `sec:MEMORY-FIG3-AND-CAUTION`: width dimension effect and resource constraint, Eq. 5 derivation, naive optimum and variance ratio, Fig. 3 curves and limits, Eq. 6 algebra issue with strict example. |
| P1-p05 | covered, discussion consolidated | `sec:MEMORY-DRIFT-SCOPE`, `sec:MEMORY-COMPARISONS`, `sec:MEMORY-FIG3-AND-CAUTION`, `sec:MEMORY-SPIKES`: model Eq. 7–11, conjectural correlated-noise scope, sensory/memory compatibility conditions, diffusion vs integration leak, need to check animal spike statistics. Broader regulatory-network/chaotic-network possibilities and the historical literature list are intentionally omitted as nonessential to reconstruction of the three central results. |
| P1-p06 | intentional-consolidation | `sec:MEMORY-SPIKES` teaches weight scaling and leading-order status; `sec:MEMORY-FIGURES` teaches what ring and mutual-inhibition simulations test; `sec:MEMORY-SYMMETRIC` reconstructs the two-cell calculation. Detailed simulation runtime, integrator step sizes, network kernel parameter list, acknowledgments, and bibliography entries are intentionally omitted because no full reproduction is requested and primary guide references are consolidated by root. |
| P1SI-p01 | covered | `sec:MEMORY-SPIKES`: population replication, n neurons per group, 1/n weights, fixed means and shrinking fluctuations. Cover/title/contents have no independent teaching content. |
| P1SI-p02 | covered | `sec:MEMORY-SPIKES`: derive mean scaling n/n and variance n/n², Gaussian approximation of summed input rather than single-cell variables, dense preferred-angle limit. Individual g dynamics do not need a second full derivation because the linear input relation and equivalent activation formulation are shown. |
| P1SI-p03 | covered | `sec:MEMORY-LINEARIZATION`, `sec:MEMORY-DIFFUSION`: Taylor expansion, matrix K, u tangent from differentiated fixed point equation, left-vector extraction, increment covariance and 2D formula. Tilted-decay example explains why the left vector is needed. |
| P1SI-p04 | covered | `sec:MEMORY-SYMMETRIC`, `sec:MEMORY-DRIFT-SCOPE`: prove Kᵀg'=0 and normalize; derive symmetric D; explain why the variance calculation alone does not identify noise-induced mean motion. |
| P1SI-p05 | covered | `sec:MEMORY-DRIFT-SCOPE`, `sec:MEMORY-DIFFUSION`: distinguish Itô and Stratonovich zero-written-drift models, derive D'/2 conversion, order dt/N vs sqrt(dt/N), stochastic tuning assumption, introduce independent multidimensional tangent/left vectors. |
| P1SI-p06 | covered | `sec:MEMORY-DIFFUSION`, `sec:MEMORY-BOUND`, `sec:MEMORY-LONG-TIME`: diffusion tensor via projected covariance, matrix info relation, and forward density motivation. The explicit symmetric multidimensional A inverse form S25–S27 is consolidated into the general vector normalization and covariance formula, which determine the same result; no new physical assumption enters those algebraic components. |
| P1SI-p07 | covered | `sec:MEMORY-LONG-TIME`: density equation, initial point mass, constant D Gaussian solution, wrapped Gaussian construction. Jacobi theta notation and the optional von Mises approximation are intentionally omitted because the exact wrapped sum teaches periodic boundaries with fewer prerequisites. |
| P1SI-p08 | covered | `sec:MEMORY-LONG-TIME`: uniform circular error integral, state dependent D moment equations, integration-by-parts justification, short-time correction D D'' t², reason linear D can still give linear variance. |
| P1SI-p09 | covered | `sec:MEMORY-LONG-TIME`, `sec:MEMORY-FI`: excitation weights, bias and attractor, direct projection gives 2D=theta/(2tau), relation to S40/S41 printing discrepancy; likelihood and FI definitions subsequently derived. |
| P1SI-p10 | covered | `sec:MEMORY-LONG-TIME` explains what Fig. S1 tests; `sec:MEMORY-FI`, `sec:MEMORY-BOUND` derive single/multicoordinate FI and start the information diffusion proof. Trial count/plot deviations are simulation details, not extra evidence of an animal effect. |
| P1SI-p11 | covered | `sec:MEMORY-BOUND`: full Cauchy Schwarz proof equivalent to S45–S49, proportional-vector equality, exponential condition and continuous-range qualification, matrix lower-bound meaning. |
| P1SI-p12 | covered | `sec:MEMORY-BOUND`, `sec:MEMORY-READOUT-SETUP`: residual matrix proof gives PSD result and explains all-direction variance meaning; total recall variance decomposed into storage and readout, conditions retained. |
| P1SI-p13 | covered | `sec:MEMORY-READOUT-SETUP`, `sec:MEMORY-IDEAL`: Gaussian likelihood approximation and limits, independent transition/observation variances, backward precision derivation. The trajectory integral and triangular A matrix are replaced by the equivalent Gaussian recursion, without skipping the marginalization step's variance addition. |
| P1SI-p14 | covered by equivalent derivation | `sec:MEMORY-IDEAL`: compressed later likelihood, transition variance addition, Gaussian precision addition, continuous limit ODE, separated solution and final variance. This replaces covariance inversion/operator algebra with a full independent derivation of the same ideal estimator result. S71/S73 sign mismatch is a source caution footnote and evidence note, not a premise. |
| P1SI-p15 | covered | `sec:MEMORY-IDEAL`, `sec:MEMORY-NAIVE`: coth result, characteristic time and tau bound, Brownian cross-time covariance, double integral and naive optimum. |
| P1SI-p16 | covered | `sec:MEMORY-NAIVE`, `sec:MEMORY-PARTIAL`, `sec:MEMORY-FIG3-AND-CAUTION`: 2/sqrt3 optimum ratio, random thinning gives alpha J, alpha scaling with assumptions, useful numerical example, Fig. S2 reading, and S83 inequality caution. |
| P1SI-p17 | covered | `sec:MEMORY-FIG3-AND-CAUTION`, `sec:MEMORY-EXTENSIONS`: integration accuracy vs integration leak; two-stage synaptic/rate model, linear state matrix and right tangent. |
| P1SI-p18 | covered | `sec:MEMORY-EXTENSIONS`: solve left-vector block equations directly, normalize, derive tau+tau_m in projected variance and info bound. The transformed swapped-time-variable construction S87–S89 is replaced by equivalent explicit linear algebra. |
| P1SI-p19 | covered, references omitted | `sec:MEMORY-EXTENSIONS`: general constant q Gaussian noise, matching likelihood FI, noise projection, Cauchy Schwarz and linear equality rule. q and tau factors remain visible rather than borrowing a normalization from S94–S95. The bibliography is consolidated into the book References rather than copied. |
| P1SI-p20 | intentional-omission | Source bibliography continuation only. Its role is accounted for by the guide's citation to the paper and supplement, and root's References. No new derivation or result is present on this page. |

## Central claims, derivations, and checks

| Claim/equation | Derivation or check | Exactness/limits |
|---|---|---|
| Jump decay equation and s=τr at fixed point | Direct spike response and fixed point cancellation; P1 7–10 | Exact model dynamics before Gaussian replacement |
| Weak Gaussian input fluctuations | n/n and n/n² scaling, matching SI I | Leading large population approximation; individual spike train need not be Gaussian |
| K=-I/τ+diag(phi')W and Ku=0 | Taylor series and derivative of fixed point equation shown | Linearized local dynamics; stable other modes assumed |
| Left-vector projection | vᵀK=0 annihilates stable modes; tilted two-state example integrated | Local leading displacement; no perpendicular projection assumed |
| 2D=sum v²r | Expand independent increment covariance term by term | Poisson conditional innovation model, leading weak noise result |
| Symmetric v and main Eq. 2 | Kᵀg'=0, normalizing vᵀu=1 then substitution | Symmetric W required, K need not be symmetric |
| Two inhibitory cells | K eigenvectors, D, J, bound at balanced/unbalanced states | Numeric script, positive-rate interior only |
| Two excitatory cells | Explicit u=(1,1), v=(1/2,1/2) | Script checks direct D and variance slope, exposes apparent S40/S41 discrepancy |
| Constant/unbounded and circular diffusion | Gaussian solution, wrapped sum, π²/3 uniform limit | Boundary convention visible; circular error is bounded |
| State-dependent variance expansion | Density equation integrated twice by parts; generator on D | Drift-free Itô process, smooth D, boundary terms absent |
| J=sum r'²/r | Poisson log likelihood differentiated, score variance computed | Information rate, not a fixed sample's total information |
| Cramér Rao | Differentiate unbiasedness and apply Cauchy Schwarz | Regular locally unbiased estimates; attainment not universal at finite sample |
| D≥1/(2τ²J), equality | Cauchy Schwarz with v sqrt r and r'/sqrt r; full normalization | Same model assumptions; isolated equality distinguished from exponential across interval |
| Matrix bound | V-U(UᵀU)^-1 residual squared | Script checks a nontrivial conjugate pair and PSD residual; J nonsingular |
| Controlled scaling N/rate/τ/width | Sums/integral measure transformed with held quantities explicit | Width law needs fixed peak, uniform dense coverage, shape, no boundaries; fixed total spikes differs |
| Readout decomposition | Storage Brownian increments + later local readout approximation | Constant D, translation invariant and no informative prior; not exact generic Poisson decoding |
| Naive variance 2DL/3+1/(JL) | Brownian covariance double integral plus independent bin count noise | Exact within the stipulated local Gaussian observation model |
| Ideal coth expression | Backward precision recursion, continuous ODE and explicit solution | Full reasoning supplied; matches S75 using a different derivation |
| Readout optimum and limit | Differentiate naive variance; series/limits of coth | Script checks optimum, ratios, L*/tau and 1/3 characteristic examples |
| Discrete Gaussian consistency | Finite covariance inversion vs separately coded precision recursion | Six direct comparisons (L=.02,.1,.3; n=80,240) agree; continuous discrepancies <2.5%; no simulation |
| Partial readout | Independent thinning derives alpha J, D fixed | Selected cells only give same alpha scaling if they carry that information fraction |
| Two times | Left-vector blocks, normalization, diffusion | Script checks block matrix zero modes and equality; noise enters s block |
| Additive Gaussian case | Explicit q covariance and matching Gaussian score | Same bound; equality linear for symmetric W, constant q |
| Eq. 6/S83 caution | Algebra plus strict D,J,tau example | Apparent printed inconsistency, not an asserted author correction |

The numeric script is `memory-numeric-checks.py`; its saved output is `memory-numeric-results.json` (38 recorded checks passed, plus structural assertions). Python 3 available locally; output records NumPy version. There are no reader-facing code listings, no large parameter scans, and no claimed paper simulation reproduction.

## Suspected source inconsistencies for independent review

These findings were checked against the rendered originals where noted. They remain source issues to assess independently, not author-correction claims.

1. Main Eq. 6 / SI S83 lower-bound direction: combine 2DJ≥τ^-2 with ideal variance sqrt(2D/J) to obtain sqrt(2D/J)≤2Dτ. The asymptotic error expression can equal the printed value at saturation, but the expression is smaller in a strict example. Main p. 4 and SI p. 16 inspected as images. Reader explanation is needed because Eq. 6 is a central result the user asked to understand.
2. SI S40 / S41: the stated s=(theta+b0/2,theta-b0/2) gives u=(1,1), v=(1/2,1/2). With rates summing to 2theta/tau, 2D=theta/(2tau), hence D=theta/(4tau), consistent with S41 slope theta/(2tau). S40 instead displays D=theta/(2tau). SI p. 9 inspected as an image. Guide teaches direct projection and labels the apparent factor discrepancy.
3. SI S71 sign: plus epsilon f'' would give oscillatory solutions, while the following S73 cosh profile satisfies f-epsilon f''=0. SI p. 14 inspected. Main derivation uses independent backward precision recursion, so no reader calculation depends on repairing S71.
4. SI S85 lower-right block: S84 has decay -r/tau_m, so linearization gives -I/tau_m. The supplied matrix prints a plus, verified against SI p. 17 as an image. The guide follows the explicit differential equation and derives left/right blocks.
5. SI S94–S95 printed normalization: explicit Gaussian strength q, matching observation noise and τ factors are reconstructed dimensionally. No independent claim about the authors' intended normalization is needed. The final bound and linear equality condition match the prose conclusions. SI p. 19 inspected.
6. Main Fig. 3 caption points to SI equation numbers inconsistent with supplied readout section; reader footnote identifies S75 and S79–S81. Treat these as stale locators rather than new scientific claims.

## Terms introduced, for glossary integration

Root's foundations already teach spikes, rates, tuning, covariance, fixed points, attractors, and Brownian diffusion. The following exact first-definition spellings appear in these two chapters:

| Term | Meaning for glossary | First teaching ID |
|---|---|---|
| neural transfer function | Function converting a neuron's summed input to its expected firing rate. | sec:MEMORY-SPIKES |
| weak fluctuation approximation | Approximation in which many small spike contributions keep total input fluctuations small and permit a Gaussian description with matched covariance. | sec:MEMORY-SPIKES |
| linearization | First-order approximation of how dynamics change around a reference state. | sec:MEMORY-LINEARIZATION |
| right zero eigenvector | Direction in state space on which a linearized dynamics matrix acts as zero; here the tangent to the fixed point family. | sec:MEMORY-LINEARIZATION |
| left zero eigenvector | Vector whose transpose times the dynamics matrix is zero; normalized here to extract the persistent coordinate change while discarding decaying modes. | sec:MEMORY-LINEARIZATION |
| diffusion tensor | Matrix giving displacement covariance per twice the elapsed time in several represented coordinates. | sec:MEMORY-DIFFUSION |
| Fokker Planck equation | Equation for the time evolution of a probability density under drift and diffusion; this chapter uses its zero-drift form. | sec:MEMORY-LONG-TIME |
| systematic drift | Nonzero average velocity of the represented coordinate. | sec:MEMORY-DRIFT-SCOPE |
| likelihood | Probability of observed data, considered as a function of a proposed parameter value. | sec:MEMORY-FI |
| score | Derivative of the log likelihood with respect to the parameter being estimated. | sec:MEMORY-FI |
| Fisher information | Expected squared score, measuring local distinguishability of nearby parameter values. | sec:MEMORY-FI |
| internal Fisher information rate | Fisher information per unit observation time in the network's spikes about its instantaneous attractor coordinate. | sec:MEMORY-FI |
| unbiased | Describes an estimator whose mean equals the true parameter, here locally over nearby memory states. | sec:MEMORY-FI |
| Cramér Rao bound | Inverse-Fisher-information lower bound on variance of a regular unbiased estimator. | sec:MEMORY-FI |
| precision | Reciprocal of a scalar Gaussian estimate's variance. | sec:MEMORY-IDEAL |

Other potentially unfamiliar concepts are explained directly where used without requiring a separate glossary entry: Itô evaluation convention, Stratonovich conversion, Gaussian precision addition, positive semidefinite matrix inequality, coth and artanh. Left/right vector definitions are matched to their use, rather than assuming general spectral theory.

## Remaining acceptance work

- Independent truth/reasoning, wording/necessity, and reader-flow reviews in separate staged calls. Writer has not self-approved.
- Recheck changed units after any reviewer repairs, using current source/rule hashes.
- Root integrates glossary, complete References, sidecars, crosslinks, and source inventory schema.
- Root verifies rendered equations/footnotes, representative layout, local anchors and DOI resolution. These chapters contain no image insertion or public publication action.
- Broader historical comparisons can live in synthesis. No extra claims were imported from unread citations in the paper's bibliography.

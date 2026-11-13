# Stage 3: reader understanding and flow, memory scope

Reviewer: independent agent /root/review_memory_guide. Local request ID memory-stage3-20261022T195452+0300. Separate stage 3 call after stage 1 and stage 2 rechecks. Requested model configuration GPT-6.1-sol/high; exact runtime model/version is not exposed. No teaching files edited.

Started 2026-10-22T19:54:52.5287737+03:00. Measured checkpoints: 19:55:50.9006926, 19:57:23.8304333, 20:05:09.1219882, 20:06:13.3952094, same date/offset. End and wall duration are in JSON. Awake execution is unverified; no sleep/resume logs were checked. Token stats unavailable. The individual paragraph record took longer than the initial estimate; a long shell-command attempt failed with Windows error206 before creating output, so records were written in smaller bounded groups.

## Reader tasks, prerequisites, and overall judgment

The reader must explain how spike-count fluctuations survive stable relaxation, derive D from a left coordinate extractor, derive J from a likelihood, prove the information bound, and distinguish storage diffusion from observation error. Foundations supply count moments, covariance, fixed/neutral directions, Brownian increments, MSD and min(s,t) covariance. Dynamics supplies exact jump/decay setup, approximation limits, left/right meanings and density evolution. Information supplies score, unbiasedness, the scalar/matrix bound, equality limits and both readout curves. The new Itô/Stratonovich, point-mass, prior and tuning definitions now occur before their dependent reasoning, except that a displayed initial condition is immediately interpreted in the following paragraph, which is an appropriate equation-to-interpretation sequence.

The actual connected reading is sufficient for these tasks except U1 below. This is a substantive review, not a conclusion from a schema or lint count. The scalar Cauchy Schwarz reconstruction and backward Gaussian precision method are suitable alternatives to the supplement's more elaborate proofs: they expose the same necessary factors with fewer unfamiliar objects. The multidimensional residual-square proof is optional for a reader focused on one coordinate but properly scoped and understandable from the declared linear algebra baseline. Its presence does not block the scalar route.

All 288 scoped paragraph objects have an individual purpose, connection, decision and reason in `memory-stage3-paragraphs.json`: 11 reading-guide, 46 foundations, 67 dynamics, 90 information and 74 glossary/reference entries. Two paragraphs, information p207 and p213, need U1; the other286 are retained with concrete reasons. Intervening displayed equations, figure caption/alt and footnote source explanations were read along with the prose. Equations and footnote definitions are not standalone objects in this packet, so the paragraph count does not claim to count every reader-visible item.

## U1: show why storage and readout errors have no cross term

Location: `03-memory-information.md`, sec:MEMORY-READOUT-SETUP, lines205–227, especially p207 (equation at210) and p213. The text states Vtotal=2DT+Vread, identifies both terms, and gives limits. It does not show the error decomposition or why its covariance term vanishes. The intended reader knows the sum-variance rule from foundations lines75–80 and unbiasedness from information lines48–64, but cannot infer independence of the two errors just from those names.

Required short bridge: write x=theta(T), s=x-Theta and e=hat{x}-x, so total error=s+e. Under the homogeneous local readout model with appropriately independent future noise and conditional unbiasedness, establish E[e|storage history]=0. Then E[se]=E[s E(e|storage history)]=0, and Var(s+e)=2DT+Vread. Marginal unbiasedness alone is not enough; the conditional expectation or an equally strong justified argument must be shown. State these conditions before relying on addition, and keep the existing caveats for boundaries, state dependence, priors and initial encoding uncertainty.

Why needed: this is the central separation used in the partial-readout example and the printed-error-bound discussion. Without the step, readers must import the reasoning from expertise. The root has accepted this repair direction; it remains open until the actual revised passages are rechecked.

## Reading order and handoffs across the book

Read PLAN and chapter-plan, both actual Part purposes in the pedagogy packets, all chapter openings/endings, the relevant eye-pathway/covariance/MSD passages, the spatial GP opening and assumption paragraphs, and the synthesis's coordinate-to-rate covariance calculation. This checks the reading path and dependencies; it does not claim a full review of the other authors' bodies.

- Reading guide to foundations: the biological examples precede the missing neural vocabulary. The two disturbance example then turns the opening activity/value distinction into algebra and a figure.
- Foundations to dynamics: foundations p143 explicitly leaves general nonperpendicular projection open; dynamics pp75–144 solve that question with left/right vectors. Foundations p183 derives the exact Brownian covariance later needed by naive readout.
- Dynamics to information: dynamics p328 asks for a statistical lower limit on derived D; information pp9–64 build likelihood and information before using them. The bound is not required before understanding D itself.
- Information to eye drift: information p456 distinguishes readout time from integrator lifetime and calls for biological spike/observation checks. Eye chapter pp3–13 distinguish shared upstream drive from a specific integrator source and introduce integrator, OMNs and plant. Eye pp167–185 explicitly supply the covariance/gain assumptions; pp226–250 reuse MSD and derive measurement-noise subtraction. The 2012 Poisson bound is not asserted to have been measured in the monkeys.
- Foundations to place fields: the alternative route is valid. Foundations pp23–25 and198–200 establish spatial rate maps versus temporal noise. Place chapter pp3–7 repeats what is fixed and what is random; pp9–25 define the random-function distribution, covariance and separate stationarity/isotropy/smoothness assumptions. No memory-readout result is needed to begin that calculation.
- Eye/place to synthesis: eye ending limits localization and emphasizes physical filtering; place ending limits wiring inference and carries thresholded spatial statistics forward. Synthesis pp3–19 distinguish the three mathematical objects; its following R_i(t)=f_i(x(t)) calculation and covariance example combine already taught tuning, linearization and variance. It labels the construction as a guide calculation rather than a jointly tested model.

The chronology foundations, memory theory, eye application, spatial statistics, synthesis is therefore reasonable. Reordering place fields ahead of memory could also work but offers no necessary prerequisite improvement. The guide's explicit branch route already lets spatial readers skip the full readout branch.

## Both Part openings

The Part openings exist as chapter-plan purpose text and in `PEDAGOGY_REVIEW_PART_01.md` and `PART_02.md`; the paragraph packet has no Part-opening objects. They are reviewed here separately.

Part1, part:MECHANISMS: “A stable population pattern can retain a continuous value while fluctuations move that value...” states the actual stable-shape versus changing-coordinate problem. Its second sentence orders background, surviving-motion calculation and information/readout limits, matching chapters1–3. Retain both sentences. They preview a relation and route without asking readers to use an untaught theorem.

Part2, part:OBSERVATIONS: its motor-pathway versus spatial-tuning distinction separates the two studies rather than inventing a direct dynamical claim about static maps. The final sentence gives synthesis a concrete job, explaining connections while keeping maps distinct from a maintenance mechanism. Retain. The opening gives a reason for the adjacent eye and place chapters even though one is not a prerequisite of the other.

Root confirmed the current Publisher generates the actual landing page from description/Part/chapter metadata and does not emit the old starter `content/index.md`. The unused starter source has now been replaced with an actual topic introduction and reading-path instructions; I read those current two paragraphs and retain their purpose and baseline. Root's generated-index/rendering check remains separate. Removing footnote-call markers from metadata purpose copies changes presentation, not body evidence, and should be verified in the output by root.

## P1/P1SI source-page disposition judgments

I compared the actual teaching with all26 P1/P1SI rows, using the primary source pages already independently read in stage1, with targeted rereads for the connected derivations. “Covered” means the guide teaches the consequential result, not that it copies every printed sentence. Equivalent derivations and the following intentional omissions are reasonable for the requested learning goal.

| Source page | Independent disposition judgment |
|---|---|
| P1-p01 | Accept consolidation: dynamics opening, spike setup and linearization teach the persistent-value problem; thermodynamic analogy, addresses and disclosures are not prerequisites. |
| P1-p02 | Accept: fixed states, general/symmetric D, FI, scaling and Fig1 interpretation have actual calculations. The main-Eq2 discrepancy is now explicit. |
| P1-p03 | Accept: scalar/matrix bounds, extension scope and Fig2 are taught. Source converse is qualified by the actual linear-family counterexample, stronger than the older ledger's isolated-state wording. |
| P1-p04 | Accept: width scaling, ideal/naive observation, figure rescaling and printed-bound algebra have explanatory locations. Total-error use remains conditional on U1. |
| P1-p05 | Accept discussion consolidation: jump/noise model, correlated-noise limits, sensory/internal matching and leak distinction are taught; broader regulatory/chaotic-system conjectures are not needed. |
| P1-p06 | Accept intentional consolidation: large-population scaling, two-cell calculation and simulation roles remain. Runtime, kernel constants and integrator steps are reasonably omitted because full reproduction is not requested. |
| P1SI-p01 | Accept: n-replication and inverse weight scaling are explained, not only cited; contents/title require no teaching. |
| P1SI-p02 | Accept: n/n mean and n/n-squared variance derivation supply the Gaussian aggregate limit; repeating the equivalent g-variable system is unnecessary. |
| P1SI-p03 | Accept: Taylor K,u,v,normalization and projected covariance are derived in reading order. |
| P1SI-p04 | Accept: symmetric extractor proof and noise-induced mean-drift limit are both taught. |
| P1SI-p05 | Accept: convention distinction, drift/noise order and multicoordinate covariance have meanings and equations. |
| P1SI-p06 | Accept consolidation: conjugate vectors plus general tensor and matrix-bound proof determine the multidimensional result; a second expanded symmetric-tensor algebra is unnecessary. |
| P1SI-p07 | Accept: density equation is now derived, and exact wrapped Gaussian explained. Omitting optional Jacobi-theta/von-Mises notation reduces extra prerequisites without losing the result. |
| P1SI-p08 | Accept: uniform angular error, variable-D moment proof and D D'' correction are explicit. |
| P1SI-p09 | Accept: excitation family and direct D resolve the printed factor discrepancy; FI is subsequently derived from likelihood. |
| P1SI-p10 | Accept: guide explains the S1 variance slope and FI/matrix setup; simulation trial count and finite-sampling deviations need not become another empirical claim. |
| P1SI-p11 | Accept with source qualification: Cauchy Schwarz replaces the longer signed-ratio proof, and the unrestricted exponential converse is not repeated. |
| P1SI-p12 | Matrix-bound coverage accepted. Readout decomposition coverage remains pending U1's missing zero-cross-term reasoning. |
| P1SI-p13 | Accept Gaussian observation scope and equivalent backward recursion; variance addition supplies the marginalization meaning without reproducing the trajectory matrix. |
| P1SI-p14 | Accept equivalent derivation: likelihood compression, transition uncertainty, precision addition, limit ODE and separated solution reconstruct the ideal curve. The operator sign issue is not used as a premise. |
| P1SI-p15 | Accept: coth limit and naive covariance double integral are fully connected to their assumptions. |
| P1SI-p16 | Accept: optimum ratio, thinning, alpha scaling, example and S2 reading are present. Total-error interpretation depends on U1. |
| P1SI-p17 | Accept: integrator accuracy versus leak and the two-stage model/matrix are explained. |
| P1SI-p18 | Accept equivalent block-equation derivation of the left vector and tau+tau_m; swapped-time auxiliary variables need not be duplicated. |
| P1SI-p19 | Accept: explicitq likelihood/projection comparison teaches the Gaussian extension while keeping normalization visible. References are consolidated. |
| P1SI-p20 | Accept intentional omission of bibliography continuation; no new mathematical result occurs here. |

No inaccessible P1 source hold remains. The source map's equality wording at P1-p03/P1SI-p11 should be refreshed when root updates dispositions, to describe the actual counterexample and sufficiency condition rather than the old continuous-range claim. This is an evidence-record update, not a demand to restore an incorrect source converse.

## Record binding check

My local subset append/read code initially used a default Windows encoding on later reads, corrupting Unicode in copied original objects. I initially attributed this to the shared packet, which root correctly checked as clean. I corrected the local layer with explicit UTF-8, copied the original packet objects again by unchanged ID, and retained the actual individual judgments. At 20:08:40.8829350 every one of the288 final subset objects matched its actual source paragraph after the packet's normal list-marker removal. The shared packet was not modified. This was a local record-handling error, not a source or teaching defect.

Stage3 remains open for U1 and the subsequent current-source recheck. No other substantive understanding/flow repair was found in this scope. Output rendering and other reviewers' full bodies are not accepted by this record.

Root saved the U1 repair at20:08:42, after the original paragraph decisions and20:08:40 source-text verification. This original report retains its open finding; the reviewed03 bytes are preserved at `verification/reviews/source-snapshots/before-final-derivation-repairs/03-memory-information.md` and bound in the JSON. A separate focused call must assess the repair. Root also reports blank-line-only footnote formatting changes; those do not change this original semantic verdict.

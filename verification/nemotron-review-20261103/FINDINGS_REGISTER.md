# Nemotron review: original findings and recommendations

These are the model's final-answer fields, not accepted edits. See REVIEW.md for the coordinator's checks and priorities. Original answers, including later-corrected claims, remain unchanged.

## Stage 1

Overall assessment: the guide is scientifically careful. I read all 24 reader units (reading guide; chapters 1-21; glossary; references) and the extracted texts of the three main papers plus supplements/peer review. Every equation I checked against the sources (Burak & Fiete 2012 Eqs. 7-9 and SI S7-S95; Ben-Shushan et al. 2022 Eqs. 1-35; Mainali et al. 2025 Eqs. 1-10 and STAR Methods) matches the guide, including units, symbol meanings, and the local/vs-global qualifications. The guide correctly distinguishes its own derivations from quoted results and explicitly flags source inconsistencies that it verified algebraically: printed main Eq. 2 missing the square on d bar g_i/d theta (confirmed vs SI S18 and the 2017 correction), SI S40 vs S41/projection factor-of-two for mutual excitation (direct projection D = theta/(4 tau) matches S41), SI S71 plus-sign vs cosh solution S73, and Mainali supplement S23 (missing sqrt2) and S25 (sign). No confirmed error in the guide's own derivations was found. Remaining limits: several background/hardware source bodies were not locally available (Cannon & Robinson 1987 and Major et al. 2004 time-constant claims; Pehle 2022, Scholze 2026, LeGallo 2023, Massoud 2011, Giulioni 2012, Ortner 2025, Wang 2026, Ilmberger 2025), and PDF equation extraction is scrambled in a few places (Burak & Fiete SI S85 block sign; Mainali supplement S18 print-vs-extraction), so a few guide-flagged source issues could not be pixel-reconfirmed. The hardware Part respects its stated 2026-10-30 snapshot and does not pretend to a current SOTA survey.

### Findings

#### F-01

**Kind:** unverified_claim

**Severity:** medium

**Guide location:** ch:PERSISTENCE, sec:PERSISTENCE-EYE-MECHANICS (guide/01b-persistence.md, L0043-L0045)

**Short excerpt:** Horizontal gaze then drifted back with a time constant of about 0.2 s, compared with more than 20 s before disruption in darkness.

**Claim or gap:** Cannon & Robinson (1987) specific time-constant claims used as motivation for neural persistence exceeding tissue mechanics.

**Source evidence:**

- source: Cannon, S. C., & Robinson, D. A. (1987), J. Neurophysiol. 57(5), 1383–1409; page or section: abstract, per guide footnote [^p-eye-integrator]; equation or figure: n/a; what it supports: reversible brainstem disruption and gaze-holding time constants before/after disruption

**Strongest retaining reading:** The numbers are background illustration, not a premise of the diffusion derivation; if inaccurate, only the motivational example is affected, not Chapters 3-6 results.

**Why it is still a problem:** I did not read Cannon & Robinson 1987 (no local body in the packet), so I cannot confirm 0.2 s vs >20 s; it remains an uncited-by-me factual anchor.

**Suggested action:** Verify against the paper's abstract/full text (or the peer-review file cited by the guide) and restate with explicit uncertainty or a softer qualifier if unverifiable.

**Confidence:** low (concerning my ability to confirm; the claim itself is plausible)

#### F-02

**Kind:** unverified_claim

**Severity:** low

**Guide location:** ch:PERSISTENCE, sec:PERSISTENCE-EYE-MECHANICS (guide/01b-persistence.md, L0045)

**Short excerpt:** Major et al. (2004) altered visual feedback in goldfish and trained their gaze holding toward drift or instability over tens of minutes to hours; normal feedback could reverse the change.

**Claim or gap:** Goldfish integrator plasticity timescale and reversibility details.

**Source evidence:**

- source: Major, G., et al. (2004), PNAS 101(20), 7739–7744; page or section: Figs. 2-4 and Discussion per guide footnote [^p-eye-plasticity]; equation or figure: n/a; what it supports: visual-feedback plasticity of gaze holding, reversibility, unresolved cellular rule

**Strongest retaining reading:** Used only to distinguish slow neural recalibration from immediate elastic/viscous mechanics; the exact timescale is not load-bearing.

**Why it is still a problem:** Not locally read; cannot confirm 'tens of minutes to hours' or reversal detail from the packet.

**Suggested action:** Check Major et al. (2004) if the timescale is to be asserted as fact; otherwise soften to 'over extended training periods'.

**Confidence:** medium

#### F-03

**Kind:** ambiguous_source

**Severity:** low

**Guide location:** ch:PLACE-SIZES, source-check block (guide/05b-place-sizes.md, around L0196-L0204)

**Short excerpt:** 'Equation S18 prints multiplication by mean size where the preceding moment formula requires division.'

**Claim or gap:** Alleged printed error in Mainali supplement Eq. S18.

**Source evidence:**

- source: Mainali et al. (2025) supplement, Methods S3-S4; page or section: supplement pp. 12-14, Eq. S18; equation or figure: Eq. S18: beta = [Gamma(D/2+1)/<s>]^{2/D}; what it supports: beta from mean field size

**Strongest retaining reading:** The extracted supplement text shows division, which matches the guide's own formula; the alleged print error is not visible in extraction and may be an extraction/print difference.

**Why it is still a problem:** Without re-reading the PDF pages I cannot confirm whether S18 truly differs from the guide; low stakes because the guide derives beta independently and explicitly says code/fits are not implicated.

**Suggested action:** Re-read the Mainali supplement PDF pp. 12-14 (Eqs. S18, S22-S25) to convert each flag to confirmed print error, extraction artifact, or no issue.

**Confidence:** medium

#### F-04

**Kind:** ambiguous_source

**Severity:** low

**Guide location:** ch:MEMORY-READOUT, footnote [^p1-two-times] (guide/03b-memory-readout.md, L0422)

**Short excerpt:** 'Its rate decay block is negative, as required by that differential equation, despite the positive sign printed in the corresponding block of S85.'

**Claim or gap:** Alleged sign error in Burak & Fiete SI Eq. S85 rate-decay block.

**Source evidence:**

- source: Burak & Fiete (2012) SI; page or section: pp. 17-18, Eq. S85; equation or figure: Eq. S85 two-time-constant linearized matrix; what it supports: sign of the -1/tau_m rate-decay block

**Strongest retaining reading:** Stability requires a negative rate-decay block (-1/tau_m); the guide's reading is physically sensible and consistent with the main text's two-time-constant result.

**Why it is still a problem:** The extracted S85 matrix is garbled ('tau −1 m delta_ij'), so I cannot confirm whether the print has a sign error or the text is scrambled. Not a guide defect unless confirmed.

**Suggested action:** Re-read SI pp. 17-18 from the PDF to check S85 block signs.

**Confidence:** medium

#### F-05

**Kind:** source_access_limit

**Severity:** medium

**Guide location:** ch:HARDWARE-MEMORY, ch:HARDWARE-DYNAMICS, ch:NEUROMORPHIC-SYSTEMS (guide/07-, 08-, 09-hardware-*.md)

**Short excerpt:** Claims about Pehle 2022 (6-bit SRAM weights, ~1000x acceleration), Scholze 2026, LeGallo 2023, Massoud 2011 (32 bumps, 11.25°), Giulioni 2012, Ortner 2025, Wang 2026, Ilmberger 2025.

**Claim or gap:** Hardware-specific parameter and performance claims whose primary bodies are not in the local packet.

**Source evidence:**

- source: Hardware source access index; page or section: hardware entries with local_files: []; equation or figure: n/a; what it supports: Pehle, Scholze, LeGallo, Massoud, Giulioni, Ortner, Wang, Ilmberger bodies are web/primary only

**Strongest retaining reading:** The guide treats Part III as a 2026-10-30 snapshot of selected studies, labels preprints and post-layout-simulation-not-fabricated-chip, and separates architecture description from performance claims; the hardware numbers are descriptive context, not load-bearing for the neural-core results. The four hardware sources I did read locally (von Neumann 1958 pp.76-82; Aitsam 2026; Kleyko 2025; Sun 2026 PMC) match the guide's characterizations.

**Why it is still a problem:** I cannot independently confirm hardware-specific numbers; review emphasis remains the three neuroscience papers.

**Suggested action:** If the reader will rely on specific hardware figures, WebFetch the primary URLs (DOIs/arXiv) listed in the access index and re-check; otherwise keep the current hedged wording.

**Confidence:** high (about the access limit); not assessed (about truth of unread claims)

### Remaining checks

- Re-read Burak & Fiete SI pp. 17-18 (Eq. S85 matrix block signs) and Mainali supplement pp. 12-14 (Eqs. S18, S22-S25) from the PDFs to convert ambiguous flags into confirmed print errors, extraction artifacts, or non-issues.
- If the background time-constant claims are to be asserted as fact, verify Cannon & Robinson (1987) (0.2 s vs >20 s) and Major et al. (2004) (training timescale/reversibility) from primary sources; otherwise soften wording.
- Optionally WebFetch the primary hardware URLs for Pehle 2022, Scholze 2026, LeGallo 2023, Massoud 2011, Giulioni 2012, Ortner 2025, Wang 2026, Ilmberger 2025 if Part III hardware numbers are to be relied on; otherwise retain current hedged treatment.
- No new code execution, simulations, or pixel audits are within this review's scope; these remain explicit limits.

## Stage 2

Stage 2 (necessity, terminology, missing explanatory steps): I inspected the full inline frozen packet (guide plus extracted source texts; no Read/WebFetch/WebSearch calls were actually made, correcting my Stage 1 source-access wording accordingly). The guide's main teaching path is generally sound: each chapter opens with a physical question, identifies actors and quantities, introduces symbols before dependent use, and connects formulas to measurable quantities. Folds are correctly used for expansions; main-path results remain visible. No new confirmed scientific errors emerged from this teaching pass. The main issues are minor terminology/symbol overloading (b across Chapters 2-3; 'state' across Parts; simulation readout proxy vs theory coordinate introduced late) and the acronym/claim load in the Parts III-IV extensions, which are explicitly requested and appropriately hedged. All Stage 1 findings F-01..F-05 remain open source-access/confirmation limits, not established guide errors.

### Findings

#### N-01

**Kind:** terminology

**Severity:** low

**Guide location:** guide/01b-persistence.md sec:FOUNDATIONS-ATTRACTOR L0068; guide/02-memory-dynamics.md sec:MEMORY-SYMMETRIC L0272-L0279

**Short excerpt:** "Let b=40 spikes per second" (ch2) vs "equal biases b" (ch3); conversion given at L0279

**Missing or unclear meaning:** Same symbol b denotes two different quantities with different units (rate baseline in spikes/s vs activation bias in activation units). The conversion exists but is easy to miss when reading across chapters.

**Earlier teaching checked:** ch2 two-cell example (L0068-L0081); ch3 symmetric mutual-inhibition example (L0272-L0283) and its footnote p1-two on activation vs rate units

**Reader consequence:** A reader may carry the wrong value or units of b between Chapters 2 and 3 and miscompute D=b/(2tau) or the two-cell rates.

**Suggested action:** Add a short unit-qualifying parenthetical at the first use of b in each chapter (e.g., "b here is a rate baseline" vs "b here is an activation bias"); keep the existing conversion line.

**Essential or optional:** optional

**Confidence:** high

#### N-02

**Kind:** missing_explanatory_step

**Severity:** low

**Guide location:** guide/01-foundations.md sec:FOUNDATIONS-SIMULATION L0294; guide/11-simulating-memory.md sec:SIMULATING-MEMORY-RING L0032

**Short excerpt:** "the ring's angle is read from the preferred angle of the neuron with the highest instantaneous rate"

**Missing or unclear meaning:** Chapter 1 presents the maximum-instantaneous-rate readout as the ring's angle without noting it is a numerical proxy distinct from the theoretical coordinate theta defined by the noise-free return flow in Chapter 3.

**Earlier teaching checked:** ch3 instantaneous attractor state via return flow (L0011); ch11 explicit distinction "numerical proxy... The theoretical coordinate theta is assigned by following noise-free relaxation... the largest-rate rule does not carry out that projection" (L0032)

**Reader consequence:** A reader may believe the simulation directly measures the theory's theta, conflating a decoder proxy with the model coordinate.

**Suggested action:** Add one clause in ch1 at L0294 cross-referencing ch3's return-flow coordinate and labeling the max-rate rule a numerical proxy (ch11 already clarifies this).

**Essential or optional:** optional

**Confidence:** medium

#### N-03

**Kind:** terminology

**Severity:** low

**Guide location:** book-level; glossary sec:GLOSSARY L0110; ch:MEMORY-DYNAMICS L0009; ch:HARDWARE-MEMORY L0009-L0011

**Short excerpt:** "state" used for neural activity vector, represented memory coordinate, and hardware neuron variable

**Missing or unclear meaning:** The familiar word "state" shifts referent across chapters (s vector / theta coordinate / artificial-neuron variable) without a cross-chapter reminder of which referent is active.

**Earlier teaching checked:** ch3 distinguishes physical network state s and memory coordinate theta (L0009); ch7 separates weights, neuron/synapse states, and remembered angle (L0009-L0011); glossary gives a general state definition (L0110)

**Reader consequence:** Possible conflation of activity state with represented value, especially when moving between Parts I and III.

**Suggested action:** Add a one-sentence local reminder at chapter openings where the referent shifts ("In this chapter, state means ..."); the glossary definition already covers the general idea.

**Essential or optional:** optional

**Confidence:** medium

#### N-04

**Kind:** missing_explanatory_step

**Severity:** low

**Guide location:** guide/09-neuromorphic-systems.md sec:NEUROMORPHIC-SYSTEMS-ARCHITECTURES and sec:NEUROMORPHIC-SYSTEMS-ADVANCES

**Short excerpt:** Five hardware studies (Kleyko, Aitsam, Ortner, Wang, Sun) plus architectures in quick succession

**Missing or unclear meaning:** No compact map from each cited study to (a) what physical quantity persists, (b) substrate, and (c) claim strength; acronym load (Loihi 2, SpiNNaker2, BrainScaleS-2, PCM, Hala Point, CrTe3, LMU).

**Earlier teaching checked:** tbl:NEUROMORPHIC-ARCHITECTURES (weights/state/update/consequence per system); tbl:HARDWARE-STORAGE (implementation/quantity/role/error)

**Reader consequence:** Difficulty comparing the studies or applying the Chapter 17 test ideas to a specific machine.

**Suggested action:** Add a short Part III opening map (one sentence or small table): study -> persistent quantity -> substrate -> claim type (measured chip / post-layout simulation / proposed). Keep existing per-study caveats.

**Essential or optional:** optional

**Confidence:** medium

### Useful additions

#### A-01

**Topic:** local 'state' referent reminder

**Placement:** chapter openings of ch:MEMORY-DYNAMICS, ch:HARDWARE-MEMORY, ch:SIMULATING-MEMORY

**Reader question:** What does 'state' denote in this chapter's equations?

**Why it helps:** Prevents conflating the neural activity state with the represented memory value or a hardware variable when crossing Parts.

**Minimum sufficient treatment:** One clause at each opening: "In this chapter, state means ...".

**Source support needed:** None; guide-derived clarification using existing definitions.

**Priority:** medium

#### A-02

**Topic:** Part III quick-read map

**Placement:** Part III introduction (guide/part-hardware) or ch:NEUROMORPHIC-SYSTEMS opening

**Reader question:** Which machine stores what, and how strong is each claim?

**Why it helps:** Reduces acronym/case load across six hardware studies and makes the measured-vs-proposed distinction scannable.

**Minimum sufficient treatment:** Short table or sentence per study: persistent quantity, substrate, claim type (measured chip / post-layout simulation / proposed hardware). Reorganize existing facts only.

**Source support needed:** Existing chapter facts already state these; no new source needed.

**Priority:** medium

#### A-03

**Topic:** simulation readout proxy vs theory coordinate

**Placement:** guide/01-foundations.md sec:FOUNDATIONS-SIMULATION near L0294

**Reader question:** Does the simulation measure the same theta as the theory?

**Why it helps:** Avoids conflating the max-rate-neuron decoder proxy with the return-flow theoretical coordinate defined in Chapter 3.

**Minimum sufficient treatment:** One sentence plus cross-reference to ch:MEMORY-DYNAMICS instantaneous-attractor-state definition.

**Source support needed:** ch3 L0011; ch11 L0032 (already in guide).

**Priority:** medium

#### A-04

**Topic:** disambiguate 'input' senses

**Placement:** guide/01-foundations.md sec:MEMORY-SPIKES near Eqs.8-9 (L0080-L0090)

**Reader question:** Which 'input' is being discussed: recurrent input g_i, constant bias b_i, or an external cue?

**Why it helps:** 'Input' is reused across synaptic drive, bias, and later cue/stimulus; a brief label prevents misassignment.

**Minimum sufficient treatment:** Parenthetical tags: "recurrent input g_i", "constant bias input b_i".

**Source support needed:** None; the distinction is already stated, just not tagged.

**Priority:** low

### Remaining checks

- No pixel/figure audit performed (not requested).
- No code or simulations executed; no original animal recordings reprocessed.
- Hardware primary bodies for Pehle 2022, Scholze 2026, LeGallo 2023, Massoud 2011, Giulioni 2012, Ortner 2025, Wang 2026, Ilmberger 2025 remain locally unread; only DOIs/URLs in the access index.
- Cannon & Robinson 1987, Major et al. 2004, Dragoi 2026 not locally read.
- No WebFetch/WebSearch performed; all content is the inline frozen packet.
- The guide's negative claim that no public Burak & Fiete simulation-code archive exists is a search statement as of 2026-10-30, not proof of absence.

## Stage 3

The guide's structure is coherent and matches its stated purpose: mechanism → mathematical derivation → interpretation for memory (Part I), recordings-first eye work and model-first place work (Part II), physical-state separation in hardware (Part III), and methods/reproduction (Part IV). All 24 units (21 chapters + reading guide + glossary + references) were inspected inline. No essential structural gap was found: each chapter opens with a physical question, identifies actors and quantities, introduces symbols before dependent use, and keeps expansions in folds. Main refinements are terminology (symbol b overloaded as rate baseline in Ch 2 vs activation bias in Ch 3; 'state' referent shifts across Parts), one cheap cross-reference (simulation readout proxy in Ch 1 ↔ return-flow coordinate in Ch 3), an optional folded running example across Ch 2-6, and a Part III quick-read map. Stage 1 source flags F-03/F-04 are now confirmed as genuine printed-source inconsistencies correctly flagged by the guide (not guide errors); F-01/F-02 are supported by primary abstracts (no guide error); F-05 remains an unread-hardware access limit. Open connected reading assessment: a reader entering at Chapter 1 can trace spikes → synaptic activation → rate code → Poisson uncertainty → attractor geometry → diffusion → information bound → readout, with cross-references at each step; branching into eye (Ch 7-9) and place (Ch 10-12) paths is explicitly contrasted; Part III and IV remain explicitly dated, hedged extensions. The only weak links in the connected path are symbol continuity (b, state) across chapter boundaries, addressed by the clarifications below.

### Structural recommendations

#### R-01

**Priority:** medium

**Current location:** Chapters 2-6 (each uses a different illustrative model: two-cell rate model, mutual-inhibition activation model, etc.)

**Proposal:** Add one folded running example (e.g., the mutual-inhibition pair) carried across Ch 2-6: encoding an angle, storage, diffusion, information bound, readout—so D, J, tau, v stay tied to a single concrete circuit.

**Teaching benefit:** Reduces symbol whiplash between chapters' illustrative models and makes the mechanism→math→interpretation chain concretely traceable.

**Prerequisite evidence:** Existing two-cell examples at Ch 2 L0068-L0102 and Ch 3 L0272-L0283 already establish the geometry; only continuity needs adding.

**Cost or risk:** Low; folded so skippable; risk of length mitigated by keeping it one compact block per chapter.

**Affected chapters:**

- ch:PERSISTENCE
- ch:MEMORY-DYNAMICS
- ch:MEMORY-INFORMATION
- ch:MEMORY-READOUT

#### R-02

**Priority:** medium

**Current location:** Part III introduction and Ch 16 opening

**Proposal:** Add a compact quick-read map: one row per hardware study (Pehle 2022, Scholze 2026, LeGallo 2023, Massoud 2011, Giulioni 2012, Ortner 2025, Wang 2026, Sun 2026) with columns: persistent quantity, substrate, claim type (measured chip / post-layout simulation / proposed hardware).

**Teaching benefit:** Makes the measured-vs-proposed distinction scannable across six studies and reduces acronym/case load in this requested extension.

**Prerequisite evidence:** Facts already stated per study in Ch 14-16; only reorganization into a map.

**Cost or risk:** Low; small table. New factual verification of unread bodies remains a proposal (F-05), not a change.

**Affected chapters:**

- part:HARDWARE
- ch:NEUROMORPHIC-SYSTEMS

### Clarifications and additions

#### C-01

**Priority:** low

**Placement:** guide/01b-persistence.md sec:FOUNDATIONS-ATTRACTOR L0068 and guide/02-memory-dynamics.md sec:MEMORY-SYMMETRIC L0272

**Proposal:** Add unit-qualifying parentheticals at first use of b: "b here is a rate baseline in spikes/s" (Ch 2) vs "b here is an activation bias in activation units" (Ch 3); keep existing conversion line at L0279.

**Reason:** Same symbol b denotes two quantities with different units; conversion exists but is easy to miss across chapters.

**Source requirement:** None; guide-derived terminology fix using existing definitions.

#### C-02

**Priority:** low

**Placement:** Openings of ch:MEMORY-DYNAMICS L0009, ch:HARDWARE-MEMORY L0009-L0011, ch:SIMULATING-MEMORY L0009

**Proposal:** Add one clause: "In this chapter, state means ..." (neural activity vector / represented coordinate / hardware neuron variable, as applicable).

**Reason:** The familiar word state shifts referent across Parts; glossary definition alone does not bind the local referent.

**Source requirement:** None; uses existing glossary definition L0110.

#### C-03

**Priority:** low

**Placement:** guide/01-foundations.md sec:FOUNDATIONS-SIMULATION near L0294

**Proposal:** Add one sentence labeling the max-instantaneous-rate rule as a numerical proxy for the represented angle, cross-referencing Ch 3's return-flow instantaneous attractor state (L0011).

**Reason:** Ch 11 already clarifies this; an early cross-reference prevents conflation of decoder proxy with theory coordinate.

**Source requirement:** None; ch:MEMORY-DYNAMICS L0011 and ch:SIMULATING-MEMORY L0032 already in guide.

#### C-04

**Priority:** low

**Placement:** guide/01-foundations.md sec:MEMORY-SPIKES near Eqs. 8-9 L0080-L0090

**Proposal:** Parenthetical tags: "recurrent input g_i", "constant bias input b_i", "external cue input" where each is introduced.

**Reason:** 'Input' is reused across synaptic drive, bias, and later cue/stimulus; tags prevent misassignment.

**Source requirement:** None; distinction already stated, untagged.

#### C-05

**Priority:** optional

**Placement:** Part III (ch:HARDWARE-MEMORY through ch:HARDWARE-TESTS)

**Proposal:** If specific hardware performance figures are to be relied on, WebFetch the primary bodies named in F-05 (Pehle 2022 DOI, Scholze 2026 arXiv, LeGallo 2023 DOI, Massoud 2011 DOI, Giulioni 2022 DOI, Ortner 2025 DOI, Wang 2026 DOI, Ilmberger 2025 arXiv) and re-check; otherwise keep current hedged wording.

**Reason:** Eight hardware entries have no local bodies; truth of hardware-specific claims remains unassessed by this review.

**Source requirement:** Primary sources named; proposal only until checked.

### Reconsidered findings

#### F-01

**Disposition:** confirmed not a guide error; source verified

**Evidence:** Coordinator source check: Cannon & Robinson 1987 J Neurophysiol 57(5), abstract—reversible brainstem disruption; intact time constant above 20 s in darkness; post-injection minimum horizontal time constant 200 ms. DOI 10.1152/jn.1987.57.5.1383.

**Reason:** Claim used only as motivational background in Ch 2 (folded spring-damper is a teaching reconstruction); no change needed.

#### F-02

**Disposition:** confirmed not a guide error; source verified

**Evidence:** Coordinator source check: Major et al. 2004 PNAS 101(20), abstract and Fig. 4 caption—tens of minutes to hours retuning under normal feedback; 80-minute training intervals. DOI 10.1073/pnas.0401970101.

**Reason:** Used only to distinguish slow neural recalibration from immediate tissue mechanics; no change needed.

#### F-03

**Disposition:** source print flag confirmed; no guide error

**Evidence:** Read of mainali-2025-supplement.pdf printed p.12/PDF p.13: Eq. S18 prints beta = [Gamma(D/2+1)〈s〉]^{2/D} (multiplication by mean size), while the preceding moment relation 〈s〉 = Gamma(D/2+1) beta^{-D/2} requires division: beta = [Gamma(D/2+1)/〈s〉]^{2/D}. Source sha256 05af1fdf...

**Reason:** Guide already flags S18 and derives beta independently; code/fits explicitly unimplicated. No guide change needed.

#### F-04

**Disposition:** source sign flag confirmed; no guide error

**Evidence:** Read of burak-fiete-2012-persistent-activity-si.pdf printed p.17: Eq. S85 lower-right block prints positive tau_m^{-1} delta_ij, while S84 (rdot_i + tau_m^{-1} r_i = ...) implies a negative rate-decay block. Source sha256 9bbff1fb...

**Reason:** Guide footnote [^p1-two-times] already flags the print sign and derives the negative block independently (Ch 6 extensions matrix A). No guide change needed.

#### F-05

**Disposition:** retained as unread-source access limit

**Evidence:** SOURCE_ACCESS.json: eight hardware entries (HW-Pehle2022, HW-Scholze2026, HW-LeGallo2023, HW-Massoud2011, HW-Giulioni2012, HW-Ortner2025, HW-Wang2026, HW-Ilmberger2025) have empty local bodies; only DOI/arXiv URLs.

**Reason:** No hardware-claim verdict possible; guide treats Part III as a 2026-10-30 snapshot and does not overclaim. C-05 names the primary sources for any future check.

### Top actions in order

#### 1

**Kind:** source-flag retention

**Finding ids:**

- F-03
- F-04

**Action:** Keep the F-03/F-04 source-print flags unchanged; they are correct and now source-confirmed via Read of the two supplied PDF pages.

**Why first:** Derived constants in Ch 3 (Eq. 2 square) and Ch 4/11 (mutual-excitation D factor-of-two; size-law beta) depend on these sources; the flags prevent misattributing print issues to the guide.

#### 2

**Kind:** structural addition

**Action:** Add the folded running example across Ch 2-6 (R-01).

**Why first:** Largest teaching benefit for symbol continuity through the core memory chain; low cost because folded.

#### 3

**Kind:** structural addition

**Action:** Add the Part III hardware quick-read map (R-02).

**Why first:** Reduces acronym/case load in the explicitly requested hardware extension.

#### 4

**Kind:** terminology clarification

**Action:** Apply C-01 (b units), C-02 (state reminders), C-03 (readout proxy cross-ref), C-04 (input tags).

**Why first:** Cheap, localized fixes that prevent reader misassignment across chapter boundaries; no science content changes.

### Coverage and limits

Actually inspected: all 24 guide units inline in the frozen packet; full extracted texts of Burak & Fiete 2012 main+SI, Ben-Shushan 2022 main+supplement-1, Mainali 2025 main+supplement; Read of two supplied PDF-page renderings (Mainali supplement p.13 Eq. S18; Burak & Fiete SI p.17 Eq. S85) confirming F-03/F-04 as source print issues; hardware sources von Neumann 1958 pp.76-82, Seung 1996, Aitsam 2026, Kleyko 2025, Sun 2026 read locally, other hardware bodies unread (F-05). Not done: no Read/WebFetch/WebSearch calls were made in Stage 1 or Stage 2—all guide/source content was supplied inline; prior statements of 'reading' files refer to the inline packet. No code execution, no simulations, no original animal-recording reprocessing, no pixel/figure audit. Guide's negative claim of no public Burak & Fiete simulation archive is a search statement as of 2026-10-30, not proof of absence.

### What to keep

- Mechanism → mathematical derivation → interpretation structure (sec:READING-MECHANISM-MATH) applied consistently in Ch 3-6, preserving premises.
- Front-matter symbol disambiguation (D, d, theta, q, C) before colliding chapters.
- Poisson counts, CV, Fano factor taught before diffusion, with the qualification that independent count draws do not make recurrent spike trains independent.
- Left/right zero-eigenvector projection, information-diffusion bound with equality condition, and the linear-family counterexample narrowing the source's 'iff' exponential claim.
- Readout naive vs ideal coth formula, partial-access alpha scaling, and the concrete counterexample to printed Eq. 6 as a universal lower bound.
- Place-field exact Kac-Rice vs high-threshold approximations, Euler-characteristic boundary terms, slice-dimension logic, and processing/selection limits.
- Simulation/methods honesty: no reruns claimed, code/data gaps labeled, sigma vs ell conversion explicit.
- Hardware Part explicit 2026-10-30 snapshot, preprint/post-layout labeling, no SOTA-overclaim.
- Contribution labels and folds used consistently; glossary/references internally consistent.


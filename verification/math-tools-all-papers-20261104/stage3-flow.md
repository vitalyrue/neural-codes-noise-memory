# Stage 3: connected reading and first-use order

Started UTC: 2026-11-04T14:33:52Z
Finished UTC: 2026-11-04T14:35:58.282496+00:00
Wall-clock elapsed: 126 seconds.
Awake execution time: unverified; Windows sleep/resume events were not checked.
Token stats unavailable.

Method: read the full expanded mathematical-tools chapter, following its visible argument with example folds treated as optional, then read the reading-guide route and glossary support and the new backlinks and symbol translations in the six requested later chapters. This is a connected-reader review of the new material and handoffs, not a full-book semantic audit, source re-review, figure review or rendered-layout review. Stage 2 repair acceptance was recorded separately in recheck-stage2.md before this pass. No guide edits or builds.

Verdict: one short main-text link is still required. The overall chapter order works for a physics/CS reader with the stated probability background and no neuroscience statistics background. The reader can otherwise follow what acts on what, distinguish model choices from consequences, and retain the exact-versus-limit boundaries with folds closed.

## Required finding

CROSSINGS-PEAKS, the paragraph beginning “This geometry predicts three different limiting size laws”: the visible previous paragraph establishes only size proportional to epsilon^(d/2). A probability distribution for epsilon is also necessary to obtain a size distribution. At present that second ingredient appears only in the optional example: U=q epsilon approaches a unit-mean exponential distribution. A reader leaving the example closed is asked to jump from geometry to Rayleigh/exponential/2/3 survival laws without this ingredient.

Add one short sentence to the visible text, for example: “At high thresholds, the scaled peak excess q epsilon approaches an exponential distribution of mean one. Combining that height distribution with the radius-to-size relation gives the following laws.” Keep the proof and variable transformation folded. This is a missing causal step in the visible argument, not an objection to the mathematical result or a demand to unfold the calculation.

## Paragraph-specific retentions

Reading guide before tools: the reader is told what neurons, fixational drift and place fields are before being routed to the mathematics. The three papers are distinguished as a memory-model bound, evidence about a shared eye-movement source, and a spatial statistical model. The new prerequisite sentence and before-Part-I route correctly advertise all three papers. The place-field short route can skip detailed memory readout and eye mechanics. No external neuroscience knowledge is needed to understand why the tools are being introduced.

Tools introduction: the three physical questions give the seven sections a common purpose without pretending they form one proof. The author/year reading paths map tools to later chapters. The assumed probability background is explicit. The promise of physical meanings and conclusions in the main text is suitable; the required finding above is the one remaining place where a crucial link sits only in an optional fold.

WEIGHTS, first four paragraphs and feedback list: an emitted spike changes a decaying activation; W maps that activation into a receiving cell's input; phi maps input to rate; later spikes feed back. These assignments establish what acts on what before the mutual-inhibition example. The positive/negative sign discussion and the need for tuned balance explain why persistence is a circuit property rather than an automatic effect of feedback. The optional two-unit calculation supports the main mechanism and can be skipped. The final fixed-weights statement distinguishes storage activity from learning. This is a sufficient neural setup for a reader coming from physics or CS.

FISHER, angle comparison through count formula: the nearby-angle question precedes the formal statistic. Tuning slope, count noise, observation duration and the represented value have different explicit roles. The Poisson mean/variance assertion gives the needed model without requiring prior neural statistics. The rate J and its time/angle units are explained before the memory bound. The closed numerical example provides a check, while the visible numerator/denominator explanation carries the meaning. Local versus distant ambiguity and independent versus shared spike fluctuations stay visible.

BOUND, benchmark through transition: the chapter separates a fixed-value estimation benchmark from the moving memory state. It defines diffusion through variance growth before stating the dynamical inequality. The dimensions, weak-fluctuation assumption, tuned persistent family and conditionally independent Poisson generation are visible. It does not claim that the Cramer Rao inequality alone proves the memory bound. The final current-value versus initial-value distinction is the right bridge into eye recordings.

SHARED, opening through teaching model: the comparison is between a spike-based prediction and measured movement, both in degrees. Covariance and correlation meanings remain visible while generic formulas can stay folded. The gain assignments and private-component independence appear before the covariance-to-shared-fraction formula. The main sentence explicitly denies that correlation alone supplies the fraction, and explains how private noise in the predictor can lower correlation without reducing the common movement. The example is a useful optional numerical check, not the sole explanation. The closing application retains calibration and many-neuron qualifications and now defines N_m.

FILTERS, opening through contrasting inputs: the muscles' response motivates a causal filter. Input angle, output angle, impulse response and response time have explicit roles and units. The differential form explains why a mismatch drives velocity. White noise and a position command that accumulates independent changes are distinct inputs, so the plateau-versus-continuing-growth conclusion has a clear cause. Lag is separated from clock time. Stationary position is defined through its relevant moments; the diffusing position is expressly nonstationary while its increments settle. The optional covariance/MSD calculation now defines its Dirac delta and C_E symbols. The last paragraph protects the distinction between a first order illustration and the paper's two muscle times plus feedback. Smoothness of the path alone is not sold as evidence of diffusion.

RANDOM-FIELDS, opening and fixed-map statement: the track question marks a clear change from time-dependent signals to position-dependent maps. The reader is expressly told that revisiting a position evaluates the same draw. Spatial covariance is an average across possible maps, not a time covariance while the animal moves. Joint Gaussianity is explained immediately, without assuming that Gaussian marginals imply it. Stationarity does not make a sample map flat; isotropy removes a preferred direction and is a separate condition. The threshold normalization, rectification and connected-component rule define activity and fields before counting begins. Correlation length is a local derivative scale with distance units, not a promise of a unique covariance shape. The rewritten nonsingular-covariance condition is understandable from the assumed linear algebra.

CROSSINGS-PEAKS, upcrossings through endpoints: the active-set definition makes it clear why an upward crossing begins a component. The conditional slope factor is explained through the distance spent near threshold, so its appearance is more than a formula to memorize. Smooth stationary Gaussian assumptions are stated for the exact density. The optional narrow-band derivation supplies details without hiding the physical counting mechanism. The finite-track paragraph explains the left-endpoint term and the chosen treatment of clipped fields. The chapter does not imply that a crossing count alone determines field sizes.

CROSSINGS-PEAKS, high fields and laws: equal field weighting is explicit. High positive threshold, isolated peak geometry, radius versus excess and the effect of spatial dimension are introduced before the calculation. The visible Rayleigh definition uses survival probability, and corresponding area and volume laws are supplied with a warning that beta has dimension-dependent units and value. Exact counting and asymptotic size laws remain clearly separated. Add the one required visible exponential-excess sentence above to complete the mechanism. The lower-threshold multiplet/shape caveat then explains why the later finite-threshold check matters.

## Later handoffs and lookup

01-foundations: the weight and shared-signal backlinks identify earlier mechanisms while retaining local explanations of spike pulses and population averaging. Removing the blue Dirac marker did not remove the local statement that its pulse integrates to one.

03b-memory-readout: the white-noise backlink points to the convention, and its local spike equation still states the variance accumulated over dt. The earlier optional definition does not become a hidden prerequisite because this local explanation remains.

04-eye-drift: the filter backlink is followed by application to spikes. Its kernel units are degrees per spike, while the teaching angle-to-angle kernel has inverse-second units; each is explicitly supplied where used. The distinction between a statistical prediction and a command sent to muscles remains in the local material. Calibration and the full inference are still developed here.

04b-eye-timing: the introduction link carries the broad white-input-versus-accumulating-input distinction forward; the later chapter compares lag dependence with actual recordings. The simple example is not substituted for the full muscle and feedback model.

05-place-fields: sigma_0 to sigma_h and ell_c to sigma are translated before the local model and subsequent formulas. Spatial stationarity, isotropy, Gaussianity and derivative conditions are retained in the application. No concept needed to count fields is removed merely because its first blue definition moved earlier.

05b-place-sizes: the ell_c/sigma translation appears before the explicit curvature derivation. The later plain-text Rayleigh description remains after removal of the competing blue first-definition marker, and still connects square-root geometry to the exponential excess variable.

Glossary: the entries support lookup rather than supplying missing first explanations. The new correlation-length entry limits it to local covariance curvature, and the spatial covariance/random-field links point back to tools. Gaussian process, jointly Gaussian, isotropy, crossing and filter entries agree with the tools usage. The Rayleigh square-root-of-exponential lookup is consistent with its visible survival form. No glossary lookup is needed to understand the main new inference steps, apart from the required height-distribution link to be brought out of the fold.

## Optional polish only

- “A cell's displacement prediction” could be “a displacement prediction computed from one cell's spikes” to make the analyst's role explicit. The reading guide and later chapters already supply that interpretation, so this is not a remaining required repair.
- Expand MSD in parentheses on first use within the tools filter section. The reading guide already introduces the abbreviation and the tools text spells out the phrase, so this is small local polish.
- The old short link from the timing chapter's white-noise reminder to the readout chapter could link directly to tools. The existing two-hop route still works conceptually.

## Current input SHA-256 hashes

- `content/chapters/00-mathematical-tools.md`: `80e524760083c9bf17e08a380ea2e99ee674d505cb1c78a954ce0a52258b0d16`
- `content/chapters/00-mathematical-tools.yaml`: `4c1b26db2e689d88d99879488adaa88b824643d6723c83bc638e100c83c5f43b`
- `content/chapters/00-reading-guide.md`: `1f4ec259e7d690a4b1b177e922fa7492e25aae3fe8a31a3c3bb0863f57ae3407`
- `content/chapters/glossary.md`: `7b4103882ca7d03206885b50d096eb2c0b4bb36c2264950dc527ab47e0fc7047`
- `content/chapters/01-foundations.md`: `54569cc3a6a93bb9ea9a67be0f81a4bfc1b498d17bc533845167b8da4165539d`
- `content/chapters/03b-memory-readout.md`: `59959bd393fa36624773027c68f297886ce6f109abbde1d79118bc36539629c0`
- `content/chapters/04-eye-drift.md`: `2fbb5f1d55126fb952e44e9e8650fc7ddc00c7e8b5dcebab8e44182a7507dc05`
- `content/chapters/04b-eye-timing.md`: `15916da716dc5c8c64acbf9be65c837877c48674ac2c265a2b4737c9f7bdebfb`
- `content/chapters/05-place-fields.md`: `60dcdf27c11276c338bbd9f6974896905e5b0dac526237cc5d90bab057d2efdf`
- `content/chapters/05b-place-sizes.md`: `da845923ade9f098aa30ccf0e6a80e498c9992c0db729c07ad5321b05399385a`

Review timing note: the coordinator applied the single reported repair while this report was being written. The chapter hash above identifies the version read at Stage 3 start, also captured in recheck-stage2.md. The repaired current version is assessed separately in recheck-stage3.md. The original finding is preserved above.

# Memory-path terminology and prerequisite audit

Start: 2026-10-30T12:45:28.5991214+02:00. Reviewer: terms_memory subagent. Scope: reader text from the reading guide through memory readout, in the actual chapter order, plus all seven sidecars' visible captions and alt text and the glossary. This is a passage-based prerequisite review, not a book-wide acceptance review. No historical findings were read and no manuscript was edited.

Audience updated by the user during the review: undergraduate math is available; expected value, variance, standard deviation and probability density are already known and must not receive a basic statistics primer. Neuroscience and paper-specific statistical relationships still need plain explanation. Earlier proposals to explain those four basic terms are withdrawn. The source reading-guide baseline at 00-reading-guide.md:74 and 00-reading-guide.yaml:47-49 assumes basic probability. No glossary entry, preview or later definition is counted as adequate earlier teaching.
Reading order verified in plan/chapter-plan.yaml: reading guide, foundations, persistence, memory dynamics, long delays, memory information, memory readout. Subsequent eye and place chapters were outside this assignment. Locations below refer to the original baseline copy at verification/fisher-terms-20261030/baseline/content/chapters, so the coordinator's simultaneous Fisher information edit does not change these locations.

Rules read: course-study-guide-builder/SKILL.md, references/concept-prerequisites.md, and the relevant audience, first-dependent-use, plain-language, prerequisite and passage-review rules in references/pedagogy-language-contract.md. No Publisher concept index was created. The findings below come from reading the passages and checking their earlier path; no automated keyword result is treated as an omission.

## Findings that need repair

Severity meanings: high means a missing foundation blocks several later calculations for the supplied audience; medium means a local use precedes adequate teaching or a key explanatory link is missing. These are teaching findings, not claims that the displayed formulas are false.

### M1 and M2 withdrawn after the user's clarification

Expected value, variance, standard deviation and probability density are assumed knowledge. The original proposed elementary lessons are withdrawn. There is no need to add general expectation notation, a variance example or a density-area explanation.

Gaussian increments at 01b-persistence.md:102 and Gaussian likelihoods at 03b-memory-readout.md:19-32 are worth a short reminder only if Gaussian/normal distributions are also unfamiliar. An optional one-sentence reminder is enough: the local approximation uses bell-shaped errors described by their mean and variance. This is not filed as a confirmed missing paper-specific prerequisite under the updated audience, and is not a reason for a statistics chapter.

### M3. Conditional independence has adequate support; optional first-use reminder

**No confirmed substantive omission under the updated audience.**

- First example: 01-foundations.md:92 pools counts from cells that each have the same fixed rate. It immediately contrasts independent count fluctuations with a common input that changes several rates together.
- Further teaching: 01-foundations.md:109 explains that independence is conditional on the modeled state and that complete recurrent spike trains can still be correlated. The caption at 01-foundations.yaml:37 explicitly limits the condition to fixed modeled rates. 02-memory-dynamics.md:59-69 then gives conditional mean and covariance, and 02b-memory-long-delays.md:145 repeats the correct limitation.
- The strongest reasonable reading is sufficient: the fixed-rate premise supplies the condition needed for the pooled-count calculation, and the recurring-state caveat is taught before the later network and information derivations depend on it.
- Optional local improvement only: put the fixed-value/fixed-rate phrase directly before the word conditional at :92. Do not add an independence lesson or duplicate :109. The earlier report's medium-severity omission is withdrawn.
### M4. Fisher information's formal steps arrive without a worked statistical bridge

**Severity: high in the original section; coordinator is already repairing it.**

- Locations: 03-memory-information.md:21 defines likelihood, :31-40 forms log likelihood and score, :43-51 averages squared score to name Fisher information, and :54-70 invokes an unbiased estimator and the Cramer Rao bound.
- Earlier support checked: tuning curves and rate slope are taught at 01-foundations.md:24; Poisson counts at :51-109; the distinction between current coordinate and original memory at 02b-memory-long-delays.md:149-158. These need not be retaught from scratch. Those earlier mathematical and statistical basics are now treated as known, following the user clarification.
- What is missing: the reader needs to hold observed counts fixed while comparing proposed values, then reverse the viewpoint when averaging over all possible count samples at a fixed true value. Those two roles are implicit in the equations. A score definition alone does not teach why its average square measures local distinguishability or why inverse information has error units.
- Repair requirements for the replacement: use one short numerical count example before the general score formula; define parameter, observed sample and estimator by their jobs; distinguish likelihood over candidate values from probability of data and from a prior; show why a rate change must be judged relative to count variation; distinguish J from Jh and variance from standard deviation; preserve the locally constant-state approximation and the unbiased/regular-model limits of the error bound. The later information-diffusion proof at :94-129 already explains the vector geometry well and need not be replaced wholesale.

## Smaller explanatory link worth fixing if the passage is retained

**Itô versus Stratonovich, 02b-memory-long-delays.md:139.** Medium priority, separate from the high-priority statistical foundations. Itô is defined at :17, and :21-39 derives its density equation from the increment's first two moments. Stratonovich at :139 is defined by midpoint evaluation, and the conversion term bb'/2 is then given as a rule. The reader can substitute b=sqrt(2D) and verify the algebra, but cannot yet explain why evaluating at the midpoint creates a mean change. A short expansion of b(theta+dtheta/2) should show the added term (b'b/2)dt, using the already stated squared-increment mean. A simple D(theta)=a theta example then makes the added mean velocity a/2 visible. This is a missing causal calculation, not an undefined label. It does not block the fixed-D Fisher explanation.

## Important terms already covered sufficiently for their present use

These are retained under the updated audience baseline. This list records actual teaching, not just keyword hits.

| Term or group | Teaching checked | Why sufficient here |
|---|---|---|
| Neuron, spike, firing rate, synapse, excitation, inhibition, recurrent connectivity | 00-reading-guide.md:14; 01-foundations.md:14-22 | Gives the physical sender, event, receiving effect and feedback path. The 20 Hz example distinguishes an average rate from regular timing. |
| Tuning curve, slope, baseline, population code, encoding and decoding | 01-foundations.md:24-34 | Supplies a rate-angle formula with units and neuron identity, then explains reading the represented value from spikes. |
| Place cell, place field, rate map and grid cell | 00-reading-guide.md:49; 01-foundations.md:39-47 | Establishes localized firing, connected field regions, spikes divided by visiting time and the repeated grid pattern. These are enough for the memory-path previews. CA1 and CA3 are identified as hippocampal areas, with the input/recurrent differences needed by the paragraph. |
| Poisson spike counts | 01-foundations.md:51-109 | Gives the count law, units, a zero-count probability and the independent/shared distinction. The needed count variability and noise assumptions are explained under the updated baseline. |
| CV and Fano factor | 01-foundations.md:116-119 | Defines each ratio and distinguishes interval variability from count variability. An exponential interval distribution is mentioned as a property, but its shape is not subsequently used in this assigned path, so I did not file it as a required missing prerequisite. |
| Covariance, correlation and gain | 01-foundations.md:123-168 | Starts with recorded shared changes, gives signed above/below-average meaning and units, then derives how common signal, gain and private noise differ. |
| Displacement, lag, MSD, random spreading and bias | 01-foundations.md:172-207; 01b-persistence.md:114-142 | Maps measured angles to changes, separates mean-squared bias from variance, and states what changes movement versus recorded movement. |
| State, fixed point, neutral direction, continuous attractor and attractor manifold | 01b-persistence.md:13-21 and :28-74 | Defines what changes and what does not, then shows two disturbances with the same initial angle and different long-term outcomes. |
| Brownian motion | 01b-persistence.md:81-121 and :157-171 | Gives increment assumptions, variance growth and shared-history covariance. The Brownian concept is taught rather than merely named; a Gaussian reminder is optional under the updated baseline. |
| Synaptic activation, transfer function, weights, time constant | 02-memory-dynamics.md:13-55 | Connects a spike's unit jump to exponential decay and the receiving cell's input/rate. Undergraduate calculus can read the decay scale from the displayed exponential. |
| Weak fluctuation approximation | 02-memory-dynamics.md:78-91 | States the approximation's object, many small contributions, matched mean/covariance and controlled population-size example. It properly distinguishes input fluctuations from a whole spike train. |
| Linearization, left/right zero eigenvectors, projection and stable modes | 02-memory-dynamics.md:107-204 | Gives the first-order expansion, why the tangent persists, why the left vector removes decaying directions and a tilted-decay example. No separate glossary expansion is needed for an undergraduate linear-algebra reader. |
| Diffusion tensor | 02-memory-dynamics.md:235-250 | Defines diagonal spreading and off-diagonal shared coordinate changes and derives them from one cell's effects. |
| Fokker Planck equation, Dirac delta and wrapped angular error | 02b-memory-long-delays.md:17-76 | Supplies the probability-redistribution calculation, point-mass initial condition and bounded-error interpretation. Probability density is known under the updated baseline; the equation and delta themselves are explained. |
| Translation symmetry and readout translation invariance | 02-memory-dynamics.md:299; 03b-memory-readout.md:35-58 | States the actual unchanged dynamics or error statistics and uses the latter to obtain cue-independent variance. |
| Prior, unbiasedness and Cramer Rao limitation | 03-memory-information.md:54-72 | Gives their meanings and the finite-sample/bias/prior qualifications. These need a clearer statistical example within M4, but are not absent labels. |
| Precision and ideal readout | 03b-memory-readout.md:130-189 | Defines inverse variance, derives Gaussian precision addition and the backward recursion, and explains what later observations estimate. |
| Hyperbolic tangent, inverse tangent and cotangent | 03b-memory-readout.md:168-200 | Defines the functions and uses separation of variables and a short-interval expansion. Undergraduate calculus is sufficient. |
| Partial spike access | 03b-memory-readout.md:233-260 | Says which spikes are withheld, shows observed-information scaling, keeps storage diffusion fixed and works through numbers. |
| Neural integrator and leak | 03b-memory-readout.md:389 | Defines accumulated input and distinguishes growing variance from a restoring change in the mean. |

## Labels and previews not misclassified as omissions

- The reading guide's lower bound, covariance, Fisher information, scalar/matrix bounds and probability-density links are previews of later teaching, including 00-reading-guide.yaml:77-100. They are not themselves sufficient teaching, but do not require complete derivations in the reading map.
- The supplementary-source footnote's reverse Kalman filter name at 03b-memory-readout.md:404 points to the source's method. The main text derives the recursion without needing that name, so no standalone Kalman-filter lesson is necessary.
- Sigmoidal at 02b-memory-long-delays.md:174 is immediately explained as S-shaped; the plot comparison does not need its full analytic formula.
- No caption adds a further required undefined paper-specific concept. The captions are generally careful about which data are constructed, how the coordinate is measured and what each curve represents.

## Source record and limits

The original 03-memory-information.md SHA256 read before the coordinator's edit was C0136CBC43748A376655D3AEBA17F76AF323DB38B05663E61C4FC481812C6DBA. All source hashes below are recomputed from the frozen baseline, not a revised live manuscript. No source PDF retrieval was needed because these findings concern missing teaching rather than a disputed scientific result. No images, builds, broad quality gate or historical review packet were opened. This audit does not establish scientific correctness or acceptance of chapters outside its assigned path.
- 00-reading-guide.md: 10073BD9D7290239DBD4A1437AEE7C5EFF9C8CB608A37C9F9F3C123EB3565A4F
- 00-reading-guide.yaml: 5DFB629BD6ACEFAA62B0281A40FE5767A4B2021902C50016628BB2C96F48A696
- 01-foundations.md: A3D82E833C2DE9D5576C6AC86C4B60C310A2985B95E6585F75E150F306109822
- 01-foundations.yaml: 56E92E2F198B7736F690495AC53930F1B269557003A23810B0C721A60D811733
- 01b-persistence.md: A45DC50A637A47D1E5E34FC12AA00DB7F0A1DF5422879C1B88B45A4DB231AA2F
- 01b-persistence.yaml: E5DE0D836DEC59FE743E24C13428376BE2590DE52C48B211DBFAD5ABCFE6280B
- 02-memory-dynamics.md: 622A08B479A8586B17FF7A8F7D847253123393EF6A64EE9A91FB52AAB69E577F
- 02-memory-dynamics.yaml: D2557621AD1B9EC338AE9B74DC8DFCB6A9104E23267AF165812BF633DF674940
- 02b-memory-long-delays.md: 57334095704E2BC12F382075F7C8C2372DB6C5A292D04BCAE866F77E1B241C50
- 02b-memory-long-delays.yaml: C7367B86D14E6EF36C2F2693A4981C3E5B69BA4222177E74AE33EE64CFC0845B
- 03-memory-information.md: C0136CBC43748A376655D3AEBA17F76AF323DB38B05663E61C4FC481812C6DBA
- 03-memory-information.yaml: 980E32B4180729ED0E7E133E238AFAE4FD27AE8EEEC5A673E240D31DFDA9171D
- 03b-memory-readout.md: 3825584BE21265F8553CA806C71BD45D213E31E55C651152BB395283B390CDF3
- 03b-memory-readout.yaml: 339BBB09ED573AC6146F77C33A7535EB4EC8060D7D68F33B68A4D0BF64BA8D2D
- glossary.md: 820EF7A60BC869DAFB2AB585AECABA1797418DEA03212C76B5F31A0790A16DE9

End: 2026-10-30T12:48:15.0445104+02:00. Wall-clock elapsed from persisted start: 166.4 seconds. Awake execution time unavailable because system sleep/resume events were not queried. Measured checkpoint 2026-10-30T12:46:14.8833824+02:00 was 46.3 seconds after start. An earlier message estimated three minutes incorrectly and was corrected to the coordinator. No system-time change was observed. Remaining work for this assigned audit: none. Token stats unavailable.


Audience clarification applied at 2026-10-30T12:48:39.6304192+02:00. The four basic-statistics omissions and the conditional-independence omission are withdrawn. Main remaining required repair: the Fisher explanation and its likelihood/estimator relationships. The Itô/Stratonovich conversion is a separate smaller mechanism gap. Token stats unavailable.

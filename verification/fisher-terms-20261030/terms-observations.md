# Terms and prerequisites: observations chapters

Read-only reviewer: `/root/terms_observations`. Start checkpoint: 2026-10-30T12:45:37.5812968+02:00. Audience supplied by coordinator: undergraduate mathematics, no statistics or neuroscience assumed. User correction received during review: expected value, variance, standard deviation and probability density are known and do not need explanation. This report follows that correction. The guide itself says calculus, basic probability and linear algebra at `content/chapters/00-reading-guide.md:74`. No general Gaussian/probability primer is proposed.

Method: read current reader text and sidecars, then trace candidate missing terms to earlier teaching. No historical review, manuscript edit, build, visual inspection, full quality gate or primary-paper fact audit. This is a terminology/prerequisite judgment, not acceptance of all scientific claims. The skill references request a concept-index tool, but this subtask used direct passage review; no automated concept-index result is claimed.

Scope: `content/index.md`; `04-eye-drift`, `04b-eye-timing`, `04c-eye-circuit`, `05-place-fields`, `05b-place-sizes`, `05c-place-tests`, `06-synthesis` Markdown and YAML; glossary and references Markdown; Part openings in `plan/chapter-plan.yaml`. Earlier teaching checked in `00-reading-guide`, `01-foundations`, `01b-persistence`, `02-memory-dynamics`, `02b-memory-long-delays`, `03-memory-information`, `03b-memory-readout`. Earlier files were checked for needed passages, not approved in full.

## Findings

### O1. Skew and excess kurtosis have formulas but lack their meaning in this test

Priority: P2, required teaching repair.

Use: `content/chapters/05c-place-tests.md:166`, repeated in `05c-place-tests.yaml:85` and `:111`. The main passage gives centered moments, both standardized formulas, and the zero values under a lognormal size model. It does not say what a nonzero value would mean about observed log lengths, or why these two measurements test a size distribution beyond its mean.

Prior teaching checked: no earlier main-text explanation of skew or kurtosis. `glossary.md:94` calls skew a measure of asymmetry; `glossary.md:29` only repeats the kurtosis formula and Gaussian zero. Those later lookup entries cannot provide the missing local interpretation.

Reader question left unanswered: “If the measured log lengths have positive skew or large excess kurtosis, what feature of their distribution differs from a Gaussian?”

Repair: before the formulas, say skew measures unequal spread toward the two sides of the mean, with positive skew indicating a longer or more influential upper side. Explain that the fourth power gives far-from-average observations strong weight, so excess kurtosis compares that standardized fourth-moment weight with the Gaussian value. Apply this to unusually large or small log lengths. Add that zero skew and excess kurtosis do not by themselves prove a Gaussian distribution. No new topic or long derivation is needed.

### O2. Map processing is listed using operations that the reader cannot reconstruct

Priority: P2, required teaching repair.

Use: `content/chapters/05c-place-tests.md:173-180`: “rectified at about 0.5 Hz” and “received a median filter” lead directly to the conclusion that processing can remove components and alter peaks and tails.

Prior teaching checked: `01-foundations.md:39` teaches rate estimation from spikes/time and warns that smoothing and cutoffs matter. `05-place-fields.md:61-68` and `05-place-fields.yaml:47-48` teach the model's threshold-and-subtract operation. Neither explains whether the empirical 0.5 Hz operation subtracts 0.5 before clipping, merely sets lower bins to zero, or uses another rule. No earlier passage explains a median filter.

Reader question left unanswered: “What changed in a recorded bin, and how could that merge or erase a small field?”

Repair: state the empirical threshold operation exactly after checking Methods; do not silently equate it with the model's rectifier. Define a median filter as replacing each spatial-bin value by the middle value of nearby-bin values, giving the neighborhood if reported. A three-value example such as `[0,8,0]` becoming 0 at the centre shows why an isolated peak can disappear. Keep this to a few sentences.

### O3. The p value definition still depends on an unexplained test statistic/reference

Priority: P2 for the supplied no-statistics audience, local addition sufficient.

Use: `content/chapters/04-eye-drift.md:114`, with later p value at `:235`. The paragraph identifies a positive-mean question and a zero-mean reference, then defines a p value through “a test statistic at least as large as observed.” It does not identify the statistic or explain what repeated data under that reference represent. A zero mean alone does not specify a full reference distribution.

Prior teaching checked: `01-foundations.md:133-168` adequately teaches covariance/correlation; that does not teach testing. No earlier main-text hypothesis-testing explanation was found. `glossary.md:73` repeats the formal conditional definition.

Reader question left unanswered: “Which number is being compared with which possible repeated results, and does the tiny p value mean a tiny probability that the shared-drive claim is wrong?”

Repair: briefly describe a reference world with no positive population relationship, identify the paper's actual test and statistic after checking Methods, and explain that its reference distribution describes the statistic across repeated samples under that assumption. One small illustrative tail-count example can make “at least this large” concrete. Explicitly distinguish this from the probability that the reference hypothesis or a particular neural mechanism is true. Do not introduce a full testing course.

### O4. The signed critical-point count is invoked without explaining which signs occur

Priority: P2, focused bridge in a mathematical section.

Use: `content/chapters/05c-place-tests.md:37-49`: Morse theory is described as a signed count, then “Morse signs” replace the absolute Hessian determinant by `det(-H)`.

Prior teaching checked: `05b-place-sizes.md:28` teaches Hessian and directional curvature; `05c-place-tests.md:17-25` teaches components/holes/Euler characteristic well. No earlier passage connects maximum, saddle, minimum to positive and negative contributions for the above-threshold region. Basic linear algebra explains determinant signs but not why those signs correspond to this topological count.

Reader question left unanswered: “Why should counting a maximum add to this quantity, while a saddle can subtract, and how does `det(-H)` encode that?”

Repair: give the 2D picture as the level descends: a maximum creates a component, a saddle joins components or creates a hole, and a minimum fills a hole. Thus their contributions to Euler characteristic are +1, -1, +1. Relate those signs to `det(-H)` and say the theorem extends the rule, including boundary terms. The text already says the theorem is not proved, so no full Morse-theory proof is requested.

### O5. Rank/Spearman correlation is a small lookup gap in the supplemental check

Priority: P3, small addition, not a blocker for the main shared-drive argument.

Use: `content/chapters/04c-eye-circuit.md:214` calls Figure 8 a rank correlation check; `04c-eye-circuit.yaml:139-142` says rank correlations also show a positive relation and calls them Spearman correlations in alt text.

Prior teaching checked: `01-foundations.md:133-157` teaches ordinary normalized covariance; `04-eye-drift.md:235` calls the main statistic Pearson correlation. No earlier main-text or glossary explanation distinguishes correlation of ranks.

Reader question left unanswered: “What changed when the authors repeated the check with ranks?”

Repair: say that Spearman correlation replaces the measured values by their ordered ranks before computing correlation. It checks whether larger predicted displacements tend to accompany larger recorded displacements without requiring a linear relation. One sentence beside the check is sufficient.

## Important terms that already have adequate support

- OMN, abducens nucleus, ocular plant and integrator: `04-eye-drift.md:14-18` gives their physical roles and signal path. No anatomy expansion needed.
- Covariance versus correlation versus common fraction: foundations `01-foundations.md:133-168`, then `04-eye-drift.md:251-359` derives the different denominators and gives one fully worked numerical case. “0.17” versus “82%” is taught, not merely labeled.
- Causal filter, impulse response and convolution: `04-eye-drift.md:142-180` connects a single spike to one position response and adds past responses; `:207-227` checks gain and units. The exponential factorization is supported by undergraduate differential equations/calculus rather than a mandatory signal-processing course.
- SEM and inverse-variance weighting: `04-eye-drift.md:235` distinguishes cell-mean uncertainty from cell spread/animal uncertainty; `:376-385` derives weights and explains their assumptions. A full sampling-theory chapter is not needed for this use.
- White noise, stationarity, low pass filtering and superdiffusion: `04b-eye-timing.md:78-127` supplies operational definitions; `:145-214` traces the stored command, mismatch, velocity and MSD. The one-pole synonym is explained at `:214`, so it is not a remaining missing term in the sidecar.
- Renewal and sub-Poisson spiking: `04c-eye-circuit.md:130-146` gives the construction, interval independence, CV and long-window count consequence. The derivation supplies the particular meaning used here.
- Upcrossing and Kac-Rice: `05-place-fields.md:123-174` derives why slope weighting counts each crossing once. A separate general theorem is unnecessary for this application.
- Stationarity versus isotropy versus smoothness: `05-place-fields.md:43-55` separates their jobs and gives a covariance counterexample. The spatial/time distinction is repeatedly explicit at `:17`, `:23`, and in synthesis `06-synthesis.md:19`.
- Rayleigh, Weibull, gamma function and change of variables: `05b-place-sizes.md:58-90`, `:115-166`, `:185` supply the construction/formulas, units and integration meaning. These do not need additional named-distribution surveys.
- Euler characteristic and Betti numbers themselves: `05c-place-tests.md:17-35` gives counts and concrete disk/ring/shell examples. Finding O4 concerns the next theorem bridge, not their definitions.
- Shared-position covariance and inhibition: `06-synthesis.md:43-81` derives slope products, supplies units and numbers, and explicitly rejects inferring an inhibitory connection from negative covariance. No additional prerequisite gap found in the synthesis calculation.
- Likelihood already has an actual definition and worked spike model at `03-memory-information.md:21-43`. Do not count it as wholly missing just because it appears again in `05c-place-tests.md:169`; however that earlier chapter is skipped by the advertised place-field route, so a brief local reminder/link would help that route.
- Place cell, hippocampus, CA1/CA3, grid cell and rate map: `00-reading-guide.md:49` and `01-foundations.md:39-47` establish their roles before the later applications.
- References are lookup entries rather than teaching claims; no demand to define every specialist word inside cited paper titles. Part openings use plain physical questions and preview scope rather than depending on unexplained quantitative methods.

## Limits and delivery

No Fisher-information repair was assigned to this reviewer. This report identifies the later chapters' use of the existing information discussion but does not duplicate the coordinator's Fisher assessment. No source PDFs were needed for the finding that reader text lacks an explanation. Implementing O2/O3 would require checking the original Methods before specifying the empirical operation or test.

Completion checkpoint and SHA256 evidence follow below. Awake execution time cannot be verified separately because Windows sleep/resume logs were not inspected. Wall-clock duration must use these actual checkpoints, not reading-speed estimates. Token stats unavailable.

Source-hash checkpoint: 2026-10-30T12:48:33.4553103+02:00.
Wall-clock at source-hash checkpoint: 175.9 seconds since start; 110 seconds since previous clock checkpoint at 12:46:43.4315281.
Source SHA256 captured at completion (not an initial freeze claim):
```
content/index.md 361396B67AD80CD60D3A9B7767E6A360E0643D17ABF80EBECE7B4741923C8BFC
plan/chapter-plan.yaml 394E5BFDCCA536683BACFEF577C10434B25361DDFD31F5588248FAB976BBF8E6
content/chapters/00-reading-guide.md 10073BD9D7290239DBD4A1437AEE7C5EFF9C8CB608A37C9F9F3C123EB3565A4F
content/chapters/01-foundations.md A3D82E833C2DE9D5576C6AC86C4B60C310A2985B95E6585F75E150F306109822
content/chapters/01b-persistence.md A45DC50A637A47D1E5E34FC12AA00DB7F0A1DF5422879C1B88B45A4DB231AA2F
content/chapters/02-memory-dynamics.md 622A08B479A8586B17FF7A8F7D847253123393EF6A64EE9A91FB52AAB69E577F
content/chapters/02b-memory-long-delays.md 57334095704E2BC12F382075F7C8C2372DB6C5A292D04BCAE866F77E1B241C50
content/chapters/03-memory-information.md A72E78AF0058DDF578F76BB8423D49E0E300A2CD1D36EFCE5F5904AC6BB3BAE2
content/chapters/03b-memory-readout.md 3825584BE21265F8553CA806C71BD45D213E31E55C651152BB395283B390CDF3
content/chapters/04-eye-drift.md FB0456DE89DE74FA7DEE8905CE60E86CC2F17E3CFE69C945B447DE4232C06CD6
content/chapters/04-eye-drift.yaml B987975477E369AF4EA4DF616B05BEC2DCC73AC2C0E04B701B5CD80D9077E41F
content/chapters/04b-eye-timing.md 4D7395F284CA8A2E09B2D301C97CEF98070C0528B756CEB06CA75570BADAC3BC
content/chapters/04b-eye-timing.yaml 0269C4F78FF2566C7FF78E51CC7D025E1CACD9C3A587A115E38DE500B3D787BE
content/chapters/04c-eye-circuit.md F1B09BB79A5B27C1FA3A8A359C5DBFAB38E8B35D73B8E3CDFB9D20F793D228D9
content/chapters/04c-eye-circuit.yaml EAF05BC6D089A80FDF8ECCD7DEA973938456A8F8A3ACF390E767CF267536E41A
content/chapters/05-place-fields.md 121BA17BB52C2E7AA55485DEACD19FCBE67EDE0BA0A1302DA7D8B977E8752AFD
content/chapters/05-place-fields.yaml 9D16F7CD09968130B4ACC80414D2ABCC73ED77031EDF470E14E5305C81D3F200
content/chapters/05b-place-sizes.md 6897F5E00F3A59FCC218A87322F29476F042D9620DC6CE8122D0C4C4CB1C866A
content/chapters/05b-place-sizes.yaml 1061EC6CB926996467ED8BACAB1716D88F32E8F371325EC56D41E811CDEC5A27
content/chapters/05c-place-tests.md D9F5F07AA39684B37124A437E2A13FF25A9AD8620AB8642B43DAA91575E87D6F
content/chapters/05c-place-tests.yaml 210C382FF32BD22F1A9DFEEF2544BAD6F670467E3F622B1CF78126A7778392DA
content/chapters/06-synthesis.md CF048EB1334D4538E6D23A8EDB59E8E5F9AE68751263C6DF9810F285F68D2122
content/chapters/06-synthesis.yaml A943E0A943DC48C0D8CC08B8BD45A9EAA94405951D4DC199418E9D997733A5E3
content/chapters/glossary.md 820EF7A60BC869DAFB2AB585AECABA1797418DEA03212C76B5F31A0790A16DE9
content/chapters/references.md 469A5434EF417D78F2FC88DEB69B5D1CFAE6D01B9CF747F7415AA2F1F32608DB
```
Final report adjustment: 2026-10-30T12:48:58.1902612+02:00. Removed the conditional Gaussian expansion after coordinator clarification; retained four focused teaching findings and one minor supplemental term.

Rules SHA256:
```
C:/Users/vital/.codex/skills/course-study-guide-builder/SKILL.md B78068E9874E6D1D97B2017BF8F940492F9B08FC11B74F20FD75019FF388984A
C:/Users/vital/.codex/skills/course-study-guide-builder/references/pedagogy-language-contract.md F4C1EB544CF640B708E1970D9572FDC758FCC6AEA806675D01A0256658DF847A
C:/Users/vital/.codex/skills/course-study-guide-builder/references/concept-prerequisites.md 4C8D4AF325FB63AF8DBE41D447D4BAC7197DF550B0DDB9F4CDB0DEA3B1FE9F9A
```

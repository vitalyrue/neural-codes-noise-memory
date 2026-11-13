# Independent stage 1: truth and reasoning

Reviewer: `/root/terms_observations`. Local request ID: `terms-observations-stage1-20261030-125233` (local label, not a platform call ID). Start checkpoint: 2026-10-30T12:52:33.2994754+02:00. This reviewer did not write the repaired sentences. Only stage 1 was requested and performed. Stages 2 and 3 remain pending separate requests.

Audience: undergraduate mathematics; expected value, variance, standard deviation and probability density are known, following the user's clarification. No primer on them is requested.

Verdict: no required truth/reasoning correction found in the requested repair and glossary entries. This is a local stage-1 result, not full guide acceptance.

## Midpoint noise and drift

Reviewed current `content/chapters/02b-memory-long-delays.md:127-158`, especially repaired `:139-150`; connected definitions at `:17-39` and `:90-100`; Brownian increments at `01b-persistence.md:102-109`; weak input fluctuations at `02-memory-dynamics.md:73-87`.

- `02b-memory-long-delays.md:139`: the positive/negative-step explanation has the correct sign. Locally increasing positive amplitude means a positive Brownian increment is multiplied by a slightly larger coefficient and a negative increment by a slightly smaller coefficient. Under the same coefficient and zero written drift this midpoint convention differs from the beginning-of-step convention. The qualification about using the same written coefficient matters: an added drift correction can express the same process in the other convention.
- `:143-147`: checked the Taylor calculation directly. Expanding `b(theta+Delta theta/2)` gives `b + b' Delta theta/2` to the retained order; substituting the leading `Delta theta=b Delta W` yields the correction `bb'(Delta W)^2/2`. This is the local small-step expansion, not an exact finite-step identity. The displayed approximation signs preserve that distinction.
- `:150`: the Brownian moments give conditional mean increment `bb' Delta t/2`. From `b^2=2D`, differentiation gives `2bb'=2D'`; hence the local Itô drift is `D'/2`. The factor and sign are correct. Constant `D` gives zero correction. The explicit positive, smooth local region at `:143` avoids extending this square-root differentiation to a zero or nonsmooth boundary.
- `:139`, `:150`, and connected `:134`: the explanation does not claim that neural drift has thereby been established. It explicitly says the microscopic neural process decides which drift arises and that the convention comparison supplies a possible scale. Boundary/domain qualifications from the surrounding section remain present. It does not infer a global mean velocity after boundary encounters from this local calculation.
- `:154`: the order comparison matches the supplied supplement's fixed-model large-population comparison: with diffusion and its variation scaling as `1/N`, noise displacement is of order `sqrt(dt/N)` and convention-related mean displacement of order `dt/N`. This is a scale estimate in the paper's setting, not a universal conclusion for arbitrary changes of coordinate or model with `N`.

Primary evidence read directly from local `assets/papers/burak-fiete-2012-persistent-activity-si.pdf`, PDF pages 4-5, “Systematic drift,” Eqs. S19-S20. The source says exact drift requires the microscopic Master equation, gives `D'/2` for the Stratonovich interpretation, and describes its magnitude comparison as plausible rather than an exact neural drift result. The repaired text preserves those limits. No historical review was read for this stage.

## New glossary entries

| Current passage | Connected teaching and check | Stage-1 verdict |
| --- | --- | --- |
| `glossary.md:28`, estimator | `03-memory-information.md:105` defines a rule from observed spike counts to an estimated represented value. The glossary's angle or other coordinate is consistent with that model and does not promise an accurate or unbiased rule. | Retain. |
| `glossary.md:35`, Fisher information | `03-memory-information.md:19-23` states local sensitivity of observation probabilities. `:37-52` derives squared expected-count slope over count variance for independent positive-rate Poisson counts; `:89-101` defines the score and its expected square. The glossary keeps the independent Poisson condition rather than making the sensitivity/noise ratio universal. Its short description agrees with the exact formal definition. | Retain. |
| `glossary.md:67`, median filter | `05c-place-tests.md:178` explains the local middle-ranked replacement and small-field consequence. The supplied Mainali main paper, STAR Methods “Data processing,” specifies `scipy.ndimage` median filtering with size 2 and 10 cm spatial bins. The glossary's “middle-ranked” wording does not assert that the implementation averages the two middle values of an even-sized neighborhood. “Reduces isolated high or low rates” is the intended local filtering effect, not a guarantee that all outliers or measurement errors disappear. | Retain. |
| `glossary.md:75`, one sided t test | `04-eye-drift.md:114-120` identifies the positive direction and `t=mean/(s/sqrt(n))`, explains the zero-mean t reference and sampling assumptions, and distinguishes cells from animals. The glossary describes this mean-comparison test correctly without claiming the independence assumption is experimentally proven. The local Ben-Shushan paper's Figure 1 caption confirms one-sided t testing across 57 cells and the quoted p value. | Retain. |
| `glossary.md:99`, Spearman correlation | `04c-eye-circuit.md:214` says both sets are replaced by ranks before correlation, with larger-prediction/larger-recording interpretation. That is consistent with normalized covariance of ranks already supported by the earlier correlation definition. It does not claim arbitrary nonlinear dependence will be detected or that the statistic identifies a source. | Retain. |

The t-test and median-filter main-text passages were read to verify the glossary's claims, not to perform their full separate terminology/flow review. No manuscript edits, builds, visual review or whole-guide audit were performed. Token stats unavailable.

## Timestamps and source evidence

Actual completion time, durations and SHA256 values are recorded below. Awake execution time is not separately verified because sleep/resume logs were not inspected. These hashes describe sources at completion; no initial frozen-source claim is made.

Completion: 2026-10-30T12:53:50.6324661+02:00
Wall-clock elapsed: 77.3 seconds. Since previous checkpoint: 42.6 seconds.
```
content/chapters/02b-memory-long-delays.md BB4C8EAE336F19236A3E46C3325EAACDD91FF96D4B238C8616657F9C777BDBB0
content/chapters/glossary.md 86944917BF60F4128BB7B06AAE1AD872BEFEDA2587F02EC3927447731BF476D3
content/chapters/01b-persistence.md A45DC50A637A47D1E5E34FC12AA00DB7F0A1DF5422879C1B88B45A4DB231AA2F
content/chapters/02-memory-dynamics.md 622A08B479A8586B17FF7A8F7D847253123393EF6A64EE9A91FB52AAB69E577F
content/chapters/03-memory-information.md 1FA7A49F1741511F9827612EBB5FCAE35ECB27399673828C4D7A6D8B9906CCBE
content/chapters/04-eye-drift.md 8E58C899BA46968D83B7A137E75CA70B46F5157BD08A50C7E0930BEC91B36933
content/chapters/04c-eye-circuit.md 54E9715273CB0DEF9E045E02F6F1B71841DCDF1A1FDFAA9C6AA46606E9236007
content/chapters/05c-place-tests.md B119F91382ACCAA6D0581AF2D2008B2DBE13A01448C3C38147F8439B62A49D75
assets/papers/burak-fiete-2012-persistent-activity-si.pdf 9BBFF1FB83DB4AA4B76364A92DE7C481DE1F27CCDD6735DCE78AE1D7B8496EFB
assets/papers/mainali-2025-universal-statistics.pdf DE2CA50A46F5B0D8D14E86269F1BEACF6AADDE7122BB348568AAD92B12FD802E
assets/papers/ben-shushan-2022-fixational-drift.pdf 15F273F99BD8D8E8DAA09A9F7809E04C53DA514B146750C0EC517812E3478CAA
```

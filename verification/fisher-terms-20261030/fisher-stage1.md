# Fisher information review: stage 1, truth and reasoning

Local request ID: fisher-stage1-20261030. Independent reviewer: /root/fisher_review. The parent is the writer. Only stage 1 was requested and performed. No previous review report, writer defense, or task baseline was read. The chapter sources and actual earlier reading path were read directly. No manuscript edits were made.

Audience: undergraduate mathematics. The parent's live audience correction says expected value, variance, standard deviation, and probability density are known. No general statistics primer is required. Fisher information and its paper-specific relationships still need explanation.

Start UTC: 2026-10-30 10:47:54. First checkpoint UTC: 2026-10-30 10:48:41, wall elapsed 47 seconds. End UTC: 2026-10-30 10:50:05 UTC. Wall duration: 131.4 seconds. Awake execution time was not separately verified from Windows events. No clock change was observed. The initial estimate was 3 to 5 minutes. Token stats unavailable.

## Decision

PASS for the truth and reasoning of the current Fisher section and its connected chapter claims. No required correction found. This does not complete stages 2 or 3, figure pixel inspection, rendered output checks, or whole-book acceptance.

## Coverage and stage questions

Read the whole of `03-memory-information.md`, its sidecar, `01-foundations.md`, `02-memory-dynamics.md`, and `02b-memory-long-delays.md`. Checked the supplied 2012 main paper pp. 2 to 5 and SI pp. 9 to 12 as primary evidence. Earlier chapters were read for connected meaning, not given a new unrelated source audit. The primary PDF pages have no line numbers, so source evidence below uses page and equation labels.

What does each main claim literally say, what would the reader infer, and does the evidence support it?

| Passage | Answer and evidence | Decision |
| --- | --- | --- |
| `03-memory-information.md:5-13` | A finite spike sample limits estimation of the current value, while the recurrent spike noise also moves that value. This does not say that the resulting diffusion bound is achieved. The distinction is already set up by `02b-memory-long-delays.md:149-158`. Main paper p. 2, Internal Fisher Information and Fig. 1, supports the connection. | Retain. |
| `03-memory-information.md:17-23` | Fisher information measures local change in observation probabilities, rather than the number of bits or the success of a chosen decoder. The text explicitly separates nearby discrimination from distant ambiguity. It holds the state fixed for the count calculation and makes conditional independence and positive rates explicit. `01-foundations.md:109` and `02b-memory-long-delays.md:145` prevent reading this as independence of full recurrent spike histories. SI p. 9, S42-S43, defines the same leading short-interval calculation. | Retain. |
| `03-memory-information.md:29-33` | Adding constant baseline firing keeps the local slope fixed and increases Poisson count variance. The relative change becomes half as large, so its squared comparison and information become one quarter as large. The example is declared illustrative and distinguishes multiplying the entire tuning curve. Independent numerical check below agrees. | Retain. |
| `03-memory-information.md:37-58` | For the given Poisson family, squared count slope divided by count variance equals Fisher information. The equality is not claimed for every distribution. Independent cell contributions add. `I_h` is interval information and `J` is its rate, with the proper coordinate and time units. Main Eq. 3 and SI S42-S44 agree. Doubling a local slope at fixed rate multiplies information by four, and a constant baseline reduces it. | Retain. |
| `03-memory-information.md:60-68`, sidecar first figure caption and alt | A smooth positive-rate peak has derivative zero and thus zero first-order local information for that cell. Other slopes may inform the population. Both analytic curves differ by a constant, so their derivatives agree and the higher baseline gives smaller information wherever slope is nonzero. This is not a claim that a single peaked curve identifies every angle globally. Caption explicitly says illustrative curves, not measured neurons or an established attractor network. | Retain. Pixel appearance was not checked. |
| `03-memory-information.md:72-101` | The parameter is the fixed value being estimated; likelihood compares candidate values using the observed count. It is correctly distinguished from a distribution over angles. The Poisson product, log likelihood, score, mean-zero score, and squared-score expectation follow algebraically. Conditional independence removes cross terms. The expectation in the definition is explicitly over data generated at the candidate true value. | Retain. |
| `03-memory-information.md:105-113` | An estimator is a data-to-value rule. Unbiasedness concerns its average over repetitions at the fixed value, not correctness of each answer. The lower bound applies to estimators unbiased across nearby values and is a variance bound. Four times information halves the bound on standard deviation, without promising decoder attainment. Main p. 3 discusses ideal-estimator saturation in the weak-fluctuation limit; the guide's approximation language is appropriately limited. | Retain. |
| `03-memory-information.md:117-137` | The proof differentiates the same estimator's unbiased expectation, uses the zero-mean score and Cauchy Schwarz, then identifies mean squared error with variance under unbiasedness. Smoothness, exchange of differentiation and summation, and positive finite information are specified. Prior information or accepted bias changes the estimation problem. No claim is made that the displayed bound applies unchanged to those cases. Boundary and zero-rate cautions are present. | Retain. |
| `03-memory-information.md:139-180` | Linear growth `I_h=hJ` is restricted to the effectively fixed state. The diffusion proof then uses the previously derived local projection with `u= tau r'` and `v^T u=1`. Taking the dot product of `v sqrt(r)` and `r'/sqrt(r)` yields `1/tau`; Cauchy Schwarz gives `D >= 1/(2 tau^2 J)`. It does not need symmetric weights. Assumptions are inherited explicitly from `02-memory-dynamics.md:107-127,210-248`. The result and units agree with main Eq. 4 and SI S45-S49. | Retain. |
| `03-memory-information.md:182-218` | Equality needs the noise projection to be proportional to slope divided by rate. For symmetric weights the same `phi'/phi` is needed among participating cells at each state. A globally constant ratio is sufficient for an exponential transfer function. The positive linear mutual-excitation example is a valid counterexample to an unrestricted converse: `u=(1,1)`, `v=(1/2,1/2)`, rates `theta/tau`, and `2DJ=1/tau^2`. The guide clearly labels its qualification of the source's converse in SI p. 11, S50-S51. Its state-dependent ratio does not spoil equality. | Retain. |
| `03-memory-information.md:230-256`, sidecar second caption and alt | The mutual-inhibition rates, slopes, information, diffusion, and bound values are correct in the positive-rate domain supplied in `02-memory-dynamics.md:303-321`. Increased information lowers the allowed minimum while actual diffusion stays fixed. Independent numeric check below agrees, as does the caption formula `J=2000/(40000-theta^2)`. | Retain. Pixel appearance was not checked. |
| `03-memory-information.md:260-289` | The matrix condition describes every linear combination, not just coordinatewise diagonal bounds. Under invertible `J`, the dimensions of `U,V`, their products, and the residual `Q^TQ` calculation are correct. SI pp. 10 and 12, S44 and S52-S56, supports this result. The singular case is explicitly excluded from the ordinary inverse formula. | Retain. |
| `03-memory-information.md:301-325` | Population, firing-scale, and synaptic-time comparisons state what is fixed. Repeated tuning curves with scaled weights give `J` proportional to population size and `D` inversely proportional to it. Multiplying rates and slopes by `a` gives `J -> aJ`. Diffusion scaling is qualified by equality or preserved symmetric tuning geometry. Holding rate curves fixed versus activation curves fixed explains the different powers of `tau`. These qualifications agree with the symmetric formula in `02-memory-dynamics.md:278-287` and clarify main p. 2's comparison. | Retain. |
| `03-memory-information.md:329-377` | With fixed peak, density, and shape, the change of integration variables gives `J` proportional to `w^(d-2)`. Radial shape and uniform coverage justify zero off-diagonal terms. Bound attainment then gives `D` proportional to `w^(2-d)`. Fixing the total rate instead changes the scaling. The guide states boundary, baseline, sparse-coverage, and correlation limits. The final sensory-memory link requires the same tuning curves and does not locate memory in an animal. Main pp. 4-5 support the paper interpretation; the additional scaling steps are properly identified as teaching derivations. | Retain. |

Do definitions, roles, conditions, and symbol meanings remain consistent?

Yes. `theta` remains the present state, `Theta` the initial value, `h` the count interval, and `tau` the neural decay time. The changed section does not exchange `h` and `tau`, nor describe `J` as an amount of information collected over an unspecified time. The angle example uses degrees, while the unit statement explicitly switches to radians conditionally. Activation coordinates in later examples are called out as such. The count model's rates and the recurrent circuit's moving state are kept separate.

Does the reason establish the conclusion, including necessary inputs and results?

Yes. The section first gives the physical count-change/noise comparison, then supplies an exact Poisson likelihood calculation for it. The Cramer Rao proof separately connects this quantity to an unbiased estimator's possible spread. The following section derives the diffusion inequality directly from the network projection, so it does not depend on assuming that the real circuit is an efficient decoder. Local ambiguity, bias, prior information, and changing state all have explicit limits rather than being left to an expert reader to supply.

## Independent numerical calculation

Executed Python with direct Poisson probability summation for counts 0 through 179. Used `p_0=exp(-mu)`, `p_n=p_(n-1)*mu/n`, and score `(r'/r)*(n-mu)`. This checks the likelihood-based definition independently of merely plugging numbers into the displayed information formula.

| Rate | Mean count | Count standard deviation | Count slope per degree | Sum of probabilities | Mean score | Mean squared score |
| --- | --- | --- | --- | --- | --- | --- |
| 40/s | 4 | 2 | 2 | 0.9999999999999997 | 2.58e-17 | 0.9999999999999998 per degree squared |
| 160/s | 16 | 4 | 2 | 0.9999999999999998 | -2.33e-17 | 0.24999999999999994 per degree squared |

Thus `J` is 10 then 2.5 per degree squared per second; the standard-deviation lower limits are 1 and 2 degrees. This confirms the claimed quarter-information result. These are bounds in this chosen model, not measured errors.

Independently computed the later mutual-inhibition example: at `theta=0`, rates are 1000 and 1000, `J=0.05`, `D=1000`, bound 1000; at `theta=100`, rates are 1500 and 500, `J=0.06666666666666667`, `D=1000`, bound 750. Differences below 3e-13 are floating-point rounding.

## Limits and next stage

No reader-facing listing was present to execute. Equations and the relevant numerical examples were checked. Caption and alt claims were read, but figure pixels and HTML were outside this request. No necessity/wording verdict or full flow verdict is implied by the stage 1 pass. Stages 2 and 3 await separate requests.

## Source and rule SHA-256 hashes

- `content/chapters/01-foundations.md`: `a3d82e833c2de9d5576c6ac86c4b60c310a2985b95e6585f75e150f306109822`
- `content/chapters/02-memory-dynamics.md`: `622a08b479a8586b17ff7a8f7d847253123393ef6a64ee9a91fb52aab69e577f`
- `content/chapters/02b-memory-long-delays.md`: `57334095704e2bc12f382075f7c8c2372db6c5a292d04bcae866f77e1b241c50`
- `content/chapters/03-memory-information.md`: `a72e78af0058ddf578f76bb8423d49e0e300a2cd1d36efce5f5904ac6bb3bae2`
- `content/chapters/03-memory-information.yaml`: `980e32b4180729ed0e7e133e238afae4fd27ae8eeec5a673e240d31dfda9171d`
- `assets/papers/burak-fiete-2012-persistent-activity.pdf`: `6ea4f05bf1d0c8870baf8f042e9fc4392c1806e9100d94d2b0d3ab35f345adea`
- `assets/papers/burak-fiete-2012-persistent-activity-si.pdf`: `9bbff1fb83db4aa4b76364a92de7c481de1f27ccdd6735dce78ae1d7b8496efb`
- `C:/Users/vital/.codex/skills/course-study-guide-builder/SKILL.md`: `b78068e9874e6d1d97b2017bf8f940492f9b08fc11b74f20fd75019ff388984a`
- `C:/Users/vital/.codex/skills/course-study-guide-builder/references/pedagogy-language-contract.md`: `f4c1eb544cf640b708e1970d9572fdc758fcc6aea806675d01a0256658df847a`
- `C:/Users/vital/.codex/skills/course-study-guide-builder/references/math-code-case-contract.md`: `ce2313f897b63e74ba59a3afe1bbc4046d3aa84584072cda7e76470a7e3cef9a`

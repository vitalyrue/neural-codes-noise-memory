# Fisher information review: stage 3, reader understanding and flow

Local request ID: fisher-stage3-20261030. Independent reviewer: /root/fisher_review. Separate stage 3 request following stage 2 and its focused recheck. No manuscript edits. Audience: undergraduate mathematics with expectation, variance, standard deviation and probability density known.

Start UTC: 2026-10-30 10:53:10. End UTC: 2026-10-30 10:55:13. Wall elapsed: 123.9 seconds. Previous review ended at 10:52:57 UTC, 13 seconds before this start. Awake execution time not separately verified from system events. No clock change observed. Token stats unavailable.

## Decision

PASS for the current Fisher explanation and its connected reading path. No remaining explanation or flow gap requiring repair was found. This is a local teaching verdict, not a whole-book, visual, or publication verdict.

Read every prose paragraph and equation in `03-memory-information.md:15-139`, the intervening figure caption and alt, the chapter opening and later bound/comparison connections, the current predecessor handoff, the next readout chapter's setup and relevant uses of J, and the two glossary entries. The complete Fisher chapter was read in stage 1 and is unchanged apart from the two already checked simplifications. Current source hashes are recorded below.

The predecessor now includes an added Stratonovich derivation, shifting its later line numbers. Its current Fisher handoff and independence explanation were read at `02b-memory-long-delays.md:158-171`. This report does not claim a new truth audit of that separate addition.

## Reader questions answered from the text

**What acts on what?** The circuit's present state theta sets each cell's firing rate through its tuning curve. That rate determines a distribution of possible spike counts during h. A receiving cell or observer has those counts and tries to infer theta. Separately, those spikes affect recurrent synaptic activations and can leave a changed memory state after the network settles. The necessary neural chain is supplied by `02-memory-dynamics.md:17-55`, and the Fisher section applies it to observation at `03-memory-information.md:17-23`. The bound returns to the effect of spikes on state at `:143-180`. The reader need not imagine that a statistical quantity itself pushes the network.

**What does Fisher information measure?** How much the probabilities of possible count patterns change when the proposed current value changes a little. In the Poisson model, it is large when expected counts change steeply with theta compared with the count noise. The state and count roles are given at `:19-23`; the local slope/noise computation appears at `:29-49`; the likelihood makes the probability meaning explicit at `:72-101`. It measures a local distinction and does not promise to distinguish distant angles that produce the same response (`:21`).

**Why square the score?** The score is the log likelihood's slope. Different count samples favor increases or decreases in theta, and at the true theta their signed slopes average to zero. Squaring keeps their size from canceling (`:93-101`). The later proof gives the square a further mathematical job: Cauchy Schwarz relates mean squared score to mean squared estimation error (`:117-133`). Thus the text supplies both the immediate reason not to average the signed slope and the reason this squared quantity controls a variance bound. The reader does not need prior knowledge of the score or an unexplained statistical theorem.

**Why does added background firing differ from multiplying all rates?** Adding a constant rate raises the count mean and Poisson variance but does not change the rate slope. In the example, count slope remains 2 per degree while standard deviation rises from 2 to 4, so information falls to one quarter (`:29-33`). Multiplying a tuning curve by a scales both its rate and its slope: the squared numerator scales by a squared, the denominator by a, and J scales by a (`:311`, using `:49`). The text first warns of that difference before deriving the fuller scaling later; it does not require the reader to know it in advance.

**How does local information differ from a memory trajectory?** I_h=hJ describes counts collected while theta remains effectively fixed (`:23,139`). It does not describe all information about an entire moving path, or erase movement that happened before observation. The earlier chapter separates movement from current-state reading (`02b-memory-long-delays.md:165-171`). The next chapter restates this distinction and constructs an explicit evolving-state model at `03b-memory-readout.md:5-32`. Its local observation variance 1/(Jh) is introduced as part of a Gaussian approximation, not inferred as an exact error of every decoder. This is a sufficient connection between the two chapters.

**What does the inverse bound promise, and what does it not promise?** An estimator unbiased across nearby values, satisfying the listed conditions, cannot have variance below 1/(hJ). Four times information halves the lower bound on standard deviation. Individual answers can still be wrong, and a given decoder may be worse than the bound (`:105-133`). Prior knowledge, systematic bias, boundaries, or zero rates require care (`:137`). The subsequent physical bound similarly allows lower diffusion when J is larger but does not make a particular network achieve it (`:180,230-256`). These limits are stated before a reader must use either bound as a comparison.

## Paragraph purpose and continuity record

All locations below are in `content/chapters/03-memory-information.md`. Hashes are the first 12 hexadecimal characters of SHA-256 of the exact paragraph line in the recorded file; full-file hashes below bind the complete text and equations. Every row is retained for the concrete reason given.

| Line | Paragraph hash prefix | Purpose and connection | Decision |
| --- | --- | --- | --- |
| 17 | `4f026c8ed47e` | States the receiving cell's problem: variable counts must distinguish angles. Follows the chapter opening's motion/readout distinction and motivates the metric. | Retain. |
| 19 | `5e0fd6be907b` | Names the needed metric, identifies observed spikes and unknown present state, and states its decoder-independent role. Prepares both the local qualification and the calculation. | Retain. |
| 21 | `7da6f4729bd5` | Explains local by comparing nearby and distant angles. Prevents the next local derivative calculation from promising global angle identification. | Retain. |
| 23 | `82f6061e48d9` | Introduces the observation interval and count model with its fixed-state, positive-rate and independence conditions. Supplies every model input needed by the example. | Retain. |
| 29 | `26859817767e` | Converts rate, duration and slope into mean count, count spread and count change per degree. Makes the physical comparison available before its formula. | Retain. |
| 31 | `1c3ecd9c30ba` | Changes only background rate and tracks exactly what changes and what does not. Shows why extra counts can reduce useful distinction; the square comparison prepares the formal expression. | Retain. |
| 33 | `df6e8ce9bc36` | Marks the numbers as illustrative and separates baseline addition from whole-curve multiplication. Prevents a misleading more-spikes conclusion and prepares the later controlled comparisons. | Retain. |
| 37 | `c68d8c144e64` | Turns the example into general notation while explaining the neural meaning of the derivative. The following single-cell equation now has a supplied numerator and denominator. | Retain. |
| 44 | `611068e0d3c9` | Identifies the ratio as exact for this Poisson family and adds independent cells. Leads directly to the total interval information and rate equations. | Retain. |
| 52 | `7912a14c241d` | Names internal information rate and separates present state, observation duration and units. Stops J from being read as an unspecified information amount or bit count. | Retain. |
| 54 | `c68511c9d710` | Introduces the short list as consequences of the expression, so the list tests the formula rather than introducing a new method. | Retain. |
| 56 | `112ce19f5e5a` | Separates a change in slope at fixed rate; the square supplies the factor of four. Gives one controlled change for comparison with baseline addition. | Retain. |
| 57 | `addbb502e2f3` | Connects the background example to the displayed denominator. Brief repetition ties the physical example to the general calculation. | Retain. |
| 58 | `f5b95eb21c13` | Uses independent addition of cells, then states the limit for shared fluctuations. Prepares the population interpretation without implying arbitrary noise independence. | Retain. |
| 60 | `e3ad8017f215` | Explains the zero-slope case and the role of other cells. Gives the reader a specific feature to look for in the following teaching curves. | Retain. |
| 68 | `9100af81004e` | Interprets the shared derivative and greater baseline noise after the figure. The last sentence explains why the formal derivation comes next. | Retain. |
| 72 | `babeb52e2bce` | Defines likelihood through fixed observed counts and varying proposed theta. The reused four-versus-sixteen count setting is concrete; the final sentence blocks confusion with probability over angles. | Retain. |
| 74 | `18911f127af2` | Combines the already established independent cell count model into the observed-vector likelihood. Prepares the product formula. | Retain. |
| 81 | `8675fc762575` | Explains why logarithms are taken and recalls the rate derivative notation. The next log likelihood and derivative follow by undergraduate calculus. | Retain. |
| 93 | `39e7ca06cea8` | Names score, interprets its sign, and explains why its raw mean vanishes at the true value. Squaring solves this cancellation and prepares its nonzero average size. | Retain. |
| 101 | `448c959b685c` | Explains each surviving term and the disappearance of cross terms, gives the formal mean-squared-score definition, and ties it back to the initial ratio. Retains the distribution limit. | Retain. |
| 105 | `64187a553f11` | Introduces the estimation rule and unbiasedness before the bound depends on them. Distinguishes average correctness from trial error and connects that error to variance. | Retain. |
| 107 | `c60099208e54` | Names the bound and attaches it to the nearby-unbiased class and smoothness assumptions. Prepares the displayed inverse-information limit. | Retain. |
| 113 | `9c175ef4fc5e` | Translates the variance limit into standard-deviation scaling and explains non-attainment versus the paper's useful approximation. Answers what the bound means before the proof. | Retain. |
| 117 | `8d1925e25388` | States the precise proof conditions, then starts from the same estimator's unbiased mean. Preserves the necessary local role and moves directly to the derivative identity. | Retain. |
| 125 | `0d4e05397343` | Explains the zero-mean-score subtraction and states Cauchy Schwarz in the form used for error and score. Makes the inequality step readable from the supplied math background. | Retain. |
| 133 | `51c904e5390c` | Explains why mean squared error is variance here and why division by information is allowed. Completes the proof without losing its conditions. | Retain. |
| 137 | `41e31a119785` | Identifies prior information, bias, boundaries and zero rates as changes or limits to this problem. The sensory/internal comparison returns to the paper's setting after the abstract proof. | Retain. |
| 139 | `0565c0c1be95` | Restores the moving network after the fixed-state calculation and separates current-state information from recovery of the initial value. Gives direct onward routes to the diffusion bound and readout. | Retain. |

The example title at line 27 states the question answered by its three paragraphs. The derivation titles at lines 70 and 115 identify optional deeper calculations whose main conclusions and meanings remain present outside the folded blocks. Equation blocks at lines 39-49, 76-99 and 109-130 were read with the paragraphs that introduce and interpret them. They do not add an unintroduced data source or unexplained neural role. Mathematical operators are appropriate to the audience and need no basic primer.

## Figure and glossary connections

`03-memory-information.yaml:44-50`: the caption supplies the actual analytic curves, their chosen width and rate units, shared derivative, zero contribution at the peak, and background-noise interpretation. It marks the curves as teaching examples and avoids claiming they establish a recurrent attractor. The alt text follows the sequence rate, derivative, information. This fits the text at chapter lines 60 and 68: the reader knows what to inspect before the figure and what it means afterward. No missing prerequisite has been delegated to the picture. Pixels were not reviewed.

`glossary.md:28`: the estimator entry is a short reminder of the observation-to-value rule taught at chapter line 105. Its angle-or-coordinate example matches the chapter's scope. As lookup text, it needs no invented transition or full bound proof.

`glossary.md:35`: the Fisher entry gives the local meaning, formal reminder and Poisson interpretation, then links to the actual explanation and example. Score is explained in that teaching location. The short entry supports recall; it is not being used as the only teaching source. No additional glossary expansion is needed.

## Chapter order and connected open read

The predecessor first derives and interprets movement of the stored value, then explicitly separates that movement from uncertainty in reading the present state. The current chapter begins with that second problem, teaches J, derives its link to D, then shows why comparing networks requires controlled changes. The next chapter asks how reading works when the state moves during observation. This order supplies the quantities before the moving-state calculations use them.

The Fisher chapter's later material gives each early distinction a purpose. The bound proof at lines 143-180 uses the information rate alongside the already taught network projection. Equality and the two-cell calculations at lines 182-256 show why a lower bound is not actual performance. The matrix discussion at lines 260-289 extends the scalar direction comparison. The controlled comparisons at lines 301-370 explain why baseline addition, rate multiplication, population changes and width changes cannot be lumped together. The sensory comparison at line 377 uses the earlier meaning of internal. The next chapter's opening then returns directly to the unresolved observation-duration problem already signposted at line 139, so another transition paragraph is unnecessary.

On the final connected read, the explanation can be followed as one chain: the observer receives variable counts; nearby states change their probabilities; rate slope relative to noise measures that local distinction; the score calculation identifies the measure formally; the inverse relation limits unbiased estimation; the same spike source also perturbs recurrent memory; and a moving state requires a new readout calculation. The text supplies each of these steps. It does not require the reader to supply an outside explanation of likelihood, score, unbiasedness, or the role of the interval. No required new repair emerged from this read.

## Limits

This pass is restricted to the changed teaching section and its needed chapter and glossary connections. No figure pixel review, browser check, build, full quality gate, unrelated chapter audit, or publication claim is included. Source footnotes identify the earlier verified paper locations; this stage did not repeat the stage 1 numerical or primary-paper checks.

## Current source and rule SHA-256 hashes

- `content/chapters/01-foundations.md`: `a3d82e833c2de9d5576c6ac86c4b60c310a2985b95e6585f75e150f306109822`
- `content/chapters/02-memory-dynamics.md`: `622a08b479a8586b17ff7a8f7d847253123393ef6a64ee9a91fb52aab69e577f`
- `content/chapters/02b-memory-long-delays.md`: `a088bae67645f1ceaa3389c8ed71700ecd24c9fcd010b8997f6adee0ced978a7`
- `content/chapters/03-memory-information.md`: `1fa7a49f1741511f9827612ebb5fcae35ecb27399673828c4d7a6d8b9906ccbe`
- `content/chapters/03-memory-information.yaml`: `980e32b4180729ed0e7e133e238afae4fd27ae8eeec5a673e240d31dfda9171d`
- `content/chapters/03b-memory-readout.md`: `3825584be21265f8553ca806c71bd45d213e31e55c651152bb395283b390cdf3`
- `content/chapters/glossary.md`: `86944917bf60f4128bb7b06aae1ad872befeda2587f02ec3927447731bf476d3`
- `C:/Users/vital/.codex/skills/course-study-guide-builder/SKILL.md`: `b78068e9874e6d1d97b2017bf8f940492f9b08fc11b74f20fd75019ff388984a`
- `C:/Users/vital/.codex/skills/course-study-guide-builder/references/pedagogy-language-contract.md`: `f4c1eb544cf640b708e1970d9572fdc758fcc6aea806675d01a0256658df847a`
- `C:/Users/vital/.codex/skills/course-study-guide-builder/references/math-code-case-contract.md`: `ce2313f897b63e74ba59a3afe1bbc4046d3aa84584072cda7e76470a7e3cef9a`

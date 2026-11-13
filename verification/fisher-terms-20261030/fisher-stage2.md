# Fisher information review: stage 2, necessity and terminology

Local request ID: fisher-stage2-20261030. Reviewer: /root/fisher_review. Separate request after completed stage 1. No edits. Stage 3 has not been performed.

Audience: undergraduate mathematics, including known expectation, variance, standard deviation, and probability density. The review does not ask for a general statistics primer.

Start: 2026-10-30 10:50:35 UTC. End: 2026-10-30 10:52:00 UTC. Wall duration: 85.3 seconds. Time since previous stage ended at 10:50:05 UTC to this start: 30 seconds. Awake execution time not separately verified. No clock change observed. Token stats unavailable.

## Decision

PASS: no required terminology or necessity repair. Two small optional deletions below remove generic labels that this audience does not need. They are not correctness defects and do not block the next review stage. No core explanation, assumption, derivation, or example should be removed.

The current chapter and sidecar match the stage 1 hashes. Read `03-memory-information.md:15-139` again directly for this stage. The earlier whole-chapter and prerequisite reading remains applicable on the unchanged text. Relevant earlier teaching: `01-foundations.md:14-34` introduces rates, tuning curves, population codes and decoding; `01-foundations.md:49-109` teaches the Poisson count model and conditional independence; `02-memory-dynamics.md:9-15,107-157,210-248` supplies the memory coordinate, stable family, projection, and local noise assumptions; `02b-memory-long-delays.md:145-158` distinguishes changing memory and reading it. The connected later chapter was considered for why the Fisher explanations are needed.

## Passage-based deletion and terminology decisions

| Passage | What it adds; deletion test; term decision |
| --- | --- |
| `03-memory-information.md:17` | Establishes the actual problem: a receiving cell sees variable spike counts and must infer angle. Removing it would leave a metric without a physical question. Rate and count are already taught. Retain. |
| `03-memory-information.md:19` | Defines Fisher information, identifies the observation and unknown value, and separates information in the model from a chosen decoder. These are distinct jobs; none is only an announcement. The exact term is central to the paper and needed. Retain. |
| `03-memory-information.md:21` | Defines the specialist meaning of local and prevents a large information value from being read as global identifiability. The distant-angle contrast earns its place even for a mathematically experienced reader. Retain. |
| `03-memory-information.md:23` | Supplies the time interval, observed counts, fixed-state approximation, positive rates and conditional independence before calculation. The mean/variance statement applies a known statistical idea to this model; it does not reteach variance. Retain. |
| `03-memory-information.md:27-33` | The extra-background example counters the tempting inference that more spikes always supply more information. The numbers expose how unchanged slope and increased variability compete. The standard deviations are needed numerical steps, not a basic-statistics lesson. The final rate-scaling contrast protects the example's scope. Retain all three paragraphs. |
| `03-memory-information.md:37-49` | Maps the known derivative to the specific neural rate change, converts it into count change, and shows why independent contributions add. The purpose of each symbol and the distinct interval quantity are needed. No generic explanation of differentiation, multiplication, or summation is added. Retain. |
| `03-memory-information.md:52` | Internal and rate are paper-specific parts of the term. Their meanings and the units prevent mixing current memory with a present external stimulus, interval information with rate, or Fisher information with stored bits. Retain. |
| `03-memory-information.md:54-60` | Slope scaling, baseline addition and extra cells give distinct consequences of the formula. The baseline bullet briefly connects the example to the equation. The zero-slope case is needed to interpret the peaked tuning curves and the limits of a cell's contribution. Infinitesimal is appropriate undergraduate mathematics and is needed for the qualification. Retain. |
| `03-memory-information.md:68` | Interprets the two analytic curves and connects the intuitive ratio to its formal definition. It helps establish why a second derivation follows, rather than repeating the definition without a purpose. Retain. |
| `03-memory-information.md:72` | Likelihood is necessary for the formal definition and score. Its fixed-observation meaning and its distinction from probability over angles both matter. The four-versus-sixteen example reuses the current count setting without adding a second scenario. The generic definition of parameter adds little because the local role of theta was already given at lines 19 and 23; see optional deletion A. |
| `03-memory-information.md:74-101` | The likelihood, log likelihood and score are mathematical objects used in the derivation, so they earn their terminology. Score is explicitly defined by its derivative and interpreted through positive/negative changes. Centered counts refers to the displayed `n_i-r_i h`, with the subtraction and covariance idea already present in foundations. Conditional independence is necessary to remove cross terms. The final distribution qualifier prevents overextending the Poisson formula. Retain. |
| `03-memory-information.md:105-113` | Estimator and unbiased are needed to state precisely which rules the bound applies to. The individual-error warning distinguishes unbiasedness from always being right. The variance sentence links that distinction to the next bound; it is brief and does not launch a known-statistics tutorial. The factor-of-four interpretation converts an inverse variance bound into a familiar error scale. Retain. |
| `03-memory-information.md:117` | Every actual assumption is needed for the proof. The generic name regularity conditions is not used later; see optional deletion B. Do not remove the listed conditions or the nearby-values condition. |
| `03-memory-information.md:125-133` | The form of Cauchy Schwarz explains how it applies to error and score. It is more than a name drop, and the mean-squared-error equality explains why unbiasedness matters. Positive and finite information is needed when dividing. Retain. |
| `03-memory-information.md:137` | Prior distribution is a necessary term if this exception is named. It is defined immediately and makes clear that extra knowledge changes the problem. Bias, boundaries, and zero rates limit the result; they are not detachable warnings. Sensory versus maintained internal value connects this formula to the paper's terminology and later comparison. Retain. |
| `03-memory-information.md:139` | Returns from the fixed-state calculation to the moving circuit and distinguishes estimating the current value from recovering the initial value. The assumption appeared earlier, but repeating it here prevents extending linear accumulation to long observations. Retain. |

Connected chapter decisions: `03-memory-information.md:143-180` needs the projection and Cauchy Schwarz steps to derive the physical bound without assuming an ideal decoder. `:182-218` needs equality conditions and the linear counterexample to keep the source qualification honest. `:230-289` needs the scalar counterexample and matrix direction calculation because they show distinct limits. `:301-377` needs the controlled comparisons because increasing information, attaining the bound, and reducing actual diffusion are different claims. These later uses justify the distinctions taught in the Fisher section. No changes to those passages are proposed in this stage.

## Optional exact simplifications

A. `03-memory-information.md:72`: parameter is already familiar undergraduate vocabulary, and its concrete role was already stated at lines 19 and 23. The new definition styling can suggest another new concept when the needed object is simply theta. Keep likelihood's full meaning. Replace the first three sentences:

> The value being estimated is called the parameter. Here it is theta during the short observation. A likelihood compares proposed parameter values by the probability each assigns to the observations already obtained.

with:

> A likelihood compares proposed values of theta by the probability each assigns to the observations already obtained.

Keep the existing likelihood definition markup, mathematical theta notation, count example, and final distinction from a distribution over angles. This removes redundant generic naming and keeps the local role explicit. It does not remove a needed assumption, since the fixed observation and meaning of theta are already established.

B. `03-memory-information.md:117`: delete only this sentence:

> These are the regularity conditions needed here.

Keep the complete preceding assumption sentence and the following differentiation instruction. The label has no later use and the conditions themselves already do the explanatory work. This is a small reader-effort saving, not a missing-definition finding.

Neither change is required to understand the current text. There is no justification for a broader rewrite, removing the numerical example, deleting likelihood or score, or adding explanations of expectation/variance/density.

## Hashes

- `content/chapters/01-foundations.md`: `a3d82e833c2de9d5576c6ac86c4b60c310a2985b95e6585f75e150f306109822`
- `content/chapters/02-memory-dynamics.md`: `622a08b479a8586b17ff7a8f7d847253123393ef6a64ee9a91fb52aab69e577f`
- `content/chapters/02b-memory-long-delays.md`: `bb4c8eae336f19236a3e46c3325eaacdd91ff96d4b238c8616657f9c777bdbb0`
- `content/chapters/03-memory-information.md`: `a72e78af0058ddf578f76bb8423d49e0e300a2cd1d36efce5f5904ac6bb3bae2`
- `content/chapters/03-memory-information.yaml`: `980e32b4180729ed0e7e133e238afae4fd27ae8eeec5a673e240d31dfda9171d`
- `C:/Users/vital/.codex/skills/course-study-guide-builder/SKILL.md`: `b78068e9874e6d1d97b2017bf8f940492f9b08fc11b74f20fd75019ff388984a`
- `C:/Users/vital/.codex/skills/course-study-guide-builder/references/pedagogy-language-contract.md`: `f4c1eb544cf640b708e1970d9572fdc758fcc6aea806675d01a0256658df847a`
- `C:/Users/vital/.codex/skills/course-study-guide-builder/references/math-code-case-contract.md`: `ce2313f897b63e74ba59a3afe1bbc4046d3aa84584072cda7e76470a7e3cef9a`

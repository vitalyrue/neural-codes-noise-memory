# Focused stage 2 repair recheck: memory and glossary

Reviewer: independent agent /root/review_memory_guide. Local request ID memory-stage2-recheck-20261022T195251+0300. Separate stage 2 recheck before stage 3. No chapter edits. Requested model configuration GPT-6.1-sol/high; exact runtime configuration not exposed.

Start: 2026-10-22T19:52:51.8601514+03:00. Checkpoint: 19:53:15.3737085 on the same date and offset. End, wall duration and current/previous input hashes are in JSON. Awake execution is unverified; no sleep/resume-log check. Token stats unavailable.

## Original findings

| Finding | Passage checked now | Decision and reason |
|---|---|---|
| N1 | 02-memory-dynamics.md, sec:MEMORY-LONG-TIME lines 237–278; sec:MEMORY-DRIFT-SCOPE line 310; new glossary entries | Closed. Itô's beginning-of-increment meaning now appears before the Taylor calculation. Dirac delta is explained as all initial probability at Theta and distinguished from the earlier matrix delta. Stratonovich's midpoint limiting convention appears beside the comparison. These meanings preserve the valid variance/drift argument without a separate stochastic-calculus chapter. |
| N2 | 02-memory-dynamics.md, sec:MEMORY-SPIKES line 60; sec:MEMORY-SYMMETRIC line 216; sec:MEMORY-FIGURES lines 320–324 | Closed. Preferred angle is tied to a rate peak before density scaling uses it. The early bump-shape aside is removed. Activity bump is introduced as a localized population-rate peak ordered by preferred angles beside the figure. Sigmoidal is paired with S-shaped. These connect the reader's tuning curves to the actual figure objects. |
| N3 | 03-memory-information.md, sec:MEMORY-FI line 64, with uses at 213 and 288; glossary prior distribution | Closed. Prior knowledge is explicitly knowledge before observing current spikes, and the term is introduced before it qualifies the error bound or no-prior readout model. The later short uses can now rely on the meaning. |
| N4 | 02-memory-dynamics.md lines 179 and 314; 03-memory-information.md line 421 | Closed. Each affected occurrence now describes generated spike-count fluctuations directly. The text preserves conditional independence, recurrent correlations and the extra correlated-noise model; no global synonym substitution was needed. |
| N5 | 03-memory-information.md, sec:MEMORY-IDEAL lines 313–334 | Closed. Exponential tanh definition, inverse artanh formula/domain/derivative, and coth=1/tanh supply the actual functions used in separating variables, solving for precision, and reading the limiting variance. The definitions are correct and need no new standalone section. |
| N6 | 03-memory-information.md, sec:MEMORY-PARTIAL line 379 | Closed. The label now says limited spike access, matching the thinning calculation and preserving the earlier linear-algebra meaning of projection. |
| N7 | 00-reading-guide.md, sec:READING-PAPERS line 13 | Closed. The prior-task history sentence is gone; published-copy and supporting-information access statements still connect to the paper links, and no source limitation was lost. |
| N8 | 01-foundations.yaml, fig:FOUNDATIONS-ATTRACTOR alt | Closed. Spaces now separate words, rates and angle units. The corrected alt retains all states and arrow meanings; no mathematical or caption change occurred. |

## Added glossary entries

Read the six new memory entries: activity bump, Dirac delta, Itô convention, preferred angle, prior distribution and Stratonovich convention. Their short lookup meanings agree with the changed body passages and retain the same term spelling. They do not replace the body teaching or create a separate prerequisite. Retain these entries.

Read the three new eye/statistical entries for basic meaning, without reviewing the eye chapter's full flow. Gain is a scale converting one signal's change to another. The p-value entry conditions its probability on the specified null comparison and the appropriate extreme statistic. Those meanings are sufficient as lookup entries within this guide.

One new truth issue was reported to root: the initial SEM entry said SEM was “distinct from ... uncertainty across animals.” SEM may be computed from independent animals and estimate the uncertainty in their mean. Root repaired it during this call. I read the final entry at 2026-10-22T19:53:54.2881837+03:00: “An estimate of uncertainty in a sample mean. Its interpretation depends on which observations are treated as independent, such as trials, cells, or animals.” This is correct, keeps the unit-of-replication qualification, and no longer turns a source-specific cell/trial warning into a universal restriction. New issue closed.

## Limits

The recheck covers the bounded repairs, new glossary meanings and their affected local connections. It does not repeat the full unchanged mathematics, accept the eye chapter's sampling argument, or perform stage 3 paragraph flow review. All eight original stage 2 findings and the new SEM-definition issue are closed at the current hashes. No open findings remain in this focused scope.

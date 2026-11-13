# Stage 2: wording and necessity, readout chapter

Review started: 2026-10-28T17:00:27.8934349+02:00.

Scope: separate wording and necessity reading of the complete current `content/chapters/03b-memory-readout.md`. This stage did not repeat the formula audit. No manuscript edits were made.

Reviewed SHA256: `567c2f7e41ca514a9169d695a94d275594a7a6162cc629539bfba08c412f9cd4`.

## Decision

Pass. No required wording repairs and therefore no required old/new replacements.

## Reasons

- The opening states the actual difficulty in ordinary words: collecting later spikes adds evidence while the represented value keeps moving. Subsequent paragraphs identify the quantities needed to follow that problem.
- “Neural question and model” accurately introduces observer problems and statistical approximations. It does not promise a biological implementation of the observer's calculation. “Neural mechanism” introduces the access restriction or the neural time-scale change. The distinction earns the slightly longer label.
- “Mathematical derivation” introduces working calculations: variance addition, covariance integration, backward precision, information loss under thinning, and noise projection. The paragraphs following the labels contain the actual reasoning rather than merely announcing it.
- “Interpretation” introduces what the calculated result means, including its restriction or practical implication. It is not used as a substitute for the calculation or its assumptions.
- The added sentence distinguishing the ideal observer from a demonstrated neural circuit prevents a likely misunderstanding introduced by separating the neural and mathematical roles. It is useful qualification, not filler.
- The moved Gaussian model paragraph retains enough words to distinguish an observation summary from a directly measured state and a continuous approximation from a literal claim about infinitesimal spike samples. Shortening those qualifications would remove teaching needed for the model.
- Repeated references to constant diffusion, local estimation, and symmetry serve different nearby calculations or restate limits at the point of interpretation. They do not require a global deletion pass. The brief second appearance of the cue-state notation also keeps the storage-error calculation readable after the observation-model equations.
- The examples expose real consequences of the formulas: partial access changes readout while leaving storage diffusion fixed, and the strict-inequality example explains the printed-bound caution. They are not decorative substitutions.
- The figure explanation and final integrator paragraph remain useful interpretation. Forcing a further three-label sequence there would add structure without adding teaching.

Reader-understanding and connected-flow review remains a separate stage. This wording pass does not establish final book acceptance or rendered-page acceptance.

Review completed: 2026-10-28T17:01:05.6216476+02:00. Wall elapsed and checkpoint delta from review start: 37.7 seconds. Awake execution unverified. Token stats unavailable.

# Stage 1: correctness and teaching order, readout chapter

Review started: 2026-10-28T16:58:04.4158832+02:00.

Scope: read-only review of the complete current `content/chapters/03b-memory-readout.md`, compared directly with its baseline and Supporting Text VI–VII, printed pp. 12–19. Audience: undergraduate mathematics, no neuroscience assumed beyond the preceding chapters. This review checks the changed teaching and order; it is not a new complete proof audit. No author ledgers, author defenses, historical reviews, or current-state notes were read for this review. Wording and reader-flow decisions remain for their separate review stages.

Reviewed current SHA256: `567c2f7e41ca514a9169d695a94d275594a7a6162cc629539bfba08c412f9cd4`.

## Decision

Pass for correctness and teaching order in the changed passages. No required repairs.

## Evidence and judgments

- **Observer computation versus neural mechanism:** the openings say “Neural question and model” for the statistical readout problem, and line 113 explicitly states that the ideal inference rule is not a demonstrated neural implementation. The backward precision calculation is therefore correctly presented as an observer's calculation. The partial-access passage, lines 195–212, describes an actual proposed neural access restriction and then states the independent thinning assumption needed for its calculation.
- **Assumptions before the equations that use them:** the Gaussian observation model is now introduced at lines 13–25, before the error decomposition. It retains the independent error assumption, many-spike regime, and warning against interpreting the infinitesimal limit as enough physical spikes in an arbitrarily short bin. Constant diffusion, no drift, an unbounded coordinate, local unbiasedness, independent future noise, and translation invariance still appear before the final additive-variance claim. Moving the observation model earlier introduces no new stronger claim. SI S58–S63 and their preceding approximation paragraph support this setup.
- **General tool and network bridge:** the ideal-reader calculation first explains why independent Gaussian likelihoods add precision, then applies that rule to the state transition and the new earliest observation. Its variables and transition variance are supplied before the recursion. The resulting S75-equivalent variance is interpreted through short and long intervals and then related to the neural information bound. The equal-weight calculation similarly explains the shared-increment covariance before using its double integral. Neither calculation needs a prior lesson on Kalman filtering.
- **Neural extension:** symmetric weights are now stated before the two-time-scale model and its matrix calculation, matching SI VII's explicit assumption. The placement of the noise and the two changing neural quantities remain visible before projection. The statement that the sum of two time constants applies only to this model remains intact. The added early symmetry sentence does not silently broaden the model.
- **Gaussian-noise extension:** the noise assumption still precedes the score/projection formulas. The division between derivation and interpretation does not change the constant-q observation model, equality condition, or distinction between sufficient transfer-function classes. The explicit-q calculation remains identified as the guide's reconstruction of SI S93–S95.
- **Results and limits:** the changed order preserves finite-observation versus asymptotic error, variance versus standard deviation, the full-access condition for the cellular-time comparison, the partial-access qualification, and the distinction between readout saturation and neural leak. SI S75, S79–S83, and “Integration time constant,” p. 17, are the relevant source passages.
- **No lost source cautions:** the S71 sign caution, S85 rate-decay-block caution, apparent S83/main Eq. 6 bound-direction issue, and absence of an asserted author correction remain in the current text. The baseline comparison shows no removal of a display equation, worked example, source footnote, or material qualification.

No manuscript changes were made. Any later change to the reviewed text needs a hash check and, if substantive, a recheck of the affected connected passage.

Review completed: 2026-10-28T16:59:04.7812358+02:00. Wall elapsed and checkpoint delta from review start: 60.4 seconds. Awake execution unverified. Token stats unavailable.

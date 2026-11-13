# Eye chapter stage 1 focused recheck

Reviewer: `/root/review_eye_guide`, the independent stage 1 reviewer. Local request ID `eye-stage1-recheck-20261022-193748`, not a platform call ID. Same inherited model setting as the initial review. Token statistics and an independently exposed model-version field are unavailable.

Measured start: 2026-10-22T19:37:48.5017173+03:00. Measured checkpoint: 2026-10-22T19:38:37.8651189+03:00. End, wall duration, current source/rule hashes and affected section hash are recorded in `eye-stage1-recheck.json`. Awake execution time is unverified; no system sleep or clock-change evidence was collected.

Scope: the repairs in `04-eye-drift.md`, lines 372–395 and 427, their equations and connected circuit section, lines 349–427. Primary sources reread: P2 p. 11, Eqs. 23–26 and 34, and the optimization paragraph; P2SI pp. 4–5 and p. 9, Extended Data Fig. 3. Needed current earlier teaching was also checked: Foundations lines 103–105 and Memory Dynamics lines 62–108. No chapter edits, builds, whole-chapter repeat review or stage 2 work.

## Result: both findings resolved

**EYE-S1-01 passes after repair.** Lines 372–385 now explicitly set feedback to zero, replace stochastic spikes by mean rates, define the saturated drives q, and multiply the shared-time-constant synaptic equations by the readout weights. This yields `tau_s * dE_OI/dt = -E_OI + G(E_OI)` directly. It is a deterministic rate replacement, not an exact equation for the unconditional mean of the stochastic nonlinear network. The manuscript correctly keeps that distinction.

The units agree: each q is a ratio of two rates and is dimensionless; eta is in degrees, so G and E_OI are in degrees. The left side is seconds times degrees/second. The argument z represents a proposed position in degrees; G'(z) is dimensionless. At a fixed value G(z)=z, the constant term cancels and the first-order equation in lines 388–392 follows by Taylor expansion. As usual this expansion applies locally where the derivative exists. The new wording does not require linearization through a rectification threshold.

The exact continuum condition G(z)=z over a range implies the local neutral condition G'(z)=1. A neutral readout by itself is not sufficient for an attractor, and line 395 now retains the necessary qualification about other stable directions. Their meaning and the need for them are already taught in the current Foundations 103–105 and Memory Dynamics 102–108. For this rate model, the linearized state matrix also has the expected form `(-I + q' c^T)/tau_s`, with c the signed readout-weight vector, so perturbations in the kernel of c^T decay at rate 1/tau_s. No unsupported stability claim was introduced.

P2's Methods explicitly describe an approximate fixed-point continuum over -50 to 50 degrees. The repaired passage correctly attributes the weight optimization to the source, labels the scalar reduction as a teaching derivation, and says that residual mismatch can drive deterministic motion. This resolves the earlier missing link between recurrence and persistence without promoting the finite fit to an exact attractor.

**EYE-S1-02 passes after repair.** Line 427 now separates a short separation between samples in an ongoing MSD from time elapsed since a new perturbation. It correctly identifies the immediate `-A E_OI(t)` term in Eq. 34. It therefore no longer treats the visual delay as a proof that an ongoing statistic cannot change at short lags.

The actual result is now tied to Extended Data Fig. 3: its caption states that feedback decreases amplitude at all lags and decreases logarithmic slope at lags around and above 100 ms. The Supplementary Notes give the same amplitude-versus-slope distinction, although they use older figure numbers. The repaired text uses the final figure numbering, preserves the model-specific nature of the finding, and explains that the delay is not a hard cutoff. The adjacent feedback equation, sign example and slow-tracking approximation remain consistent with these statements.

## Version and reuse limits

Current chapter SHA-256: `66f81083469e2e7aa5bd9a7738fee091980140608b88b2bf7a9c7d4b44fdc669`.

Normalized section hashes show that only EYE-CIRCUIT-MODEL changed within this chapter. All other target-chapter sections match the initial review. The primary sources and applicable rule files also match. The three earlier chapter files have changed since the initial review; the directly needed current fixed-point/neutral-direction passages were read above and still provide the required meanings. This focused recheck does not grant a fresh general approval to unrelated changes in those earlier chapters. Book-level integration of their reviews belongs to the coordinator.

No required truth/reasoning repair remains in this rechecked scope. The initial stage 1 judgments can be retained for unchanged target sections, subject to the coordinator's dependency integration. Stages 2 and 3 remain pending separate requests. Token stats unavailable.

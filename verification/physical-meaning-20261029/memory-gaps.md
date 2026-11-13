# Focused review of physical meaning in the memory chapters

Recorded start checkpoint: 2026-10-29T10:59:18.4235489+02:00.
Source-read checkpoint: 2026-10-29T11:01:41.0587476+02:00.
Wall time between these checkpoints: 2 minutes 22.6 seconds. Awake execution time was not separately verified from Windows sleep/resume events.

Scope: current `01b-persistence.md`, `02-memory-dynamics.md`, `02b-memory-long-delays.md`, `03-memory-information.md`, `03b-memory-readout.md`, with actual `01-foundations.md` as earlier context. Audience: calculus, basic probability, and linear algebra are assumed; neuroscience is taught. This is a focused gap search, not the three later truth, wording, and flow review calls. No manuscript, build, or current-state changes were made.

Rules read: course-study-guide-builder/SKILL.md and references/pedagogy-language-contract.md. The memory registry at MEMORY.md:69 was used only to confirm the user's earlier request for change, affected quantity, mechanism, and consequence. Current teaching judgments below come from the current chapters, not old findings.

## Result

The chapters already contain substantial causal explanation. Four small repairs would make the physical meaning and parameter effects easier to follow. The first concerns what remains visible when a calculation is folded, rather than missing book teaching. The next three fill specific connections between the equations and the neural process. No new section or chapter is needed.

### 1. Keep the meaning of the two persistence disturbances visible before the folded calculation

Location: `01b-persistence.md`, section `sec:FOUNDATIONS-ATTRACTOR`, after the paragraph beginning “Memory of a continuous quantity calls for a family of persistent states” and before the folded example at lines 13–58.

Strongest contextual reading: lines 3 and 11 already distinguish a stored value from activity and define restoring versus neutral directions. The example correctly demonstrates the distinction at lines 43–50. The gap is that the only concrete account of which activities change together and which change oppositely is hidden in the example, while the visible text is mostly formal definitions.

Suggested visible bridge: “In the two-cell example below, raising both firing rates leaves their difference unchanged. The feedback removes that common increase, so the stored angle stays the same. Raising one rate while lowering the other changes the angle encoded by their difference. The ideal model has no restoring response to that change.”

Keep its status as an illustrative model. Do not describe its imposed differential equations as an experimentally established synaptic circuit. The rate-to-angle conversion, the positive-rate range, and numerical checks are already supplied. In the example, increasing `a` speeds restoration of the common activity, with relaxation time `1/a`; it does not restore an angle error. This one parameter sentence can remain with the calculation.

Folding: the formal state/fixed-point/manifold definitions can move into a short definition fold after a plain explanation of activity patterns, a stored value, restoration, and its absence along the memory direction. Keep those physical meanings visible. The existing worked example may stay folded. Its essential two-disturbance contrast should not be folded away with all of its algebra.

Support: this guide's explicitly illustrative dynamics, recomputed by adding and subtracting the two rate equations; main paper p. 2, Fig. 1 and flow definition. No additional experimental claim is needed.

### 2. Connect a spike to the receiving cell and interpret the two terms in K

Locations: `02-memory-dynamics.md`, `sec:MEMORY-SPIKES`, paragraph beginning “The fixed weights W_ij say how neuron j affects neuron i” at line 48; and `sec:MEMORY-LINEARIZATION`, immediately after K at lines 105–111.

Strongest contextual reading: foundations lines 11–16 teach excitatory/inhibitory synapses and recurrence. This chapter correctly says spikes renew decaying activation and defines the input sum and transfer rule. It does not yet spell out the complete cell-j to cell-i chain or the physical competition in K. A reader can follow its algebra while missing why decay, weight, and firing sensitivity set the return flow.

Suggested replacement/extension at line 48: “A spike from cell j raises s_j by one. It therefore changes cell i's total input by W_ij; that contribution then decays with time constant tau. For an increasing transfer rule, a positive weight raises the receiving cell's firing rate and a negative weight lowers it. The transfer function phi gives the rate produced by the combined input.”

Suggested short interpretation after K: “The first term removes an activation disturbance as its synaptic effect fades. The second term is recurrent renewal: a disturbance in cell j's activation changes cell i's input through W_ij, and phi'(g_i) converts that input change into a rate change. A steeper transfer rule makes this recurrent response stronger. Whether a disturbance decays, persists, or grows depends on the combined response of all cells.”

Conditions/units: keep the increasing-transfer qualification on the sign claim. `s` is dimensionless in this spike convention; `g` has model input units, not automatically volts; W has input units per activation unit; phi' has firing-rate units per input unit. Each K entry has units inverse seconds. A stronger single connection alone does not guarantee better memory or a stable attractor.

Folding: Taylor expansion, formal eigenvector equations, and the proof that the left vector discards decaying modes can fold. Keep the spike-to-input-to-rate chain, the physical meaning of K, the left vector's role as the lasting coordinate change per activation disturbance, and the final diffusion relation visible.

Support checked directly in local PDFs: main p. 5, Eqs. 7–11; SI p. 3, Eqs. S7–S15. The interpretation follows directly from these equations.

### 3. Explain why mutual excitation retains one change and why higher activation increases noise

Location: `02b-memory-long-delays.md`, `sec:MEMORY-LONG-TIME`, paragraph beginning “The rate of random spreading can change as the stored value changes” at line 72, with its result at lines 89–96.

Strongest contextual reading: the chapter already explains that current rates set spike variability and explicitly computes D. Earlier material explains recurrence generally. The missing local connection is what mutual excitation does to the two disturbances, and why this particular coordinate changes the noise amplitude rather than only changing a symbol in D.

Suggested insert after the fixed activation states: “When both activations rise together, each cell raises the other's firing enough to replace the extra synaptic decay. That common increase persists and changes the stored value. A disturbance in their difference decays back to the bias-set difference. Larger theta raises both firing rates, so it also raises both Poisson noise variances; because the projection weights here stay fixed, the retained fluctuations become larger.”

Conditions/units: this uses exactly the stated linear rule `phi(g)=g/tau`, weights `+1`, and opposite biases. The physical active range is `theta > |b_0|/2`, where both steady rates are positive. Theta here is an activation coordinate, not an angle. Keep the existing boundary/domain qualification and the separately identified printed factor discrepancy. This insert does not resolve behavior after the process reaches the edge of the active range.

Folding: the moment identities and short-time variance expansion can fold; keep their consequence visible: different local spreading rates can change long-delay error, and a D linear in theta can still give linear variance growth under the stated no-drift/domain conditions.

Support: SI p. 9, Eqs. S38–S41 checked directly in the local PDF; decay of the difference follows by subtracting the two deterministic activation equations.

### 4. Explain the physical reason for the controlled tau comparison

Location: `03-memory-information.md`, `sec:MEMORY-COMPARISONS`, paragraph beginning “Changing tau while holding the rate tuning curves and their input relation fixed” at line 220.

Strongest contextual reading: this paragraph correctly states two different exponents and explicitly requires retuning. The chapter already explains extra neurons, rate-dependent count noise, baseline firing, and tuning width. What is missing for tau is the causal step behind the inverse-square result.

Suggested insert: “At fixed firing rates, a longer-lasting spike effect gives a larger mean activation, since s_bar=tau r_bar. The activation change separating two nearby stored values grows by the same factor. In the symmetric comparison with the rate and input curves fixed, a one-unit spike disturbance therefore produces a smaller lasting change in the stored value: each projection weight scales as 1/tau. The spike variance per unit time stays fixed, so its contribution to memory variance scales as 1/tau squared.”

Conditions/units: retain symmetry and the controlled tuning/input comparison. This explains the existing formula, not a claim that changing a synaptic time constant alone preserves an attractor. Retain the adjacent linear example where holding activation curves fixed changes rates and gives inverse tau instead. Tau is in seconds; coordinate units and the spike-jump convention stay fixed.

Folding: the formal scaling calculation can fold after this explanation and its controlled-comparison condition; keep the different physical quantities being held fixed visible.

Support checked directly: main p. 2, Eq. 1 and parameter comparison after Eq. 2; main p. 5, Eqs. 7–11; SI p. 3 projection formula. The explicit fixed-curve projection scaling is a guide derivation, not an extra experimental result.

## Sufficient passages to retain

- `02-memory-dynamics.md`: outgoing synaptic activation, conditional noise, population replication, lasting displacement versus perpendicular projection, and the warning that higher rates alone do not imply more memory damage are already explained. Do not replace them with an unrelated membrane-current model.
- `02b-memory-long-delays.md`: wrapping, repeated-trial density, state-dependent diffusion, systematic drift, and the scope of conditional independence already have causes and limits. No additional physics paragraph is needed for each mathematical name.
- `03-memory-information.md`: slopes relative to Poisson variation, baseline spikes, the information/diffusion distinction, non-guaranteed equality, and tuning width versus active-cell count already explain parameter effects. Population averaging is also taught in foundations. Do not duplicate these explanations.
- `03b-memory-readout.md`: storage motion versus observation uncertainty, harm from equal weighting, declining value of later observations, partial access, and gradual rate adjustment are already causal. It explicitly avoids claiming a biological implementation of the ideal observer. No additional physical mechanism section is needed.

## Other formal material that can fold while keeping its meaning visible

This is a placement recommendation, not additional scientific findings:

- Persistence: the full Brownian definition and covariance proof can fold after visible random-increment meaning, the D convention, and the consequence that error spread grows with time. Keep boundary limits visible.
- Information: likelihood/score algebra and the Cramer Rao proof can fold. Keep J as squared tuning slope relative to spike variance, the interpretation of inverse information, the diffusion bound and its conditions, and the distinction between a lower bound and achieved stability visible. The matrix construction and matrix-order definition can fold together; retain its meaning as a bound for every combination of coordinates.
- Readout: precision, tanh/artanh/coth definitions, separation of variables, and backward recursion can fold together. Keep the physical tradeoff, the meaning of the limiting error, L* as a gradual saturation scale, and what changes under partial access visible. Do not introduce hyperbolic functions in visible prose only to explain an already folded calculation.

Later requested separate truth, wording, and flow checks remain pending for any actual repairs. No full-book acceptance, visual check, or release judgment is implied.

## Completion checkpoint

Saved at 2026-10-29T11:03:41.8624432+02:00. Awake duration remains unverified. No sleep/resume event audit was needed for this brief source review.

Source SHA256 values at completion:
- 01-foundations.md: C83DE02188F833833AC124F5E9E1563D80BC33FAB3BF5B5B5AACE870B071B335
- 01b-persistence.md: 9F0CB9E173497C001747F11483F3EC198DF51F49314F63378897365306DB4F61
- 02-memory-dynamics.md: 5DD6132D9197D14A47FBAC02CB99DF78733039C45A04E53109FD834D7332D922
- 02b-memory-long-delays.md: A2893E0FE10B0AF8A2E874451D89407BD2C5558D3CB19CFEF7282A9C28F6B0C6
- 03-memory-information.md: 2B5684C62D0068E49E4A2B06C071401C75B4D6C83DAB63044D45463DFFB190D3
- 03b-memory-readout.md: EC48CFFA812EEEE81B6DF9472F048C821923DDA4E260DD7B7DE8D654FF61F97C

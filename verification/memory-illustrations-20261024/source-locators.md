# Chapter 2 source locations

Recorded: 2026-10-24T18:09:25.153251+03:00

Read-only map of the current chapter against the saved 6-page Early Edition main paper and 20-page Supporting Text. Page numbers below are PDF page numbers. No reader files were edited. No paper line numbers are invented.

## Source versions

- `main`: burak-fiete-2012-persistent-activity.pdf, 6 pages, SHA256 `6ea4f05bf1d0c8870baf8f042e9fc4392c1806e9100d94d2b0d3ab35f345adea`.
- `si`: burak-fiete-2012-persistent-activity-si.pdf, 20 pages, SHA256 `9bbff1fb83db4aa4b76364a92de7c481de1f27ccdd6735dce78ae1d7b8496efb`.
- Chapter SHA256: `355cc06de2e14005708a6b87ec3b0617627773a90b3ef2d5b9e670e8afbc6266`.

## Main findings

- All S7-S15 are on SI p. 3; the existing projection footnote can be narrowed from pp. 3-4 to p. 3.
- Main Eq. 2 visibly lacks the numerator square; SI S18 has it. The guide square follows S18 and direct projection. This is a source comparison, not an author-confirmed erratum.
- SI S40 prints D=theta/(2 tau), while S41 prints variance=Theta t/(2 tau). With the guide convention Var=2Dt, the guide calculation D=theta/(4 tau) matches S41. Both printed values were visually checked.
- The tilted-decay example is original teaching material. The paper supplies the left-vector projection, but not that example.
- The guide mutual-inhibition coordinate is theta=s1-s2. The paper figure caption uses a firing-rate difference; the coordinates differ by tau, so diffusion coefficients differ by tau squared.
- Arbitrary covariance Q is a guide extension. The Discussion calls correlated neural models conjectures still to be tested. Independent, unequal Poisson variances are already present in S10 and S15.

## Suggested nearby links

- **model-and-spikes**: After ds_i=-s_i dt/tau+dN_i and the g_i/r_i equations. [Paper model, Eqs. 7-9](../../assets/papers/burak-fiete-2012-persistent-activity.pdf#page=5). Direct model, with count notation rewritten.
- **weak-noise**: After the Brownian approximation and its total-input qualification. [Weak fluctuation limit, Eqs. 10-11](../../assets/papers/burak-fiete-2012-persistent-activity.pdf#page=5). The most useful link for the approximation itself; the existing large-N footnote can link SI S1-S6.
- **left-projection**: After v^T K=0 and v^T u=1. [Left mode and normalization, SI S12-S13](../../assets/papers/burak-fiete-2012-persistent-activity-si.pdf#page=3). Keep close to the first left-vector definition; source explains why K need not be symmetric.
- **tilted-example**: At the end of the tilted-decay example, beside existing figure. [Projection argument, SI S12-S15](../../assets/papers/burak-fiete-2012-persistent-activity-si.pdf#page=3). Label the example as a guide reconstruction; the paper does not contain xdot=ay, ydot=-lambda y.
- **diffusion-result**: Immediately after boxed 2D=sum_i v_i^2 rbar_i. [Projected diffusion, SI S14-S15](../../assets/papers/burak-fiete-2012-persistent-activity-si.pdf#page=3). This is the exact general one-dimensional result.
- **symmetric-result**: After boxed symmetric-weight diffusion formula and discrepancy sentence. [Symmetric-weight formula, SI S18](../../assets/papers/burak-fiete-2012-persistent-activity-si.pdf#page=4). Use SI as primary. Footnote can also link main Eq. 2 for the actual printed difference.
- **long-time**: After the Fokker-Planck result or the wrapped-Gaussian discussion. [Density evolution and wrapping, SI S28-S31](../../assets/papers/burak-fiete-2012-persistent-activity-si.pdf#page=7). For the wrapping sentence itself prefer a second link to si-wrapped; pi^2/3 is derived in the guide.
- **varying-diffusion**: After Var(theta)=2D(Theta)t+D(Theta)Ddoubleprime(Theta)t^2. [State-dependent diffusion, SI S33-S37](../../assets/papers/burak-fiete-2012-persistent-activity-si.pdf#page=8). The derivation is expanded in the guide, ending at the exact source expression S37.
- **systematic-drift**: After the Ito/Stratonovich explanation and comparison of scales. [Systematic drift, SI S19-S20](../../assets/papers/burak-fiete-2012-persistent-activity-si.pdf#page=5). Source explicitly warns the exact drift needs microscopic equations.
- **correlated-noise**: After the general covariance extension and conjecture limitation. [Scope of correlated-noise extensions, Discussion p. 5](../../assets/papers/burak-fiete-2012-persistent-activity.pdf#page=5). Do not make this link appear to prove 2D=v^T Q v or a universal correlated-noise inequality.

## Every existing footnote

| Footnote | Exact source locations | Reader/source distinction |
|---|---|---|
| `p1-model` | [Materials and Methods, Neural Network, Eqs. 7-9, PDF p. 5](../../assets/papers/burak-fiete-2012-persistent-activity.pdf#page=5); [Eq. 1 and instantaneous attractor state definition, PDF p. 2](../../assets/papers/burak-fiete-2012-persistent-activity.pdf#page=2) | Count-process form, conditional Poisson moments, convolution sum and units are expanded teaching notation. Eqs. 7-9 and Eq. 1 are the exact source equations. |
| `p1-weak` | [Weak Fluctuations, Eqs. 10-11 and following paragraph, PDF p. 5](../../assets/papers/burak-fiete-2012-persistent-activity.pdf#page=5); [Weak Fluctuations continuation, large N and leading order assumptions, PDF p. 6](../../assets/papers/burak-fiete-2012-persistent-activity.pdf#page=6); [Section I, S2-S5 and Gaussian-limit paragraph, PDF p. 2](../../assets/papers/burak-fiete-2012-persistent-activity-si.pdf#page=2) | Brownian increments dB and dM are guide rewrites of jump counts and Gaussian white noise. The source explicitly puts the weak-fluctuation condition on total inputs g. |
| `p1-large` | [Section I, equivalent sub-populations and weight scaling S1, PDF p. 1](../../assets/papers/burak-fiete-2012-persistent-activity-si.pdf#page=1); [Section I, S2-S5 and Gaussian-limit paragraph, PDF p. 2](../../assets/papers/burak-fiete-2012-persistent-activity-si.pdf#page=2); [Section I, ring label density and scaling S6, PDF p. 2](../../assets/papers/burak-fiete-2012-persistent-activity-si.pdf#page=2) | S1 is PDF p. 1; S2-S6 are PDF p. 2. Large population scaling is directly supported. |
| `p1-projection` | [Section II, linearization S7-S10, PDF p. 3](../../assets/papers/burak-fiete-2012-persistent-activity-si.pdf#page=3); [Right zero mode S11, PDF p. 3](../../assets/papers/burak-fiete-2012-persistent-activity-si.pdf#page=3); [Nonsymmetric K paragraph; left mode S12 and normalization S13, PDF p. 3](../../assets/papers/burak-fiete-2012-persistent-activity-si.pdf#page=3); [Projected surviving displacement and diffusion S14-S15, PDF p. 3](../../assets/papers/burak-fiete-2012-persistent-activity-si.pdf#page=3) | Every cited S7-S15 is on SI PDF p. 3, not spread across pp. 3-4. The stable-mode orthogonality proof and 2D tilted decay example are guide teaching expansions. SI p. 4 starts the symmetric-weight specialization. |
| `p1-multid` | [Generalization to a multi-dimensional attractor, S21, PDF p. 5](../../assets/papers/burak-fiete-2012-persistent-activity-si.pdf#page=5); [Multi-dimensional tangents, conjugate left modes and covariance, S22-S27, PDF p. 6](../../assets/papers/burak-fiete-2012-persistent-activity-si.pdf#page=6) | S21 is on SI PDF p. 5; S22-S27 are on p. 6. The guide uses S21-S24; S25-S27 are the symmetric-weight extension. |
| `p1-symmetric` | [Symmetric W derivation, S16-S18, PDF p. 4](../../assets/papers/burak-fiete-2012-persistent-activity-si.pdf#page=4); [Eq. 2, symmetric weight diffusion expression as printed, PDF p. 2](../../assets/papers/burak-fiete-2012-persistent-activity.pdf#page=2) | SI S16-S18 are all on PDF p. 4. Link S18 as the primary formula and main Eq. 2 as the printed comparison, keeping the source-discrepancy note. |
| `p1-two` | [Fig. 2 caption, including wrapped error convention, transfer functions and two-neuron coordinate, PDF p. 3](../../assets/papers/burak-fiete-2012-persistent-activity.pdf#page=3); [Network Simulations, mutual-inhibition paragraph, PDF p. 6](../../assets/papers/burak-fiete-2012-persistent-activity.pdf#page=6) | Main Fig. 2E-G is PDF p. 3; method paragraph is p. 6, right column. The guide fixed points and u/v calculation are derived using theta=s1-s2; the figure caption only says a firing-rate difference represents memory. Keep the coordinate rescaling explicit. |
| `p1-fp` | [Section III, assumptions for diffusion along attractor, PDF p. 6](../../assets/papers/burak-fiete-2012-persistent-activity-si.pdf#page=6); [Zero drift Fokker-Planck equation and point initial condition, S28-S29, PDF p. 7](../../assets/papers/burak-fiete-2012-persistent-activity-si.pdf#page=7); [Unbounded constant diffusion solution and variance, S30, PDF p. 7](../../assets/papers/burak-fiete-2012-persistent-activity-si.pdf#page=7); [Periodic state, uniform limit and wrapped Gaussian, S31, PDF p. 7](../../assets/papers/burak-fiete-2012-persistent-activity-si.pdf#page=7); [Wrapped variance convention and integral, S32, PDF p. 8](../../assets/papers/burak-fiete-2012-persistent-activity-si.pdf#page=8) | Section III begins on SI PDF p. 6. S28-S31 are p. 7; S32 p. 8. Test-function derivation, twice integrating by parts, and explicit pi^2/3 limit are guide reconstructions from these results. |
| `p1-variable` | [State-dependent diffusion, Ito convention and short-time expansion S33-S37, PDF p. 8](../../assets/papers/burak-fiete-2012-persistent-activity-si.pdf#page=8) | S33-S37 all appear on SI PDF p. 8. Moment identities and generator calculation are guide derivation steps supporting S37. |
| `p1-excitation` | [Mutual excitation weights, states, displayed diffusion and variance, S38-S41, PDF p. 9](../../assets/papers/burak-fiete-2012-persistent-activity-si.pdf#page=9); [Fig. S1A-B and full caption, PDF p. 10](../../assets/papers/burak-fiete-2012-persistent-activity-si.pdf#page=10) | Example heading begins at bottom of SI p. 8; S38-S41 are p. 9 and Fig. S1 p. 10. Guide projection identifies an internal factor-two inconsistency in S40 vs S41, not an author-confirmed erratum. |
| `p1-systematic` | [Systematic drift discussion, nonlinear noise coupling and need for microscopic treatment, PDF p. 4](../../assets/papers/burak-fiete-2012-persistent-activity-si.pdf#page=4); [Microscopic master equation, S19-S20, drift scaling and tuning assumption, PDF p. 5](../../assets/papers/burak-fiete-2012-persistent-activity-si.pdf#page=5) | Systematic drift prose starts on SI p. 4; S19-S20, scale comparison and final zero-drift tuning assumption are p. 5. |
| `p1-correlation` | [Discussion, paragraph beginning Our spiking model for single neurons is quite simple, PDF p. 5](../../assets/papers/burak-fiete-2012-persistent-activity.pdf#page=5); [Section II, linearization S7-S10, PDF p. 3](../../assets/papers/burak-fiete-2012-persistent-activity-si.pdf#page=3); [Projected surviving displacement and diffusion S14-S15, PDF p. 3](../../assets/papers/burak-fiete-2012-persistent-activity-si.pdf#page=3) | Main Discussion PDF p. 5 left column, paragraph beginning Our spiking model for single neurons is quite simple. General 2D=v^T Q v is a guide linear-algebra extension of S14-S15, not a displayed paper theorem. Heterogeneous independent Poisson intensities are already allowed by S10/S15; arbitrary correlated intensities need a new joint likelihood. |
| `p1-fig1` | [Fig. 1A-B and full caption, PDF p. 2](../../assets/papers/burak-fiete-2012-persistent-activity.pdf#page=2); [Paragraph beginning In what follows, and Fig. 1A caption, PDF p. 2](../../assets/papers/burak-fiete-2012-persistent-activity.pdf#page=2) | Main PDF p. 2 Fig. 1A gives flow-defined projection; 1B shows state diffusion plus finite-spike inference error. Generic guide drawings should be labelled as reconstructions. |
| `p1-fig2` | [Fig. 2A-G and full caption, PDF p. 3](../../assets/papers/burak-fiete-2012-persistent-activity.pdf#page=3); [Network Simulations, ring-attractor paragraph, PDF p. 6](../../assets/papers/burak-fiete-2012-persistent-activity.pdf#page=6); [Network Simulations, mutual-inhibition paragraph, PDF p. 6](../../assets/papers/burak-fiete-2012-persistent-activity.pdf#page=6); [Wrapped variance convention and integral, S32, PDF p. 8](../../assets/papers/burak-fiete-2012-persistent-activity-si.pdf#page=8) | Main PDF p. 3 full figure/caption; ring simulation p. 6 left column; mutual inhibition p. 6 right column. Long-time ring prediction explicitly uses SI S32, p. 8. |

## Locator rectangles and evidence

Coordinates are PDF points from the top left. The JSON contains full extracted evidence inside each rectangle, a stable page fragment, and an optional viewer-dependent zoom fragment. Equation labels and paragraph openings are the authoritative locators.

### main-model
main PDF p. 5: Materials and Methods, Neural Network, Eqs. 7-9. Rectangle: `[295, 397, 543, 566]`.

### main-steady-state
main PDF p. 2: Eq. 1 and instantaneous attractor state definition. Rectangle: `[37, 85, 285, 299]`.

### main-flow-definition
main PDF p. 2: Paragraph beginning In what follows, and Fig. 1A caption. Rectangle: `[37, 216, 285, 298]`.

### main-diffusion-scope
main PDF p. 2: Diffusive Drift due to Ongoing Neural Noise, opening paragraph. Rectangle: `[37, 308, 285, 460]`.

### main-weak
main PDF p. 5: Weak Fluctuations, Eqs. 10-11 and following paragraph. Rectangle: `[295, 575, 543, 688]`.

### main-large
main PDF p. 6: Weak Fluctuations continuation, large N and leading order assumptions. Rectangle: `[37, 47, 285, 118]`.

### main-eq2
main PDF p. 2: Eq. 2, symmetric weight diffusion expression as printed. Rectangle: `[354, 113, 543, 165]`.
Numerator visibly has no square on d gbar_i / d theta. SI S18 and the guide derivation contain the square. Do not present an author-confirmed correction.

### main-diffusion-context
main PDF p. 2: Paragraphs after Eq. 2, scaling and simulation tests. Rectangle: `[295, 165, 543, 528]`.

### main-fig1
main PDF p. 2: Fig. 1A-B and full caption. Rectangle: `[37, 464, 543, 729]`.

### main-fig2
main PDF p. 3: Fig. 2A-G and full caption. Rectangle: `[37, 43, 285, 454]`.

### main-fig2-caption
main PDF p. 3: Fig. 2 caption, including wrapped error convention, transfer functions and two-neuron coordinate. Rectangle: `[37, 230, 285, 454]`.

### main-ring-sim
main PDF p. 6: Network Simulations, ring-attractor paragraph. Rectangle: `[37, 128, 285, 290]`.

### main-two-sim
main PDF p. 6: Network Simulations, mutual-inhibition paragraph. Rectangle: `[295, 47, 544, 210]`.
Figure 2 caption describes a firing-rate difference; guide theta=s1-s2 is an activation difference and differs by tau from a rate difference.

### main-correlations
main PDF p. 5: Discussion, paragraph beginning Our spiking model for single neurons is quite simple. Rectangle: `[37, 167, 285, 378]`.
Correlated spike models are proposed extensions and described as conjectures remaining to be tested, not a proved general correlated-noise inequality.

### main-subpoisson-limit
main PDF p. 5: Discussion, paragraph beginning The quantitative expression for the diffusion rate derived here. Rectangle: `[37, 638, 285, 729]`.
Explicit warning that Eq. 2 cannot directly apply to significantly sub-Poisson oculomotor spikes; paragraph continues top of right column.

### si-population
si PDF p. 1: Section I, equivalent sub-populations and weight scaling S1. Rectangle: `[71, 573, 540, 743]`.

### si-gaussian
si PDF p. 2: Section I, S2-S5 and Gaussian-limit paragraph. Rectangle: `[71, 153, 540, 557]`.

### si-ring-large
si PDF p. 2: Section I, ring label density and scaling S6. Rectangle: `[71, 564, 540, 740]`.

### si-linearization
si PDF p. 3: Section II, linearization S7-S10. Rectangle: `[71, 107, 540, 337]`.

### si-tangent
si PDF p. 3: Right zero mode S11. Rectangle: `[71, 353, 540, 425]`.

### si-left
si PDF p. 3: Nonsymmetric K paragraph; left mode S12 and normalization S13. Rectangle: `[71, 434, 540, 594]`.

### si-project
si PDF p. 3: Projected surviving displacement and diffusion S14-S15. Rectangle: `[71, 601, 540, 741]`.

### si-symmetric
si PDF p. 4: Symmetric W derivation, S16-S18. Rectangle: `[71, 73, 540, 360]`.
S18 has (d gbar_i/d theta)^2 in the numerator. The text after S18 refers to main Eq. 3, although main diffusion formula is Eq. 2; cite equation labels directly.

### si-drift-limit
si PDF p. 4: Systematic drift discussion, nonlinear noise coupling and need for microscopic treatment. Rectangle: `[71, 387, 540, 739]`.

### si-drift
si PDF p. 5: Microscopic master equation, S19-S20, drift scaling and tuning assumption. Rectangle: `[71, 73, 540, 586]`.

### si-multid-start
si PDF p. 5: Generalization to a multi-dimensional attractor, S21. Rectangle: `[71, 617, 540, 741]`.

### si-multid
si PDF p. 6: Multi-dimensional tangents, conjugate left modes and covariance, S22-S27. Rectangle: `[71, 73, 540, 549]`.

### si-fp-intro
si PDF p. 6: Section III, assumptions for diffusion along attractor. Rectangle: `[71, 570, 540, 739]`.

### si-fp
si PDF p. 7: Zero drift Fokker-Planck equation and point initial condition, S28-S29. Rectangle: `[71, 73, 540, 305]`.

### si-gaussian-line
si PDF p. 7: Unbounded constant diffusion solution and variance, S30. Rectangle: `[71, 354, 540, 480]`.

### si-wrapped
si PDF p. 7: Periodic state, uniform limit and wrapped Gaussian, S31. Rectangle: `[71, 508, 540, 739]`.

### si-wrapped-moment
si PDF p. 8: Wrapped variance convention and integral, S32. Rectangle: `[71, 73, 540, 145]`.

### si-variable
si PDF p. 8: State-dependent diffusion, Ito convention and short-time expansion S33-S37. Rectangle: `[71, 164, 540, 645]`.

### si-excitation
si PDF p. 9: Mutual excitation weights, states, displayed diffusion and variance, S38-S41. Rectangle: `[71, 73, 540, 479]`.
S40 displays D=theta/(2 tau) but S41 displays variance=Theta t/(2 tau). With Var=2Dt, direct projection of S39 gives D=theta/(4 tau). The guide labels this discrepancy openly.

### si-excitation-fig
si PDF p. 10: Fig. S1A-B and full caption. Rectangle: `[71, 70, 540, 330]`.
Caption specifies initial Theta=100 and 4000 random trials. The supplied caption does not specify tau, so do not infer a numerical slope from axes alone.

### si-gaussian-generalization
si PDF p. 19: Section VII, White Gaussian noise, S93-S95. Rectangle: `[71, 73, 540, 497]`.
This is an alternative additive Gaussian model. It does not establish the arbitrary Q correlated-noise case.

## Suggested illustrations

- **synaptic-feedback**: Original schematic: each spike adds one activation unit, exponential decay between spikes, weighted input determines rate, rates determine new random spikes. Use a small impulse-response trace beside the feedback loop. Connects the short spike to long synaptic state and shows where noise enters.
- **left-vector-projection**: Original diagram: attractor tangent u, tilted decaying path, actual surviving displacement and perpendicular comparison. Label v^T delta s as the final coordinate change. Directly explains why a left vector is required. Keep the guide x/y example label.
- **wrapped-error**: Original two-panel diagram: a noisy coordinate spreading on a line and the same coordinate wrapped on a ring; error distribution becomes uniform on [-pi,pi). Show 2Dt at short times and pi^2/3 as the circular-error plateau. Prevents reading the plateau as noise stopping.

## Check scope and timing

Chapter, original source PDFs, and existing extracted text read. Main PDF p. 2 and SI pp. 3, 4 and 9 rendered and inspected to verify the two formula differences. Exact PDF text blocks and source hashes saved in `pdf-block-evidence.json`. No whole-book pass, external link resolution, or publishing check.

Task start: 2026-10-24T18:06:16.7630300+03:00. Checkpoint: 2026-10-24T18:09:25.153251+03:00. Awake time unverified; sleep/resume logs were not inspected. Token stats unavailable.

## Direct inline targets with focus positions

| Target | Exact source location | Rectangle in PDF points | Direct link |
|---|---|---|---|
| model-and-spikes | Materials and Methods, Neural Network, Eqs. 7-9, PDF p. 5 | `[295, 397, 543, 566]` | [Paper model, Eqs. 7-9](../../assets/papers/burak-fiete-2012-persistent-activity.pdf#page=5&zoom=125,0,397) |
| weak-noise | Weak Fluctuations, Eqs. 10-11 and following paragraph, PDF p. 5 | `[295, 575, 543, 688]` | [Weak fluctuation limit, Eqs. 10-11](../../assets/papers/burak-fiete-2012-persistent-activity.pdf#page=5&zoom=125,0,575) |
| left-projection | Nonsymmetric K paragraph; left mode S12 and normalization S13, PDF p. 3 | `[71, 434, 540, 594]` | [Left mode and normalization, SI S12-S13](../../assets/papers/burak-fiete-2012-persistent-activity-si.pdf#page=3&zoom=125,0,434) |
| tilted-example | Projected surviving displacement and diffusion S14-S15, PDF p. 3 | `[71, 601, 540, 741]` | [Projection argument, SI S12-S15](../../assets/papers/burak-fiete-2012-persistent-activity-si.pdf#page=3&zoom=125,0,601) |
| diffusion-result | Projected surviving displacement and diffusion S14-S15, PDF p. 3 | `[71, 601, 540, 741]` | [Projected diffusion, SI S14-S15](../../assets/papers/burak-fiete-2012-persistent-activity-si.pdf#page=3&zoom=125,0,601) |
| symmetric-result | Symmetric W derivation, S16-S18, PDF p. 4 | `[71, 73, 540, 360]` | [Symmetric-weight formula, SI S18](../../assets/papers/burak-fiete-2012-persistent-activity-si.pdf#page=4&zoom=125,0,73) |
| long-time | Zero drift Fokker-Planck equation and point initial condition, S28-S29, PDF p. 7 | `[71, 73, 540, 305]` | [Density evolution and wrapping, SI S28-S31](../../assets/papers/burak-fiete-2012-persistent-activity-si.pdf#page=7&zoom=125,0,73) |
| varying-diffusion | State-dependent diffusion, Ito convention and short-time expansion S33-S37, PDF p. 8 | `[71, 164, 540, 645]` | [State-dependent diffusion, SI S33-S37](../../assets/papers/burak-fiete-2012-persistent-activity-si.pdf#page=8&zoom=125,0,164) |
| systematic-drift | Microscopic master equation, S19-S20, drift scaling and tuning assumption, PDF p. 5 | `[71, 73, 540, 586]` | [Systematic drift, SI S19-S20](../../assets/papers/burak-fiete-2012-persistent-activity-si.pdf#page=5&zoom=125,0,73) |
| correlated-noise | Discussion, paragraph beginning Our spiking model for single neurons is quite simple, PDF p. 5 | `[37, 167, 285, 378]` | [Scope of correlated-noise extensions, Discussion p. 5](../../assets/papers/burak-fiete-2012-persistent-activity.pdf#page=5&zoom=125,0,167) |

## All footnote call sites

- Chapter line 3: `p1-model`. Exact PDF targets: Materials and Methods, Neural Network, Eqs. 7-9, PDF p. 5; Eq. 1 and instantaneous attractor state definition, PDF p. 2.
- Chapter line 30: `p1-model`. Exact PDF targets: Materials and Methods, Neural Network, Eqs. 7-9, PDF p. 5; Eq. 1 and instantaneous attractor state definition, PDF p. 2.
- Chapter line 58: `p1-weak`. Exact PDF targets: Weak Fluctuations, Eqs. 10-11 and following paragraph, PDF p. 5; Weak Fluctuations continuation, large N and leading order assumptions, PDF p. 6; Section I, S2-S5 and Gaussian-limit paragraph, PDF p. 2.
- Chapter line 60: `p1-large`. Exact PDF targets: Section I, equivalent sub-populations and weight scaling S1, PDF p. 1; Section I, S2-S5 and Gaussian-limit paragraph, PDF p. 2; Section I, ring label density and scaling S6, PDF p. 2.
- Chapter line 93: `p1-projection`. Exact PDF targets: Section II, linearization S7-S10, PDF p. 3; Right zero mode S11, PDF p. 3; Nonsymmetric K paragraph; left mode S12 and normalization S13, PDF p. 3; Projected surviving displacement and diffusion S14-S15, PDF p. 3.
- Chapter line 179: `p1-projection`. Exact PDF targets: Section II, linearization S7-S10, PDF p. 3; Right zero mode S11, PDF p. 3; Nonsymmetric K paragraph; left mode S12 and normalization S13, PDF p. 3; Projected surviving displacement and diffusion S14-S15, PDF p. 3.
- Chapter line 189: `p1-multid`. Exact PDF targets: Generalization to a multi-dimensional attractor, S21, PDF p. 5; Multi-dimensional tangents, conjugate left modes and covariance, S22-S27, PDF p. 6.
- Chapter line 226: `p1-symmetric`. Exact PDF targets: Symmetric W derivation, S16-S18, PDF p. 4; Eq. 2, symmetric weight diffusion expression as printed, PDF p. 2.
- Chapter line 241: `p1-two`. Exact PDF targets: Fig. 2 caption, including wrapped error convention, transfer functions and two-neuron coordinate, PDF p. 3; Network Simulations, mutual-inhibition paragraph, PDF p. 6.
- Chapter line 286: `p1-fp`. Exact PDF targets: Section III, assumptions for diffusion along attractor, PDF p. 6; Zero drift Fokker-Planck equation and point initial condition, S28-S29, PDF p. 7; Unbounded constant diffusion solution and variance, S30, PDF p. 7; Periodic state, uniform limit and wrapped Gaussian, S31, PDF p. 7; Wrapped variance convention and integral, S32, PDF p. 8.
- Chapter line 303: `p1-variable`. Exact PDF targets: State-dependent diffusion, Ito convention and short-time expansion S33-S37, PDF p. 8.
- Chapter line 312: `p1-excitation`. Exact PDF targets: Mutual excitation weights, states, displayed diffusion and variance, S38-S41, PDF p. 9; Fig. S1A-B and full caption, PDF p. 10.
- Chapter line 318: `p1-systematic`. Exact PDF targets: Systematic drift discussion, nonlinear noise coupling and need for microscopic treatment, PDF p. 4; Microscopic master equation, S19-S20, drift scaling and tuning assumption, PDF p. 5.
- Chapter line 324: `p1-correlation`. Exact PDF targets: Discussion, paragraph beginning Our spiking model for single neurons is quite simple, PDF p. 5; Section II, linearization S7-S10, PDF p. 3; Projected surviving displacement and diffusion S14-S15, PDF p. 3.
- Chapter line 330: `p1-fig1`. Exact PDF targets: Fig. 1A-B and full caption, PDF p. 2; Paragraph beginning In what follows, and Fig. 1A caption, PDF p. 2.
- Chapter line 336: `p1-fig2`. Exact PDF targets: Fig. 2A-G and full caption, PDF p. 3; Network Simulations, ring-attractor paragraph, PDF p. 6; Network Simulations, mutual-inhibition paragraph, PDF p. 6; Wrapped variance convention and integral, S32, PDF p. 8.

Offsets supplement page and equation/paragraph labels. Actual PDF viewer support must be checked during integration. No copied paper passages are proposed for reader text.

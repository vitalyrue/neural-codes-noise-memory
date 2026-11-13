# Exam review: connect mechanisms, measurements and results {#ch:EXAM-REVIEW}

Start by recalling **what physical system each paper studies, what changes inside it, and what the measurements can establish**. Then use a formula to support that explanation. This page is a return point after studying the guide; you do not need to master it before Part I.

For a quick review:

1. Read the three reasoning chains below. Try to explain each one without notation.
2. Follow the paper where your explanation breaks down. Its core results stay visible; supporting results open on request.
3. Read the paper's **shared notation** first. Each formula then lists only its extra symbols and notes, followed by **Paper location** and **Guide location**. PDF page means the page counted by the PDF viewer. Supporting Information is abbreviated SI.

The central and supporting labels describe each result's role in the paper, rather than predict an exam syllabus. A formula marked **guide-derived** has its own derivation here; its paper link gives the source context and does not claim that the paper prints the same equation. The [mathematical-tools chapter](ch-mathematical-tools.html) supplies the longer introductions.

## Three questions organize the three papers {#sec:EXAM-MAP}

<div class="table-responsive">

{{block:tbl:EXAM-MAP}}

</div>

## Feedback sustains activity while noisy spikes move the remembered value {#sec:EXAM-MEMORY}

**Burak and Fiete (2012): continuous memory in a modeled neural circuit.** The stored value is a coordinate of a persistent neural activity pattern. Fixed recurrent connections sustain that pattern. Random spikes disturb it; the circuit removes some disturbances, while others leave the value displaced. The derivation follows that surviving displacement and asks how its variance relates to how clearly the spikes distinguish nearby values.

**Recall the chain:** feedback mechanism (M1) → surviving displacement (M3) → spike information (M7) → diffusion bound and equality (M8–M9) → readout (M13). Long-delay storage error and total recall error are M6 and M14 in the additional results below.

Primes on rate and input tuning curves denote derivatives with respect to the represented value. In M9, $\phi'$ differentiates the transfer function with respect to its input. The shared key below defines recurring symbols; rows list only additions and exceptions. Diffusion and Fisher information are scalars in the main argument; M5 gives their matrix generalization for several stored coordinates.

<span id="notation-memory"></span>

**Shared memory notation.** These definitions apply to both memory tables. A row states any changed meaning or extra symbol.

- [$N$: number of neurons; $i,j$: neuron indices. $W_{ij}$ sends activation from cell $j$ to receiver $i$.]{.definition-explanation}
- [$\theta$: current represented coordinate; $\Theta$: its initial value; $\hat\theta$: an estimate from observations. Their units are the chosen coordinate units, for example radians.]{.definition-explanation}
- [$t$: time; $h$: short counting window; $T$: storage delay; $L$: observation duration after the recall cue (all seconds). The source writes readout duration as $\Delta T$.]{.definition-explanation}
- [$s_i$: outgoing activation of cell $i$, dimensionless with one unit added per spike. A bar, as in $\bar s_i$, denotes a noise-free steady value.]{.definition-explanation}
- [$r_i,\bar r_i$: firing rate and steady firing rate (spikes/s); $\bar r_i'=d\bar r_i/d\theta$: tuning slope (rate per coordinate unit).]{.definition-explanation}
- [$g_i$: total input; $b_i$: constant bias (same input units). $W$ is an $N\times N$ matrix in input units per activation unit. $\phi(g)$ converts input into rate; $\phi'$ differentiates with respect to input.]{.definition-explanation}
- [$\tau$: synaptic activation decay time (s).]{.definition-explanation}
- [$D$: scalar diffusion coefficient (coordinate units squared/s); $2D$ is the local displacement-variance growth rate. $J$: scalar information per second about the coordinate (inverse coordinate units squared/s). M5 and M11 use matrix versions.]{.definition-explanation}
- [$K$: $N\times N$ linear response matrix (s$^{-1}$). $\mathbf u=\partial\bar{\mathbf s}/\partial\theta$: tangent $N$-vector (activation/coordinate). $\mathbf v$: normalized left zero vector; $v_i$ measures the retained coordinate shift per activation unit from cell $i$.]{.definition-explanation}
- [$V$ with a subscript denotes error variance (coordinate units squared); the subscript identifies the estimate being assessed.]{.definition-explanation}

<div class="table-responsive">

{{block:tbl:EXAM-MEMORY-CORE}}

</div>

<details class="publisher-long-content publisher-long-note">
<summary>More memory results: count noise, symmetry, multiple coordinates, storage and partial readout, scaling, and extensions</summary>
<div class="publisher-fold-body">

<div class="table-responsive">

{{block:tbl:EXAM-MEMORY-SUPPORT}}

</div>

</div>
</details>

<details class="publisher-long-content publisher-long-note">
<summary>Recall check: why can persistent activity still lose the original value?</summary>
<div class="publisher-fold-body">

The circuit can restore the shape of its activity pattern without restoring its original coordinate along the family of patterns. The left projection weights measure the displacement that remains. Fisher information concerns reading the present value from spikes; diffusion concerns how that present value has departed from the original cue. A decoder can therefore read the present state precisely while the original memory is already inaccurate.

</div>
</details>

## Covariance identifies a shared component of eye movement {#sec:EXAM-EYE}

**Ben-Shushan et al. (2022): horizontal eye drift during fixation in macaque monkeys.** A recorded motor neuron's spikes are converted into a prediction in degrees. Comparing that prediction with actual displacement asks how much variation they share. A second argument asks whether independent motor noise, after muscle filtering, could explain the measured mean squared displacement (MSD).

**Recall the chain:** calibrate the spike-to-movement filter (E1) → estimate the shared variance fraction (E3) → compare filtered stationary noise with an accumulating command (E5–E6). E6 is a simplified guide calculation, not the paper's full circuit model. The separate population bound (E2) challenges independent motor noise alone; it is in the additional results below.

The time lag in an MSD is the separation between two readings. The eye response time in E6 is different from the synaptic decay time in the 2012 theory. Measurement correction and parameter scaling remain available below the core argument.

<span id="notation-eye"></span>

**Shared eye-motion notation.** These definitions apply to both eye tables. Filter normalization and response times are specified in the rows that use them.

- [$t$: time; $\ell$: separation between two readings; $u$: integration lag (all seconds). A dot differentiates with respect to time.]{.definition-explanation}
- [$E$: true eye angle; $\widehat E$: spike-predicted angle; $E_{\rm obs}$: measured angle (degrees).]{.definition-explanation}
- [$M(\ell)=\mathbb E[(E(t+\ell)-E(t))^2]$: mean squared displacement (MSD), in degrees$^2$. $C_E(\ell)$: covariance of centered eye position at lag $\ell$, also in degrees$^2$.]{.definition-explanation}
- [$D$: temporal angle diffusion coefficient (degrees$^2$/s). It is unrelated to place-field dimension $d$.]{.definition-explanation}
- [$h$: causal response kernel. Its units depend on the input normalization in E1 or E5; it is not the spatial input map in the place-field model.]{.definition-explanation}
- [$N_m$: number of contributing motor neurons; $i$: motor-neuron index; $R_i$: correlation between cell $i$'s displacement prediction and measured displacement over the same 350 ms intervals, dimensionless. $R$ omits the cell index.]{.definition-explanation}

<div class="table-responsive">

{{block:tbl:EXAM-EYE-CORE}}

</div>

<details class="publisher-long-content publisher-long-note">
<summary>More eye results: the independent-noise bound, measurement error, and parameter scaling</summary>
<div class="publisher-fold-body">

<div class="table-responsive">

{{block:tbl:EXAM-EYE-SUPPORT}}

</div>

</div>
</details>

<details class="publisher-long-content publisher-long-note">
<summary>Recall check: why does weak single-cell correlation not imply a small shared contribution?</summary>
<div class="publisher-fold-body">

Private spike noise can make one cell's prediction much noisier than the movement. Correlation divides covariance by both signals' standard deviations, so the noisy predictor lowers it. The calibrated shared-fraction estimate instead divides covariance by measured displacement variance. This interpretation needs the gain and noise assumptions; locating the source upstream also needs a biological premise about private motor-neuron variability.

</div>
</details>

## Thresholded Gaussian input links spatial structure to place-field statistics {#sec:EXAM-PLACE}

**Mainali, Azeredo da Silveira, and Burak (2025): place fields in rodent and bat recordings, compared with a spatial statistical model.** A cell's input is a correlated Gaussian map over position. Once drawn, that map stays fixed during traversal. Thresholding it makes connected active regions. Crossings determine 1D counts and mean lengths; isolated high peaks supply the limiting size laws in different dimensions. Slices and holes test spatial structure beyond a size histogram.

**Recall the chain:** input map and threshold (P1) → exact crossings and mean-length constraints (P3–P4) → high-threshold size law (P6). Slice and topology tests (P9 and P11) probe spatial structure further; they are in the additional results below.

The map varies over **space**, unlike the memory coordinate that diffuses over **time**. The local distance scale is written as $\ell_c$ here; the place-field chapters call the same scale $\sigma$. It is distinct from input standard deviation $\sigma_0$.

<span id="notation-place"></span>

**Shared place-field notation.** These definitions apply to both place-field tables. The independent variable is position, rather than time.

- [$x,y$: spatial positions, scalar on a track or vectors in $\mathbb R^d$ (distance units); $d$: spatial dimension, 1, 2 or 3.]{.definition-explanation}
- [$h(x)$: fixed Gaussian input map; $\mu$: constant input mean; $\sigma_0$: input standard deviation; $h_{\rm th}$: absolute firing threshold (all in input units).]{.definition-explanation}
- [$z=(h-\mu)/\sigma_0$: normalized input; $q=(h_{\rm th}-\mu)/\sigma_0$: normalized threshold; $\epsilon$: peak excess above $q$ (all dimensionless).]{.definition-explanation}
- [$F$: firing rate (Hz); $a$: gain converting normalized excess into firing rate (Hz). It is not the eye model's tuning slope.]{.definition-explanation}
- [$C(x,y)$, or $C(y-x)$ for a stationary map: covariance of unnormalized input, in input units squared. It is not the eye model's shared displacement $C$. Spatial primes differentiate with respect to distance.]{.definition-explanation}
- [$\ell_c$: local distance scale, written $\sigma$ in the place-field chapters; distinct from input standard deviation $\sigma_0$.]{.definition-explanation}
- [$Q(q)=\Pr(Z>q)$ for a standard normal scalar $Z$: dimensionless Gaussian upper-tail probability. $\nu_+(q)$: upcrossing density (distance$^{-1}$).]{.definition-explanation}
- [$s$: complete-field size (length, area or volume, with distance$^d$ units); $S$: nonnegative cutoff in the same units.]{.definition-explanation}
- [$v_d$: dimensionless unit-ball volume, with $v_1=2$, $v_2=\pi$ and $v_3=4\pi/3$. $\beta$: size-law coefficient, in inverse distance squared in every dimension.]{.definition-explanation}

<div class="table-responsive">

{{block:tbl:EXAM-PLACE-CORE}}

</div>

<details class="publisher-long-content publisher-long-note">
<summary>More place-field results: wiring, counts and gaps, peaks, moments, slices, boundary slopes, and topology</summary>
<div class="publisher-fold-body">

<div class="table-responsive">

{{block:tbl:EXAM-PLACE-SUPPORT}}

</div>

</div>
</details>

<details class="publisher-long-content publisher-long-note">
<summary>Recall check: why do exact crossing counts not make the size law exact?</summary>
<div class="publisher-fold-body">

The crossing calculation averages height and slope at threshold under the smooth stationary Gaussian model. It does not require high threshold. The universal size argument additionally replaces a typical field by an isolated nearly quadratic high peak and uses the limiting peak-excess distribution. At finite threshold a field can have several peaks or an irregular shape. The extra approximation has to be checked, even when the crossing formula is exact.

</div>
</details>

## Different quantities answer different questions {#sec:EXAM-DISTINCTIONS}

Before giving a result, check which of these questions it answers:

- **Activity, stored value or estimate?** Neural activations form the circuit state; a coordinate identifies the represented value; a decoder computes an estimate from observations. Persistent activity alone does not guarantee accurate memory. [M1](#result-m1), [M3](#result-m3), [M13](#result-m13).
- **Present-state precision or storage loss?** Fisher information measures a local distinction in present spike probabilities. Diffusion measures accumulated movement of the stored value. [M7–M8](#result-m7).
- **Correlation or a causal variance fraction?** A shared-fraction interpretation needs calibrated gains and a noise model. Correlation alone does not supply it. [E3](#result-e3).
- **Internal command or observed movement?** Muscle response and feedback change how internal fluctuations appear in eye motion. [E5–E6](#result-e5).
- **Temporal noise or a fixed spatial map?** The 2012 and 2022 arguments concern evolving signals. The 2025 spatial randomness describes an ensemble of possible maps, not fresh input at each revisit. [M6](#result-m6), [P1](#result-p1).
- **Exact model identity or limiting approximation?** Gaussian crossing and topology formulas have their stated exact model scope. Universal field-size laws need a high threshold; nearly independent field locations need sufficiently decaying spatial dependence as well. [P3](#result-p3), [P6](#result-p6), [P4 and its supporting rare-event result](#result-p4).

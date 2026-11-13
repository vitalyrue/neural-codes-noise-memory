# High peaks explain size laws across dimensions {#ch:PLACE-SIZES}

[Knowing the average field length does not tell us how often very small or very large fields occur. Why should the same spatial model give one size distribution on a track, another in an arena, and a third in a room?]{.key-statement} The next step is to find the shape of a typical field when only unusually high input peaks rise above the threshold.

Near such a peak, the smooth input is approximately a downward parabola. Its height above the threshold sets a radius, and converting that radius into length, area or volume gives the different size laws. Cuts through a map test its spatial structure, and slopes at field edges provide a separate check on the predicted field widths. [The size laws use a high threshold approximation; the boundary-slope law has a separate exact derivation under the smooth stationary Gaussian assumptions.]{.key-statement}

We keep the earlier notation: $z(x)$ is the spatial input normalized to variance one, $q$ is its threshold, $\sigma$ is its local distance scale, and $a$ converts positive excess input into firing rate. The number of spatial dimensions is $d$. The firing rule remains $F(x)=a[z(x)-q]_+$, where $[u]_+=\max(u,0)$.

## Near a high peak, the input is nearly parabolic {#sec:PLACE-RARE-PEAKS}

The crossing calculation determines a mean length exactly, but it does not yet explain the shape of the length histogram. To obtain that distribution, we examine the small region around a peak that barely exceeds a high threshold.

The following is a teaching reconstruction of the high excursion argument in Methods S4, with algebraic corrections made explicit below. It assumes:

- a sufficiently smooth, stationary, isotropic, unit variance Gaussian field;
- an invertible covariance matrix for the relevant derivative variables;
- the limit $q\to\infty$;
- typical components counted once each, away from environment boundaries.

It is not a proof of the full excursion convergence theorem for every allowed covariance.[^p3-rare-source]

[The [**Hessian**]{.definition-term custom-style="Definition Term"} is the matrix $H$ of second spatial derivatives; its eigenvalues describe curvature along the principal directions.]{.definition-explanation} Isotropy and the definition of $\sigma$ imply

$$
\operatorname{Cov}(\partial_i\partial_j z,z)
=-\frac{\delta_{ij}}{\sigma^2}.
$$

Here $\delta_{ij}$ is one for equal indices and zero otherwise. For jointly Gaussian variables, conditioning $Y$ on a scalar $Z$ of variance one gives $\mathbb E[Y\mid Z=b]=\operatorname{Cov}(Y,Z)b$ when both means vanish. One way to see this is to write $Y=\operatorname{Cov}(Y,Z)Z+\epsilon$; the remainder has zero covariance with $Z$ and is therefore independent of it. Applying this to each Hessian entry gives

$$
\mathbb E[H\mid z=b]=-\frac{b}{\sigma^2}I.
$$

The conditional fluctuations around this mean have a variance that does not grow with $b$. For a high peak, the negative mean curvature is of order $q$, so its relative fluctuations become small. Conditioning the gradient to zero does not change this Gaussian conditional mean, because the gradient has zero covariance with both height and Hessian in a stationary isotropic field. Selecting an actual maximum also weights curvatures, but its leading high peak shape is the same.

Let the peak height be $q+\epsilon$, with $\epsilon>0$, and put the peak at the origin. The gradient there is zero. The Taylor expansion becomes, to leading order,

$$
z(x)-q\simeq\epsilon-\frac{q}{2\sigma^2}\|x\|^2.
$$

It is positive inside an approximately round region of radius

$$
r_*\simeq\sigma\sqrt{\frac{2\epsilon}{q}}.
$$

The remaining question is how $\epsilon$ is distributed when we select one high field at a time. In one dimension, the number of high maxima is asymptotically the number of upcrossings, proportional to $e^{-q^2/2}$. Therefore the fraction of peaks above $q$ that also exceed $q+\epsilon$ is approximately

$$
\frac{e^{-(q+\epsilon)^2/2}}{e^{-q^2/2}}
=e^{-q\epsilon-\epsilon^2/2}.
$$

Define $U=q\epsilon$. At fixed $u\ge0$ and as $q$ increases,

$$
\Pr(U>u)\simeq
e^{-u-u^2/(2q^2)}\longrightarrow e^{-u}.
$$

[Thus the scaled excess height approaches an exponential variable of mean one.]{.key-statement} In several dimensions, high peak counts have the additional leading factor $q^{d-1}$. Its ratio at $q+u/q$ and $q$ tends to one, so the same excess-height limit remains. The higher dimensional count factor will also follow from the [Euler characteristic calculation](ch-place-tests.html#sec-place-topology). A rigorous conclusion requires control of the remainder and of components containing multiple peaks, beyond this local argument.

In one dimension, the full field length is $s=2r_*$. Eliminating $\epsilon$ gives

$$
s\simeq\frac{2\sqrt2\sigma}{q}\sqrt U,
\qquad
\epsilon\simeq\frac{q s^2}{8\sigma^2}.
$$

This supplies two distinct predictions:

- [The length is a scaled square root of an exponential variable, giving a [**Rayleigh distribution**]{.definition-term custom-style="Definition Term"}.]{.definition-explanation}
- The peak firing rate is $a\epsilon$, so at fixed high $q$ it is proportional to $s^2$.

The exponent two concerns rate versus linear size. In three dimensions a suitable linear size is $s^{1/3}$ when $s$ denotes volume.

At moderate thresholds the omitted shape fluctuations matter. Figure 3C reports a rate versus length exponent of $1.42$ in the 200 m bat data and $1.46$ in finite threshold model simulations. Figure 3D reports $1.75$ versus $1.71$ using cube root of volume in 3D. These are compatible with a model that approaches exponent two only as the threshold becomes large; they are not measurements of the limiting exponent. Figure 5A–C illustrates the progression toward simpler, usually single peak fields as $q$ increases. Figure 4C tests this trend in the shorter bat tunnel.[^p3-shapes]

<details class="publisher-long-content publisher-source-figure">
<summary>Original paper figure: Mainali, Azeredo da Silveira, and Burak (2025), Figure 5</summary>
<div class="publisher-fold-body">

{{block:fig:PAPER-PLACE-5}}

</div>
</details>

## Geometry gives different size laws in each dimension {#sec:PLACE-SIZE-LAW}

A round region's radius and its volume have different units and different distributions. This geometric conversion explains why the model predicts different histograms in a track, an arena, and a room.

Let $v_d=\pi^{d/2}/\Gamma(1+d/2)$ be the volume of a unit ball in $d$ dimensions. For $d=1,2,3$, it is $2,\pi,4\pi/3$. [The symbol $\Gamma$ is the [**gamma function**]{.definition-term custom-style="Definition Term"}, defined for $t>0$ by $\Gamma(t)=\int_0^\infty u^{t-1}e^{-u}\,du$. It extends factorials: $\Gamma(n+1)=n!$.]{.definition-explanation}

Using the radius from the preceding section, the field size is

$$
s\simeq v_d\left(\frac{\sqrt2\sigma}{q}\right)^d U^{d/2},
\qquad
U=\beta s^{2/d},\qquad
\beta=\frac{q^2}{2\sigma^2v_d^{2/d}}.
$$

The same local radius gives a length, an area, or a volume depending on the dimension of the region.

<div class="figure-scroll">

{{block:fig:PLACE-SIZE-GEOMETRY}}

</div>

The round shape and exponential excess belong to the high-threshold limit, so they do not make every measured place field spherical.

Since the density of $U$ is $e^{-u}$ for $u>0$, changing variables gives

$$
\begin{aligned}
p_d(s)&=e^{-\beta s^{2/d}}\frac{d}{ds}(\beta s^{2/d})\\
&=\frac{2\beta}{d}s^{2/d-1}e^{-\beta s^{2/d}},\qquad s>0.
\end{aligned}
$$

This is the paper's Equation 1. The expression for $\beta$ above is its leading high threshold geometric scale, not an exact finite threshold identity. A finite threshold simulation can share the approximate shape while having a different fitted scale.[^p3-size-source]

The mean and its corresponding scale are

$$
\mu_s=\Gamma(1+d/2)\beta^{-d/2},\qquad
\beta=\left[\frac{\Gamma(1+d/2)}{\mu_s}\right]^{2/d}.
$$

::: {.publisher-clarification-note .publisher-fold-always title="Derivation: normalization and higher size moments"}

Normalization needs no special integral: $\int_0^\infty p_d(s)\,ds=\int_0^\infty e^{-u}\,du=1$. The same substitution supplies every positive moment,

$$
\mathbb E[s^k]
=\beta^{-kd/2}\int_0^\infty u^{kd/2}e^{-u}\,du
=\beta^{-kd/2}\Gamma(1+kd/2).
$$

:::

Size has units of distance to the power $d$, while $\beta$ has units of inverse distance squared in every dimension. This makes $\beta s^{2/d}$ dimensionless, and makes $p_d(s)$ a density per unit size. These checks catch mistakes in changing variables.

Writing dimensionless size as $w=\beta^{d/2}s$ removes the size scale. The dimensional size laws then differ in shape, while the transformed variable $U=\beta s^{2/d}=w^{2/d}$ has the same exponential law.

<div class="figure-scroll">

{{block:fig:PLACE-SIZE-DENSITY-COLLAPSE}}

</div>

Removing units does not erase the difference between length, area, and volume distributions. The nonlinear transformation to U removes that shape difference; its shared exponential law is the assumption used in the change of variables. See [Field-size laws, Eq. 1, p. 1111](../papers/mainali-2025-universal-statistics.pdf#page=3).

<div class="table-responsive">

{{block:tbl:PLACE-SIZE-LAWS}}

</div>

[A [**Weibull distribution**]{.definition-term custom-style="Definition Term"} has survival probability $\exp[-(s/b)^k]$ for size $s>0$, scale $b>0$, and shape $k>0$.]{.definition-explanation} Here $k=2/d$ and $b=\beta^{-d/2}$. In 3D the diverging density does not mean a positive probability of exactly zero volume; the probability of $0<s<\delta$ still tends to zero as $\delta\to0$.

For a concrete comparison, set $\sigma=1$ m and $q=5$ in this limiting calculation. The mean size is $0.5013$ m in 1D, $0.2513$ m$^2$ in 2D, and $0.1260$ m$^3$ in 3D. These values describe the same local distance scale and threshold, rather than fields with the same numerical size in different units. More generally, the geometry and moment formula simplify to $\mu_s\simeq(\sqrt{2\pi}\sigma/q)^d$.

This approximation has a measurable error even for a smooth Gaussian process. At $q=1.1,\sigma=2.4$ m, its 1D mean is $5.469$ m, compared with the [exact stationary crossing result](ch-place-fields.html#sec-place-inference) $3.746$ m, an overestimate of $46.0\%$. At $q=5$ the error is $3.73\%$. [This is why the paper compares data to finite threshold simulations as well as to limiting curves.]{.key-statement}

::: {.publisher-clarification-note .publisher-fold-always title="Source check: three printed steps in the supplement"}

The printed supplement appears to contain three algebraic errors in this calculation:

- Equation S18 prints multiplication by mean size where the preceding moment formula requires division.
- Equation S23 omits a factor $\sqrt2$ when solving the parabola in S22 for full width.
- In S25 the finite-height quadratic exponent should be negative.

The derivation above retains the main paper's distributional form and obtains the constants from the displayed parabola, the moment integral, and the independent crossing calculation. These corrections concern the printed derivation; they do not establish that the simulation code or empirical fits used the same mistakes.[^p3-corrections]

:::

## Slices test spatial structure beyond field volume {#sec:PLACE-SLICES}

A model can fit field volumes and still place activity incorrectly within those volumes. Slicing the map tests that internal spatial structure.

Restrict a Gaussian field to a straight line $x=x_0+tv$. At any chosen values $t_1,\ldots,t_n$, its values are a subset of the original jointly Gaussian values. They therefore remain jointly Gaussian. Along the line the covariance is $C((t-t')v)$; for a unit direction in an isotropic field it has the same local length scale $\sigma$. The same argument applies to a flat plane. First slicing and then thresholding gives the same active portions as thresholding and then slicing.[^p3-slices-source]

Thus a line through a 2D or 3D map has the one dimensional excursion prediction, and a plane through a 3D map has the two dimensional prediction. The field being counted is now a connected active interval or patch in that slice. One 3D component can be missed, cut into multiple pieces, or intersect several slices.

The sampling rule matters. Choosing one original field uniformly and cutting through its centre is different from choosing lines uniformly through space. Large fields are more likely to be hit by a spatially sampled line, and most hits pass away from their centres. The Gaussian restriction argument describes excursions along the sampled line. The radius distribution for fields counted once each cannot be used directly as the distribution of lengths observed along a line. In the high peak picture, an isotropic $d$ dimensional field has a radius of order $\sigma/q$; converting this same radius into $d$ dimensional size and then cutting it requires both hit probability and cut position.

Figure 2 separates the measurements by spatial dimension:

- Panels A–B illustrate 2D thresholding. C measures lengths along slices, D measures original field areas, and E counts fields per observed cell.
- F–G show 3D examples; H, I, and J compare line lengths, planar areas, and full volumes.

<details class="publisher-long-content publisher-source-figure">
<summary>Original paper figure: Mainali, Azeredo da Silveira, and Burak (2025), Figure 2</summary>
<div class="publisher-fold-body">

{{block:fig:PAPER-PLACE-2}}

</div>
</details>

[The dashed analytical curves change with the dimension of the measurement, even within one recorded map. The alternative spherical-field model in Figure S2 matches empirical volumes and peak rates by construction but fails these slice distributions and the topology test. Matching volumes alone is therefore insufficient.]{.key-statement}[^p3-slices-source]

<details class="publisher-long-content publisher-source-figure">
<summary>Original paper figure: Mainali, Azeredo da Silveira, and Burak (2025), Figure S2</summary>
<div class="publisher-fold-body">

{{block:fig:PAPER-PLACE-S2}}

</div>
</details>

## Why slopes at field boundaries are Rayleigh {#sec:PLACE-SLOPES}

The derivative at an arbitrary position is Gaussian. A field boundary is a selected position, however, and selecting it changes the derivative distribution.

Return to the [crossing integral](ch-place-fields.html#sec-place-kac-rice) and retain only slopes between $v$ and $v+dv$. Their contribution is proportional to $v p_{z'}(v)dv$. Dividing by the total contribution of positive slopes gives the slope density at a typical upcrossing:

$$
p_{\uparrow}(v)
=\frac{v p_{z'}(v)}{\int_0^\infty w p_{z'}(w)\,dw}
=\sigma^2v\exp[-\sigma^2v^2/2],\qquad v>0.
$$

The height density cancels because height and slope are independent. [This Rayleigh law is therefore independent of $q$ under the smooth stationary Gaussian model, without a high threshold approximation.]{.key-statement} Absolute slopes at downward boundaries have the same law. The rate slope is $av$, so its scale also depends on the firing rate gain. This selection effect explains why a half Gaussian law for a positive derivative sampled uniformly in space would be wrong at crossings.[^p3-slope-source]

::: {.publisher-clarification-note .publisher-fold-always title="Independent check: recover field width from its boundary slope"}

There is also an independent check on the high threshold width constant. Starting at an upcrossing with slope $v$, the local excursion is approximately

$$
z(x)-q\simeq vx-\frac{q}{2\sigma^2}x^2.
$$

Its second root is $s=2\sigma^2v/q$. Changing variables in the exact crossing slope law gives $p(s)=2\beta s e^{-\beta s^2}$ with $\beta=q^2/(8\sigma^2)$, the same constant as the peak calculation for $v_1=2$.

:::

Figure 3A identifies which width, peak, and slopes are measured. B compares local peak counts, C–D compare rate and size, and E compares boundary slopes. The paper measures boundary slopes by a finite difference between samples 0.1 m apart. This approximates a derivative and has its own spatial resolution. It is not a direct observation of the underlying synaptic input.

<details class="publisher-long-content publisher-source-figure">
<summary>Original paper figure: Mainali, Azeredo da Silveira, and Burak (2025), Figure 3</summary>
<div class="publisher-fold-body">

{{block:fig:PAPER-PLACE-3}}

</div>
</details>

[^p3-rare-source]: Mainali et al. (2025), *Universal statistics of hippocampal place fields across species and dimensionalities*, Neuron, 113, 1110–1120.e3, [doi:10.1016/j.neuron.2025.01.017](https://doi.org/10.1016/j.neuron.2025.01.017), Supplemental Methods S4, pp. 12–14, especially Equations S22–S25. The supplement cites Adler (1981) for the peak approximation. The main article cites Nosko (1988), reference 32, for asymptotic field statistics. This chapter supplies a local derivation and does not claim to reproduce either full theorem proof.

[^p3-shapes]: Mainali et al. (2025), *Universal statistics of hippocampal place fields across species and dimensionalities*, Neuron, 113, 1110–1120.e3, [doi:10.1016/j.neuron.2025.01.017](https://doi.org/10.1016/j.neuron.2025.01.017), Figures 3C–D, 4C, 5A–C, pp. 1115–1117; STAR Methods, “Maximum firing rate vs. field width.” The gain is matched through the fitted log-log intercept.

[^p3-size-source]: Mainali et al. (2025), *Universal statistics of hippocampal place fields across species and dimensionalities*, Neuron, 113, 1110–1120.e3, [doi:10.1016/j.neuron.2025.01.017](https://doi.org/10.1016/j.neuron.2025.01.017), main Equation 1 and Supplemental Methods S3–S4. The isotropic ball calculation and its explicit leading $\beta$ are reconstructed here.

[^p3-corrections]: Mainali et al. (2025), *Universal statistics of hippocampal place fields across species and dimensionalities*, Neuron, 113, 1110–1120.e3, [doi:10.1016/j.neuron.2025.01.017](https://doi.org/10.1016/j.neuron.2025.01.017), supplement printed pp. 12–14, Equations S18, S22–S25. Direct inspection of the PDF confirms these are printed expressions rather than text-extraction errors. The corrected constants also reproduce the large-$q$ limit of S14.

[^p3-slices-source]: Mainali et al. (2025), *Universal statistics of hippocampal place fields across species and dimensionalities*, Neuron, 113, 1110–1120.e3, [doi:10.1016/j.neuron.2025.01.017](https://doi.org/10.1016/j.neuron.2025.01.017), Figure 2 and “Place fields in two and three dimensions,” pp. 1113–1114; Figure S2A–C, supplemental p. 2. Sampling distinctions follow from restricting the process and are explained here.

[^p3-slope-source]: Mainali et al. (2025), *Universal statistics of hippocampal place fields across species and dimensionalities*, Neuron, 113, 1110–1120.e3, [doi:10.1016/j.neuron.2025.01.017](https://doi.org/10.1016/j.neuron.2025.01.017), Figure 3E, p. 1115; STAR Methods, “Boundary slopes.” The derivation is reconstructed from crossing counts. Mainali's [author teaching notes, “Slope at an upcrossing”](https://nischmainali.github.io/blog/gp-code-notes/), give the same slope weighting.

# Why place fields have different sizes and shapes {#ch:PLACE-FIELDS}

A cell recorded on a short track may have one smooth firing hill. On a long track, the same kind of cell may have several separated fields, each with a different width and height. In a room, its active regions can bend, split, and surround inactive holes. How could one model produce this variety and still make useful predictions?

Mainali, Azeredo da Silveira, and Burak propose that a cell's spatial input is a smooth random function. The cell fires where this function exceeds a threshold. The model predicts distributions of field lengths, areas, and volumes, rather than the location of a particular cell's next field. Its strongest tests ask whether fitting field sizes and counts also explains field shapes and holes.[^p3-question]

This chapter develops the calculations behind that claim. Spatial randomness here describes different possible rate maps. Once a map is drawn, it is fixed while the animal moves through it. The spatial coordinate is not time, and the model does not by itself describe memory drift, spike timing, or learning.

## From a rate map to a random function {#sec:PLACE-GP}

To predict a field's width, we need to relate activity at nearby positions. A histogram of firing rates alone loses that information: rearranging its values could turn one broad field into many tiny fields without changing the histogram.

A [**Gaussian process**]{.definition-term custom-style="Definition Term"} is a probability distribution over functions such that the values at any finite set of positions form a jointly Gaussian random vector. For positions $x_1,\ldots,x_n$, the vector $(h(x_1),\ldots,h(x_n))$ therefore has a multivariate Gaussian distribution. Its mean vector and covariance matrix are obtained by evaluating two functions,

$$
m(x)=\mathbb E[h(x)],\qquad
C(x,y)=\mathbb E[(h(x)-m(x))(h(y)-m(y))].
$$

The expectation runs over possible maps, or over cells assumed to share these statistics. These two functions determine every finite joint distribution. A Gaussian process can thus produce many different curves while keeping a precise rule for their spatial dependence. A jointly Gaussian vector is one for which every linear combination of its entries is Gaussian. For this family, zero covariance between two subvectors implies their independence. That extra property, which does not hold for general distributions, will simplify the crossing calculation. The values after thresholding will generally not have a Gaussian distribution.[^p3-model]

Three assumptions have different jobs. [**Stationarity**]{.definition-term custom-style="Definition Term"} means that moving the observation window does not change the map's probability law. Here it gives a constant mean and a covariance $C(x,y)=C(y-x)$ that depends on separation. It does not say that a particular map is flat. [**Isotropy**]{.definition-term custom-style="Definition Term"} means that rotating the separation does not change the covariance: in several dimensions, $C(\Delta x)$ depends only on $\|\Delta x\|$. It rules out a preferred direction in the model's statistics. Stationarity alone does not imply isotropy. Finally, smoothness controls whether the map has well defined spatial derivatives. Crossing calculations below require differentiable sample functions and nondegenerate joint distributions: the relevant vector of heights and derivatives must have an invertible covariance matrix, rather than obey an exact linear constraint. Peak calculations require second derivatives and enough regularity to control their local approximation. A Gaussian distribution of values does not guarantee this smoothness. For example, a covariance proportional to $e^{-|x-y|/b}$ has a sharp corner at zero separation and does not supply the differentiable paths assumed below.

Set the mean to zero and write $\sigma_h^2=C(0)$ for input variance. A constant input mean can be absorbed into the threshold. It is useful to normalize the input,

$$
z(x)=\frac{h(x)}{\sigma_h},\qquad
F(x)=a\,[z(x)-q]_+,
\quad [u]_+=\max(u,0).
$$

Here $z$ has variance one, $q$ is a dimensionless threshold, and $a>0$ converts normalized input to firing rate, in Hz. The paper writes $\theta$ for $q$, $r$ for covariance, and $D$ for spatial dimension; this guide uses $q,C,d$ to avoid conflicts with earlier chapters. The original input threshold is $q\sigma_h$. In the paper's Equation 3 the firing rate is proportional to $[h-q\sigma_h]_+$, which is equivalent to this form after choosing the gain.[^p3-model]

The [**excursion set**]{.definition-term custom-style="Definition Term"} above $q$ is

$$
A_q=\{x:z(x)>q\}.
$$

Each connected piece of $A_q$ is a model place field. In one dimension its size is length. In two and three dimensions it is area and volume. Two nearby peaks belong to one field if an above-threshold path joins them. Counting peaks and counting fields therefore answer different questions.

For a one dimensional stationary process, differentiation of covariance gives

$$
\operatorname{Var}(h')=
\left.\partial_x\partial_y C(y-x)\right|_{y=x}=-C''(0).
$$

The minus sign comes from differentiating $y-x$ once with respect to each variable. The paper defines the spatial scale

$$
\sigma=\sqrt{-\frac{C(0)}{C''(0)}};
\qquad \operatorname{Var}(z')=\frac{1}{\sigma^2}.
$$

Thus $\sigma$ compares typical height with typical slope and has units of distance. In an isotropic field, the same definition applies along any unit direction. For the smooth Gaussian covariance $C(\Delta x)=\sigma_h^2\exp[-\|\Delta x\|^2/(2\sigma^2)]$, it is exactly the parameter in that exponent. The paper uses a Gaussian covariance for its simulations. Other smooth covariances can share this local scale while having different longer distance structure.[^p3-scale]

## Count fields by counting crossings {#sec:PLACE-KAC-RICE}

Finding every root of a random curve is difficult. Counting how often the curve passes a level is easier because a small interval around a crossing has a width determined by its slope.

Consider a differentiable fixed curve and a simple upward crossing $x_0$ of $q$, with slope $v=z'(x_0)>0$. Close to the crossing,

$$
z(x)-q\simeq v(x-x_0).
$$

The curve lies in the vertical band $|z-q|<\varepsilon$ for a spatial distance approximately $2\varepsilon/v$. Integrating $z'(x)/(2\varepsilon)$ over that interval contributes one. Restricting to positive slopes counts only upward crossings. Under the usual regularity conditions, averaging this counting identity gives the [**Kac–Rice formula**]{.definition-term custom-style="Definition Term"} for the mean upcrossing density,

$$
\nu_+(q)=\int_0^\infty v\,p_{z,z'}(q,v)\,dv.
$$

The density $p_{z,z'}(q,v)$ describes how often height is near $q$ and slope near $v$. Multiplication by $v$ compensates for the shorter spatial window of a steep crossing. Merely multiplying the probability of being above threshold by a typical slope would miss this weighting.[^p3-crossings]

We can evaluate the integral because height and slope are independent here. Stationarity gives

$$
\mathbb E[zz']=\frac12\frac{d}{dx}\mathbb E[z(x)^2]=0.
$$

Height and slope are jointly Gaussian; zero covariance therefore makes them independent. Their distributions are $z\sim\mathcal N(0,1)$ and $z'\sim\mathcal N(0,\sigma^{-2})$. Consequently,

$$
\begin{aligned}
\nu_+(q)
&=\frac{e^{-q^2/2}}{\sqrt{2\pi}}
  \int_0^\infty v\frac{\sigma}{\sqrt{2\pi}}
                  e^{-\sigma^2v^2/2}\,dv\\
&=\frac{e^{-q^2/2}}{\sqrt{2\pi}}
  \frac{1}{\sigma\sqrt{2\pi}}
=\frac{e^{-q^2/2}}{2\pi\sigma}.
\end{aligned}
$$

In the integral, use $u=\sigma^2v^2/2$, so $v\,dv=du/\sigma^2$. This result is exact for the stated smooth stationary Gaussian model. A high threshold is not needed. Its units are inverse distance: increasing $\sigma$ stretches the map and reduces crossings per metre.

On a finite track $[0,L]$, each upcrossing starts a field, but a field may already be active at the left endpoint. If $N_L$ counts all components intersecting the track, then, under regularity conditions that exclude tangencies and give nonzero slopes at crossings,

$$
N_L=N_+(q;[0,L])+\mathbf1\{z(0)>q\},
\qquad
\mathbb E[N_L]=L\nu_+(q)+Q(q),
$$

where $Q(q)=1-\Phi(q)$ and $\Phi$ is the standard normal cumulative distribution function. The last term is the endpoint correction. Removing incomplete boundary fields changes the counting convention, so the same correction cannot then be used unchanged. This identity also gives the paper's exact one dimensional mean Euler characteristic, Equation 8.[^p3-ec-source]

## Infer a threshold and a spatial scale {#sec:PLACE-INFERENCE}

A low field count can result from a high threshold or a slowly varying map. Field lengths help separate those possibilities.

At a uniformly chosen position, the probability of activity is $Q(q)$. Hence a track of length $L$ has expected occupied length $LQ(q)$. On a long stationary track, the average occupied length per field is the occupied length per unit distance divided by the number of fields per unit distance. The corresponding gap calculation uses the inactive fraction $\Phi(q)$:

$$
\begin{aligned}
\mu_s&=\frac{Q(q)}{\nu_+(q)}
      =2\pi\sigma Q(q)e^{q^2/2},\\
\mu_g&=\frac{\Phi(q)}{\nu_+(q)}
      =2\pi\sigma\Phi(q)e^{q^2/2}.
\end{aligned}
$$

These are stationary per-field and per-gap means, ignoring clipping at track boundaries. They are not an assertion that the expectation of a finite sample's ratio equals the ratio of its expectations. Subject to suitable averaging over a long track or many maps, they give the inference rule in Methods S3, Equations S14–S15.[^p3-means]

Adding and dividing removes one unknown at a time:

$$
\mu_s+\mu_g=2\pi\sigma e^{q^2/2},\qquad
\frac{\mu_s}{\mu_s+\mu_g}=Q(q).
$$

Thus

$$
q=\Phi^{-1}\!\left(\frac{\mu_g}{\mu_s+\mu_g}\right),
\qquad
\sigma=\frac{\mu_s+\mu_g}{2\pi}e^{-q^2/2}.
$$

For example, $q=1.1$ and $\sigma=2.4$ m, the fitted parameters reported for the 200 m bat tunnel, give $Q(q)=0.1357$, $\nu_+=0.03621$ per metre, $\mu_s=3.746$ m, and $\mu_g=23.868$ m in the continuous model. Putting these two means into the inversion recovers $q=1.1$ and $\sigma=2.4$ m. The expected number of intersecting fields on a 200 m track is $7.2425+0.1357=7.3782$, including the left endpoint term. These are calculations from the fitted model, not fresh estimates from raw recordings.

The means do not imply a full gap or count distribution. At high thresholds, distant rare excursions can approach independent events if correlations decay sufficiently with distance. In that regime, field locations approach a Poisson process, counts in a long interval are approximately Poisson, and gaps are approximately exponential. Smoothness and stationarity alone do not ensure this independence. A periodic Gaussian process, for example, retains long distance dependence. Upward and downward crossings that enclose the same small field remain strongly related even when fields far apart are almost independent.

Experimental selection also matters. If cells with no fields are excluded, a Poisson model with unconditioned mean $\lambda$ gives

$$
\Pr(N=n\mid N\ge1)=
\frac{e^{-\lambda}\lambda^n}{n!(1-e^{-\lambda})},\quad n\ge1,
\qquad
\mathbb E[N\mid N\ge1]=\frac{\lambda}{1-e^{-\lambda}}.
$$

The mean follows because the omitted $n=0$ term contributes zero to $\sum n\Pr(N=n)=\lambda$, while conditioning divides all remaining probabilities by $1-e^{-\lambda}$. For $\lambda=1$, $36.8\%$ of cells are excluded and the observed mean is $1.582$, not one. Using $1.582$ as the unconditioned mean would infer too many fields. The paper applies this correction to its two dimensional count fit, Equation 5.[^p3-selection]

## Why rare high fields are nearly parabolic {#sec:PLACE-RARE-PEAKS}

The crossing calculation determines a mean length exactly, but it does not yet explain the shape of the length histogram. To obtain that distribution, we examine the small region around a peak that barely exceeds a high threshold.

The following is a teaching reconstruction of the high excursion argument in Methods S4, with algebraic corrections made explicit below. It assumes a sufficiently smooth, stationary, isotropic, unit variance Gaussian field, an invertible covariance matrix for the relevant derivative variables, and $q\to\infty$. It describes typical components counted once each, away from environment boundaries. It is not a proof of the full excursion convergence theorem for every allowed covariance.[^p3-rare-source]

The [**Hessian**]{.definition-term custom-style="Definition Term"} is the matrix $H$ of second spatial derivatives; its eigenvalues describe curvature along the principal directions. Isotropy and the definition of $\sigma$ imply

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

Thus the scaled excess height approaches an exponential variable of mean one. In several dimensions, high peak counts have the additional leading factor $q^{d-1}$. Its ratio at $q+u/q$ and $q$ tends to one, so the same excess-height limit remains. The higher dimensional count factor will also follow from the Euler characteristic calculation below. A rigorous conclusion requires control of the remainder and of components containing multiple peaks, beyond this local argument.

In one dimension, the full field length is $s=2r_*$. Eliminating $\epsilon$ gives

$$
s\simeq\frac{2\sqrt2\sigma}{q}\sqrt U,
\qquad
\epsilon\simeq\frac{q s^2}{8\sigma^2}.
$$

This supplies two distinct predictions. The length is a scaled square root of an exponential variable, giving a Rayleigh distribution. The peak firing rate is $a\epsilon$, so at fixed high $q$ it is proportional to $s^2$. The exponent two concerns rate versus linear size. In three dimensions a suitable linear size is $s^{1/3}$ when $s$ denotes volume.

At moderate thresholds the omitted shape fluctuations matter. Figure 3C reports a rate versus length exponent of $1.42$ in the 200 m bat data and $1.46$ in finite threshold model simulations. Figure 3D reports $1.75$ versus $1.71$ using cube root of volume in 3D. These are compatible with a model that approaches exponent two only as the threshold becomes large; they are not measurements of the limiting exponent. Figure 5A–C illustrates the progression toward simpler, usually single peak fields as $q$ increases. Figure 4C tests this trend in the shorter bat tunnel.[^p3-shapes]

## Derive the size law in each dimension {#sec:PLACE-SIZE-LAW}

A round region's radius and its volume have different units and different distributions. This geometric conversion explains why the model predicts different histograms in a track, an arena, and a room.

Let $v_d=\pi^{d/2}/\Gamma(1+d/2)$ be the volume of a unit ball in $d$ dimensions. For $d=1,2,3$, it is $2,\pi,4\pi/3$. The symbol $\Gamma$ is the gamma function, defined for $t>0$ by $\Gamma(t)=\int_0^\infty u^{t-1}e^{-u}\,du$. It extends factorials: $\Gamma(n+1)=n!$.

Using the radius from the preceding section, the field size is

$$
s\simeq v_d\left(\frac{\sqrt2\sigma}{q}\right)^d U^{d/2},
\qquad
U=\beta s^{2/d},\qquad
\beta=\frac{q^2}{2\sigma^2v_d^{2/d}}.
$$

Since the density of $U$ is $e^{-u}$ for $u>0$, changing variables gives

$$
\begin{aligned}
p_d(s)&=e^{-\beta s^{2/d}}\frac{d}{ds}(\beta s^{2/d})\\
&=\frac{2\beta}{d}s^{2/d-1}e^{-\beta s^{2/d}},\qquad s>0.
\end{aligned}
$$

This is the paper's Equation 1. The expression for $\beta$ above is its leading high threshold geometric scale, not an exact finite threshold identity. A finite threshold simulation can share the approximate shape while having a different fitted scale.[^p3-size-source]

Normalization needs no special integral: $\int_0^\infty p_d(s)\,ds=\int_0^\infty e^{-u}\,du=1$. The same substitution supplies every positive moment,

$$
\mathbb E[s^k]
=\beta^{-kd/2}\int_0^\infty u^{kd/2}e^{-u}\,du
=\beta^{-kd/2}\Gamma(1+kd/2).
$$

In particular,

$$
\mu_s=\Gamma(1+d/2)\beta^{-d/2},\qquad
\beta=\left[\frac{\Gamma(1+d/2)}{\mu_s}\right]^{2/d}.
$$

Size has units of distance to the power $d$, while $\beta$ has units of inverse distance squared in every dimension. This makes $\beta s^{2/d}$ dimensionless, and makes $p_d(s)$ a density per unit size. These checks catch mistakes in changing variables.

<div class="table-responsive">

{{block:tbl:PLACE-SIZE-LAWS}}

</div>

A [**Weibull distribution**]{.definition-term custom-style="Definition Term"} has survival probability $\exp[-(s/b)^k]$ for size $s>0$, scale $b>0$, and shape $k>0$. Here $k=2/d$ and $b=\beta^{-d/2}$. In 3D the diverging density does not mean a positive probability of exactly zero volume; the probability of $0<s<\delta$ still tends to zero as $\delta\to0$.

For a concrete comparison, set $\sigma=1$ m and $q=5$ in this limiting calculation. The mean size is $0.5013$ m in 1D, $0.2513$ m$^2$ in 2D, and $0.1260$ m$^3$ in 3D. These values describe the same local distance scale and threshold, rather than fields with the same numerical size in different units. More generally, the geometry and moment formula simplify to $\mu_s\simeq(\sqrt{2\pi}\sigma/q)^d$.

This approximation has a measurable error even for a smooth Gaussian process. At $q=1.1,\sigma=2.4$ m, its 1D mean is $5.469$ m, compared with the exact stationary crossing result $3.746$ m, an overestimate of $46.0\%$. At $q=5$ the error is $3.73\%$. This is why the paper compares data to finite threshold simulations as well as to limiting curves.

**Reading the supplement carefully.** The printed supplement appears to contain algebraic errors in this calculation. Its Equation S18 prints multiplication by mean size where the preceding moment formula requires division. Its Equation S23 omits a factor $\sqrt2$ when solving the parabola in S22 for full width. In S25 the finite-height quadratic exponent should be negative. The derivation above retains the main paper's distributional form and obtains the constants from the displayed parabola, the moment integral, and the independent crossing calculation. These corrections concern the printed derivation; they do not establish that the simulation code or empirical fits used the same mistakes.[^p3-corrections]

## Why slices are a separate test {#sec:PLACE-SLICES}

A model can fit field volumes and still place activity incorrectly within those volumes. Slicing the map tests that internal spatial structure.

Restrict a Gaussian field to a straight line $x=x_0+tv$. At any chosen values $t_1,\ldots,t_n$, its values are a subset of the original jointly Gaussian values. They therefore remain jointly Gaussian. Along the line the covariance is $C((t-t')v)$; for a unit direction in an isotropic field it has the same local length scale $\sigma$. The same argument applies to a flat plane. First slicing and then thresholding gives the same active portions as thresholding and then slicing.[^p3-slices-source]

Thus a line through a 2D or 3D map has the one dimensional excursion prediction, and a plane through a 3D map has the two dimensional prediction. The field being counted is now a connected active interval or patch in that slice. One 3D component can be missed, cut into multiple pieces, or intersect several slices.

The sampling rule matters. Choosing one original field uniformly and cutting through its centre is different from choosing lines uniformly through space. Large fields are more likely to be hit by a spatially sampled line, and most hits pass away from their centres. The Gaussian restriction argument describes excursions along the sampled line. It does not justify assigning an unchanged field-counted radius distribution to all observed chords. In the high peak picture, an isotropic $d$ dimensional field has a radius of order $\sigma/q$; converting this same radius into $d$ dimensional size and then cutting it requires both hit probability and cut position.

Read Figure 2 with these distinctions in mind. Panels A–B illustrate 2D thresholding. C measures lengths along slices, D measures original field areas, and E counts fields per observed cell. F–G show 3D examples; H, I, and J compare line lengths, planar areas, and full volumes. The dashed analytical curves change with the dimension of the measurement, even within one recorded map. The alternative spherical-field model in Figure S2 matches empirical volumes and peak rates by construction but fails these slice distributions and the topology test. Matching volumes alone is therefore insufficient.[^p3-slices-source]

## Why slopes at field boundaries are Rayleigh {#sec:PLACE-SLOPES}

The derivative at an arbitrary position is Gaussian. A field boundary is a selected position, however, and selecting it changes the derivative distribution.

Return to the crossing integral and retain only slopes between $v$ and $v+dv$. Their contribution is proportional to $v p_{z'}(v)dv$. Dividing by the total contribution of positive slopes gives the slope density at a typical upcrossing:

$$
p_{\uparrow}(v)
=\frac{v p_{z'}(v)}{\int_0^\infty w p_{z'}(w)\,dw}
=\sigma^2v\exp[-\sigma^2v^2/2],\qquad v>0.
$$

The height density cancels because height and slope are independent. This Rayleigh law is therefore independent of $q$ under the smooth stationary Gaussian model, without a high threshold approximation. Absolute slopes at downward boundaries have the same law. The rate slope is $av$, so its scale also depends on the firing rate gain. This selection effect explains why a half Gaussian law for a positive derivative sampled uniformly in space would be wrong at crossings.[^p3-slope-source]

There is also an independent check on the high threshold width constant. Starting at an upcrossing with slope $v$, the local excursion is approximately

$$
z(x)-q\simeq vx-\frac{q}{2\sigma^2}x^2.
$$

Its second root is $s=2\sigma^2v/q$. Changing variables in the exact crossing slope law gives $p(s)=2\beta s e^{-\beta s^2}$ with $\beta=q^2/(8\sigma^2)$, the same constant as the peak calculation for $v_1=2$.

Figure 3A identifies which width, peak, and slopes are measured. B compares local peak counts, C–D compare rate and size, and E compares boundary slopes. The paper measures boundary slopes by a finite difference between samples 0.1 m apart. This approximates a derivative and has its own spatial resolution. It is not a direct observation of the underlying synaptic input.

## Count holes as well as connected fields {#sec:PLACE-TOPOLOGY}

Two maps can have the same field count and total active area but different holes. To test this part of the geometry, raise the activity threshold and watch how regions split, join, appear, and disappear.

The [**Euler characteristic**]{.definition-term custom-style="Definition Term"}, written $\chi$, combines these counts. In 1D it equals the number of connected active intervals. In 2D it is the number of connected components minus the number of independent holes. Three disjoint disks have $\chi=3$; one connected ring has $\chi=1-1=0$. In 3D it is components minus independent tunnels plus enclosed cavities. A solid ball has $\chi=1$, a solid ring has $\chi=0$, and a hollow spherical shell has $\chi=2$. These counts are the first three [**Betti numbers**]{.definition-term custom-style="Definition Term"}: numbers of independent components, loops, and cavities, respectively.[^p3-ec-source]

The expected Euler characteristic has an exact Gaussian formula even where identifying it with field count would be wrong. We already derived the 1D case. To understand the higher dimensional factors, we use a mathematical input: for a smooth function on a compact domain whose critical points have zero gradient and invertible Hessians, the Euler characteristic of a level set region can be computed as a signed count of critical points, including boundary contributions. This is the relevant conclusion of Morse theory. We do not prove that topological theorem here. The calculation below shows how its Gaussian expectation produces the paper's polynomials and boundary terms; the general Gaussian result is given by Taylor's kinematic formula.[^p3-taylor]

First take the interior of a $j$ dimensional region, with $j\le3$, and set $\lambda=\sigma^{-2}$. A critical point has gradient zero. The multidimensional Kac–Rice rule counts these zeros with the absolute Hessian determinant; the Morse signs replace that absolute determinant by $\det(-H)$. The resulting signed density above level $q$ is

$$
\eta_j(q)=p_{\nabla z}(0)
\int_q^\infty
\mathbb E[\det(-H)\mid z=b,\nabla z=0]\,\phi(b)\,db,
$$

where $\phi(b)=e^{-b^2/2}/\sqrt{2\pi}$. The gradient's $j$ components are independent Gaussians of variance $\lambda$, so $p_{\nabla z}(0)=(2\pi\lambda)^{-j/2}$. The determinant measures how spatial volume near a gradient zero converts to gradient volume, just as the slope did for a scalar crossing.

Here are the Gaussian algebra steps behind the determinant average. Write the conditional Hessian as $H=-b\lambda I+G$, where $G$ has zero mean. Differentiating an isotropic covariance four times gives, for distinct indices $i,k$,

$$
\mathbb E[G_{ii}G_{kk}]=\kappa-\lambda^2,
\qquad
\mathbb E[G_{ik}^2]=\kappa.
$$

The constant $\kappa$ describes a fourth derivative of covariance. Conditioning on height subtracts $\lambda^2$ from the covariance of the two diagonal entries, but not from the off-diagonal variance. Hence each pair contributes

$$
\mathbb E[G_{ii}G_{kk}-G_{ik}^2]=-\lambda^2.
$$

For $j=1$, $\mathbb E[\det(-H)\mid b]=b\lambda$. For $j=2$, expand the two by two determinant to obtain $\lambda^2(b^2-1)$. For $j=3$, the leading term is $b^3\lambda^3$; the three index pairs each contribute $-b\lambda^3$, and all odd centered Gaussian products vanish. The result is $\lambda^3(b^3-3b)$. The unknown fourth derivative $\kappa$ has canceled.

Integrating the three polynomials gives

$$
\begin{aligned}
\int_q^\infty b\phi(b)\,db&=\phi(q),\\
\int_q^\infty(b^2-1)\phi(b)\,db&=q\phi(q),\\
\int_q^\infty(b^3-3b)\phi(b)\,db&=(q^2-1)\phi(q).
\end{aligned}
$$

For example, differentiate $-q\phi(q)$ to get $(q^2-1)\phi(q)$, which verifies the second integral using its vanishing upper endpoint. Combining the determinant, gradient density, and integral yields

$$
\eta_1=\frac{e^{-q^2/2}}{2\pi\sigma},\qquad
\eta_2=\frac{q e^{-q^2/2}}{(2\pi)^{3/2}\sigma^2},\qquad
\eta_3=\frac{(q^2-1)e^{-q^2/2}}{(2\pi)^2\sigma^3}.
$$

These are signed densities per length, area, and volume, not three formulas for positive field counts.

Now include the boundary of an ordinary closed square or cube of side $L$, whose opposite faces are not joined and with every intersecting component retained. On a $j$ dimensional face, derivatives along the face give the same calculation as above. Each of its $d-j$ gradient components perpendicular to the face and directed out of the box must have the appropriate sign to contribute to the boundary Morse count. Symmetry and independence give a factor $2^{-(d-j)}$. There are $2^{d-j}\binom dj$ such faces, each of size $L^j$. Their combined coefficient is therefore $\binom djL^j$. Corners supply $Q(q)$ in total. With $r=L/\sigma$, the formulas become

$$
\begin{aligned}
\mathbb E[\chi_1]&=Q(q)+\frac{r}{2\pi}e^{-q^2/2},\\
\mathbb E[\chi_2]&=Q(q)+
\left[\frac{2r}{2\pi}+\frac{r^2q}{(2\pi)^{3/2}}\right]e^{-q^2/2},\\
\mathbb E[\chi_3]&=Q(q)+
\left[\frac{3r}{2\pi}+\frac{3r^2q}{(2\pi)^{3/2}}
+\frac{r^3(q^2-1)}{(2\pi)^2}\right]e^{-q^2/2}.
\end{aligned}
$$

These reproduce the paper's Equations 8–10 for interval, square, and cube geometry. They are not the formulas for a periodic box. For a rectangle or rectangular room, replace $2L$ or $3L$ by the sum of side lengths, $3L^2$ by the sum of pairwise side products, and $L^3$ by volume. A general domain requires its own geometric boundary factors. Applying only the volume term to a small room would discard real boundary contributions.

The limiting checks are informative. As $q\to-\infty$, the whole box becomes active and all three expectations tend to one. As $q\to+\infty$, they tend to zero. At intermediate thresholds the higher dimensional signed densities can be negative because tunnels or holes outnumber components. For example a cube with $L/\sigma=10$ has expected $\chi=-20.06$ at $q=0$. A negative expected Euler characteristic is meaningful; a negative expected field count would not be.

At a sufficiently high threshold, almost every component is a small solid blob with one peak and no holes. Then $\chi\simeq N$. For a large box, retaining the leading volume term and the leading power of $q$ gives

$$
\mathbb E[N]\simeq
\frac{V}{(2\pi)^{(d+1)/2}\sigma^d}
q^{d-1}e^{-q^2/2},
$$

where $V$ is environment length, area, or volume. Dividing $VQ(q)$ by this count and using $Q(q)\simeq\phi(q)/q$ recovers $\mu_s\simeq(\sqrt{2\pi}\sigma/q)^d$, independently checking the size-law mean. The exact EC formula and this approximate component count have different ranges of validity.[^p3-higher-count]

Read Figure 3F–H as whole curves, rather than single field counts. Increasing the applied firing rate cutoff by $t\ge0$ changes the normalized level to $q+t/a$. It can reveal separation between peaks or remove components. The measured maps only test levels at or above their original effective cutoff; the rest of an analytic curve is a prediction. The gain was matched using mean maximum firing rate before the EC comparison, so the horizontal conversion from Hz to normalized level also uses fitted information. Two dimensional holes and three dimensional tunnels help explain the nonmonotonic curves.[^p3-ec-source]

## What was fitted and what was tested {#sec:PLACE-DATA}

The experiments supply estimated firing rate maps, not the hidden Gaussian input. To assess a prediction, we must therefore track both which summaries set its parameters and which processing decisions change the map's geometry.

The paper reanalyzes earlier bat and rodent recordings. It uses different available summaries in different conditions. The inspected article and supplement do not clearly give the final included cell count for every analysis, particularly the long-tunnel and 3D reanalyses; counts from an original recording study should therefore not be silently substituted for those final samples.[^p3-processing]

<div class="table-responsive">

{{block:tbl:PLACE-DATA-COMPARISONS}}

</div>

The STAR Methods call the virtual-track animals rats in one sentence; Figure 1F and the main results identify them as mice. Several STAR figure cross-references also appear displaced. The table follows the main figure captions and the analyses described in full, rather than those isolated labels.

Figure 1C distinguishes a limiting analytical Rayleigh curve from the finite threshold simulation histogram. Its parameters were constrained by both mean length and mean gap, so the full length histogram is an additional check. Figure 1D does the same for gaps. E tests skew and excess kurtosis of log lengths. For $Y=\log s$, write $m_k=\mathbb E[(Y-\mathbb EY)^k]$; then skew is $m_3/m_2^{3/2}$ and excess kurtosis is $m_4/m_2^2-3$. A lognormal size distribution makes $Y$ Gaussian and both population quantities zero. Finite sample estimates still fluctuate, which is why the figure compares simulated sampling distributions.[^p3-fit-tests]

For the long-tunnel data, the authors compared the Gaussian excursion model with a fitted lognormal using likelihoods and criteria that penalize fitted parameter count. Those comparisons favored the Gaussian model. These are in-sample model comparisons. They are not reported held-out forecasts. Model histogram error bars come from $10^4$ simulations matched to the number of recorded cells; they do not quantify every source of animal-level or measurement uncertainty.[^p3-fit-tests]

The processing choices affect the quantities being compared. Bat maps were rectified at about 0.5 Hz for denoising. The 3D maps, sampled in 10 cm bins, also received a median filter. Fields larger than three standard deviations above mean 3D volume were removed as possible merges, including from slice analyses. Peak counting excluded incomplete boundary fields and used a range of smoothing widths. The 1D rate versus width comparison used an additional 1 Hz cutoff. These decisions can remove small components, alter peaks, and change tails. They belong to the definition of the analyzed fields.[^p3-processing]

The supplement adds useful checks. Figure S1 matches the rat maze's 15 cm minimum length cutoff in simulations and removes unusually large empirical fields; changing that cutoff changes log-length moments. Figure S5 shows sensitivity of the higher-moment comparison across small denoising thresholds, while the rate versus width slope becomes stable above about 1 Hz. Figure S2 compares the spherical-field alternative and measures boundary curvature. Locally, mean curvature averages bending in two principal directions and Gaussian curvature multiplies them: a spherical patch bends the same way in both directions, while a saddle bends in opposite directions. These are extra shape measurements; they are not needed to derive the field-size law. Surface representations and finite differences affect their estimates.[^p3-supp-tests]

Figure 4A–B summarizes fitted parameter changes across a small set of environments. The correlation length increases with environment size while the threshold generally decreases. Increasing $\sigma$ reduces crossings per metre; decreasing $q$ increases them. Both parameters also affect mean length, so these effects must be considered together. Figure S3 reports count scaling exponents below one and hence a weak decline in count per unit environment size. These cross-experiment trends do not establish a biological scaling law. In particular, the 3D table's reported $\sigma=4.0$ has an unclear distance-unit conversion relative to the spatial binning, so it should not be read as a verified value in metres.[^p3-trends]

The model also allows differences between cells. Figure S4 draws a positive threshold separately for each cell and keeps that threshold for two otherwise independent maps representing opposite flight directions. Low-threshold cells tend to have more and larger fields in both maps; this shared cell property creates correlations between flight directions even when field locations differ between directions. Two distribution parameters were chosen to match the two empirical correlations, so those correlations are fitted features of this extension. Its continued agreement with length and gap distributions is the additional comparison. This extension should not be described as a two-parameter model shared by all cells.[^p3-threshold-variation]

## What Gaussian maps imply about synaptic input {#sec:PLACE-WIRING}

The statistical model becomes biologically useful if it suggests how a circuit could make the maps. A random weighted sum of many inputs is one possible mechanism, and the supplement makes its assumptions explicit.

Let $u_i(x)$ be the fixed spatial tuning of input neuron $i$, and let independent weights $W_i$ have zero mean and variance $v_W$. The profiles $u_i$ may have nonzero spatial means. The expectation below is over weights: their zero means make the summed input $h(x)$ have mean zero. The postsynaptic input is

$$
h(x)=\sum_{i=1}^n W_i u_i(x).
$$

At a finite list of positions this is a sum of independent random vectors, one per presynaptic cell. Under a multivariate central limit condition, with a suitable normalization and no single input dominating, the sum approaches a Gaussian vector as the number of contributing inputs grows. Applying this at every finite list supplies the Gaussian-process description. The theorem needs many contributing inputs at the positions in question; a large anatomical input count alone does not show that this condition holds.[^p3-wiring-source]

The covariance calculation exposes which assumption supplies spatial structure:

$$
\begin{aligned}
\mathbb E[h(x)h(y)]
&=\sum_{i,j}\mathbb E[W_iW_j]u_i(x)u_j(y)\\
&=v_W\sum_i u_i(x)u_i(y).
\end{aligned}
$$

If inputs are translated copies $u_i(x)=u_0(x-x_i)$ with centres densely and uniformly covering space at density $\rho$, the sum is approximately

$$
C(y-x)\simeq v_W\rho\int u_0(s)u_0(s+y-x)\,ds.
$$

Uniform coverage supplies stationarity away from boundaries; smooth input tuning supplies smoothness. Random weights supply the Gaussian limit under their independence and size conditions. These are separate assumptions. For heterogeneous shapes, average the last integral over the distribution of input shapes, as in Methods S2, Equation S8.

For example, take $u_0(s)=R_0e^{-s^2/(2b^2)}$ in one dimension. Completing the square gives

$$
\int u_0(s)u_0(s+\Delta)\,ds
=R_0^2\sqrt\pi b\,e^{-\Delta^2/(4b^2)}.
$$

The covariance's Gaussian standard deviation is $\sqrt2 b$. This calculation specifies the width convention, avoiding an ambiguous assertion that covariance is simply “twice as wide.”

Agreement with the Gaussian field predictions supports this random-summation account as a possible explanation. It does not uniquely recover synaptic weights from rate maps. Correlated inputs, a structured component added to many random contributions, plasticity, or recurrent processing could also produce approximately Gaussian spatial input under some conditions. The paper measures rate maps, rather than the relevant weights or subthreshold input directly. Its analyzed environments were familiar and fairly uniform; stationarity may fail near landmarks, boundaries, rewards, or in changing tasks.[^p3-discussion]

The result to carry into the synthesis is therefore specific: thresholding a smooth spatial Gaussian field links field arrangement, shape, and topology through a small set of parameters and gives several successful cross-checks. Turning that statistical agreement into a claim about circuit mechanism requires additional measurements or perturbations.

[^p3-question]: Mainali, N., Azeredo da Silveira, R., & Burak, Y. (2025). *Universal statistics of hippocampal place fields across species and dimensionalities*. Neuron, 113, 1110–1120.e3. [https://doi.org/10.1016/j.neuron.2025.01.017](https://doi.org/10.1016/j.neuron.2025.01.017), Introduction and Results, pp. 1110–1111; Figure 1.

[^p3-model]: Mainali et al. (2025), *Universal statistics of hippocampal place fields across species and dimensionalities*, Neuron, 113, 1110–1120.e3, [doi:10.1016/j.neuron.2025.01.017](https://doi.org/10.1016/j.neuron.2025.01.017), STAR Methods, Equations 2–3, p. e1; Supplemental Methods S1, p. 8.

[^p3-scale]: Mainali et al. (2025), *Universal statistics of hippocampal place fields across species and dimensionalities*, Neuron, 113, 1110–1120.e3, [doi:10.1016/j.neuron.2025.01.017](https://doi.org/10.1016/j.neuron.2025.01.017), STAR Methods, Equation 4, p. e2; Supplemental Methods S3, Equations S10–S11. The derivative calculation here is expanded for teaching.

[^p3-crossings]: Mainali et al. (2025), *Universal statistics of hippocampal place fields across species and dimensionalities*, Neuron, 113, 1110–1120.e3, [doi:10.1016/j.neuron.2025.01.017](https://doi.org/10.1016/j.neuron.2025.01.017), Supplemental Methods S3, Equations S9–S13, pp. 10–11. The narrow-band upcrossing argument is a reconstruction. See also Mainali, N. (2026, August 6), *Mathematical properties of Gaussian process neural code: Excursion geometry, spectral structure, and coding error*, [author teaching notes, “The Kac-Rice formula” and “Expected crossing count”](https://nischmainali.github.io/blog/gp-code-notes/).

[^p3-ec-source]: Mainali et al. (2025), *Universal statistics of hippocampal place fields across species and dimensionalities*, Neuron, 113, 1110–1120.e3, [doi:10.1016/j.neuron.2025.01.017](https://doi.org/10.1016/j.neuron.2025.01.017), Figure 3F–H; STAR Methods, “Euler characteristics,” Equations 8–10, p. e3.

[^p3-means]: Mainali et al. (2025), *Universal statistics of hippocampal place fields across species and dimensionalities*, Neuron, 113, 1110–1120.e3, [doi:10.1016/j.neuron.2025.01.017](https://doi.org/10.1016/j.neuron.2025.01.017), Supplemental Methods S3, Equations S14–S15; STAR Methods, “Parameter inference in 1D environments.” The explicit inversion is derived here.

[^p3-selection]: Mainali et al. (2025), *Universal statistics of hippocampal place fields across species and dimensionalities*, Neuron, 113, 1110–1120.e3, [doi:10.1016/j.neuron.2025.01.017](https://doi.org/10.1016/j.neuron.2025.01.017), STAR Methods, Equation 5 and “Parameter inference in 2D environments,” p. e2.

[^p3-rare-source]: Mainali et al. (2025), *Universal statistics of hippocampal place fields across species and dimensionalities*, Neuron, 113, 1110–1120.e3, [doi:10.1016/j.neuron.2025.01.017](https://doi.org/10.1016/j.neuron.2025.01.017), Supplemental Methods S4, pp. 12–14, especially Equations S22–S25. The supplement cites Adler (1981) for the peak approximation. The main article cites Nosko (1988), reference 32, for asymptotic field statistics. This chapter supplies a local derivation and does not claim to reproduce either full theorem proof.

[^p3-shapes]: Mainali et al. (2025), *Universal statistics of hippocampal place fields across species and dimensionalities*, Neuron, 113, 1110–1120.e3, [doi:10.1016/j.neuron.2025.01.017](https://doi.org/10.1016/j.neuron.2025.01.017), Figures 3C–D, 4C, 5A–C, pp. 1115–1117; STAR Methods, “Maximum firing rate vs. field width.” The gain is matched through the fitted log-log intercept.

[^p3-size-source]: Mainali et al. (2025), *Universal statistics of hippocampal place fields across species and dimensionalities*, Neuron, 113, 1110–1120.e3, [doi:10.1016/j.neuron.2025.01.017](https://doi.org/10.1016/j.neuron.2025.01.017), main Equation 1 and Supplemental Methods S3–S4. The isotropic ball calculation and its explicit leading $\beta$ are reconstructed here.

[^p3-corrections]: Mainali et al. (2025), *Universal statistics of hippocampal place fields across species and dimensionalities*, Neuron, 113, 1110–1120.e3, [doi:10.1016/j.neuron.2025.01.017](https://doi.org/10.1016/j.neuron.2025.01.017), supplement printed pp. 12–14, Equations S18, S22–S25. Direct inspection of the PDF confirms these are printed expressions rather than text-extraction errors. The corrected constants also reproduce the large-$q$ limit of S14.

[^p3-slices-source]: Mainali et al. (2025), *Universal statistics of hippocampal place fields across species and dimensionalities*, Neuron, 113, 1110–1120.e3, [doi:10.1016/j.neuron.2025.01.017](https://doi.org/10.1016/j.neuron.2025.01.017), Figure 2 and “Place fields in two and three dimensions,” pp. 1113–1114; Figure S2A–C, supplemental p. 2. Sampling distinctions follow from restricting the process and are explained here.

[^p3-slope-source]: Mainali et al. (2025), *Universal statistics of hippocampal place fields across species and dimensionalities*, Neuron, 113, 1110–1120.e3, [doi:10.1016/j.neuron.2025.01.017](https://doi.org/10.1016/j.neuron.2025.01.017), Figure 3E, p. 1115; STAR Methods, “Boundary slopes.” The derivation is reconstructed from crossing counts. Mainali's [author teaching notes, “Slope at an upcrossing”](https://nischmainali.github.io/blog/gp-code-notes/), give the same slope weighting.

[^p3-taylor]: Taylor, J. E. (2006). *A Gaussian kinematic formula*. The Annals of Probability, 34(1), 122–158. [https://doi.org/10.1214/009117905000000594](https://doi.org/10.1214/009117905000000594); [author preprint](https://arxiv.org/pdf/math/0602545), Equation 1.4, Theorem 4.1, Section 5.1 and Equation 5.1. This chapter uses the signed critical-point and boundary-counting framework, then derives the Gaussian algebra for dimensions at most three and the face factors for a box, matching Mainali et al.'s Equations 8–10. It does not prove the underlying Morse or kinematic theorem.

[^p3-higher-count]: Mainali et al. (2025), *Universal statistics of hippocampal place fields across species and dimensionalities*, Neuron, 113, 1110–1120.e3, [doi:10.1016/j.neuron.2025.01.017](https://doi.org/10.1016/j.neuron.2025.01.017), Supplemental Methods S3, Equations S16–S17, p. 12. These are high threshold, volume-dominated approximations.

[^p3-processing]: Mainali et al. (2025), *Universal statistics of hippocampal place fields across species and dimensionalities*, Neuron, 113, 1110–1120.e3, [doi:10.1016/j.neuron.2025.01.017](https://doi.org/10.1016/j.neuron.2025.01.017), STAR Methods, “Data processing,” “Parameter inference,” “Fields in 3D,” “Number of local peaks within a field,” and “Maximum firing rate vs. field width,” pp. e2–e3; Figures 1F, 2, 5D.

[^p3-fit-tests]: Mainali et al. (2025), *Universal statistics of hippocampal place fields across species and dimensionalities*, Neuron, 113, 1110–1120.e3, [doi:10.1016/j.neuron.2025.01.017](https://doi.org/10.1016/j.neuron.2025.01.017), Figure 1C–F; STAR Methods, “Fields in 1D,” “Kurtosis and skew,” Equations 6–7, pp. e2–e3. Centered moment notation is made explicit here.

[^p3-supp-tests]: Mainali et al. (2025), *Universal statistics of hippocampal place fields across species and dimensionalities*, Neuron, 113, 1110–1120.e3, [doi:10.1016/j.neuron.2025.01.017](https://doi.org/10.1016/j.neuron.2025.01.017), Figures S1–S2 and S5, supplemental pp. 1–3, 6–7. Curvature comparisons use local surface derivatives; the empirical surface representation does not supply an exact analytic reconstruction of every field surface.

[^p3-trends]: Mainali et al. (2025), *Universal statistics of hippocampal place fields across species and dimensionalities*, Neuron, 113, 1110–1120.e3, [doi:10.1016/j.neuron.2025.01.017](https://doi.org/10.1016/j.neuron.2025.01.017), Figure 4A–B and accompanying text, p. 1116; Figure S3, supplemental p. 4.

[^p3-threshold-variation]: Mainali et al. (2025), *Universal statistics of hippocampal place fields across species and dimensionalities*, Neuron, 113, 1110–1120.e3, [doi:10.1016/j.neuron.2025.01.017](https://doi.org/10.1016/j.neuron.2025.01.017), Figure S4 and caption, supplemental p. 5; “Parameter variation across experiments,” p. 1116. The threshold distribution is positive-conditioned skew normal, its mean fixed to the baseline fit and its two remaining parameters fitted to correlations.

[^p3-wiring-source]: Mainali et al. (2025), *Universal statistics of hippocampal place fields across species and dimensionalities*, Neuron, 113, 1110–1120.e3, [doi:10.1016/j.neuron.2025.01.017](https://doi.org/10.1016/j.neuron.2025.01.017), Supplemental Methods S2, Equations S2–S8, pp. 9–10; Figure 1B. The Gaussian autocorrelation integral is evaluated explicitly here.

[^p3-discussion]: Mainali et al. (2025), *Universal statistics of hippocampal place fields across species and dimensionalities*, Neuron, 113, 1110–1120.e3, [doi:10.1016/j.neuron.2025.01.017](https://doi.org/10.1016/j.neuron.2025.01.017), Discussion, pp. 1117–1118. The distinction between a sufficient mechanism and a uniquely identified mechanism is this guide's inference from the model and measurement scope.

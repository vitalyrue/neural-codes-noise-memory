# Why the eyes drift during fixation {#ch:EYE-DRIFT}

Looking steadily at a small spot does not hold the eye perfectly still. Between brief, rapid movements called [**microsaccades**]{.definition-term custom-style="Definition Term"}, the eye makes a small, smooth, irregular movement called [**fixational drift**]{.definition-term custom-style="Definition Term"}. Does this movement begin as noise in the muscles, or does the brain send a changing command to them? Ben-Shushan and colleagues answer this in two stages. Their recordings support a large shared drive upstream of the motor neurons. Their model then proposes a particular source: random motion of the eye position stored in a memory circuit.[^p2-question]

This distinction connects the previous chapters to a measurement outside the brain. A memory coordinate can diffuse inside a neural network, but the movement produced by that coordinate also depends on the muscles and the mechanics of the eye. We need to follow the signal through those stages before comparing a neural diffusion law with an eye trajectory.

## From stored eye position to muscle action {#sec:EYE-PATHWAY}

The eye needs an ongoing command to maintain a position. A brief command to move is therefore insufficient: after the movement, a circuit must maintain activity representing the new position. The [**oculomotor integrator**]{.definition-term custom-style="Definition Term"} is the neural circuit that performs this storage. “Integrator” refers to turning a movement command into a lasting position signal. In the proposed mechanism, the continuous attractor described in Chapters 1 and 2 stores horizontal eye position. Noise moves the stored value along that attractor.[^p2-pathway]

The signal reaches [**ocular motoneurons (OMNs)**]{.definition-term custom-style="Definition Term"}, neurons whose spikes activate the eye muscles. The recordings came from the [**abducens nucleus**]{.definition-term custom-style="Definition Term"}, a group of brainstem neurons that includes OMNs activating the lateral rectus muscle, which turns the eye outward. Other neurons in that nucleus carry signals to other neurons rather than directly to muscle. The study separated these cell types using their eye movement response parameters. Finally, the muscles and the mechanical properties of the eye, together called the [**ocular plant**]{.definition-term custom-style="Definition Term"}, turn neural activity into movement.[^p2-recordings]

There are three possible contributions to an observed drift: a changing shared command sent to many OMNs, private spike variability in individual OMNs, and variability after those neurons, including muscle and measurement noise. Private spike fluctuations can partly cancel when many neurons act together. A common command survives this averaging. This is why the noisy activity of one neuron can reveal a source that dominates the much smoother eye movement.

## What the recordings can and cannot reveal {#sec:EYE-RECORDINGS}

The authors reanalyzed earlier experiments in two male rhesus macaques. The animals first fixated a stationary target and then tracked a moving target. A wire search coil on one eye measured eye position while an electrode recorded one neuron's spikes. There were 57 identified OMNs. Each recording paired one OMN with eye movement; there were no simultaneous recordings of multiple OMNs. Thus the analysis cannot directly measure the covariance between two recorded motor neurons.[^p2-recordings][^p2-single]

The initial stationary target was followed by 500–700 ms of required fixation before the target stepped and began moving. Neural voltage was sampled at 25 kHz and eye position at 1 kHz. The authors detected microsaccades using eye speed and acceleration, removed 30 ms on each side of them, and manually checked the remaining segments. For the main displacement analysis, segments shorter than 350 ms were excluded and longer ones were split into nonoverlapping 350 ms pieces. There were 302 such pieces per cell on average, with different counts across cells. These repeated observations improve estimates within two animals; they do not create 57 independent animal samples.[^p2-segments]

The large movements have a useful role even though the scientific question concerns tiny drifts. They produce enough rate change to estimate how each cell's activity depends on eye movement. The fitted relationship is then applied during fixation. This transfer is an assumption to examine, because an incorrect [**gain**]{.definition-term custom-style="Definition Term"} during drift would change the inferred common variance. Gain is the scale that converts a change in one signal into a change in the other.

The diagram separates the physical pathway from the paired recordings and the later calculation of predicted eye position.

<div class="figure-scroll">

{{block:fig:EYE-PHYSICAL-AND-RECORDED}}

</div>

The upper path describes a possible physical source and its output. The recording design provides one cell and eye movement at a time; it does not measure covariance between simultaneously recorded motor neurons. The predicted position is a later analysis result, not a signal sent backward through the physical pathway.

## Fitting movement to firing rate {#sec:EYE-FORWARD-FIT}

Position alone does not predict a motor neuron's activity during a movement. At the same position, firing can differ when the eye is moving or accelerating. The paper therefore fits

$$
\widehat f(t)=k[E(t+\Delta t)-E_T]
 +r\dot E(t+\Delta t)+m\ddot E(t+\Delta t).
$$

Here $E$ is horizontal eye position in degrees and $\widehat f$ is predicted firing rate in spikes/s. The position threshold $E_T$ sets where the position term reaches zero. The coefficients have units

$$
[k]=\frac{\text{spikes}}{\text{s}\,\text{deg}},\qquad
[r]=\frac{\text{spikes}}{\text{deg}},\qquad
[m]=\frac{\text{spikes}\,\text{s}}{\text{deg}}.
$$

Multiplying by position, velocity, and acceleration gives spikes/s in all three terms. The delay $\Delta t$ is in seconds: firing at time $t$ predicts movement at the later time $t+\Delta t$ for a positive neural lead. This is the paper's Eq. 2, including its threshold and time shift.[^p2-forward]

The observed rate $f(t)$ was estimated as the inverse of the interval between successive spikes, constant between those spikes. For each cell, the authors minimized the sum of squared rate errors,

$$
L=\sum_{a=1}^{n_{\rm trials}}\sum_{t_j\in[0,T_a]}
\left[f_a(t_j)-\widehat f_a(t_j;k,r,m,\Delta t,E_T)\right]^2.
$$

$a$ labels trials and $T_a$ is trial duration. This is Eq. 3 with the trial count renamed so that it cannot be confused with a neuron count. Fits used full trials, including fixation and pursuit. To predict a trial's rate, that trial was left out of the parameter fit. Acceleration was estimated from velocity after local polynomial smoothing over 21 ms. Trials in which the rate fell below 20 Hz were discarded: the linear formula is intended for active cells above firing threshold, whereas firing cannot become negative.[^p2-forward]

During fixation, the authors subtracted each segment's mean firing rate, joined the segments, and compared observed and predicted rate fluctuations. Figure 1c illustrates a weak relationship for one cell; Fig. 1d shows a positive population effect. The one sided test asks whether the mean correlation is positive, compared with a zero-mean reference. Its [**p value**]{.definition-term custom-style="Definition Term"} is the probability, under that reference, of a test statistic at least as large as observed. Across 57 cells it gave $p=3\times10^{-9}$. A weak single cell relationship is expected here because the tiny movement produces small rate changes against much larger spike variability. This is the first evidence of a relationship, before any estimate of the fraction of common motion.[^p2-rate-result]

## Putting spikes in units of eye position {#sec:EYE-INVERSE-FILTER}

To ask how much eye movement is shared with a neuron, it helps to express both signals in degrees. The paper reverses the fitted relationship: a cell's spike train becomes the input, and its prediction of eye position becomes the output. This operation is an inverse of the movement-to-rate fit, rather than a new fit to small drift residuals.

Let $x(t)=E(t)-E_T$. Ignoring the time shift for a moment, the deterministic relation is

$$
m\ddot x+r\dot x+kx=f.
$$

A [**causal filter**]{.definition-term custom-style="Definition Term"} computes its present output from present and past input. For the equation above, its [**impulse response**]{.definition-term custom-style="Definition Term"} $h_0(u)$ is the position response to one instantaneous spike at time zero. To factor the equation, consider a time component $e^{pt}$: differentiation multiplies it by $p$. The algebraic ratio of output to input for that component is

$$
H_0(p)=\frac{1}{mp^2+rp+k}
=\frac{1}{m(p+1/\tau_+)(p+1/\tau_-)}.
$$

Factoring the quadratic gives the slow and fast decay times

$$
\tau_+=\frac{2}{r/m-\sqrt{(r/m)^2-4k/m}},\qquad
\tau_-=\frac{2}{r/m+\sqrt{(r/m)^2-4k/m}}.
$$

These are the paired signs in the paper's Eq. 7, with $\tau_+>\tau_-$ when $k,r,m>0$ and $r^2>4km$. In this case both components decay without oscillation. The same factorization gives two useful identities:

$$
\tau_+\tau_-=\frac{m}{k},\qquad
\tau_++\tau_-=\frac{r}{k}.
$$

We can obtain the response to a spike directly from the differential equation. After the spike, the input is zero, and each of the two exponentials solves the remaining homogeneous equation. Write their combination as

$$
h_0(u)=A e^{-u/\tau_+}+B e^{-u/\tau_-},\qquad u>0.
$$

To find $A$ and $B$, treat the spike as a short pulse of unit area and shrink its duration to zero. The position change during that pulse tends to zero, so $h_0(0^+)=0$. Integrating $m h_0''+r h_0'+k h_0$ across the pulse gives $m h_0'(0^+)=1$: the velocity changes by $1/m$, while position and velocity before the causal response are zero. Therefore

$$
A+B=0,\qquad
-\frac{A}{\tau_+}-\frac{B}{\tau_-}=\frac1m.
$$

Substituting $B=-A$ gives $A(1/\tau_- -1/\tau_+)=1/m$, hence $A=\tau_+\tau_-/[m(\tau_+-\tau_-)]$. Making the response zero before the spike gives

$$
h_0(u)=\frac{\Theta(u)}{m}\,
\frac{\tau_+\tau_-}{\tau_+-\tau_-}
\left(e^{-u/\tau_+}-e^{-u/\tau_-}\right).
$$

$\Theta(u)$ is zero for $u<0$ and one for $u>0$; it imposes causality. Restoring the fitted neural lead delays this response: $h(u)=h_0(u-\Delta t)$. Write the spike train as $\xi(t)=\sum_j\delta(t-t_j)$, where $\delta$ is an ideal instantaneous impulse of unit area, so integration over one spike counts one event. The prediction is

$$
\widehat E(t)=E_T+\int_{-\infty}^{t}h(t-v)\xi(v)\,dv
=E_T+\sum_j h(t-t_j).
$$

These expressions reproduce Eqs. 4–6, including the factor $\tau_+\tau_-/m$ and the delay. The [**convolution**]{.definition-term custom-style="Definition Term"} integral adds the responses to all past spikes. With spike count treated as a count, $\xi$ has units spikes/s and $h$ has units degrees/spike. Each spike contributes a decaying position response; adding those responses produces degrees.[^p2-inversion]

The kernel's area checks its normalization:

$$
\int_0^\infty h_0(u)\,du
=\frac{\tau_+\tau_-}{m(\tau_+-\tau_-)}(\tau_+-\tau_-)
=\frac1k.
$$

Thus a constant input rate $f_0$ predicts $E_T+f_0/k$, exactly the static forward relation. A kernel with unit area would give the wrong conversion unless $k$ had already been absorbed into the input. When the two decay times coincide, $r^2=4km$, the limit is $h_0(u)=\Theta(u)u e^{-u/\tau}/m$. The distinct exponential formula is used for the fitted responses in the paper.

For a constructed example, take $k=4$ spikes/(s deg), $\tau_+=0.120$ s, and $\tau_-=0.005$ s. The identities above require $r=0.500$ spikes/deg and $m=0.00240$ spikes s/deg. Then

$$
h_0(u)=2.174\left(e^{-u/0.120}-e^{-u/0.005}\right)
\ \text{deg/spike},\quad u>0,
$$

and its area is $2.174(0.120-0.005)=0.250$ deg s/spike, equal to $1/k$. A steady rate of 80 spikes/s predicts an offset of 20 degrees above $E_T$. This checks the gain as well as the time constants; it is not a fit to a recorded cell.

Figure 2a–b shows typical fitted times of about 5 ms and 120 ms. Figure 2c shows that a single cell's reconstructed drift is much noisier than the measured movement. Across 350 ms displacement pairs, the mean Pearson correlation was $\langle R\rangle=0.17\pm0.02$, where the error is the [**standard error of the mean (SEM)**]{.definition-term custom-style="Definition Term"}. SEM estimates uncertainty in the across-cell mean, rather than the spread of individual cells or uncertainty across animals. The one sided test gave $p=3.8\times10^{-12}$. Shuffling which measured segment was paired with which spike prediction centered the comparison near zero. Here and below $\langle\cdot\rangle$ over cells means a population average.[^p2-correlation]

## Why a small correlation implies shared variation {#sec:EYE-SHARED-VARIANCE}

A correlation of 0.17 does not immediately tell us how much motion comes from the common command. First we can ask a more limited question: could all the motion come from independent motor neuron fluctuations?

For a centered displacement $Y$ and one centered prediction $X$, the best linear prediction $bX$ minimizes $\operatorname{Var}(Y-bX)$. Differentiating with respect to $b$ gives $b=\operatorname{Cov}(X,Y)/\operatorname{Var}(X)$. Its explained fraction of variance is

$$
\frac{b^2\operatorname{Var}(X)}{\operatorname{Var}(Y)}
=\frac{\operatorname{Cov}(X,Y)^2}{\operatorname{Var}(X)\operatorname{Var}(Y)}
=R^2.
$$

This is the [**coefficient of determination**]{.definition-term custom-style="Definition Term"} for a linear prediction with a fitted gain. It does not assert that the raw, unscaled position predictor itself has a small squared error.

Suppose there are $N_m$ independent single neuron predictors $X_i$. Standardize each to variance one and also standardize $Y$. Independence makes the $X_i$ uncorrelated, so the residual after using them all has variance

$$
\operatorname{Var}\left(Y-\sum_i R_iX_i\right)
=1-2\sum_iR_i^2+\sum_iR_i^2
=1-\sum_iR_i^2\ge0.
$$

Consequently $\sum_iR_i^2\le1$, and an average neuron explains at most $1/N_m$. This proves the bound used in Supplementary Eq. S1. It does not require equal muscle effects from all neurons. Applying it to the sampled cells does require their average explanatory power to represent the relevant motor population.[^p2-independent-bound]

The authors avoid directly averaging noisy squared correlations. Instead,

$$
\langle R^2\rangle-\langle R\rangle^2=\operatorname{Var}(R)\ge0,
\qquad
\langle R^2\rangle\ge(0.17)^2=0.0289.
$$

Thus the estimated mean correlation implies an average explained fraction of at least about 2.9%. For 1,000 independently contributing motor neurons, the bound would be 0.1%; for several thousand it is smaller. The mismatch argues against independent OMN noise as the sole source. Shared fluctuations can allow many cells to explain the same part of the movement, so their explained fractions can overlap.[^p2-independent-bound]

This step finds shared variation. Locating its source upstream also uses a biological premise: the private variability generated within OMNs is taken to be independent across cells. The paper supports that premise using anatomical and stimulation studies indicating little local recurrent coupling in the relevant motor nuclei. It was not tested by simultaneous recordings in this data set. Common inputs can correlate the total activity of OMNs even when their privately generated spike noise is independent.[^p2-independence]

## The fraction driven by the common command {#sec:EYE-CHI}

The variance bound establishes that a shared signal exists, but leaves its size open. The next calculation uses the fact that the inverse filter has a calibrated gain in degrees. For one 350 ms interval, write the measured displacement and the single cell prediction as

$$
Y=\delta E=C+\eta,\qquad
X=\delta\widehat E=C+\epsilon,
$$

where $C=\delta E_C$ is the common upstream contribution, $\eta$ combines motor neuron, muscle, and measurement contributions to measured displacement, and $\epsilon$ is the prediction error from the individual cell. All are displacement variables in degrees. The assumptions are that the common contribution enters both signals with unit gain, meaning the same one-for-one displacement scale, and that $C,\eta,\epsilon$ are pairwise uncorrelated to the required accuracy.

Expanding the covariance shows exactly what those assumptions buy:

$$
\operatorname{Cov}(X,Y)=\operatorname{Var}(C)
+\operatorname{Cov}(C,\eta)+\operatorname{Cov}(\epsilon,C)
+\operatorname{Cov}(\epsilon,\eta)
\simeq\operatorname{Var}(C).
$$

The common fraction is therefore estimated by

$$
\chi=\frac{\operatorname{Var}(C)}{\operatorname{Var}(Y)}
\simeq\frac{\operatorname{Cov}(X,Y)}{\operatorname{Var}(Y)}.
$$

These are Eqs. 11–15 in displacement form. The gain assumption requires that the relation calibrated during larger movements still applies during drift. There is also a small covariance between $\epsilon$ and $\eta$, because the recorded neuron's private spikes contribute both to its predictor and to actual eye motion. The paper neglects this contribution as order $1/N_m$ under its many neuron model.[^p2-chi-method]

Correlation divides the same covariance by a different denominator:

$$
R=\frac{\operatorname{Cov}(X,Y)}{\sqrt{\operatorname{Var}(X)\operatorname{Var}(Y)}},
\qquad
\chi\simeq R\sqrt{\frac{\operatorname{Var}(X)}{\operatorname{Var}(Y)}}.
$$

Large private noise in a cell inflates $\operatorname{Var}(X)$ and makes $R$ small. It need not make the common contribution to the real movement small, because many independent private contributions average down there.

**Example: correlation 0.17 with a common fraction 0.82.** These numbers are constructed to expose the distinction, not extracted from individual cells. Take independent centered variables with

$$
\operatorname{Var}(C)=0.00820\ \text{deg}^2,\quad
\operatorname{Var}(\eta)=0.00180\ \text{deg}^2,\quad
\operatorname{Var}(\epsilon)=0.22446\ \text{deg}^2.
$$

Then $\operatorname{Var}(Y)=0.01000$, $\operatorname{Var}(X)=0.23266$, and $\operatorname{Cov}(X,Y)=0.00820$, all in deg$^2$. It follows that

$$
R=\frac{0.00820}{\sqrt{0.01000\times0.23266}}\simeq0.170,
\qquad \chi=\frac{0.00820}{0.01000}=0.820.
$$

One cell explains $R^2\simeq2.89\%$ of displacement variance after linear rescaling, while the common signal supplies 82% of actual displacement variance. The larger, poorly predicted part of the single cell signal is private prediction noise.

The constructed variance example above gives a small correlation even though the common command supplies most of the movement variance.

<div class="figure-scroll">

{{block:fig:EYE-SHARED-PRIVATE-VARIANCE}}

</div>

Private prediction noise enlarges the denominator of R without changing the covariance. The bars use the same physical scale, so the equal common pieces have equal lengths. See [Shared and private variability, Eqs. 11–15, p. 10](../papers/ben-shushan-2022-fixational-drift.pdf#page=10).

In the experiment, each cell gives a noisy estimate $\chi_i$, and those estimates can lie outside $[0,1]$. The underlying variance fraction remains in that interval under the model, but the sample covariance need not. The paper estimates each standard error $\Delta\chi_i$ mainly from covariance uncertainty, treating the measured displacement variance in the denominator as comparatively well determined. It then uses inverse variance weighting:

$$
w_i=\frac{1}{(\Delta\chi_i)^2},\qquad
\widehat\chi=\frac{\sum_iw_i\chi_i}{\sum_iw_i},\qquad
\sigma_{\widehat\chi}=\left(\sum_iw_i\right)^{-1/2}.
$$

To see the weighting, let normalized weights $a_i$ sum to one. Independent errors give variance $\sum_i a_i^2(\Delta\chi_i)^2$ for $\sum_i a_i\chi_i$. Minimizing this subject to $\sum_i a_i=1$ gives $a_i\propto1/(\Delta\chi_i)^2$ and the error above. The paper additionally assumes approximately normal errors around a common value. The last expression is a propagated estimation error under those assumptions. It does not measure variation across animals or uncertainty in the gain and independence assumptions. The reported result was $0.82\pm0.07$, a weighted mean and weighted error for horizontal displacement over 350 ms. It is neither a fraction of distance traveled nor the fraction that one neuron's spikes accurately predict.[^p2-chi-error]

## Separating measurement noise from movement in the MSD {#sec:EYE-MEASUREMENT-NOISE}

The common variance calculation uses one interval length. To learn what kind of process drives motion, the authors next compare displacements at many time separations. As in Chapter 1,

$$
M(\ell)=\mathbb E\{[E(t+\ell)-E(t)]^2\}
$$

is the mean squared displacement, or MSD, at lag $\ell$. The data estimate it within each microsaccade free segment, then average the available segment estimates at each lag. Larger lags have fewer eligible segments. The 1 ms sampling sets the available lag spacing.[^p2-msd]

At short lags, the displacement can be smaller than the search coil's measurement error. Suppose its reading is $E_{\rm obs}(t)=E(t)+\nu(t)$, where the measurement error has zero mean, variance $\sigma_m^2$, is independent of true movement, and is uncorrelated between distinct sampled times. For a positive lag,

$$
\begin{aligned}
M_{\rm obs}(\ell)
&=\mathbb E[(\delta E+\delta\nu)^2]\\
&=M(\ell)+\mathbb E[\nu(t+\ell)^2]+\mathbb E[\nu(t)^2]
-2\mathbb E[\nu(t+\ell)\nu(t)]\\
&=M(\ell)+2\sigma_m^2.
\end{aligned}
$$

The mixed movement-error term vanishes by independence. This is Eqs. 18–19. The correction is the variance of a difference of two errors, $2\sigma_m^2$, rather than the variance of a single position error. At exactly zero lag the same error is subtracted from itself, so the MSD is zero. A positive lag plateau near zero lag can still occur when successive measurement errors are independent.[^p2-msd-noise]

The authors estimated the plateau contribution at order $10^{-3}$ deg$^2$, checked its scale with a coil fixed in space, and subtracted that contribution from the observed MSD. This is a correction of an average statistic, not knowledge of each trial's unknown noise. Smoothing the eye trajectories instead would also change the movement statistics the analysis seeks to measure. If the plateau estimate has uncertainty $10^{-4}$ deg$^2$, a corrected MSD of that size is unreliable even when the plateau itself is much larger. The peer review response uses this example to explain the shortest lag limitation.[^p2-noise-limit]

For instance, a constructed measured MSD of $0.0014$ deg$^2$ with an estimated noise contribution $0.0010$ deg$^2$ leaves $0.0004$ deg$^2$. A $0.0001$ deg$^2$ uncertainty in the subtraction is already 25% of that result. This is why a corrected short lag point needs an uncertainty assessment as well as a positive value. If measurement errors were temporally correlated, the correction would instead be $2[\sigma_m^2-C_\nu(\ell)]$, where $C_\nu$ is their covariance at lag $\ell$; a constant subtraction would then need revision.

For a constructed Brownian movement with $D=0.010$ deg$^2$/s, adding independent position measurement errors with $2\sigma_m^2=0.0010$ deg$^2$ shifts every positive-lag MSD upward by the same amount.

<div class="figure-scroll">

{{block:fig:EYE-MSD-MEASUREMENT-OFFSET}}

</div>

The offset comes from two independent position errors, one at each endpoint. Its removal changes the average MSD; it does not recover each trajectory’s unknown error. The Brownian movement is chosen only to make the constant offset visible. See [Measurement noise correction, Eqs. 18–19, p. 10](../papers/ben-shushan-2022-fixational-drift.pdf#page=10).

## Filtering white noise and filtering Brownian motion differ {#sec:EYE-FILTERED-MSD}

The corrected MSD keeps increasing over the observed range, toward a second, while its logarithmic slope decreases and remains between one and two. Define that local slope by

$$
\alpha(\ell)=\frac{d\log M(\ell)}{d\log\ell}
=\frac{\ell M'(\ell)}{M(\ell)}.
$$

Ordinary diffusion has $M=2D\ell$ and $\alpha=1$. A roughly constant velocity over a short interval gives displacement $v\ell$ and $M=\mathbb E[v^2]\ell^2$, so $\alpha=2$. Growth faster than linear is called [**superdiffusion**]{.definition-term custom-style="Definition Term"}. Here it describes a finite range of lags; it does not assert a single power law for arbitrarily long times.[^p2-msd-result]

Could temporally uncorrelated motor noise acquire the observed MSD just by passing through muscles? A [**low pass filter**]{.definition-term custom-style="Definition Term"} suppresses rapid input changes relative to slow ones. [**White noise**]{.definition-term custom-style="Definition Term"} here is an ideal zero mean input whose fluctuations at different times are uncorrelated. In continuous time its strength is defined by an intensity multiplying a delta function, rather than a finite variance at an individual time. A stable, decaying response to this noise produces a [**stationary process**]{.definition-term custom-style="Definition Term"} in the sense needed here: its mean is constant and its covariance depends only on time separation. Its position variance consequently does not grow with absolute time. Let $E=h*\xi$, where

$$
\mathbb E[\xi(t)\xi(t')]=A\delta(t-t').
$$

The noise intensity $A$ has units input$^2$ times seconds. Expanding the convolution and using the delta function yields, for $\ell\ge0$,

$$
C_E(\ell)=\mathbb E[E(t)E(t+\ell)]
=A\int_0^\infty h(u)h(u+\ell)\,du.
$$

For a stationary centered position, expanding the squared difference then gives

$$
M(\ell)=2[C_E(0)-C_E(\ell)].
$$

If the kernel decays sufficiently rapidly, its overlap with a shifted copy tends to zero. The MSD consequently approaches $2C_E(0)$, a finite plateau. This reconstructs the reasoning of Eqs. 20–22.[^p2-white-noise]

For the one exponential filter $h(u)=\Theta(u)e^{-u/\tau}/\tau$,

$$
C_E(\ell)=\frac{A}{2\tau}e^{-\ell/\tau},\qquad
M_{\rm white}(\ell)=\frac A\tau(1-e^{-\ell/\tau}).
$$

This simple filter has a short lag MSD proportional to $\ell$ and a long lag plateau. A double exponential filter is smoother at short lags, but still gives a plateau because its kernel also decays. Increasing $A$ raises the curve without removing its flattening. The paper's simulated private OMN noise, passed through muscle dynamics, is both too small and too flat at long lags. In Fig. 3b, using 2,000 heterogeneous OMNs, its contribution is about 1% of the observed variance near 900 ms.[^p2-msd-result]

Now suppose the input is a stored position $B(t)$ undergoing Brownian motion with $\mathbb E[(B(t+\ell)-B(t))^2]=2D\ell$. Its position variance accumulates. A low pass filter with nonzero static gain smooths the path while retaining that accumulating long time displacement variance. The following one exponential example is a teaching reconstruction, not the paper's full muscle model. It derives how smooth movement can have a slope between one and two even though the stored position undergoes ordinary diffusion.

Let

$$
\tau\dot E+E=B,\qquad dB=\sqrt{2D}\,dW.
$$

$W$ is a Brownian process with unit increment variance per unit time, so $D$ has units deg$^2$/s. Define velocity $v=\dot E=(B-E)/\tau$. Taking its increment gives

$$
\tau\,dv=-v\,dt+\sqrt{2D}\,dW.
$$

Velocity loses its past value over time $\tau$ and receives new random input. After its velocity transient has decayed, its solution is

$$
v(t)=\frac{\sqrt{2D}}{\tau}\int_{-\infty}^{t}e^{-(t-u)/\tau}\,dW(u),
\qquad
C_v(s)=\frac D\tau e^{-|s|/\tau}.
$$

The covariance follows by multiplying the two integrals: only their shared increments contribute, with the same exponential overlap as in the white noise calculation. Integrating velocity over an interval gives position change. The double integral over its covariance reduces to

$$
\begin{aligned}
M_{\rm Brownian}(\ell)
&=\int_0^\ell\int_0^\ell C_v(u-v)\,du\,dv\\
&=2\int_0^\ell(\ell-s)C_v(s)\,ds\\
&=2D[\ell-\tau(1-e^{-\ell/\tau})].
\end{aligned}
$$

At short lags, $1-e^{-\ell/\tau}=\ell/\tau-\ell^2/(2\tau^2)+\cdots$, so

$$
M_{\rm Brownian}(\ell)\simeq(D/\tau)\ell^2.
$$

The eye keeps approximately the same velocity over that interval. At long lags,

$$
M_{\rm Brownian}(\ell)\simeq2D(\ell-\tau),
$$

which grows linearly rather than approaching a plateau. Its local slope is

$$
\alpha(\ell)=\frac{\ell(1-e^{-\ell/\tau})}
{\ell-\tau(1-e^{-\ell/\tau})},
$$

approaching two at short lags and one at long lags. At $\ell=\tau$ it is $e-1\simeq1.718$; at $\ell=5\tau$ it is about $1.239$. Thus an intermediate slope can arise from filtering ordinary diffusion, without faster than Brownian accumulation inside the memory circuit.

The curves compare the two inputs after the same filter with one exponential response, also called a one pole filter.

<div class="figure-scroll">

{{block:fig:EYE-FILTERED-NOISE-MSD}}

</div>

The white-input short-lag slope of one belongs to this one-pole example.

The actual muscle response contains fast and slow exponential components, and the full model also contains motor neuron filtering and feedback. Those ingredients change the detailed curve. The one exponential derivation teaches the distinction relevant to Fig. 3: a decaying low pass filter of stationary white noise saturates, whereas the same filter, with nonzero static gain, retains accumulating displacement from a wandering position. A slow correlated peripheral source is a different hypothesis from the temporally uncorrelated noise rejected by this comparison.

## The proposed circuit from memory to movement {#sec:EYE-CIRCUIT-MODEL}

The recording analysis places much of the drive upstream of OMNs. To test whether integrator noise could supply it, the authors build a model from a noisy memory circuit through to the eye. The model adapts an earlier goldfish integrator architecture to primate tuning and variability. There are two populations, with excitation within each and inhibition between them. Their firing increases for opposite directions of gaze. This supplies the recurrent interaction needed to maintain a range of stored positions.[^p2-network]

For the right population, the model's rate is

$$
\lambda_i^R(t)=\left[\zeta_i^R E_{OI}(t)+\lambda_i^0+\zeta_i^R F(t)\right]_+,
\qquad [a]_+=\max(a,0).
$$

$E_{OI}$ is the internally represented position in degrees, $\zeta_i^R$ is a tuning slope in spikes/(s deg), and $\lambda_i^0$ is a rate offset in spikes/s. Taking the maximum with zero prevents negative firing. $F$ is a feedback input in degrees, defined below. The matching left neuron has the opposite slope, $\zeta_i^L=-\zeta_i^R$. In an active neuron, a change of one degree changes its rate by $\zeta_i$.

Spikes produce synaptic activity according to

$$
\tau_s\dot S_i^R=-S_i^R+X_i^R,\qquad
X_i^R(t)=\frac{\xi_i^R(t)}{\lambda_t+\lambda_i^R(t)},\qquad
E_{OI}(t)=\sum_i\eta_i[S_i^R(t)-S_i^L(t)].
$$

Here $\xi_i^R$ is a spike train generated at rate $\lambda_i^R$, $\tau_s$ is the synaptic decay time, and $\lambda_t=60$ Hz sets the rate scale in the nonlinear synaptic response. Treating spikes as counts, $X_i$ and $S_i$ are dimensionless, and the weights $\eta_i$ are in degrees. Between spikes, $S_i$ decays exponentially; one spike adds a jump of $1/[\tau_s(\lambda_t+\lambda_i^R)]$. Replacing spikes by their mean rate gives a drive $\lambda_i^R/(\lambda_t+\lambda_i^R)$ that approaches one as the rate increases. This is the model's saturating synaptic effect, rather than the purely linear synapses of the basic 2012 example.[^p2-network]

The readout $E_{OI}$ feeds back into the rates, so these equations define a recurrent network. Persistence requires a further condition on that feedback. Set $F=0$ and replace spikes by their mean rates. Define the mean saturated drives at a proposed stored value $z$ by

$$
q_i^R(z)=\frac{\lambda_i^R(z)}{\lambda_t+\lambda_i^R(z)},
\qquad
q_i^L(z)=\frac{\lambda_i^L(z)}{\lambda_t+\lambda_i^L(z)}.
$$

Multiply each synaptic equation by its readout weight, subtract the left contribution, and sum. Since the same $\tau_s$ applies to every unit, the readout obeys

$$
\tau_s\dot E_{OI}=-E_{OI}+G(E_{OI}),
\qquad
G(z)=\sum_i\eta_i[q_i^R(z)-q_i^L(z)].
$$

An exact continuum of persistent readout values would require $G(z)=z$ over the represented range. For a small displacement from a fixed value, Taylor expansion gives

$$
\tau_s\,\frac{d\,\delta E_{OI}}{dt}
=[G'(z)-1]\delta E_{OI}.
$$

Thus $G'(z)=1$ is the local neutral condition for the stored coordinate. Stable directions of the remaining synaptic state are also needed for an attractor. The weights were optimized to approximate the fixed-point relation across $-50$ to $50$ degrees. Residual mismatch can produce deterministic drift, so this finite optimized circuit provides approximate persistence rather than an exactly neutral continuum. The tuning slopes and thresholds were sampled to match reported macaque relationships and variation. With spikes, perturbations along the nearly neutral direction additionally accumulate. This reduction is a teaching derivation from the paper's equations; Figure 4 separates the resulting internal diffusion from later muscle smoothing.[^p2-network]

The motor neurons receive this position signal:

$$
\lambda_i^M(t)=[k_i(E_{OI}(t)-E_{T_i})]_+,
\qquad
\tau_{MN}\dot s_i^M=-s_i^M+\xi_i^M.
$$

$\lambda_i^M$ is a motor rate in spikes/s, $E_{T_i}$ is that neuron's position threshold in degrees, and $k_i$ is its position sensitivity. $\xi_i^M$ is its generated spike train. The filtered output $s_i^M$ also has units spikes/s, with decay time $\tau_{MN}$. One spike makes a jump of $1/\tau_{MN}$; at constant mean rate, the mean output is that rate.

Each motor unit's muscle and plant response is represented by a position contribution $E_i$ satisfying

$$
s_i^M=k_i(E_i-E_{T_i})+r_i\dot E_i+m_i\ddot E_i,
\qquad E=\frac1{N_m}\sum_{i=1}^{N_m}E_i.
$$

These are Eqs. 28–31. The second order equation uses the same roles and units as the forward fit. At constant $E_{OI}$, an active unit has mean $s_i^M=k_i(E_{OI}-E_{T_i})$, giving mean $E_i=E_{OI}$ when derivatives vanish. Averaging therefore transmits the common position while reducing independent private fluctuations. This is an effective model of combined motor output, not a claim that one motor unit moves an isolated eye of its own.[^p2-motor]

The model used diverse thresholds and response coefficients, with motor thresholds sampled between $-45$ and $-5$ degrees, and imposed $m_i<r_i^2/(4k_i)$ to give nonoscillatory individual response kernels. Main Methods report $N=30{,}000$ integrator neurons, $N_m=1{,}000$ OMNs, and $\tau_s=20$ ms for the main full simulation. The separate private OMN comparison in Fig. 3 used 2,000 OMNs. These neuron counts belong to different simulation comparisons.[^p2-motor]

The final loop is delayed visual feedback:

$$
F(t)=A[E(t-\tau_d)-E_{OI}(t)],
\qquad \tau_d\simeq70\ \text{ms}.
$$

Both positions are in degrees, so $A$ is dimensionless in this formulation. The main value is $A=0.015$. If gaze and its internal representation have recently moved rightward, the delayed position is to their left, making $F$ negative. Its contribution to the integrator rates then opposes continued rightward movement. The difference can serve as an estimate of recent movement; it is not an error relative to a fixed absolute target position. For a slowly varying position that the eye tracks, $E(t-\tau_d)-E_{OI}(t)\simeq-\tau_d\dot E(t)$, showing the velocity-like action and sign. The approximation requires tracking and slow change over the delay.[^p2-feedback]

The effect on the ongoing MSD must be checked from the coupled model, rather than inferred from the delay alone. A short MSD lag is a separation between two samples in a running process, not the time since a new perturbation. Past measurements can already affect both samples, and $F$ also contains the immediate term $-A E_{OI}(t)$. Extended Data Fig. 3 compares the model with and without feedback: feedback changes amplitude across lags, while its larger effect on logarithmic slope occurs at longer lags. Figure 5 shows the full model. Muscle filtering supplies the short-lag smoothness, and feedback improves the detailed longer-lag fit. These are results of this model comparison, not a hard delay-based cutoff or a claim excluding visual control under other tasks.[^p2-feedback]

## Which neural parameters set the amount of drift? {#sec:EYE-SCALING}

An agreement in amplitude is informative only if we know how much freedom the model has. The paper uses regular spike trains. Chapter 1 defined the interspike interval coefficient of variation (CV) as the interval standard deviation divided by its mean. A Poisson process at constant rate has CV one; the model uses about 0.22 for integrator neurons and about 0.07 for OMNs. Such firing is called [**sub-Poisson spiking**]{.definition-term custom-style="Definition Term"} here because its long window count variability is lower than a Poisson process at the same rate, under the interval construction used in the model.[^p2-cv]

The construction starts with a Poisson process at $M$ times the desired rate and retains every $M$th spike. At constant rate, a retained interval is the sum of $M$ independent exponential intervals. Each initial interval has mean $1/(M\lambda)$ and variance $1/(M\lambda)^2$. The retained interval therefore has mean $1/\lambda$, variance $1/(M\lambda^2)$, and CV $1/\sqrt M$. This preserves the mean rate while reducing variability. Its use at changing rates is part of the model; the simple interval derivation assumes a constant rate.

At constant rate, the retained intervals are independent. This is a [**renewal process**]{.definition-term custom-style="Definition Term"}, a spike process whose successive intervals are independent and identically distributed. Let their mean be $\mu=1/\lambda$ and standard deviation $\sigma_I$. The time to $n$ spikes has variance $n\sigma_I^2$. For a long fixed window $L\simeq n\mu$, a fluctuation in total interval time produces the opposite fluctuation in count divided by $\mu$. Thus

$$
\operatorname{Var}(n)\simeq\frac{n\sigma_I^2}{\mu^2}
\simeq\lambda L\left(\frac{\sigma_I}{\mu}\right)^2
=\lambda L\,\mathrm{CV}^2.
$$

This explains why the diffusion scale contains CV squared: it is the strength of the accumulated spike fluctuations relative to the Poisson case. Chapters 2 and 3 show how projecting those fluctuations onto a neutral memory direction adds a factor proportional to $1/\tau_s^2$ and, for a comparable independent population, $1/N$.

Rate and sensitivity need more care. Write the absolute local rate slope as $a=d\lambda/dE$, in spikes/(s deg). If $N$ similar cells fire near rate $\lambda_0$, their Poisson information per unit time about position is

$$
J\simeq\frac{Na^2}{\lambda_0}.
$$

Using the information-diffusion relation of Chapter 3 as a scale, including the $\mathrm{CV}^2$ factor just derived and holding the network geometry fixed,

$$
D\ \propto\ \frac{\mathrm{CV}^2}{\tau_s^2J}
=\frac{\mathrm{CV}^2\lambda_0}{N a^2\tau_s^2}.
$$

If instead sensitivity is expressed as the fractional slope $b=a/\lambda_0$, in inverse degrees, the same expression becomes

$$
D\ \propto\ \frac{\mathrm{CV}^2}{N\lambda_0 b^2\tau_s^2}.
$$

This second form has the dependence printed in the paper's Eq. 1,
$D\propto\mathrm{CV}^2N^{-1}\lambda_0^{-1}k_0^{-2}\tau_s^{-2}$.
However, its surrounding text calls $k_0$ position sensitivity without specifying fractional normalization. If $k_0$ means an absolute slope in Hz/degree, that printed expression has the wrong units for $D$; the version with $\lambda_0$ in the numerator has the required units deg$^2$/s. The guide therefore distinguishes $a$ and $b$ rather than silently treating the printed $k_0$ as unambiguous. This scaling is a comparison under fixed network geometry and noise assumptions, not an exact formula for every recurrent circuit.[^p2-scaling]

Doubling $N$ halves this diffusion scale; doubling CV multiplies it by four; doubling $\tau_s$ divides it by four. Doubling the absolute slope at fixed rate also divides it by four. Increasing rate reduces diffusion when the fractional slope is fixed, because more spikes then also supply a proportionally steeper absolute slope. Increasing rate at fixed absolute slope is a different comparison and increases the scale in the first formula. A rate change alone does not specify which comparison is intended.

Could the measured CV itself mostly reflect drift rather than private spike variability? Supplementary Notes test this. Let $\lambda(t)=\bar\lambda+aB(t)$ during a fixation of length $T$, with the rate changes small relative to $\bar\lambda$. For a Brownian path starting at zero, the expected time averaged squared position is $DT$, and the expected squared time mean is $2DT/3$. Subtracting gives the expected within-segment position variance $DT/3=2DT/6$:

$$
\mathbb E\!\left[\frac1T\int_0^T(B(t)-\bar B)^2dt\right]
=\frac{DT}{3}.
$$

The second term follows from $\mathbb E[B(t)B(s)]=2D\min(t,s)$ and
$T^{-2}\int_0^T\int_0^T2D\min(t,s)\,dt\,ds=2DT/3$.
Expanding $1/(\bar\lambda+aB)$ to first order gives $1/\bar\lambda-aB/\bar\lambda^2$. Dividing its standard deviation by its mean then gives

$$
\mathrm{CV}_{\rm drift}\simeq
\frac{|a|}{\bar\lambda}\sqrt{\frac{2DT}{6}}.
$$

With the supplement's values $a=1/15$ spikes/(s arcmin), $2D=100$ arcmin$^2$/s, $T=0.5$ s, and $\bar\lambda=80$ Hz, this is about $0.0024$, well below the OMN CV near 0.07. These are an order of magnitude check, not a fitted diffusion constant for the whole model. Since one degree is 60 arcmin, that $2D$ equals $0.0278$ deg$^2$/s, or $D=0.0139$ deg$^2$/s.[^p2-cv-drift]

## Reading the figures as an argument {#sec:EYE-FIGURES}

The five figures address different steps. Their agreement is easier to assess when those questions remain separate.

<div class="table-responsive">

{{block:tbl:EYE-FIGURE-GUIDE}}

</div>

The most useful supplemental comparisons are Extended Data Fig. 1 for individual uncertainty, Fig. 2 for noise subtraction and its simulated control, Fig. 3 for feedback, Fig. 4 for a no-central-drive control, and Fig. 5 for the other monkey's fit. In the no-central-drive control, $\widehat\chi=-0.09\pm0.22$ is compatible with zero; that negative estimate is sampling variation. Figures 6–8 document cell classification, segment sampling, and a rank correlation check. Figure 9 shows the heterogeneous model parameters. Figure 10 separates spiking noise passed directly to the output from spiking noise that drives diffusion inside the integrator: internal stochastic spikes remain in the latter comparison. Its caption reports little direct output-noise effect beyond 50 ms.[^p2-supp-figures]

## What remains uncertain {#sec:EYE-LIMITS}

The data and model answer different localization questions. The common variance estimate supports a drive upstream of OMNs, given the calibration and noise assumptions. The MSD comparison supports a command that accumulates variation over the measured interval, rather than stationary white noise passed through a decaying muscle filter. The circuit model shows that integrator noise with plausible parameters can generate such a command and explain its filtered amplitude and timing.

Those results do not uniquely locate the noise inside integrator neurons. No integrator neurons were recorded in this study. No selective change of that circuit tested whether it was necessary for drift. Noisy inputs to the integrator, or an already diffusive upstream signal, remain possible. The authors make this distinction in the Discussion and explicitly in their peer review response. Several combinations of neuron count, variability, and synaptic time constant can also fit an amplitude, so matching one curve does not uniquely recover those parameters.[^p2-localization]

The study's empirical scope is horizontal motion during these fixation segments in two animals. Visual tasks, feedback, and other sources of input can alter the statistics. Its contribution to the connection with the 2012 theory is more precise: a continuous memory can diffuse internally, while a mechanical output of that memory looks smooth and superdiffusive at shorter lags. To compare a memory theory with behavior, the mapping from stored value to measured movement is part of the calculation.

[^p2-question]: Ben-Shushan, N., Shaham, N., Joshua, M., & Burak, Y. (2022). *Fixational drift is driven by diffusive dynamics in central neural circuitry*. Nature Communications, 13, 1697. https://doi.org/10.1038/s41467-022-29201-y. Main pp. 1–2, abstract and introduction.

[^p2-pathway]: Ben-Shushan, N., Shaham, N., Joshua, M., & Burak, Y. (2022). *Fixational drift is driven by diffusive dynamics in central neural circuitry*. Nature Communications, 13, 1697. https://doi.org/10.1038/s41467-022-29201-y. Main pp. 5–8, “Stochastic diffusion in a memory circuit,” Figs. 4–5.

[^p2-recordings]: Ben-Shushan, N., Shaham, N., Joshua, M., & Burak, Y. (2022). *Fixational drift is driven by diffusive dynamics in central neural circuitry*. Nature Communications, 13, 1697. https://doi.org/10.1038/s41467-022-29201-y. Main p. 9, “Behavioral task and recordings”; Supplementary Information, p. 11, Extended Data Fig. 6.

[^p2-single]: Ben-Shushan, N., Shaham, N., Joshua, M., & Burak, Y. (2022). *Fixational drift is driven by diffusive dynamics in central neural circuitry*. Nature Communications, 13, 1697, peer review file, p. 19, authors' response to Reviewer 3: recordings did not contain multiple simultaneous OMNs. https://doi.org/10.1038/s41467-022-29201-y.

[^p2-segments]: Ben-Shushan, N., Shaham, N., Joshua, M., & Burak, Y. (2022). *Fixational drift is driven by diffusive dynamics in central neural circuitry*. Nature Communications, 13, 1697. https://doi.org/10.1038/s41467-022-29201-y. Main p. 4, Fig. 2 caption; pp. 9–10, “Extracting the fixational segments” and “Eye position correlation coefficients”; Supplementary Information, p. 12, Extended Data Fig. 7.

[^p2-forward]: Ben-Shushan, N., Shaham, N., Joshua, M., & Burak, Y. (2022). *Fixational drift is driven by diffusive dynamics in central neural circuitry*. Nature Communications, 13, 1697. https://doi.org/10.1038/s41467-022-29201-y. Main p. 9, “OMN firing rate estimators,” Eqs. 2–3.

[^p2-rate-result]: Ben-Shushan, N., Shaham, N., Joshua, M., & Burak, Y. (2022). *Fixational drift is driven by diffusive dynamics in central neural circuitry*. Nature Communications, 13, 1697. https://doi.org/10.1038/s41467-022-29201-y. Main p. 3, Fig. 1; p. 9, “Firing rate correlation coefficients.”

[^p2-inversion]: Ben-Shushan, N., Shaham, N., Joshua, M., & Burak, Y. (2022). *Fixational drift is driven by diffusive dynamics in central neural circuitry*. Nature Communications, 13, 1697. https://doi.org/10.1038/s41467-022-29201-y. Main p. 9, “Model inversion,” Eqs. 4–7. Factorization, units, static gain check, and repeated-pole limit are guide derivations of those equations.

[^p2-correlation]: Ben-Shushan, N., Shaham, N., Joshua, M., & Burak, Y. (2022). *Fixational drift is driven by diffusive dynamics in central neural circuitry*. Nature Communications, 13, 1697. https://doi.org/10.1038/s41467-022-29201-y. Main pp. 2–4, Fig. 2; pp. 9–10, “Eye position correlation coefficients,” Eq. 8 and shuffle procedure.

[^p2-independent-bound]: Ben-Shushan, N., Shaham, N., Joshua, M., & Burak, Y. (2022). *Fixational drift is driven by diffusive dynamics in central neural circuitry*. Nature Communications, 13, 1697. https://doi.org/10.1038/s41467-022-29201-y. Main p. 3, “Central source”; Supplementary Information, p. 2, “The explanatory power of a single OMN,” Eqs. S1–S2. The residual-variance proof is expanded here for teaching.

[^p2-independence]: Ben-Shushan, N., Shaham, N., Joshua, M., & Burak, Y. (2022). *Fixational drift is driven by diffusive dynamics in central neural circuitry*. Nature Communications, 13, 1697. https://doi.org/10.1038/s41467-022-29201-y. Main p. 7, Discussion, anatomical and stimulation support for independent intrinsic OMN variability; peer review file, pp. 19, 21, 23.

[^p2-chi-method]: Ben-Shushan, N., Shaham, N., Joshua, M., & Burak, Y. (2022). *Fixational drift is driven by diffusive dynamics in central neural circuitry*. Nature Communications, 13, 1697. https://doi.org/10.1038/s41467-022-29201-y. Main pp. 4–5, Fig. 2e–f; p. 10, Eqs. 11–15.

[^p2-chi-error]: Ben-Shushan, N., Shaham, N., Joshua, M., & Burak, Y. (2022). *Fixational drift is driven by diffusive dynamics in central neural circuitry*. Nature Communications, 13, 1697. https://doi.org/10.1038/s41467-022-29201-y. Main p. 4, Fig. 2f; p. 10, Eqs. 9, 16–17. The explanation distinguishes the reported weighted estimation error from unmodeled biological and calibration uncertainty.

[^p2-msd]: Ben-Shushan, N., Shaham, N., Joshua, M., & Burak, Y. (2022). *Fixational drift is driven by diffusive dynamics in central neural circuitry*. Nature Communications, 13, 1697. https://doi.org/10.1038/s41467-022-29201-y. Main p. 10, “Calculation of empirical MSD.”

[^p2-msd-noise]: Ben-Shushan, N., Shaham, N., Joshua, M., & Burak, Y. (2022). *Fixational drift is driven by diffusive dynamics in central neural circuitry*. Nature Communications, 13, 1697. https://doi.org/10.1038/s41467-022-29201-y. Main p. 10, “Removal of measurement noise,” Eqs. 18–19; Supplementary Information, p. 8, Extended Data Fig. 2. The plotted plateau is the displacement noise contribution, twice the single position noise variance.

[^p2-noise-limit]: Ben-Shushan, N., Shaham, N., Joshua, M., & Burak, Y. (2022). *Fixational drift is driven by diffusive dynamics in central neural circuitry*. Nature Communications, 13, 1697, peer review file, pp. 20–21, measurement noise subtraction, uncertainty example, and short lag restriction. https://doi.org/10.1038/s41467-022-29201-y.

[^p2-msd-result]: Ben-Shushan, N., Shaham, N., Joshua, M., & Burak, Y. (2022). *Fixational drift is driven by diffusive dynamics in central neural circuitry*. Nature Communications, 13, 1697. https://doi.org/10.1038/s41467-022-29201-y. Main pp. 5–6, “Central source” timing argument and Fig. 3.

[^p2-white-noise]: Ben-Shushan, N., Shaham, N., Joshua, M., & Burak, Y. (2022). *Fixational drift is driven by diffusive dynamics in central neural circuitry*. Nature Communications, 13, 1697. https://doi.org/10.1038/s41467-022-29201-y. Main p. 10, “MSD curve of low-pass filtered white noise,” Eqs. 20–22. The normalized one exponential example and filtered Brownian derivation are teaching reconstructions.

[^p2-network]: Ben-Shushan, N., Shaham, N., Joshua, M., & Burak, Y. (2022). *Fixational drift is driven by diffusive dynamics in central neural circuitry*. Nature Communications, 13, 1697. https://doi.org/10.1038/s41467-022-29201-y. Main pp. 10–11, “Oculomotor integrator network,” Eqs. 23–27; Supplementary Information, p. 13, Extended Data Fig. 9.

[^p2-motor]: Ben-Shushan, N., Shaham, N., Joshua, M., & Burak, Y. (2022). *Fixational drift is driven by diffusive dynamics in central neural circuitry*. Nature Communications, 13, 1697. https://doi.org/10.1038/s41467-022-29201-y. Main p. 11, “OMN activity and actual eye position,” Eqs. 28–33 and simulation parameters; p. 6, Fig. 3 caption, private OMN comparison.

[^p2-feedback]: Ben-Shushan, N., Shaham, N., Joshua, M., & Burak, Y. (2022). *Fixational drift is driven by diffusive dynamics in central neural circuitry*. Nature Communications, 13, 1697. https://doi.org/10.1038/s41467-022-29201-y. Main pp. 7, 9, 11, “Visual feedback,” Eq. 34; Supplementary Information, pp. 4–5 and p. 9, Extended Data Fig. 3. Some supplement cross references use earlier figure/equation numbers; p. 5 also mentions 15K integrator neurons, whereas final main Methods specify 30,000. This guide uses final main paper numbering and its main simulation parameters.

[^p2-cv]: Ben-Shushan, N., Shaham, N., Joshua, M., & Burak, Y. (2022). *Fixational drift is driven by diffusive dynamics in central neural circuitry*. Nature Communications, 13, 1697. https://doi.org/10.1038/s41467-022-29201-y. Main p. 11, “Sub-Poisson spike trains,” Eq. 35 and integrator variability specification. The interval-sum derivation expands the construction given there.

[^p2-scaling]: Ben-Shushan, N., Shaham, N., Joshua, M., & Burak, Y. (2022). *Fixational drift is driven by diffusive dynamics in central neural circuitry*. Nature Communications, 13, 1697. https://doi.org/10.1038/s41467-022-29201-y. Main p. 6, Eq. 1 and its parameter discussion; peer review file, p. 23, changes in slope, synaptic time constant, and neuron count. The absolute versus fractional slope distinction is the guide's dimensional interpretation of the printed normalization ambiguity, connected to Chapters 2–3.

[^p2-cv-drift]: Ben-Shushan, N., Shaham, N., Joshua, M., & Burak, Y. (2022). *Fixational drift is driven by diffusive dynamics in central neural circuitry*. Nature Communications, 13, 1697. https://doi.org/10.1038/s41467-022-29201-y. Supplementary Information, pp. 2–3, “Contribution of oculomotor state to the CV of OMNs,” Eqs. S3–S6. https://doi.org/10.1038/s41467-022-29201-y. Intermediate covariance integrals and numerical evaluation are expanded here.

[^p2-supp-figures]: Ben-Shushan, N., Shaham, N., Joshua, M., & Burak, Y. (2022). *Fixational drift is driven by diffusive dynamics in central neural circuitry*. Nature Communications, 13, 1697, Supplementary Information, pp. 7–14, Extended Data Figs. 1–10. https://doi.org/10.1038/s41467-022-29201-y. The no-central-drive result is Extended Data Fig. 4, p. 10; the output-noise comparison is Extended Data Fig. 10, p. 14.

[^p2-localization]: Ben-Shushan, N., Shaham, N., Joshua, M., & Burak, Y. (2022). *Fixational drift is driven by diffusive dynamics in central neural circuitry*. Nature Communications, 13, 1697. https://doi.org/10.1038/s41467-022-29201-y. Main pp. 7, 9, Discussion; peer review file, pp. 12–13, distinction between recording-based upstream localization and the integrator hypothesis. The XFA reporting summary in Supplementary File 5 was inaccessible to ordinary extraction; this guide makes no claims based on its form contents.

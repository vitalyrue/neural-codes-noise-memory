<!-- vale ai-tells.ExplainerHeadings = NO -->
# Readout accuracy depends on how a moving memory is observed {#ch:MEMORY-READOUT}
<!-- vale ai-tells.ExplainerHeadings = YES -->

<!-- vale ai-tells.EmptyPadding = NO -->
When a recall cue arrives, the stored value has already moved. Later spikes can help estimate the value present at that cue, but they cannot reveal the particular random displacements that occurred before it. Waiting for more spikes also allows the network to move further. [The question is how much observation helps when the value being read keeps changing.]{.key-statement}
<!-- vale ai-tells.EmptyPadding = YES -->

Separating the error accumulated during storage from the error of reading the cue state makes that question precise. Equal weighting of later observations shows why waiting can become harmful. Allowing for the state's motion then shows how observation can keep helping toward a limit, and how access to only some spikes changes the useful duration. The time constants and noise assumptions also need checking before the resulting limits can be compared with the paper's final error claim.

<!-- vale ai-tells.VerbTricolon = NO -->
As before, the memory coordinate is $\theta$, its initial value is $\Theta$, and its displacement variance is $2Dt$ for constant diffusion coefficient $D$ without boundaries or systematic drift. The storage delay $T$ ends at the recall cue. The observation interval $L$ begins there. The [spike information rate $J$](ch-memory-information.html#sec-memory-fi) measures how clearly nearby present states can be distinguished, and $\tau$ is the basic model's common synaptic time constant.
<!-- vale ai-tells.VerbTricolon = YES -->

## Storage loss and readout error add under specific assumptions {#sec:MEMORY-READOUT-SETUP}

**Neural question and model.** At time $T$, a recall cue arrives. The observer must estimate the original value $\Theta$, but only has access to future spikes. The network has already diffused during storage.

To solve the readout problem, the supplement approximates the [likelihood](ch-memory-information.html#sec-memory-fi) from each short bin of duration $h$ as Gaussian. Let $x=\theta(T)$ and index subsequent bins by $k$, starting with $\theta_0=x$. The increment $\eta_k$ is the change in the stored value between bins. The observation $y_k$ summarizes the bin's population spikes as an estimate of $\theta_k$, and $\epsilon_k$ is its estimation error. In this approximation, these increments and errors are independent, zero-mean Gaussian variables. The equivalent observation model is

$$
\theta_{k+1}=\theta_k+\eta_k,
\qquad y_k=\theta_k+\epsilon_k,
$$

$$
\operatorname{Var}(\eta_k)=2Dh,
\qquad \operatorname{Var}(\epsilon_k)=\frac1{Jh}.
$$

<!-- vale ai-tells.ParallelStaccato = NO -->
The value $y_k$ is inferred from spikes, not an additional directly measured physical coordinate. The continuous limit is a convenient mathematical description of the many spike, weak fluctuation regime. It does not assert that an arbitrarily short physical bin already contains enough spikes for a Gaussian fit. The derivations below are exact within this local Gaussian readout model.[^p1-read-gaussian]
<!-- vale ai-tells.ParallelStaccato = YES -->

**Mathematical derivation.** For an unbounded coordinate with constant $D$ and no drift, let $x=\theta(T)$ and let $\widehat x$ estimate that state from later spikes. Write the storage displacement as $s=x-\Theta$ and the readout error as $e=\widehat x-x$. The total recall error is their sum:

$$
\widehat x-\Theta=s+e,\qquad
\operatorname{Var}(s+e)=\operatorname{Var}(s)+\operatorname{Var}(e)
+2\operatorname{Cov}(s,e).
$$

<!-- vale ai-tells.FormalTransitions = NO -->
Assume the readout is locally unbiased at every possible $x$ and the future noise is independent of the storage history. Conditional on that history, the readout error then has mean zero. Since $s$ is fixed by the history, $\mathbb E[se]=\mathbb E[s\,\mathbb E(e\mid\text{storage history})]=0$. Both errors have zero mean, so their covariance vanishes. [In this readout model, [**translation invariance**]{.definition-term custom-style="Definition Term"} means that shifting the represented value does not change the statistics of the readout error.]{.definition-explanation} Its variance is therefore the same at every $x$. Denote it by $V_{\mathrm{read}}(L)$. Using $\operatorname{Var}(s)=2DT$ gives
<!-- vale ai-tells.FormalTransitions = YES -->

$$
V_{\mathrm{total}}(T,L)=2DT+V_{\mathrm{read}}(L).
$$

<!-- vale ai-tells.CataphoricForecasting = NO -->
**Interpretation.** The two terms describe different sources of error:
<!-- vale ai-tells.CataphoricForecasting = YES -->

- $2DT$ comes from storage.
- $V_{\mathrm{read}}(L)$ concerns estimation of $\theta(T)$ from spikes after $T$.

The supplement derives this decomposition for a locally translation invariant diffusion and readout model. State dependence, boundaries, informative priors, or uncertain initial encoding require corresponding changes.[^p1-read-setup]

A timeline separates the displacement accumulated before the cue from the error in estimating the cue state afterward.

<div class="figure-scroll">

{{block:fig:MEMORY-READOUT-TIMELINE}}

</div>



## Equal weighting becomes harmful when observation lasts too long {#sec:MEMORY-NAIVE}

**Neural question and model.** A decoder designed for a stationary state averages its observations with equal weight. That reduces independent observation noise, but late observations reflect a state that has moved further from $x$.

**Mathematical derivation.** Write $\theta(T+t)=x+B_D(t)$, where $B_D$ has Brownian covariance

$$
E[B_D(t)B_D(s)]=2D\min(t,s).
$$

The covariance arises because the two values share increments up to the earlier time. Their later increments are independent. The continuous average is

$$
\hat x_{\mathrm{naive}}=\frac1L\int_0^L y(t)dt.
$$

Count noise contributes $1/(JL)$: $n=L/h$ bins, each of variance $1/(Jh)$, give average variance $[n/(Jh)]/n^2=1/(JL)$. The motion contribution is

$$
\frac{2D}{L^2}\int_0^L\int_0^L\min(t,s)\,dt\,ds.
$$

<!-- vale ai-tells.FormalTransitions = NO -->
Split the square into its two equal triangles. On the triangle $0\le s\le t\le L$, the minimum is $s$. Therefore
<!-- vale ai-tells.FormalTransitions = YES -->

$$
\int_0^L\int_0^L\min(t,s)\,dt\,ds
=2\int_0^L\!dt\int_0^t\!s\,ds
=\int_0^L t^2dt=\frac{L^3}{3}.
$$

Combining the terms gives

$$
\boxed{V_{\mathrm{naive}}(L)=\frac{2DL}{3}+\frac1{JL}.}
$$

<!-- vale ai-tells.CataphoricForecasting = NO -->
The two contributions have opposite dependence on $L$. Differentiating,
<!-- vale ai-tells.CataphoricForecasting = YES -->

$$
\frac{dV_{\mathrm{naive}}}{dL}=\frac{2D}{3}-\frac1{JL^2}=0
\quad\Longrightarrow\quad
L_{\mathrm{naive}}^*=\sqrt{\frac3{2DJ}}.
$$

At that duration the two error terms are equal, and

$$
V_{\mathrm{naive}}^{\min}
=\frac2{\sqrt3}\sqrt{\frac{2D}{J}}.
$$

**Interpretation.** [Waiting longer eventually increases error, even with more spikes available. The problem is their equal weighting for a moving state.]{.key-statement}[^p1-naive]

## Accounting for diffusion makes readout improve toward a limit {#sec:MEMORY-IDEAL}

<!-- vale ai-tells.ParallelStaccato = NO -->
**Neural question and model.** An observer that accounts for diffusion can use later observations without confusing them with direct measurements of $x$. Their value is limited by the motion separating them from $x$. This is an ideal inference rule for an observer. The readout calculation does not demonstrate a neural circuit implementing it. Its error can be derived by combining information backward from the end of the observation interval.
<!-- vale ai-tells.ParallelStaccato = YES -->

**Mathematical derivation.** [The [**precision**]{.definition-term custom-style="Definition Term"} of a scalar Gaussian estimate is the reciprocal of its variance.]{.definition-explanation} Independent Gaussian measurements of one value add precisions. To verify this, multiply likelihoods proportional to $\exp[-(x-a)^2/(2V_a)]$ and $\exp[-(x-b)^2/(2V_b)]$: the coefficient of $x^2/2$ becomes $1/V_a+1/V_b$.

<!-- vale ai-tells.FormalTransitions = NO -->
Let $P(L)$ be the precision about the state at the beginning of an interval of length $L$, using all observations in that interval and no informative prior. Suppose we have already compressed the later part into a likelihood about the next bin's state with variance $1/P$. Bringing that likelihood one step backward adds transition variance $q=2Dh$, since the next state equals the earlier state plus an independent Gaussian increment. Its precision about the earlier state is therefore
<!-- vale ai-tells.FormalTransitions = YES -->

$$
\frac{1}{1/P+q}=\frac{P}{1+2DhP}.
$$

<!-- vale ai-tells.FormalTransitions = NO -->
The new earliest observation adds precision $Jh$. Thus, up to bin endpoint conventions that disappear as $h\to0$,
<!-- vale ai-tells.FormalTransitions = YES -->

$$
P(L+h)=Jh+\frac{P(L)}{1+2DhP(L)}.
$$

Expand the denominator for small $h$:

$$
P(L+h)=P(L)+[J-2DP(L)^2]h+O(h^2).
$$

The continuous equation and starting condition are

$$
\frac{dP}{dL}=J-2DP^2,
\qquad P(0)=0.
$$

With no observations, precision starts at zero. The term $J$ adds information from new observations. The term $2DP^2$ reduces that gain because later observations are separated from the cue state by diffusion.

For $D>0$ and $J>0$, the solution gives the readout variance at any observation duration $L>0$:

$$
\boxed{V_{\mathrm{ideal}}(L)
=\sqrt{\frac{2D}{J}}\coth(\sqrt{2DJ}\,L).}
$$

[The [**hyperbolic cotangent**]{.definition-term custom-style="Definition Term"} is $\coth z=(e^{2z}+1)/(e^{2z}-1)$.]{.definition-explanation} For positive $z$, it falls from large values toward one. This function describes how the readout variance decreases toward its limit as observation continues.

::: {.publisher-clarification-note .publisher-fold-always title="Mathematical solution: hyperbolic functions and finite-time readout error"}

[The [**hyperbolic tangent**]{.definition-term custom-style="Definition Term"} is $\tanh z=(e^z-e^{-z})/(e^z+e^{-z})$.]{.definition-explanation} [Its [**inverse hyperbolic tangent**]{.definition-term custom-style="Definition Term"} on $(-1,1)$ is $\operatorname{artanh}z=\tfrac12\log[(1+z)/(1-z)]$, whose derivative is $1/(1-z^2)$.]{.definition-explanation} Set $a=\sqrt{J/(2D)}$ and $k=\sqrt{2DJ}$. Separating variables gives

$$
\int_0^{P/a}\frac{dz}{1-z^2}=kL,
\qquad
\operatorname{artanh}(P/a)=kL.
$$

Taking the inverse function and then the reciprocal yields

$$
P(L)=\sqrt{\frac{J}{2D}}\tanh(\sqrt{2DJ}\,L),
$$

Taking the reciprocal of $P(L)$ gives the displayed finite-time readout variance.

<!-- vale ai-tells.AnthropomorphicCognition = NO -->
<!-- vale ai-tells.EmDashUsage = NO -->
The identity $\coth z=1/\tanh z$ connects this result to the finite-time variance. This backward precision derivation is a teaching reconstruction equivalent to the Gaussian covariance calculation in SI Eqs. S58–S75. It makes explicit how diffusion limits the value of later observations.[^p1-ideal]
<!-- vale ai-tells.EmDashUsage = YES -->
<!-- vale ai-tells.AnthropomorphicCognition = YES -->

For short intervals, $\coth z=1/z+z/3+O(z^3)$, so

$$
V_{\mathrm{ideal}}(L)=\frac1{JL}+\frac{2DL}{3}+O(L^3).
$$

<!-- vale ai-tells.FormalTransitions = NO -->
The naive and ideal estimators therefore agree through the displayed terms.
<!-- vale ai-tells.FormalTransitions = YES -->

:::

For long intervals,

$$
V_{\mathrm{ideal}}(L)\longrightarrow\sqrt{2D/J},
\qquad L^*=\frac1{\sqrt{2DJ}}.
$$

**Interpretation.** The ideal observer keeps improving, but the improvement becomes small. Its variance relative to the limiting variance is:

- $1.313$ at $L=L^*$.
- $1.037$ at $2L^*$.
- $1.005$ at $3L^*$.

These are variances, so their ratios are not ratios of standard deviations.

Using $2DJ\ge\tau^{-2}$ gives

$$
L^*\le\tau,
\qquad L_{\mathrm{naive}}^*=\sqrt3L^*\le\sqrt3\tau.
$$

<!-- vale ai-tells.FormalTransitions = NO -->
[Thus the paper's statement about readout within a cellular time constant concerns a characteristic saturation time under full spike access. It does not mean all benefit ends abruptly at $\tau$.]{.key-statement} The naive observer's best variance is only $2/\sqrt3\simeq1.155$ times the ideal observer's asymptotic variance. Its best standard deviation is about $1.075$ times as large.[^p1-time]
<!-- vale ai-tells.FormalTransitions = YES -->

## Limited access can make observation slower {#sec:MEMORY-PARTIAL}

**Neural mechanism.** [A downstream area may receive only some of the memory network's spikes. That reduces its information without reducing the fluctuations that already move the full memory network.]{.key-statement}

**Mathematical derivation.** If every spike is independently retained with probability $\alpha$, the observed rates and their slopes both scale by $\alpha$. Substitution in the Poisson information formula gives

$$
J_{\mathrm{obs}}=\sum_i\frac{(\alpha r_i')^2}{\alpha\bar r_i}=\alpha J.
$$

<!-- vale ai-tells.FormalTransitions = NO -->
The network diffusion coefficient stays $D$. Hence
<!-- vale ai-tells.FormalTransitions = YES -->

$$
L_{\mathrm{obs}}^*=\frac1{\sqrt{2D\alpha J}}
=\frac{L^*}{\sqrt\alpha},
\qquad
V_{\mathrm{ideal,obs}}(\infty)=\sqrt{\frac{2D}{\alpha J}}.
$$

**Interpretation.** The same factor $1/\sqrt\alpha$ multiplies the naive optimal interval and its minimum variance. The information bound implies $L_{\mathrm{obs}}^*\le\tau/\sqrt\alpha$, which can exceed $\tau$. A selected subset of neurons has exactly $\alpha J$ only when it carries that fraction of the information. A fraction of neurons or spikes chosen by a biased rule need not do so.[^p1-partial]

<div class="publisher-worked-calculation publisher-fold-always">

**Example: limited spike access changes the useful interval.**

Take $\tau=0.1\,\mathrm{s}$, $J=10{,}000\,\mathrm{rad}^{-2}\mathrm{s}^{-1}$, and $D=0.005\,\mathrm{rad}^2/\mathrm{s}$. These values attain the information bound. Full access gives $L^*=0.1\,\mathrm{s}$ and limiting readout variance $0.001\,\mathrm{rad}^2$. The naive optimum is $0.1732\,\mathrm{s}$ with variance $0.001155\,\mathrm{rad}^2$.

If $\alpha=0.1$, then $J_{\mathrm{obs}}=1000\,\mathrm{rad}^{-2}\mathrm{s}^{-1}$. The ideal characteristic interval becomes $0.3162\,\mathrm{s}$ and its limiting variance becomes $0.003162\,\mathrm{rad}^2$. The naive optimum becomes $0.5477\,\mathrm{s}$. A two second storage delay contributes $2DT=0.020\,\mathrm{rad}^2$ in both cases, giving total ideal asymptotic variances $0.021$ and $0.023162\,\mathrm{rad}^2$. Limited access leaves the storage error unchanged but increases the time and uncertainty involved in reading the cue state.

</div>

## Time scales and noise laws change the bound and its equality condition {#sec:MEMORY-EXTENSIONS}

<!-- vale ai-tells.FigurativeCarries = NO -->
**Neural mechanism.** The time constant in the inequality comes from the dynamics that carry an activation fluctuation into a lasting memory change. If both synaptic activation and firing rate adjust gradually, which time constant matters?
<!-- vale ai-tells.FigurativeCarries = YES -->

In the basic model, the firing rate changes immediately when the summed input changes. Assume symmetric weights. The extension instead lets $r_i$ approach $\phi(g_i)$ gradually, with time constant $\tau_m$, while synaptic activation still decays with time constant $\tau$.

The symbol $\xi_i$ writes the spike fluctuation as a drive in a rate-of-change equation. [[**White noise**]{.definition-term custom-style="Definition Term"} is an ideal zero-mean input whose fluctuations at different times are uncorrelated. Its continuous-time strength is defined through a delta-function covariance, rather than a finite variance at an individual time.]{.definition-explanation} In the Gaussian approximation used here, $\xi_i\,dt=\sqrt{r_i}\,dB_i$, with independent Brownian increments $dB_i$. Conditional on the current rates, its contribution over $dt$ has variance $r_i\,dt$, the same spike-count variance as in the basic model. The two dynamical equations are

$$
\dot s_i=-s_i/\tau+r_i+\xi_i,
\qquad
\tau_m\dot r_i=-r_i+\phi(g_i).
$$

**Mathematical derivation.** In this symmetric weight extension, the linear state is $(\delta\mathbf s,\delta\mathbf r)$ and its deterministic matrix is

$$
A=\begin{pmatrix}
-I/\tau&I\\
\operatorname{diag}(\phi')W/\tau_m&-I/\tau_m
\end{pmatrix}.
$$

<!-- vale ai-tells.NegatedObject = NO -->
The right tangent is $(\tau\mathbf r',\mathbf r')$. Write the left zero vector as $(\mathbf a,\mathbf b)$. The second block of $(\mathbf a^T,\mathbf b^T)A=0$ gives $\mathbf b=\tau_m\mathbf a$. The first then gives $W^T\operatorname{diag}(\phi')\mathbf a=\mathbf a/\tau$, so symmetry again permits $\mathbf a\propto\mathbf g'$. Normalizing its dot product with the right tangent yields
<!-- vale ai-tells.NegatedObject = YES -->

$$
a_i=\frac{g_i'}{(\tau+\tau_m)\sum_jg_j'r_j'}.
$$

<!-- vale ai-tells.FormalTransitions = NO -->
Only the $s$ block receives the modeled spike noise, so $2D=\sum_i a_i^2\bar r_i$. The symmetric formula consequently becomes
<!-- vale ai-tells.FormalTransitions = YES -->

$$
2D=\frac{\sum_i\bar r_i(g_i')^2}
{(\tau+\tau_m)^2[\sum_i g_i'r_i']^2},
\qquad
2D\ge\frac{J^{-1}}{(\tau+\tau_m)^2}.
$$

<!-- vale ai-tells.ParallelStaccato = NO -->
**Interpretation.** The sum of the two time constants replaces $\tau$. When one time constant is much larger, it supplies most of that sum. This result belongs to the two stage model and noise placement just described. The paper does not prove that arbitrary collections of biological time constants can always be added.[^p1-two-times]
<!-- vale ai-tells.ParallelStaccato = YES -->

**Neural question and model.** The equality condition also depends on the noise law. To see why, replace Poisson spike-count fluctuations with independent additive Gaussian noise of constant strength $q>0$:

$$
ds_i=F_i(\mathbf s)dt+\sqrt q\,dB_i.
$$

**Mathematical derivation.** The short interval observation of the mean rate is now Gaussian with variance $q/h$. Repeating the score calculation gives $J=\sum_i(r_i')^2/q$, while projection gives $2D=q\sum_i v_i^2$. The same Cauchy Schwarz proof yields $2DJ\ge\tau^{-2}$. Equality requires $v_i\propto r_i'$ because all cells have the same noise strength. In a symmetric network $v_i\propto g_i'$, so a linear transfer rule supplies the condition by keeping $\phi'(g)$ constant across participating inputs.

**Interpretation.** In the Poisson case, variance grows with rate and an exponential rule is a sufficient way to attain equality. The pointwise projection condition remains the general criterion, including the [linear-family counterexample](ch-memory-information.html#sec-memory-bound) already derived. The difference between these sufficient classes follows from the noise weighting, not from linearity being universally preferable.[^p1-gaussian]

<!-- vale ai-tells.AnthropomorphicCognition = NO -->
<!-- vale ai-tells.EmDashUsage = NO -->
This explicit $q$ formulation is a teaching reconstruction that keeps dimensions and the noise normalization visible. The supplement's Gaussian subsection establishes the change in equality condition. Here the matched noise and likelihood derivation supplies all factors of $q$ and $\tau$ without requiring the reader to infer a normalization from SI Eqs. S94–S95.
<!-- vale ai-tells.EmDashUsage = YES -->
<!-- vale ai-tells.AnthropomorphicCognition = YES -->

## Readout saturates, and one printed error bound needs qualification {#sec:MEMORY-FIG3-AND-CAUTION}

Figure 3 isolates readout uncertainty, rescaling variance by $\sqrt{2D/J}$ and duration by $L^*$. Write $z=L/L^*=\sqrt{2DJ}\,L$ for this dimensionless observation duration. In these axes the ideal curve is $\coth z$ and the naive curve is $z/3+1/z$. Both diverge like $1/z$ at short durations because too few spikes are available. The plotted features are:

- The ideal solid curve approaches one.
- The naive dashed curve reaches $2/\sqrt3$ at $z=\sqrt3$, then rises because its equal weighting gives increasing importance to displaced states.
- The dotted vertical line marks that naive optimum.

The storage delay contribution $2DT$ is not part of these rescaled curves. Figure S2 repeats the comparison for partial access, showing the rightward and upward shifts when $\alpha=0.1$.[^p1-fig3]

<details class="publisher-long-content publisher-source-figure">
<summary>Original paper figure: Burak and Fiete (2012), Figure 3</summary>
<div class="publisher-fold-body">

{{block:fig:PAPER-MEMORY-3}}

</div>
</details>

<details class="publisher-long-content publisher-source-figure">
<summary>Original paper figure: Burak and Fiete (2012), Figure S2</summary>
<div class="publisher-fold-body">

{{block:fig:PAPER-MEMORY-S2}}

</div>
</details>

<div class="figure-scroll">

{{block:fig:MEMORY-READOUT-CURVES}}

</div>

More observation keeps helping the ideal reader, with diminishing benefit, while equal weighting eventually gives too much influence to a state that has moved.

One printed inequality deserves special care. Main Eq. 6 says that total error is at least $2D(T+\tau)$. SI Eq. S83 uses a lower bound with readout term $2D\tau/\sqrt\alpha$. But the paper's other derived results imply

$$
2DJ\ge\tau^{-2}
\quad\Longrightarrow\quad
J\ge\frac1{2D\tau^2}
\quad\Longrightarrow\quad
\sqrt{\frac{2D}{J}}\le2D\tau.
$$

<!-- vale ai-tells.FormalTransitions = NO -->
Thus the ideal asymptotic readout term is at most $2D\tau$, with equality when the information diffusion inequality is saturated. Substituting an upper bound for this term cannot establish the printed universal lower bound on total error. Within the local Gaussian model, the defensible statement is
<!-- vale ai-tells.FormalTransitions = YES -->

$$
V_{\mathrm{total}}(T,L)
\ge2DT+\sqrt{2D/J},
$$

with equality approached as $L\to\infty$ for the ideal observer. At saturation this asymptotic expression becomes $2D(T+\tau)$. For partial access the same issue occurs with the factor $1/\sqrt\alpha$. This is an apparent inconsistency between printed formulas, identified by algebra using the supplied sources. It is not a claim that the authors issued a correction.[^p1-printed]

For a concrete strict inequality case, keep $\tau=0.1\,\mathrm{s}$ and $D=0.005\,\mathrm{rad}^2/\mathrm{s}$ but set $J=40{,}000\,\mathrm{rad}^{-2}\mathrm{s}^{-1}$. Then $2DJ=400\,\mathrm{s}^{-2}$ exceeds $\tau^{-2}=100\,\mathrm{s}^{-2}$. The limiting readout variance is $0.0005\,\mathrm{rad}^2$, whereas $2D\tau=0.001\,\mathrm{rad}^2$. At $T=2\,\mathrm{s}$, the Gaussian ideal total limit is $0.0205\,\mathrm{rad}^2$, below $2D(T+\tau)=0.021\,\mathrm{rad}^2$. These values expose the algebraic problem without assuming the bound is saturated.

<!-- vale ai-tells.EmptyPadding = NO -->
<!-- vale ai-tells.ParallelStaccato = NO -->
When a continuous attractor circuit is used to accumulate an incoming signal over time, its stored value represents the integral of that signal. The short useful readout interval does not imply a short lifetime for this accumulated value. A tuned circuit can continue to represent the mean of accumulated inputs while its variance grows. A leak would instead pull its mean toward a particular value. [Diffusion limits the accuracy of the integral and the usefulness of long observation. It does not by itself introduce that restoring pull.]{.key-statement} Applying these predictions to an animal also requires checking its spike statistics, tuning, drift, access to spikes, and other sources of movement noise.[^p1-integrator]
<!-- vale ai-tells.ParallelStaccato = YES -->
<!-- vale ai-tells.EmptyPadding = YES -->

[^p1-read-setup]: Burak, Y., & Fiete, I. R. (2012). *Fundamental limits on persistent activity in networks of noisy neurons*, Supporting Text, p. 12, Eq. S57. [DOI](https://doi.org/10.1073/pnas.1117386109).

<!-- vale ai-tells.EmDashUsage = NO -->
[^p1-read-gaussian]: Burak, Y., & Fiete, I. R. (2012). *Fundamental limits on persistent activity in networks of noisy neurons*, Supporting Text, p. 13, Eqs. S58–S63 and the approximation paragraph preceding them. [DOI](https://doi.org/10.1073/pnas.1117386109).
<!-- vale ai-tells.EmDashUsage = YES -->

<!-- vale ai-tells.EmDashUsage = NO -->
[^p1-naive]: Burak, Y., & Fiete, I. R. (2012). *Fundamental limits on persistent activity in networks of noisy neurons*, Supporting Text, pp. 15–16, Eqs. S76–S81. [DOI](https://doi.org/10.1073/pnas.1117386109). The double integral calculation exposes the covariances between different times compressed in the printed derivation.
<!-- vale ai-tells.EmDashUsage = YES -->

<!-- vale ai-tells.EmDashUsage = NO -->
[^p1-ideal]: Burak, Y., & Fiete, I. R. (2012). *Fundamental limits on persistent activity in networks of noisy neurons*, Supporting Text, pp. 13–15, Eqs. S58–S75. [DOI](https://doi.org/10.1073/pnas.1117386109). The supplement identifies the solution with a reverse Kalman filter. Here the equivalent precision recursion supplies a derivation without assuming prior knowledge of that filter. The printed plus sign in S71 does not match its hyperbolic cosine solution S73. The recursion independently gives the final S75 result.
<!-- vale ai-tells.EmDashUsage = YES -->

<!-- vale ai-tells.EmDashUsage = NO -->
[^p1-time]: Burak, Y., & Fiete, I. R. (2012). *Fundamental limits on persistent activity in networks of noisy neurons*. PNAS, 109(43), 17645–17650, main Eq. 5 and Optimal Observation Time; Supporting Text, Eqs. S75 and S80–S81. [DOI](https://doi.org/10.1073/pnas.1117386109).
<!-- vale ai-tells.EmDashUsage = YES -->

[^p1-partial]: Burak, Y., & Fiete, I. R. (2012). *Fundamental limits on persistent activity in networks of noisy neurons*, Supporting Text, p. 16, Incomplete readout, Eq. S82 and Fig. S2. [DOI](https://doi.org/10.1073/pnas.1117386109). The random thinning derivation states when the fraction of spikes equals the fraction of information.

<!-- vale ai-tells.EmDashUsage = NO -->
[^p1-two-times]: Burak, Y., & Fiete, I. R. (2012). *Fundamental limits on persistent activity in networks of noisy neurons*, Supporting Text, pp. 17–18, Eqs. S84–S92. [DOI](https://doi.org/10.1073/pnas.1117386109). The linear matrix here follows directly from S84. Its rate decay block is negative, as required by that differential equation, despite the positive sign printed in the corresponding block of S85.
<!-- vale ai-tells.EmDashUsage = YES -->

<!-- vale ai-tells.EmDashUsage = NO -->
[^p1-gaussian]: Burak, Y., & Fiete, I. R. (2012). *Fundamental limits on persistent activity in networks of noisy neurons*, Supporting Text, p. 19, White Gaussian noise, Eqs. S93–S95; main pp. 3–4. [DOI](https://doi.org/10.1073/pnas.1117386109). Constant noise strength $q$ and its likelihood are retained explicitly in the guide's reconstruction.
<!-- vale ai-tells.EmDashUsage = YES -->

<!-- vale ai-tells.EmDashUsage = NO -->
[^p1-fig3]: Burak, Y., & Fiete, I. R. (2012). *Fundamental limits on persistent activity in networks of noisy neurons*. PNAS, 109(43), 17645–17650, Fig. 3, p. 4; Supporting Text, Fig. S2, p. 16. [DOI](https://doi.org/10.1073/pnas.1117386109). The caption's readout equation numbers are stale relative to the supplied supplement. The corresponding results are S75 and S79–S81.
<!-- vale ai-tells.EmDashUsage = YES -->

<!-- vale ai-tells.EmDashUsage = NO -->
[^p1-printed]: Burak, Y., & Fiete, I. R. (2012). *Fundamental limits on persistent activity in networks of noisy neurons*. PNAS, 109(43), 17645–17650, main Eqs. 4–6; Supporting Text, Eqs. S75 and S83. [DOI](https://doi.org/10.1073/pnas.1117386109). The inequality direction is checked algebraically here, without assuming an author correction or changing the supplied source.
<!-- vale ai-tells.EmDashUsage = YES -->

<!-- vale ai-tells.EmDashUsage = NO -->
[^p1-integrator]: Burak, Y., & Fiete, I. R. (2012). *Fundamental limits on persistent activity in networks of noisy neurons*. PNAS, 109(43), 17645–17650, Discussion, p. 5; Supporting Text, Integration time constant, p. 17. [DOI](https://doi.org/10.1073/pnas.1117386109).
<!-- vale ai-tells.EmDashUsage = YES -->

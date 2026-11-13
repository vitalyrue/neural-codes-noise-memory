# Spike information limits memory stability {#ch:MEMORY-INFORMATION}

A neuron that receives spikes from a memory circuit can use them to estimate the value stored by that circuit. [Collecting more spikes helps distinguish nearby activity patterns, but during collection the pattern itself keeps moving.]{.key-statement} The same variability that limits readout also perturbs the recurrent network. Burak and Fiete connect these two effects by deriving a lower bound on memory diffusion from the information in the spikes.[^p1-info-main]

The useful quantity is how clearly a short spike sample distinguishes nearby memory values. Comparing that quantity with the random motion already derived gives a minimum rate of memory spreading. This is a limit for a particular network, so using it to compare different networks also requires keeping track of what changes and what stays fixed. More information can permit better stability without ensuring that a particular circuit achieves it.

We retain the memory coordinate $\theta$, initial value $\Theta$, firing rate $\bar r_i(\theta)$, synaptic time constant $\tau$, and diffusion convention $\operatorname{Var}(\Delta\theta)=2D\Delta t$. The [network projection](ch-memory-dynamics.html#sec-memory-linearization) determines which activity changes remain as changes in the stored value.

## Rate slopes and spike variability determine local information {#sec:MEMORY-FI}

**Neural mechanism.** Suppose two nearby memory values produce almost identical rates. A short spike sample cannot reliably tell them apart. If a small change in memory instead produces a large rate change relative to spike variability, that sample is more useful. We need a quantity that measures this local distinction.

In a short interval $h$, let $n_i$ be neuron $i$'s count. Treat the memory state as locally constant and use the conditionally independent Poisson approximation from the neural model. The calculation below uses positive rates.

**Mathematical derivation.** [A [**likelihood**]{.definition-term custom-style="Definition Term"} is the probability of observed data as a function of a proposed parameter value.]{.definition-explanation} For the neural model,

$$
p(\mathbf n\mid\theta)=\prod_i
\frac{[\bar r_i(\theta)h]^{n_i}e^{-\bar r_i(\theta)h}}{n_i!}.
$$

Taking the logarithm turns the product into a sum. With $r_i'=d\bar r_i/d\theta$,

$$
\ell(\theta)=\log p(\mathbf n\mid\theta)
=\sum_i\{n_i\log[\bar r_i(\theta)h]-\bar r_i(\theta)h-\log(n_i!)\},
$$

$$
S(\theta)=\frac{d\ell}{d\theta}
=\sum_i\frac{r_i'}{\bar r_i}(n_i-\bar r_i h).
$$

[The [**score**]{.definition-term custom-style="Definition Term"} $S$ measures how the log likelihood changes when the proposed memory value changes.]{.definition-explanation} Its mean is zero because $E[n_i]=\bar r_i h$. Its mean square is

$$
E[S^2]
=\sum_i\frac{(r_i')^2}{\bar r_i^2}\operatorname{Var}(n_i)
=h\sum_i\frac{(r_i')^2}{\bar r_i}.
$$

The cross terms vanish by conditional independence, and Poisson variance supplies $\operatorname{Var}(n_i)=\bar r_i h$. [[**Fisher information**]{.definition-term custom-style="Definition Term"} is this expected squared score. The paper divides it by observation duration and calls the result the [**internal Fisher information rate**]{.definition-term custom-style="Definition Term"}:]{.definition-explanation}

$$
\boxed{J(\theta)=\sum_i\frac{(r_i')^2}{\bar r_i}.}
$$

[To understand why inverse information is an error scale, let $\hat\theta(\mathbf n)$ be an estimator whose mean equals $\theta$ locally. Such an estimator is [**unbiased**]{.definition-term custom-style="Definition Term"}.]{.definition-explanation} Differentiate $E_\theta[\hat\theta]=\theta$ with respect to $\theta$. Under the usual conditions allowing differentiation through the sum over data,

$$
1=\sum_{\mathbf n}\hat\theta(\mathbf n)\partial_\theta p(\mathbf n\mid\theta)
=E[\hat\theta S]
=E[(\hat\theta-\theta)S].
$$

The last equality uses $E[S]=0$. Cauchy Schwarz now gives

$$
1\le E[(\hat\theta-\theta)^2]E[S^2],
\qquad
\boxed{\operatorname{Var}(\hat\theta)\ge\frac{1}{Jh}.}
$$

**Interpretation.** [This is the [**Cramér Rao bound**]{.definition-term custom-style="Definition Term"}. It is a local bound for regular unbiased estimation.]{.definition-explanation} It does not guarantee that every finite spike sample admits an estimator attaining it. The paper works in a weak noise, informative sample regime where local likelihoods can be approximated as Gaussian and efficient estimation can approach the bound. [A [**prior distribution**]{.definition-term custom-style="Definition Term"} represents knowledge about likely parameter values before observing the spikes.]{.definition-explanation} A strong prior, bias, boundaries, or globally ambiguous tuning changes the estimation problem.[^p1-cr]

If the coordinate is an angle in radians, $J$ has units $\mathrm{rad}^{-2}\mathrm{s}^{-1}$. The information in a locally stationary interval of duration $h$ is $Jh$, not $J$.[^p1-fi-source] A vanishing rate requires a suitable limit and regularity of the likelihood.

Each cell contributes squared slope divided by its count variance per unit time. High rates with zero slope do not distinguish neighboring values, so they contribute no local information. A sharply changing rate can be informative even if it is smaller than another cell's peak rate. The coordinate here describes the network's present internal state. It need not be a currently visible external stimulus. Sensory Fisher information has the same Poisson formula only when the stimulus dependent tuning curves are the relevant rates.

Two positive tuning curves with the same changing part isolate the effect of extra baseline firing.

<div class="figure-scroll">

{{block:fig:MEMORY-TUNING-INFORMATION}}

</div>

The rate peak has zero local slope, so it contributes no local information at that point. Extra spikes from a constant baseline increase Poisson variability without making nearby values easier to distinguish. See [Internal Fisher information, Eq. 3, p. 2](../papers/burak-fiete-2012-persistent-activity.pdf#page=2).

## Spike information sets a lower bound on memory diffusion {#sec:MEMORY-BOUND}

**Neural mechanism.** The network has no access to its exact firing rates as noiseless numbers. Its recurrent input is built from the same random spikes that an external observer sees. The lower bound on diffusion follows directly by comparing the state sensitivity of the network with the spike information.

**Mathematical derivation.** Cauchy Schwarz bounds a dot product by the product of the two vector lengths. Here the normalization of the memory projection fixes that dot product, while the two lengths measure diffusion and information. From the [projection and diffusion calculation](ch-memory-dynamics.html#sec-memory-diffusion),

$$
2D=\sum_i v_i^2\bar r_i,
\qquad
u_i=\tau r_i',
\qquad
\sum_i v_i u_i=1.
$$

Define two vectors $a_i=v_i\sqrt{\bar r_i}$ and $b_i=r_i'/\sqrt{\bar r_i}$. Their dot product is

$$
\sum_i a_i b_i=\sum_i v_i r_i'=\frac{1}{\tau}.
$$

Their squared lengths are $\sum_i a_i^2=2D$ and $\sum_i b_i^2=J$. Cauchy Schwarz therefore gives

$$
\left(\frac1\tau\right)^2
\le\left(\sum_i a_i^2\right)\left(\sum_i b_i^2\right)=2DJ,
$$

or

$$
\boxed{D\ge\frac{1}{2\tau^2J}.}
$$

**Interpretation.** This proof uses the general left vector formula, so symmetric weights are unnecessary. It is a shorter teaching reconstruction of the scalar proof in SI Section V. Its assumptions are those used to derive $D$ and $J$; it is not a general statement about all possible noisy memory systems.[^p1-bound-source]

The units agree: $\tau^2J$ has units of time per coordinate squared, so its reciprocal has the units of diffusion. [Small internal information forces a large minimum diffusion coefficient. Large information allows small diffusion, but does not guarantee it.]{.key-statement}

**Neural mechanism.** [Reaching the bound requires the network's retained response to each cell's spike noise to match that cell's information about memory.]{.key-statement} A cell that adds retained noise without helping distinguish nearby values prevents equality.

**Mathematical derivation.** Equality requires the two vectors in the proof to be proportional:

$$
v_i=c\frac{r_i'}{\bar r_i}
\quad\text{for every contributing cell},
\qquad c=\frac{1}{\tau J}.
$$

Cells with zero tuning slope cannot contribute extra projected noise if equality is to hold. In a symmetric network, $v_i$ is proportional to $g_i'$, and $r_i'=\phi'(\bar g_i)g_i'$. At each state, the participating cells therefore need a common value of $\phi'(\bar g_i)/\phi(\bar g_i)$. A sufficient way to satisfy this at all states is to choose that ratio equal to the same constant $k$ throughout the relevant input range. Solving

$$
\frac{d}{dg}\log\phi(g)=k
$$

gives $\phi(g)=A e^{kg}$.

**Interpretation.** This exponential family attains equality for symmetric weights with Poisson noise, under the other model assumptions. It is a sufficient condition, rather than a general necessity: the common ratio may depend on the current memory state.[^p1-equality]

::: {.publisher-clarification-note .publisher-fold-always title="Check: equality can also hold with a linear transfer rule"}

The [mutual-excitation example](ch-memory-long-delays.html#sec-memory-long-time) supplies a counterexample to the unrestricted converse. Set its bias $b_0=0$ and use the linear rule $\phi(g)=g/\tau$ on positive inputs. Its fixed states are $s_1=s_2=\theta>0$, with $\mathbf u=(1,1)^T$ and $\mathbf v=(1/2,1/2)^T$. Both rates are $\theta/\tau$, and both rate derivatives are $1/\tau$. Therefore

$$
2D=\frac{\theta}{2\tau},\qquad
J=\frac{2}{\tau\theta},\qquad
2DJ=\frac{1}{\tau^2}.
$$

Equality holds throughout this family even though its transfer rule is linear. At each state both cells receive the same input, and the ratio $\phi'/\phi=1/\theta$ changes between states. A converse that forces an exponential rule needs additional restrictions linking the participating input values across cells and states. Continuous variation of the represented value alone does not supply them. This qualification concerns the source's claimed converse, while leaving the information–diffusion inequality intact.

:::

<div class="publisher-worked-calculation publisher-fold-never">

**Example: the same diffusion with a looser information bound.** In the two cell mutual inhibition model, use $b=200$ activation units and $\tau=0.1\,\mathrm{s}$. The memory coordinate is an activation difference, not an angle. At $\theta=0$ both rates are $1000\,\mathrm{s}^{-1}$ and their slopes are $\pm5\,\mathrm{s}^{-1}$ per activation unit. Thus

$$
J=\frac{25}{1000}+\frac{25}{1000}=0.05,
\qquad D=\frac{b}{2\tau}=1000.
$$

Here $J$ has units of inverse activation unit squared per second, and $D$ has activation unit squared per second. The bound is $1/(2\tau^2J)=1000$, so equality holds at this balanced state. At $\theta=100$, the rates become $1500$ and $500\,\mathrm{s}^{-1}$, while their slopes stay $\pm5$. Now

$$
J=\frac{25}{1500}+\frac{25}{500}=\frac1{15}\simeq0.06667,
\qquad \frac1{2\tau^2J}=750.
$$

The actual diffusion remains $1000$. The inequality is strict because these two unequal rates no longer align the network's projection weights with the information optimal weights. This also shows why equality at a special state does not force the transfer function to be exponential on its whole domain. A constant lower bound attained everywhere and an accidental equality at one state are different claims.



<div class="figure-scroll">

{{block:fig:MEMORY-BOUND-STRICTNESS}}

</div>

The gap at $\theta=100$ shows why a lower minimum allowed by the inequality is not a reduction in the network’s actual diffusion. See [Diffusion bound, Eq. 4, p. 3](../papers/burak-fiete-2012-persistent-activity.pdf#page=3).

</div>

**Neural mechanism.** When a circuit stores several coordinates, a spike can shift more than one of them. Comparing each coordinate separately would miss combinations of shifts. The information and diffusion must therefore describe these shared directions.

**Mathematical derivation.** For $m$ memory coordinates the information is a matrix,

$$
J_{\alpha\beta}=\sum_i
\frac{\partial_{\theta_\alpha}\bar r_i\,
\partial_{\theta_\beta}\bar r_i}{\bar r_i}.
$$

The matrix calculation assumes that every independent small coordinate change can be distinguished through a change in rates, so $J$ is invertible. The matrix bound $2D\succeq\tau^{-2}J^{-1}$ means that every linear combination of coordinate displacements obeys the corresponding variance lower bound. Here $A\succeq B$ means $\mathbf z^T(A-B)\mathbf z\ge0$ for every real vector $\mathbf z$. To derive it, form $N\times m$ matrices $U_{i\alpha}=u_i^\alpha/\sqrt{\bar r_i}$ and $V_{i\alpha}=v_i^\alpha\sqrt{\bar r_i}$. Then

$$
U^TV=I,\qquad U^TU=\tau^2J,\qquad V^TV=2D.
$$

::: {.publisher-clarification-note .publisher-fold-always title="Check: the residual matrix proves the lower bound"}

Set $Q=V-U(U^TU)^{-1}$. Expanding $Q^TQ$ and using $U^TV=I$ gives

$$
Q^TQ=V^TV-(U^TU)^{-1}
=2D-\tau^{-2}J^{-1}\succeq0.
$$

:::

**Interpretation.** The bound controls every combination of stored coordinates, including coupled directions that separate scalar bounds would miss. If $J$ is singular, this ordinary inverse formula cannot be used.[^p1-matrix]

## Improving persistence depends on what a comparison holds fixed {#sec:MEMORY-COMPARISONS}

**Neural mechanism.** [The inequality compares diffusion and information for the same network. To compare different networks, we must say what stays fixed.]{.key-statement} Otherwise an apparent benefit of a parameter change may come from changing another property at the same time. The comparisons below control how added neurons, altered firing rates, or slower synaptic decay affect the tuning curves and recurrent input.

**Mathematical derivation.** Increasing $N$ while retaining the same distribution of tuning curves and scaling weights as $1/N$ keeps individual inputs and rates fixed. The sums in the symmetric formula scale as $N$ in the numerator and $N^2$ in the denominator. Consequently $D\propto1/N$, while $J\propto N$. This is a controlled density or population replication comparison, not a promise about adding arbitrary neurons.

If all tuning rates are multiplied by a factor $a$, their slopes are also multiplied by $a$, so $J\mapsto aJ$. For equality achieving exponential networks, $D\mapsto D/a$ immediately follows. The same scaling follows from the symmetric diffusion formula when the change preserves $g_i'$ up to a common scale and preserves the tuning geometry. For a general fixed nonlinear transfer rule, multiplying rates need not preserve those quantities or even the attractor. The paper's rate comparison is made with the tuning shapes and appropriate network scaling held under control.[^p1-scaling]

Changing $\tau$ while holding the rate tuning curves and their input relation fixed gives $D\propto\tau^{-2}$ in the symmetric formula. Maintaining those curves requires retuning the network, because $\bar s=\tau\bar r$. In contrast, holding activation curves and dimensionless weights fixed in the linear two cell example makes rates scale as $1/\tau$, so $D=b/(2\tau)\propto\tau^{-1}$.

**Interpretation.** These two statements concern different controlled comparisons. A larger cellular time constant can improve memory stability while the exponent of its effect depends on what the experiment keeps fixed.

**Neural mechanism.** The paper also links tuning width to memory persistence. The reason for its opposite predictions in one and three dimensions can be derived from the number of active cells and their slopes. This derivation is a teaching reconstruction of the tuning width argument cited in the main text, rather than a proof that every tuning family follows one power law.[^p1-width]

Assume preferred positions $\mathbf c$ have uniform density $\rho$ in a $d$ dimensional stimulus or memory space. Away from boundaries, let identical tuning curves have fixed peak rate $a$ and a common shape $f$:

$$
\bar r_{\mathbf c}(\boldsymbol\theta)
=a f[(\boldsymbol\theta-\mathbf c)/w].
$$

The width $w$ is varied while $a$, $\rho$, and the shape $f$ are fixed.

**Mathematical derivation.** For one coordinate direction $\alpha$, replace the population sum by an integral and substitute $\mathbf z=(\boldsymbol\theta-\mathbf c)/w$:

$$
J_{\alpha\alpha}
\simeq\rho\int d^d c\,
\frac{a^2w^{-2}(\partial_\alpha f)^2}{af}
=\rho a w^{d-2}
\int d^d z\,\frac{(\partial_\alpha f)^2}{f}.
$$

Two factors determine how information changes with tuning width:

- The volume element contributes $w^d$ because broader fields recruit more neurons.
- The squared slope contributes $w^{-2}$ because broader curves change more slowly.

Each diagonal entry therefore scales as $J_{\alpha\alpha}\propto w^{d-2}$. Now restrict the tuning shape $f$ to depend only on distance from its center. Uniformly distributing those centers makes every coordinate direction equivalent: off-diagonal information terms vanish, and all diagonal entries are equal. For an exponential network that attains the matrix bound, $D_{\alpha\alpha}=1/(2\tau^2J_{\alpha\alpha})\propto w^{2-d}$.

**Interpretation.** The resulting comparisons are:

- Narrower curves help in $d=1$.
- Width has no leading effect in $d=2$.
- Broader curves help in $d=3$.

[These conclusions change under another resource constraint. Fixing the total population spike rate instead of peak rate makes $a\propto w^{-d}$, giving $J\propto w^{-2}$ in every dimension.]{.key-statement} Sparse coverage, a large baseline rate, finite boundaries, correlated noise, or a width too small for the population integral can also change the comparison. Attaining equality means the network reaches the diffusion lower bound for its information rate and synaptic time constant. Minimizing diffusion still requires deciding how much information the allowed architecture and firing budget can supply.

If an external stimulus produces the same tuning curves as the network's input free memory states, the sensory and internal Fisher information are equal. In a symmetric exponential network, maximizing this information then improves sensory estimation and minimizes memory diffusion together. This is why the paper suggests that one circuit could support both sensory estimation and memory storage. The mathematical compatibility does not establish where a particular animal stores a memory, and the equality of tuning curves must be checked rather than inferred from the shared formula.[^p1-colocation]

[^p1-info-main]: Burak, Y., & Fiete, I. R. (2012). *Fundamental limits on persistent activity in networks of noisy neurons*. Proceedings of the National Academy of Sciences, 109(43), 17645–17650, main pp. 2–4, Eqs. 3–5. [DOI](https://doi.org/10.1073/pnas.1117386109).

[^p1-fi-source]: Burak, Y., & Fiete, I. R. (2012). *Fundamental limits on persistent activity in networks of noisy neurons*, Supporting Text, pp. 9–10, Section IV, Eqs. S42–S44; main Eq. 3. [DOI](https://doi.org/10.1073/pnas.1117386109). The score variance calculation is expanded for teaching.

[^p1-cr]: Burak, Y., & Fiete, I. R. (2012). *Fundamental limits on persistent activity in networks of noisy neurons*. PNAS, 109(43), 17645–17650, p. 3, Information-Diffusion Inequality and Saturation. [DOI](https://doi.org/10.1073/pnas.1117386109). The scalar Cramér Rao proof is a teaching reconstruction of the bound invoked there.

[^p1-bound-source]: Burak, Y., & Fiete, I. R. (2012). *Fundamental limits on persistent activity in networks of noisy neurons*, Supporting Text, pp. 10–11, Eqs. S45–S49; main Eq. 4. [DOI](https://doi.org/10.1073/pnas.1117386109).

[^p1-equality]: Burak, Y., & Fiete, I. R. (2012). *Fundamental limits on persistent activity in networks of noisy neurons*, Supporting Text, p. 11, Eqs. S47–S51. [DOI](https://doi.org/10.1073/pnas.1117386109). The linear-family counterexample is a guide calculation qualifying the source's converse.

[^p1-matrix]: Burak, Y., & Fiete, I. R. (2012). *Fundamental limits on persistent activity in networks of noisy neurons*, Supporting Text, pp. 10–12, Eqs. S44 and S52–S56. [DOI](https://doi.org/10.1073/pnas.1117386109). The residual matrix proof here is an equivalent teaching reconstruction.

[^p1-scaling]: Burak, Y., & Fiete, I. R. (2012). *Fundamental limits on persistent activity in networks of noisy neurons*. PNAS, 109(43), 17645–17650, p. 2, discussion after Eq. 2; pp. 5–6, Weak Fluctuations. [DOI](https://doi.org/10.1073/pnas.1117386109). Comparisons with different held quantities are made explicit here.

[^p1-width]: Burak, Y., & Fiete, I. R. (2012). *Fundamental limits on persistent activity in networks of noisy neurons*. PNAS, 109(43), 17645–17650, p. 4, tuning width discussion. [DOI](https://doi.org/10.1073/pnas.1117386109). The paper cites Zhang and Sejnowski's tuning work. The integral scaling and alternative firing budget here are teaching derivations, not a separate verification of that cited paper.

[^p1-colocation]: Burak, Y., & Fiete, I. R. (2012). *Fundamental limits on persistent activity in networks of noisy neurons*. PNAS, 109(43), 17645–17650, pp. 4–5, sensory representation comparison and footnote concerning similarity of sensory and persistent tuning. [DOI](https://doi.org/10.1073/pnas.1117386109).

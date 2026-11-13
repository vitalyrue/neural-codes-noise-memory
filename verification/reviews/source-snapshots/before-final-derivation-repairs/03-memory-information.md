# Information, memory loss, and the time needed for recall {#ch:MEMORY-INFORMATION}

A downstream neuron reads a memory through spikes. Collecting more spikes helps distinguish nearby activity patterns, but during collection the pattern itself keeps moving. The same variability that limits readout also perturbs the recurrent network. Burak and Fiete connect these two effects by deriving a lower bound on memory diffusion from the information in the spikes.[^p1-info-main]

We retain the memory coordinate $\theta$, initial value $\Theta$, firing rate $\bar r_i(\theta)$, synaptic time constant $\tau$, and diffusion convention $\operatorname{Var}(\Delta\theta)=2D\Delta t$. Here $T$ is the delay before a recall cue and $L$ is the observation interval after that cue. They answer different questions: $T$ determines how much memory has already been lost; $L$ determines how well the surviving state can be read.

## Deriving information from the spike count likelihood {#sec:MEMORY-FI}

Suppose two nearby memory values produce almost identical rates. A short spike sample cannot reliably tell them apart. If a small change in memory instead produces a large rate change relative to spike variability, that sample is more useful. We need a quantity that measures this local distinction.

A [**likelihood**]{.definition-term custom-style="Definition Term"} is the probability of observed data as a function of a proposed parameter value. In a short interval $h$, let $n_i$ be neuron $i$'s count. Treat the state as locally constant and use the conditional independent Poisson approximation. Then

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

The [**score**]{.definition-term custom-style="Definition Term"} $S$ measures how the log likelihood changes when the proposed memory value changes. Its mean is zero because $E[n_i]=\bar r_i h$. Its mean square is

$$
E[S^2]
=\sum_i\frac{(r_i')^2}{\bar r_i^2}\operatorname{Var}(n_i)
=h\sum_i\frac{(r_i')^2}{\bar r_i}.
$$

The cross terms vanish by conditional independence, and Poisson variance supplies $\operatorname{Var}(n_i)=\bar r_i h$. [**Fisher information**]{.definition-term custom-style="Definition Term"} is this expected squared score. The paper divides it by observation duration and calls the result the [**internal Fisher information rate**]{.definition-term custom-style="Definition Term"}:

$$
\boxed{J(\theta)=\sum_i\frac{(r_i')^2}{\bar r_i}.}
$$

If the coordinate is an angle in radians, $J$ has units $\mathrm{rad}^{-2}\mathrm{s}^{-1}$. The information in a locally stationary interval of duration $h$ is $Jh$, not $J$. We write formulas for positive rates; a vanishing rate requires a suitable limit and regularity of the likelihood.[^p1-fi-source]

Each cell contributes squared slope divided by its count variance per unit time. High rates with zero slope do not distinguish neighboring values, so they contribute no local information. A sharply changing rate can be informative even if it is smaller than another cell's peak rate. The coordinate here describes the network's present internal state. It need not be a currently visible external stimulus. Sensory Fisher information has the same Poisson formula only when the stimulus dependent tuning curves are the relevant rates.

To understand why inverse information is an error scale, let $\hat\theta(\mathbf n)$ be an estimator whose mean equals $\theta$ locally. Such an estimator is [**unbiased**]{.definition-term custom-style="Definition Term"}. Differentiate $E_\theta[\hat\theta]=\theta$ with respect to $\theta$. Under the usual conditions allowing differentiation through the sum over data,

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

This is the [**Cramér Rao bound**]{.definition-term custom-style="Definition Term"}. It is a local bound for regular unbiased estimation. It does not guarantee that every finite spike sample admits an estimator attaining it. The paper works in a weak noise, informative sample regime where local likelihoods can be approximated as Gaussian and efficient estimation can approach the bound. A [**prior distribution**]{.definition-term custom-style="Definition Term"} represents knowledge about likely parameter values before observing the spikes. A strong prior, bias, boundaries, or globally ambiguous tuning changes the estimation problem.[^p1-cr]

## The information diffusion inequality, step by step {#sec:MEMORY-BOUND}

The network has no access to its exact firing rates as noiseless numbers. Its recurrent input is built from the same random spikes that an external observer sees. The lower bound on diffusion follows directly by comparing the state sensitivity of the network with the spike information.

From the preceding chapter,

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

This proof uses the general left vector formula, so symmetric weights are unnecessary. It is a shorter teaching reconstruction of the scalar proof in SI Section V. Its assumptions are those used to derive $D$ and $J$; it is not a general statement about all possible noisy memory systems.[^p1-bound-source]

The units agree: $\tau^2J$ has units of time per coordinate squared, so its reciprocal has the units of diffusion. Small internal information forces a large minimum diffusion coefficient. Large information allows small diffusion, but does not guarantee it.

Equality requires the two vectors in the proof to be proportional:

$$
v_i=c\frac{r_i'}{\bar r_i}
\quad\text{for every contributing cell},
\qquad c=\frac{1}{\tau J}.
$$

Cells with zero tuning slope cannot contribute extra projected noise if equality is to hold. In a symmetric network, $v_i$ is proportional to $g_i'$, and $r_i'=\phi'(\bar g_i)g_i'$. At each state, the participating cells therefore need a common value of $\phi'(\bar g_i)/\phi(\bar g_i)$. A sufficient way to satisfy this at all states is to choose that ratio equal to the same constant $k$ throughout the relevant input range. Solving

$$
\frac{d}{dg}\log\phi(g)=k
$$

gives $\phi(g)=A e^{kg}$. This exponential family attains equality for symmetric weights with Poisson noise, under the other model assumptions. It is a sufficient condition, rather than a general necessity: the common ratio may depend on the current memory state.[^p1-equality]

The mutual-excitation example in Chapter 2 supplies a counterexample to the unrestricted converse. Set its bias $b_0=0$ and use the linear rule $\phi(g)=g/\tau$ on positive inputs. Its fixed states are $s_1=s_2=\theta>0$, with $\mathbf u=(1,1)^T$ and $\mathbf v=(1/2,1/2)^T$. Both rates are $\theta/\tau$, and both rate derivatives are $1/\tau$. Therefore

$$
2D=\frac{\theta}{2\tau},\qquad
J=\frac{2}{\tau\theta},\qquad
2DJ=\frac{1}{\tau^2}.
$$

Equality holds throughout this family even though its transfer rule is linear. At each state both cells receive the same input, and the ratio $\phi'/\phi=1/\theta$ changes between states. A converse that forces an exponential rule needs additional restrictions linking the participating input values across cells and states. Continuous variation of the represented value alone does not supply them. This qualification concerns the source's claimed converse, while leaving the information–diffusion inequality intact.

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

For $m$ memory coordinates the information is a matrix,

$$
J_{\alpha\beta}=\sum_i
\frac{\partial_{\theta_\alpha}\bar r_i\,
\partial_{\theta_\beta}\bar r_i}{\bar r_i}.
$$

The matrix statement $2D\succeq\tau^{-2}J^{-1}$ means that every linear combination of coordinate displacements obeys the corresponding variance lower bound. Here $A\succeq B$ means $\mathbf z^T(A-B)\mathbf z\ge0$ for every real vector $\mathbf z$. To derive it, form $N\times m$ matrices $U_{i\alpha}=u_i^\alpha/\sqrt{\bar r_i}$ and $V_{i\alpha}=v_i^\alpha\sqrt{\bar r_i}$. Then

$$
U^TV=I,\qquad U^TU=\tau^2J,\qquad V^TV=2D.
$$

Set $Q=V-U(U^TU)^{-1}$. Expanding $Q^TQ$ and using $U^TV=I$ gives

$$
Q^TQ=V^TV-(U^TU)^{-1}
=2D-\tau^{-2}J^{-1}\succeq0.
$$

This proves the matrix inequality when every independent small coordinate change can be distinguished through a change in rates, so $J$ is invertible. It also explains why a scalar bound in each coordinate separately would miss coupled directions.[^p1-matrix]

## What changes actually improve persistence? {#sec:MEMORY-COMPARISONS}

The inequality compares diffusion and information for the same network. To compare different networks, we must say what stays fixed. Otherwise an apparent benefit of a parameter change may come from changing another property at the same time.

Increasing $N$ while retaining the same distribution of tuning curves and scaling weights as $1/N$ keeps individual inputs and rates fixed. The sums in the symmetric formula scale as $N$ in the numerator and $N^2$ in the denominator. Consequently $D\propto1/N$, while $J\propto N$. This is a controlled density or population replication comparison, not a promise about adding arbitrary neurons.

If all tuning rates are multiplied by a factor $a$, their slopes are also multiplied by $a$, so $J\mapsto aJ$. For equality achieving exponential networks, $D\mapsto D/a$ immediately follows. The same scaling follows from the symmetric diffusion formula when the change preserves $g_i'$ up to a common scale and preserves the tuning geometry. For a general fixed nonlinear transfer rule, multiplying rates need not preserve those quantities or even the attractor. The paper's rate comparison is made with the tuning shapes and appropriate network scaling held under control.[^p1-scaling]

Changing $\tau$ while holding the rate tuning curves and their input relation fixed gives $D\propto\tau^{-2}$ in the symmetric formula. Maintaining those curves requires retuning the network, because $\bar s=\tau\bar r$. In contrast, holding activation curves and dimensionless weights fixed in the linear two cell example makes rates scale as $1/\tau$, so $D=b/(2\tau)\propto\tau^{-1}$. These two statements concern different controlled comparisons. A larger cellular time constant can improve memory stability while the exponent of its effect depends on what the experiment keeps fixed.

The paper also links tuning width to memory persistence. The reason for its opposite predictions in one and three dimensions can be derived from the number of active cells and their slopes. This derivation is a teaching reconstruction of the tuning width argument cited in the main text, rather than a proof that every tuning family follows one power law.[^p1-width]

Assume preferred positions $\mathbf c$ have uniform density $\rho$ in a $d$ dimensional stimulus or memory space. Away from boundaries, let identical tuning curves have fixed peak rate $a$ and a common shape $f$:

$$
\bar r_{\mathbf c}(\boldsymbol\theta)
=a f[(\boldsymbol\theta-\mathbf c)/w].
$$

The width $w$ is varied while $a$, $\rho$, and the shape $f$ are fixed. For one coordinate direction $\alpha$, replace the population sum by an integral and substitute $\mathbf z=(\boldsymbol\theta-\mathbf c)/w$:

$$
J_{\alpha\alpha}
\simeq\rho\int d^d c\,
\frac{a^2w^{-2}(\partial_\alpha f)^2}{af}
=\rho a w^{d-2}
\int d^d z\,\frac{(\partial_\alpha f)^2}{f}.
$$

The volume element contributes $w^d$ because broader fields recruit more neurons. The squared slope contributes $w^{-2}$ because broader curves change more slowly. Under these assumptions $J\propto w^{d-2}$. In an equality achieving isotropic exponential network, diffusion in each coordinate consequently scales as $D\propto w^{2-d}$. Narrower curves help in $d=1$, width has no leading effect in $d=2$, and broader curves help in $d=3$.

These conclusions change under another resource constraint. Fixing the total population spike rate instead of peak rate makes $a\propto w^{-d}$, giving $J\propto w^{-2}$ in every dimension. Sparse coverage, a large baseline rate, finite boundaries, correlated noise, or a width too small for the population integral can also change the comparison. Saturating the inequality identifies efficient self tracking for a given information rate; minimizing diffusion still requires deciding how much information the allowed architecture and firing budget can supply.

If an external stimulus produces the same tuning curves as the network's input free memory states, the sensory and internal Fisher information are equal. In a symmetric exponential network, maximizing this information then improves sensory estimation and minimizes memory diffusion together. This is the paper's reason for suggesting that one circuit could serve both functions. The mathematical compatibility does not establish where a particular animal stores a memory, and the equality of tuning curves must be checked rather than inferred from the shared formula.[^p1-colocation]

## Readout trades count noise against motion during observation {#sec:MEMORY-READOUT-SETUP}

At time $T$, a recall cue arrives. The observer now wants the original value $\Theta$, but only has access to future spikes. The network has already diffused during storage. Even perfect knowledge of the state $\theta(T)$ cannot recover its particular earlier random displacements.

For an unbounded coordinate with constant $D$ and no drift, write the total recall error variance as

$$
V_{\mathrm{total}}(T,L)=2DT+V_{\mathrm{read}}(L).
$$

The first term comes from storage. The second concerns estimation of $\theta(T)$ from spikes after $T$. The supplement derives this decomposition for a locally translation invariant diffusion and readout model; state dependence, boundaries, informative priors, or uncertain initial encoding require corresponding changes.[^p1-read-setup]

To solve the readout problem, the supplement approximates the likelihood from each short bin as Gaussian. Let $x=\theta(T)$ and index subsequent bins by $k$. The equivalent observation model is

$$
\theta_{k+1}=\theta_k+\eta_k,
\qquad y_k=\theta_k+\epsilon_k,
$$

$$
\operatorname{Var}(\eta_k)=2Dh,
\qquad \operatorname{Var}(\epsilon_k)=\frac1{Jh}.
$$

The Gaussian increments and observation errors are independent in this approximation. The value $y_k$ summarizes information about the state from that bin's population spikes; it is not an additional directly measured physical coordinate. The continuous limit is a convenient mathematical description of the many spike, weak fluctuation regime. It does not assert that an arbitrarily short physical bin already contains enough spikes for a Gaussian fit. The derivations below are exact within this local Gaussian readout model.[^p1-read-gaussian]

## Why averaging for too long becomes harmful {#sec:MEMORY-NAIVE}

A decoder designed for a stationary state averages its observations with equal weight. That reduces independent observation noise, but late observations reflect a state that has moved further from $x$.

Write $\theta(T+t)=x+B_D(t)$, where $B_D$ has Brownian covariance

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

Split the square into its two equal triangles. On the triangle $0\le s\le t\le L$, the minimum is $s$. Therefore

$$
\int_0^L\int_0^L\min(t,s)\,dt\,ds
=2\int_0^L\!dt\int_0^t\!s\,ds
=\int_0^L t^2dt=\frac{L^3}{3}.
$$

Combining the terms gives

$$
\boxed{V_{\mathrm{naive}}(L)=\frac{2DL}{3}+\frac1{JL}.}
$$

The two contributions have opposite dependence on $L$. Differentiating,

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

Waiting longer eventually increases error, even with more spikes available. The problem is their equal weighting for a moving state.[^p1-naive]

## Deriving the ideal observer's readout curve {#sec:MEMORY-IDEAL}

An observer that accounts for diffusion can use later observations without confusing them with direct measurements of $x$. Their value is limited by the motion separating them from $x$. We can derive its error by combining information backward from the end of the observation interval.

The [**precision**]{.definition-term custom-style="Definition Term"} of a scalar Gaussian estimate is the reciprocal of its variance. Independent Gaussian measurements of one value add precisions. To verify this, multiply likelihoods proportional to $\exp[-(x-a)^2/(2V_a)]$ and $\exp[-(x-b)^2/(2V_b)]$: the coefficient of $x^2/2$ becomes $1/V_a+1/V_b$.

Let $P(L)$ be the precision about the state at the beginning of an interval of length $L$, using all observations in that interval and no informative prior. Suppose we have already compressed the later part into a likelihood about the next bin's state with variance $1/P$. Bringing that likelihood one step backward adds transition variance $q=2Dh$, since the next state equals the earlier state plus an independent Gaussian increment. Its precision about the earlier state is therefore

$$
\frac{1}{1/P+q}=\frac{P}{1+2DhP}.
$$

The new earliest observation adds precision $Jh$. Thus, up to bin endpoint conventions that disappear as $h\to0$,

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

The hyperbolic tangent is $\tanh z=(e^z-e^{-z})/(e^z+e^{-z})$. Its inverse on $(-1,1)$ is $\operatorname{artanh}z=\tfrac12\log[(1+z)/(1-z)]$, whose derivative is $1/(1-z^2)$. Initially no observation means zero precision. The term $J$ adds new information; the term $2DP^2$ accounts for uncertainty when carrying that information backward through diffusion. Set $a=\sqrt{J/(2D)}$ and $k=\sqrt{2DJ}$. Separating variables gives

$$
\int_0^{P/a}\frac{dz}{1-z^2}=kL,
\qquad
\operatorname{artanh}(P/a)=kL.
$$

Taking the inverse function and then the reciprocal yields

$$
P(L)=\sqrt{\frac{J}{2D}}\tanh(\sqrt{2DJ}\,L),
$$

$$
\boxed{V_{\mathrm{ideal}}(L)
=\sqrt{\frac{2D}{J}}\coth(\sqrt{2DJ}\,L).}
$$

Here $\coth z=1/\tanh z$. This backward precision derivation is a teaching reconstruction equivalent to the Gaussian covariance calculation in SI Eqs. S58–S75. It makes explicit how diffusion limits the value of later observations.[^p1-ideal]

For short intervals, $\coth z=1/z+z/3+O(z^3)$, so

$$
V_{\mathrm{ideal}}(L)=\frac1{JL}+\frac{2DL}{3}+O(L^3).
$$

The naive and ideal estimators therefore agree through the displayed terms. For long intervals,

$$
V_{\mathrm{ideal}}(L)\longrightarrow\sqrt{2D/J},
\qquad L^*=\frac1{\sqrt{2DJ}}.
$$

The ideal observer keeps improving, but the improvement becomes small. At $L=L^*$ its variance is $1.313$ times the limit; at $2L^*$ it is $1.037$ times the limit; at $3L^*$ it is $1.005$ times the limit. These are variances, so their ratios are not ratios of standard deviations.

Using $2DJ\ge\tau^{-2}$ gives

$$
L^*\le\tau,
\qquad L_{\mathrm{naive}}^*=\sqrt3L^*\le\sqrt3\tau.
$$

Thus the paper's statement about readout within a cellular time constant concerns a characteristic saturation time under full spike access. It does not mean all benefit ends abruptly at $\tau$. The naive observer's best variance is only $2/\sqrt3\simeq1.155$ times the ideal observer's asymptotic variance. Its best standard deviation is about $1.075$ times as large.[^p1-time]

## Limited access can make observation slower {#sec:MEMORY-PARTIAL}

A downstream area may receive only some of the memory network's spikes. That reduces its information without reducing the fluctuations that already move the full memory network.

If every spike is independently retained with probability $\alpha$, the observed rates and their slopes both scale by $\alpha$. Substitution in the Poisson information formula gives

$$
J_{\mathrm{obs}}=\sum_i\frac{(\alpha r_i')^2}{\alpha\bar r_i}=\alpha J.
$$

The network diffusion coefficient stays $D$. Hence

$$
L_{\mathrm{obs}}^*=\frac1{\sqrt{2D\alpha J}}
=\frac{L^*}{\sqrt\alpha},
\qquad
V_{\mathrm{ideal,obs}}(\infty)=\sqrt{\frac{2D}{\alpha J}}.
$$

The same factor $1/\sqrt\alpha$ multiplies the naive optimal interval and its minimum variance. The information bound implies $L_{\mathrm{obs}}^*\le\tau/\sqrt\alpha$, which can exceed $\tau$. A selected subset of neurons has exactly $\alpha J$ only when it carries that fraction of the information; a fraction of neurons or spikes chosen by a biased rule need not do so.[^p1-partial]

**Example: limited spike access changes the useful interval.** Take $\tau=0.1\,\mathrm{s}$, $J=10{,}000\,\mathrm{rad}^{-2}\mathrm{s}^{-1}$, and $D=0.005\,\mathrm{rad}^2/\mathrm{s}$. These values attain the information bound. Full access gives $L^*=0.1\,\mathrm{s}$ and limiting readout variance $0.001\,\mathrm{rad}^2$. The naive optimum is $0.1732\,\mathrm{s}$ with variance $0.001155\,\mathrm{rad}^2$.

If $\alpha=0.1$, then $J_{\mathrm{obs}}=1000\,\mathrm{rad}^{-2}\mathrm{s}^{-1}$. The ideal characteristic interval becomes $0.3162\,\mathrm{s}$ and its limiting variance becomes $0.003162\,\mathrm{rad}^2$. The naive optimum becomes $0.5477\,\mathrm{s}$. A two second storage delay contributes $2DT=0.020\,\mathrm{rad}^2$ in both cases, giving total ideal asymptotic variances $0.021$ and $0.023162\,\mathrm{rad}^2$. Longer observation can reduce the readout cost; it cannot undo the random displacement during the delay.

## Two cellular time scales and a different noise law {#sec:MEMORY-EXTENSIONS}

The time constant in the inequality comes from the dynamics that carry an activation fluctuation into a lasting memory change. If those dynamics contain both synaptic and rate relaxation, which time constant matters?

The supplement adds rate relaxation with time constant $\tau_m$:

$$
\dot s_i=-s_i/\tau+r_i+\xi_i,
\qquad
\tau_m\dot r_i=-r_i+\phi(g_i).
$$

The activation noise retains its Poisson strength. In this symmetric weight extension, the linear state is $(\delta\mathbf s,\delta\mathbf r)$ and its deterministic matrix is

$$
A=\begin{pmatrix}
-I/\tau&I\\
\operatorname{diag}(\phi')W/\tau_m&-I/\tau_m
\end{pmatrix}.
$$

The right tangent is $(\tau\mathbf r',\mathbf r')$. Write the left zero vector as $(\mathbf a,\mathbf b)$. The second block of $(\mathbf a^T,\mathbf b^T)A=0$ gives $\mathbf b=\tau_m\mathbf a$. The first then gives $W^T\operatorname{diag}(\phi')\mathbf a=\mathbf a/\tau$, so symmetry again permits $\mathbf a\propto\mathbf g'$. Normalizing its dot product with the right tangent yields

$$
a_i=\frac{g_i'}{(\tau+\tau_m)\sum_jg_j'r_j'}.
$$

Only the $s$ block receives the modeled spike noise, so $2D=\sum_i a_i^2\bar r_i$. The symmetric formula consequently becomes

$$
2D=\frac{\sum_i\bar r_i(g_i')^2}
{(\tau+\tau_m)^2[\sum_i g_i'r_i']^2},
\qquad
2D\ge\frac{J^{-1}}{(\tau+\tau_m)^2}.
$$

The sum of the two time constants replaces $\tau$. The larger one dominates when they are very different. This result belongs to the two stage model and noise placement just described; the paper does not prove that arbitrary collections of biological time constants can always be added.[^p1-two-times]

The equality condition also depends on the noise law. To see why, replace Poisson spike-count fluctuations with independent additive Gaussian noise of constant strength $q>0$:

$$
ds_i=F_i(\mathbf s)dt+\sqrt q\,dB_i.
$$

The short interval observation of the mean rate is now Gaussian with variance $q/h$. Repeating the score calculation gives $J=\sum_i(r_i')^2/q$, while projection gives $2D=q\sum_i v_i^2$. The same Cauchy Schwarz proof yields $2DJ\ge\tau^{-2}$. Equality requires $v_i\propto r_i'$ because all cells have the same noise strength. In a symmetric network $v_i\propto g_i'$, so a linear transfer rule supplies the condition by keeping $\phi'(g)$ constant across participating inputs. In the Poisson case, variance grows with rate and an exponential rule is a sufficient way to attain equality. The pointwise projection condition remains the general criterion, including the linear-family counterexample already derived. The difference between these sufficient classes follows from the noise weighting, not from linearity being universally preferable.[^p1-gaussian]

This explicit $q$ formulation is a teaching reconstruction that keeps dimensions and the noise normalization visible. The supplement's Gaussian subsection establishes the change in equality condition. Here the matched noise and likelihood derivation supplies all factors of $q$ and $\tau$ without requiring the reader to infer a normalization from SI Eqs. S94–S95.

## Reading the readout curves and the printed error bound {#sec:MEMORY-FIG3-AND-CAUTION}

Figure 3 isolates readout uncertainty, rescaling variance by $\sqrt{2D/J}$ and duration by $L^*$. In these axes the ideal curve is $\coth z$ and the naive curve is $z/3+1/z$. Both diverge like $1/z$ at short durations because too few spikes are available. The ideal solid curve approaches one. The naive dashed curve reaches $2/\sqrt3$ at $z=\sqrt3$, then rises because its equal weighting gives increasing importance to displaced states. The dotted vertical line marks that naive optimum. The storage delay contribution $2DT$ is not part of these rescaled curves. Figure S2 repeats the comparison for partial access, showing the rightward and upward shifts when $\alpha=0.1$.[^p1-fig3]

One printed inequality deserves special care. Main Eq. 6 says that total error is at least $2D(T+\tau)$; SI Eq. S83 likewise uses a lower bound with readout term $2D\tau/\sqrt\alpha$. But the paper's other derived results imply

$$
2DJ\ge\tau^{-2}
\quad\Longrightarrow\quad
J\ge\frac1{2D\tau^2}
\quad\Longrightarrow\quad
\sqrt{\frac{2D}{J}}\le2D\tau.
$$

Thus the ideal asymptotic readout term is at most $2D\tau$, with equality when the information diffusion inequality is saturated. Substituting an upper bound for this term cannot establish the printed universal lower bound on total error. Within the local Gaussian model, the defensible statement is

$$
V_{\mathrm{total}}(T,L)
\ge2DT+\sqrt{2D/J},
$$

with equality approached as $L\to\infty$ for the ideal observer. At saturation this asymptotic expression becomes $2D(T+\tau)$. For partial access the same issue occurs with the factor $1/\sqrt\alpha$. This is an apparent inconsistency between printed formulas, identified by algebra using the supplied sources. It is not a claim that the authors issued a correction.[^p1-printed]

For a concrete strict inequality case, keep $\tau=0.1\,\mathrm{s}$ and $D=0.005\,\mathrm{rad}^2/\mathrm{s}$ but set $J=40{,}000\,\mathrm{rad}^{-2}\mathrm{s}^{-1}$. Then $2DJ=400\,\mathrm{s}^{-2}$ exceeds $\tau^{-2}=100\,\mathrm{s}^{-2}$. The limiting readout variance is $0.0005\,\mathrm{rad}^2$, whereas $2D\tau=0.001\,\mathrm{rad}^2$. At $T=2\,\mathrm{s}$, the Gaussian ideal total limit is $0.0205\,\mathrm{rad}^2$, below $2D(T+\tau)=0.021\,\mathrm{rad}^2$. These values expose the algebraic problem without assuming the bound is saturated.

Finally, the short readout interval is not a short lifetime of the underlying integrator. A tuned integrator can continue to represent the mean of accumulated inputs while its variance grows. A leak would instead pull its mean toward a particular value. Diffusion limits the accuracy of the integral and the usefulness of long observation; it does not by itself introduce that restoring pull. Applying these predictions to an animal also requires checking its spike statistics, tuning, drift, access to spikes, and other sources of movement noise.[^p1-integrator]

[^p1-info-main]: Burak, Y., & Fiete, I. R. (2012). *Fundamental limits on persistent activity in networks of noisy neurons*. Proceedings of the National Academy of Sciences, 109(43), 17645–17650, main pp. 2–4, Eqs. 3–5. https://doi.org/10.1073/pnas.1117386109.

[^p1-fi-source]: Burak, Y., & Fiete, I. R. (2012). *Fundamental limits on persistent activity in networks of noisy neurons*, Supporting Text, pp. 9–10, Section IV, Eqs. S42–S44; main Eq. 3. https://doi.org/10.1073/pnas.1117386109. The score variance calculation is expanded for teaching.

[^p1-cr]: Burak, Y., & Fiete, I. R. (2012). *Fundamental limits on persistent activity in networks of noisy neurons*. PNAS, 109(43), 17645–17650, p. 3, Information-Diffusion Inequality and Saturation. https://doi.org/10.1073/pnas.1117386109. The scalar Cramér Rao proof is a teaching reconstruction of the bound invoked there.

[^p1-bound-source]: Burak, Y., & Fiete, I. R. (2012). *Fundamental limits on persistent activity in networks of noisy neurons*, Supporting Text, pp. 10–11, Eqs. S45–S49; main Eq. 4. https://doi.org/10.1073/pnas.1117386109.

[^p1-equality]: Burak, Y., & Fiete, I. R. (2012). *Fundamental limits on persistent activity in networks of noisy neurons*, Supporting Text, p. 11, Eqs. S47–S51. https://doi.org/10.1073/pnas.1117386109. The linear-family counterexample is a guide calculation qualifying the source's converse.

[^p1-matrix]: Burak, Y., & Fiete, I. R. (2012). *Fundamental limits on persistent activity in networks of noisy neurons*, Supporting Text, pp. 10–12, Eqs. S44 and S52–S56. https://doi.org/10.1073/pnas.1117386109. The residual matrix proof here is an equivalent teaching reconstruction.

[^p1-scaling]: Burak, Y., & Fiete, I. R. (2012). *Fundamental limits on persistent activity in networks of noisy neurons*. PNAS, 109(43), 17645–17650, p. 2, discussion after Eq. 2; pp. 5–6, Weak Fluctuations. https://doi.org/10.1073/pnas.1117386109. Comparisons with different held quantities are made explicit here.

[^p1-width]: Burak, Y., & Fiete, I. R. (2012). *Fundamental limits on persistent activity in networks of noisy neurons*. PNAS, 109(43), 17645–17650, p. 4, tuning width discussion. https://doi.org/10.1073/pnas.1117386109. The paper cites Zhang and Sejnowski's tuning work. The integral scaling and alternative firing budget here are teaching derivations, not a separate verification of that cited paper.

[^p1-colocation]: Burak, Y., & Fiete, I. R. (2012). *Fundamental limits on persistent activity in networks of noisy neurons*. PNAS, 109(43), 17645–17650, pp. 4–5, sensory representation comparison and footnote concerning similarity of sensory and persistent tuning. https://doi.org/10.1073/pnas.1117386109.

[^p1-read-setup]: Burak, Y., & Fiete, I. R. (2012). *Fundamental limits on persistent activity in networks of noisy neurons*, Supporting Text, p. 12, Eq. S57. https://doi.org/10.1073/pnas.1117386109.

[^p1-read-gaussian]: Burak, Y., & Fiete, I. R. (2012). *Fundamental limits on persistent activity in networks of noisy neurons*, Supporting Text, p. 13, Eqs. S58–S63 and the approximation paragraph preceding them. https://doi.org/10.1073/pnas.1117386109.

[^p1-naive]: Burak, Y., & Fiete, I. R. (2012). *Fundamental limits on persistent activity in networks of noisy neurons*, Supporting Text, pp. 15–16, Eqs. S76–S81. https://doi.org/10.1073/pnas.1117386109. The double integral calculation exposes the cross time covariance terms compressed in the printed derivation.

[^p1-ideal]: Burak, Y., & Fiete, I. R. (2012). *Fundamental limits on persistent activity in networks of noisy neurons*, Supporting Text, pp. 13–15, Eqs. S58–S75. https://doi.org/10.1073/pnas.1117386109. The supplement identifies the solution with a reverse Kalman filter. Here the equivalent precision recursion supplies a derivation without assuming prior knowledge of that filter. The printed plus sign in S71 does not match its hyperbolic cosine solution S73; the recursion independently gives the final S75 result.

[^p1-time]: Burak, Y., & Fiete, I. R. (2012). *Fundamental limits on persistent activity in networks of noisy neurons*. PNAS, 109(43), 17645–17650, main Eq. 5 and Optimal Observation Time; Supporting Text, Eqs. S75 and S80–S81. https://doi.org/10.1073/pnas.1117386109.

[^p1-partial]: Burak, Y., & Fiete, I. R. (2012). *Fundamental limits on persistent activity in networks of noisy neurons*, Supporting Text, p. 16, Incomplete readout, Eq. S82 and Fig. S2. https://doi.org/10.1073/pnas.1117386109. The random thinning derivation states when the fraction of spikes equals the fraction of information.

[^p1-two-times]: Burak, Y., & Fiete, I. R. (2012). *Fundamental limits on persistent activity in networks of noisy neurons*, Supporting Text, pp. 17–18, Eqs. S84–S92. https://doi.org/10.1073/pnas.1117386109. The linear matrix here follows directly from S84; its rate decay block is negative, as required by that differential equation, despite the positive sign printed in the corresponding block of S85.

[^p1-gaussian]: Burak, Y., & Fiete, I. R. (2012). *Fundamental limits on persistent activity in networks of noisy neurons*, Supporting Text, p. 19, White Gaussian noise, Eqs. S93–S95; main pp. 3–4. https://doi.org/10.1073/pnas.1117386109. Constant noise strength $q$ and its likelihood are retained explicitly in the guide's reconstruction.

[^p1-fig3]: Burak, Y., & Fiete, I. R. (2012). *Fundamental limits on persistent activity in networks of noisy neurons*. PNAS, 109(43), 17645–17650, Fig. 3, p. 4; Supporting Text, Fig. S2, p. 16. https://doi.org/10.1073/pnas.1117386109. The caption's readout equation numbers are stale relative to the supplied supplement; the corresponding results are S75 and S79–S81.

[^p1-printed]: Burak, Y., & Fiete, I. R. (2012). *Fundamental limits on persistent activity in networks of noisy neurons*. PNAS, 109(43), 17645–17650, main Eqs. 4–6; Supporting Text, Eqs. S75 and S83. https://doi.org/10.1073/pnas.1117386109. The inequality direction is checked algebraically here, without assuming an author correction or changing the supplied source.

[^p1-integrator]: Burak, Y., & Fiete, I. R. (2012). *Fundamental limits on persistent activity in networks of noisy neurons*. PNAS, 109(43), 17645–17650, Discussion, p. 5; Supporting Text, Integration time constant, p. 17. https://doi.org/10.1073/pnas.1117386109.

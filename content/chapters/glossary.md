# Glossary {#ch:GLOSSARY}

These short definitions support lookup after the explanations and examples in the main chapters.

- [[**abducens nucleus:**]{.definition-term custom-style="Definition Term"} A brainstem group containing the motor neurons recorded in the eye-drift study. Their axons activate the lateral rectus eye muscle.]{.definition-explanation}
- [[**activity bump:**]{.definition-term custom-style="Definition Term"} A localized peak of population firing rates across neurons ordered by their preferred represented values.]{.definition-explanation}
- [[**attractor manifold:**]{.definition-term custom-style="Definition Term"} The continuous family of persistent activity states, described by its represented coordinates rather than by every neural activity separately.]{.definition-explanation}
- [[**Betti numbers:**]{.definition-term custom-style="Definition Term"} Counts of independent connected components, loops, cavities, and their higher-dimensional counterparts.]{.definition-explanation}
- [[**Brownian motion:**]{.definition-term custom-style="Definition Term"} A continuous random process starting at zero with independent Gaussian increments of mean zero and variance equal to elapsed time.]{.definition-explanation}
- [[**causal filter:**]{.definition-term custom-style="Definition Term"} A rule whose current output depends only on present and past input.]{.definition-explanation}
- [[**coefficient of determination:**]{.definition-term custom-style="Definition Term"} For the optimal linear prediction with an intercept, the fraction of response variance removed by prediction. With one predictor it equals the squared correlation.]{.definition-explanation}
- [[**coefficient of variation:**]{.definition-term custom-style="Definition Term"} Standard deviation divided by mean. In the spike-train discussion it is applied to interspike intervals.]{.definition-explanation}
- [[**continuous attractor:**]{.definition-term custom-style="Definition Term"} A continuous family of fixed points with restoring dynamics toward the family and neutral motion along it in the ideal deterministic model.]{.definition-explanation}
- [[**convolution:**]{.definition-term custom-style="Definition Term"} An integral or sum combining past input values with a shifted response kernel to obtain a filtered output.]{.definition-explanation}
  <!-- vale ai-tells.ConsequenceParticiple = NO -->
- [[**correlation coefficient:**]{.definition-term custom-style="Definition Term"} Covariance divided by the product of standard deviations, giving a dimensionless measure of linear association.]{.definition-explanation}
  <!-- vale ai-tells.ConsequenceParticiple = YES -->
- [[**correlation length:**]{.definition-term custom-style="Definition Term"} The local distance scale $\ell_c=\sqrt{-C(0)/C''(0)}$ for a smooth stationary spatial map. It compares input variation with variation of its slope; it need not specify covariance at large separations. [Spatial-map explanation](../frontmatter/ch-mathematical-tools.html#sec-math-tools-random-fields).]{.definition-explanation}
- [[**covariance:**]{.definition-term custom-style="Definition Term"} The mean product of two centered random variables, measuring their shared variation.]{.definition-explanation}
- [[**connection matrix:**]{.definition-term custom-style="Definition Term"} The matrix $W$ of fixed connection weights. Entry $W_{ij}$ maps sending neuron $j$'s synaptic activation into receiving neuron $i$'s input. [Mechanism and example](../frontmatter/ch-mathematical-tools.html#sec-math-tools-weights).]{.definition-explanation}
- [[**Cramér Rao bound:**]{.definition-term custom-style="Definition Term"} A lower bound on local unbiased estimation variance under the required regularity conditions, expressed through inverse Fisher information.]{.definition-explanation}
- [[**critical point:**]{.definition-term custom-style="Definition Term"} A point where a function's gradient is zero. The Euler calculation also requires invertible Hessians.]{.definition-explanation}
- [[**decoding:**]{.definition-term custom-style="Definition Term"} Estimating a represented value from neural responses.]{.definition-explanation}
- [[**dendrite:**]{.definition-term custom-style="Definition Term"} A branching input structure of a neuron.]{.definition-explanation}
- [[**diffusion coefficient:**]{.definition-term custom-style="Definition Term"} The coefficient $D$ in the local one-dimensional displacement variance $2Dt$. Its units are coordinate squared per time.]{.definition-explanation}
- [[**diffusion tensor:**]{.definition-term custom-style="Definition Term"} The matrix giving local coordinate-displacement covariances per twice the elapsed time.]{.definition-explanation}
- [[**Dirac delta:**]{.definition-term custom-style="Definition Term"} An ideal unit impulse, with integral one across its location. In the spike equation it adds one unit of synaptic activation at the spike time. In the probability initial condition it concentrates all probability at one coordinate.]{.definition-explanation}
- [[**displacement:**]{.definition-term custom-style="Definition Term"} The change in a coordinate between two observations. For eye angle, $\Delta x=x(t+\ell)-x(t)$ over lag $\ell$.]{.definition-explanation}
- [[**elasticity:**]{.definition-term custom-style="Definition Term"} The tendency of stretched muscles and surrounding tissues to exert restoring forces.]{.definition-explanation}
- [[**encoding:**]{.definition-term custom-style="Definition Term"} Establishing a population activity pattern from an input.]{.definition-explanation}
- [[**estimator:**]{.definition-term custom-style="Definition Term"} A rule that converts observed data into an estimated value. The memory decoder estimates an angle or other represented coordinate from spikes.]{.definition-explanation}
- [[**Euler characteristic:**]{.definition-term custom-style="Definition Term"} The alternating sum of Betti numbers. In three dimensions, components minus independent loops plus enclosed cavities.]{.definition-explanation}
- [[**excess kurtosis:**]{.definition-term custom-style="Definition Term"} The fourth centered moment divided by the squared variance, minus three. It is zero for a Gaussian population.]{.definition-explanation}
- [[**excitatory input:**]{.definition-term custom-style="Definition Term"} In the models used here, an input that increases a receiving neuron's tendency to fire.]{.definition-explanation}
- [[**excursion set:**]{.definition-term custom-style="Definition Term"} The positions where a function exceeds a specified level.]{.definition-explanation}
- [[**extraocular muscles:**]{.definition-term custom-style="Definition Term"} The six muscles attached to the outside of each eyeball that control its orientation.]{.definition-explanation}
- [[**Fano factor:**]{.definition-term custom-style="Definition Term"} Spike-count variance divided by mean count, for a specified counting interval and condition.]{.definition-explanation}
- [[**firing rate:**]{.definition-term custom-style="Definition Term"} The expected number of spikes per unit time, conditional on the modeled circumstances.]{.definition-explanation}
- [[**Fisher information:**]{.definition-term custom-style="Definition Term"} How sensitively the probabilities of observations change with a small change in the value being estimated. Formally, the expected squared score. In the independent Poisson model it compares squared changes in expected counts with count variance. [Explanation and example](../frontmatter/ch-mathematical-tools.html#sec-math-tools-fisher); [formal derivation](../chapters/ch-memory-information.html#sec-memory-fi).]{.definition-explanation}
- [[**fixational drift:**]{.definition-term custom-style="Definition Term"} Slow eye motion during attempted fixation, between rapid eye movements. The name includes random wandering; it does not imply systematic mean motion.]{.definition-explanation}
- [[**fixed point:**]{.definition-term custom-style="Definition Term"} A state whose deterministic rate of change is zero.]{.definition-explanation}
- [[**Fokker Planck equation:**]{.definition-term custom-style="Definition Term"} An equation describing how a probability density evolves under drift and diffusion. The convention is stated before using it.]{.definition-explanation}
- [[**gain:**]{.definition-term custom-style="Definition Term"} The scale that converts a change in one signal into a change in another.]{.definition-explanation}
- [[**gamma function:**]{.definition-term custom-style="Definition Term"} The function $\Gamma(t)=\int_0^\infty u^{t-1}e^{-u}\,du$ for $t>0$, extending factorials through $\Gamma(n+1)=n!$.]{.definition-explanation}
- [[**Gaussian curvature:**]{.definition-term custom-style="Definition Term"} For a surface in three dimensions, the product of its two principal curvatures.]{.definition-explanation}
- [[**Gaussian process:**]{.definition-term custom-style="Definition Term"} A distribution over functions whose values at any finite collection of positions have a joint Gaussian distribution.]{.definition-explanation}
- [[**grid cell:**]{.definition-term custom-style="Definition Term"} A spatially tuned entorhinal neuron with repeated firing fields, often approximately hexagonally arranged in a two-dimensional arena.]{.definition-explanation}
- [[**Hessian:**]{.definition-term custom-style="Definition Term"} The matrix of second derivatives of a function with respect to its coordinates.]{.definition-explanation}
- [[**hippocampus:**]{.definition-term custom-style="Definition Term"} A brain region involved in memory and navigation.]{.definition-explanation}
- [[**hyperbolic cotangent:**]{.definition-term custom-style="Definition Term"} The function $\coth z=1/\tanh z$, for real $z\ne0$.]{.definition-explanation}
- [[**hyperbolic tangent:**]{.definition-term custom-style="Definition Term"} The function $\tanh z=(e^z-e^{-z})/(e^z+e^{-z})$.]{.definition-explanation}
- [[**impulse response:**]{.definition-term custom-style="Definition Term"} The output of a linear filter in response to a unit-area input impulse, from which responses to general input can be assembled.]{.definition-explanation}
- [[**inertia:**]{.definition-term custom-style="Definition Term"} Resistance to a change in motion. Rotational inertia relates torque to angular acceleration; it does not supply a stationary holding torque.]{.definition-explanation}
- [[**inhibitory input:**]{.definition-term custom-style="Definition Term"} In the models used here, an input that reduces a receiving neuron's tendency to fire.]{.definition-explanation}
- [[**internal Fisher information rate:**]{.definition-term custom-style="Definition Term"} The local information per unit observation time about the instantaneous attractor coordinate, as defined by the 2012 spike model.]{.definition-explanation}
- [[**inverse hyperbolic tangent:**]{.definition-term custom-style="Definition Term"} The inverse of $\tanh$ on $(-1,1)$, given by $\operatorname{artanh}z=\tfrac12\log[(1+z)/(1-z)]$.]{.definition-explanation}
- [[**instantaneous attractor state:**]{.definition-term custom-style="Definition Term"} The point on the attractor reached by following noise-free dynamics from a nearby network state. Its coordinate assigns a represented value even when the current activity lies slightly off the attractor.]{.definition-explanation} [Explanation](../chapters/ch-memory-dynamics.html#sec-memory-linearization).
- [[**isotropy:**]{.definition-term custom-style="Definition Term"} Invariance of the spatial probability law under rotations.]{.definition-explanation}
- [[**Itô convention:**]{.definition-term custom-style="Definition Term"} A stochastic-increment convention that evaluates the noise coefficient at the beginning of each increment.]{.definition-explanation}
- [[**jointly Gaussian vector:**]{.definition-term custom-style="Definition Term"} A random vector for which every linear combination of its entries is Gaussian.]{.definition-explanation}
  <!-- vale ai-tells.EmDashUsage = NO -->
- [[**Kac–Rice formula:**]{.definition-term custom-style="Definition Term"} A way to compute expected crossing or critical-point counts from the joint distribution of a random function and its derivatives, under the relevant regularity assumptions.]{.definition-explanation}
  <!-- vale ai-tells.EmDashUsage = YES -->
  <!-- vale ai-tells.NegatedObject = NO -->
- [[**left zero eigenvector:**]{.definition-term custom-style="Definition Term"} A vector $v$ with $v^T A=0$. With appropriate normalization it extracts the persistent coordinate from a small state disturbance.]{.definition-explanation}
  <!-- vale ai-tells.NegatedObject = YES -->
- [[**likelihood:**]{.definition-term custom-style="Definition Term"} The probability or density of the observed data considered as a function of a proposed parameter value.]{.definition-explanation}
- [[**linearization:**]{.definition-term custom-style="Definition Term"} The first-order approximation to a dynamical equation near a reference state.]{.definition-explanation}
- [[**lognormal distribution:**]{.definition-term custom-style="Definition Term"} A distribution of positive values whose logarithms are Gaussian.]{.definition-explanation}
- [[**low pass filter:**]{.definition-term custom-style="Definition Term"} A filter that suppresses sufficiently rapid input changes relative to slower ones.]{.definition-explanation}
- [[**mean curvature:**]{.definition-term custom-style="Definition Term"} For a surface in three dimensions, the average of its two principal curvatures.]{.definition-explanation}
- [[**lag:**]{.definition-term custom-style="Definition Term"} The time separation between two observations, such as the start and end of a measured displacement.]{.definition-explanation}
- [[**line attractor:**]{.definition-term custom-style="Definition Term"} A one-dimensional continuous family of fixed points, with restoring dynamics toward the family and neutral motion along it in the ideal deterministic model.]{.definition-explanation} [Explanation](../chapters/ch-persistence.html#sec-foundations-attractor).
- [[**locally unbiased:**]{.definition-term custom-style="Definition Term"} An estimate whose mean equals the true value and has derivative one with respect to that value at the point being studied. [Precision bound](../frontmatter/ch-mathematical-tools.html#sec-math-tools-bound).]{.definition-explanation}
- [[**mean squared displacement:**]{.definition-term custom-style="Definition Term"} The average squared change in a coordinate across a specified time lag. An MSD curve plots this average against the lag; squared angle has units of degrees squared, while its square root has units of degrees.]{.definition-explanation}
- [[**median filter:**]{.definition-term custom-style="Definition Term"} A rule replacing each sampled value with a middle-ranked value from its local neighborhood. In the place maps it reduces isolated high or low rates and can change small field features.]{.definition-explanation}
- [[**microsaccades:**]{.definition-term custom-style="Definition Term"} Brief, rapid eye movements that occur during attempted fixation.]{.definition-explanation}
- [[**Morse theory:**]{.definition-term custom-style="Definition Term"} A theory relating the topology of a function's level-set regions to its critical points. The analysis uses a signed critical-point count under its smoothness and nondegeneracy assumptions, including boundary contributions.]{.definition-explanation}
- [[**neural transfer function:**]{.definition-term custom-style="Definition Term"} The modeled relationship between a neuron's input and its expected firing rate.]{.definition-explanation}
- [[**neuron:**]{.definition-term custom-style="Definition Term"} A signaling cell in the nervous system.]{.definition-explanation}
- [[**ocular motoneurons (OMNs):**]{.definition-term custom-style="Definition Term"} Neurons whose spikes activate the eye muscles.]{.definition-explanation}
- [[**ocular plant:**]{.definition-term custom-style="Definition Term"} The muscles and mechanical eye system that transform motor activity into eye motion.]{.definition-explanation}
- [[**oculomotor integrator:**]{.definition-term custom-style="Definition Term"} A neural circuit that converts movement commands into a maintained eye-position command.]{.definition-explanation}
- [[**one sided t test:**]{.definition-term custom-style="Definition Term"} A test of a mean against a reference value in a specified direction, using the mean difference divided by its estimated sampling uncertainty. The eye paper tests whether the mean cell correlation exceeds zero.]{.definition-explanation}
- [[**p value:**]{.definition-term custom-style="Definition Term"} Under the specified null comparison, the probability of a test statistic at least as extreme in the tested direction as the observed one.]{.definition-explanation}
- [[**path integration:**]{.definition-term custom-style="Definition Term"} Updating an estimate of position from movement.]{.definition-explanation}
  <!-- vale ai-tells.FigurativeFires = NO -->
- [[**place cell:**]{.definition-term custom-style="Definition Term"} A spatially selective hippocampal neuron that fires strongly in one or more localized regions of an environment.]{.definition-explanation}
  <!-- vale ai-tells.FigurativeFires = YES -->
- [[**place field:**]{.definition-term custom-style="Definition Term"} A connected region of elevated spatial firing, as defined by the model or stated measurement procedure.]{.definition-explanation}
- [[**plasticity:**]{.definition-term custom-style="Definition Term"} A lasting, experience-dependent change in neural responses or connections. In gaze control it can change how well the holding circuit is calibrated.]{.definition-explanation}
- [[**Poisson process:**]{.definition-term custom-style="Definition Term"} A counting process with independent increments and a deterministic constant or time-dependent event rate. Its count over an interval has equal mean and variance. In a recurrent model, conditionally Poisson instantaneous spike generation does not make complete spike trains have independent increments.]{.definition-explanation}
  <!-- vale ai-tells.FigurativeCarries = NO -->
- [[**population code:**]{.definition-term custom-style="Definition Term"} A representation carried by the pattern of responses across neurons.]{.definition-explanation}
  <!-- vale ai-tells.FigurativeCarries = YES -->
- [[**precision:**]{.definition-term custom-style="Definition Term"} The reciprocal of variance for a scalar Gaussian estimate.]{.definition-explanation}
- [[**preferred angle:**]{.definition-term custom-style="Definition Term"} An angle where a neuron's tuning curve peaks.]{.definition-explanation}
- [[**prior distribution:**]{.definition-term custom-style="Definition Term"} A distribution representing knowledge about likely parameter values before observing the current data.]{.definition-explanation}
- [[**random field:**]{.definition-term custom-style="Definition Term"} A random function indexed by spatial position. For a Gaussian random field, values at every finite collection of positions are jointly Gaussian. One drawn map can remain fixed while an animal revisits positions. [Meaning and model](../frontmatter/ch-mathematical-tools.html#sec-math-tools-random-fields).]{.definition-explanation}
- [[**rate map:**]{.definition-term custom-style="Definition Term"} An estimate of spatial firing rate from spikes per time spent at each position.]{.definition-explanation}
- [[**Rayleigh distribution:**]{.definition-term custom-style="Definition Term"} The distribution of a positive variable that is a scaled square root of an exponential variable.]{.definition-explanation}
- [[**recurrent connectivity:**]{.definition-term custom-style="Definition Term"} Connections that feed activity back into the same neuronal population.]{.definition-explanation}
- [[**renewal process:**]{.definition-term custom-style="Definition Term"} An event process with independent, identically distributed intervals under the fixed conditions being modeled.]{.definition-explanation}
- [[**retina:**]{.definition-term custom-style="Definition Term"} The light-sensitive tissue at the back of the eye.]{.definition-explanation}
- [[**right zero eigenvector:**]{.definition-term custom-style="Definition Term"} A state-space direction $u$ satisfying $Au=0$ for the linearized dynamics.]{.definition-explanation}
- [[**root mean squared displacement:**]{.definition-term custom-style="Definition Term"} The square root of mean squared displacement, expressed in the original coordinate's units.]{.definition-explanation}
- [[**saccade:**]{.definition-term custom-style="Definition Term"} A rapid eye movement that changes gaze direction.]{.definition-explanation}
- [[**score:**]{.definition-term custom-style="Definition Term"} The derivative of log likelihood with respect to the parameter being estimated.]{.definition-explanation}
- [[**skew:**]{.definition-term custom-style="Definition Term"} The third centered moment divided by the variance to the power $3/2$, measuring asymmetry.]{.definition-explanation}
- [[**smoothness:**]{.definition-term custom-style="Definition Term"} The existence and regularity of derivatives of a function. The crossing and peak calculations require different derivative orders.]{.definition-explanation}
- [[**spatial covariance:**]{.definition-term custom-style="Definition Term"} The covariance of input values at two positions across possible spatial maps. For a stationary map it depends on separation, rather than absolute position. [Spatial-map explanation](../frontmatter/ch-mathematical-tools.html#sec-math-tools-random-fields).]{.definition-explanation}
- [[**Spearman correlation:**]{.definition-term custom-style="Definition Term"} Correlation computed after replacing observations by their ranks. It checks whether the two measured quantities tend to increase together without requiring a linear relation.]{.definition-explanation}
- [[**spike:**]{.definition-term custom-style="Definition Term"} A brief electrical event emitted by a neuron.]{.definition-explanation}
- [[**standard error of the mean (SEM):**]{.definition-term custom-style="Definition Term"} An estimate of uncertainty in a sample mean. Its interpretation depends on which observations are treated as independent, such as trials, cells, or animals.]{.definition-explanation}
- [[**state:**]{.definition-term custom-style="Definition Term"} The quantities that specify a modeled system's current condition and determine its subsequent dynamics together with future inputs and noise.]{.definition-explanation}
- [[**Stationarity:**]{.definition-term custom-style="Definition Term"} In the place-field model, invariance of spatial statistics under translating the map.]{.definition-explanation}
- [[**stationary process:**]{.definition-term custom-style="Definition Term"} A random process whose probability law is unchanged by shifting its time or position origin. Weaker covariance-only stationarity must be specified when used.]{.definition-explanation}
- [[**Stratonovich convention:**]{.definition-term custom-style="Definition Term"} A stochastic-increment convention using midpoint evaluation in the limiting increments.]{.definition-explanation}
- [[**sub-Poisson spiking:**]{.definition-term custom-style="Definition Term"} Spiking with less variability than a matched Poisson reference according to the stated measure and conditions.]{.definition-explanation}
- [[**superdiffusion:**]{.definition-term custom-style="Definition Term"} Mean squared displacement growing faster than linearly with lag over the range being described.]{.definition-explanation}
- [[**synapse:**]{.definition-term custom-style="Definition Term"} A connection through which one neuron influences another.]{.definition-explanation}
- [[**synaptic activation:**]{.definition-term custom-style="Definition Term"} In the 2012 model, the decaying trace of a neuron's outgoing spikes. Each spike adds one unit; connection weights convert this trace into input to other cells.]{.definition-explanation}
- [[**systematic drift:**]{.definition-term custom-style="Definition Term"} A nonzero mean velocity of the represented coordinate, distinct from random spreading.]{.definition-explanation}
- [[**tonic firing:**]{.definition-term custom-style="Definition Term"} Sustained neural firing during a holding period; the spike times need not be perfectly periodic.]{.definition-explanation}
- [[**torque:**]{.definition-term custom-style="Definition Term"} The turning effect of a force.]{.definition-explanation}
- [[**Translation invariance:**]{.definition-term custom-style="Definition Term"} In the readout model, invariance under shifts of the represented value. It makes the readout variance independent of the cue state.]{.definition-explanation}
- [[**translation symmetry:**]{.definition-term custom-style="Definition Term"} Shifting an activity pattern along the represented coordinate leaves the network dynamics unchanged in form.]{.definition-explanation} This describes the network dynamics. The readout calculation separately assumes that its estimation-error statistics are unchanged when the represented value is shifted.
- [[**tuning curve:**]{.definition-term custom-style="Definition Term"} A neuron's expected firing rate as a function of a represented variable.]{.definition-explanation}
- [[**unbiased:**]{.definition-term custom-style="Definition Term"} Describes an estimator whose expected value equals the parameter locally under the conditions used in the estimation bound.]{.definition-explanation}
- [[**upcrossing:**]{.definition-term custom-style="Definition Term"} A point where a function crosses upward through a specified threshold.]{.definition-explanation}
- [[**viscosity:**]{.definition-term custom-style="Definition Term"} Mechanical resistance to motion that dissipates energy. It damps movement but supplies no holding torque at zero velocity.]{.definition-explanation}
- [[**weak fluctuation approximation:**]{.definition-term custom-style="Definition Term"} An expansion about the deterministic population dynamics in which the aggregate effects of many small spike contributions remain small.]{.definition-explanation}
- [[**Weibull distribution:**]{.definition-term custom-style="Definition Term"} A positive-variable distribution with survival probability $\exp[-(s/b)^k]$, scale $b>0$, and shape $k>0$.]{.definition-explanation}
- [[**White noise:**]{.definition-term custom-style="Definition Term"} An ideal noise input with zero covariance at unequal times and a delta-function covariance at equal times. Its integrated increments have finite variance.]{.definition-explanation}

## Physical implementation and neural memory {#sec:GLOSSARY-HARDWARE}

These terms are explained in the linked Part III passages.

- [[**analog state:**]{.definition-term custom-style="Definition Term"} A physical magnitude, such as capacitor voltage, used to represent a model quantity.]{.definition-explanation} [Explanation](../chapters/ch-hardware-memory.html#sec-hardware-memory-storage).
<!-- vale ai-tells.CataphoricForecasting = NO -->
- [[**bistability:**]{.definition-term custom-style="Definition Term"} Two locally stable states under the same ongoing conditions.]{.definition-explanation} [Explanation](../chapters/ch-hardware-dynamics.html#sec-hardware-dynamics-evidence).
<!-- vale ai-tells.CataphoricForecasting = YES -->
- [[**device mismatch:**]{.definition-term custom-style="Definition Term"} Persistent differences between nominally identical circuit elements.]{.definition-explanation} [Explanation](../chapters/ch-hardware-memory.html#sec-hardware-memory-storage).
- [[**digital storage:**]{.definition-term custom-style="Definition Term"} Discrete symbols represented by distinguishable physical ranges.]{.definition-explanation} [Explanation](../chapters/ch-hardware-memory.html#sec-hardware-memory-storage).
- [[**in-memory computing:**]{.definition-term custom-style="Definition Term"} Performing operations where values are stored, reducing transfers to a separate arithmetic unit.]{.definition-explanation} [Explanation](../chapters/ch-hardware-memory.html#sec-hardware-memory-updates).
- [[**mixed-signal hardware:**]{.definition-term custom-style="Definition Term"} Hardware combining analog circuit variables with digital storage, communication, or calculation.]{.definition-explanation} [Explanation](../chapters/ch-hardware-memory.html#sec-hardware-memory-updates).
- [[**neuromorphic computing:**]{.definition-term custom-style="Definition Term"} Electronic computation inspired by neural organization or dynamics, with digital, analog, or combined implementations.]{.definition-explanation} [Explanation](../chapters/ch-hardware-memory.html#sec-hardware-memory-roles).
- [[**nonvolatile storage:**]{.definition-term custom-style="Definition Term"} Storage that can retain its state without continuous power, within its retention limits.]{.definition-explanation} [Explanation](../chapters/ch-hardware-memory.html#sec-hardware-memory-storage).
- [[**on-chip learning:**]{.definition-term custom-style="Definition Term"} Computing and applying some weight changes using circuitry on the chip.]{.definition-explanation} [Explanation](../chapters/ch-neuromorphic-systems.html#sec-neuromorphic-systems-architectures).
- [[**phase-change memory (PCM):**]{.definition-term custom-style="Definition Term"} Storage in a material atomic arrangement read through its resistance or conductance.]{.definition-explanation} [Explanation](../chapters/ch-hardware-memory.html#sec-hardware-memory-storage).
- [[**pinning:**]{.definition-term custom-style="Definition Term"} Attraction of a nominally continuous memory toward preferred states.]{.definition-explanation} [Explanation](../chapters/ch-hardware-dynamics.html#sec-hardware-dynamics-errors).
- [[**static random-access memory (SRAM):**]{.definition-term custom-style="Definition Term"} Digital storage whose powered transistor feedback maintains bits.]{.definition-explanation} [Explanation](../chapters/ch-hardware-memory.html#sec-hardware-memory-storage).
- [[**working memory:**]{.definition-term custom-style="Definition Term"} Keeping information about recent input available for a later task.]{.definition-explanation} [Explanation](../chapters/ch-hardware-memory.html#sec-hardware-memory-roles).
- [[**capacitor:**]{.definition-term custom-style="Definition Term"} A component that stores separated electric charge, with charge and voltage related by its capacitance.]{.definition-explanation} [Explanation](../chapters/ch-hardware-memory.html#sec-hardware-memory-storage).
- [[**conductance:**]{.definition-term custom-style="Definition Term"} Current per unit applied voltage where current is approximately proportional to voltage. It is the inverse of resistance.]{.definition-explanation} [Explanation](../chapters/ch-hardware-memory.html#sec-hardware-memory-storage).
- [[**current:**]{.definition-term custom-style="Definition Term"} Electric charge flowing per unit time.]{.definition-explanation} [Explanation](../chapters/ch-hardware-memory.html#sec-hardware-memory-storage).
- [[**host computer:**]{.definition-term custom-style="Definition Term"} A separate computer running parts of an experiment outside the neuromorphic chip.]{.definition-explanation} [Explanation](../chapters/ch-neuromorphic-systems.html).
- [[**register:**]{.definition-term custom-style="Definition Term"} A small, fast digital storage location.]{.definition-explanation} [Explanation](../chapters/ch-neuromorphic-systems.html#sec-neuromorphic-systems-limits).
- [[**unwrapping:**]{.definition-term custom-style="Definition Term"} Tracking crossings of a full turn to continue an angular trajectory, when sampling resolves the crossings reliably.]{.definition-explanation} [Explanation](../chapters/ch-hardware-tests.html#sec-hardware-tests-protocol).
- [[**voltage:**]{.definition-term custom-style="Definition Term"} Electrical energy difference per unit charge.]{.definition-explanation} [Explanation](../chapters/ch-hardware-memory.html#sec-hardware-memory-storage).

## Simulation and methods {#sec:GLOSSARY-SIMULATION}

These terms describe how the models are executed and checked in Part IV.

- [[**Euler update:**]{.definition-term custom-style="Definition Term"} A numerical step that approximates change over a short interval by the current derivative times that interval.]{.definition-explanation}
- [[**fitted statistic:**]{.definition-term custom-style="Definition Term"} A measured summary used to choose a model's parameters.]{.definition-explanation}
- [[**random seed:**]{.definition-term custom-style="Definition Term"} A value used to initialize a pseudorandom generator so that a specified implementation can repeat a sample sequence.]{.definition-explanation}
- [[**discretization:**]{.definition-term custom-style="Definition Term"} Representing a continuous variable such as time or position with finitely many sample points.]{.definition-explanation}
- [[**convergence check:**]{.definition-term custom-style="Definition Term"} A test of whether a reported quantity changes acceptably little when numerical resolution is refined.]{.definition-explanation}
- [[**Monte Carlo simulation:**]{.definition-term custom-style="Definition Term"} Estimating a quantity through repeated calculations with random samples.]{.definition-explanation}

- [[**Gaussian filter:**]{.definition-term custom-style="Definition Term"} A smoothing rule that averages nearby values with weights that decrease with distance according to a Gaussian function.]{.definition-explanation}

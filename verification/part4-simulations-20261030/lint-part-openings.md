# Noise limits memory accuracy in continuous attractor models

In a model neural circuit, a pattern of firing rates across many nerve cells can represent a remembered angle. Random spike timing can change that angle while activity persists. The central source, [Burak and Fiete (2012)](https://doi.org/10.1073/pnas.1117386109), derives how quickly accuracy can be lost and how well the value can be read. Chapters 1 and 2 establish the background. Chapters 3 and 5 develop the central diffusion and information results. Chapters 4 and 6 explain long-delay behavior and readout. Expanded examples and marked checks of printed formulas are guide-derived.

The contribution labels describe the role of each result here. **Central** is a main finding of the cited paper. **Supporting** establishes or qualifies that finding. **Background** supplies needed concepts. **Guide-derived** identifies an explanation, comparison, or proposed test developed in this guide.

- **Chapter 1, background:** Neural firing rates and spike variability supply the quantities needed for the later memory calculation. [Burak and Fiete (2012)](https://doi.org/10.1073/pnas.1117386109) supply the Poisson network model. [Ben-Shushan et al. (2022)](https://doi.org/10.1038/s41467-022-29201-y) and [Mainali et al. (2025)](https://doi.org/10.1016/j.neuron.2025.01.017) supply eye-control and spatial-coding context. The elementary numerical examples are guide-derived.

- **Chapter 2, background and mechanism:** A stable pattern of neural activity can retain a value while noise moves that value along a family of states. This is the continuous-memory setup of [Burak and Fiete (2012)](https://doi.org/10.1073/pnas.1117386109). The two-variable illustrations are guide-derived.

- **Chapter 3, central result:** [Burak and Fiete (2012)](https://doi.org/10.1073/pnas.1117386109) derive memory diffusion by projecting spike fluctuations through the network dynamics. The symmetric formula uses the authors' [2017 correction](https://doi.org/10.1073/pnas.1706051114). Expanded projection examples are guide-derived.

- **Chapter 4, supporting results:** [Burak and Fiete (2012)](https://doi.org/10.1073/pnas.1117386109) explain long-delay behavior, angular boundaries, and state-dependent diffusion. These qualify how the central diffusion result can be used. The guide adds explicit boundary calculations and distinguishes its checks of other printed equations from the official correction.

- **Chapter 5, central result:** [Burak and Fiete (2012)](https://doi.org/10.1073/pnas.1117386109) relate the information in spikes to a lower bound on memory diffusion. The guide expands the proofs and labels its counterexamples and comparisons of fixed quantities.

- **Chapter 6, central readout result and supporting extensions:** [Burak and Fiete (2012)](https://doi.org/10.1073/pnas.1117386109) derive limits on estimating a value that moves during observation. Partial access and alternative time scales extend that result. The guide supplies intermediate calculations and identifies source formulas needing qualification.

# Eye motion and place fields constrain different parts of a neural code

These studies connect neural activity to eye control in monkeys and location in rodents and bats. [Ben-Shushan et al. (2022)](https://doi.org/10.1038/s41467-022-29201-y) supply the central shared-drive inference and a possible integrator explanation in Chapters 7 to 9. [Mainali et al. (2025)](https://doi.org/10.1016/j.neuron.2025.01.017) supply the spatial model, field-size predictions, and supporting shape tests in Chapters 10 to 12. Chapter 13 is a guide-derived comparison of those results with Burak and Fiete (2012). The eye chapters begin with recordings and then test a possible neural source. The place chapters begin with a spatial input model and then test its field statistics.

The contribution labels describe the role of each result here. **Central** is a main finding of the cited paper. **Supporting** establishes or qualifies that finding. **Background** supplies needed concepts. **Guide-derived** identifies an explanation, comparison, or proposed test developed in this guide.

- **Chapter 7, central empirical result:** [Ben-Shushan et al. (2022)](https://doi.org/10.1038/s41467-022-29201-y) infer a substantial shared drive upstream of ocular motor neurons from recorded eye motion and spikes. The filter and covariance calculations explain the assumptions behind that inference.

- **Chapter 8, supporting test:** [Ben-Shushan et al. (2022)](https://doi.org/10.1038/s41467-022-29201-y) compare displacement statistics with the predictions of mechanical filtering and private motor noise. The one-filter calculation is a guide-derived teaching model, distinct from the full simulation.

- **Chapter 9, central proposed explanation:** [Ben-Shushan et al. (2022)](https://doi.org/10.1038/s41467-022-29201-y) show that a noisy integrator model can account for the motion after muscle filtering and delayed feedback. [Aksay et al. (2007)](https://doi.org/10.1038/nn1877) supply supporting circuit architecture. The match supports a possible source, rather than uniquely identifying it.

- **Chapter 10, central spatial model:** [Mainali et al. (2025)](https://doi.org/10.1016/j.neuron.2025.01.017) describe fields and gaps as regions of a smooth random input above or below threshold. Expanded crossing and parameter-inference calculations are guide-derived.

- **Chapter 11, central size predictions:** [Mainali et al. (2025)](https://doi.org/10.1016/j.neuron.2025.01.017) derive dimension-dependent field-size statistics and compare them with recordings. The guide expands the local-peak derivation and separates limiting laws from finite-threshold behavior.

- **Chapter 12, supporting tests and circuit interpretation:** [Mainali et al. (2025)](https://doi.org/10.1016/j.neuron.2025.01.017) examine shapes, slices, and connectedness beyond the fitted summaries. The underlying recordings include [Eliav et al. (2021)](https://doi.org/10.1126/science.abg4020), [Harland et al. (2021)](https://doi.org/10.1016/j.cub.2021.03.003), and [Yartsev and Ulanovsky (2013)](https://doi.org/10.1126/science.1235338). Gaussian maps constrain possible inputs without uniquely identifying wiring.

- **Chapter 13, guide-derived synthesis:** The comparison joins the questions asked by [Burak and Fiete (2012)](https://doi.org/10.1073/pnas.1117386109), [Ben-Shushan et al. (2022)](https://doi.org/10.1038/s41467-022-29201-y), and [Mainali et al. (2025)](https://doi.org/10.1016/j.neuron.2025.01.017). Its common-displacement calculation and proposed joint experiment are developed here. The three papers did not jointly test that model.

# Neural memory in electronic hardware

<!-- vale ai-tells.SequencingMarkers = NO -->
<!-- vale ai-tells.VerbTricolon = NO -->
> “Lastly, I would like to mention that systems of nerve cells, which stimulate each other in various possible cyclical ways, also constitute memories.”
<!-- vale ai-tells.VerbTricolon = YES -->
<!-- vale ai-tells.SequencingMarkers = YES -->

John von Neumann, *The Computer and the Brain* (1958), [printed page 66, PDF page 78](https://vpb.smallyu.net/%5BAuthor%5D%20John.Von.Neumann/The%20Computer%20and%20The%20Brain.pdf#page=78).

Von Neumann compares mutually stimulating nerve cells with electronic circuits that preserve a state through feedback. In the following pages he also questions whether active elements alone could provide the nervous system's main large-capacity store. His comparison invites us to distinguish a memory's physical mechanism from the information it keeps. It does not establish that every brain memory uses persistent activity, or that present hardware follows one historical line from his book.

The setting here is experimental and computational neuroscience joined with electronic engineering. We ask how a silicon circuit can retain a quantity such as an angle, and what physical processes limit its accuracy. [A durable connection weight, a lasting activity pattern, and an accurately remembered value are three different achievements.]{.key-statement}

<!-- vale ai-tells.VerbTricolon = NO -->
The path starts with what is stored and where, then explains what feedback preserves. With those distinctions in place, we compare digital spiking processors, analog neural circuits, and phase-change weight storage. The final chapter turns the comparison into measurements of drift, noise, decoding error, and energy. Parts I and II provide the neural models and experimental reasoning. This Part extends them to selected hardware research current to **October 30, 2026**.
<!-- vale ai-tells.VerbTricolon = YES -->

For a first pass, read the physical explanations, main results, and interpretations. Worked calculations and deeper derivations are folded. The comparison assumes the calculus, basic probability, and linear algebra used earlier. Electronics terms are introduced as they become necessary.

The contribution labels describe the role of each result here. **Central** is a main finding of the cited paper. **Supporting** establishes or qualifies that finding. **Background** supplies needed concepts. **Guide-derived** identifies an explanation, comparison, or proposed test developed in this guide.

- **Chapter 14, background and hardware mechanisms:** von Neumann (1958) motivates the comparison. [Pehle et al. (2022)](https://doi.org/10.3389/fnins.2022.795876), Intel Labs (2021), Scholze et al. (2026), and [Le Gallo et al. (2023)](https://doi.org/10.1038/s41928-023-01010-1) supply the architecture descriptions. Separating stored weights, changing neural states, and remembered values is the guide's organizing comparison.

- **Chapter 15, central neural distinction with supporting hardware examples:** [Seung (1996)](https://doi.org/10.1073/pnas.93.23.13339) and [Burak and Fiete (2012)](https://doi.org/10.1073/pnas.1117386109) explain graded persistence and noise. [Massoud and Horiuchi (2011)](https://doi.org/10.1109/TCSI.2010.2055310) and [Giulioni et al. (2012)](https://doi.org/10.3389/fnins.2011.00149) supply distinct silicon demonstrations. The reduced feedback and error comparisons are guide-derived.

- **Chapter 16, central results of selected hardware studies:** [Kleyko et al. (2025)](https://doi.org/10.1038/s41467-025-55832-y) test temporal computation. [Aitsam et al. (2026)](https://doi.org/10.3389/fnins.2026.1910808) demonstrate persistent spatial activity. [Ortner et al. (2025)](https://doi.org/10.1038/s41467-025-56345-4) study adaptation with phase-change computing. [Wang et al. (2026)](https://doi.org/10.1038/s41563-025-02361-0) study material-state stability. [Sun et al. (2026)](https://doi.org/10.1038/s42256-026-01255-3) evaluate a proposed dual-memory design. These results concern different kinds of memory, as the chapter explains.

- **Chapter 17, guide-derived experiments:** The proposed measurements combine the diffusion and readout questions of [Burak and Fiete (2012)](https://doi.org/10.1073/pnas.1117386109), the output-filtering lesson of [Ben-Shushan et al. (2022)](https://doi.org/10.1038/s41467-022-29201-y), and the spatial-versus-temporal distinction exposed by [Mainali et al. (2025)](https://doi.org/10.1016/j.neuron.2025.01.017). They are suggested tests, not a reported common hardware experiment.

# Simulations connect model assumptions to measurable outcomes

A formula predicts behavior under stated assumptions. A simulation lets us generate the resulting neural activity, eye motion, or spatial map and measure it in the same way as a theoretical prediction or experiment. The useful question is what each computation adds to the evidence, and which physical assumptions determine its output.

The contribution labels describe the role of each result here. **Central** is a main finding of the cited paper. **Supporting** establishes or qualifies that finding. **Background** supplies needed concepts. **Guide-derived** identifies an explanation, comparison, or proposed test developed in this guide.

- **Chapter 18, supporting simulations of a central theory:** [Burak and Fiete (2012)](https://doi.org/10.1073/pnas.1117386109) compare stochastic network trajectories with their analytical diffusion prediction. The 2017 correction applies to Eq. 2. The simulations test the modeled dynamics, rather than measure memory errors in animals.

- **Chapter 19, model support for a central explanation:** [Ben-Shushan et al. (2022)](https://doi.org/10.1038/s41467-022-29201-y) combine recorded-data analysis with a noisy integrator, motor neurons, muscles, and delayed feedback. Aksay et al. (2007) supply supporting circuit architecture. The generated signals test whether that mechanism can reproduce the measured statistics.

- **Chapter 20, central model comparisons:** [Mainali et al. (2025)](https://doi.org/10.1016/j.neuron.2025.01.017) generate thresholded Gaussian spatial maps, fit selected summaries, and test additional field properties. Original animal recordings supply the comparison data. These are static-map simulations rather than recurrent memory dynamics.

- **Chapter 21, guide-derived methods and tool comparison:** The shared reproduction procedure is assembled here from the three studies. Author code is distinguished from optional numerical tools. No new full-paper reproduction is claimed.

The path starts with how recurrent spikes move a stored value. It then adds the motor pathway and measurement procedure needed to compare an internal command with behavior. The spatial-field study changes the independent variable from time to position. With those differences established, the final chapter explains how to choose software and check numerical resolution.

Numerical settings for each paper and implementation cautions are folded. The main text keeps the modeled objects, actions, measurements, and limits visible. Blue definitions introduce simulation terms. Basic expectation, variance, standard deviation, and probability density are assumed.

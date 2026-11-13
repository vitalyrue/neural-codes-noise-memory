import json, pathlib, re, hashlib, math

ROOT=pathlib.Path(r'C:/dev/clsc/burak-papers/guide')
OUT=ROOT/'verification/teaching-alignment-20261029'
P=json.loads((OUT/'final-place-input.json').read_text(encoding='utf-8-sig'))
DATA={}

def unit(short, refs, setting, roles, flow, assumptions, mechanism, objection, reason, question, answer, sources):
    DATA[short]=dict(refs=refs,setting=setting,roles=roles,flow=flow,assumptions=assumptions,mechanism=mechanism,objection=objection,reason=reason,question=question,answer=answer,sources=sources)

unit('ch:GLOSSARY',[7,23,41,49,58,79,91,100],
 'Lookup after the chapter explanations, rather than an independent derivation.',
 'Entries identify neural structures, probability objects and the distinct spatial and temporal models.',
 'A reader finds the meaning already taught in the relevant main chapter.',
 'Local diffusion uses variance 2Dt; Poisson counts require a deterministic rate for independent increments; the recurrent conditional spike model is explicitly distinguished.',
 'Checked mathematical definitions against the displayed chapter formulas: left vectors satisfy v^T A=0 and extract the surviving coordinate, right vectors satisfy Au=0; covariance, score, Fisher information, Euler characteristic and distribution definitions retain their mathematical roles.',
 'The short Poisson or diffusion entries could imply independent complete spike trains or identify spatial scale with temporal diffusion.',
 'The Poisson entry explicitly excludes that recurrent-train inference; diffusion units are coordinate squared per time, whereas Gaussian process and stationarity entries describe a map over position. The definitions match the chapter uses.',
 'Does lookup preserve the distinctions on which the place and synthesis calculations depend?',
 'Yes. Gaussian process means finite joint Gaussian values, excursion set means positions above a level, and local diffusion means variance growth of a coordinate. The entries do not turn a spatial random map into motion. The left/right vector entries agree with the earlier linearized network calculation.',
 ['01-foundations.md sec:FOUNDATIONS-SPIKES and sec:FOUNDATIONS-POISSON','01b-persistence.md sec:FOUNDATIONS-ATTRACTOR and sec:FOUNDATIONS-DIFFUSION','02-memory-dynamics.md sec:MEMORY-LINEARIZATION','03-memory-information.md sec:MEMORY-FI','05-place-fields.md sec:PLACE-GP','05c-place-tests.md sec:PLACE-TOPOLOGY'])

unit('ch:REFERENCES',[3,6,9,12,16,20,24,35,38,41,58,62,65],
 'Bibliography for the three main papers and the cited supporting work.',
 'Authors, dates, venues and identifiers identify publications; the main-article entries also cover their supplements.',
 'Claim footnotes lead to a publication, with the full list supplying source identity.',
 'This is a text and source-identity check, not a claim that all DOI redirects, rendered footnotes or links have passed release checks.',
 'Compared the main articles with their local title pages; checked Maimon volume 655(8125), 1242-1251 against the local primary metadata; checked Taylor, Koyluoglu, Seeholzer, Burak/Fiete 2009, Druckmann and Bittner against primary publication records; the author notes give 6 August 2026.',
 'An inaccessible DOI or a newly published article could hide an incorrect source identity.',
 'The relevant publication identities were recovered from primary pages, local paper text or publication metadata. Some DOI resolver attempts failed, but alternate publisher or author records identify the works. Failed resolver attempts are not recorded as successful link checks.',
 'Do the entries identify the works actually cited in the reviewed explanations?',
 'Yes. The 2012, 2022 and 2025 entries match their papers, the Gaussian notes are separate, Taylor is the cited EC theorem source, and the remaining entries match the related-study paragraph. No source-identity contradiction was found. Citation styling and full first-use order belong to Stage 2/3.',
 ['assets/papers main article title pages','research/related-2026-ca3-ca1-metadata.json','https://nischmainali.github.io/blog/gp-code-notes/','https://arxiv.org/pdf/math/0602545','https://elifesciences.org/articles/22225','https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1006928','https://pubmed.ncbi.nlm.nih.gov/24412418/','https://pubmed.ncbi.nlm.nih.gov/28883072/'])

unit('ch:PLACE-FIELDS',[3,7,9,15,17],
 'Place-cell recordings on routes, floors and in flight volumes motivate one spatial model.',
 'Animal position selects an input-map value; the model threshold converts it into firing rate; recordings estimate rates.',
 'A fixed spatial input map is thresholded, producing connected active intervals or regions.',
 'The route is treated as one dimensional; input is not directly measured; predicted statistics are not the next field location.',
 'The opening correctly separates spatial randomness across maps from fluctuations through time and previews counts plus occupied/gap lengths as information about threshold and spatial scale.',
 'Calling the random input a rate map might imply that the data directly measure synaptic input or that the field map evolves while the animal moves.',
 'p9 identifies combined synaptic input as the interpretation and says recordings estimate firing rates; p17 explicitly fixes each drawn map over movement. Mainali Methods S1 and Eq. 2-3 support these roles.',
 'What is random, and what changes when the animal moves?',
 'The ensemble contains different input functions. During traversal of one draw, x changes and the function is evaluated at x. The chapter does not introduce diffusion or learning.',
 ['Mainali main Eq. 2-3 and introduction','Mainali supplement Methods S1','01-foundations.md spatial rate-map teaching'])

unit('sec:PLACE-GP',[23,27,36,47,50,52,54,66,68,85,98,105],
 'A smooth stationary Gaussian input on physical space is normalized before thresholding.',
 'h is input, z=h/sigma_h is unit variance input, q is a dimensionless cutoff, a converts excess input to Hz, and sigma is distance.',
 'Choose mean and covariance, draw a fixed map, then apply a[z-q]_+ and take its connected positive regions.',
 'Sample smoothness and derivative nondegeneracy are required separately from Gaussian marginal values; isotropy is an additional assumption; the zero-rate field definition differs from a positive measurement cutoff.',
 'Differentiating C(y-x) in x and y gives -C second derivative at zero; normalization gives Var(z prime)=1/sigma squared. Joint Gaussianity turns zero covariance into independence. Rectification creates non-Gaussian output values.',
 'The gain or input amplitude could be treated as interchangeable with threshold or distance scale.',
 'p68 separates their effects and explicitly limits gain-invariant boundaries to the zero-rate definition. p105 allows equal local scales with different long-distance covariance. This preserves both parameter roles and the regularity assumptions.',
 'Why can Gaussian heights be used in the crossing calculation, while firing rates cannot simply be assumed Gaussian?',
 'The process definition applies to h and z before rectification. The jointly Gaussian height and derivative have the derivative covariance given in the chapter; applying max(u,0) adds zero mass and changes the distribution. The chapter says this before crossings depend on it.',
 ['Mainali Eq. 2-4','Mainali supplement S1 and S10-S11','author notes Gaussian-process definition and expected crossing count'])

unit('sec:PLACE-KAC-RICE',[123,125,131,139,149,157,173,177,185],
 'Simple threshold crossings of a differentiable stationary map on a finite track.',
 'v is the positive local slope; the joint height/slope density supplies crossing frequency; an initially active endpoint contributes one extra component.',
 'A narrow vertical band has width 2 epsilon/v; slope weighting gives one crossing; average and integrate positive slopes.',
 'Regularity excludes tangent crossings; connected components intersecting the track are retained; the Gaussian law is stationary and differentiable.',
 'The weighted Gaussian integral equals exp(-q squared/2)/(2 pi sigma). Height/slope independence follows from constant variance. On [0,L], component count is upcrossings plus the active-left-end indicator, so the expected correction is Q(q).',
 'The exact crossing density could be mistaken for an exact finite-track field count without the left endpoint term.',
 'p177-185 gives the exact counting identity and warns that removing incomplete fields changes the convention. The caption uses two upcrossings plus one initially active field consistently.',
 'Why does a steep crossing not count more than once, and why does the finite track need a correction?',
 'Its larger slope is canceled by its narrower threshold-band width. A field can enter before x=0, so it intersects the track without a counted upcrossing; its expected indicator is Q(q).',
 ['Mainali supplement S9-S13','Mainali Eq. 8','author notes Kac-Rice formula and expected crossing count'])

unit('sec:PLACE-INFERENCE',[189,191,204,206,223,229,237,246],
 'Field and gap statistics of long tracks or an ensemble of stationary maps.',
 'Occupied fraction Q and inactive fraction Phi share the crossing density; q and sigma are inferred separately.',
 'Divide each fraction by crossing intensity, add the resulting means, then invert the Gaussian tail and solve the scale.',
 'Per-field means are stationary averages, not an expectation-of-ratio identity for a finite sample. Poisson counts and exponential gaps need high levels and sufficiently decaying dependence. Silent cells require conditioning.',
 'Derived both means and their inversion, and recalculated q=1.1, sigma=2.4: Q=.135666, crossing density=.0362127/m, mean field=3.74637m, mean gap=23.86826m, count including endpoint=7.37820. Zero-truncated Poisson mean at lambda=1 is 1.58198.',
 'Exact first moments could be used to claim a Poisson count distribution at all thresholds, or fitted selected-cell means could be treated as unconditional.',
 'p229 supplies the extra rare-event/dependence conditions and a periodic counterexample; p237-246 derives the selection correction. Both distinctions are necessary and correctly stated.',
 'Can a low count distinguish a high threshold from a slowly changing map?',
 'Not alone. The field/gap ratio determines the active fraction and thus q; their total mean then gives sigma. This is a model-based inference under the stated averaging and selection conventions.',
 ['Mainali supplement S14-S15','Mainali Eq. 5','accept-place-stage1-calculations.json'])

unit('ch:PLACE-SIZES',[3,9,11],
 'Field-size histograms in one, two and three dimensions.',
 'A high input peak supplies excess height and radius; dimension changes radius into size; boundary slopes have a separate law.',
 'Move from exact mean counts to a high-peak local shape and a size distribution.',
 'The size law is a high-threshold limit, whereas the crossing slope distribution is exact under the earlier Gaussian assumptions.',
 'The opening preserves the same h/z/q/sigma/a roles and does not claim that exact crossing means alone determine the whole size distribution.',
 'The reader might infer that every field is parabolic at the fitted threshold.',
 'The opening explicitly identifies the high-threshold approximation and the following section lists the limit and derivative requirements. Finite-threshold departures are later quantified.',
 'Which later result is approximate and which has an independent exact argument?',
 'The parabolic geometry and induced size laws are asymptotic. The slope selection law follows directly from stationary Gaussian crossing weights.',
 ['Mainali supplement Methods S4','05-place-fields.md sec:PLACE-KAC-RICE'])

unit('sec:PLACE-RARE-PEAKS',[17,21,22,23,24,28,35,43,45,57,73,79,90,92,96],
 'A typical high excursion component counted once, away from the environment edge.',
 'H is the Hessian; peak height q+epsilon sets curvature and radius; U=q epsilon has a limiting exponential law.',
 'Condition the Hessian on height, approximate the peak by a downward parabola, derive the radius, and convert the height tail to a width tail.',
 'Smooth stationary isotropic unit-variance Gaussian field, suitable nondegeneracy, q tending to infinity, and control beyond the local argument for a full convergence theorem.',
 'Gaussian conditioning gives E(H|z=b)=-b I/sigma squared with bounded conditional variance. The radius is sigma sqrt(2 epsilon/q), full length twice that radius. The peak-count ratio gives exp(-u-u squared/(2q squared)) and its exponential limit; the higher-dimensional polynomial ratio tends to one.',
 'Selecting a maximum could invalidate the height-conditioned Hessian mean, or the finite data exponents could be claimed as the limiting exponent two.',
 'p43 acknowledges maximum-selection curvature weighting and only claims its leading high-peak shape. p96 reports source exponents 1.42/1.46 and 1.75/1.71 as finite-threshold comparisons, not measurements of two. The primary Figure 3 labels confirm the numbers.',
 'Why does peak height lead to a Rayleigh width law?',
 'The typical excess is order 1/q, while curvature is order q. Width is proportional to sqrt(U)/q; U has an exponential limiting law. Peak rate is proportional to excess and hence to width squared at fixed high q.',
 ['Mainali supplement S22-S25, inspected PDF pp.13-14','Mainali Figure 3C-D and Figure 5','author notes upcrossing and excursion shape'])

unit('sec:PLACE-SIZE-LAW',[113,115,117,126,134,136,145,147,156,166,168,176,184,188,190,196,198,199,200,204],
 'Convert one high-peak radius into length, area or volume.',
 'v_d is unit-ball volume, s is d-dimensional size, beta rescales s to exponential U, and w removes physical units.',
 'Use ball geometry, transform the exponential density with its Jacobian, integrate moments and compare with the exact 1D mean.',
 'Spherical local shape and beta=q squared/(2 sigma squared v_d to power 2/d) are leading high-threshold results, not exact finite-level fits.',
 'The Jacobian gives (2 beta/d) s^(2/d-1) exp(-beta s^(2/d)); moments give beta^(-kd/2) Gamma(1+kd/2). Checked table rows, inverse-length-squared units of beta, means .5013/.2513/.1260 at q=5, and mean errors 45.98% at q=1.1 and 3.730% at q=5.',
 'A wrong width factor or inverted mean-size scale in the printed supplement could contaminate the guide formulas.',
 'Inspected the printed S18, S23 and S25 directly: the guide correctly distinguishes division by mean, the missing sqrt(2), and the negative finite-height quadratic exponent. Its constants also agree with the independent boundary-slope derivation and exact 1D high-q mean.',
 'Why do the three density shapes differ even though their transformed variable agrees?',
 'Size is proportional to radius to the power d. The nonlinear map U=beta s^(2/d) changes the density by a dimension-dependent Jacobian; merely removing units with w does not remove that shape difference. The 3D divergence is integrable and creates no atom at zero.',
 ['Mainali Eq. 1','Mainali supplement S18 and S22-S25, PDF pp.12-14 inspected','accept-place-stage1-calculations.json','tbl:PLACE-SIZE-LAWS','SVG text of place-size-geometry and place-size-density-collapse'])

unit('sec:PLACE-SLICES',[208,210,212,216,218,222,224,226,229,233,242],
 'Spatially sampled lines and planes through a higher-dimensional Gaussian map.',
 'The restricted map is a Gaussian process on the slice; a connected slice field need not be an entire original component.',
 'Restrict jointly Gaussian values and covariance to the slice, then threshold and measure components in the slice dimension.',
 'Unit direction and isotropy preserve the local scale; sampling original fields uniformly differs from sampling cuts through space.',
 'Restriction preserves every finite joint Gaussian law; thresholding commutes pointwise with restriction. Larger original fields have a higher hit probability and noncentral cuts change lengths, so no direct reuse of the per-component radius law is justified.',
 'A matching volume histogram might automatically imply matching line and plane histograms.',
 'The text explains hit probability and cut position and cites the spherical comparison in S2. That primary caption matches volume and peak rate by construction but reports slice and EC disagreement, supporting the stated distinction.',
 'What is counted after a line cuts a 3D field?',
 'Connected active intervals on the line. A 3D component may be missed or cut into several intervals, and its sampling probability depends on geometry. The chapter states those differences before using the slice comparison.',
 ['Mainali Figure 2 and Results place fields in two and three dimensions','Mainali supplement Figure S2A-C'])

unit('sec:PLACE-SLOPES',[257,259,267,273,279,283],
 'Slopes sampled at crossings rather than at uniformly selected positions.',
 'v is an input derivative at an upcrossing; a v is the corresponding rate slope; finite differences approximate recorded slopes.',
 'Weight the positive Gaussian derivative density by v, normalize, then use the high-q local parabola for an independent width check.',
 'Exact slope law uses the stationary differentiable Gaussian assumptions; the slope-to-width conversion additionally uses high q. Data slopes use 0.1m spacing.',
 'Normalizing v p(v) gives sigma squared v exp(-sigma squared v squared/2), independent of q. The second parabolic root is 2 sigma squared v/q, leading to beta=q squared/(8 sigma squared).',
 'Rayleigh boundary slopes might be presented as a high-threshold result or as a half-Gaussian derivative sampled at random positions.',
 'The height factor cancels exactly; p267 states q independence and contrasts the spatially uniform derivative sample. The width check is separately labeled high threshold. STAR Methods confirms the 0.1m finite difference.',
 'Why is the positive boundary derivative not half Gaussian?',
 'The sampling event is a crossing. Crossings weight each positive slope by its magnitude, changing the normalized density to Rayleigh.',
 ['Mainali Figure 3E and STAR Methods Boundary slopes','author notes Theorem 2.3','05-place-fields.md crossing integral'])

unit('ch:PLACE-TESTS',[3,7,9],
 'Spatial shape tests and the biological interpretation of the statistical fit.',
 'Connected fields, holes, observed boundaries, fitted summaries and candidate input circuits have distinct roles.',
 'Count topology, inspect measurement/fitting choices, then test what a random-input mechanism could explain.',
 'The map remains fixed; d is dimension and is not the earlier temporal diffusion coefficient D.',
 'The opening correctly frames an additional test: equal field counts or sizes do not fix the holes or the producing circuit.',
 'A good spatial fit might be claimed to recover the producing synapses.',
 'The opening asks how much the agreement tells us and the wiring section concludes that additional circuit measurements are needed. This is the right interpretation of a sufficient statistical construction.',
 'What is the new evidence beyond a size histogram?',
 'The arrangement of components and holes across thresholds, with measured boundaries retained, can reject shapes that share the same sizes. It still does not uniquely identify a circuit.',
 ['Mainali Figures 3 and S2','05c-place-tests.md sec:PLACE-TOPOLOGY and sec:PLACE-WIRING'])

unit('sec:PLACE-TOPOLOGY',[13,17,19,21,23,25,35,37,39,49,59,63,69,79,93,99,114,120,121,123,129,137,139],
 'Excursion sets of a smooth stationary isotropic Gaussian map inside an ordinary closed interval, square or cube.',
 'Betti counts give chi; signed Hessian determinants count interior topology; outward-gradient sign conditions supply boundary terms.',
 'Use Morse signed counts and Gaussian Kac-Rice expectation, evaluate the determinant polynomials, then add face and corner contributions.',
 'Regularity and nondegenerate critical points are required; the topological theorem is cited rather than proved; EC is not component count where holes remain; high-q field counts are a separate approximation.',
 'The conditional determinant averages are lambda^j times b, b squared-1, and b cubed-3b. Gaussian integrals yield 1,q,q squared-1 factors. Face signs and counts yield binomial(d,j)L^j coefficients. The three equations match Mainali 8-10; q=0,r=10 gives -20.05565 for a cube.',
 'Negative EC or omission of boundary factors could make the formulas look like impossible negative field counts.',
 'The chapter defines holes and cavities first, labels signed densities, retains Q(q) and face terms, and only identifies EC with field count at high thresholds. Taylor Eq.1.4/5.1 supports the polynomial structure; the box algebra is shown in the guide.',
 'Why can expected chi be negative while a field count cannot?',
 'Chi subtracts tunnels/holes as well as adding components and cavities. The q=0 cube example has more negative topological contribution on average. Only the sparse high-level regime makes each component approximately one solid blob.',
 ['Mainali Eq.8-10','Mainali supplement S16-S17','https://arxiv.org/pdf/math/0602545 Eq.1.4, Theorem4.1, Section5.1/Eq.5.1','accept-place-stage1-calculations.json'])

unit('sec:PLACE-DATA',[147,151,163,165,169,173,174,175,176,177,179,183,203,229],
 'Reanalysis of recorded firing-rate maps from several conditions.',
 'Mean sizes, gaps, counts or occupied fractions set spatial parameters; additional statistics test the chosen model; gain sets rate comparisons.',
 'Fit using the condition-specific available summaries, then compare histograms, shapes, slices and EC under the processing rules.',
 'In-sample comparisons, simulation error bars and samples of supplied cells do not establish held-out forecasting or all animal-level uncertainty. The 3D sigma unit conversion remains explicitly unverified.',
 'Checked each table row against STAR Methods and figure captions: 200m mean length/gap; 6m length/occupied fraction with 40 cells in Fig.5D; 130m and 48m length/count; virtual mice direct beta fit; 2D mean area/count with selection; 3D mean volume/occupied fraction. The 20-cell slice and EC subsets match Fig.2C and Fig.3H.',
 'A fitted statistic, rate multiplier or cell-selection decision could be hidden as an independent prediction.',
 'The text identifies what was fitted, the separate gain, processing thresholds, subset counts, and the two fitted parameters in the varying-threshold extension. S1-S5 and Methods support those distinctions. It also flags the main/STAR mouse-rat mismatch rather than silently resolving it.',
 'Which comparisons add evidence beyond fitting mean field size?',
 'Length and gap histogram shapes, log-length moments, slices and topology are additional comparisons with the conditions specified. The variable-threshold correlations themselves are fitted; the continued length/gap agreement is the additional check.',
 ['Mainali STAR Methods pp.e2-e3','Mainali Figures1-5 and supplement S1-S5','Mainali Figure4A source parameter crop'])

unit('sec:PLACE-WIRING',[244,246,248,254,258,268,272,280,281,282,284,286,288,297,299,303],
 'Fixed spatial input profiles combine at a receiving cell through random weights.',
 'u_i is the presynaptic profile; W_i is one weight used at every position; weight averaging defines input covariance.',
 'Form the weighted sum; use the multivariate CLT under size/independence conditions; calculate covariance; approximate dense translations by an autocorrelation integral.',
 'Many contributing inputs per position, suitable normalization, independent zero-mean weights, and no dominating term are needed. Uniform coverage gives stationarity away from edges. Signed effective weights do not identify biological synapse signs.',
 'Independence cancels cross terms and gives v_W sum u_i(x)u_i(y). Dense translated profiles yield v_W rho times their autocorrelation. Completing the square for Gaussian profiles gives R0 squared sqrt(pi)b exp(-Delta squared/(4b squared)), hence covariance standard deviation sqrt(2)b.',
 'Anatomical input count alone or Gaussian output statistics could be said to prove a random circuit.',
 'The text requires active contributors and CLT conditions, separates amplitude from width changes, and calls this one possible mechanism. It explicitly allows correlations, structured input, plasticity or recurrent processing and asks for further circuit measurements.',
 'Which assumptions create Gaussianity and which create spatial covariance?',
 'Random weighted summation supplies the finite joint Gaussian limit under its conditions. The input profiles and their overlap determine covariance; dense uniform placement gives translation invariance, and smooth profiles supply the regularity assumed for the map.',
 ['Mainali supplement S2-S8','Mainali Discussion pp.1117-1118','author notes Gaussian input fields'])

unit('ch:SYNTHESIS',[3,5],
 'Comparison of a spatial map model, a persistent-memory model and a measured movement model.',
 'Maps assign rates to coordinates; dynamics change a represented coordinate; downstream systems turn signals into movement.',
 'Separate the three objects, derive a local shared-position covariance, then compare evidence and propose a joint experiment.',
 'This is a guide connection, not a claim that the studies tested one joint model.',
 'The opening correctly separates explanatory targets and their evidence, avoiding an identification of static field disorder with temporal noise.',
 'Shared vocabulary such as position or noise might make the three papers appear to test the same object.',
 'The next unit identifies each coordinate and its role and the local calculation is explicitly a new guide construction. The opening is supported by those concrete distinctions.',
 'What would be missing from a model that matches field shapes but has no dynamics?',
 'It would not specify how a represented position changes or how a downstream measurement filters it. The synthesis makes those missing pieces its subject.',
 ['Burak/Fiete2012 main Eqs.1-5','Ben-Shushan2022 main Figures2-5','Mainali2025 Eq.2-3'])

unit('sec:SYNTHESIS-QUESTIONS',[13,15,16,17,19,21,29],
 'Three models with distinct position variables.',
 'theta indexes the network attractor; the eye model separates internal command and actual angle; x indexes physical locations in place-cell maps.',
 'Memory-coordinate noise can drive a command and a filtered movement; a place-field map needs an added trajectory before it gives time-dependent expected rates.',
 'The eye result supports a shared upstream source and model sufficiency, not measured Fisher information or equality in the 2012 bound.',
 'Checked the comparison table against the original models. Its random objects and observables differ appropriately: coordinate increments/readout, filtered movement covariance/MSD, and spatial map geometry.',
 'The 2022 behavioral fit could be called an experimental test of the full 2012 information-diffusion bound.',
 'p29 explicitly denies that inference and identifies the unmeasured information quantity. This is supported by the studies actual methods and the earlier information chapter.',
 'What extra specification turns a fixed spatial tuning curve into a dynamical prediction?',
 'A time path for the represented coordinate. Without x(t), f_i(x) supplies values across space, not a time course or a diffusion coefficient.',
 ['Burak/Fiete2012 Eq.3-4','Ben-Shushan2022 central source and circuit model','Mainali2025 Eq.2-3','03-memory-information.md sec:MEMORY-FI'])

unit('sec:SYNTHESIS-JOINT-CALCULATION',[33,39,43,50,58],
 'A local one-dimensional represented displacement applied to fixed rate functions.',
 'x(t) changes, f_i is fixed, R_i(t)=f_i(x(t)) is expected rate, and actual spikes have further variability.',
 'Linearize each rate at x0, multiply the centered leading changes, and average the common displacement.',
 'Conditional on x0, displacement has zero mean and variance 2Dt and is small enough for local linearization; extra private/shared fluctuations and threshold nonsmoothness are excluded.',
 'Taylor expansion gives delta R_i approximately f_i prime delta x and covariance approximately 2Dt f_i prime f_j prime. Units are Hz squared, and signs follow the product of slopes.',
 'The formula could be mistaken for total recurrent spike-count covariance or used across a firing threshold.',
 'p39 and p58 explicitly distinguish expected rates from spike counts, name additional variability, and restrict the linear approximation near thresholds or large moves.',
 'Why do two cells become correlated even though their tuning functions are fixed?',
 'They share the same random displacement. Each converts it to a rate change through its own slope, so the covariance is the displacement variance multiplied by those slopes.',
 ['01-foundations.md covariance teaching','01b-persistence.md diffusion variance','displayed Taylor and covariance algebra'])

unit('sec:SYNTHESIS-COVARIANCE-EXAMPLE',[68,81,83,91,95],
 'Two locally linear rate curves with opposite slopes under one common position error.',
 'Slopes are +2 and -1 Hz/m, D=.01 m squared/s, duration=.5s, and the 10Hz baseline displays positive rates.',
 'Compute displacement variance .01m squared, multiply by squared slopes and their product, then normalize covariance to a correlation.',
 'Only the common position source contributes to the stated perfect correlation; private independent variance reduces its magnitude.',
 'Recalculated variances .04 and .01 Hz squared, covariance -.02 Hz squared and correlation -1. A +.1m displacement gives +.2 and -.1Hz. The SVG text and caption use the same values.',
 'Negative covariance could be interpreted as an inhibitory connection, or -1 could be claimed with other noise sources present.',
 'p81 limits the result to the single common source and directly separates covariance sign from connection sign. p91 explains the line in rate-change coordinates.',
 'What produces the negative sign, and what would private noise change?',
 'Opposite tuning slopes map the same position change into opposite rate changes. Independent private noise adds variances without adding this covariance, reducing the absolute correlation.',
 ['accept-place-stage1-calculations.json','fig:SYNTHESIS-SHARED-POSITION caption, alt and SVG text'])

unit('sec:SYNTHESIS-EVIDENCE',[103,105,109,114],
 'Assess the evidence for each model using its actual observable.',
 'Fitted place summaries set parameters; eye calibration and decomposition identify shared drive; the memory inequality constrains diffusion and information.',
 'Separate fit from additional comparison, source location from source identity, and a mathematical inequality from empirical scaling.',
 'Finite-threshold simulations, gain fitting, calibration, correlation assumptions, two animals and horizontal movement remain visible.',
 'The place paragraph matches the Methods fit choices; the eye paragraph matches the stationary-filter versus accumulating-command distinction; the memory paragraph requires the correct information rate and time constants, not only 1/N scaling.',
 'The eye paragraph might exclude every peripheral noise process, including slow correlated ones.',
 'It states that changing amplitude alone cannot reproduce the accumulating signal. The earlier timing chapter explicitly distinguishes a slow correlated peripheral hypothesis from the white-noise alternative rejected by the comparison. Read together, the scope is adequate.',
 'Why is 1/N scaling not enough to test the information-diffusion inequality?',
 'The inequality also specifies the information quantity, time constants and noise/dynamics assumptions. Many mechanisms can have the same population-size scaling without matching that quantitative bound.',
 ['Mainali STAR Methods','Ben-Shushan2022 Figure3 and central source discussion','04b-eye-timing.md final comparison and limits','Burak/Fiete2012 Eq.4'])

unit('sec:SYNTHESIS-RELATED',[119,121,123,125,128,131],
 'Related work changes circuit, storage or sensory-use assumptions.',
 'Integrator perturbations constrain circuit structure; coding and plasticity alter storage; large-environment recordings constrain maps; perception studies examine benefits of movement.',
 'Match each cited study to the distinct question it answers, without transferring an estimate across species or protocols.',
 'Grid accuracy is model-specific; the 2025 place article reanalyzes earlier data; CA3/CA1 comparisons and perceptual benefits do not uniquely identify the producing mechanism.',
 'Checked Seung and Aksay abstracts, the 2009 grid study, Koyluoglu and Seeholzer primary reports, Maimon main results, Druckmann/Bittner primary abstracts and Nghiem Results. Each supports the bounded claim attached to it.',
 'A related study may be used as direct support for a macaque variance estimate or a unique random-wiring account.',
 'The paragraph explicitly withholds those transfers. Maimon reports predominantly single CA3 fields and multiple CA1 fields with similar sizes; Druckmann reports nonuniform clustered connectivity; Bittner links plateau events to plasticity and field formation; Nghiem addresses visual benefit rather than generator identity.',
 'Do structured connections and plasticity contradict a useful Gaussian description of field statistics?',
 'No. The statistical model does not uniquely specify its biological construction. These studies identify structure and learning that may coexist with a good aggregate spatial description, while motivating separate circuit measurements.',
 ['research/ben-shushan-2022-related-seung-1996.txt abstract','research/ben-shushan-2022-related-aksay-2007.txt abstract','https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1000291','https://elifesciences.org/articles/22225','https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1006928','research/related-2026-ca3-ca1-body.txt main results','https://pubmed.ncbi.nlm.nih.gov/24412418/','https://pubmed.ncbi.nlm.nih.gov/28883072/','research/related-2025-active-sensation-body.txt Results'])

unit('sec:SYNTHESIS-NEXT',[135,137,138,139,140,142],
 'A proposed future experiment on maps and fluctuations in the same population.',
 'Tuning maps predict rate-change directions; population changes estimate shared fluctuations; observation filters matter when behavior is compared.',
 'Estimate maps and uncertainty, measure fluctuations with little external correction, fit an appropriate local diffusion range, and include downstream filters if needed.',
 'These are proposed measurements, not a reported replication or a guarantee that agreement identifies one circuit.',
 'The proposal follows directly from the local covariance calculation and from each paper incomplete coverage of the other objects. Static maps cannot determine D without dynamics, and a diffusion coefficient does not determine a field distribution.',
 'Agreement with both statistics could be claimed to uniquely verify a complete circuit.',
 'p142 says it constrains the model more and calls for further tests after a mismatch. It also explicitly labels the work proposed, so no experiment or replication is fabricated.',
 'What two kinds of data are required for the proposed joint test?',
 'Spatial tuning estimates and fluctuations from the same population, with enough information about correction signals and measurement filters to interpret their relationship.',
 ['06-synthesis.md local covariance calculation','main paper models and their measurement scope'])

# These check groups encode judgments made during this call. They are serialized
# onto the selected claim rows; the script does not decide scientific truth.
CHECKS={}
def checks(short, entries): CHECKS[short]=entries
checks('ch:GLOSSARY',[
 ('1','Manifold coordinates distinguish represented dimensions from neuron state dimensions; matches persistence chapter.'),
 ('2','Causality is dependence on present/past inputs, matching the earlier filter model.'),
 ('3-5','Gamma, coth and artanh definitions and their displayed real domains agree with the mathematical formulas.'),
 ('6','Finite linear combinations define joint Gaussianity, consistent with the GP chapter.'),
 ('7-9','Left/right null-vector equations and the normalized persistent projection match the earlier linearized dynamics.'),
 ('10','Centered third moment divided by variance to power 3/2 is the displayed skew convention.'),
 ('11','The sentence distinguishes strict stationarity from a weaker covariance-only convention.'),
 ('12','Weak aggregate spike perturbations are the approximation used by the 2012 model.'),
 ('13','Weibull survival with positive scale and shape differentiates to the size-law density.')])
checks('ch:REFERENCES',[
 ('1-3','DOI and title identify the corresponding local main-paper title page; a link label alone is not a scientific proposition.'),
 ('4-5','Maimon title/DOI and publication details match local primary metadata, including Nature 655(8125),1242-1251.'),
 ('6','Taylor DOI is printed on the author preprint; the direct DOI resolver failed, so live link success is not claimed.'),
 ('7-8','Seung and Aksay identifiers match the local primary article text.'),
 ('9-11','Burak/Fiete 2009, Koyluoglu and Seeholzer identifiers match the live primary publisher records.'),
 ('12-14','Eliav, Harland and Yartsev identifiers match the Mainali primary references and original publication details.'),
 ('15','Druckmann DOI/venue/authors match PubMed primary article record 24412418.'),
 ('16','Bittner DOI/venue/authors match PubMed primary article record 28883072.'),
 ('17','Nghiem DOI and title match the local primary article metadata and Results.')])
checks('ch:PLACE-FIELDS',[
 ('1','Mainali Methods S1 interprets h as mean synaptic input; rate-map recordings do not directly measure it.'),
 ('2','Mainali Figures2-3 and S2 add slice/shape/topology comparisons beyond fitted means; strongest is an evidential judgment with those concrete tests.'),
 ('3','Eq.2 defines a spatial function draw; x changes during movement while that draw is fixed.')])
checks('sec:PLACE-GP',[
 ('1','Gaussian values alone do not imply differentiable paths; p52 and the exponential-covariance counterexample supply the needed distinction.'),
 ('2-3','Finite multivariate Gaussian laws are determined by mean/covariance, and zero cross-covariance makes Gaussian subvectors independent.'),
 ('4','Threshold-linear rectification has a zero-mass component and is generally not Gaussian.'),
 ('5','For constant-mean Gaussian spatial fields, rotation-invariant covariance gives the stated isotropic law.'),
 ('6-7','Smooth sample paths and derivative nondegeneracy are explicit assumptions, not inferred from Gaussian marginals.'),
 ('8-10','Zero mean is absorbed into threshold; z has unit variance and a supplies Hz. Gain rescaling makes this equivalent to paper Eq.3.'),
 ('11','Visible disclosure title identifies Figure1; tags are controls rather than a scientific claim.'),
 ('12','Caption content matches primary Figure1C-F; exact excerpt pixel fidelity remains deferred.'),
 ('13-15','Directly differentiated stationary covariance: d_x d_y C(y-x)=-C second derivative. Gaussian kernel has Var(z prime)=1/sigma squared; other kernels can match this derivative only.'),
 ('16-17','The chosen q=.8 and a=6 define a teaching map, and the formula, SVG text, caption and alt agree on those values; full pixel acceptance is deferred.'),
 ('18','The source pointer names Mainali Eq.2-3 on PDF page13; checked that page text.')])
checks('sec:PLACE-KAC-RICE',[
 ('1-5','A simple crossing gives band width 2epsilon/v, so the weighted integral contributes one. Positive slopes select upcrossings; probability above q cannot replace the density at q.'),
 ('6-7','Two upcrossings plus one left-edge active component gives three intersecting fields; the counting convention is explicitly stated. Caption/alt/SVG labels agree, pixels deferred.'),
 ('8-9','Stationary unit variance implies E(zz prime)=0; joint Gaussianity supplies independence and derivative variance 1/sigma squared.'),
 ('10-11','The substitution u=sigma squared v squared/2 evaluates the positive-slope Gaussian integral to 1/(sigma sqrt(2pi)).'),
 ('12-14','The active-left-end probability is the standard-normal upper tail Q; changing boundary-field selection changes the correction. Mainali Eq.8 is the same 1D EC expression.')])
checks('sec:PLACE-INFERENCE',[
 ('1-4','Occupied/inactive fractions divided by crossing intensity give the per-component means; their ratio yields Phi inverse and their sum yields sigma. The finite-sample ratio caveat is explicit.'),
 ('5-7','Recomputed from q=1.1,sigma=2.4: Q=.13566606,nu=.0362126851,means=3.74636845/23.86826429m,E N=7.37820309; inversion returns q=1.1.'),
 ('8-9','Stationarity alone permits persistent periodic dependence; rare excursions need decay for a Poisson limit, while the two sides of one small excursion stay linked.'),
 ('10-14','Conditioning a Poisson law on positive count divides by 1-exp(-lambda); at lambda=1 exclusion=.36787944 and mean=1.58197671. Paper Eq.5 uses this correction.')])
checks('ch:PLACE-SIZES',[
 ('1','The motivating question concerns a full distribution beyond a mean; the next section explicitly assumes high q.'),
 ('2','The firing rule and positive-part definition are identical to the preceding chapter.')])
checks('sec:PLACE-RARE-PEAKS',[
 ('1-3','The target is a typical high component, counted once away from edges, with a local reconstruction rather than a claimed general theorem proof.'),
 ('4-5','Gaussian Hessian mean scales with peak height, conditional variance stays bounded; maximum-selection weighting is acknowledged before using the leading parabola.'),
 ('6-10','High maxima/upcrossing asymptotics give the exponential peak-count ratio; substituting epsilon=u/q yields exp(-u-u squared/(2q squared)); higher-dimensional q^(d-1) ratio tends to one.'),
 ('11-12','Full 1D width is twice radius; cube-root volume is the relevant 3D linear size for the rate-versus-linear-size exponent.'),
 ('13-17','Directly inspected primary Figure3C-D labels 1.42/1.46 and 1.75/1.71; Figure5 caption and Figure4C support finite-threshold progression rather than a measured limit two.'),
 ('18','Disclosure summary identifies primary Figure5; markup is not a scientific statement.'),
 ('19','Caption matches primary Figure5 high-threshold shape/exponent trend; excerpt pixel fidelity deferred.')])
checks('sec:PLACE-SIZE-LAW',[
 ('1-4','Unit-ball volume and the positive-argument Gamma integral give v1=2,v2=pi,v3=4pi/3 and the factorial extension.'),
 ('5-7','Substituting the high-peak radius into v_d r^d gives beta=q squared/(2sigma squared v_d^(2/d)); round regions are explicitly limiting constructions.'),
 ('8-10','Differentiate U=beta s^(2/d) to obtain the density and recognize the finite-q fitted-scale caveat; agrees with main Eq.1.'),
 ('11-14','Integrating after u=beta s^(2/d) gives Gamma(1+kd/2) beta^(-kd/2), normalization and the inverse-mean scale; printed S18 differs as stated.'),
 ('15-18','Since size has length^d units, beta has length^-2 and w=beta^(d/2)s is dimensionless; U=w^(2/d) removes the remaining shape difference.'),
 ('19-20','Caption distinguishes limiting densities from finite-threshold data; the survival is exp(-u), and the source pointer locates main Eq.1. Pixel fidelity deferred.'),
 ('21','The table caption names a table whose three formulas were read and checked.'),
 ('22-24','Substitute d=1,2,3 in the density: Rayleigh, exponential and shape-2/3 Weibull; the s^(-1/3) singularity is integrable.'),
 ('25-26','With shape k=2/d and scale b=beta^(-d/2), the Weibull survival matches; near-zero cumulative probability tends to zero.'),
 ('27-30','Recomputed q=5 means .50132565,.25132741,.12599688; q=1.1 asymptotic/exact means 5.46900714/3.74636845, error45.98156%; q=5 error3.73008%.'),
 ('31','Printed algebra errors were visually checked on supplement PDF pp13-15, but no simulation-code inference follows; the guide preserves that limit.')])
checks('sec:PLACE-SLICES',[
 ('1-3','Finite sampled slice values are original jointly Gaussian values; restricting covariance and thresholding commute pointwise.'),
 ('4','A field sampled once and a spatially sampled line have different hit and cut-position weights, as the paragraph explains.'),
 ('5','Primary Figure2 caption identifies C as line lengths,D as original areas,E as counts,H-I-J as line/plane/volume comparisons.'),
 ('6','Disclosure title identifies primary Figure2; markup is not a scientific proposition.'),
 ('7','The caption follows restriction to the measured dimension under the high-threshold size-law context; primary Figure2 shows those comparisons. Pixels deferred.'),
 ('8-9','Read primary S2 caption: null fields have matching volumes and peak rates, but slice distributions and EC disagree.'),
 ('10','Disclosure title identifies S2; markup is not a scientific proposition.'),
 ('11','Caption states the conclusion supported by S2A-C; original-image fidelity remains deferred.')])
checks('sec:PLACE-SLOPES',[
 ('1-3','Weight positive derivative density by v and divide by its first positive moment; the height factor cancels, producing Rayleigh rather than half Gaussian at crossings.'),
 ('4-5','The positive second root of vx-q x squared/(2sigma squared) is 2sigma squared v/q; changing variables gives beta=q squared/(8sigma squared).'),
 ('6-7','Primary Figure3A defines measurements, and STAR Boundary slopes specifies adjacent samples 0.1m apart.'),
 ('8','Disclosure title identifies Figure3; markup is not a scientific statement.'),
 ('9','Primary Figure3 caption and panels support shape/slope/EC comparisons beyond mean size; pixels deferred.')])
checks('sec:PLACE-TOPOLOGY',[
 ('1-4','Betti alternating sums give three disks3,ring0,ball1,solid torus0,hollow sphere2; definitions match the topology being counted.'),
 ('5','Caption arithmetic matches components minus holes (-1,0,4,3) and nested-threshold reasoning; SVG text agrees. No pixel acceptance claimed.'),
 ('6','Read Taylor Eq.1.4, Theorem4.1 and Eq.5.1, which give the stated expected-EC form and Gaussian density polynomials.'),
 ('7-11','Gaussian gradient density times the signed Hessian determinant integral has units length^-j and gives the displayed j=1,2,3 densities.'),
 ('12-17','Expanded determinants with conditional diagonal covariance kappa-lambda squared and off-diagonal variance kappa; pair terms cancel kappa. Differentiation verifies the three Gaussian integrals.'),
 ('18-21','Ordinary box faces supply 2^(-(d-j)) sign probability times 2^(d-j) binomial(d,j) faces; corners give Q. The final equations agree with Mainali8-10 and explicitly exclude a periodic box.'),
 ('22','Direct arithmetic for q=0,r=10 gives .5+30/(2pi)-1000/(2pi)^2=-20.05564762.'),
 ('23-25','Only in the high-level single-blob regime can EC approximate count; the leading volume term gives q^(d-1), consistent with supplement S16-S17 and the size mean.'),
 ('26-28','The instruction points to full EC curves; rate threshold t adds t/a to q, and only observed nonnegative extra cutoffs test the data. Gain normalization is explicitly fitted.')])
checks('sec:PLACE-DATA',[
 ('1-3','Read STAR Methods and figure captions: data are rate maps and final sample counts are not explicit for every reanalysis; original-study totals cannot be silently reused.'),
 ('4','Table caption identifies fitted and additional comparisons; each row was checked against Methods.'),
 ('5-10','Read Methods parameter inference for1D/2D/3D, Fig5D40cells, Fig1F four mice, Fig2C20cells and Fig3H20cells; all table fitting/measurement roles match.'),
 ('11-13','Main Figure1F identifies mice; Methods says rats in that sentence. Fig1C/D distinguish limiting analytical curves from finite-threshold simulations.'),
 ('14-15','Centered Gaussian log-size has zero skew and excess kurtosis; finite-sample values fluctuate, consistent with the simulated-distribution comparison.'),
 ('16','The error bars are from 10^4 cell-matched simulations in Fields in1D; this does not quantify all animal or measurement uncertainty.'),
 ('17-19','Data processing, Fields in3D, peak-count and rate-width Methods give .5Hz denoising, median filtering, outlier removal, boundary exclusion and 1Hz cutoff; these change analyzed geometry.'),
 ('20-23','Supplement S1 specifies15cm cutoff, S5 varies denoising and rate-width threshold, S2 gives curvature computation; mean/product definitions of principal curvature are correct.'),
 ('24','Disclosure title identifies S1; markup is not a scientific proposition.'),
 ('25','Primary S1 caption states the same15cm cutoff for data and model; pixels deferred.'),
 ('26','Disclosure title identifies S5; markup is not a scientific proposition.'),
 ('27','Primary S5 caption supports changing log moments and stabilized rate-width exponent above1Hz; pixels deferred.'),
 ('28-31','Figure4 parameter table and S3 caption support trends and exponents .86/.82. The printed3D sigma4.0 is visible; guide does not assert an unverified metre conversion.'),
 ('32','Disclosure title identifies Figure4; markup is not a scientific proposition.'),
 ('33','Figure4 and accompanying text support increasing fitted scale and changing threshold/shape; pixels deferred.'),
 ('34','Disclosure title identifies S3; markup is not a scientific proposition.'),
 ('35','S3B exponents .86 and .82 are below one, so count/environment size decreases in those comparisons; pixels deferred.'),
 ('36-37','S4 caption uses positive-conditioned skew-normal thresholds fixed for each cell across two map draws and fits two remaining distribution parameters to the correlations.'),
 ('38','Disclosure title identifies S4; markup is not a scientific proposition.'),
 ('39','S4A-F supports the caption mechanism: shared cell thresholds correlate statistics across independent directional maps; pixels deferred.')])
checks('sec:PLACE-WIRING',[
 ('1-3','Independent zero-mean fixed weights give a sum of independent vectors at finite positions; suitable normalization/no-dominance conditions and active input count are explicitly required for CLT.'),
 ('4-5','Completed square: s squared+(s+Delta) squared=2(s+Delta/2) squared+Delta squared/2; Gaussian integration gives R0 squared sqrt(pi)b exp(-Delta squared/(4b squared)).'),
 ('6-7','Primary Discussion confines measured environments to familiar/uniform conditions and discusses plasticity; guide treats the random sum as sufficient, not uniquely identified.')])
checks('sec:SYNTHESIS-QUESTIONS',[
 ('1','The 2022 model explicitly connects a noisy integrator through motor/plant filtering to eye displacement; source-location evidence is not a unique generator identification.'),
 ('2','Table title identifies the three comparison rows.'),
 ('3','2012 Eq1-5 and SI define coordinate diffusion, spike noise, recurrent dynamics and readout error.'),
 ('4','2022 model includes command/motor fluctuations and measurement correction; principal tests use displacement covariance and MSD.'),
 ('5','Mainali Eq2-3 and Fig1-5 define a random spatial function with covariance/threshold and geometrical observables.'),
 ('6','A static tuning map lacks a time evolution; the next section explicitly supplies x(t).')])
checks('sec:SYNTHESIS-JOINT-CALCULATION',[
 ('1-3','Taylor expansion under a small zero-mean displacement gives the leading covariance 2Dt times the product of local slopes.'),
 ('4-5','The prose restricts this to conditional expected-rate changes and explicitly excludes arbitrary spike covariance and threshold/large-move linearization.')])
checks('sec:SYNTHESIS-COVARIANCE-EXAMPLE',[
 ('1','This is the wrapper for a folded calculation, not a scientific proposition.'),
 ('2-6','The stipulated slopes and diffusion imply position variance .01, rate variances .04/.01, and covariance-.02 in the displayed units.'),
 ('7-8','With only the single shared displacement, covariance divided by sqrt(.04*.01)=-1; +.1m gives +.2/-.1Hz. The figure text and caption match; pixels deferred.'),
 ('9','Opposite slopes explain the sign; testing their alignment needs rate-change measurements, which field shape alone does not supply.')])
checks('sec:SYNTHESIS-EVIDENCE',[
 ('1','Mainali rate-width intercept and EC mean-max-rate matching use an extra gain, explicitly identified earlier.'),
 ('2-4','2022 Methods decomposes shared and independent terms; fixed stationary filtered-noise amplitude cannot supply unbounded accumulated displacement. Earlier timing limits distinguish slow correlated alternatives and empirical scope.'),
 ('5','The2012 bound also contains tau and instantaneous information; common1/N behavior alone cannot identify those quantities or equality.')])
checks('sec:SYNTHESIS-RELATED',[
 ('1','Burak/Fiete2009 abstract and Results attach accuracy to simulated networks, noise and parameters, as the guide says.'),
 ('2','Koyluoglu changes encoding/storage assumptions; Seeholzer adds synaptic facilitation/depression and derives modified diffusion/drift. Neither is described as refuting the original assumptions.'),
 ('3','Maimon primary Results distinguish single-field CA3 and multifield CA1 with similar sizes; the guide conclusion is explicitly a separation of constraints.'),
 ('4','Druckmann mapping and Bittner perturbation/plasticity findings support the availability of circuit/learning measurements beyond a map histogram.'),
 ('5','Nghiem Results link human performance and a retinal model to movement amplitude; they do not uniquely identify the motor noise source.')])
checks('sec:SYNTHESIS-NEXT',[
 ('1','This is a qualified proposed fitting instruction, with local and measurement limitations stated.'),
 ('2-3','A spatial map law has no time coefficient, while D alone supplies no spatial covariance/threshold or field-size law; joint agreement adds constraints without proving a unique circuit.')])

NOT_CLAIMS={
 'ch:REFERENCES':set(range(1,18))-{4},
 'sec:PLACE-GP':{11,18},'sec:PLACE-RARE-PEAKS':{18},
 'sec:PLACE-SIZE-LAW':{20,21},'sec:PLACE-SLICES':{5,6,10},
 'sec:PLACE-SLOPES':{8},'sec:PLACE-DATA':{4,24,26,32,34,38},
 'sec:SYNTHESIS-QUESTIONS':{2},'sec:SYNTHESIS-COVARIANCE-EXAMPLE':{1}}
CONDITIONED={'sec:PLACE-GP','sec:PLACE-KAC-RICE','sec:PLACE-INFERENCE','sec:PLACE-RARE-PEAKS','sec:PLACE-SIZE-LAW','sec:PLACE-SLICES','sec:PLACE-SLOPES','sec:PLACE-TOPOLOGY','sec:PLACE-WIRING','sec:SYNTHESIS-JOINT-CALCULATION','sec:SYNTHESIS-COVARIANCE-EXAMPLE','sec:SYNTHESIS-EVIDENCE','sec:SYNTHESIS-NEXT'}

def expand(spec):
    for part in spec.split(','):
        nums=part.split('-')
        yield from range(int(nums[0]),int(nums[-1])+1)

assessments=[]; claims=[]; para_inventory=[]
for uid,u in P['units'].items():
    short=uid.split('::')[1]
    d=DATA[short]
    existing={x['id'] for x in u['paragraphs']}
    refs=[uid+'::p'+str(n) for n in d['refs'] if 'p'+str(n) in existing]
    assert refs,(uid,d['refs'])
    fields={
      'System setup and component relationships':{
        'setting':d['setting'],'roles':d['roles'],'flow':d['flow'],
        'assumptions':d['assumptions'],'verdict':'retain','source_refs':refs},
      'Mechanism, calculation, or state change':{'evidence':d['mechanism'],'source_refs':refs,'sources':d['sources'],'verdict':'retain'},
      'Assumptions, limits, trade-offs, or failure modes':{'evidence':d['assumptions'],'source_refs':refs,'verdict':'retain'},
      'Expert objection':{'objection':d['objection'],'kind':'correctness','target':refs,'disposition':'not sustained on complete reading','reason':d['reason']}}
    assessments.append({'unit_id':uid,'status':'pass','unresolved':[],
       'questions':[{'question':d['question'],'answer':d['answer'],'source_refs':refs},
                    {'question':'Does the strongest reasonable complete reading survive the correctness objection?',
                     'answer':d['reason'],'source_refs':refs}],
       'fields':fields,'source_support':d['sources']})
    manual={}
    for nums,check in CHECKS.get(short,[]):
        for n in expand(nums):
            assert n not in manual,(short,n)
            manual[n]=check
    for cid,line,quote,*rest in u['claims']:
        n=int(cid[1:]); assert n in manual,(short,cid)
        verdict='not a claim' if n in NOT_CLAIMS.get(short,set()) else ('condition stated' if short in CONDITIONED else 'true as written')
        near=[x for x in u['paragraphs'] if x['line']<=line]
        pref=uid+'::'+max(near,key=lambda x:x['line'])['id'] if near else uid
        claims.append({'unit_id':uid,'claim_id':cid,'line':line,'verdict':verdict,'check':manual[n],
                       'source_refs':[uid,pref] if pref!=uid else [uid],
                       'evidence_sources':d['sources']})
    assert set(manual)=={int(c[0][1:]) for c in u['claims']},(short,'extra/missing check')
    for x in u['paragraphs']:
        cleaned=re.sub(r'<!--[\s\S]*?-->','',x['text'])
        visible=re.sub(r'<[^>]+>','',cleaned).strip()
        kind='hidden control only' if not cleaned.strip() else ('structural markup only' if not visible else 'reader text')
        para_inventory.append({'id':uid+'::'+x['id'],'source_hash':x['source_hash'],'classification':kind,
            'stage1_read':'read as part of connected source' if kind=='reader text' else 'inspected and excluded from prose truth claims',
            'flow_decision':'awaiting separately requested Stage3'})

report={
 'run_id':'final-place-truth-20261029-01','run_id_type':'local request ID',
 'reviewer_id':'/root/accept_place','assigned_model':'GPT-6 Astra','assigned_reasoning':'high',
 'authorship':'Reviewer did not author any assessed guide text.',
 'stage':'truth_reasoning','context':'fresh',
 'started_at':'2026-10-29T13:19:47.4518693+02:00','completed_at':None,
 'input_hash':P['input_hash'],'review_contract_hash':P['review_contract_hash'],
 'scope':'Three place chapters, synthesis, glossary, references, their sidecar text, captions, alt text, fold titles and available SVG labels. Needed earlier teaching and primary sources were read.',
 'initial_read':'Read current manuscript and sidecars before prior verdicts or proposed repair reasons. No prior verdict reports were read. Initial checks targeted possible confusion between static maps and time noise, exact and asymptotic results, gain fitting and independent tests, and Gaussian fit versus a unique mechanism. These concerns were tested against the complete passages and sources.',
 'status':'Stage1 text correctness pass within declared scope; not three-stage acceptance or release approval',
 'findings':[],
 'retained_with_reasons':[
  'Exact crossing means and q-independent slope law remain distinct from the high-q size law.',
  'The finite-track endpoint correction and silent-cell selection correction retain different purposes.',
  'The supplement correction box is supported by direct primary PDF inspection and independent algebra.',
  'The EC calculation retains box boundaries and permits signed topology without treating negative chi as a negative component count.',
  'The wiring argument includes active-input/CLT conditions and does not uniquely identify biological synapses.',
  'The synthesis adds an explicitly hypothetical local rate-covariance construction and does not turn it into a joint experimental result.'
 ],
 'assessments':assessments,'claims':claims,'paragraph_inventory':para_inventory,
 'counts':{'units':len(assessments),'paragraphs':len(para_inventory),'selected_claims':len(claims)},
 'deferred':[
  'Stage2 necessity, terminology, definition emphasis and contextual wording.',
  'Stage3 every-paragraph purpose/connections and final connected reader-understanding assessment.',
  'Guide figure pixel acceptance, layout, and exact artwork-excerpt fidelity, as instructed. Textual labels/captions were checked; no approval of rendered artwork is claimed.',
  'Full publication link/footnote rendering audit and release-format checks. Some DOI resolver attempts failed while alternate primary sources supplied identity and content.'
 ],
 'code_listings':'No reader code listings in this scope. The local calculation script checks displayed numerical examples rather than reader code.',
 'source_verification':{
  'packet_current_source_match':'All six full Markdown source strings exactly matched their packet review_asset_definitions during this call.',
  'source_hash_file':'accept-place-stage1-source-hashes.json',
  'calculation_file':'accept-place-stage1-calculations.json',
  'fresh_extractions':['accept-place-main-source.txt','accept-place-supplement-source.txt'],
  'printed_equation_pages':['accept-place-supp-13.png','accept-place-supp-14.png','accept-place-supp-15.png'],
  'source_figures_inspected':['research/mainali-2025-figure3.png','research/mainali-2025-parameters-crop.png'],
  'svg_labels_read':['place-crossings','place-gp-to-firing','place-size-geometry','place-size-density-collapse','place-topology','synthesis-shared-position']},
 'timing':{'preparation_started_at':'2026-10-29T13:05:39.8301214+02:00','stage_started_at':'2026-10-29T13:19:47.4518693+02:00',
   'measured_checkpoints':['2026-10-29T13:21:43.5424428+02:00','2026-10-29T13:23:38.4751132+02:00','2026-10-29T13:25:22.7758431+02:00'],
   'mistyped_commentary_label':'13:22:42','correction':'The next measured Get-Date was 13:21:43.5424428+02:00. The earlier label was a reporting error, not evidence of a system-clock change. It was disclosed to the coordinator and in commentary.',
   'awake_execution':'unverified','token_stats':'unavailable'},
 'stage2_3_fields':'Awaiting separate calls; no paragraph-flow judgments or later-stage acceptance fabricated.'}
assert report['counts']=={'units':22,'paragraphs':429,'selected_claims':258},report['counts']
(OUT/'final-place-stage1.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
md=['# Place group: Stage 1 truth and reasoning','',
 'Local request: `final-place-truth-20261029-01`. Reviewer: `/root/accept_place`, assigned GPT-6 Astra, high reasoning. Fresh first manuscript review; no authorship of assessed text.',
 '',f"Input: `{P['input_hash']}`.",f"Contract: `{P['review_contract_hash']}`.",'',
 'Stage 1 found no required scientific correction in the frozen text. This is not complete teaching acceptance or release approval. Stage 2 and Stage 3 remain pending, and figure pixel acceptance remains deferred.',
 '', 'All 22 units, 429 extracted paragraph records and 258 selected claim rows are represented in the JSON. Hidden Vale comments and structural wrappers are distinguished from reader text. Equations, typed tables, source notes, captions, alt text and available SVG labels were read alongside the prose.',
 '', '## Source and numerical checks','',
 'The source strings of all six Markdown files matched the neutral packet. The Mainali paper and supplement were read directly; supplement PDF pages 13-15 were rendered to verify S18, S23 and S25. Those printed expressions support the guide correction box. The recalculated means, crossing count, Poisson conditioning, limiting means, percentage errors, negative EC example and synthesis covariance agree with the text.',
 '', 'Source metadata and bounded related-study claims were checked using local primary text and the cited publisher/author records. Some DOI resolver attempts failed; alternate primary pages supplied the needed source identity. This review does not claim a complete live-link or rendered-footnote pass.',
 '', '## Unit answers','']
for a in assessments:
    md += ['### '+a['unit_id'],'',a['questions'][0]['question'],'',a['questions'][0]['answer'],'',
      'Correctness objection: '+a['fields']['Expert objection']['objection'],'',
      'Decision: retain. '+a['fields']['Expert objection']['reason'],'',
      'References: '+', '.join(a['questions'][0]['source_refs']), '']
md += ['## Limits and timing','',*['- '+s for s in report['deferred']],'',
 'Measured Stage 1 start: 2026-10-29T13:19:47.4518693+02:00. Completion and measured durations are added after the records are checked.',
 'One commentary label, 13:22:42, was mistyped. The next measured timestamp was 13:21:43.5424428+02:00; this was a reporting error, not evidence of a system-clock change.',
 'Awake execution time unverified. Token stats unavailable.']
(OUT/'final-place-stage1.md').write_text('\n'.join(md)+'\n',encoding='utf-8')
print(json.dumps(report['counts']))

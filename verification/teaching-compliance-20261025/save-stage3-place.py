import pathlib,json,hashlib,datetime,re
T=pathlib.Path('C:/dev/clsc/burak-papers/guide/verification/teaching-compliance-20261025'); B=pathlib.Path('C:/dev/clsc/burak-papers/guide'); C=B/'content/chapters'
P=json.loads((T/'pedagogy-final/PARAGRAPH_REVIEW.json').read_text(encoding='utf-8')); X=json.loads((T/'concept-index-final.json').read_text(encoding='utf-8')); S1=json.loads((T/'stage1-place.json').read_text(encoding='utf-8'));S2=json.loads((T/'stage2-place.json').read_text(encoding='utf-8'))
def sha(p):return hashlib.sha256(pathlib.Path(p).read_bytes()).hexdigest()
notes={}
def add(file,rows):
 for row in rows.strip().split('\n'):
  n,p,c=row.split('|',2);notes[(file,int(n))]=(p,c)
add('05-place-fields.md','''
3|Pose the observed variety of fields across environments.|Opens with shapes a reader can picture before a statistical model.
5|Give the proposed input model and its distribution-level target.|Answers the opening question and separates fitted sizes/counts from further shape tests.
7|Explain why track crossings and gaps are the first route.|Connects the model to measurable parameters needed by later sizes and shapes.
9|Distinguish randomness across maps from movement through one map.|Prevents carrying temporal diffusion into the new spatial calculation.
13|Show why a rate histogram cannot determine field widths.|Makes the need for covariance concrete before defining a Gaussian process.
15|Define the Gaussian function distribution at finite positions.|Supplies the object whose covariance can determine later spatial predictions.
22|Explain ensemble expectation and the special Gaussian independence rule.|Interprets the preceding functions and supplies the crossing simplification.
24|Separate assumptions by what they allow.|Prepares three independently needed conditions rather than one vague model label.
26|Teach spatial stationarity and its covariance consequence.|Provides constant statistics for averaging along a track without claiming a flat sample.
27|Teach isotropy and distinguish it from stationarity.|Prepares equal directional scales and later round high peaks.
28|State sample derivative and nondegeneracy conditions.|Makes crossing versus peak calculations depend on the correct regularity.
30|Give a Gaussian covariance that does not support smooth paths.|Prevents assuming Gaussian values alone permit differentiating sample maps.
32|Absorb the mean into threshold and normalize input variance.|Prepares a dimensionless threshold and transparent gain in the following rule.
40|Define normalized variables, units and the paper's notation mapping.|Makes the displayed firing rule and source equations comparable.
42|Name the above-level position set.|Introduces the exact mathematical object before discussing connected fields.
48|Identify connected pieces as fields and choose size by dimension.|Separates peak count from component count before crossing and topology tests.
50|Introduce derivative variance from covariance.|Begins the needed relation between spatial statistics and crossing slope.
57|Explain the derivative minus sign and introduce local distance scale.|Turns the covariance derivative into an interpretable positive scale.
64|Interpret sigma as height versus slope and state covariance scope.|Links units to field spacing without assuming all smooth covariances are Gaussian-shaped.
66|Set the fixed teaching map's covariance, threshold and gain.|Makes the following picture an interpretable computation rather than unexplained artwork.
74|Interpret the two panels as one thresholded spatial map.|Closes the figure with connected fields and prevents a temporal-trajectory reading.
78|Motivate crossing counting through a small-band construction.|Extends the earlier upcrossing definition into a calculation without locating roots.
80|Set a simple crossing and its positive local slope.|Provides the tangent approximation used in the band-width argument.
86|Derive unit crossing weight and introduce Kac–Rice afterward.|Explains why integrating slope over a short band counts one crossing.
92|Interpret the joint height/slope density and slope weight.|Connects the integral to selection at crossings rather than above-level occupancy.
94|Introduce the curve that combines edge activity and slope weighting.|Bridges the abstract local argument to the finite-track count convention.
102|State that boundary-clipped fields are included.|Fixes the counting convention before adding the endpoint term.
104|Use stationarity to show zero height/slope covariance.|Starts the independence step required to evaluate the crossing integral.
110|Turn zero Gaussian covariance into independent normal densities.|Supplies the two factors and slope variance in the displayed integral.
124|Evaluate the substitution and interpret exactness and units.|Completes the density calculation before moving to a finite track.
126|Add a field that already intersects the left endpoint.|Converts upcrossing density to the defined finite-track field count.
134|Define the Gaussian tail and qualify the endpoint convention.|Connects the identity to source EC without changing boundary-field selection.
138|Show why a count alone cannot identify threshold and scale.|Uses the exact count result to motivate lengths and gaps as extra summaries.
140|Divide occupied and inactive fractions by field density.|Derives mean sizes/gaps from the previously established event rate.
151|Clarify stationary averaging rather than a finite-sample ratio identity.|Protects the inference algebra from a likely expectation/ratio mistake.
153|Remove one unknown by sums and ratios.|Explains the algebraic route to the inversion rather than only printing it.
160|Introduce the resulting inverse relations.|Closes the preceding two identities with directly usable parameters.
168|Compute mean lengths and finite-track count from fitted parameters.|Makes the equations numerical while clearly distinguishing model calculation from recording estimates.
170|Limit Poisson count and exponential gap claims to rare weakly related fields.|Prevents promoting an exact mean formula to an unjustified full distribution.
172|Condition counts on the experimental exclusion of zero-field cells.|Introduces a concrete sampling change before its probability formula.
181|Derive the conditional mean and show its bias numerically.|Explains why a reported mean can exceed the unconditional model mean.
''')
add('05b-place-sizes.md','''
3|Ask what mean lengths leave unknown about the whole size distribution.|Builds on the preceding inference chapter and motivates a high-peak calculation.
5|Give the peak-to-radius-to-size route and separate slope exactness.|Preserves a useful overview before the first section and announces distinct approximation status.
7|Recall normalized input, threshold, scale, gain and dimension.|Makes the chapter usable without redefining a second statistical model.
11|Explain why the crossing mean does not determine a histogram.|Narrows the overview into the specific high-peak question.
13|Declare a reconstruction and introduce its assumptions.|Places scope before the local calculation that uses it.
15|Keep the smooth stationary isotropic normalized-field setting.|Carries the earlier model conditions needed for derivatives and equal directional curvature.
16|Require nondegenerate derivative statistics.|Prevents conditioning on an ill-defined derivative vector in the curvature calculation.
17|State the high-threshold limit.|Governs all later approximate roundness and exponential excess claims.
18|Specify field sampling and boundary exclusion.|Defines what a typical component means before a distribution is derived.
20|Limit the local argument's theorem claim.|Keeps a teaching reconstruction distinct from a full convergence proof.
22|Define Hessian and relate curvature to height covariance.|Supplies the derivative matrix needed to justify the parabola.
29|Derive Gaussian conditional mean through an independent remainder.|Explains the conditioning step before applying it entry by entry to the Hessian.
35|Explain concentration of curvature at high peaks.|Connects conditional mean to the nearly deterministic local peak shape and keeps maximum-selection scope.
37|Place a peak of excess epsilon at the origin.|Sets the expansion point and zero gradient before the parabola formula.
43|Read the positive parabola as a radius.|Converts the local expansion into geometric extent.
49|Derive an excess-height survival ratio by counting high peaks.|Provides the random ingredient still missing after radius versus height.
56|Scale epsilon to keep a nontrivial high-threshold variable.|Prepares the exponential survival limit instead of letting excess vanish.
63|Interpret the exponential limit and qualify higher-dimensional extension.|Connects peak-count powers to the later Euler check without pretending to prove the full theorem.
65|Convert radius to full one-dimensional length.|Fixes the factor2 before the size law and rate-versus-width statement.
73|Separate two consequences of the same peak calculation.|Prepares one distribution prediction and one rate/size prediction.
75|Identify the square-root-exponential length law as Rayleigh.|Gives the technical family after its constructive meaning.
76|Relate peak rate to squared full length.|Provides the second observable consequence using the defined gain.
78|Explain linear size versus volume in the exponent comparison.|Prevents comparing a length exponent directly to a volume exponent.
80|Compare moderate-threshold exponents with the limiting value.|Keeps data and finite simulations as checks within their actual regime.
84|Motivate converting a radius distribution into dimensional size laws.|Uses the peak result to explain the different track/arena/room histograms.
86|Give unit-ball factors and teach the gamma function.|Supplies the geometric constants and moment notation used next.
88|Apply the derived radius to dimension-dependent size.|Introduces the size transformation and beta scale together.
97|Interpret the same radius in each dimension.|Connects the algebra to the following interval/disk/ball construction.
105|Keep round shape and exponential excess within their limiting regime.|Interprets the idealized figure without turning measured fields into spheres.
107|Use the exponential variable and Jacobian to get size density.|Completes the geometric transformation as a probability calculation.
116|Connect the density to Equation1 and separate finite-threshold scale.|Prevents treating the leading beta formula as an exact fit relation.
118|Extract mean size and its inverse scale relation.|Makes the density usable for parameter interpretation.
127|Check normalization and derive higher positive moments.|Supplies optional verification of the moment formula by the same substitution.
137|Check dimensions of size, beta and the density.|Turns the variable change into a result that can be interpreted with physical units.
139|Distinguish scale removal w from the shape-changing U transform.|Prepares the two-panel comparison and avoids claiming all dimensionless densities coincide.
147|Interpret what the density and survival collapse shows.|Closes the figure by naming which transformation removes the shape difference.
155|Define Weibull and explain a diverging density without zero-volume mass.|Interprets the3D table entry rather than leaving its singular end misleading.
157|Compare mean lengths, areas and volumes at common sigma and q.|Makes the dimensional law concrete without equating unlike units.
159|Quantify the high-threshold approximation error.|Explains why finite-threshold simulations remain necessary after a limiting formula.
163|Introduce specific printed-source algebra checks.|Prepares readers for guide constants that differ from the source's intermediate steps.
165|Identify mean-size division in S18.|Connects the correction directly to the preceding gamma-moment inversion.
166|Identify the missing full-width factor in S23.|Connects the correction to the displayed parabola's two roots.
167|Identify the finite-height exponent sign in S25.|Connects the correction to expanding the survival ratio.
169|State which derivation supports the constants and limit the code inference.|Preserves source accountability without claiming to have found simulation mistakes.
175|Ask whether matching volumes also matches within-field arrangement.|Motivates slicing as an additional spatial test.
177|Derive Gaussian restriction and threshold/slice commutation.|Provides a reason lower-dimensional laws apply on a sampled line or plane.
179|Define connected fields in a slice and their relation to original components.|Prevents treating one3D component as exactly one measurement in every slice.
181|Explain size-biased hits and off-centre cuts.|Restricts which sampling rule the Gaussian line prediction describes.
183|Introduce source panels by measurement dimension.|Helps readers inspect which observed quantity tests which law.
185|Map the2D source panels to line lengths, areas and counts.|Makes the lower-dimensional versus full-map distinction operational.
186|Map the3D source panels to lines, planes and volumes.|Extends the same measurement logic without changing what size means.
188|Use the spherical alternative to show why volume fits are insufficient.|Explains the extra evidence supplied by slices and motivates topology next.
192|Contrast uniformly chosen positions with selected boundaries.|Creates the question the slope-weighting derivation answers.
194|Normalize a restricted crossing contribution to a slope density.|Reuses the earlier Kac–Rice mechanism rather than assuming half-Gaussian sampling.
202|Interpret threshold independence and convert input slope to rate slope.|States the exact model conditions and why gain still matters for recorded rates.
206|Set up an independent local-width check at an upcrossing.|Connects the exact slope law back to the high-threshold geometry constant.
212|Change from boundary slope to full width.|Checks the factor in beta against the peak derivation without claiming exact width geometry.
216|Map source measurements and state finite-difference resolution.|Connects theoretical derivatives to what the boundary-slope comparison actually measures.
''')
add('05c-place-tests.md','''
3|Ask whether maps with matched sizes/counts can differ in holes.|Extends the previous slice comparison to topology and circuit interpretation.
5|Explain the route through holes, boundaries, fitted data and random sums.|Keeps a motivated chapter overview with reasons for each next step.
7|Recall spatial parameters and distinguish d from diffusion D.|Prevents importing temporal dynamics into a fixed spatial map.
11|Show threshold changes can alter components and holes separately.|Motivates a signed count rather than only a field count.
13|Introduce Euler characteristic as the combined count.|Prepares dimension-specific meanings before a formula is used.
15|Give the1D component-count case.|Connects the new topological quantity to the earlier exact track count.
16|Give the2D components-minus-holes rule with disks/ring.|Makes a zero or negative signed count geometrically understandable.
17|Give the3D components/tunnels/cavities rule.|Adds the extra cavity term needed for the room geometry.
19|Name Betti counts after their geometric meaning.|Links the concrete counts to source terminology without relying on a glossary.
21|Introduce one fixed map at multiple thresholds.|Keeps the upcoming comparison about changing level rather than changing samples.
29|Interpret negative chi and the no-hole count case.|Prevents reading the picture as a negative number of place fields.
31|Invoke the critical-point theorem and state its proof limit.|Bridges the geometric count to an expected Gaussian formula without hiding the theorem.
33|Extend Kac–Rice to signed critical-point density.|Uses the earlier crossing idea to motivate the Hessian-determinant integral.
41|Explain gradient density and the determinant volume factor.|Supplies the factors in the integral before its dimension-specific values.
43|Introduce the three signed densities.|Connects the integral to the displayed polynomials used in the box formula.
51|Interpret the densities as signed quantities with physical units.|Prevents applying them directly as positive component densities.
55|Decompose the conditional Hessian and expose covariance pairs.|Begins an optional algebra check of the density factors.
63|Explain what kappa measures and what conditioning subtracts.|Provides the cancellation mechanism rather than only a final determinant result.
69|Expand determinants through three dimensions.|Shows why the unknown fourth derivative cancels from the expected polynomials.
71|Integrate the determinant polynomials over heights.|Connects the conditional curvature algebra to above-threshold density.
81|Verify an integral by differentiation and combine factors.|Closes the optional derivation with a check tied to the displayed result.
85|Count boundary faces and normal-gradient signs.|Adds the finite-box geometry that an interior-only result lacks.
98|State the interval/square/cube match and general-domain limits.|Prevents silently using periodic or volume-only geometry for a small room.
100|Introduce two endpoint sanity checks.|Prepares intuitive threshold extremes for the expected Euler formula.
102|Check the all-active low-threshold limit.|Connects the formula to one connected box.
103|Check the no-active high-threshold limit.|Connects the formula to disappearance of excursions.
105|Compute a negative expected EC at an intermediate threshold.|Demonstrates why exact EC is not an exact field-count formula.
107|Identify the rare simple-blob regime where EC approximates count.|States the extra approximation before retaining a leading volume/q term.
115|Recover the earlier mean-size law from occupied volume and count.|Connects topology to the size calculation as an independent consistency check.
117|Interpret EC curves, firing cutoff conversion and gain fitting.|Explains which parts of the analytic curve measured maps actually test.
121|Distinguish estimated firing maps from hidden Gaussian input.|Motivates tracking fitted summaries and processing before judging prediction.
123|State reuse of recordings and limits of included-sample counts.|Prepares the comparison table without substituting original-study totals.
131|Resolve isolated source label conflicts using full figure analyses.|Explains why the table uses mice and specific panel/sample descriptions.
133|Explain histogram, log-moment and lognormal comparisons.|Teaches skew/kurtosis before interpreting those source tests.
135|Separate in-sample model comparisons from held-out prediction.|Keeps fitted-parameter penalties and simulated error bars within their evidential role.
137|Introduce processing choices that define the compared fields.|Prepares independent measurement decisions in a compact list.
139|State the bat-map denoising threshold.|Identifies a cutoff that can remove small components.
140|State3D binning and median filtering.|Identifies spatial resolution and smoothing affecting shape estimates.
141|State removal of large-volume outliers, including slices.|Identifies a tail change relevant to the distribution comparison.
142|State boundary exclusion and smoothing for peak counts.|Keeps this measurement convention separate from the earlier all-intersecting count.
143|State the extra cutoff for rate-versus-width fits.|Preserves the measurement condition behind the reported exponent.
145|Explain why these decisions affect geometry and tails.|Interprets the processing list as part of the field definition.
147|Add cutoff/curvature comparisons and surface-estimation limits.|Extends validation beyond one histogram without making curvature a prerequisite of the size law.
149|Interpret cross-environment parameter trends and their limits.|Combines threshold/scale effects and keeps the unclear3D unit conversion visible.
151|Explain correlations from a cellwise threshold shared across flight directions.|Shows a fitted heterogeneity extension without implying correlated field locations.
155|Ask how a circuit might produce the successful Gaussian statistics.|Moves from tested map description to one possible biological mechanism.
157|Define fixed input profiles and centered independent random weights.|Sets the averaging ensemble and objects for the weighted sum.
163|Explain the finite-vector central-limit route and its conditions.|Supplies a reason for Gaussian input without treating anatomy count as sufficient.
165|Ask which assumption supplies spatial covariance.|Prepares the cross-term cancellation and profile-overlap calculation.
175|Use uniformly dense translated inputs to obtain covariance by overlap.|Connects the weighted sum to a stationary spatial function away from boundaries.
181|Separate the assumptions' contributions.|Prevents assigning every property of the model to random weights alone.
183|Assign stationarity to uniform spatial coverage.|Interprets the translation-based covariance integral.
184|Assign smoothness to smooth input tuning.|Keeps differentiable paths dependent on input profiles.
185|Assign the Gaussian limit to weight/size conditions.|Keeps the central-limit mechanism separate from spatial regularity.
187|Extend identical profile shapes to a distribution of shapes.|Makes the simple translated-input case an example rather than a universal restriction.
189|Compute covariance for Gaussian input profiles.|Gives a concrete overlap integral with a stated width convention.
196|Interpret the covariance standard-deviation width.|Prevents confusing twice the variance parameter with twice the standard deviation.
198|Limit circuit identification and list conditions where stationarity may fail.|Protects successful aggregate statistics from a unique-wiring conclusion.
200|Carry the statistical result and missing circuit evidence into synthesis.|Closes the chapter with the particular distinction the next chapter needs.
''')
add('06-synthesis.md','''
3|State why successful map, dynamics and behavior claims need different tests.|Makes comparison a scientific question rather than a summary of three papers.
5|Explain the route from distinct objects to a shared-error calculation and joint test.|Keeps the motivated overview before details and states why that sequence helps.
9|Introduce the three questions for a position representation.|Sets up a parallel comparison at a common conceptual level.
11|Identify the map question with place-field statistics.|Uses a known model to specify the first distinct object.
12|Identify temporal maintenance with the persistent-activity model.|Adds the changing represented coordinate that a static map lacks.
13|Identify downstream movement with the eye model.|Adds physical transformation between a neural signal and measured behavior.
15|Resolve three different meanings of position.|Prevents equating an attractor coordinate, internal command and environmental coordinate.
17|Point to the already taught guide comparison figure.|Offers visual retrieval after the conceptual distinctions have been stated.
25|State the direct2012/2022 link and missing information-bound measurement.|Explains why connecting the2025 map still requires a specified moving state.
29|Construct rates by composing fixed tuning with a moving estimate.|Introduces a labeled guide model whose objects have been distinguished.
35|Interpret fixed map versus time-varying rates and extra spike variability.|Prevents treating the composition as a jointly tested circuit model.
37|Set local zero-mean displacement and small-change assumptions.|Places the Taylor approximation's scope before its calculation.
44|Compute covariance from common displacement and local slopes.|Uses the earlier covariance definition to derive a concrete cross-paper connection.
52|State expected-rate, conditional-start and omitted-noise limits.|Prevents mistaking the local result for every spiking-network covariance.
56|Choose slopes, diffusion and duration for a signed example.|Makes opposite responses to one position error numerically testable.
69|Interpret perfect negative correlation and its loss under private noise.|Explains the sign without inferring an inhibitory connection.
71|Choose positive baselines and introduce the two figure panels.|Connects the numerical example to fixed curves and paired changes.
79|Interpret the line of paired changes and effects of private noise.|Closes the figure with its shared-variable geometry.
81|State what population alignment would need to be measured.|Moves from the illustrative covariance to an experimental requirement.
85|Introduce separate evidence tests for the proposed connection.|Uses the shared-error calculation to explain why all three kinds of measurement matter.
87|Explain fit-versus-additional-test distinctions for spatial statistics.|Keeps gain fitting and finite-threshold checks visible in the synthesis.
89|Explain eye calibration, shared covariance and timing evidence limits.|Separates evidence for common drive from a unique circuit location.
91|Explain what an empirical information-bound test would require.|Keeps a mathematical inequality distinct from matching one scaling exponent.
95|Introduce related studies by their role in assumptions and open questions.|Makes the source list an extension of the model comparison.
97|Connect integration background and simulated path integration.|Adds circuit constraints and moving-input assumptions without transferring macaque estimates.
99|Connect coded storage and changing synapses to altered memory assumptions.|Shows why extensions can change predictions while preserving the original calculation's scope.
101|Identify reused place recordings and laterCA3/CA1 comparison.|Distinguishes cross-data agreement from one newly collected protocol and upstream mechanism.
103|Use measured connectivity and place-field plasticity to leave mechanisms open.|Explains why Gaussian aggregate maps do not rule out structure or learning.
105|Separate sensory benefit from source of fixational motion.|Completes the comparison without turning a perceptual advantage into a generator claim.
109|Introduce a joint measurement sequence on the same population.|Turns the missing connection into a concrete proposed experiment.
111|Estimate tuning maps and their uncertainty first.|Supplies the reference changes against which fluctuations will be compared.
112|Measure weakly corrected fluctuations and compare their covariance alignment.|Tests the specific shared-position direction predicted by the maps.
113|Limit diffusion fitting to justified local and measurement ranges.|Preserves the assumptions used by the calculation and earlier noise corrections.
114|Conditionally include observation filters for behavior.|Adds the downstream transformation only when movement is part of the comparison.
116|State the joint constraint and what a mismatch would identify.|Closes with distinct inferential requirements and keeps follow-up separate from replication.
''')

selected=[]
for p in P['paragraphs']:
 f=pathlib.Path(p['source']).name if p.get('source') else ''
 if f not in S1['scope']:continue
 key=(f,p['line']);wrap=p['text'].strip().startswith(('<div','</div>'))
 if wrap: purpose='Keep the adjacent figure/table in its layout container.';connection='Joins the introduced object to its following interpretation; no reader claim is added.';reason='Structural wrapper only; not treated as a separate explanatory paragraph.'
 else:
  assert key in notes,(key,p['text'][:80]);purpose,connection=notes[key];reason=connection+' The needed object or distinction is present in the final text rather than supplied from outside knowledge.'
 selected.append({'id':p['id'],'source_hash':p['source_hash'],'purpose':purpose,'connection':connection,'decision':'retain','reason':reason,'kind':p['kind']})

gloss=[]
for g in S2['glossary_entries']:
 found=[p for p in P['paragraphs'] if 'glossary.md' in p['id'] and p['text'].startswith('[**'+g['term']+':**]')];assert len(found)==1
 p=found[0];gloss.append({'id':p['id'],'source_hash':p['source_hash'],'purpose':'Lookup of '+g['term']+'.','connection':'Refers back to the explicit first teaching in the main reading path; it does not supply an earlier missing prerequisite.','decision':'retain','reason':g['reason']})
refs=[];refroles=['persistent-activity limit','fixational-drift evidence','spatial-field statistics','laterCA3/CA1 comparison','author excursion notes','Gaussian EC theorem','line-attractor background','goldfish perturbation evidence','velocity path-integration model','coded memory storage extension','short-term synaptic-change extension','long-tunnel data source','large-arena data source','3D bat data source','structured connectivity evidence','field-formation plasticity evidence','perceptual benefit of fixational motion']
for p in P['paragraphs']:
 if 'references.md' not in p['id']:continue
 if p['line']==3: purpose='Explain bibliography order and supplement grouping.';connection='Helps readers locate cited works after the chapters.';reason='The preface supplies a lookup rule rather than repeating a scientific result.'
 else:
  index=(p['line']-5)//2;role=refroles[index];purpose='Identify the '+role+' source.';connection='Self-contained lookup for its main-text citation; no transition to the next reference is needed.';reason='Formal title/authors/publication details serve retrieval; the study has a concrete role in the guide, so this is not an unrelated reading list.'
 refs.append({'id':p['id'],'source_hash':p['source_hash'],'purpose':purpose,'connection':connection,'decision':'retain','reason':reason})

# Preserve actual technical objections from Stage1, and give meaningful ones where its default was too general.
objections=[
'A smooth random input does not predict temporal drift or an individual next-field position; the opening explicitly limits its target to map distributions.',
'Covariance alone does not determine a general non-Gaussian law; the definition and independence argument explicitly require joint Gaussianity.',
'Gaussian marginals do not ensure smooth paths or isotropy; the three assumptions and exponential-covariance counterexample separate them.',
'A peak count can differ from connected-field count; the excursion definition explicitly joins peaks connected above threshold.',
'Local sigma does not determine every long-distance covariance; that distinction is explicit after its derivative definition.',
'An above-level probability times an arbitrary slope is not a crossing density; the narrow-band derivation establishes slope weighting.',
'Zero covariance does not imply independence in general; the argument states joint Gaussianity before factorizing the densities.',
'Finite-track fields can be active at the left edge; the identity adds exactly that endpoint component under the stated convention.',
'Expected finite-sample ratios need not equal ratios of expectations; the means are stated as stationary per-field/per-gap averages.',
'Numbers from fitted model parameters could be mistaken for new estimates; their model-calculation status is explicit.',
'Stationarity alone does not imply Poisson fields; distant-correlation decay and a periodic counterexample are explicit.',
'Conditioning on at least one field changes the mean; the zero-truncated law and numerical correction are derived.',
'A local peak sketch is not a full high-excursion convergence proof; assumptions and the proof limit precede the argument.',
'Conditioning on height is not identical to sampling a maximum; the curvature-weighting distinction is retained and only leading high-peak shape is claimed.',
'Peak-count ratios have polynomial factors in higher dimensions; the ratio is explained to tend to1 at q+u/q and the full-theorem limit is explicit.',
'Rate-versus-volume exponent cannot be compared directly to rate-versus-length; cube-root volume and limiting versus finite exponents are distinguished.',
'Finite-threshold beta need not equal its geometric asymptote; the expression is explicitly a leading high-threshold scale.',
'A density diverging near0 need not put mass at0; the integral and delta-window probability interpretation resolve it.',
'High-threshold means can be poor at fitted q1.1; the46% error is displayed rather than hidden.',
'A printed-source discrepancy might arise from extraction or imply code errors; PDFs were checked and the guide limits its correction to printed algebra.',
'Uniform field selection and spatial line sampling have different size bias and offsets; both are explained before applying slice statistics.',
'A uniform-position positive derivative is half-Gaussian, but a crossing derivative is slope-weighted; the exact selected density and approximate width conversion are distinct.',
'Nested sets need not have monotone EC, and negative EC is not negative field count; concrete components/holes and the repaired caption make this explicit.',
'Invoking Morse theory does not prove it; the guide states the theorem being used and derives only the Gaussian expectation factors.',
'Fourth covariance derivatives might remain in determinant averages; the pair cancellation and zero odd Gaussian products show why they cancel here.',
'Interior-only densities omit finite boundaries; face/sign factors and the nonperiodic closed-box condition are explicit.',
'Exact EC cannot generally stand for component count; high threshold, solid blobs, volume dominance and leading q terms are separate conditions.',
'Fitting summaries, source sample counts and likelihood criteria do not establish held-out forecasts; the table and prose retain these distinctions.',
'Preprocessing can alter geometry and tails; binning, rectification, filtering, exclusion and finite surface estimation are listed as part of analyzed fields.',
'Cross-experiment fitted trends or cellwise-threshold correlations need not be biological scaling laws or predictions without extra fitting; both limits are stated.',
'Many inputs do not automatically yield a Gaussian limit; centered independent weights, normalization and no single dominating contributor are explicit.',
'Random weights do not establish stationarity, smoothness or unique wiring; coverage/tuning conditions and alternative circuit mechanisms remain explicit.',
'The three position variables are different; the comparison names each object and does not treat static maps as a memory update law.',
'The shared-displacement covariance is conditional and local, for expected rates; Taylor and noise limitations are explicit.',
'Negative covariance need not mean inhibition or remain perfect with private noise; the example makes the common-position cause explicit.',
'Compatible-looking scaling does not test the full bound and common-drive evidence does not uniquely locate its source; the test-matching bullets preserve those limits.',
'Related study summaries might be transferred across animals, scales or model choices; each contribution is limited and Stage1 checked original-source support.',
'A map or diffusion fit alone does not establish their joint coupling; the proposed steps require same-population maps/fluctuations and relevant filters.'
]
units=[]
for i,old in enumerate(S1['passage_judgments']):
 file=pathlib.Path(old['file']).name;covered=[p for p in selected if pathlib.Path(p['id'].split('::')[0]).name==file and old['start_line']<=int(p['id'].split('::p')[-1])<=old['end_line']]
 units.append({'id':old['id'].replace('s1','s3'),'paragraph_ids':[p['id'] for p in covered],'essential_reasoning_chain':old['stage1_answer'],'strongest_correctness_objection':objections[i],'verdict':'retain with stated conditions','scientific_support':'stage1-place.json#'+old['id'],'source_locator':old['source_locator']})

# Exact IDs and spans in the final concept packet, kept in a separate import file.
byid={p['id']:p for p in X['passages']};relations=[];catalog=[]
specs=[
('spatial-tuning',['ch:FOUNDATIONS/p18','ch:FOUNDATIONS/p28'],['ch:PLACE-FIELDS/p5','ch:SYNTHESIS/p29'],'Expected rate as a function of represented value and measured spatial maps are explained before model use.'),
('covariance-and-correlation',['ch:FOUNDATIONS/p97','ch:FOUNDATIONS/p112','ch:FOUNDATIONS/p119'],['ch:PLACE-FIELDS/p15','ch:PLACE-FIELDS/p22','ch:SYNTHESIS/p44','ch:SYNTHESIS/p69'],'Centered covariance, correlation normalization and their interpretation are actual preceding teaching.'),
('diffusion-variance',['ch:PERSISTENCE/p74','ch:PERSISTENCE/p84'],['ch:SYNTHESIS/p37','ch:SYNTHESIS/p56'],'Final persistence text derives2Dt and teaches Brownian assumptions; synthesis states the same local zero-mean variance.'),
('poisson-counts',['ch:FOUNDATIONS/p39','ch:FOUNDATIONS/p47','ch:FOUNDATIONS/p84'],['ch:PLACE-FIELDS/p170','ch:PLACE-FIELDS/p172','ch:PLACE-FIELDS/p181'],'Count law and independent-increment scope precede the separate spatial independence assumption and truncation.'),
('gaussian-process',['ch:PLACE-FIELDS/p15','ch:PLACE-FIELDS/p22'],['ch:PLACE-SIZES/p22','ch:PLACE-SIZES/p177','ch:PLACE-TESTS/p163'],'Finite-position Gaussian vectors, covariance specification and Gaussian independence are taught before conditioning/restriction/limit interpretation.'),
('excursion-component',['ch:PLACE-FIELDS/p40','ch:PLACE-FIELDS/p42','ch:PLACE-FIELDS/p48'],['ch:PLACE-FIELDS/p78','ch:PLACE-SIZES/p179','ch:PLACE-TESTS/p11'],'Normalized threshold and connected above-level pieces are taught before counting/slicing/topology.'),
('local-spatial-scale',['ch:PLACE-FIELDS/p57','ch:PLACE-FIELDS/p64'],['ch:PLACE-FIELDS/p110','ch:PLACE-SIZES/p22','ch:PLACE-TESTS/p33'],'Derivative-based sigma and distance units precede crossing slope, curvature and EC factors.'),
('crossing-slope-weight',['ch:PLACE-FIELDS/p80','ch:PLACE-FIELDS/p86','ch:PLACE-FIELDS/p92','ch:PLACE-FIELDS/p110','ch:PLACE-FIELDS/p124'],['ch:PLACE-SIZES/p194','ch:PLACE-SIZES/p202','ch:PLACE-SIZES/p212'],'Band width, unit crossing contribution, independent Gaussian factors and exact density are taught before selected-slope reuse.'),
('gaussian-conditioning',['ch:PLACE-SIZES/p29','ch:PLACE-SIZES/p35'],['ch:PLACE-SIZES/p37','ch:PLACE-TESTS/p55','ch:PLACE-TESTS/p63'],'Independent-remainder regression and bounded conditional fluctuation explain the later peak and determinant calculations.'),
('high-peak-excess-and-size',['ch:PLACE-SIZES/p37','ch:PLACE-SIZES/p43','ch:PLACE-SIZES/p49','ch:PLACE-SIZES/p56','ch:PLACE-SIZES/p63','ch:PLACE-SIZES/p65','ch:PLACE-SIZES/p75'],['ch:PLACE-SIZES/p88','ch:PLACE-SIZES/p107','ch:PLACE-TESTS/p107'],'Parabola radius, scaled exponential excess and full width precede dimensional Jacobian and later topology check.'),
('gamma-and-size-moments',['ch:PLACE-SIZES/p86','ch:PLACE-SIZES/p107','ch:PLACE-SIZES/p118','ch:PLACE-SIZES/p127'],['ch:PLACE-SIZES/p137','ch:PLACE-SIZES/p157'],'Gamma meaning and density/moment substitution precede numerical dimensional means; the longer moment check is optional verification.'),
('euler-and-betti',['ch:PLACE-TESTS/p13','ch:PLACE-TESTS/p15','ch:PLACE-TESTS/p16','ch:PLACE-TESTS/p17','ch:PLACE-TESTS/p19','ch:PLACE-TESTS/p29'],['ch:PLACE-TESTS/p31','ch:PLACE-TESTS/p85','ch:PLACE-TESTS/p105','ch:PLACE-TESTS/p117'],'Concrete components/holes/tunnels/cavities and signed-count examples precede Gaussian expectation and threshold-curve interpretation.'),
('critical-points-and-morse',['ch:PLACE-TESTS/p31','ch:PLACE-TESTS/p33','ch:PLACE-TESTS/p41'],['ch:PLACE-TESTS/p43','ch:PLACE-TESTS/p55','ch:PLACE-TESTS/p85'],'The invoked theorem, zero-gradient object, signed determinant and local volume factor are explained before their expectation/boundary calculation.')]
teachsets=[]
for cid,teaches,uses,reason in specs:
 catalog.append({'id':cid,'aliases':[]})
 for role,ids in [('teach',teaches),('use',uses)]:
  for pid in ids:
   p=byid[pid];d={'concept_id':cid,'passage_id':pid,'role':role,'span':[0,len(p['text'])],'status':'reviewed','review':'stage3-place-20261025','evidence':reason}
   if role=='teach':d['adequacy']='partial' if len(teaches)>1 else 'adequate'
   else:d['need']='required'
   relations.append(d)
 teachsets.append({'concept_id':cid,'passage_ids':teaches,'adequacy':'adequate','status':'reviewed','review':'stage3-place-20261025','evidence':reason})
concepts={'audience':{'status':'reviewed','description':'Undergraduate calculus, basic probability and linear algebra, per canonical content/index.md and00-reading-guide.md. Neuroscience, diffusion, information, filtering and spatial random-field concepts require actual teaching.','assumed_concepts':['undergraduate-calculus','basic-probability','linear-algebra']},'concepts':catalog,'sections':{s['id']:'reviewed' for s in X['sections'] if s['chapter_id'] in ['ch:PLACE-FIELDS','ch:PLACE-SIZES','ch:PLACE-TESTS','ch:SYNTHESIS']},'relations':relations,'teaching_sets':teachsets,'reading_order_judgment':'All required uses occur after the cited adequate teaching sets. The later Euler count factor referenced in high-peak discussion is an optional independent check; the local ratio argument explains why its polynomial factor cancels before relying on the limiting excess law. No whole-chapter swap is needed.','index_sha256':sha(T/'concept-index-final.json')}
(T/'concept-judgments-place.json').write_text(json.dumps(concepts,ensure_ascii=False,indent=2),encoding='utf-8')

rule=pathlib.Path('C:/dev/NBIS/publisher-releases/0.8.23/skills/course-study-guide-builder'); files=[C/n for n in S1['scope']]+[C/n.replace('.md','.yaml') for n in S1['scope']]+[C/'glossary.md',C/'references.md',C/'references.yaml',B/'guide-project.yaml',B/'plan/chapter-plan.yaml']
now=datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=2))).isoformat()
typed=[]
for j in S2['typed_reader_fields']:
 p=C/pathlib.Path(j['file']).name;txt=p.read_text(encoding='utf-8').splitlines();a=j['start_line'];end=min(j['end_line'],len(txt));current='\n'.join(txt[a-1:end])
 typed.append({'file':str(p),'start_line':a,'end_line':end,'sha256':hashlib.sha256(current.encode()).hexdigest(),'decision':'retain','purpose':'Orient the section or interpret its associated table/figure.','connection':j['reason'],'truth_check':'Stage1 source/math evidence reused for unchanged claims; repaired GP and EC captions separately passed stage1-recheck-place-stage2.json. The final actual fields were read again for their role and placement.'})
context=[{'source':'plan/chapter-plan.yaml:21-26','purpose':'Explain why observed eye motion and spatial tuning form Part2 and why synthesis follows them.','connection':'Uses neural fluctuations and tuning already taught in Part1, then distinguishes downstream behavior from a static map.','decision':'retain','reason':'This is a reader overview of the particular route, not empty chapter bookkeeping.'},{'source':'guide-project.yaml:10-13','purpose':'Identify three sources and teaching depth, then direct readers to assumed knowledge and reading path.','connection':'Guide metadata orients entry before the technical chapters.','decision':'retain','reason':'A concise description has a different role from the longer reading-guide opening; it need not reproduce derivations.'}]
final_hashes=[{'file':str(p),'sha256':sha(p),'matches_final_packet':X['source_sha256'].get(str(p.relative_to(B)).replace('\\','/')) in [None,sha(p)]} for p in files]
d={'local_request_id':'stage3-place-20261025','reviewer':'/root/compliance_place','model_allocation':'GPT6.1-sol/high per brief; exact runtime variant unexposed','stage':3,'task_started':'2026-10-25T20:11:31.8244846+02:00','stage_started':'2026-10-25T20:39:35.8210938+02:00','completed_at':now,'awake_time':'unverified','scope':S1['scope'],'result':'All assigned final paragraphs retained with individual purpose/connection reasons. No new reader-understanding or flow defect found; previous seven wording repairs are accepted in their final contexts.','findings':[],'paragraph_reviews':selected+gloss+refs,'chapter_units':units,'typed_reader_fields':typed,'context_reviews':context,'concept_judgments_file':str(T/'concept-judgments-place.json'),'concept_mapping':{'concepts':len(catalog),'relations':len(relations),'teaching_sets':len(teachsets),'final_index_sha256':sha(T/'concept-index-final.json'),'earlier_prerequisites_checked':['ch:FOUNDATIONS/p18,p28,p39,p47,p84,p97,p112,p119','ch:PERSISTENCE/p74,p84'],'scope':'Local four-chapter dependency subset, not whole-book concept-index acceptance.'},'scientific_evidence_reuse':{'stage1_record':str(T/'stage1-place.json'),'stage1_sha256':sha(T/'stage1-place.json'),'repair_recheck':str(T/'stage1-recheck-place-stage2.json'),'repair_recheck_sha256':sha(T/'stage1-recheck-place-stage2.json'),'basis':'The complete scientific reading, source comparisons and arithmetic remain in Stage1. Current canonical paragraphs were read again for Stage3. Changed captions and terms received the separate focused truth check. Source hashes are preserved rather than changed in older calls.'},'source_hashes':final_hashes,'rule_hashes':[{'file':str(p),'sha256':sha(p)} for p in [rule/'SKILL.md',rule/'references/pedagogy-language-contract.md',rule/'references/math-code-case-contract.md',rule/'references/concept-prerequisites.md']],'paragraph_packet_hash':sha(T/'pedagogy-final/PARAGRAPH_REVIEW.json'),'chapter_order_verdict':'PLACE-FIELDS establishes covariance/scale/crossing density before PLACE-SIZES needs them; PLACE-SIZES establishes Gaussian curvature conditioning before PLACE-TESTS uses Hessians and distinguishes the higher-dimensional component approximation. SYNTHESIS then needs all three source conclusions and earlier tuning/covariance/diffusion. Openings provide a question, contribution and route in each chapter and should remain.','figure_source_judgments':'Six guide figures retain their function in the reasoning chain: threshold support, crossing unit weight/endpoint, radius-to-size conversion, density versus survival scaling, nonmonotonic signed topology and shared-position rate covariance. Bitmap content was inspected in Stage1; unchanged assets and final captions/alt text are retained. This stage is not a new full pixel sweep.','limits':['This independent record covers the assigned chapters and23glossary entries, plus17References entries and their preface and Part2/description roles. It does not approve unread chapters.','Native equations, source notes and typed cells were read with their connected prose; paragraph extractor wrappers are marked structural rather than falsely treated as teaching.','No full animal-data reanalysis, simulation replication, full convergence/Morse proof, rendered-book acceptance or publication.','Bibliographic identifiers and link resolution remain root\'s separate checks.'],'token_stats':'Token stats unavailable'}
assert len(selected)==211 and len(gloss)==23 and len(refs)==18
(T/'stage3-place.json').write_text(json.dumps(d,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({'saved':str(T/'stage3-place.json'),'completed_at':now,'chapter_paragraphs':len(selected),'glossary_entries':len(gloss),'references_entries_and_preface':len(refs),'concept_relations':len(relations),'concept_teaching_sets':len(teachsets),'findings':0},indent=2))

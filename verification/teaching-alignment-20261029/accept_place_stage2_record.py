import json, pathlib, re, hashlib, collections

ROOT=pathlib.Path('C:/dev/clsc/burak-papers/guide')
OUT=ROOT/'verification/teaching-alignment-20261029'
P=json.loads((OUT/'final-place-input.json').read_text(encoding='utf-8-sig'))
S=json.loads((OUT/'final-place-style-input.json').read_text(encoding='utf-8-sig'))
DATA={}
def add(k,lines,definition,phrase,paraphrase,actor,obj,action,condition,reason,necessity):
    DATA[k]=dict(lines=lines,definition=definition,phrase=phrase,paraphrase=paraphrase,actor=actor,object=obj,action_or_state_change=action,condition_or_consequence=condition,reason=reason,necessity=necessity)

add('ch:GLOSSARY',[3,20,41,55,74,87,99,100],
 'Every glossary item uses the prescribed blue definition span. The 23 terms first marked in the reviewed teaching chapters have matching glossary spellings. Definitions distinguish a critical point from the extra nondegeneracy condition, a stationary process from the spatial Stationarity entry, and Rayleigh from Weibull. This is lookup after main teaching, as p3 says.',
 'The positions where a function exceeds a specified level.',
 'An excursion set contains every position whose function value is higher than the cutoff.',
 'The mathematical definition','positions in the function domain','selects positions by their values','The value must exceed the specified level.',
 'This is the shortest useful lookup meaning. The exact term excursion set is needed to locate the chapter calculation; replacing it by a loose synonym would break lookup.',
 'Short entries let readers recover meanings without replaying derivations. Repeating the blue term here is the explicit glossary exception, not a second chapter introduction. The warnings about sample means, conditional rates, and regularity preserve meaning rather than inflate the entries.')
add('ch:REFERENCES',[3,6,20,24,44],
 'The bibliography introduces no new technical definition. Italics identify publication titles, and author names and titles retain source spelling. Definition blue is not appropriate for titles or identifiers.',
 'The paper\'s supporting information shares its main article entry.',
 'The article and its supplement are found under one bibliography item.',
 'The bibliography','article and supplement','groups their source identity','Separate author notes have their own entry because they are also cited.',
 'This tells the reader where to find supporting equations. Removing it could make an absent separate supplement entry look like a missing source.',
 'Names, dates, article titles, venues, and identifiers enable retrieval. Author-separating semicolons and page ranges are bibliographic conventions, not inflated explanatory prose. The title containing very large is a source title, not the guide praising a result.')
add('ch:PLACE-FIELDS',[7,11,15,17],
 'Place cell, place field, hippocampus, synapse and firing rate are taught earlier. Upcrossing is newly marked at line15 and immediately means an upward passage through the threshold. It is taught before the counting calculation.',
 'The recordings estimate firing rates rather than measuring this input directly.',
 'The measured maps describe firing; the summed synaptic input is a model interpretation.',
 'The recordings','firing rates and modeled input','estimate the former without directly observing the latter','The model is assessed through firing geometry.',
 'The contrast prevents a concrete measurement error. It is needed where the modeled input is first related to the experiment.',
 'Tunnel, floor, and room examples explain why dimension changes. The synaptic interpretation connects the model to cells. The fixed-map limit prevents readers importing the earlier time-noise model. Removing those distinctions would leave the later fit claims ambiguous.')
add('sec:PLACE-GP',[21,23,28,37,47,50,52,68,79,87,105],
 'Gaussian process is blue at23 with its map role;28 supplies the finite jointly Gaussian definition, and37 defines jointly Gaussian vector before the zero-covariance implication is used. Stationarity, Isotropy and Smoothness have separate marked meanings at47/50/52. Excursion set at79 is completed by its displayed set and connected-field explanation. Each has one marked teaching occurrence and a matching glossary entry.',
 'A fitted threshold describes the balance of input and response.',
 'The fitted cutoff combines properties of incoming activity and the cell\'s response.',
 'The fitted threshold','input and response properties','summarizes their combined effect','A changed fit does not identify which biological quantity changed.',
 'Balance is made concrete by the preceding q, input-amplitude, and gain cases. The sentence prevents assigning a single biological cause to a statistical parameter.',
 'The height histogram counterexample motivates covariance before its formula. The smoothness counterexample is needed because Gaussian values alone do not permit derivatives. Repeated fixed-map wording at17/23/117 has different local uses: overall scope, the draw/evaluate operation, and interpreting a plotted horizontal axis. It is not three unexplained slogans.')
add('sec:PLACE-KAC-RICE',[123,132,139,151,157,173,177,185],
 'Upcrossing was taught at15. Kac–Rice formula is blue at132 only after the narrow-band counting operation is explained. The following integral gives its precise role. Phi and Q are defined at185 where the finite endpoint correction needs them. The exact mathematical name and its en dash should remain.',
 'Multiplication by $v$ compensates for the shorter spatial window of a steep crossing.',
 'A faster crossing spends less distance in the narrow height band; weighting by its slope restores one count.',
 'The slope factor v','the narrow-band contribution','cancels the inverse-slope window width','Each regular upward crossing contributes one.',
 'Compensates names the cancellation just calculated. Shortening this to a label such as slope weighting would hide why the integral counts crossings.',
 'The narrow-band example, Gaussian independence argument and endpoint term each supply a different necessary step. The last boundary qualification distinguishes retaining intersecting components from removing incomplete fields.')
add('sec:PLACE-INFERENCE',[189,191,204,206,223,232,237,246],
 'Field and gap are already defined by connected active and inactive intervals. The normal tail is defined at185. Poisson process was taught in foundations;232 specifies its new spatial use and the additional rare-event and distance-dependence limits. No duplicate blue definition is needed.',
 'Field lengths help separate those possibilities.',
 'Lengths add information that distinguishes a higher threshold from a more slowly varying map.',
 'The length measurement together with field count','threshold q and distance scale sigma','separates their effects','Count alone can be reduced by either change.',
 'Those possibilities has the explicit high-threshold and slow-map antecedents in the preceding sentence. This short bridge supplies the reason for the inversion.',
 'The ratio caveat limits what the displayed means assert. The example shows inverse inference and finite boundaries. Silent-cell conditioning answers a separate sampling problem; it is not another version of the endpoint correction.')
add('ch:PLACE-SIZES',[5,9,11],
 'No new technical name is needed in the opening. It uses ordinary peak, radius, length, area and volume before formal Hessian or distribution terms appear. The notation reminder explicitly distinguishes d from the map parameters.',
 'Its height above the threshold sets a radius',
 'The amount by which the peak exceeds the cutoff determines how far the nearby active region extends.',
 'The peak excess together with local curvature','the active region','sets its approximate radius','The peak is high and the smooth input is locally parabolic.',
 'The approximation is announced in the preceding sentence and the high-threshold condition is repeated at the exact-versus-limiting distinction. Sets does not imply a general exact rule for arbitrary fields.',
 'The opening moves from a mean to the missing size distribution. The short notation reminder avoids making readers infer whether size means length, area or volume; the next derivation depends on that distinction.')
add('sec:PLACE-RARE-PEAKS',[15,28,35,58,75,90,92,94,97],
 'Hessian is marked with its matrix-of-second-derivatives meaning and principal-curvature role at28. Rayleigh distribution is marked at90 as a scaled square root of an exponential variable; the subsequent density derives the same object. Exponential variables and the Gaussian conditioning calculation are explained before the transformation is used.',
 'The remaining question is how $\\epsilon$ is distributed when we select one high field at a time.',
 'We need the peak excess distribution for fields counted equally, not for arbitrary spatial points.',
 'Selection of one high field','its excess height epsilon','defines the population whose distribution is calculated','The high-threshold, single-peak approximation applies.',
 'The sampling phrase is essential. Deleting it would make the Gaussian value tail at random positions seem interchangeable with the field-weighted excess law.',
 'The Hessian and conditioning explanation establish curvature, then the survival ratio establishes excess height. The finite-threshold exponent examples stop the asymptotic squared-width prediction from being described as an observed exact exponent.')
add('sec:PLACE-SIZE-LAW',[113,115,145,156,166,168,176,185,188,192,198,204],
 'Gamma function is blue and defined by its integral and factorial relation at115 before ball volume and moments rely on it. Weibull distribution is blue with its survival probability at185. Rayleigh is reused plainly. Units and the distinction between dimensionless w and transformed U are explicit.',
 'Removing units does not erase the difference between length, area, and volume distributions.',
 'Scaling each size to a unitless value leaves different density shapes; the nonlinear U transformation is another operation.',
 'The linear removal of size units','the dimensional size distributions','removes scale but preserves shape differences','Only U=beta times size to the power 2/d gives the common exponential law.',
 'This negation addresses the adjacent density-collapse figure, where a reader could otherwise mistake unit normalization for the full transformation.',
 'The moment integral checks normalization and scale. The q=1.1 versus q=5 numerical comparison makes the approximation error usable. The printed-source corrections belong here because otherwise the reader obtains conflicting constants from the cited supplement.')
add('sec:PLACE-SLICES',[210,213,218,222,227,230,243],
 'Slice is established as restriction to a line or plane at213, not as selecting a field centre. Joint Gaussianity, covariance, isotropy and connected components have prior teaching. Panel letters are source labels, so I is not a first-person pronoun. Centre is ordinary British spelling and need not be changed.',
 'Large fields are more likely to be hit by a spatially sampled line',
 'A line chosen through space encounters bigger fields more often.',
 'Spatial sampling of lines','fields of different sizes','weights which fields are encountered','This differs from choosing each original field with equal probability.',
 'The sampling bias is the necessary reason the original radius distribution cannot simply be reused for line lengths.',
 'The restriction proof and the sampling warning answer different questions. The spherical alternative demonstrates that matching volumes does not ensure the right spatial structure. Figure-panel guidance lets readers locate the actual slice comparisons.')
add('sec:PLACE-SLOPES',[257,259,268,273,279,284],
 'Derivative and boundary are already taught. Rayleigh keeps its earlier exact term and is not marked again. The text explicitly distinguishes a derivative at an arbitrary spatial position from a slope selected at a crossing.',
 'A field boundary is a selected position, however, and selecting it changes the derivative distribution.',
 'The distribution at crossings differs from the distribution at a randomly chosen position.',
 'Conditioning on a threshold crossing','the derivative distribution','weights derivatives by crossing rate','Positive crossing slopes receive the v weighting derived earlier.',
 'Selected is statistical selection, not a vague choice by an observer. The following crossing integral supplies its operation.',
 'The exact q-independent slope law needs its separate derivation to avoid inheriting the high-threshold restriction. The width calculation is a short independent check on the missing square-root-of-two factor, not an unnecessary second full derivation.')
add('ch:PLACE-TESTS',[4,7,9],
 'The opening uses rings, tunnels, regions and holes before naming Euler characteristic. q, sigma and a are restated as a short notation reminder, and d is separated from the earlier diffusion coefficient D.',
 'One may contain rings or tunnels that the other lacks.',
 'Equal field-size statistics can conceal different holes in the active map.',
 'Two possible maps','their connected active regions','arrange them differently','Their field sizes and counts may still agree.',
 'The concrete shapes establish the question before the technical topology name. They make the missing information visible without extra terminology.',
 'The question motivates tests beyond size. The short boundary warning matters for the forthcoming exact formula, while the circuit question prepares the distinction between statistical success and unique biological cause.')
add('sec:PLACE-TOPOLOGY',[17,19,21,23,25,35,37,40,59,100,114,124,141],
 'Euler characteristic is marked before the 1D/2D/3D counting definitions; Betti numbers follows concrete counts. Critical point and Morse theory are marked with the zero-gradient condition and signed-count theorem role. The stated Hessian restriction belongs to the theorem conditions, not the general meaning of critical point. Glossary wording preserves that distinction.',
 'These are signed densities per length, area, and volume, not three formulas for positive field counts.',
 'The quantities count components and holes with signs per spatial size; they need not be nonnegative.',
 'The signed critical-point calculation','expected Euler-characteristic density','combines contributions with plus and minus signs','At high threshold it can approximate field count; at intermediate levels holes can dominate.',
 'Signed is exact mathematical vocabulary needed before the negative example. Replacing it by a softer word would conceal the reason negative values are allowed.',
 'Disk/ring and ball/tunnel/cavity examples teach the alternating count. The boundary derivation prevents applying an infinite-volume expression to a small box. The later negative expected-chi example tests the formula, whereas35 interprets the constructed 2D picture; retaining both supports two different reader tasks.')
add('sec:PLACE-DATA',[148,153,163,166,169,173,177,183,206,230],
 'Skew, excess kurtosis and lognormal distribution are marked with formulas or a transform meaning at166 before interpreting the comparison. Mean curvature and Gaussian curvature at183 are marked with the two principal bend operations and sphere/saddle examples. In-sample and held-out are expressed through the fitting-versus-additional-test discussion rather than an unexplained evaluation label.',
 'Two distribution parameters were chosen to match the two empirical correlations',
 'The threshold-distribution fit uses both measured correlations as fitting targets.',
 'The model fit','two threshold-distribution parameters','chooses them to match measured correlations','Those correlations are fitted quantities; length and gap comparisons provide further checks.',
 'The passive form keeps the fitting operation in focus. The paper and its model are already the actors, so inventing we or the team would not clarify the mechanism.',
 'The table and processing list define what the reported tests actually compare. Uncertain final sample sizes, mice/rats wording, and the unresolved 3D unit conversion must remain visible to prevent false precision. The heterogeneous-threshold extension needs its own parameter accounting.')
add('sec:PLACE-WIRING',[244,246,248,255,269,278,280,281,282,286,297,300],
 'Input profiles, weights and their variance are defined before the covariance calculation. The Gaussian limit is described through independent vectors, normalization and no dominant input. The existing Gaussian-process, stationarity and smoothness terms are reused without new blue spans.',
 'A large anatomical input count alone does not establish how many inputs contribute there.',
 'Many anatomical connections do not guarantee that many of them are active at this position.',
 'An anatomical count','the local set of contributing inputs','fails to determine its active size','The Gaussian approximation requires many actual contributions at the position.',
 'Alone and there have precise jobs: count is insufficient evidence, and there refers to each position. The negative corrects a likely biological overreading of the central-limit argument.',
 'The overlap interpretation explains covariance instead of leaving only an equation. The separate amplitude/width cases explain what each circuit parameter changes. The final alternatives preserve the difference between a sufficient construction and a uniquely identified circuit.')
add('ch:SYNTHESIS',[3,6],
 'The opening uses earlier neural code, circuit and behavior concepts without new terms. It states the comparison problem before the section distinguishes represented and physical position.',
 'keeping each claim with the mathematical or experimental test that supports it',
 'Evaluate each conclusion using the kind of evidence that can establish it.',
 'The comparison of papers','their claims and tests','keeps the support attached to the proper claim','A good spatial fit does not alone establish maintenance dynamics or a unique noise source.',
 'Supports is a concrete evidential relation developed in the next sections. The sentence gives a criterion for comparing the papers, not praise for the guide.',
 'The opening prevents combining three different successes into one untested whole-circuit claim. Its short plan is justified because the next calculation is a new hypothetical connection whose status must stay clear.')
add('sec:SYNTHESIS-QUESTIONS',[13,15,16,17,19,29],
 'Spatial map, memory motion and observed movement are bold list labels, not new technical terms disguised as definitions. The following paragraph distinguishes each paper\'s position coordinate. Fisher information is earlier teaching, and no repeat blue marker is needed.',
 'The objects differ even when the word position appears in all three.',
 'Position can mean a represented network coordinate or the physical position used to evaluate a rate map.',
 'Each paper\'s model','the coordinate called position','assigns it a distinct role','The equations cannot be joined by matching the word alone.',
 'Objects is immediately resolved by theta(t), the internal command, measured eye position and physical map position. It is not left as abstract vocabulary.',
 'The comparison table gives common columns for the random object, determinants and observation. The Fisher-information limit stops a claim that the eye experiment tested equality in the memory bound.')
add('sec:SYNTHESIS-JOINT-CALCULATION',[33,40,43,50,58],
 'The setup defines x(t), f_i and R_i before use and labels the construction as a guide calculation. The local displacement and starting point are defined before Taylor expansion. Covariance and expected rate are prior definitions.',
 'conditional on the starting position',
 'The averaging holds the initial represented position fixed.',
 'The covariance calculation','rate changes from a shared displacement','averages changes at fixed x0','Slopes are evaluated at x0 and the displacement is small.',
 'Conditional is an exact probabilistic restriction. Replacing it with a general association phrase would wrongly suggest an unconditional spike-covariance formula.',
 'The short Taylor step is the direct connection between map shape and time variation. The expected-rate, small-displacement and extra-noise limits are essential because the previous papers contain richer spiking models.')
add('sec:SYNTHESIS-COVARIANCE-EXAMPLE',[68,81,83,91,97],
 'No new definition needs emphasis: slope, variance, covariance and correlation are already taught. The example gives slope units, D, time and the display baseline before reporting the numbers. Calculation and figure is a content label; Example in the heading is not a duplicate Example: example construction.',
 'Both changes are set by the same position displacement',
 'One random position error determines both rate changes.',
 'The common position displacement','the two rate changes','sets both through their different slopes','With no private fluctuations, the pair lies on one line and has correlation minus one.',
 'The passive form has its actor in the same sentence. One direction in the two-rate plane describes the displayed line, not an unexplained geometric metaphor.',
 'The two opposite slopes isolate the sign of covariance with only one random quantity. The baseline only keeps displayed rates positive and is explicitly separated from the covariance. Private-noise commentary explains why the ideal line is not a universal data prediction.')
add('sec:SYNTHESIS-EVIDENCE',[103,105,109,114],
 'Place-field statistics, Eye drift and Memory stability are parallel list labels. The text reuses previous gain, covariance, MSD and information-rate meanings. It does not mark these terms a second time.',
 'Shared covariance then carries information that independent private fluctuations cannot supply under the decomposition\'s assumptions.',
 'Under the stated decomposition, correlation across the observations reveals a shared contribution that independent private noise does not create.',
 'Covariance between the reconstructed and measured changes','the shared component','provides evidence about that component','The decomposition and independence assumptions must hold.',
 'Carries information is resolved by the concrete covariance/decomposition claim. The condition prevents an absolute assertion about all correlated sources. A replacement synonym would not improve this local mechanism.',
 'The section sorts fitted quantities, extra tests and mathematical bounds. The separate gain, stationary-noise amplitude and 1/N limits are needed because each would otherwise make the evidence look stronger than it is.')
add('sec:SYNTHESIS-RELATED',[119,121,123,125,128,131],
 'Path integration is blue at121 with updating a position estimate from movement. Dendrite is blue at128 with branching input structures. Both have matching glossary entries. Earlier CA1, CA3, plasticity, integrator and retina teaching provides the other meanings; titles and author names are source identity, not definitions.',
 'The source and use of eye motion are different questions.',
 'What produces the motion differs from what the motion helps the visual system do.',
 'The two research questions','eye movement','separate its cause from its sensory effect','A perceptual benefit does not uniquely locate the neural generator.',
 'The sentence supplies the reason the perception study belongs next to a noise-source account and prevents a false contradiction between useful motion and internal noise.',
 'The grouped references add model limits, new circuit constraints and distinct behavioral functions. Each group states its relationship to the three core papers; a bare list of related titles would lose that connection.')
add('sec:SYNTHESIS-NEXT',[135,137,138,139,140,143],
 'No new technical definition is introduced. Tuning maps, fluctuations, diffusion and filters refer to the preceding calculations. If comparing behavior is an explicit conditional list label, not a new term.',
 'Fit diffusion only over a range where the local approximation and measurement corrections are justified.',
 'Estimate diffusion from measurements only in the range where this model and its corrections apply.',
 'A proposed joint experiment','the diffusion estimate','fits an applicable range','Local tuning and measurement assumptions must be supported.',
 'Only supplies an operational limit, and the passive justified refers to model and measurement checks. The instruction is appropriate in a proposed procedure, not an unexplained command to believe a claim.',
 'The sequence specifies measurements that would test the new connection. Its final proposed-work label prevents confusing a useful experiment with one the guide or source papers already performed.')

def refs(uid,lines):
    u=P['units'][uid]; out=[]
    for n in lines:
        prior=[p for p in u['paragraphs'] if p['line']<=n]
        if prior:
            ref=uid+'::'+max(prior,key=lambda x:x['line'])['id']
            if ref not in out:out.append(ref)
    return out or [uid]

assessments=[]
for uid,u in P['units'].items():
    d=DATA[uid.split('::')[1]]; rr=refs(uid,d['lines'])
    wording={k:d[k] for k in ['phrase','paraphrase','actor','object','action_or_state_change','condition_or_consequence']}
    wording.update({'verdict':'retain','retention_reason':d['reason'],'deletion_test':d['necessity'],'source_refs':rr})
    assessments.append({'unit_id':uid,'status':'pass','unresolved':[],
      'questions':[{'question':'Are necessary terms taught and marked where this unit needs them?','answer':d['definition'],'source_refs':rr},
                   {'question':'What would be lost by simplifying or deleting the reviewed wording?','answer':d['necessity']+' '+d['reason'],'source_refs':rr}],
      'fields':{'Definition and emphasis':{'verdict':'adequate','evidence':d['definition'],'source_refs':rr},P['review_fields'][3]:wording}})

# The following records serialize the contextual judgments made in this call.
# They do not infer acceptance from the native diagnostic severity.
RULE_REASON={
 'Google.Parens':'Parentheses here carry publication dates, equation labels, acronyms or mathematical arguments. They do not insert a competing prose explanation.',
 'Google.Semicolons':'This alert is in a source note or bibliography entry. The semicolon separates source identities or source locations. It is not a long teaching sentence joined by punctuation.',
 'Microsoft.Semicolon':'This alert is in a source note or bibliography entry. The semicolon separates source identities or source locations. It is not a long teaching sentence joined by punctuation.',
 'Google.Passive':'The object or result is the useful focus, and the mathematical operation, paper, model, or recording supplies the actor in context. No causal actor needed by the explanation is hidden.',
 'Microsoft.Passive':'The object or result is the useful focus, and the mathematical operation, paper, model, or recording supplies the actor in context. No causal actor needed by the explanation is hidden.',
 'Microsoft.Vocab':'The matched word has its ordinary or precise mathematical role in this passage: sample, above threshold, parameter specification, or source author. The surrounding formula or object resolves the meaning.',
 'Microsoft.SentenceLength':'The flagged record includes necessary conditions, definitions, source markup or a connected result. Its actual sentences preserve the object and operation; the raw record length is not a demonstrated comprehension failure.',
 'Google.We':'We introduces a shared derivation or the next necessary comparison; it does not invent experimental work, claim consensus, or instruct a feeling.',
 'Microsoft.We':'We introduces a shared derivation or the next necessary comparison; it does not invent experimental work, claim consensus, or instruct a feeling.',
 'Microsoft.Adverbs':'The modifier changes the claim or belongs to a source title: generally/nearly qualify an approximation, separately distinguishes objects, and very occurs in a publication title.',
 'Microsoft.HeadingAcronyms':'The heading remains a meaningful statement of its subject. Its identifier or established notation is not an unexplained acronym in reader prose.',
 'Google.OxfordComma':'The flagged span contains a two-item pair or a qualifying phrase, not an unpunctuated three-item prose list. No missing comma changes its grouping.',
 'Microsoft.OxfordComma':'The flagged span contains a two-item pair or a qualifying phrase, not an unpunctuated three-item prose list. No missing comma changes its grouping.',
 'Google.Headings':'The heading is a chapter or reference label, or a scientific subject statement. No punctuation or capitalization change is needed to understand its role.',
 'Microsoft.Headings':'The heading is a chapter or reference label, or a scientific subject statement. No punctuation or capitalization change is needed to understand its role.',
 'Google.Will':'The future tense points to the later crossing or Euler derivation, while generally not Gaussian describes the effect of thresholding. Neither is an unsupported promise.',
 'Microsoft.QuestionMarks':'The list deliberately poses three different scientific questions whose answers are the three models. Question marks match that role.',
 'Google.ExcessiveClaims':'The actual claim denies that Gaussian values guarantee smoothness and supplies a covariance counterexample. The trigger word is not an excessive guarantee.',
 'Google.Spelling':'Centre is a standard British spelling in the geometric sampling explanation.',
 'Google.FirstPerson':'I is a figure panel letter in the H, I, J sequence, not the author speaking in first person.',
 'Microsoft.FirstPerson':'I is a figure panel letter in the H, I, J sequence, not the author speaking in first person.'}
alerts=[]
for i,a in enumerate(S['alerts']):
    reason=RULE_REASON[a['Check']]
    alerts.append({'alert_index':i,'source':a['source'],'line':a['Line'],'check':a['Check'],'match':a['Match'],'decision':'retain','reason':reason})

CONTROL_REASON={
 'ai-tells.EmDashUsage':'The character is a range dash in a source/figure location or the established Kac–Rice name. The actual rule also matches en dashes; this is not an em dash joining teaching clauses.',
 'ai-tells.FormalTransitions':'The connector marks an actual algebraic consequence, example, or parameter-dependent case in the surrounding calculation. Removing it would weaken the local relation, and no replacement synonym is needed.',
 'ai-tells.VerbTricolon':'The items are actual dimensions, operations, source-title terms, or distinct measured/model objects. Their number does not make the explanation ornamental.',
 'ai-tells.CataphoricForecasting':'The count refers to actual dimensions, components, maps, assumptions or source papers, or introduces the corresponding concrete mathematical cases. It is not an invented list framework.',
 'ai-tells.ParallelStaccato':'The short parallel statements distinguish different model objects, assumptions or evidence limits. Merging them would make the comparison harder to follow.',
 'Vale.Repetition':'Repeated initials or title words belong to publication identity. They are not repeated explanatory prose to rewrite.',
 'ai-tells.EmptyPadding':'The passage establishes a missing question or scope distinction: input versus measured firing, stationary statistics versus a flat map, or mean versus distribution. Its removal loses the reason for the following step.',
 'ai-tells.AnthropomorphicCognition':'Teaching reconstruction and author teaching notes describe a human document or its purpose, not a mathematical object possessing a mind.',
 'ai-tells.StrawmanContrast':'The distinction separates measured rates from unobserved input or statistical sufficiency from unique circuit identification. These are actual inference limits of the model.',
 'ai-tells.ContrastiveFormulas':'The contrast identifies calculated model values versus fresh empirical estimates, or the guide construction versus a jointly tested source model. It prevents a false experimental claim.',
 'ai-tells.SemicolonUsage':'The locally retained semicolon separates source loci in a bibliographic note. It does not join an inflated teaching sentence.',
 'Microsoft.Quotes':'Quotation marks identify headings in the author source being cited.',
 'ai-tells.FillerPhrases':'The passage states the exponential excess limit or the Weibull survival function and its zero-size interpretation. These are necessary mathematical statements, not filler.',
 'ai-tells.ConsequenceParticiple':'The participle states the consequence of a defined transformation or normalization: Rayleigh from a square root, or dimensionless correlation from covariance scaling.',
 'ai-tells.NounString':'The noun sequence names the measured rate-versus-length exponent or the spatial Gaussian-input model already explained. The actor and measured quantity remain identifiable.',
 'ai-tells.FigurativeCarries':'Population responses encode a value, or shared covariance supplies evidence under a stated decomposition. The surrounding definition states what carries means.',
 'proselint.Very':'Very large is part of the exact title of the cited Eliav paper, not an optional intensifier in the teaching explanation.',
 'ai-tells.LabelAndExplain':'The calculation and exact-model qualification are needed to interpret the integral; the qualification is not a decorative label.',
 'ai-tells.ExplainerLeads':'The quantified approximation error explains why finite-threshold simulations are compared with the limiting law. The causal lead has an actual reason.',
 'ai-tells.OverusedVocabulary':'Meaningful distinguishes a signed topological expectation from an impossible negative count; the numerical example makes the distinction precise.',
 'ai-tells.FillerIntensifier':'The local active-input condition changes whether the central-limit argument applies. A large anatomical count alone does not establish it.',
 'Google.Units':'The matched S2/S8 tokens are supplement section or equation identifiers in a source citation, not unspaced measurement units.',
 'Microsoft.HeadingColons':'Example: identifies the worked calculation type and its subject. It does not introduce a duplicated label.',
 'ai-tells.NegatedObject':'Zero is an eigenvalue condition in the exact term left zero eigenvector, not a vague negated rhetorical object.',
 'ai-tells.FigurativeFires':'Fires is the established neural activity verb in the place-cell definition, connected to spike events earlier.'}
controls=[]
for i,c in enumerate(S['control_regions']):
    controls.append({'control_index':i,'source':c['source'],'rule':c['rule'],'start_line':c['start_line'],'end_line':c['end_line'],'region_sha256':c['region_sha256'],'decision':'retain bounded control','reason':CONTROL_REASON[c['rule']]})

terms=collections.defaultdict(list)
for f in (ROOT/'content/chapters').glob('*.md'):
    for n,s in enumerate(f.read_text(encoding='utf-8').splitlines(),1):
        for t in re.findall(r'\[\*\*(.*?)\*\*\]\{\.definition-term',s):
            terms[t.rstrip(':').casefold()].append({'source':str(f.relative_to(ROOT)).replace('\\','/'),'line':n,'spelling':t.rstrip(':')})
term_checks=[]
for t,locs in terms.items():
    if any(pathlib.Path(x['source']).name.startswith(('05','06')) for x in locs):
        main=[x for x in locs if not x['source'].endswith('glossary.md')]; gloss=[x for x in locs if x['source'].endswith('glossary.md')]
        assert len(main)==1 and len(gloss)==1
        assert main[0]['spelling']==gloss[0]['spelling']
        term_checks.append({'term':main[0]['spelling'],'first_marked_teaching':main[0],'glossary':gloss[0],'verdict':'retain','meaning_check':'See the unit-specific Definition and emphasis answer; marker presence alone is not the judgment.'})

report={'run_id':'final-place-language-20261029-02','run_id_type':'local request ID','reviewer_id':'/root/accept_place','assigned_model':'GPT-6 Astra','assigned_reasoning':'high','stage':'necessity_language','context':'reviewer_continuation','started_at':'2026-10-29T13:34:56.7709936+02:00','completed_at':None,
 'input_hash':P['input_hash'],'review_contract_hash':P['review_contract_hash'],'style_input_sha256':hashlib.sha256((OUT/'final-place-style-input.json').read_bytes()).hexdigest(),
 'scope':'All text in the 22 assigned units, sidecar purposes/summaries, captions, alt text, fold titles and available SVG labels; advisory alerts and bounded controls checked in context. No pixel review.',
 'status':'Stage2 pass within text scope; not complete teaching acceptance or release approval','findings':[],'unresolved':[],
 'assessments':assessments,'advisory_alert_decisions':alerts,'bounded_control_decisions':controls,'definition_checks':term_checks,
 'counts':{'units':len(assessments),'advisory_alerts':len(alerts),'unique_alert_source_lines':len({(x['source'],x['line']) for x in alerts}),'bounded_control_regions':len(controls),'new_teaching_terms_in_scope':len(term_checks)},
 'concision_decisions':[
  {'locations':['05-place-fields.md:17','05-place-fields.md:23','05-place-fields.md:117'],'decision':'retain','reason':'The first limits model scope, the second explains drawing versus evaluating a function, and the caption prevents reading a spatial axis as time. These local reader tasks differ.'},
  {'locations':['05c-place-tests.md:35','05c-place-tests.md:124'],'decision':'retain','reason':'The first explains the constructed 2D picture; the second interprets a negative expected value from the derived 3D formula. The repeated nonnegative-count distinction is needed when applying a signed formula.'},
  {'locations':['05b-place-sizes.md:9','05b-place-sizes.md:145','05b-place-sizes.md:192','05b-place-sizes.md:268'],'decision':'retain','reason':'The scope reminder, beta interpretation, quantified approximation error, and exact boundary-slope contrast qualify different results. Deleting them together would blur which claims require a high threshold.'},
  {'locations':['06-synthesis.md:40','06-synthesis.md:143'],'decision':'retain','reason':'The first identifies the hypothetical model at its introduction; the second identifies the proposed experiment as future work. Neither claims new data.'}],
 'sidecar_and_caption_judgment':'Sidecar summaries preserve the same object and limits as their sections. Captions distinguish reconstructions, limiting calculations, simulations, and original figure excerpts. Alt text describes the plotted quantities and units. Fold titles identify the original paper and figure or the worked calculation, with no new unsupported promise. Exact excerpt/pixel identity remains deferred.',
 'native_diagnostic_limit':'511 alerts represent 160 unique source lines. Duplicate Google/Microsoft warnings and source-punctuation matches are retained with reasons. Native error count does not establish semantic quality. Bounded controls were inspected as passages, not treated as proof that rules were satisfied.',
 'stage1_serialization_addendum':{'original_run_id':'final-place-truth-20261029-01','original_artifact_preserved':True,'scope':'Formatting-only meaning clarification; no new scientific pass','mappings':[{'field':'System setup and component relationships','original_verdict':'retain','official_verdict':'adequate','applies_to':'all 22 Stage1 assessments','reason':'The recorded settings, roles, flow and assumptions were judged sufficient at their cited locations.'},{'field':'Expert objection','original_disposition':'not sustained on complete reading','official_disposition':'does not apply','applies_to':'all 22 Stage1 assessments','reason':'Each proposed correctness objection is answered by the complete passage and its stated conditions, for the individual recorded reason.'}]},
 'tooling_notes':['An initial combined diagnostic read exceeded output limits; targeted smaller reads recovered the passages. One default Windows text read displayed UTF-8 sidecar punctuation incorrectly; explicit UTF-8 reads verified the source has the correct characters. No encoding defect was inferred from that display.'],
 'deferred':['Stage3 ten remaining fields and all paragraph purpose/connection decisions','Guide pixel/layout acceptance','Full publication and release checks'],
 'timing':{'preparation_started_at':'2026-10-29T13:05:39.8301214+02:00','stage1_completed_at':'2026-10-29T13:34:27.4925756+02:00','measured_checkpoints':['2026-10-29T13:34:56.7709936+02:00','2026-10-29T13:36:24.7608816+02:00','2026-10-29T13:37:15.7313178+02:00'],'awake_execution':'unverified','token_stats':'unavailable'}}
assert report['counts']=={'units':22,'advisory_alerts':511,'unique_alert_source_lines':160,'bounded_control_regions':139,'new_teaching_terms_in_scope':23}
allrefs=set(P['units'])|{uid+'::'+x['id'] for uid,u in P['units'].items() for x in u['paragraphs']}
for a in assessments:
    for q in a['questions']:assert set(q['source_refs'])<=allrefs
hashes=json.loads((OUT/'accept-place-stage1-source-hashes.json').read_text(encoding='utf-8'))
for f,h in hashes['files'].items():assert hashlib.sha256((ROOT/f).read_bytes()).hexdigest()==h,f
report['source_hash_verification']='All 12 Markdown and sidecar hashes remain unchanged from the current Stage1 snapshot.'
import yaml
summary_needs={
 'sec:SYNTHESIS-QUESTIONS':(18,18,'Identify the distinction between a spatial map, change in the represented coordinate, and observed downstream movement. The reader should not be left waiting for the three questions.'),
 'sec:SYNTHESIS-EVIDENCE':(30,32,'Give a complete statement about matching each model claim to its relevant test, without introducing an absent list. The existing map-and-rate-change requirement can remain.'),
 'sec:SYNTHESIS-RELATED':(36,37,'State the role of the related studies in testing assumptions or leaving circuit choices open as a complete summary, without promising absent items.'),
 'sec:SYNTHESIS-NEXT':(41,42,'Describe the proposed joint measurements as a complete summary, without introducing an absent sequence. Preserve that the work is proposed and concerns the same population.')}
summary_records=[]
for fn in ['05-place-fields.yaml','05b-place-sizes.yaml','05c-place-tests.yaml','06-synthesis.yaml','glossary.yaml','references.yaml']:
    source=ROOT/'content/chapters'/fn
    yd=yaml.safe_load(source.read_text(encoding='utf-8'))
    for section in yd['section_list']:
        short=section['id']; uid='content/chapters/'+fn.replace('.yaml','.md')+'::'+short
        item={'unit_id':uid,'source':'content/chapters/'+fn,'section_id':short,'summary':section['summary'],'decision':'retain','reason':'The summary gives a complete subject, operation or question and does not depend on an omitted following object.'}
        if short in summary_needs:
            lo,hi,need=summary_needs[short]; fid='PLACE-LANGUAGE-SUMMARY-'+short.split('-')[-1]
            finding={'id':fid,'unit_id':uid,'status':'open','kind':'incomplete reader-facing section summary','severity':'required text repair','source':'content/chapters/'+fn,'start_line':lo,'end_line':hi,'phrase':section['summary'],'failed_check':'Read the sidecar summary by itself: its trailing colon introduces a list that is not part of the summary. The body has the list, but cannot complete this separate reader-facing text.','meaning_needed':need,'source_refs':[uid],'repair_applied':False}
            report['findings'].append(finding);report['unresolved'].append(fid)
            item.update({'decision':'revise','reason':finding['failed_check'],'finding_id':fid})
            assessment=next(a for a in assessments if a['unit_id']==uid)
            assessment['status']='open';assessment['unresolved']=[fid]
            original=assessment['fields'][P['review_fields'][3]]
            assessment['retained_body_wording']=original
            assessment['fields'][P['review_fields'][3]]={'phrase':section['summary'],'paraphrase':'The summary announces the next list, but its items are absent from the summary.','actor':'The section summary','object':'the questions, evidence distinctions, related-study roles or proposed sequence','action_or_state_change':'introduces an omitted list','condition_or_consequence':'When read independently, the summary stops before supplying what its colon promises.','verdict':'revise','replacement_or_retention_reason':need,'deletion_test':'Keep the useful complete claim, but remove the dependence on missing list items or supply their necessary meaning in a standalone statement.','source_refs':[uid],'sidecar_location':finding['source']+':'+str(lo)}
            assessment['questions'].append({'question':'Does the section summary make sense without the chapter body?','answer':'No. '+finding['failed_check']+' Meaning needed: '+need,'source_refs':[uid]})
        summary_records.append(item)
report['section_summary_decisions']=summary_records
report['counts']['section_summaries']=len(summary_records)
report['counts']['incomplete_summaries']=len(report['findings'])
report['status']='Stage2 open: four section summaries need repair and a later check'
report['sidecar_and_caption_judgment']='The bounded independent read found four incomplete synthesis section summaries; these remain open. The other 12 section summaries make complete statements. Caption and alt wording preserves the objects, units and distinctions between reconstructions, limiting calculations, simulations, and original excerpts. Fold titles identify the source figure or worked calculation. Exact artwork identity and pixels remain deferred.'
report['review_update']='After the initial draft, the coordinator identified incomplete summaries in another group and requested an explicit bounded standalone read. This reviewer then read all 16 assigned section summaries independently of their body lead-ins and confirmed the four findings recorded here. The initial no-defect draft was not finalized.'
renderer_evidence={
 'publisher_pin':'0.8.23 / 825ab072f34e06df5d8da6f31552fa0206073045',
 'lock':'publisher-lock.yaml',
 'pinned_source_checked':'git show 825ab072f34e06df5d8da6f31552fa0206073045:src/book_runtime/renderers/quarto.py',
 'source_locations':['src/book_runtime/renderers/quarto.py:1069 (chapter.content_blocks)','src/book_runtime/renderers/quarto.py:1136 (paragraph nodes)','src/book_runtime/renderers/quarto.py:1145 (list nodes)','src/book_runtime/compiler/loader.py:459 (summary loaded as metadata)'],
 'finding':'The pinned Quarto path does not use section.summary to render standalone section text. It renders source paragraph and list nodes, so the body lead-ins have their actual lists. Summary references occur in loader/model/semantic/release metadata.',
 'working_tree_difference':'Three added tooltip CSS lines in quarto.py. The pinned source was also inspected; these lines do not change summary rendering.',
 'scope_limit':'No standalone consumer of section.summary was found in the checked renderer path. A future consumer could need completed summaries; that conditional possibility does not require rewriting current internal metadata.'}
report['renderer_summary_check']=renderer_evidence
for finding in report['findings']:
    finding['classification_history']=[{'classification':'required reader-text repair','basis':'Initial assumption that the sidecar summary was displayed independently.'},{'classification':'conditional internal-metadata note, nonblocking','basis':'Independent pinned renderer inspection found no standalone summary use; the rendered body contains the following list.'}]
    finding['status']='conditional internal-metadata note'
    finding['severity']='nonblocking for current rendered reader text'
    finding['kind']='incomplete if used as a standalone summary'
    finding['condition_for_repair']='Only if a consumer begins displaying section.summary independently.'
    finding['current_repair_required']=False
    finding['failed_check']='Fails only the hypothetical standalone-summary check. It does not fail the current Quarto body path, where the following list is rendered.'
    assessment=next(a for a in assessments if a['unit_id']==finding['unit_id'])
    assessment['status']='pass';assessment['unresolved']=[]
    assessment['fields'][P['review_fields'][3]]=assessment['retained_body_wording']
    assessment['questions'][-1]={'question':'Does the section summary create an incomplete current reader-facing statement?','answer':'No. The metadata would be incomplete if displayed alone, but the pinned Quarto renderer uses the body content nodes and following list. This is a conditional internal-metadata note, not a required current text repair.','source_refs':[finding['unit_id']]}
for item in summary_records:
    if 'finding_id' in item:
        item['decision']='retain as current internal metadata'
        item['reason']='The summary is incomplete only if displayed alone. The pinned renderer does not do that; the corresponding body lead-in is followed by its list.'
report['unresolved']=[]
report['status']='Stage2 pass within current rendered text scope; four conditional internal-metadata notes preserved'
report['counts']['required_repairs']=0
report['counts']['conditional_metadata_notes']=4
report['sidecar_and_caption_judgment']='All reader-facing chapter purposes, captions, alt text and fold titles preserve the relevant objects and scope. Four section-summary metadata values end with list lead-ins; these are preserved as conditional notes because the pinned Quarto renderer does not display them independently. In the body, all four lead-ins have their lists. The other 12 metadata summaries are complete even alone. Artwork identity and pixels remain deferred.'
report['review_update']+=' The coordinator then corrected the standalone-output assumption. Independent renderer inspection confirmed that correction. The report preserves the observations and their classification history rather than deleting them or requiring harmless metadata edits.'
(OUT/'final-place-stage2.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
md=['# Place group: Stage 2 necessity and language','',
 'Request: `final-place-language-20261029-02`. Reviewer: `/root/accept_place`, assigned GPT-6 Astra, high reasoning. Context: reviewer_continuation.',
 '',f"Input hash: `{P['input_hash']}`.",f"Contract hash: `{P['review_contract_hash']}`.",'',
 'No required current reader-text repair was found. Four incomplete-if-standalone synthesis summary values are preserved as conditional internal-metadata notes. Independent inspection of the pinned Quarto renderer confirms that it uses the body paragraphs and their lists, not these summaries as standalone reader text. The review covers all 22 assigned units. The JSON records 511 advisory alert decisions across 160 source lines, 139 bounded control decisions, and 23 newly marked terms with matching glossary entries. These counts describe coverage, not an automatic quality result.',
 '', '## Unit judgments','']
for a in assessments:
    f=a['fields'][P['review_fields'][3]]
    md += ['### '+a['unit_id'],'',a['questions'][0]['answer'],'',
      'Reviewed phrase: '+f['phrase'],'','Plain meaning: '+f['paraphrase'],'',
      f['verdict'].capitalize()+': '+f.get('retention_reason',f.get('replacement_or_retention_reason','')),'','Necessity: '+f['deletion_test'],'',
      'References: '+', '.join(f['source_refs']),'']
md += ['## Conditional internal-metadata notes','']
for finding in report['findings']:
    md += ['- '+finding['source']+':'+str(finding['start_line'])+' ('+finding['unit_id'].split('::')[1]+'): If displayed independently, '+finding['meaning_needed'][0].lower()+finding['meaning_needed'][1:]]
md += ['', 'These observations were initially classified as required reader-text repairs under a standalone-output assumption. That classification was withdrawn after independent inspection of pinned Publisher 0.8.23. Quarto renders chapter.content_blocks and their paragraph/list nodes, without using section.summary. The observations and classification history remain in the JSON. No current metadata rewrite is required, and no manuscript edits were made.',
 '', '## Diagnostic and format decisions','',report['native_diagnostic_limit'],'',report['sidecar_and_caption_judgment'],'',
 'The Stage 1 report remains unchanged. Its system-field verdict retain means adequate. Its expert-objection disposition not sustained on complete reading means does not apply. These mappings apply to all 22 assessments for their original individual reasons. They clarify serialization only.',
 '', '## Timing and limits','',
 'Stage 2 started at 2026-10-29T13:34:56.7709936+02:00. Completion is added after record validation.',
 'Stage 3 remains pending. No guide pixel acceptance or release approval is claimed. Awake execution time unverified. Token stats unavailable.']
(OUT/'final-place-stage2.md').write_text('\n'.join(md)+'\n',encoding='utf-8')
print(json.dumps(report['counts']))

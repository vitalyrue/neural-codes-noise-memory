import pathlib,json,re,hashlib,datetime
TASK=pathlib.Path('C:/dev/clsc/burak-papers/guide/verification/teaching-compliance-20261025')
ROOT=TASK/'proposed'; CH=ROOT/'content/chapters'
S1=json.loads((TASK/'stage1-place.json').read_text(encoding='utf-8'))
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def lines(p):return p.read_text(encoding='utf-8').splitlines()
def locate(file,before):
 p=CH/file;txt=p.read_text(encoding='utf-8'); assert txt.count(before)==1,(file,before,txt.count(before)); at=txt.index(before);return {'file':str(p),'start_line':txt.count('\n',0,at)+1,'end_line':txt.count('\n',0,at+len(before))+1}
findings=[]
def repair(id,file,before,after,reason,deletion,priority=3,kind='necessary wording repair'):
 findings.append({'id':id,**locate(file,before),'before':before,'after':after,'kind':kind,'priority':priority,'failed_check':'Stage2 exact terms, local necessity and everyday wording','reason':reason,'deletion_test':deletion,'retained_conditions':'No scientific assumption, fitted quantity, unit, source citation or limiting condition is removed.','status':'proposed; no manuscript edit'})
repair('place-s2-01','05-place-fields.yaml','Values below $q$ become zero; values above $q$ keep their relative heights after subtraction\n    and scaling.','Values below $q$ become zero; values above $q$ are reduced by $q$ and multiplied by $a$.','Relative heights could mean height ratios, which subtraction does not preserve. The caption can describe the actual two operations without asking readers to choose a meaning of relative.','Keep a verbal explanation of threshold subtraction and gain: deleting the sentence would remove the plain-language mechanism beside the symbolic rule.')
repair('place-s2-02','05c-place-tests.yaml','The above-threshold regions\n    shrink as the threshold rises, even though this signed count does not change in one direction.','The above-threshold regions\n    shrink as the threshold rises, while the Euler characteristic can rise or fall.','Does not change in one direction is an indirect and ambiguous way to describe a nonmonotonic count; it can sound like no change in one spatial direction. The named quantity and rise-or-fall relation are already taught.','Retain the distinction between nested regions and a count that can rise or fall; deleting it would remove the figure\'s interpretation.')
repair('place-s2-03a','05c-place-tests.md','The postsynaptic input is','The summed input is','Postsynaptic is a new specialist word and has no separate job in this sum. The receiving cell\'s input is already identified as h(x), while the input cells and their profiles have been introduced.','The sentence introduces the following equation, so retain its role and use the established object name.')
repair('place-s2-03b','05c-place-tests.md','At a finite list of positions this is a sum of independent random vectors, one per presynaptic cell.','At a finite list of positions this is a sum of independent random vectors, one per input cell.','Presynaptic is another unexplained name for the already introduced input cell. Input cell states the relevant role for the independent-vector sum.','Retain the one-vector-per-input-cell step: it explains what independence applies to in the multivariate limit argument.')
repair('place-s2-04','05c-place-tests.md','For heterogeneous shapes, average the last integral over the distribution of input shapes, as in Methods S2, Equation S8.','For input profiles with different shapes, average the last integral over the distribution of those shapes, as in Methods S2, Equation S8.','Heterogeneous is unnecessary specialist shorthand here. The input profiles, what differs between them, and what is averaged can be stated directly.','Retain this extension because otherwise the identical-translated-input assumption could look necessary for every Gaussian-input account.')
repair('place-s2-05','05b-place-sizes.md','It does not justify assigning an unchanged field-counted radius distribution to all observed chords.','The radius distribution for fields counted once each cannot be used directly as the distribution of lengths observed along a line.','Field-counted is an unexplained compressed label. The surrounding paragraph already contrasts counting original fields with sampling lines; the replacement says the sampling rule directly and uses the same length object as the slice calculation.','Retain the warning about applying a field-sampled distribution to line measurements: it prevents the exact sampling error this paragraph explains.')
repair('place-s2-optional-01','05b-place-sizes.md','The changing power comes from geometry. The round shape and exponential excess belong to the high-threshold limit, so they do not make every measured place field spherical.','The round shape and exponential excess belong to the high-threshold limit, so they do not make every measured place field spherical.','The first sentence repeats the section title, preceding geometric conversion and the figure\'s powers. The second sentence supplies a separate and needed limit.','Removing the first sentence loses no definition, step, assumption, example or connection when read with the preceding equation and figure. The limit remains intact.',kind='optional small deletion')

reasons=[
 'The firing hill and holes give an observable problem in ordinary words. Upcrossing is immediately explained. The fixed-map reminder prevents confusing position with time; deleting it would blur the book\'s central distinction.',
 'Histogram rearrangement gives covariance a purpose before Gaussian process and jointly Gaussian vector appear. Those exact names are needed for the independence argument; the local definitions explain their meanings.',
 'Stationarity, isotropy and smoothness cannot be replaced by one general word: each licenses a different later step. Nondegenerate is immediately unpacked as invertible covariance versus an exact constraint. The exponential-covariance example prevents a real false implication.',
 'The input normalization and paper-to-guide symbol mapping are needed to interpret q, sigma and d without carrying incompatible meanings from earlier chapters. Excursion set is the source term for the exact connected-region object used throughout.',
 'Typical height and slope supply an everyday interpretation of the derivative-based distance scale. Units, covariance choice and the fixed simulated map are all needed to interpret the construction; its caption receives one exact-operations proposal.',
 'The vertical band, distance2epsilon/v and one-crossing contribution are actual reasoning steps. Kac–Rice is introduced after those steps, so the name supports source lookup rather than standing in for explanation.',
 'Jointly Gaussian and independence are repeated exactly because replacing them with similar words would weaken the integral\'s premise. The substitution and inverse-distance interpretation keep the displayed result usable.',
 'Active at the left endpoint and counts all intersecting components specify the convention needed for Q(q). Clipped is explained by boundary fields, and removing that qualifier would change the count.',
 'Per-field mean, occupied fraction and ratio of expectations distinguish the stationary averaging result from an invalid finite-sample claim. The necessary qualification should stay despite its length.',
 'The fitted parameters, model-derived status and endpoint addition make the numerical example a real computation. Removing the model-versus-recording distinction would make the numbers look like new empirical estimates.',
 'Decay of distant correlations and periodic counterexample are necessary conditions, not defensive filler. Poisson and exponential describe different measured quantities, so their exact names should stay.',
 'Unconditioned and conditioned means are exact probability terms with the zero-field selection explained beside them. The lambda1 example shows the size and direction of the selection error.',
 'The chapter distinguishes distribution shape from a mean and approximate geometry from exact crossing slopes. These qualifiers prevent extending the limiting argument to moderate thresholds.',
 'Hessian, eigenvalues and jointly Gaussian conditioning are the mathematical objects the derivation needs. Hessian is defined, and the independent-remainder explanation earns the conditioning formula without an extra regression term.',
 'Leading order, scaled excess and asymptotic count are needed to state the limiting argument accurately. One-field-at-a-time sampling prevents confusing location-sampled values with peak selection.',
 'Full field length and linear size prevent a factor-of-two or dimension error. The numerical nonlimiting exponents explain why finite-threshold data need not show exponent2.',
 'Unit-ball volume, gamma function and change of variables are necessary names for a compact all-dimension derivation. The round-shape qualification must remain; one optional repeated geometry sentence can be removed.',
 'Density versus probability, positive moments and dimensionless size need distinct words. The two transformations are not interchangeable, so the after-figure interpretation has a concrete teaching role.',
 'The q5 example compares physical units, and the q1.1 example exposes a46% approximation error. Neither merely substitutes round numbers to repeat the formula.',
 'Printed supplement and apparent algebraic errors are exact evidence limits, not rhetorical hedging. The note tells readers which formula steps differ without claiming that author code used the same mistakes.',
 'Restriction to a line and connected active interval identify the new object after slicing. The sampling paragraph prevents a wrong radius-to-chord inference; field-counted receives a direct replacement.',
 'The arbitrary-position versus selected-crossing contrast is required for the slope weighting. Rayleigh is needed and has been defined. Exact slope law and approximate width check must remain separately qualified.',
 'Components, holes, tunnels and cavities use ordinary geometric examples before Betti numbers. Signed Euler count needs its exact name because it is not a field count. The caption\'s indirect change phrase receives a direct replacement.',
 'Critical point and Morse theory state the invoked mathematical result and its proof limit. Signed density and determinant identify the calculation\'s object; deleting them would hide why positive-count intuition fails.',
 'Conditional Hessian, centered Gaussian products and fourth derivative are mathematically necessary for the cancellation. Kappa is explained before use and disappears for a reason shown in the derivation.',
 'Closed square/cube, opposite faces not joined and every intersecting component retained are all necessary conditions. Face counts and symmetry describe actual factors rather than broad method labels.',
 'Solid blob gives plain geometry for the rare-component approximation. Leading volume and q terms mark two approximations. The firing cutoff conversion and fitted gain prevent counting a fitted axis as a new prediction.',
 'Fitted, additional comparison and final included cell count have separate meanings. Likelihood penalties and simulated sample moments are explained without adding unnecessary AIC/BIC abbreviations to the main teaching.',
 'The processing list contains independent decisions affecting the map, so bullets suit it. Mean/Gaussian curvature are defined in terms of local bending, and the surface-estimation warning states a concrete measurement limit.',
 'Generally decreases and cross-experiment trend retain real scope limits. The cellwise threshold explanation is needed to explain correlation without shared field locations; fitted features versus extra comparison stays explicit.',
 'The sum and expectation need each input-cell role and the no-dominating-input condition. Two unexplained pre/post-synaptic labels add no needed distinction and receive replacements with the established input/summed-input wording.',
 'Uniform coverage, smooth tuning and random weights must remain separate assumptions. The different-shape extension is useful but its heterogeneous label can be direct. The final mechanism claim needs possible and the measurement limits.',
 'The three positions are genuinely different objects: stored coordinate, command versus movement, and animal location. These distinctions earn their recap at the synthesis; table terms match earlier teaching.',
 'Fixed expected rate and common displacement identify the actors in the composition. To leading order, conditional on starting position, and additional noise are necessary limits, not removable hedges.',
 'One source, opposite slopes and independent private noise explain the sign and magnitude of covariance. The no-inhibitory-link warning prevents a likely causal misreading of negative covariance.',
 'Each evidence bullet names a different claim and how it is tested. Additional fitted gain, calibration validity and compatible conditions are necessary to avoid stronger conclusions than the tests supply.',
 'Related studies are grouped by which assumption or measurement they add. Path integration and dendrite are defined in place. Brief study summaries belong because they constrain possible connections rather than merely listing titles.',
 'The numbered joint-test steps have a real order and the behavior-filter step is conditional. Same population and local approximation are necessary conditions. Proposed follow-up status prevents a false empirical claim.'
]
assert len(reasons)==len(S1['passage_judgments'])
judgments=[]
for old,reason in zip(S1['passage_judgments'],reasons):
 p=CH/pathlib.Path(old['file']).name; a,b=old['start_line'],old['end_line'];quote='\n'.join(lines(p)[a-1:b]); hits=[f['id'] for f in findings if f['file']==str(p) and f['start_line']<=b and f['end_line']>=a]
 judgments.append({'id':old['id'].replace('s1','s2'),'file':str(p),'start_line':a,'end_line':b,'quote':quote,'sha256':hashlib.sha256(quote.encode()).hexdigest(),'decision':'revise indicated phrases; retain remaining teaching' if hits else 'retain','findings':hits,'necessity_and_wording_answer':reason})

covered=[]
for name in S1['scope']:
 p=CH/name;txt=p.read_text(encoding='utf-8')
 for i,m in enumerate(re.finditer(r'\S(?:.*?\S)?(?=\n\s*\n|\Z)',txt,re.S),1):
  t=m.group();a=txt.count('\n',0,m.start())+1;b=a+t.count('\n');matched=[j['id'] for j in judgments if j['file']==str(p) and j['start_line']<=b and j['end_line']>=a]
  hit=[f['id'] for f in findings if f['file']==str(p) and f['start_line']<=b and f['end_line']>=a]
  covered.append({'file':str(p),'unit':i,'start_line':a,'end_line':b,'sha256':hashlib.sha256(t.encode()).hexdigest(),'quote':t[:160],'read_in_this_stage':True,'judgments':matched,'decision':'revise phrase' if hit else 'retain','repair_ids':hit,'source_note_or_markup_reason':None if matched else 'Source notes identify where the adjacent result was obtained and which calculation was reconstructed; exact titles/identifiers are reference text. Markup adds no reader wording. No extra transition is needed.'})

typed=[]
for name in S1['scope']:
 p=CH/name.replace('.md','.yaml');txt=p.read_text(encoding='utf-8');ls=txt.splitlines()
 for i,line in enumerate(ls,1):
  if re.match(r'\s*(title:|purpose:|summary:|caption:|alt:|headers:|rows:)',line):
   indent=len(line)-len(line.lstrip());end=i
   while end<len(ls) and (not ls[end].strip() or len(ls[end])-len(ls[end].lstrip())>indent or ls[end].lstrip().startswith('- ')):end+=1
   quote='\n'.join(ls[i-1:end]);hits=[f['id'] for f in findings if f['file']==str(p) and f['start_line']<=end and f['end_line']>=i]
   typed.append({'file':str(p),'start_line':i,'end_line':end,'quote':quote,'decision':'revise indicated caption phrase' if hits else 'retain','findings':hits,'reason':'Title/purpose/summary names the question or relationship; table cells retain exact variables, conditions and measured/fitted distinctions; caption/alt explains the associated object and separates guide constructions from measurements. Caption/alt repetition supports separate access to the figure and is not prose filler.'})

term_reason={
'upcrossing':'The threshold-crossing direction is needed for counting fields; the short definition gives both action and level.',
'Gaussian process':'The finite-position joint distribution is the essential mathematical definition, not replaceable by random curve.',
'jointly Gaussian vector':'The every-linear-combination property supplies the independence implication used later.',
'Stationarity':'Spatial translation invariance identifies the exact probability-law property rather than flatness of one map.',
'Isotropy':'Rotation invariance is a distinct needed condition for round high-peak geometry and equal directional scales.',
'Smoothness':'Derivative existence/regularity is needed; the note distinguishes crossing and peak derivative orders.',
'excursion set':'Exceeds a level defines the active-position set and is the source term for later field geometry.',
'Kac–Rice formula':'Crossing/critical-point counts and joint derivative distribution identify purpose and needed data; regularity qualifier stays.',
'Hessian':'Second-derivative matrix is concise and exact; the main text explains its curvature role.',
'Rayleigh distribution':'Scaled square root of an exponential matches the guide derivation and distinguishes it from an arbitrary positive law.',
'gamma function':'The defining integral and factorial relation are needed for dimensional size moments.',
'Weibull distribution':'Survival, scale and shape parameters identify the exact family used for3D volume.',
'Euler characteristic':'Alternating sum and3D interpretation distinguish it from positive component count.',
'Betti numbers':'Components/loops/cavities specify what is counted; higher-dimensional counterparts belong in a lookup definition.',
'critical point':'Zero gradient is the definition; invertible Hessian is separately a calculation assumption.',
'Morse theory':'The signed critical-point count and boundary contribution state the exact invoked connection without claiming a full proof.',
'skew':'Centered third moment and variance power are essential; asymmetry states purpose.',
'excess kurtosis':'Centered fourth moment, squared variance and minus3 must all stay to identify the statistic tested.',
'lognormal distribution':'Positive values with Gaussian logarithms is the needed comparator definition.',
'mean curvature':'Average of principal curvatures is a concise exact lookup after the main bending explanation.',
'Gaussian curvature':'Product of principal curvatures is distinct from mean curvature and needs its exact name.',
'path integration':'Updating position from movement gives both action and represented quantity.',
'dendrite':'Branching input structure identifies the physical object without adding cell-biophysics detail.'}
glossary=[]
for i,line in enumerate(lines(CH/'glossary.md'),1):
 for term,reason in term_reason.items():
  if line.startswith('- [**'+term+':**]'):glossary.append({'term':term,'file':str(CH/'glossary.md'),'line':i,'quote':line,'decision':'retain','reason':reason})

refs=[]
for i,line in enumerate(lines(CH/'references.md'),1):
 if re.match(r'\d+\. ',line):refs.append({'line':i,'quote':line,'decision':'retain','reason':'This short reference identifies the work discussed in the guide. Formal title, author list and publication details serve lookup; they should not be simplified into everyday prose or forced into a teaching transition. Identifier accuracy and target resolution are root\'s separate checks.'})
refs_purpose=lines(CH/'references.md')[2]
context=[{'file':str(ROOT/'plan/chapter-plan.yaml'),'start_line':26,'end_line':32,'quote':'\n'.join(lines(ROOT/'plan/chapter-plan.yaml')[25:32]),'decision':'retain','reason':'The Part2 title/purpose separates a motor pathway from spatial tuning and explains why synthesis follows both. Spatial tuning, neural fluctuations and dynamical model have been taught before this Part; these words do not add an unexplained new method.'}, {'file':str(ROOT/'guide-project.yaml'),'start_line':10,'end_line':13,'quote':'\n'.join(lines(ROOT/'guide-project.yaml')[9:13]),'decision':'retain','reason':'As guide metadata the description identifies the three source papers, neural background and mathematical depth, then points to the reading path. This orientation role justifies concise guide-level wording.'},{'file':str(CH/'references.md'),'line':3,'quote':refs_purpose,'decision':'retain','reason':'The preface explains first-use order and how supplements/author notes are grouped. This helps readers find a cited work and is not a repeated scientific explanation.'}]
rule=pathlib.Path('C:/dev/NBIS/publisher-releases/0.8.23/skills/course-study-guide-builder')
paths=[CH/n for n in S1['scope']]+[CH/n.replace('.md','.yaml') for n in S1['scope']]+[CH/n for n in ['glossary.md','references.md','references.yaml']]+[ROOT/'plan/chapter-plan.yaml',ROOT/'guide-project.yaml']
now=datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=2))).isoformat()
d={'local_request_id':'stage2-place-20261025','reviewer':'/root/compliance_place','model_allocation':'GPT-6.1-sol/high per brief; exact runtime variant unexposed','stage':2,'stage_name':'necessity and exact terminology','task_started':'2026-10-25T20:11:31.8244846+02:00','stage_started':'2026-10-25T20:27:36.6255648+02:00','completed_at':now,'awake_time':'unverified','scope':S1['scope'],'additional_scope':['23matching glossary terms','References appendix all17entries and purpose/typed metadata','Part2 title/purpose','guide-project description'],'source_read':'Actual proposed files read during this separate Stage2 call; Stage1 locators reused only to avoid duplicating mathematical source research.','result':'Six necessary phrase repairs across five connected findings; one optional repeated-sentence deletion. Remaining wording retained. No edits applied.','findings':findings,'passage_judgments':judgments,'covered_units':covered,'typed_reader_fields':typed,'glossary_entries':glossary,'references_entries':refs,'context_judgments':context,'source_hashes':[{'file':str(p),'sha256':sha(p)} for p in paths],'rule_hashes':[{'file':str(p),'sha256':sha(p)} for p in [rule/'SKILL.md',rule/'references/pedagogy-language-contract.md',rule/'references/math-code-case-contract.md']],'meaningful_figure_label_review':{'assets':S1['typed_fields']['figures'],'decision':'retain all bitmap labels; two caption phrases proposed for repair','reason':'Threshold level, width/radius, dimensionless size/survival, signed topology counts and rate-change axes are the actual mathematical quantities needed for each picture. The image labels do not add unneeded technical terms. The same six current bitmap contents were inspected in Stage1 and their labels reread for this Stage2 judgment; this is not a rendered-page sweep.','asset_hashes':[x for x in S1['sources'] if x['file'].endswith('.png') and ('assets' in x['file'])]},'limits':['This is Stage2 only; no Stage3 reader-understanding or flow approval is implied.','Bibliographic identifier accuracy, ordering and link resolution remain root\'s assigned checks.','No global word substitution, canonical edit, title/order change, art generation, build or publication performed.'],'token_stats':'Token stats unavailable'}
assert len(glossary)==23 and len(refs)==17
(TASK/'stage2-place.json').write_text(json.dumps(d,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({'saved':str(TASK/'stage2-place.json'),'completed_at':now,'findings':len(findings),'paragraph_units':len(covered),'passage_judgments':len(judgments),'typed_fields':len(typed),'glossary_entries':len(glossary),'references_entries':len(refs)},indent=2))

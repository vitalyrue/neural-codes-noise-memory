from pathlib import Path
import datetime, hashlib, json, re, difflib, math
p=Path(__file__).parent
names=['03-memory-information.md','03b-memory-readout.md','04-eye-drift.md','04b-eye-timing.md','04c-eye-circuit.md']
def sha(path): return hashlib.sha256(path.read_bytes()).hexdigest()
def item(file,anchor,quote,answer,checked):
 text=(p/'proposed/content/chapters'/file).read_text(encoding='utf-8')
 assert quote in text,(file,quote)
 return {'file':file,'section':anchor,'passage':quote,'proposed_line':text[:text.index(quote)].count('\n')+1,'verdict':'retain','truth_and_reasoning_answer':answer,'connected_evidence_checked':checked}
rows=[
item(names[0],'sec:MEMORY-BOUND','The matrix bound',
 'Calling the matrix statement a bound accurately describes the positive-semidefinite inequality. The every-linear-combination interpretation, invertible-J condition and residual-matrix proof are retained.',
 'Information matrix definition, U/V identities and folded Q^TQ proof.'),
item(names[0],'sec:MEMORY-COMPARISONS','Two factors determine',
 'The w^d volume factor and w^-2 squared-slope factor follow from the preceding change of variables. Splitting them into bullets does not turn either into a separate scaling assumption.',
 'Fixed peak a, density rho and shape f; integral for J_alphaalpha.'),
item(names[0],'sec:MEMORY-COMPARISONS','The resulting comparisons are:',
 'From D proportional to w^(2-d), decreasing width lowers D for d=1, the leading exponent vanishes for d=2 and increasing width lowers D for d=3. Equality-achieving, isotropic, exponential-network scope remains in the introduction.',
 'D scaling equation and following alternative fixed-total-rate comparison.'),
item(names[0],'sec:MEMORY-COMPARISONS','Attaining equality identifies',
 'The new wording describes equality in the information-diffusion bound as efficient tracking for fixed information. It still distinguishes this from choosing a firing budget or maximizing available information.',
 'Cauchy-Schwarz equality condition and resource constraints in the same paragraph.'),
item(names[0],'sec:MEMORY-COMPARISONS','This is why the paper suggests',
 'Replacing both functions with sensory estimation and memory storage preserves the conditional claim. Equal sensory/internal tuning and symmetric exponential network conditions remain, and biological colocation is not asserted.',
 'The preceding two conditional sentences and the following animal-location limitation.'),
item(names[1],'sec:MEMORY-READOUT-SETUP','Translation invariance',
 'The new blue occurrence retains the model-specific consequence that the readout variance is independent of x. The glossary correctly gives invariance under represented-value shifts. Constant D, no drift, no boundaries, local unbiasedness and future-noise independence still precede the variance decomposition.',
 'Error decomposition s+e, conditional covariance argument, local Gaussian observation model and glossary entry.'),
item(names[1],'sec:MEMORY-READOUT-SETUP','The two terms describe different sources of error:',
 'Storage contribution 2DT and estimation of theta(T) after T remain distinct. The list is followed by the original state-dependence, boundary, prior and encoding limitations.',
 'Storage/readout timeline, definition of T/L and variance decomposition.'),
item(names[1],'sec:MEMORY-IDEAL','inverse hyperbolic tangent',
 'The tanh exponential formula, real inverse artanh formula on (-1,1), and derivative 1/(1-z^2) are correct. Blue styling identifies existing definitions; the P/a integration uses 0<=P/a<1 for finite positive L.',
 'Precision equation P prime=J-2DP^2, a/k definitions and separated-variable integral; matching glossary definitions.'),
item(names[1],'sec:MEMORY-IDEAL','hyperbolic cotangent',
 'Coth is the reciprocal of tanh, as required when taking reciprocal precision. The glossary adds the correct real-domain exclusion z=0; the readout formula applies to positive L.',
 'P(L) expression, V_ideal expression and short-duration expansion.'),
item(names[1],'sec:MEMORY-IDEAL','Its variance relative to the limiting variance is:',
 'Coth(1), coth(2), coth(3) round to 1.313, 1.037 and 1.005. The following sentence explicitly keeps variance ratios separate from standard-deviation ratios.',
 'Ideal variance formula and characteristic interval Lstar.'),
item(names[1],'sec:MEMORY-FIG3-AND-CAUTION','The plotted features are:',
 'The normalized ideal curve tends to one. Differentiating z/3+1/z gives its minimum at sqrt(3), with value 2/sqrt(3). The dotted line remains identified with that naive optimum; 2DT is explicitly excluded.',
 'Naive/ideal equations and the unchanged Figure 3 discussion and sidecar.'),
item(names[1],'sec:MEMORY-FIG3-AND-CAUTION','The short readout interval is not',
 'Deleting Finally leaves the same distinction between readout saturation, continued mean storage, variance growth and leak-induced restoring motion. The animal-application assumptions remain.',
 'Preceding readout-limit derivation and following spike-statistics, drift and access qualifications.'),
item(names[2],'ch:EYE-DRIFT','small, smooth, irregular movement called fixational drift',
 'Removing repeat blue styling leaves the full movement explanation intact. The reading guide has already defined fixational drift. The distinction between upstream evidence and a proposed integrator source is unchanged.',
 'Reading-guide eye section and this opening paragraph.'),
item(names[2],'sec:EYE-PATHWAY','There are three possible contributions',
 'Shared drive, private OMN variability and downstream muscle/measurement contributions remain the three terms. The paragraph still says private noise can partly cancel; the list does not assert complete cancellation.',
 'Pathway definitions and subsequent covariance model C+eta/C+epsilon.'),
item(names[2],'sec:EYE-RECORDINGS','Gain',
 'Blue styling now marks the actual explanation: gain converts one signal change to the other. The movement-to-rate fit and inverse filter later give its units and scale. Calibration transfer to drift remains an assumption.',
 'Forward-fit coefficients, inverse-filter area 1/k and the unit-gain covariance condition.'),
item(names[2],'sec:EYE-CHI','The calculation assumes:',
 'Both required conditions survive: equal one-for-one common displacement gain and pairwise uncorrelated components to the required accuracy. The later paragraph still identifies the small nonzero recorded-cell covariance neglected as order 1/Nm.',
 'Full covariance expansion, chi formula and small-private-contribution qualification.'),
item(names[3],'ch:EYE-TIMING','To test whether the command accumulates changes',
 'The transition correctly identifies the question answered by comparing two inputs after muscle filtering. It keeps the distinction between noise subtraction and subsequent dynamics testing.',
 'Chapter opening, measurement-error section and filtered-input derivations.'),
item(names[3],'sec:EYE-MEASUREMENT-NOISE','The measurement error is assumed to have:',
 'The three bullets preserve zero mean, common variance, independence from true movement and lack of correlation across distinct samples. They give the same positive-lag offset 2 sigma_m^2; the zero-lag exception and correlated-noise alternative remain visible.',
 'MSD expansion and later covariance correction 2[sigma_m^2-C_nu(lag)].'),
item(names[3],'sec:EYE-FILTERED-MSD','Filtered white noise cannot explain continued long-lag growth.',
 'In connected context, filtered white noise refers to the stable decaying response just derived. Its covariance overlap tends to zero and its MSD plateaus, while the Brownian-input output grows at long lag. The new transition is supported in that scope; the final paragraph explicitly preserves slow correlated peripheral noise as a different hypothesis.',
 'Stationary C_E formula, finite plateau proof, one-exponential example and final scope paragraph.'),
item(names[4],'sec:EYE-SCALING','At fixed network geometry and under the noise assumptions above',
 'From D proportional to CV^2 lambda0/(N a^2 tau_s^2), the four doubling comparisons have factors 1/2, 4, 1/4 and 1/4. Fixed rate remains explicit for the absolute-slope comparison, and fixed geometry/noise scope is repeated. The subsequent rate comparison retains fractional versus absolute slope distinctions.',
 'Both scaling expressions, units discussion and preceding independent-population qualification.'),
item(names[4],'sec:EYE-LIMITS','The data and model answer different questions',
 'The three list entries preserve three different strengths: calibrated covariance supports upstream drive, MSD supports accumulation over the measured interval, and the circuit model supplies a possible integrator mechanism. The list does not turn model compatibility into localization.',
 'Shared-variance chapter, filtered-MSD chapter and complete circuit equations.'),
item(names[4],'sec:EYE-LIMITS','Two missing tests limit that conclusion:',
 'The absence of integrator recordings and selective intervention remains explicit. The next paragraph retains noisy integrator inputs, an already diffusive upstream signal, parameter nonuniqueness and source-response distinction. The two-animal, horizontal-motion scope remains afterward.',
 'Recording design, original localization paragraph, source note p2-localization and final empirical-scope paragraph.')
]
files=[]
for name in names:
 a=p/'baseline/content/chapters'/name;b=p/'proposed/content/chapters'/name
 at=a.read_text(encoding='utf-8');bt=b.read_text(encoding='utf-8')
 def extract(pattern,t):return re.findall(pattern,t,re.M)
 checks={
  'headings_unchanged':extract(r'^#+ .*$',at)==extract(r'^#+ .*$',bt),
  'display_math_unchanged':extract(r'\$\$[\s\S]*?\$\$',at)==extract(r'\$\$[\s\S]*?\$\$',bt),
  'figure_table_markers_unchanged':extract(r'\{\{block:.*?\}\}',at)==extract(r'\{\{block:.*?\}\}',bt),
  'folds_unchanged':extract(r'^:::.*$',at)==extract(r'^:::.*$',bt),
  'footnote_definitions_unchanged':extract(r'^\[\^.*$',at)==extract(r'^\[\^.*$',bt),
  'link_targets_unchanged':extract(r'\]\([^)]*\)',at)==extract(r'\]\([^)]*\)',bt),
 }
 assert all(checks.values()),(name,checks)
 side=Path(name).with_suffix('.yaml').name
 sidecheck=None
 if (p/'baseline/content/chapters'/side).exists() and (p/'proposed/content/chapters'/side).exists():
  sidecheck=sha(p/'baseline/content/chapters'/side)==sha(p/'proposed/content/chapters'/side)
  assert sidecheck
 changes=[]
 al=at.splitlines();bl=bt.splitlines()
 for op,i,j,k,l in difflib.SequenceMatcher(a=al,b=bl).get_opcodes():
  if op!='equal': changes.append({'baseline_lines':[i+1,j],'proposed_lines':[k+1,l],'old':'\n'.join(al[i:j]),'new':'\n'.join(bl[k:l])})
 files.append({'file':name,'baseline_sha256':sha(a),'proposed_sha256':sha(b),'preservation_checks':checks,'matching_sidecar_unchanged':sidecheck,'changed_hunks':changes})
rule=Path(r'C:/dev/NBIS/publisher-releases/0.8.23/skills/course-study-guide-builder')
now=datetime.datetime.now().astimezone().isoformat()
out={'local_request_id':'stage1-information-eye','stage':'1. Truth and reasoning','reviewer':'structure_foundations_memory, independent of the five chapter writers','model':'GPT-6.1-sol/high','task_started_at':'2026-10-24T21:32:54.8366363+03:00','review_started_at':'2026-10-24T21:39:17.6995106+03:00','finished_at':now,'awake_execution':'unverified','fresh_context':'Read actual frozen proposed chapters and matching baselines, reading guide and earlier foundation/memory teaching. Did not read the information-eye writer ledger, rationale or historical verdicts.','rule_hashes':{str(rule/'SKILL.md'):sha(rule/'SKILL.md'),str(rule/'references/pedagogy-language-contract.md'):sha(rule/'references/pedagogy-language-contract.md')},'source_files':files,'glossary':{'file':'glossary.md','proposed_sha256':sha(p/'proposed/content/chapters/glossary.md'),'reviewed_entries':['Translation invariance','hyperbolic tangent','inverse hyperbolic tangent','hyperbolic cotangent'],'verdict':'retain','evidence':'The shift-invariance meaning matches the constant readout-variance statement. Tanh and artanh formulas match the solution of the precision ODE; coth is reciprocal tanh with zero excluded in the glossary. All are correct in the positive-L readout setting.'},'passage_reviews':rows,'numerical_checks':{'coth_1':1/math.tanh(1),'coth_2':1/math.tanh(2),'coth_3':1/math.tanh(3),'naive_minimum_z':math.sqrt(3),'naive_minimum_value':2/math.sqrt(3)},'verdict':'No correctness defect found in changed passages. Stage 1 only.','defects':[],'unresolved_questions':[],'limits':['No fresh audit of unchanged whole source papers or rerun of original experimental data.','Preservation checks cover source figure/table markers and unchanged sidecars, not rendered pixels.','Wording necessity and reader flow are separate later reviews.'],'token_stats':'unavailable'}
(p/'stage1-information-eye.json').write_text(json.dumps(out,indent=2,ensure_ascii=False),encoding='utf-8')
print(json.dumps({'finished_at':now,'passage_reviews':len(rows),'files':len(files),'defects':0,'checks':'passed'}))

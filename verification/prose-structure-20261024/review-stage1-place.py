from pathlib import Path
import difflib,hashlib,json,re
from datetime import datetime
p=Path('C:/dev/clsc/burak-papers/guide/verification/prose-structure-20261024')
comments={
'05-place-fields.md':[
 'The new upcrossing name describes exactly the previous upward threshold passage. The later finite-track identity still adds the active left-endpoint component; this opening does not replace that correction.',
 'Every linear combination being Gaussian is the correct definition. The following zero-covariance implication remains restricted to the jointly Gaussian family, matching the later height/slope independence calculation and the earlier foundations warning that zero covariance is insufficient in general.',
 'The list retains separate stationarity and isotropy requirements, differentiable samples, invertible derivative covariance, stronger second-derivative requirements for peaks, and the nondifferentiable exponential-covariance counterexample. No assumption becomes an implication of Gaussian marginal values.',
 'The revised transition connects the field-count question to the slope-weighted crossing identity. The next narrow-band calculation retains a simple upward crossing, positive slope and regularity; the finite-track endpoint contribution remains explicit later.'
],
'05b-place-sizes.md':[
 'The shorter opening still separates spatial slicing from the independent boundary-slope check on width. It retains the contrast between high-threshold size approximation and exact Gaussian crossing-slope law.',
 'All previous restrictions survive as list items: smooth stationary isotropic unit-variance Gaussian field, invertible derivative covariance, q tending to infinity, typical components counted once, and absence of boundary clipping. The statement that this is a local reconstruction rather than the full convergence proof remains.',
 'The two predictions follow from the preceding s proportional to square-root U and epsilon proportional to s squared equations. The Rayleigh description is correct, and the second prediction remains restricted to fixed high q and linear size; the volume cube-root interpretation remains after the list.',
 'Gamma is defined by the same positive-domain integral and factorial identity already used for the unit-ball volume. Styling adds no changed mathematical claim.',
 'The three source-formula cautions retain exactly the same equation numbers, factor and sign judgments. Their derivational checks remain visible above, and the paragraph still denies an inference that the simulations or empirical fits used those printed errors. This review checks preservation and shown algebra, not a new PDF audit.',
 'The two figure groups retain every panel-to-measurement association. The distinction between spatially sampled slice pieces and original fields remains in the preceding paragraphs; the spherical alternative still matches volumes by construction but fails additional tests.'
],
'05c-place-tests.md':[
 'The dimensional Euler-characteristic rules and all examples are unchanged. The signs agree with beta0 minus beta1 plus beta2: disk components, ring, solid torus and shell are distinguished from positive field counts.',
 'The newly emphasized critical point and Morse theory terms retain zero gradient, invertible-Hessian conditions for this calculation, compact domain and boundary contributions. The glossary correctly defines a critical point by zero gradient alone and treats invertibility as an extra condition. The text still declares that the topological theorem is an external mathematical input rather than a proof supplied here.',
 'The two threshold limits are separate checks of the same bounded closed box: full occupancy gives Euler characteristic one and empty occupancy gives zero. Negative intermediate Euler characteristic remains distinguished from an impossible negative component count.',
 'The skew and excess-kurtosis ratios are unchanged and correctly refer to centered moments of log size. Lognormal sizes make those logs Gaussian with zero population skew and excess kurtosis. The finite-sample fluctuation warning prevents interpreting those zero values as exact sample estimates.',
 'The processing list preserves each original dataset, dimension, cutoff, filter, exclusion and slice-analysis condition. Its following interpretation still says these choices define measured fields and can change components, peaks and tails; none becomes a biological property of the hidden input.',
 'Mean curvature as average and Gaussian curvature as product of the two principal curvatures are correct for a surface in three dimensions. The spherical/saddle explanation and the limitations from surface estimation and finite differences remain. These measurements remain additional tests rather than premises of the size law.',
 'The three sources of model assumptions remain distinct and qualified: uniform dense coverage away from boundaries, smooth input tuning, and the Gaussian limit under independent weights and no dominant contribution. The following convolution gives covariance width square-root two times the input width, so the shorter width sentence retains the exact convention.'
]}
combined=comments['05c-place-tests.md']
combined[4]=combined[4]+' '+combined.pop(5)
combined.append('The shorter covariance-width sentence retains the exact square-root-two factor and its reference to the Gaussian standard deviation. It removes only the unnecessary twice-as-wide phrase; the completed-square integral immediately above still determines the width.')
files=[]
for n,answers in comments.items():
 bp=p/'baseline/content/chapters'/n;np=p/'proposed/content/chapters'/n
 b=bp.read_text(encoding='utf8');a=np.read_text(encoding='utf8')
 bl=b.splitlines();al=a.splitlines()
 ops=[x for x in difflib.SequenceMatcher(None,bl,al).get_opcodes() if x[0]!='equal']
 # Nearby edits can split into multiple opcodes, so group using unified-diff context.
 groups=list(difflib.SequenceMatcher(None,bl,al).get_grouped_opcodes(0))
 assert len(groups)==len(answers),(n,len(groups),len(answers))
 units=[]
 for i,(g,answer) in enumerate(zip(groups,answers),1):
  changed=[o for o in g if o[0]!='equal']; i1=min(o[1] for o in changed);i2=max(o[2] for o in changed);j1=min(o[3] for o in changed);j2=max(o[4] for o in changed)
  units.append({'unit':i,'baseline_lines':[i1+1,i2],'proposed_lines':[j1+1,j2],'before':'\n'.join(bl[i1:i2]),'after':'\n'.join(al[j1:j2]),'verdict':'retain','correctness_evidence':answer,'unresolved_questions':[]})
 for pattern,label in [(r'\$\$.*?\$\$','display_equations'),(r'^\[\^.*$','footnotes'),(r'\]\(([^)]+)\)','link_targets'),(r'\{\{block:.*?\}\}','figure_table_blocks'),(r'^:::.*$','fold_directives')]:
  flags=re.S if label=='display_equations' else re.M
  assert re.findall(pattern,b,flags)==re.findall(pattern,a,flags),(n,label)
 files.append({'baseline_path':str(bp),'proposed_path':str(np),'baseline_sha256':hashlib.sha256(bp.read_bytes()).hexdigest(),'proposed_sha256':hashlib.sha256(np.read_bytes()).hexdigest(),'full_proposed_chapter_read':True,'changed_units':units,'preservation_checks':'Display equations, footnote definitions, links, figure/table blocks and fold directives unchanged.'})
terms=['upcrossing','jointly Gaussian vector','Smoothness','gamma function','critical point','Morse theory','Rayleigh distribution','skew','excess kurtosis','lognormal distribution','mean curvature','Gaussian curvature']
gp=p/'proposed/content/chapters/glossary.md';gl=gp.read_text(encoding='utf8')
ge=[]
for term in terms:
 lines=[x for x in gl.splitlines() if x.startswith('- [**'+term+':**]')]
 assert len(lines)==1,term
 ge.append({'term':term,'passage':lines[0],'verdict':'retain','reason':'Matches the corresponding main-chapter definition and preserves its mathematical object and applicable conditions.'})
rules=Path('C:/dev/NBIS/publisher-releases/0.8.23/skills/course-study-guide-builder/references/pedagogy-language-contract.md')
support=p/'proposed/content/chapters/01-foundations.md'
out={'local_request_id':'stage1-place','stage':1,'review_kind':'Independent correctness only','reviewer':'/root/structure_information_eye, GPT-6.1-sol/high','started_at':'2026-10-24T21:39:22.3899367+03:00','completed_at':datetime.now().astimezone().isoformat(),'fresh_context':'Actual proposed chapters and glossary; normalized baseline diffs and earlier covariance teaching. No writer ledger, rationale or historical review verdict read.','task_wall_start':'2026-10-24T21:32:54.8366363+03:00','awake_execution':'unverified','rule_path':str(rules),'rule_sha256':hashlib.sha256(rules.read_bytes()).hexdigest(),'earlier_teaching':{'path':str(support),'sha256':hashlib.sha256(support.read_bytes()).hexdigest(),'location':'sec:FOUNDATIONS-COVARIANCE; covariance definition, variance of sums, and zero covariance versus independence'},'files':files,'glossary':{'path':str(gp),'sha256':hashlib.sha256(gp.read_bytes()).hexdigest(),'entries':ge},'defects':[],'unresolved_questions':[],'limits':['No new whole-paper or source-PDF audit requested or performed.','Wording and reader-flow stages remain separate and pending.','Glossary coverage is limited to the twelve assigned entries.'],'verdict':'All changed passages retained for correctness; no required repair.','token_stats':'unavailable'}
(p/'stage1-place.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
print(out['completed_at'],sum(len(x['changed_units']) for x in files),'changed passage groups;',len(ge),'glossary definitions; no correctness defects')

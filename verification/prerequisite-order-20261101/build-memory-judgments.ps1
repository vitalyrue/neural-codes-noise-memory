$root='C:\dev\clsc\burak-papers\guide'
$dir=Join-Path $root 'verification\prerequisite-order-20261101'
$idx=Get-Content -LiteralPath (Join-Path $dir 'concept-index-final.json') -Raw | ConvertFrom-Json
$baseline=Get-Content -LiteralPath (Join-Path $dir 'concept-index-baseline.json') -Raw | ConvertFrom-Json
$chapters=@('ch:READING-GUIDE','ch:FOUNDATIONS','ch:PERSISTENCE','ch:MEMORY-DYNAMICS','ch:MEMORY-LONG-DELAYS','ch:MEMORY-INFORMATION','ch:MEMORY-READOUT')
$passages=@{}; foreach($p in $idx.passages){$passages[$p.id]=$p}
$relations=[System.Collections.Generic.List[object]]::new()
function Add-Rel($concept,$passageKey,$role,$startText,$stopText,$evidence) {
  $p=$passages[$passageKey]; if($null -eq $p){throw "Missing $passageKey"}
  $start=if($startText){$p.text.IndexOf($startText,[StringComparison]::Ordinal)}else{0}
  if($start -lt 0){throw "Missing start $passageKey $startText"}
  $end=if($stopText){$p.text.IndexOf($stopText,$start,[StringComparison]::Ordinal)}else{$p.text.Length}
  if($end -le $start){throw "Bad end $passageKey $stopText"}
  $r=[ordered]@{concept_id=$concept;passage_id=$passageKey;role=$role;span=@($start,$end);status='reviewed';review='stage3-memory';evidence=$evidence}
  if($role -eq 'teach'){$r.adequacy='adequate'}elseif($role -eq 'use'){$r.need='required'}
  $relations.Add([pscustomobject]$r)
}
Add-Rel 'brownian-motion' 'ch:PERSISTENCE/p124' 'teach' '[**Brownian motion**]' ' The independence' 'Defines path, start, Gaussian independent increments, mean and variance; now on main path.'
Add-Rel 'brownian-motion' 'ch:MEMORY-DYNAMICS/p39' 'use' 'Let $B_i$' ' The increment' 'Independent Brownian processes used as model noise; prior main-path definition supplies meaning.'
Add-Rel 'brownian-motion' 'ch:MEMORY-READOUT/p74' 'use' 'Write ' '' 'Brownian memory path introduced for readout covariance; earlier definition and local covariance explanation provide required process.'
Add-Rel 'brownian-increments' 'ch:MEMORY-DYNAMICS/p39' 'teach' 'The increment' ' Multiplying' 'Explicit dB=B(t+dt)-B(t), zero mean and variance dt before noise scaling.'
Add-Rel 'brownian-increments' 'ch:MEMORY-DYNAMICS/p39' 'use' 'Multiplying' '' 'Variance matching requires increment scale defined earlier within the same paragraph.'
Add-Rel 'brownian-increments' 'ch:MEMORY-DYNAMICS/p182' 'use' 'The independent Brownian' '' 'Uses increment covariance to calculate projected diffusion; direct display equations also inspected.'
Add-Rel 'centered-spike-count' 'ch:MEMORY-DYNAMICS/p28' 'teach' 'Write ' ' Splitting' 'Defines dM as count minus conditional mean and surplus/deficit.'
Add-Rel 'centered-spike-count' 'ch:MEMORY-DYNAMICS/p28' 'use' 'Splitting' '' 'Mean/noise decomposition follows explicit count definition; next display checked directly.'
Add-Rel 'centered-spike-count' 'ch:MEMORY-DYNAMICS/p39' 'use' 'Multiplying' '' 'Comparison with centered spike count uses earlier explicit dM definition.'
Add-Rel 'mean-activation-drift' 'ch:MEMORY-DYNAMICS/p39' 'teach' 'Let $F_i' ' Let $B_i$' 'F role established before its displayed equation; equation checked directly.'
Add-Rel 'mean-activation-drift' 'ch:MEMORY-DYNAMICS/p99' 'use' 'Differentiate' '' 'Fixed point derivative uses F defined earlier in same chapter.'
Add-Rel 'linear-response-matrix' 'ch:MEMORY-DYNAMICS/p77' 'teach' 'Let $K$' ' Let $R$' 'K maps disturbance to its first-order mean rate of change; algebra follows and is directly checked.'
Add-Rel 'linear-response-matrix' 'ch:MEMORY-DYNAMICS/p88' 'use' 'The entries of $K$' '' 'Units interpretation follows role and algebra.'
Add-Rel 'local-spike-covariance' 'ch:MEMORY-DYNAMICS/p77' 'teach' 'Let $R$' ' Then' 'R is diagonal spike count variance rates at fixed point; R=diag(rbar) equation checked directly.'
Add-Rel 'local-spike-covariance' 'ch:MEMORY-DYNAMICS/p88' 'use' 'In this leading local calculation' ' The entries' 'Interprets evaluation of noise strengths immediately after R definition.'
Add-Rel 'memory-projection-vector' 'ch:MEMORY-DYNAMICS/p173' 'teach' 'Recall ' '' 'Inline delta theta=sum v_i delta s_i and lasting angular effect per activation make projection meaning explicit; prior full v equations inspected directly.'
Add-Rel 'memory-projection-vector' 'ch:MEMORY-DYNAMICS/p175' 'use' 'Multiplying' '' 'Projection removes deterministic term using already-derived normalized left vector.'
Add-Rel 'likelihood' 'ch:MEMORY-INFORMATION/p80' 'teach' 'To compare possible angles' '' 'Observed counts held fixed while proposed theta varies; probability over parameter explicitly distinguished.'
Add-Rel 'likelihood' 'ch:MEMORY-READOUT/p19' 'use' 'To solve' ' Let $x=' 'Gaussian likelihood approximation now has preceding main-path meaning.'
Add-Rel 'likelihood' 'ch:MEMORY-READOUT/p133' 'use' 'To verify this' '' 'Multiplication of likelihoods uses earlier meaning and local explicit Gaussian expressions.'
Add-Rel 'gaussian-observation-bin' 'ch:MEMORY-READOUT/p19' 'teach' 'Let $x=' ' The equivalent' 'State at cue, bin index, eta transition, y estimate and epsilon error plus independent zero-mean Gaussian assumptions all established; display variances inspected directly.'
Add-Rel 'gaussian-observation-bin' 'ch:MEMORY-READOUT/p86' 'use' 'Count noise' '' 'Count-noise averaging uses defined bin observation variance 1/(Jh).'
Add-Rel 'coth-readout-factor' 'ch:MEMORY-READOUT/p173' 'teach' '[The ' ' For positive' 'Explicit exponential expression defines coth factor; adjacent display169-170 supplies full finite readout formula and is checked directly.'
Add-Rel 'coth-readout-factor' 'ch:MEMORY-READOUT/p220' 'use' '' '' 'Ratio at one characteristic time is coth(1); finite formula and L* display checked directly.'
Add-Rel 'coth-readout-factor' 'ch:MEMORY-READOUT/p221' 'use' '' '' 'Ratio at two characteristic times uses same earlier result.'
Add-Rel 'coth-readout-factor' 'ch:MEMORY-READOUT/p222' 'use' '' '' 'Ratio at three characteristic times uses same earlier result.'
Add-Rel 'white-noise' 'ch:MEMORY-READOUT/p278' 'teach' 'The symbol' ' The two dynamical' 'Noise drive, ideal unequal-time decorrelation, no finite point variance, xi dt=sqrt(r)dB and conditional integrated variance supplied before equations.'
Add-Rel 'white-noise' 'ch:MEMORY-READOUT/p278' 'use' 'The two dynamical' '' 'Leads immediately to directly inspected xi-driven equations; indexed prose is a location marker, not replacement for equation review.'
Add-Rel 'white-noise' 'ch:EYE-TIMING/p89' 'use' 'The input is idealized' ' [A stable' 'Ch8 filtering model refers to earlier main-path white-noise definition and repeats required unequal-time decorrelation.'
Add-Rel 'readout-time-normalization' 'ch:MEMORY-READOUT/p336' 'teach' 'Write $z=' ' In these axes' 'Explicit dimensionless time z=L/L*=sqrt(2DJ)L before formulas.'
Add-Rel 'readout-time-normalization' 'ch:MEMORY-READOUT/p336' 'use' 'In these axes' '' 'Both normalized curve expressions follow their axis definition within paragraph.'
$sections=[ordered]@{}; foreach($s in $idx.sections){if($chapters -contains $s.chapter_id){$sections[$s.id]='reviewed'}}
$concepts=@(); foreach($id in ($relations.concept_id | Select-Object -Unique)){$concepts += [pscustomobject]@{id=$id;aliases=@()}}
$out=[ordered]@{concepts=$concepts;sections=$sections;relations=$relations.ToArray();teaching_sets=@()}
$out | ConvertTo-Json -Depth 15 | Set-Content -LiteralPath (Join-Path $dir 'concept-judgments-memory.json') -Encoding utf8
$hashes=[ordered]@{}; foreach($prop in $idx.source_sha256.PSObject.Properties){$file=$prop.Name; if($file -match '^content/chapters/(00-reading-guide|01-foundations|01b-persistence|02-memory-dynamics|02b-memory-long-delays|03-memory-information|03b-memory-readout)\.'){ $actual=(Get-FileHash -LiteralPath (Join-Path $root $file) -Algorithm SHA256).Hash.ToLowerInvariant(); if($actual -ne $prop.Value){throw "Stale index $file"}; $hashes[$file]=$actual }}
$adoption=@(); foreach($s in $idx.sections){ if($chapters -contains $s.chapter_id){$old=$baseline.sections | Where-Object {$_.id -eq $s.id}; $adoption += [pscustomobject]@{section_id=$s.id;heading=$s.heading;sha256=$s.sha256;basis=if($old -and $old.sha256 -eq $s.sha256){'Initial full diagnosis adopted only for unchanged section; outgoing/incoming connections rechecked'}else{'Changed section reread with connected definitions and dependent uses'};scope='Prerequisite order and connected reading path only'}} }
$now=[DateTime]::UtcNow
$report=[ordered]@{stage='3 connected reader understanding and flow';status='pass for frontmatter and Part I prerequisite path';task_start_utc='2026-11-01T13:32:42Z';review_start_utc='2026-11-01T13:51:28Z';review_complete_utc=$now.ToString('yyyy-MM-ddTHH:mm:ssZ');wall_elapsed_seconds_since_task_start=[int]($now-[DateTime]::Parse('2026-11-01T13:32:42Z').ToUniversalTime()).TotalSeconds;awake_execution_time='unverified';file_hashes=$hashes;section_coverage=$adoption;concept_index='concept-index-final.json';concept_judgments='concept-judgments-memory.json';judgment_counts=@{sections=$sections.Count;concepts=$concepts.Count;relations=$relations.Count};chapter_order='Retain signals/model, persistence geometry, local projected diffusion, boundary/drift extension, information bound, then moving-state readout. Frontmatter and Part previews orient without requiring later proofs. Short foundations satisfy actual dependencies; chapter moves would separate mechanisms from the question that motivates them.';connection_evidence=@(
'Ch1 establishes spikes, synaptic activation, weighted input and transfer before Ch2 persistent states; Ch2 now supplies Brownian process meaning in main text before Ch3.',
'Ch3 teaches centered count, mean activation drift, Brownian increment scale and matrix roles before the matching equations; v purpose precedes normalization, and later diffusion recalls its angular meaning. Existing weak-noise and conditional independence restrictions stay connected.',
'Unchanged Ch4 extends local D with boundary and state-dependent noise qualifications; figure discussion then motivates estimating the moving state, rather than relying on an unexplained information metric.',
'Ch5 defines local information using rate sensitivity and count noise before the bound. Likelihood definition is now main text before Ch6 Gaussian observation approximation; optional score proof is no longer the only access to likelihood meaning.',
'Ch6 defines cue state, transition increment and observation error before bin equations. The precision recursion follows those roles; finite result and coth meaning are visible before ratio interpretation. Integration remains optional.',
'Ch6 white-noise/increment bridge precedes xi equations and later Ch8 filtering use. Ch8 repeats unequal-time decorrelation, so the cross-Part connection requires neither an unseen definition nor a general stochastic calculus lesson.',
'Ch6 dimensionless z is explicit before normalized figure expressions. Stage2 repaired variance sentence names total readout variance and leaves the positive limiting value clear.'
);direct_display_math_checks=@(
'02-memory-dynamics.md:30-35 centered count equation;41-45 Brownian SDE;81-86 K/R;113-116 v normalization. These displays are absent from extracted passages but were read directly.',
'03b-memory-readout.md:21-29 observation equations;168-171 finite ideal variance;213-216 L* and limit;280-284 white-noise model. Direct review supplies mathematical evidence not present in packet prose.'
);limitations=@('Extractor omits display math. Exact indexed prose spans organize important dependencies, while this report records direct display inspection. No bare prose lead-in is claimed to teach a missing mathematical formula.','Section judgments cover prerequisite order, adopting initial whole-section diagnosis only where unchanged and rechecking changed connections. They do not establish a full source-claim, visual or publication acceptance.');remaining_findings=@();required_repairs=@();source_edits_made=$false;token_stats='unavailable'}
$report | ConvertTo-Json -Depth 20 | Set-Content -LiteralPath (Join-Path $dir 'stage3-memory.json') -Encoding utf8
[pscustomobject]@{time=$report.review_complete_utc;sections=$sections.Count;concepts=$concepts.Count;relations=$relations.Count;files=$hashes.Count;status=$report.status} | ConvertTo-Json

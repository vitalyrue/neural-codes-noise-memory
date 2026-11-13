from pathlib import Path
import json,yaml,hashlib,datetime,subprocess,sys
ROOT=Path(__file__).resolve().parents[2]; OUT=Path(__file__).resolve().parent
RELEASE=Path('C:/dev/NBIS/publisher-releases/0.8.23')
SHARED=Path('C:/dev/NBIS/performance-engineering-course')
COMMIT='825ab072f34e06df5d8da6f31552fa0206073045'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
export=json.loads((OUT/'source-export-check.json').read_text(encoding='utf-8-sig'))
print('Independent source export evidence present:',OUT/'source-export-check.json')
inputs={str(p.relative_to(ROOT)).replace('\\','/'):sha(p) for d in ('content','assets/styles') for p in (ROOT/d).rglob('*') if p.is_file()}
(OUT/'reader-inputs-before.json').write_text(json.dumps(inputs,indent=2),encoding='utf-8')
checks={}
for skill,version in [('course-study-guide-builder','2.1.0-rc.38'),('course-quality-gate','1.0.25')]:
    cmd=[sys.executable,str(RELEASE/'tools/release_skill.py'),'--publisher-root',str(RELEASE),'--skill-name',skill,'--version',version,'--install-root','C:/Users/vital/.codex/skills','--check']
    process=subprocess.run(cmd,capture_output=True,text=True,encoding='utf-8')
    assert process.returncode==0,process.stderr
    checks[skill]=json.loads(process.stdout)
pub=ROOT/'publisher-lock.yaml'; data=yaml.safe_load(pub.read_text(encoding='utf-8'))
data['publisher'].update(version='0.8.23',source='https://github.com/vitalyrue/study-guide-publisher.git',git_tag='v0.8.23',git_head=COMMIT,working_tree_dirty=False)
pub.write_text(yaml.safe_dump(data,sort_keys=False,allow_unicode=True),encoding='utf-8',newline='\n')
skillfile=ROOT/'skill-lock.yaml'; data=yaml.safe_load(skillfile.read_text(encoding='utf-8'))
for name,version in [('course-study-guide-builder','2.1.0-rc.38'),('course-quality-gate','1.0.25'),('course-diagram-builder','1.6.1')]:
    manifest=RELEASE/'releases'/f'{name}-{version}-manifest.json'
    data['skills'][name]={'version':version,'release_manifest_sha256':sha(manifest)}
data['skills']['course-study-guide-builder'].update(contract_schema=4,publisher_contract='book_runtime-guide-project-v4')
data['skills']['course-quality-gate'].update(diagnostic_schema=1)
skillfile.write_text(yaml.safe_dump(data,sort_keys=False,allow_unicode=True),encoding='utf-8',newline='\n')
config=ROOT/'.vale.ini'
assert not config.exists(),'Do not overwrite an existing project prose profile'
original=(SHARED/'.vale.ini').read_text(encoding='utf-8-sig')
assert 'StylesPath = styles' in original
config.write_text('# Shared NBIS technical-course prose profile. Rules and severities retained.\n'+original.replace('StylesPath = styles','StylesPath = C:/dev/NBIS/performance-engineering-course/styles'),encoding='utf-8',newline='\n')
receipt={'checked_at':datetime.datetime.now().astimezone().isoformat(),'upstream_commit':COMMIT,'upstream_tag':'v0.8.23','runtime_root':str(RELEASE),'installed_package_checks':checks,'installation_action':'No reinstall needed: installed teaching and quality packages already match latest released manifests.','book_diagram_package':str(RELEASE/'skills/course-diagram-builder'),'global_diagram':'Existing local1.6.2 retained unchanged; guide uses released1.6.1 directly.','vale_profile':{'source':str(SHARED/'.vale.ini'),'source_sha256':sha(SHARED/'.vale.ini'),'project_sha256':sha(config),'styles':str(SHARED/'styles'),'rules':{str(p.relative_to(SHARED/'styles')).replace('\\','/'):sha(p) for p in (SHARED/'styles').rglob('*') if p.is_file()},'change':'Only StylesPath made absolute; no rule or severity changes. No packages downloaded.'},'reader_inputs_before':inputs}
(OUT/'alignment-receipt.json').write_text(json.dumps(receipt,indent=2),encoding='utf-8')
print('Guide pins aligned; existing NBIS Vale profile connected; package checks saved.')

from pathlib import Path
import json
p=Path(__file__).resolve().parent
old=json.loads((p/'concept-index-before-table-format.json').read_text(encoding='utf-8'))
new=json.loads((p/'concept-index-tables.json').read_text(encoding='utf-8'))
judgments=json.loads((p/'concept-judgments-merged.json').read_text(encoding='utf-8'))
old_by_id={x['id']:x for x in old['passages']};mapping={}
def locate(pid):
 if pid in mapping:return mapping[pid]
 src=old_by_id[pid]
 candidates=[x for x in new['passages'] if x['chapter_id']==src['chapter_id'] and x['section_id']==src['section_id'] and x['kind']==src['kind'] and x['text']==src['text']]
 assert len(candidates)==1,(pid,len(candidates))
 mapping[pid]=candidates[0]['id'];return mapping[pid]
for relation in judgments['relations']:relation['passage_id']=locate(relation['passage_id'])
for group in judgments.get('teaching_sets',[]):group['passage_ids']=[locate(x) for x in group['passage_ids']]
judgments['formatting_reuse']='table-format-reuse.json preserves all reviewed table cells. rebind-locators.json maps every indexed reviewed passage to identical text in the same chapter and section after table formatting.'
(p/'concept-judgments-final.json').write_text(json.dumps(judgments,indent=2,ensure_ascii=False),encoding='utf-8')
(p/'rebind-locators.json').write_text(json.dumps({'all_reviewed_passage_text_unchanged':True,'mapping':mapping},indent=2),encoding='utf-8')
print('Rebound',len(mapping),'identical passages after table formatting.')

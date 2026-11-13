from pathlib import Path
from datetime import datetime
import json,sys
out=Path(__file__).resolve().parent
now=datetime.now().astimezone();start=datetime.fromisoformat('2026-10-24T20:17:28.7375959+03:00')
path=out/'checkpoints.jsonl'
previous=datetime.fromisoformat(json.loads(path.read_text(encoding='utf-8').splitlines()[-1])['at']) if path.exists() else start
row={'at':now.isoformat(),'wall_elapsed_seconds':round((now-start).total_seconds(),1),'since_previous_checkpoint_seconds':round((now-previous).total_seconds(),1),'awake_execution_time':'unverified','summary':' '.join(sys.argv[1:])}
with path.open('a',encoding='utf-8') as f:f.write(json.dumps(row,ensure_ascii=False)+'\n')
with (out/'RUN.md').open('a',encoding='utf-8') as f:f.write(f"\n{row['at']}: {row['summary']} Wall elapsed {row['wall_elapsed_seconds']}s; checkpoint delta {row['since_previous_checkpoint_seconds']}s; awake unverified.\n")
print(json.dumps(row,ensure_ascii=False))

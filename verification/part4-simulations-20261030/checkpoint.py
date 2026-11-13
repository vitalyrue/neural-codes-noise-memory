from pathlib import Path
from datetime import datetime,timezone
import json,sys
p=Path(__file__).with_name('STATE.json');d=json.loads(p.read_text(encoding='utf-8'))
now=datetime.now(timezone.utc);start=datetime.fromisoformat(d['started_at']);prev=datetime.fromisoformat(d['checkpoint_at'])
entry=dict(at=now.isoformat(),status=sys.argv[1],wall_elapsed_seconds=round((now-start).total_seconds()),since_previous_saved_checkpoint_seconds=round((now-prev).total_seconds()),awake_execution='unverified')
d.update(checkpoint_at=entry['at'],status=entry['status']);d.setdefault('checkpoints',[]).append(entry)
p.write_text(json.dumps(d,indent=2),encoding='utf-8');print(json.dumps(entry))

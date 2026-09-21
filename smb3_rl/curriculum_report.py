"""Separate practice success from complete-level success in saved training traces."""
import gzip
import json
from collections import defaultdict
from .common import write_json

def build(run):
    groups=defaultdict(lambda:{'completed_episodes':0,'clears':0,'deaths':0,'frame_limits':0,'max_progress_pixels':0})
    for path in sorted((run/'logs').glob('*training-trace.jsonl.gz')):
        with gzip.open(path,'rt') as stream:
            for line in stream:
                row=json.loads(line)
                if not (row.get('terminated') or row.get('truncated')):continue
                out=groups[row['start_condition']]
                out['completed_episodes']+=1
                out['clears']+=int(row['level_complete'])
                out['deaths']+=int(row['death'])
                out['frame_limits']+=int(row['termination_reason']=='frame_limit')
                out['max_progress_pixels']=max(out['max_progress_pixels'],row['progress_pixels'])
    write_json(run/'curriculum-outcomes.json',dict(groups))
    lines=['# Training outcomes by starting condition','','These are on-policy training episodes, not acceptance trials. Practice clears are not full-level wins. Progress is measured from each episode’s own start. Incomplete trailing episodes are excluded.','','| Start condition | Completed episodes | Clears | Deaths | Frame limits | Furthest progress (pixels) |','|---|---:|---:|---:|---:|---:|']
    for name,g in groups.items():lines.append('| '+name+' | '+' | '.join(str(v) for v in g.values())+' |')
    (run/'CURRICULUM.md').write_text('\n'.join(lines)+'\n')

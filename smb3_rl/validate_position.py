"""Integration regressions for the isolated page-sample quarantine."""
import gzip,json
from .common import ROOT,read_json,write_json,digest
from .validate import run
from .validate_recovery import extra_checks as recovery_checks

def extra_checks(env,out,checks,report):
    recovery_checks(env,out,checks,report)
    source=ROOT/'sessions/2026-09-21-smb3-overnight-curriculum/logs/05-training-trace.jsonl.gz'
    episodes=[];current=[]
    with gzip.open(source,'rt') as stream:
        for line in stream:
            r=json.loads(line);current.append(r)
            if r.get('terminated') or r.get('truncated'):
                if r['start_condition']=='full_level' and (r['level_complete'] or r['telemetry_invalid']):episodes.append(current)
                current=[]
    results=[]
    for rows in episodes:
        env.reset();matched=True;rewards=[]
        for row in rows:
            _,reward,t,tr,info=env.step(row['action']);rewards.append(reward)
            if row is not rows[-1]:matched &= info['x_pos']==row['x_pos'] and info['frames']==row['frames']
            if t or tr:break
        if rows[-1]['level_complete']:
            checks[f'archived_clear_{len(results)+1}']=matched and info['level_complete'] and not info['telemetry_invalid']
        else:
            checks['failure_prefix_unchanged']=matched
            checks['single_frame_anomaly_quarantined']=not t and not tr and info['position_quarantine_count']>=1
            before=env.progress.maximum
            for _ in range(400):
                _,reward,t,tr,info=env.step(1)
                if t or tr:break
            checks['continuation_has_no_false_progress']=env.progress.maximum==before and not info['level_complete']
            checks['continued_episode_ends_at_frame_limit']=tr and info['termination_reason']=='frame_limit' and not info['telemetry_invalid']
        results.append(info)
    report['archived_replay_results']=results
    report['source_trace_sha256']=digest(source)
    report['position_guard_sha256']=digest(ROOT/'smb3_rl/position.py')
    write_json(out/'position-replay-results.json',results)

if __name__=='__main__':run('configs/smb3-1-1-position.json','sessions/2026-09-21-position-validation',extra_checks)

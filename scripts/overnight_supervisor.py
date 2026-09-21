"""Unattended six-hour supervisor: no input, bounded children, job-bound wake assertion."""
import argparse
import json
import os
from pathlib import Path
import signal
import subprocess
import sys
import time

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from smb3_rl.common import write_json,now

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--session',required=True)
    p.add_argument('--deadline-epoch',required=True,type=float)
    a=p.parse_args()
    state=ROOT/'.cache'/f'{a.session}-supervisor.json'
    record={'started':now(),'pid':os.getpid(),'deadline_epoch':a.deadline_epoch,'status':'starting'}
    write_json(state,record)
    stopped=[False]
    for sig in (signal.SIGINT,signal.SIGTERM):
        signal.signal(sig,lambda *_:stopped.__setitem__(0,True))
    wake=subprocess.Popen(['/usr/bin/caffeinate','-is','-w',str(os.getpid())],stdin=subprocess.DEVNULL)
    cmd=[sys.executable,'-m','smb3_rl.session','--config','configs/smb3-1-1-recovery.json',
         '--session',a.session,'--active-minutes','330','--curriculum',
         '--deadline-epoch',str(a.deadline_epoch-120),'--allow-source-change',
         '--resume',str(ROOT/'sessions/2026-09-20-smb3-recovery-session-02/checkpoints/final.zip'),
         '--budget-note','User approved six hours total overnight, including setup and evaluation. Curriculum only; unchanged rewards; no further training authorized.',
         '--eval-seconds','240']
    child=None
    try:
        child=subprocess.Popen(cmd,cwd=ROOT,stdin=subprocess.DEVNULL,start_new_session=True)
        record.update(status='running',training_pid=child.pid,caffeinate_pid=wake.pid)
        write_json(state,record)
        while child.poll() is None and time.time()<a.deadline_epoch-90 and not stopped[0]:
            if wake.poll() is not None:
                raise RuntimeError('Sleep prevention exited unexpectedly')
            time.sleep(1)
        if child.poll() is None:
            record['stop_reason']='stop_request' if stopped[0] else 'wall_time_limit'
            child.send_signal(signal.SIGTERM)
            try:child.wait(timeout=45)
            except subprocess.TimeoutExpired:
                os.killpg(child.pid,signal.SIGKILL);child.wait()
                record['forced_stop']=True
        record.update(status='completed' if child.returncode==0 else 'failed',exit_code=child.returncode,finished=now())
    except BaseException as exc:
        record.update(status='failed',error=repr(exc),finished=now())
        if child is not None and child.poll() is None:
            child.send_signal(signal.SIGTERM)
            try:child.wait(timeout=30)
            except subprocess.TimeoutExpired:os.killpg(child.pid,signal.SIGKILL);child.wait()
    finally:
        write_json(state,record)
        wake.terminate()
        wake.wait(timeout=5)

if __name__=='__main__':main()

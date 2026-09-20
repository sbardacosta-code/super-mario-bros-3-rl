import numpy as np
from smb3_rl.common import ROOT,read_json
from smb3_rl.env import MarioEnv


def test_recovery_changes_only_actions_and_protocol_metadata():
    old=read_json(ROOT/'configs/smb3-1-1.json');new=read_json(ROOT/'configs/smb3-1-1-recovery.json')
    assert new['actions'][:5]==old['actions']
    assert new['actions'][5:]==[['left'],['left','A']]
    for key in old:
        if key not in ('actions','action_names','protocol','validation_file'):assert new[key]==old[key]


def test_left_moves_back_without_resetting_high_water():
    c=read_json(ROOT/'configs/smb3-1-1-recovery.json');e=MarioEnv(c,validate=False)
    try:
        first,_=e.reset(seed=123)
        for _ in range(8):e.step(1)
        start=e.info['x_pos'];maximum=e.progress.maximum
        for _ in range(16):o,r,t,tr,i=e.step(5)
        assert i['x_pos']<start and i['max_x']>=maximum
        assert not t and not tr and o.shape==(4,84,84)
        again,_=e.reset(seed=123);assert np.array_equal(first,again)
    finally:e.close()

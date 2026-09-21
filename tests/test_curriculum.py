import numpy as np
from smb3_rl.common import ROOT,read_json
from smb3_rl.curriculum import CurriculumEnv

def test_curriculum_resets_accounting_and_verified_goal():
    env=CurriculumEnv(read_json(ROOT/'configs/smb3-1-1-position.json'))
    try:
        for condition,offset,x in [('full_level',0,24),('approach_goal',350,2585),('missed_goal',400,2792)]:
            old_frames=env.total_frames
            first,info=env.reset(seed=123,options={'start_condition':condition})
            second,again=env.reset(seed=123,options={'start_condition':condition})
            assert np.array_equal(first,second)
            assert info['x_pos']==again['x_pos']==x
            assert info['progress_pixels']==info['frames']==info['decisions']==0
            assert env.total_frames==old_frames
            assert info['scripted_setup_frames']==offset*4
            for action in env.prefix[offset:]:
                _,_,term,trunc,out=env.step(action)
                if term or trunc:break
            assert out['level_complete'] and not out['telemetry_invalid']
            assert out['start_condition']==condition
            assert env.total_frames-old_frames==out['frames']
    finally:env.close()

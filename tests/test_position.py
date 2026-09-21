from smb3_rl.position import PositionGuard
from smb3_rl.env import HighWater

def test_isolated_page_error_cannot_earn_progress():
    for suspect in (1588,2100):
        g=PositionGuard(1843);h=HighWater(1843)
        x,ok,bad=g.observe(suspect)
        assert not ok and not bad and h.update(x,ok)==0
        x,ok,bad=g.observe(1843)
        assert ok and not bad and h.update(x,ok)==0
        assert h.maximum==1843

def test_persistent_or_unrelated_jump_is_rejected():
    for sequence in [(1588,1588),(1588,2100),(2200,)]:
        g=PositionGuard(1843)
        for x in sequence:_,_,bad=g.observe(x)
        assert bad

def test_normal_page_crossing_and_backtracking_stay_valid():
    g=PositionGuard(250);h=HighWater(250)
    for x in [254,258,254,250,254,258]*20:
        value,ok,bad=g.observe(x)
        assert ok and not bad
        h.update(value,ok)
    assert h.maximum==258 and g.samples_quarantined==0

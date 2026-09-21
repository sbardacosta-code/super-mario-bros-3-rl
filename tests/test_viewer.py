import importlib.util
from pathlib import Path
from smb3_rl.common import ROOT


def test_viewer_lists_archived_samples_without_altering_session():
    spec=importlib.util.spec_from_file_location('viewer',ROOT/'scripts/watch_training.py')
    module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
    session=ROOT/'sessions/2026-09-20-smb3-recovery-pilot';before=(session/'manifest.json').read_bytes()
    m,progress,samples=module.snapshot(session)
    assert m['status']=='completed' and len(samples)==30
    assert {s['stage'] for s in samples}=={'00-untrained','01-stage','final'}
    assert all(s['path'].is_file() and s['part'] in ('beginning','ending') for s in samples)
    assert before==(session/'manifest.json').read_bytes()

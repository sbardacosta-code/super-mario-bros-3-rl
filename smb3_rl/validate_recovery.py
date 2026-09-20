"""Validate seven-action controls and a reproducible missed-card recovery."""
import argparse
import json
from PIL import Image, ImageDraw
from .common import ROOT, read_json, write_json
from .validate import run


def extra_checks(env, out, checks, report):
    controls={}
    for action in (0,5,6):
        env.reset()
        for _ in range(8):env.step(1)
        start=env.info['x_pos'];rows=[];frames=[];previous=env.progress.maximum
        for _ in range(16):
            _,reward,term,trunc,info=env.step(action)
            rows.append({'action':action,'reward':reward,**info});frames.append(Image.fromarray(env.render()))
            if term or trunc:break
        controls[str(action)]={'start_x':start,'end_x':info['x_pos'],'min_y':min(r['y_pos'] for r in rows),'start_high_water':previous,'end_high_water':env.progress.maximum}
        write_json(out/f'recovery-control-{action}.json',rows)
        frames[0].save(out/f'recovery-control-{action}.gif',save_all=True,append_images=frames[1:],duration=67,loop=0)
    checks['left_reduces_world_x']=controls['5']['end_x']<controls['5']['start_x']
    checks['left_jump_moves_left_and_up']=controls['6']['end_x']<controls['6']['start_x'] and controls['6']['min_y']<controls['5']['min_y']
    report['recovery_controls']=controls
    # Backtracking/revisiting must not earn additional positive progress reward.
    env.reset()
    for _ in range(8):env.step(1)
    revisit=[]
    for a in [5]*12+[1]*12:
        maximum=env.progress.maximum
        _,reward,t,tr,info=env.step(a)
        if info['max_x']==maximum:revisit.append(reward)
        if t or tr:break
    checks['real_backtracking_has_no_positive_reward']=bool(revisit) and all(r<=0 for r in revisit)
    actions=read_json(ROOT/'.cache/recovery-controller-actions.json')
    env.reset();rows=[];frames=[]
    for a in actions:
        _,reward,t,tr,info=env.step(a);rows.append({'action':a,'reward':reward,**info});frames.append(Image.fromarray(env.render()))
        if t or tr:break
    write_json(out/'recovery-actions.json',actions)
    write_json(out/'recovery-trace.json',rows)
    checks['recovery_starts_from_missed_card_boundary']=rows[399]['x_pos']==2792 and not rows[399]['level_complete']
    checks['return_left_after_boundary']=any(r['x_pos']<2700 and r['in_level'] for r in rows[400:])
    checks['recovery_collects_card_and_clears']=info['level_complete'] and not info['death'] and t and not tr
    report['recovery_outcome']=info
    clip=frames[350:]
    clip[0].save(out/'recovery-ending.gif',save_all=True,append_images=clip[1:],duration=67,loop=0)
    indices=list(range(350,len(frames),max(1,(len(frames)-350)//11)))[:11]+[len(frames)-1]
    sheet=Image.new('RGB',(1024,260*((len(indices)+3)//4)),'white');draw=ImageDraw.Draw(sheet)
    for j,i in enumerate(indices):
        x=j%4*256;y=j//4*260;sheet.paste(frames[i],(x,y));draw.text((x+3,y+241),f'Decision {i+1}',fill='black')
    sheet.save(out/'recovery-contact-sheet.png')
    report['recovery_note']='Scripted integration test: replays 400 decisions of an archived failed policy trial, then tests leftward recovery. These actions are never supplied as PPO demonstrations.'

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--config',default='configs/smb3-1-1-recovery.json')
    p.add_argument('--output',default='sessions/2026-09-20-smb3-recovery-validation-02')
    args=p.parse_args();run(args.config,args.output,extra_checks)

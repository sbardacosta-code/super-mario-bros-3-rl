"""Floating checkpoint GIF viewer with live counters; never controls training."""
import argparse
import json
from pathlib import Path
import time


def snapshot(session):
    """Read atomically written metadata; list only finished, recorded trials."""
    m=json.loads((session/'manifest.json').read_text())
    progress_path=session/'progress.json'
    progress=json.loads(progress_path.read_text()) if progress_path.exists() else {}
    samples=[]
    for stage in m['stages']:
        p=session/stage['id']/'evaluation.json'
        if not p.exists():continue
        e=json.loads(p.read_text())
        for ep in e.get('episodes',[]):
            for media in ep.get('media',[]):
                path=p.parent/media
                if path.exists():samples.append({'stage':stage['id'],'minutes':stage['training_seconds']/60,
                    'seed':ep['seed'],'part':Path(media).stem.split('-')[-1],'path':path,
                    'outcome':ep.get('termination_reason','unknown'),'progress':ep['progress_pixels']})
    return m,progress,samples


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('session',type=Path);args=p.parse_args()
    session=args.session.resolve();snapshot(session)
    import tkinter as tk
    from tkinter import ttk
    from PIL import Image,ImageTk,ImageSequence
    root=tk.Tk();root.title('Super Mario Bros. 3 — training viewer');root.configure(bg='#101522')
    root.geometry('590x750+70+50');root.resizable(False,False);root.attributes('-topmost',True)
    tk.Label(root,text='Super Mario Bros. 3',font=('Helvetica',20,'bold'),fg='#ffe260',bg='#101522').pack(pady=(12,2))
    tk.Label(root,text='Recorded checkpoint samples · live training counters',fg='#b9c4d6',bg='#101522').pack()
    live=tk.StringVar(value='Waiting for training metadata…');tk.Label(root,textvariable=live,fg='white',bg='#101522',justify='center').pack(pady=8)
    choice=ttk.Combobox(root,state='readonly',width=65);choice.pack(pady=3)
    caption=tk.StringVar();tk.Label(root,textvariable=caption,fg='#b9c4d6',bg='#101522').pack(pady=5)
    screen=tk.Label(root,bg='black',width=512,height=480);screen.pack()
    state={'samples':[],'frames':[],'delays':[],'index':0,'paused':False,'loops':0,'selected':None,'latest_stage':None}
    follow=tk.BooleanVar(value=True);top=tk.BooleanVar(value=True)
    def select(sample):
        frames=[];delays=[]
        with Image.open(sample['path']) as gif:
            for frame in ImageSequence.Iterator(gif):
                frames.append(ImageTk.PhotoImage(frame.convert('RGB').resize((512,480),Image.Resampling.NEAREST),master=root))
                delays.append(max(20,frame.info.get('duration',67)))
        state.update(frames=frames,delays=delays,index=0,paused=False,loops=0,selected=str(sample['path']))
        pause.configure(text='Pause')
        caption.set(f"{sample['minutes']:.2f} active min at save · {sample['progress']} pixels · {sample['outcome']}")
    def chosen(_=None):
        i=choice.current()
        if i>=0:select(state['samples'][i])
    choice.bind('<<ComboboxSelected>>',chosen)
    def toggle():
        if state['loops']>=2:state.update(index=0,loops=0)
        state['paused']=not state['paused'];pause.configure(text='Play' if state['paused'] else 'Pause')
    def replay():state.update(index=0,loops=0,paused=False);pause.configure(text='Pause')
    controls=tk.Frame(root,bg='#101522');controls.pack(pady=6)
    pause=tk.Button(controls,text='Pause',command=toggle);pause.pack(side='left',padx=5)
    tk.Button(controls,text='Replay',command=replay).pack(side='left',padx=5)
    tk.Checkbutton(controls,text='Follow new checkpoints',variable=follow,bg='#101522',fg='white',selectcolor='#101522').pack(side='left')
    tk.Checkbutton(root,text='Keep above other windows',variable=top,command=lambda:root.attributes('-topmost',top.get()),bg='#101522',fg='white',selectcolor='#101522').pack()
    tk.Label(root,text='Plays twice. Closing this window does not stop training. Esc to close.',fg='#b9c4d6',bg='#101522',font=('Helvetica',10)).pack(pady=5)
    def tick():
        delay=100
        if state['frames']:
            i=state['index'];screen.configure(image=state['frames'][i]);delay=state['delays'][i]
            if not state['paused']:
                if i==len(state['frames'])-1:
                    state['loops']+=1
                    if state['loops']>=2:state['paused']=True;pause.configure(text='Play again')
                    else:state['index']=0
                else:state['index']+=1
        root.after(delay,tick)
    def poll():
        try:
            m,progress,samples=snapshot(session)
            decisions=max(progress.get('model_decisions',0),max((s['total_model_decisions'] for s in m['stages']),default=0))
            age=max(0,time.time()-(session/'progress.json').stat().st_mtime) if (session/'progress.json').exists() else None
            status=m['status'];age_text=f' · counter update {age:.0f}s ago' if status=='running' and age is not None else ''
            live.set(f"Session: {status} · {decisions:,} cumulative model decisions{age_text}\nSaved active training: {m['training_seconds']/60:.2f} min · checkpoint clips update after evaluation")
            labels=[f"{s['stage']} · seed {s['seed']} · {s['part']}" for s in samples]
            state['samples']=samples;choice['values']=labels
            if samples:
                latest=samples[-1]['stage']
                if state['selected'] is None or (follow.get() and latest!=state['latest_stage']):
                    wanted=next((s for s in samples if s['stage']==latest and s['seed']==m['config']['evaluation_seeds'][0] and s['part']=='beginning'),samples[-1])
                    choice.current(samples.index(wanted));select(wanted)
                state['latest_stage']=latest
        except (OSError,ValueError,KeyError) as exc:live.set(f'Metadata temporarily unavailable: {type(exc).__name__}')
        root.after(3000,poll)
    root.bind('<Escape>',lambda _:root.destroy());root.lift();poll();tick();root.mainloop()

if __name__=='__main__':main()

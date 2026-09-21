from smb3_rl.common import ROOT,read_json,write_json
from smb3_rl.env import MarioEnv
from PIL import Image,ImageDraw
from collections import deque
import gzip,json
s=ROOT/'sessions/2026-09-21-smb3-overnight-curriculum';out=s/'review/failure-replays';out.mkdir(exist_ok=True)
episodes=[];current=[]
with gzip.open(s/'logs/05-training-trace.jsonl.gz','rt') as f:
 for line in f:
  r=json.loads(line);current.append(r)
  if r.get('terminated') or r.get('truncated'):
   if r['start_condition']=='full_level' and (r['level_complete'] or r['telemetry_invalid']):episodes.append(current)
   current=[]
e=MarioEnv(read_json(s/'config.json'));results=[]
for n,rows in enumerate(episodes):
 label=f'full-start-clear-{n+1}' if rows[-1]['level_complete'] else 'telemetry-failure'
 obs,info=e.reset(seed=123);frames=deque(maxlen=150);begin=[];match=True
 for r in rows:
  obs,reward,t,tr,info=e.step(r['action']);match=match and info['x_pos']==r['x_pos'] and info['frames']==r['frames']
  im=Image.fromarray(e.render());frames.append(im)
  if len(begin)<150:begin.append(im)
  if t or tr:break
 for suffix,seq in [('beginning',begin),('ending',list(frames))]:
  seq[0].save(out/f'{label}-{suffix}.gif',save_all=True,append_images=seq[1:],duration=67,loop=0)
 sheet=Image.new('RGB',(1024,264),'white');d=ImageDraw.Draw(sheet);seq=list(frames)
 for col,i in enumerate([0,len(seq)//3,2*len(seq)//3,len(seq)-1]):
  sheet.paste(seq[i],(256*col,24));d.text((256*col,4),f'{label}: ending sample {i}',fill='black')
 sheet.save(out/f'{label}.png')
 results.append({'label':label,'matched_position_and_frame_trace':match,'source_decision_start':rows[0]['model_decision'],'source_decision_end':rows[-1]['model_decision'],'source_trace':'../../logs/05-training-trace.jsonl.gz','final':info})
 print(label,match,{k:info[k] for k in ['x_pos','y_pos','frames','level_complete','telemetry_invalid']})
e.close();write_json(out/'replay-results.json',results)

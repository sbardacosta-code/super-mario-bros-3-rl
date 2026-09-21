"""Training-only reset curriculum. Evaluation always uses the normal level start."""
import time
import numpy as np
from .common import ROOT, read_json
from .env import MarioEnv, HighWater

class CurriculumEnv(MarioEnv):
    def __init__(self, config):
        super().__init__(config)
        self.prefix = read_json(ROOT/'sessions/2026-09-20-smb3-recovery-validation-02/recovery-actions.json')
        self.practice_probability = .75
        self.setup_frames = self.setup_decisions = self.practice_resets = self.full_resets = 0
        self.setup_seconds = 0.0
        self.start_condition = 'full_level'
        self.setting_up = False

    def reset(self, *, seed=None, options=None):
        obs, info = super().reset(seed=seed, options=options)
        forced = (options or {}).get('start_condition')
        choice = forced or ('practice' if self.np_random.random() < self.practice_probability else 'full_level')
        if choice == 'practice':
            choice = str(self.np_random.choice(['approach_goal','missed_goal']))
        if choice not in ('full_level','approach_goal','missed_goal'):
            raise ValueError('Unknown curriculum start')
        self.start_condition = choice
        self.episode_setup_frames = 0
        if choice != 'full_level':
            before = self.total_frames, self.total_decisions, self.simulation_seconds
            tick = time.perf_counter()
            self.setting_up = True
            try:
                for action in self.prefix[:350 if choice == 'approach_goal' else 400]:
                    obs, _, term, trunc, info = super().step(action)
                    if term or trunc:
                        raise RuntimeError('Curriculum prefix ended the episode')
            finally:
                self.setting_up = False
            self.episode_setup_frames = self.total_frames-before[0]
            self.setup_frames += self.episode_setup_frames
            self.setup_decisions += self.total_decisions-before[1]
            self.setup_seconds += time.perf_counter()-tick
            self.total_frames, self.total_decisions, self.simulation_seconds = before
            self.frames = self.decisions = 0
            self.progress = HighWater(info['x_pos'])
            self.last_x = int(info['x_pos'])
            info = self.metrics(info,0,False,False)
            self.practice_resets += 1
        else:
            self.full_resets += 1
        self.info = {**info, 'start_condition':choice, 'scripted_setup_frames':self.episode_setup_frames}
        return obs, self.info

    def step(self, action):
        obs,reward,term,trunc,info = super().step(action)
        info.update(start_condition=self.start_condition, scripted_setup_frames=self.episode_setup_frames)
        return obs,reward,term,trunc,info

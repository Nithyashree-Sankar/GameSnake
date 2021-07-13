import gym
from cooooooonfff.py import taskk

import matplotlib.pyplot as plt

from gym import spaces
import numpy as np
import random

s = spaces.Box(-100,100,shape=(3,3))
print(s)

class DVFS(gym.Env): #inheriting methods and properties from openai gym environment
    def __init__(self):
        super(DVFS,self).__init__()
        self.done = False
        self.statespace = spaces.Box(-100,100,shape=(3,)) #ds,uti,temp
        self.action_space = spaces.Discrete(5) #0,1,2,3,4
        self.scheduler = [ccedf,rm,hg,hj,hj]
        #reading/setting the starting state
        self.state = 100 #current freq()assumption
    def _take_action(self,action):
        curr_action = random.uniform(self.action_space)
        return curr_action

    def step(self,action):
        #self._take_action(action)
        #reward = +1 if self.cp
        # 0-1 ---> dec the freq,1-1--->reaving as such,2-1--->inc the curr freq
         #applying action to our curr state
        self.scheduler[action]
        if self.cpu_usage < 50 and self.curr_freq < 50:
            reward = +1
        else:
            reward = -1
        return self.state,reward
    def reset(self):
        self.state = 100
        return self.state

            

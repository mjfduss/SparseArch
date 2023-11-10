import gymnasium as gym
import numpy as np
from gymnasium import spaces
from py_bridge_designer.bridge import Bridge
from py_bridge_designer.parameters import Section


class BridgeEnv(gym.Env):
     def __init__(self):
        super().__init__()
        self.bridge = Bridge()



# Testing code
env = BridgeEnv()
env.bridge.add_member((3,4),(1,2),0,0,3)

for member in env.bridge.members:
   print(member.length)
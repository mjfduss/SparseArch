import gymnasium as gym
import numpy as np
from gymnasium import spaces
from py_bridge_designer.bridge import Bridge


class BridgeEnv(gym.Env):
    def __init__(self, load_scenario_index: int):
        super().__init__()
        self.bridge = Bridge(load_scenario_index)


# Testing code

"""
NUM_LOAD_SCENARIOS = 392
x_values = []
y_values = []
for i in range(NUM_LOAD_SCENARIOS):

    env = BridgeEnv(i)
    x_values.append(env.bridge.load_scenario.grid_size)
    # y_values.append(joint.y)

max_x = max(x_values)
min_x = min(x_values)
max_y = max(y_values)
min_y = min(y_values)

print('max_x', max_x)
print('min_x', min_x)
print('max_y', max_y)
print('min_y', min_y)

# env.bridge.add_member(3, 4, 1, 2, 0, 0, 3)
print(env.bridge.load_scenario.desc.id)
print(env.bridge.load_scenario.over_meters)
print(env.bridge.load_scenario.under_meters)
print(env.bridge.joint_coords.keys())
"""


# Max Y is 32
# Min Y is -96
# Total Y size is 128

# Max X is 208
# Min X is -32
# Total X size is 240

# So Adjecency matrix (input) size is 240x128

# When the Bridge converts from Adj Matrix to real x,y values
# it will need to subtract 32 from X and 96 from Y

# <DONE!> Will need also to reject X and Y values outside of the Load Scenario Min and Max X

# Could also try to figure out how to reject X and Y values that are "in the ground" (referencing the Bridge Designer GUI)

# Could use the Max joints and members as rejection points,
# or could let there be as many joints and members as desired,
# since these numbers were taken from the C library
# not sure whether they are arbitrary or not
# define MAX_JOINTS 100
# define MAX_MEMBERS 200

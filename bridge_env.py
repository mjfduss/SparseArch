import gymnasium as gym
import numpy as np
from gymnasium import spaces
from py_bridge_designer.bridge import Bridge


class BridgeEnv(gym.Env):
    def __init__(self, load_scenario_index=0, seed=42):
        super().__init__()
        self.bridge = Bridge(load_scenario_index)

        # Define action space
        max_x_action = self.bridge.load_scenario.max_x + 1
        max_y_action = self.bridge.max_y + 1
        min_x_action_value = self.bridge.load_scenario.min_x
        min_y_action_value = self.bridge.min_y

        self.action_space = spaces.MultiDiscrete(
            nvec=[max_x_action, max_y_action, max_x_action, max_y_action, self.bridge.max_material_types,
                  self.bridge.max_section_types, self.bridge.max_section_size],
            start=[min_x_action_value, min_y_action_value,
                   min_x_action_value, min_y_action_value, 0, 0, 0],
            dtype=np.int16,
            seed=seed)

        # Define observation space
        self.observation_space = spaces.MultiBinary(
            n=[2, self.bridge.matrix_y, self.bridge.matrix_x],
            seed=seed)


# Testing code
env = BridgeEnv()
print("action space shape", env.action_space.shape)
print("action space sample", env.action_space.sample())
print("action space sample", env.action_space.sample())
print("action space sample", env.action_space.sample())
print("action space sample", env.action_space.sample())
print("action space sample", env.action_space.sample())
print("observation space shape", env.observation_space.shape)
print("observation space sample", env.observation_space.sample())
env.bridge.analyze()
"""
member_added = env.bridge.add_member(3, 4, 1, 2, 0, 0, 3)
print("member_added:", member_added)
print(env.bridge.n_joints)
print(len(env.bridge.joints))
print(len(env.bridge.joint_coords))
# print(env.bridge.joint_coords.keys())
print(np.sum(env.bridge.get_state()[0]))

NUM_LOAD_SCENARIOS = 392
# x_values = []
# y_values = []
scenarios_to_check = [7, 105, 203, 301]
# for i in range(NUM_LOAD_SCENARIOS):
for i in scenarios_to_check:
    env = BridgeEnv(i)

    print("Load Scenario:", i)
    print("n_joints:", env.bridge.n_joints)
    print("length of joints list:", len(env.bridge.joints))
    printout = "joints list:"
    for joint in env.bridge.joints:
        printout += f" ({joint.x}, {joint.y}),"
    print(printout)
    print("length of joint_coords:", len(env.bridge.joint_coords))
    print("joint_coords:", env.bridge.joint_coords.keys())
    print("state:", np.sum(env.bridge.get_state()[0]))
    print("support type:", env.bridge.load_scenario.support_type)
    print("under grids:", env.bridge.load_scenario.under_grids)
    print("id:", env.bridge.load_scenario.desc.id)
    print("-------------------")

# x_values.append(env.bridge.load_scenario.grid_size)
# y_values.append(joint.y)

# max_x = max(x_values)
# min_x = min(x_values)
# max_y = max(y_values)
# min_y = min(y_values)

# print('max_x', max_x)
# print('min_x', min_x)
# print('max_y', max_y)
# print('min_y', min_y)


print(env.bridge.load_scenario.desc.id)
print(env.bridge.load_scenario.over_meters)
print(env.bridge.load_scenario.under_meters)
print(env.bridge.joint_coords.keys())
"""

# <DONE!>
# Max Y is 32
# Min Y is -96
# Total Y size is 128
# <DONE!>
# Max X is 208
# Min X is -32
# Total X size is 240

# <DONE!> Max number of Joints from C library is defined as 100, will use 128 as max

# <DONE!> When the Bridge Adj Matrix to real x,y values
#         subtract 32 from X and 96 from Y

# <DONE!> Will need also to reject X and Y values outside of the Load Scenario Min and Max X

# Could also try to figure out how to reject X and Y values that are "in the ground" (referencing the Bridge Designer GUI)

# Apply Convolution layers to the input, since like an image, there will be many zeros in the state tensor

from gym.envs.registration import register

register(
    id='SparsePendulum-v0',
    entry_point='sparse_pendulum.envs:SparsePendulumEnv',
    kwargs={
        'reward_angle_limit':5.0,
        'reward_speed_limit':2.0
    }

)

from envs import *

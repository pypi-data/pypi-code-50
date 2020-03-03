from gym.envs.classic_control.pendulum import PendulumEnv, angle_normalize
import numpy as np

class SparsePendulumEnv(PendulumEnv):

    def __init__(self, reward_angle_limit, reward_speed_limit):
        super().__init__()
        self.reward_speed_limit = reward_speed_limit
        self.reward_angle_limit = reward_angle_limit

    def reward(self, th, thdot, u):
        angle = np.degrees(angle_normalize(th))
        if self.check_angle(angle) and self.check_speed(thdot):
            return 1

        return 0

    def check_angle(self, angle):
        return (angle >= -self.reward_angle_limit) and (angle <= self.reward_angle_limit)

    def check_speed(self, thdot):
        return (thdot >= -self.reward_speed_limit) and (thdot <= self.reward_speed_limit)

    def step(self, u):
        th, thdot = self.state # th := theta

        g = self.g
        m = self.m
        l = self.l
        dt = self.dt

        u = np.clip(u, -self.max_torque, self.max_torque)[0]
        self.last_u = u # for rendering
        reward = self.reward(th, thdot, u)

        newthdot = thdot + (-3*g/(2*l) * np.sin(th + np.pi) + 3./(m*l**2)*u) * dt
        newth = th + newthdot*dt
        newthdot = np.clip(newthdot, -self.max_speed, self.max_speed) #pylint: disable=E1111

        self.state = np.array([newth, newthdot])
        return self._get_obs(), reward, False, {}

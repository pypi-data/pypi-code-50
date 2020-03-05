# encoding: utf-8

import numpy as np

from rl import RL

np.random.seed(42)


class QLearning(RL):


    def __init__(self, world, n, epsilon, alpha, gamma):

        super(QLearning, self).__init__(world, n)
        self.epsilon = epsilon
        self.alpha   = alpha
        self.gamma   = gamma


    def choose_state(self, states):

        return np.random.choice(states)


    def choose_action(self, state):

        rn = np.random.rand()

        if rn < self.epsilon:
            return self.world.price_max_action(state)
        else:
            return np.random.choice(self.world.get_actions(state))


    def update(self):

        price_current  = self.world.price(self.state_current, self.action_current)
        price_next_max = self.world.price_max(self.state_next)
        reward_next    = self.world.get_rewards(self.state_next)

        p = (1-self.alpha)*price_current + self.alpha*(reward_next + self.gamma*price_next_max)

        self.world.price_set(self.state_current, self.action_current, p)



    def finish_iteration(self):

        return self.state_current.end


    def finish_fit(self):

        pass

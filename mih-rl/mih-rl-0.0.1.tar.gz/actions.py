# encoding: utf-8

import numpy as np


class Actions(object):


    def get(self, state):

        pass


    def price(self, state, action):

        pass


    def prices(self, state):

        return [self.price(state, action) for action in self.get(state)]


    def price_max(self, state):

        return max(self.prices(state))


    def price_max_action(self, state):

        return self.get(state)[np.argmax(self.prices(state))]


    def price_set(self, state, action, p):

        pass


    def take(self, state, action, states):

        pass




class ActionsQLearning(Actions):


    def __init__(self, q):

        self.q = q


    def get(self, state):

        # TODO: to be overwrite
        pass


    def price(self, state, action):

        return self.q[state][action]


    def price_set(self, state, action, p):

        self.q[state][action] = p


    def take(self, state, action, states):

        # TODO: to be overwrite
        pass

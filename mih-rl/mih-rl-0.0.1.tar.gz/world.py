# encoding: utf-8

class World(object):


    def __init__(self, states, actions, rewards):

        self.states  = states
        self.actions = actions
        self.rewards = rewards


    @property
    def starts(self):

        return self.states.starts


    def get_actions(self, state):

        return self.actions.get(state)


    def price(self, state, action):

        return self.actions.price(state, action)


    def price_max(self, state):

        return self.actions.price_max(state)


    def price_max_action(self, state):

        return self.actions.price_max_action(state)


    def price_set(self, state, action, p):

        return self.actions.price_set(state, action, p)


    def take(self, state, action):

        return self.actions.take(state, action, self.states)


    def get_rewards(self, *args, **kwargs):

        return self.rewards.get(*args, **kwargs)

# encoding: utf-8

from collections import OrderedDict


class States(object):


    def __init__(self):
        self.full  = OrderedDict()
        self.starts = []


    def append(self, state):
        self.full[state.key] = state
        
        if state.start:
            self.starts.append(state)


    def __getitem__(self, key):

        return self.full[key]

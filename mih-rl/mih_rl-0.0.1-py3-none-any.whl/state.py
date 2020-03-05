# encoding: utf-8

class State(object):


    def __init__(self, value, key, start=False, end=False):

        self.value = value
        self.key   = key
        self.start = start
        self.end   = end


    def __repr__(self):

        return 'state %s:%s start:%s end:%s' % (self.key, self.value, self.start, self.end)



class StateCategory(State):


    def __init__(self, value, key, start=False, end=False, stype=None):
    
        super(StateCategory, self).__init__(value, key, start, end)
        self.stype = stype



class StateRange(State):

    
    pass

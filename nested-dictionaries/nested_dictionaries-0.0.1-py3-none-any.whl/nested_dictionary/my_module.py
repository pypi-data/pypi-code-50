from collections import defaultdict

########################################################################################################
# Class definition
########################################################################################################
class NestedDictionary(defaultdict):
    def __init__(self, *args, **kwargs):
        super(NestedDictionary, self).__init__(NestedDictionary, *args, **kwargs)
    def __repr__(self):
        return repr(dict(self))



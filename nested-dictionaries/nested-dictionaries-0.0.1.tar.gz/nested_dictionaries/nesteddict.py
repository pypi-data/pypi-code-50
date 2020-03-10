from collections import defaultdict

class NestedDictionaries(defaultdict):
    def __init__(self, *args, **kwargs):
        super(NestedDictionaries, self).__init__(NestedDictionaries, *args, **kwargs)
    def __repr__(self):
        return repr(dict(self))



__version__ = '0.1.0'

from collections import defaultdict

class viv_dotdict(defaultdict):

    def __getattr__(self, key):
        return self[key]

    def __setattr__(self, key, val):
        self[key] = val

def dotree(): return viv_dotdict(dotree)


__version__ = '0.1.3'

import re
from collections import defaultdict


# a dict based solution 
class Viv(dict):

    def __missing__(self, key):
       val = self[key] = type(self)() 
       return val  

    def __getattr__(self, key):
        return self[key]

    def __setattr__(self, key, val):
        self[key] = val

# a def_dict base 
class viv_dotdict(defaultdict):

    def __getattr__(self, key):
        return self[key]

    def __setattr__(self, key, val):
        self[key] = val

def dotree(): return viv_dotdict(dotree)


# big fan of the following 
def strMUT(text, dic):
    """ Replaces keys of dic with values of dic in text. 2005-02 by Emanuel Rumpf """
    pat = "(%s)" % "|".join(map(re.escape, dic.keys()))
    return re.sub(pat, lambda m: dic[m.group()], text)


 



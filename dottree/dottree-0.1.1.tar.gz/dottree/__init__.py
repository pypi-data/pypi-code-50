__version__ = '0.1.1'

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



 
 



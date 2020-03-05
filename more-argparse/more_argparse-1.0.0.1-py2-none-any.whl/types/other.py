from .._common import *
import glob

def _is_wildcard(string):
    if '*' in string: return True
    if '?' in string: return True
    in_escape = False
    in_bracket = False
    for char in string:
        if char == '\\':
            in_escape = not in_escape
        elif char == '[':
            if in_escape:
                in_escape = False
            else:
                in_bracket = True
        elif char == ']':
            if in_escape:
                in_escape = False
            else:
                if in_bracket:
                    return True
    return False
def GlobbingType(basetype:callable=(lambda x: x), recursive:bool=False):
    """If the argument is a glob, glob the argument and add each filename to a list as basetype(filename)

Parameters
---------
basetype : callable
    see above; use case: basetype=argparse.FileType('r')
recursive : bool
    passed to glob.glob"""
    def internal_type(argument):
        nonlocal basetype, recursive
        if _is_wildcard(argument):
            res = []
            for fname in glob.iglob(argument, recursive=recursive):
                res.append(basetype(fname))
            return res
        else:
            return [basetype(argument)]
    return internal_type

__all__ = ['GlobbingType']
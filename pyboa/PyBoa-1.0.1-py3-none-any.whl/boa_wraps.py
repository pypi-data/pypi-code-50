from functools import wraps
from .boa_obj import boa


def boa_wraps(attribut):
    if callable(attribut):
        @wraps(attribut)
        def dec(*args, **kwargs):
            res = attribut(*args, **kwargs)
            if type(res).__name__[0].islower():
                return boa(res)
            return BoaWraps(res)
        return dec
    return boa(attribut)


class BoaWraps:
    def __init__(self, obj):
        self.obj = obj
        self.__class__ = type(obj.__class__.__name__,
                              (obj.__class__,),
                              {'__getattribute__': __getattribute__,
                               '__doc__': obj.__doc__})


def __getattribute__(self, name):
    return boa_wraps(object.__getattribute__(self, name))

import types
from functools import wraps
from .boa_obj import boa


def boa_wraps(attribut):
    if isinstance(attribut, types.FunctionType) or attribut.__class__.__name__ == 'method':
        @wraps(attribut)
        def dec(*args, **kwargs):
            res = attribut(*args, **kwargs)
            if res is None:
                return None
            if type(res).__name__[0].islower():
                return boa(res)
            return BoaWraps(res)
        return dec
    if callable(attribut):  # it's a class
        return attribut
    return boa(attribut)


class BoaWraps:
    def __init__(self, obj):
        methods = {
            '__getattribute__': gen__getattribute__(obj),
            '__doc__': obj.__doc__
        }
        self.__class__ = type(obj.__class__.__name__,
                              (obj.__class__,),
                              methods)


def gen__getattribute__(obj):
    def __getattribute__(self, name):
        return boa_wraps(getattr(obj, name))
    return __getattribute__

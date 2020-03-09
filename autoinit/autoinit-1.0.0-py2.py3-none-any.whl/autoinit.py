#!/bin/env python

from functools import wraps as _wraps
from inspect import isclass as _isclass, isfunction as _isfunction
from warnings import warn as _warn
from sys import version_info


VERSION = '1.0.0'


class AutoinitWarning(UserWarning, ValueError):
    pass


def autoinit(*decoargs, **decokwargs):
    '''
    Decorator for automatic initialization instance attributes

        @autoinit
        def __init__(self, a, b=10):
            pass

    is equivalent to

        def __init__(self, a, b=10):
            self.a = a
            self.b = b

    The decorator can be equally applied to both the __init__ method and the entire class.

    Options:
        exclude: str or iterable of strs  # skip specified attributes
        no_warn: bool = False # do not warn when decorator applied to not __init__,
        reverse: bool = False # call wrapped method before the assignment

    '''
    reverse = decokwargs.get('reverse', False)
    no_warn = decokwargs.get('no_warn', False)
    exclude = decokwargs.get('exclude', [])

    if version_info.major > 2:
        unicode = str
    else:
        unicode = type(u"")

    acceptable_str_types = (str, unicode)

    if isinstance(exclude, acceptable_str_types):
        exclude = [exclude]

    def inner_decorator(init_or_class):
        if _isclass(init_or_class):
            func = getattr(init_or_class, '__init__')
        elif _isfunction(init_or_class):
            func = init_or_class
        else:
            raise ValueError("autoinit decorator should be applied to class or its __init__ method")

        if (func.__name__  != '__init__' or func.__code__.co_name != '__init__') and not no_warn:
            _warn(AutoinitWarning("autoinit decorator intended to be applied only to __init__ method (use autoinit(no_warn=True) to suppress this warning)"))

        args_names = func.__code__.co_varnames[1:func.__code__.co_argcount]

        @_wraps(func)
        def inner(self, *args, **kwargs):
            if reverse:
                func(self, *args, **kwargs)
            args_vals = args[:]
            if func.__defaults__:
                args_vals += func.__defaults__[len(args) - len(args_names):]
            for k, v in zip(args_names, args_vals):
                if k not in exclude:
                    if (type(self.__class__).__name__ != 'classobj' and
                        hasattr(self, '__slots__') and k not in self.__slots__):
                        raise AttributeError("Can not assign attribute '%s': it is not listed in %s.__slots__" % (k, self.__class__))
                    setattr(self, k, v)
            if not reverse:
                func(self, *args, **kwargs)

        if _isclass(init_or_class):
            init_or_class.__init__ = inner
            return init_or_class
        else:
            return inner

    if decoargs and (_isfunction(decoargs[0]) or _isclass(decoargs[0])):
        return inner_decorator(decoargs[0])
    return inner_decorator

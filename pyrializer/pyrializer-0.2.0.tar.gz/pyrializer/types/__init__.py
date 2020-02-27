import inspect

from .builtin import BoolType
from .builtin import CustomType
from .builtin import FloatType
from .builtin import IntType
from .builtin import StrType

__all__ = [
    'BoolType',
    'CustomType',
    'FloatType',
    'IntType',
    'StrType',
    'augment'
    'is_custom_type',
]


def is_custom_type(ftype):
    return isinstance(ftype, CustomType)


_floatType = FloatType()
_intType = IntType()
_boolType = BoolType()
_strType = StrType()


def augment(ftype):
    if ftype is int:
        return _intType
    elif ftype is float:
        return _floatType
    elif ftype is bool:
        return _boolType
    elif ftype is str:
        return _strType
    elif is_custom_type(ftype):
        return ftype
    elif type(ftype) is list:
        return [augment(item) for item in ftype]
    elif inspect.isclass(ftype) and issubclass(ftype, CustomType):
        return ftype()
    return ftype

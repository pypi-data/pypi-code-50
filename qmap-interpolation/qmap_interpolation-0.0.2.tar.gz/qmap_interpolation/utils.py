"""
Common functions and structures.
"""

from typing import Callable
from .typed_tuple import TypedTuple


def lazy_property(func: Callable):
    attr = f'_lazy_{func.__name__}'

    @property
    def _lazy_property(self):
        if not hasattr(self, attr):
            setattr(self, attr, func(self))
        return getattr(self, attr)

    return _lazy_property


class Size(TypedTuple):
    z: int
    y: int

    def __init__(self, *args, **kwargs):
        super().__init__()
        assert self.z > 0, f'Z size should be a positive integer, provided {self.z} instead.'
        assert self.y > 0, f'Y size should be a positive integer, provided {self.y} instead.'


class BeamCenter(TypedTuple):
    z: int
    y: int

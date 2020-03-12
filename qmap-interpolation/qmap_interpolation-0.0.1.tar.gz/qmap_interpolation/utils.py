"""
Common functions and structures.
"""

from typing import Callable, NamedTuple


def lazy_property(func: Callable):
    attr = f'_lazy_{func.__name__}'

    @property
    def _lazy_property(self):
        if not hasattr(self, attr):
            setattr(self, attr, func(self))
        return getattr(self, attr)

    return _lazy_property


class Size(NamedTuple):
    z: int
    y: int


class BeamCenter(NamedTuple):
    z: int
    y: int

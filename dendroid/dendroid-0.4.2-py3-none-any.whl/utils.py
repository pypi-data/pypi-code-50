import weakref
from collections import deque
from itertools import count
from typing import (Any,
                    Iterable,
                    Optional)

from .hints import Domain


def to_balanced_tree_height(size: int) -> int:
    return size.bit_length() - 1


def _maybe_weakref(object_: Optional[Domain]
                   ) -> Optional[weakref.ReferenceType]:
    return (object_
            if object_ is None
            else weakref.ref(object_))


def _dereference_maybe(maybe_reference: Optional[weakref.ref]
                       ) -> Optional[Domain]:
    return (maybe_reference
            if maybe_reference is None
            else maybe_reference())


def capacity(iterable: Iterable[Any]) -> int:
    """
    Returns number of elements in iterable.

    >>> capacity(range(0))
    0
    >>> capacity(range(10))
    10
    """
    counter = count()
    # order matters: if `counter` goes first,
    # then it will be incremented even for empty `iterable`
    deque(zip(iterable, counter),
          maxlen=0)
    return next(counter)

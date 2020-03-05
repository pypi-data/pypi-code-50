# -*- coding:utf-8 -*-
#
# Copyright (C) 2020, Maximilian Köhl <mkoehl@cs.uni-saarland.de>

from __future__ import annotations

import typing as t


ElementT = t.TypeVar("ElementT")


def iter_lookahead(
    iterable: t.Iterable[ElementT],
) -> t.Iterator[t.Tuple[ElementT, t.Optional[ElementT]]]:
    iterator = iter(iterable)
    current_element = next(iterator, None)
    while current_element is not None:
        next_element = next(iterator, None)
        yield current_element, next_element
        current_element = next_element

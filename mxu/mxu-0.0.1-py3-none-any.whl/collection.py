# -*- coding:utf-8 -*-
#
# Copyright (C) 2020, Maximilian Köhl <mkoehl@cs.uni-saarland.de>

from __future__ import annotations

import typing as t


KeyT = t.TypeVar("KeyT")
ValueT = t.TypeVar("ValueT")


class _IdentityKey(t.Generic[KeyT]):
    __slots__ = ["wrapped"]

    wrapped: KeyT

    def __init__(self, wrapped: KeyT) -> None:
        self.wrapped = wrapped

    def __hash__(self) -> int:
        return object.__hash__(self.wrapped)

    def __eq__(self, other: t.Any) -> bool:
        if isinstance(other, _IdentityKey):
            return self.wrapped is other.wrapped
        return False


class IdentityMap(t.MutableMapping[KeyT, ValueT], t.Generic[KeyT, ValueT]):
    _dict: t.Dict[_IdentityKey[KeyT], ValueT]

    def __init__(
        self,
        base: t.Optional[t.Mapping[KeyT, ValueT]] = None,
        *,
        _dict: t.Optional[t.Dict[_IdentityKey[KeyT], ValueT]] = None,
    ) -> None:
        if base is not None:
            assert _dict is None, "`_dict` must be None if `base` is given"
            self._dict = {_IdentityKey(key): value for key, value in base.items()}
        elif _dict is not None:
            self._dict = _dict
        else:
            self._dict = {}
        self._hash = None

    def __getitem__(self, key: KeyT) -> ValueT:
        return self._dict[_IdentityKey(key)]

    def __setitem__(self, key: KeyT, value: ValueT) -> None:
        self._dict[_IdentityKey(key)] = value

    def __delitem__(self, key: KeyT):
        del self._dict[_IdentityKey(key)]

    def __iter__(self) -> t.Iterator[KeyT]:
        return (key.wrapped for key in self._dict.keys())

    def __len__(self) -> int:
        return len(self._dict)

    def __repr__(self) -> str:
        return f"<IdentityMap {self._dict!r}>"

# -*- coding:utf-8 -*-
#
# Copyright (C) 2020, Maximilian Köhl <mkoehl@cs.uni-saarland.de>

from __future__ import annotations

import typing as t

import dataclasses

from .stringify import StringifyResult, Path


@dataclasses.dataclass(frozen=True)
class Region:
    start: int
    end: int


@dataclasses.dataclass(frozen=True)
class Group:
    region: Region

    _stringify_result: StringifyResult
    _group_index: int

    _python_match: t.Match[str]

    def __repr__(self) -> str:
        return f"<orex.Group; region=({self.start},{self.end}), text={self.text!r}>"

    @property
    def text(self) -> str:
        return self._python_match.group(self._group_index)

    @property
    def start(self) -> int:
        return self.region.start

    @property
    def end(self) -> int:
        return self.region.end

    def iter_groups(self) -> t.Iterator[Group]:
        for offset in range(1, self._stringify_result.subgroups[self._group_index] + 1):
            yield self.get_group(offset)

    def iter_named_groups(self) -> t.Iterator[t.Tuple[Path, str, Group]]:
        own_prefix = len(self._stringify_result.paths[self._group_index]) + 1
        for offset in range(1, self._stringify_result.subgroups[self._group_index] + 1):
            index = self._group_index + offset
            try:
                name = self._stringify_result.names[index]
            except KeyError:
                pass
            else:
                path = self._stringify_result.paths[index][own_prefix:]
                yield path, name, self.get_group(offset)

    def get_group(self, name_or_index: t.Union[str, int]) -> Group:
        if isinstance(name_or_index, int):
            assert name_or_index <= self._stringify_result.subgroups[self._group_index]
            index = self._group_index + name_or_index
        else:
            path = self._stringify_result.paths[self._group_index]
            name = self._stringify_result.get_full_group_name(path, name=name_or_index)
            index = self._stringify_result.indices[name]
        region = Region(*self._python_match.span(index))
        return Group(region, self._stringify_result, index, self._python_match)


__all__ = ["Region", "Group"]

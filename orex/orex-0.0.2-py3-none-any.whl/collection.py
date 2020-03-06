# -*- coding:utf-8 -*-
#
# Copyright (C) 2020, Maximilian Köhl <mkoehl@cs.uni-saarland.de>

from __future__ import annotations

import typing as t

import dataclasses

from .backend import CompileFlags, DEFAULT_FLAGS, CompiledPattern, compile_pattern
from .match import Group
from .patterns import Pattern, choice, named_group


@dataclasses.dataclass
class PatternCollection:
    flags: CompileFlags = DEFAULT_FLAGS

    _patterns: t.List[Pattern] = dataclasses.field(default_factory=list)
    _map: t.Dict[str, Pattern] = dataclasses.field(default_factory=dict)

    _compiled_pattern: t.Optional[CompiledPattern] = None

    def add_pattern(self, pattern: Pattern) -> None:
        self._compiled_pattern = None
        self._map[f"PATTERN_{len(self._patterns)}"] = pattern
        self._patterns.append(pattern)

    def _compile(self) -> CompiledPattern:
        if self._compiled_pattern is None:
            self._compiled_pattern = compile_pattern(
                choice(
                    [
                        named_group(f"PATTERN_{index}", pattern)
                        for index, pattern in enumerate(self._patterns)
                    ]
                )
            )
        return self._compiled_pattern

    def _resolve(self, group: t.Optional[Group]) -> t.Optional[t.Tuple[Pattern, Group]]:
        if group is None:
            return None
        assert group._python_match.lastgroup is not None
        pattern = self._map[group._python_match.lastgroup]
        return pattern, group.get_group(group._python_match.lastgroup)

    def match(
        self, string: str, *, start: int = 0, end: t.Optional[int] = None
    ) -> t.Optional[t.Tuple[Pattern, Group]]:
        return self._resolve(self._compile().match(string, start=start, end=end))

    def search(
        self, string: str, *, start: int = 0, end: t.Optional[int] = None
    ) -> t.Optional[t.Tuple[Pattern, Group]]:
        return self._resolve(self._compile().search(string, start=start, end=end))


__all__ = ["PatternCollection"]

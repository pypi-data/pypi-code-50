# -*- coding:utf-8 -*-
#
# Copyright (C) 2020, Maximilian Köhl <mkoehl@cs.uni-saarland.de>

from __future__ import annotations

import typing as t

import dataclasses
import enum
import re

from .match import Region, Group
from .patterns import Pattern
from .stringify import StringifyResult, stringify


class CompileFlags(enum.Flag):
    NONE = 0
    IGNORECASE = re.IGNORECASE
    MULTILINE = re.MULTILINE


DEFAULT_FLAGS = CompileFlags.NONE


@dataclasses.dataclass
class CompiledPattern:
    pattern: Pattern
    flags: CompileFlags

    _python_pattern: t.Pattern[str]
    _stringify_result: StringifyResult

    def match(
        self, string: str, *, start: int = 0, end: t.Optional[int] = None
    ) -> t.Optional[Group]:
        if end is None:
            python_match = self._python_pattern.match(string, pos=start)
        else:
            python_match = self._python_pattern.match(string, pos=start, endpos=end)
        if python_match is None:
            return None
        else:
            region = Region(*python_match.span(0))
            return Group(region, self._stringify_result, 0, python_match)

    def search(
        self, string: str, *, start: int = 0, end: t.Optional[int] = None
    ) -> t.Optional[Group]:
        if end is None:
            python_match = self._python_pattern.search(string, pos=start)
        else:
            python_match = self._python_pattern.search(string, pos=start, endpos=end)
        if python_match is None:
            return None
        else:
            region = Region(*python_match.span(0))
            return Group(region, self._stringify_result, 0, python_match)


def compile_pattern(
    pattern: Pattern, *, flags: CompileFlags = DEFAULT_FLAGS
) -> CompiledPattern:
    stringify_result = stringify(pattern)
    python_pattern = re.compile(stringify_result.string, flags=flags.value)
    return CompiledPattern(pattern, flags, python_pattern, stringify_result)


__all__ = ["CompileFlags", "CompiledPattern", "compile_pattern"]

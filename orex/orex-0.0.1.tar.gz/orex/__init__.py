# -*- coding:utf-8 -*-
#
# Copyright (C) 2020, Maximilian Köhl <mkoehl@cs.uni-saarland.de>

from __future__ import annotations

from .backend import CompileFlags, CompiledPattern, compile_pattern

from .collection import PatternCollection

from .match import Region, Group

from .patterns import (
    Pattern,
    Atom,
    Class,
    PrototypePattern,
    ensure_pattern,
    literal,
    repeat,
    at_most_once,
    at_least_once,
    character_range,
    character_set,
    choice,
    group,
    named_group,
    concat,
    word,
    WORD,
    WHITESPACE,
)

from .stringify import StringifyOptions, Style, Path, StringifyResult, stringify

__all__ = [
    "CompileFlags",
    "CompiledPattern",
    "compile_pattern",
    "PatternCollection",
    "Region",
    "Group",
    "Pattern",
    "Atom",
    "Class",
    "PrototypePattern",
    "ensure_pattern",
    "literal",
    "repeat",
    "at_most_once",
    "at_least_once",
    "character_range",
    "character_set",
    "choice",
    "group",
    "named_group",
    "concat",
    "word",
    "WORD",
    "WHITESPACE",
    "StringifyOptions",
    "Style",
    "Path",
    "StringifyResult",
    "stringify",
]

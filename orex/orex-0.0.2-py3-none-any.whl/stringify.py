# -*- coding:utf-8 -*-
#
# Copyright (C) 2020, Maximilian Köhl <mkoehl@cs.uni-saarland.de>

from __future__ import annotations

import typing as t

import abc
import dataclasses
import enum
import functools
import re

from mxu.itertools import iter_lookahead
from mxu.sanity import check_singledispatch

from . import patterns

from .patterns import Pattern


@dataclasses.dataclass(frozen=True)
class StringifyOptions:
    hierarchic_groups: bool = True
    strip_group_names: bool = False
    group_name_prefix: str = ""


DEFAULT_OPTIONS = StringifyOptions()


class _Style(abc.ABC):
    @abc.abstractmethod
    def begin_named_group(self, name: str, ctx: _Context) -> None:
        raise NotImplementedError()


class _StylePython(_Style):
    def begin_named_group(self, name: str, ctx: _Context) -> None:
        ctx.chunks.append(f"(?P<{name}>")


class _StyleOniguruma(_Style):
    def begin_named_group(self, name: str, ctx: _Context) -> None:
        ctx.chunks.append(f"(?<{name}>")


class Style(enum.Enum):
    PYTHON = _StylePython()
    ONIGURUMA = _StyleOniguruma()

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__}.{self.name}>"


DEFAULT_STYLE = Style.PYTHON


Path = t.Tuple[str, ...]


@dataclasses.dataclass(frozen=True)
class StringifyResult:
    pattern: Pattern
    options: StringifyOptions
    style: Style
    string: str
    indices: t.Mapping[str, int]
    subgroups: t.Mapping[int, int]
    names: t.Mapping[int, str]
    paths: t.Mapping[int, Path]

    def get_full_group_name(
        self, path: t.Sequence[str], *, name: t.Optional[str] = None
    ) -> str:
        if not path:
            if name is None:
                raise Exception("invalid path")
            return name
        suffix = "" if name is None else f"__{name}"
        return f"{self.options.group_name_prefix}{'__'.join(path)}{suffix}"


@dataclasses.dataclass
class _Context:
    options: StringifyOptions
    style: _Style
    indices: t.Dict[str, int] = dataclasses.field(default_factory=dict)
    subgroups: t.Dict[int, int] = dataclasses.field(default_factory=dict)
    names: t.Dict[int, str] = dataclasses.field(default_factory=dict)
    paths: t.Dict[int, t.Tuple[str, ...]] = dataclasses.field(default_factory=dict)

    last_group_index: int = 0
    path: t.List[str] = dataclasses.field(default_factory=list)
    defined_groups: t.Set[str] = dataclasses.field(default_factory=set)
    chunks: t.List[str] = dataclasses.field(default_factory=list)

    def advance_group_index(self) -> int:
        self.last_group_index += 1
        return self.last_group_index


def stringify(
    pattern: Pattern,
    *,
    options: StringifyOptions = DEFAULT_OPTIONS,
    style: Style = DEFAULT_STYLE,
) -> StringifyResult:
    ctx = _Context(options, style.value)
    ctx.paths[0] = ()
    _stringify_pattern(pattern, ctx)
    return StringifyResult(
        pattern,
        options,
        style,
        "".join(ctx.chunks),
        ctx.indices,
        ctx.subgroups,
        ctx.names,
        ctx.paths,
    )


@functools.singledispatch
def _stringify_pattern(pattern: patterns.Pattern, ctx: _Context) -> None:
    raise NotImplementedError(
        f"unable to compile pattern {pattern} to regular expression in Python syntax"
    )


@_stringify_pattern.register(patterns.Atom)
@_stringify_pattern.register(patterns.Class)
def _stringify_singleton(
    pattern: t.Union[patterns.Atom, patterns.Class], ctx: _Context
) -> None:
    ctx.chunks.append(pattern.value)


@_stringify_pattern.register
def _stringify_literal(pattern: patterns.Literal, ctx: _Context) -> None:
    ctx.chunks.append(re.escape(pattern.literal))


@_stringify_pattern.register
def _stringify_repeat(pattern: patterns.Repeat, ctx: _Context) -> None:
    _stringify_pattern(pattern.pattern, ctx)
    if pattern.lower_bound == 0 and pattern.upper_bound is None:
        ctx.chunks.append("*")
    elif pattern.lower_bound == 1 and pattern.upper_bound is None:
        ctx.chunks.append("+")
    elif pattern.lower_bound == 0 and pattern.upper_bound == 1:
        ctx.chunks.append("?")
    elif pattern.upper_bound is None:
        ctx.chunks.append(f"{{{pattern.lower_bound}}}")
        _stringify_pattern(pattern.pattern, ctx)
        ctx.chunks.append("*")
    else:
        ctx.chunks.append(f"{{{pattern.lower_bound},{pattern.upper_bound}}}")
    if not pattern.is_greedy:
        ctx.chunks.append("?")


@_stringify_pattern.register
def _stringify_set(pattern: patterns.Set, ctx: _Context) -> None:
    ctx.chunks.append("[")
    if pattern.is_negated:
        ctx.chunks.append("^")
    for element in pattern.elements:
        if isinstance(element, patterns.Range):
            start = re.escape(element.start)
            end = re.escape(element.end)
            ctx.chunks.append(f"{start}-{end}")
        elif isinstance(element, patterns.Class):
            ctx.chunks.append(element.value)
        else:
            ctx.chunks.append(re.escape(element))
    ctx.chunks.append("]")


@_stringify_pattern.register
def _stringify_choice(pattern: patterns.Choice, ctx: _Context) -> None:
    ctx.chunks.append("(?:")
    for alternative, lookahead in iter_lookahead(pattern.alternatives):
        _stringify_pattern(alternative, ctx)
        if lookahead is not None:
            ctx.chunks.append("|")
    ctx.chunks.append(")")


@_stringify_pattern.register
def _stringify_group(pattern: patterns.Group, ctx: _Context) -> None:
    index = ctx.advance_group_index()
    ctx.paths[index] = tuple(ctx.path)

    ctx.chunks.append("(")
    _stringify_pattern(pattern.pattern, ctx)
    ctx.chunks.append(")")

    ctx.subgroups[index] = ctx.last_group_index - index


@_stringify_pattern.register
def _stringify_named_group(pattern: patterns.NamedGroup, ctx: _Context) -> None:
    index = ctx.advance_group_index()
    ctx.paths[index] = tuple(ctx.path)
    ctx.names[index] = pattern.name

    ctx.path.append(pattern.name)
    if ctx.options.hierarchic_groups:
        full_name = ctx.options.group_name_prefix + "__".join(ctx.path)
    else:
        full_name = ctx.options.group_name_prefix + pattern.name

    ctx.indices[full_name] = index

    if ctx.options.strip_group_names:
        ctx.chunks.append("(")
    else:
        if full_name in ctx.defined_groups:
            raise Exception(f"group {full_name} has already been defined")
        ctx.defined_groups.add(full_name)
        ctx.style.begin_named_group(full_name, ctx)
    _stringify_pattern(pattern.pattern, ctx)
    ctx.chunks.append(")")
    ctx.path.pop()

    ctx.subgroups[index] = ctx.last_group_index - index


@_stringify_pattern.register
def _stringify_sequence(pattern: patterns.Sequence, ctx: _Context) -> None:
    for child in pattern.patterns:
        _stringify_pattern(child, ctx)


check_singledispatch(_stringify_pattern, patterns.Pattern)


__all__ = [
    "StringifyOptions",
    "Style",
    "Path",
    "StringifyResult",
    "stringify",
]

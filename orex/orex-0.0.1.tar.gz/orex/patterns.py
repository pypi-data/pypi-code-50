# -*- coding:utf-8 -*-
#
# Copyright (C) 2020, Maximilian Köhl <mkoehl@cs.uni-saarland.de>

from __future__ import annotations

import typing as t

import dataclasses
import enum


class Pattern:
    pass


class Atom(Pattern, enum.Enum):
    ANY = "."

    START = "^"
    END = "$"

    STRING_START = r"\A"
    STRING_END = r"\Z"

    WORD_BOUNDARY = r"\b"
    NOT_WORD_BOUNDARY = r"\B"

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__}.{self.name}>"


class Class(Pattern, enum.Enum):
    WORD = r"\w"
    NOT_WORD = r"\W"

    WHITESPACE = r"\s"
    NOT_WHITESPACE = r"\S"

    DIGIT = r"\d"
    NOT_DIGIT = r"\D"

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__}.{self.name}>"


@dataclasses.dataclass(frozen=True)
class Literal(Pattern):
    literal: str

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__} {self.literal!r}>"


@dataclasses.dataclass(frozen=True)
class Repeat(Pattern):
    pattern: Pattern

    lower_bound: int = 0
    upper_bound: t.Optional[int] = None

    is_greedy: bool = True

    def __repr__(self) -> str:
        greedy_flag = "" if self.is_greedy else "?"
        upper_bound = "∞" if self.upper_bound is None else str(self.upper_bound)
        return (
            f"<{self.__class__.__name__} {self.pattern!r} "
            f"{{{self.lower_bound},{upper_bound}}}{greedy_flag}>"
        )


@dataclasses.dataclass(frozen=True)
class Range:
    start: str
    end: str

    def __post_init__(self) -> None:
        if len(self.start) != 1 or len(self.end) != 1:
            raise Exception(f"invalid character range {self.start!r}-{self.end!r}")

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__} {self.start!r}-{self.end!r}>"


@dataclasses.dataclass(frozen=True)
class Set(Pattern):
    elements: t.FrozenSet[t.Union[Range, Class, str]]
    is_negated: bool = False

    def __post_init__(self) -> None:
        if not self.elements:
            raise Exception("pattern set must not be empty")
        for element in self.elements:
            if isinstance(element, str) and len(element) != 1:
                raise Exception(f"invalid set element {element!r}")

    def __repr__(self) -> str:
        elements = ", ".join(map(repr, self.elements))
        return f"<{self.__class__.__name__} is_negated={self.is_negated} {elements}>"

    def negate(self) -> Set:
        return Set(self.elements, is_negated=not self.is_negated)


@dataclasses.dataclass(frozen=True)
class Choice(Pattern):
    alternatives: t.Tuple[Pattern, ...]

    def __post_init__(self) -> None:
        if not self.alternatives:
            raise Exception("alternatives must not be empty")

    def __repr__(self) -> str:
        alternatives = " | ".join(map(repr, self.alternatives))
        return f"<{self.__class__.__name__} {alternatives}>"


@dataclasses.dataclass(frozen=True)
class Group(Pattern):
    pattern: Pattern

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__} {self.pattern!r}>"


@dataclasses.dataclass(frozen=True)
class NamedGroup(Pattern):
    name: str
    pattern: Pattern

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__} name={self.name!r} {self.pattern!r}>"


@dataclasses.dataclass(frozen=True)
class Sequence(Pattern):
    patterns: t.Tuple[Pattern, ...]

    def __post_init__(self) -> None:
        if not self.patterns:
            raise Exception("sequence must not be empty")

    def __repr__(self) -> str:
        patterns = " ".join(map(repr, self.patterns))
        return f"<{self.__class__.__name__} {patterns}>"


PrototypePattern = t.Union[  # type: ignore
    Pattern,
    str,
    t.AbstractSet["PrototypePattern"],  # type: ignore
    t.Mapping[str, "PrototypePattern"],  # type: ignore
    t.Sequence["PrototypePattern"],  # type: ignore
]


def ensure_pattern(prototype: PrototypePattern) -> Pattern:
    if isinstance(prototype, Pattern):
        return prototype
    elif isinstance(prototype, str):
        return literal(prototype)
    elif isinstance(prototype, t.Mapping):
        assert len(prototype) == 1
        name, child = next(iter(prototype.items()))
        return NamedGroup(name, ensure_pattern(child))
    elif isinstance(prototype, t.AbstractSet):
        return Choice(tuple(ensure_pattern(alternative) for alternative in prototype))
    else:
        return Sequence(tuple(ensure_pattern(element) for element in prototype))


def literal(literal: str) -> Literal:
    return Literal(literal)


def repeat(
    pattern: PrototypePattern,
    *,
    lower_bound: int = 0,
    upper_bound: t.Optional[int] = None,
    is_greedy: bool = True,
) -> Repeat:
    return Repeat(
        ensure_pattern(pattern),
        lower_bound=lower_bound,
        upper_bound=upper_bound,
        is_greedy=is_greedy,
    )


def at_most_once(prototype: PrototypePattern, *, is_greedy: bool = True) -> Repeat:
    return repeat(prototype, lower_bound=0, upper_bound=1, is_greedy=is_greedy)


def at_least_once(prototype: PrototypePattern, *, greedy: bool = True) -> Repeat:
    return repeat(prototype, lower_bound=1, is_greedy=greedy)


def character_range(start: str, end: str) -> Range:
    return Range(start, end)


def character_set(*elements: t.Union[Range, Class, str]) -> Set:
    return Set(frozenset(elements))


def choice(alternatives: t.Iterable[PrototypePattern]) -> Choice:
    return Choice(tuple(ensure_pattern(alternative) for alternative in alternatives))


def group(*alternatives: PrototypePattern) -> Group:
    return Group(choice(alternatives))


def named_group(name: str, prototype: PrototypePattern) -> NamedGroup:
    return NamedGroup(name, ensure_pattern(prototype))


def concat(*prototypes: PrototypePattern) -> Sequence:
    return Sequence(tuple(ensure_pattern(prototype) for prototype in prototypes))


def word(prototype: PrototypePattern) -> Pattern:
    return concat(Atom.WORD_BOUNDARY, ensure_pattern(prototype), Atom.WORD_BOUNDARY)


WORD = at_least_once(Class.WORD)
WHITESPACE = at_least_once(Class.WHITESPACE)


__all__ = [
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
]

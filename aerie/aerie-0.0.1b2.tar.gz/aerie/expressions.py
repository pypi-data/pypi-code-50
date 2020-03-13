from __future__ import annotations

import enum
import functools
from typing import Any, Literal, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .fields import Field


class Conditions(enum.Enum):
    CONCAT = 'concat'
    LIKE = 'like'
    ILIKE = 'ilike'
    IN = 'in'
    IS = 'is'
    STARTS_WITH = 'starts_with'
    ENDS_WITH = 'ends_with'
    CONTAINS = 'contains'
    MATCH = 'match'
    BETWEEN = 'between'
    EQUALS = 'equals'
    GREATER = 'greater'
    GREATER_OR_EQUAL = 'greater_or_equal'
    LESSER = 'lesser'
    LESSER_OR_EQUAL = 'lesser_or_equal'
    NEGATE = 'negate'
    ADD = 'add'
    RIGHT_ADD = 'right_add'
    SUBTRACT = 'subtract'
    RIGHT_SUBTRACT = 'right_subtract'
    MULTIPLY = 'multiply'
    RIGHT_MULTIPLY = 'right_multiply'
    DIVIDE = 'divide'
    RIGHT_DIVIDE = 'right_divide'
    MODULO = 'modulo'
    RIGHT_MODULO = 'right_modulo'

    # logical
    OR = 'or'
    AND = 'and'


class Expr:
    def __init__(self, field: Field, condition: Conditions, value: Any = None,
                 negate: bool = False):
        self.field = field
        self.condition = condition
        self.value = value
        self.negate = negate

    def __invert__(self) -> Expr:
        self.negate = not self.negate
        return self

    def __str__(self) -> str:
        return (
            f'<{self.__class__.__name__}: '
            f'field={self.field.__class__.__name__} '
            f'condition={self.condition} '
            f'value={self.value} '
            f'negate={self.negate}>'
        )

    def __or__(self, other: Expr) -> LogicalExpr:
        return LogicalExpr(self, other, Conditions.OR)

    def __and__(self, other: Expr) -> LogicalExpr:
        return LogicalExpr(self, other, Conditions.AND)


class LogicalExpr:
    def __init__(self, left: ExprLike, right: ExprLike, condition: Conditions):
        self.left = left
        self.right = right
        self.condition = condition

    def __or__(self, other: ExprLike) -> LogicalExpr:
        return LogicalExpr(self, other, Conditions.OR)

    def __and__(self, other: ExprLike) -> LogicalExpr:
        return LogicalExpr(self, other, Conditions.AND)

    def __str__(self):
        return f'{self.left} {self.condition} {self.right}'


ExprLike = Union[Expr, LogicalExpr]


class Sort(enum.Enum):
    ASC = 'asc'
    DESC = 'desc'


class Nulls(enum.Enum):
    FIRST = 'first'
    LAST = 'last'
    UNDEFINED = 'undefined'


def and_(*exprs: ExprLike):
    return functools.reduce(
        lambda agg, value: agg & value, exprs[1:], exprs[0]
    )


def or_(*exprs: ExprLike):
    return functools.reduce(
        lambda agg, value: agg | value, exprs[1:], exprs[0]
    )


class OrderBy:

    def __init__(
            self,
            field: Field,
            sort: Literal[Sort.ASC, Sort.DESC],
            nulls: Literal[
                Nulls.LAST, Nulls.FIRST, Nulls.UNDEFINED
            ] = Nulls.UNDEFINED,
    ):
        self.field = field
        self.sort = sort
        self.nulls = nulls

    def nulls_first(self) -> OrderBy:
        self.nulls = Nulls.FIRST
        return self

    def nulls_last(self) -> OrderBy:
        self.nulls = Nulls.LAST
        return self

    def asc(self) -> OrderBy:
        self.sort = Sort.ASC
        return self

    def desc(self) -> OrderBy:
        self.sort = Sort.DESC
        return self

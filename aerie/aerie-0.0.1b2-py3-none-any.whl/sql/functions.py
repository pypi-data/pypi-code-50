from __future__ import annotations

import sqlalchemy as sa
from typing import Any

from aerie.fields import Field


class Function:
    name: str
    func: Any

    def __init__(self, field: Field, *args, alias: str = None):
        self._field = field
        self._args = args
        self._alias = alias or field.attr_name + '_' + self.name

    def alias(self, alias: str) -> Function:
        self._alias = alias
        return self

    def __expr__(self, column: sa.Column) -> sa.sql.ClauseElement:
        return self.func(column).label(self._alias)

    def __str__(self):
        return f'<Function: name={self.name} field={self._field}>'


class Avg(Function):
    func = sa.sql.func


class Min(Function): ...


class Max(Function): ...


class Sum(Function): ...


class Count(Function): ...


class Round(Function): ...


class Abs(Function): ...


class Ceil(Function): ...


class Floor(Function): ...


class MD5(Function): ...


class Upper(Function): ...


class Lower(Function): ...

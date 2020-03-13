from __future__ import annotations

import asyncio
from functools import reduce
from typing import (
    Any,
    Callable,
    Generic,
    List,
    Mapping,
    TYPE_CHECKING,
    Type,
    TypeVar,
    Union)

import sqlalchemy as sa

from aerie.sql import functions as func
from aerie.collections import Collection
from aerie.sql.connections import Connection
from aerie.expressions import ExprLike
from aerie.fields import Field
from aerie.preloading import Preload
from aerie.protocols import Adapter
from aerie.queries.base import BaseQuery
from aerie.query import QueryBuilder
from aerie.row import Row

if TYPE_CHECKING:
    from aerie.schemas import Schema

SQLLike = Union[str, sa.sql.ClauseElement]
And = sa.sql.and_
Or = lambda *args: sa.sql.and_(sa.sql.or_(*args))
Not = sa.sql.not_

RE = TypeVar("RE")  # entity for RawQuery. does not need to be a Schema
E = TypeVar("E", bound="Schema")
S = TypeVar("S", bound="Schema")
Factory = Callable[[Mapping, Type[E]], E]


def _format_sql(sql: str) -> str:
    try:
        import pygments
        import pygments.lexers
        import pygments.formatters

        lexer = pygments.lexers.get_lexer_by_name("sql")
        formatter = pygments.formatters.get_formatter_by_name("console")
        sql = pygments.highlight(sql, lexer, formatter)
    except ImportError:
        pass
    return sql


class DeleteEntityQuery(Generic[E], BaseQuery):
    def __init__(self, adapter: Adapter, entity: E):
        self._adapter = adapter
        self._entity = entity

    async def execute(self) -> None:
        await self._adapter.delete(self._entity)


class UpdateQuery(BaseQuery):
    def __init__(
            self,
            adapter: Adapter,
            schema: Type[Schema],
            values: Mapping,
            where: ExprLike = None,
    ):
        self._schema = schema
        self._adapter = adapter
        self._values = values

        if isinstance(where, list):
            where = reduce(sa.and_, where) if len(where) > 0 else None
        self._where = where

    async def execute(self) -> None:
        await self._adapter.update_all(
            self._schema, self._values, self._where,
        )


class DeleteQuery(BaseQuery):
    def __init__(
            self,
            adapter: Adapter,
            schema: Type[Schema],
            where: ExprLike = None,
    ):
        self._schema = schema
        self._adapter = adapter
        self._where = where

    async def execute(self) -> None:
        await self._adapter.delete_all(self._schema, self._where)


def dumps(fn):
    def wrapper(self: QueryBuilder, *args, **kwargs):
        if self._dump:
            self._dump_writer.write(
                '\n' + _format_sql(str(self))
            )
        return fn(self, *args, **kwargs)

    return wrapper


class SelectQuery(Generic[E], BaseQuery):
    def __init__(
            self,
            adapter: Adapter,
            schema: Type[Schema],
            query: QueryBuilder,
            *,
            preload_one: List[Preload],
            preload_many: List[Preload],
    ):
        self._connection = connection
        self._schema = schema
        self._query = query
        self._preload_one = preload_one
        self._preload_many = preload_many

    async def execute(self) -> Collection[E]:
        entities = [
            self._schema.from_row(
                row, [r._relation for r in self._preload_one]
            )
            for row in await self._connection.fetch_all(
                self._query.get_expr(),
            )
        ]

        await asyncio.gather(*[
            preloader.process_rows(entities)
            for preloader in self._preload_many
        ])

        return Collection(entities)


class SelectColumnQuery(BaseQuery):
    def __init__(self, connection: Connection, query: QueryBuilder,
                 field: Field):
        self._connection = connection
        self._query = query
        self._field = field

    async def execute(self) -> Collection[Any]:
        rows = await self._connection.fetch_all(self._build_expr())
        return Collection([row[self._field.column_name] for row in rows])


class AggregateQuery(BaseQuery):
    def __init__(self, connection: Connection, query: QueryBuilder,
                 **fn: func.Function):
        self._connection = connection
        self._query = query
        self._fns = fn

    async def execute(self) -> Row:
        row = await self._connection.fetch_one(self._build_expr())
        return Row(**{
            col_name: row[col_name]
            for col_name in self._fns.keys()
        })

    async def get_value(self, name: Union[str, Field]) -> Any:
        row = await self
        return getattr(row, str(name))


class CountQuery(BaseQuery):
    def __init__(self, connection: Connection, query: QueryBuilder):
        self._connection = connection
        self._query = query

    async def execute(self) -> int:
        expr = self._build_expr()
        return await self._connection.fetch_val(expr)


class ExistsQuery(BaseQuery):
    def __init__(self, adapter: Connection, query: QueryBuilder,
                 negate: bool = False):
        self._adapter = adapter
        self._query = query
        self._negate = negate

    async def execute(self) -> bool:
        expr = self._build_expr()
        exists = await self._connection.fetch_val(expr)
        return exists is False if self._negate else exists is True

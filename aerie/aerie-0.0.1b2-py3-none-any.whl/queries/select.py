from __future__ import annotations

import sys
from typing import (Any, AsyncGenerator, Generic, Optional, TextIO, Tuple,
                    TypeVar, Union)

from aerie.collections import Collection
from aerie.protocols import Adapter
from aerie.queries.base import AwaitableQuery
from aerie.query import QueryBuilder
from aerie.schemas import Schema
from aerie.utils import format_sql

T = TypeVar('T', bound=Schema)


class SelectQuery(Generic[T], AwaitableQuery):
    def __init__(self, adapter: Adapter, query: QueryBuilder):
        self._adapter = adapter
        self._schema = query._schema
        self._query = query

    async def all(self) -> Collection[T]:
        rows = await self._adapter.fetch_all(self._query)
        return Collection([self._schema.from_row(row) for row in rows])

    execute = all

    async def one(self) -> T:
        self._query = self._query.limit(2)
        rows = await self.all()
        if len(rows) == 0:
            raise self._schema.DoesNotExist(
                "Exactly one row expected but zero found.")

        if len(rows) > 1:
            raise self._schema.MultipleResults(
                f"Exactly one row expected but zero {len(rows)} found."
            )
        return rows.first()

    async def one_or_none(self) -> Optional[T]:
        try:
            return await self.one()
        except self._schema.DoesNotExist:
            return None

    async def iterate(self) -> AsyncGenerator[T, None]:
        async for row in self._adapter.iterate(self._query):
            yield self._schema.from_row(row)

    async def scalar(self) -> Optional[Union[Any, Tuple[Any]]]:
        rows = await self._adapter.fetch_all(self._query)
        if len(rows) == 0:
            return None
        row = rows[0]
        values = tuple([row[f.source_name] for f in self._query._fields])
        if len(values) == 1:
            return values[0]
        return values

    async def exists(self) -> bool:
        return await self._adapter.exists(self._query)

    async def count(self) -> int:
        return await self._adapter.count(self._query)

    def dump(self, writer: TextIO = sys.stdout) -> SelectQuery[T]:
        formatted = format_sql(str(self))
        writer.write(formatted)
        return self

    def __str__(self):
        return self._adapter.to_string(self._query)

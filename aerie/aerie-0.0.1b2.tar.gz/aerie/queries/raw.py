from __future__ import annotations

from typing import (Any, AsyncGenerator, Generic, Mapping, Optional,
                    Type, TypeVar)

from aerie.collections import Collection
from aerie.exceptions import DoesNotExist, MultipleResults
from aerie.protocols import Adapter
from aerie.queries.base import AwaitableQuery
from aerie.row import Row

T = TypeVar('T')
MAP_TO = TypeVar('MAP_TO')


class RawQuery(Generic[T], AwaitableQuery):
    entity: Type[T]

    def __init__(
            self,
            adapter: Adapter,
            query: str,
            values: Mapping = None,
            map_to: Type[T] = Row,
    ):
        self._query = query
        self._adapter = adapter
        self._values = values
        self._map_to = map_to

    def map_to(self, map_to: Type[MAP_TO]) -> RawQuery[MAP_TO]:
        return self.clone(map_to=map_to)

    def clone(self, **kwargs: Any) -> RawQuery[T]:
        defaults = dict(
            adapter=self._adapter,
            query=self._query,
            values=self._values,
            map_to=self._map_to,
        )
        defaults.update(kwargs)
        return type(self)(**defaults)

    async def all(self) -> Collection[T]:
        rows = await self._adapter.fetch_all(self._query, self._values)
        return Collection([
            self._map_to(**row) for row in rows
        ])

    async def one(self) -> T:
        rows = Collection([
            self._map_to(**row)
            for row in await self._adapter.fetch_all(self._query, self._values)
        ])
        if len(rows) == 0:
            raise DoesNotExist("Exactly one row expected but zero found.")

        if len(rows) > 1:
            raise MultipleResults(
                f"Exactly one row expected but zero {len(rows)} found."
            )
        return rows.first()

    async def one_or_none(self) -> Optional[T]:
        try:
            return await self.one()
        except DoesNotExist:
            return None

    async def execute(self) -> Any:
        return await self._adapter.execute(self._query, self._values)

    async def iterate(self) -> AsyncGenerator[T, None]:
        async for row in self._adapter.iterate(self._query, self._values):
            yield self._map_to(**row)

    def __str__(self):
        return self._query

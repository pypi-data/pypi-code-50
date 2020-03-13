from __future__ import annotations

from typing import (Iterable, Mapping, Sequence, Type, TypeVar, Union, Any,
                    Tuple)

from .expressions import ExprLike
from .fields import Field
from .protocols import Adapter
from .queries.delete_all import DeleteAllQuery
from .queries.delete_object import DeleteObjectQuery
from .queries.insert_all import InsertAllQuery
from .queries.insert_object import InsertObjectQuery
from .queries.raw import RawQuery
from .queries.select import SelectQuery
from .queries.update_all import UpdateAllQuery
from .queries.update_object import UpdateObjectQuery
from .query import QueryBuilder
from .schemas import Schema

E = TypeVar("E", bound=Schema)


class Store:
    def __init__(self, adapter: Adapter):
        self._adapter = adapter

    def raw(self, query: str, params: Mapping = None) -> RawQuery[E]:
        return RawQuery(
            adapter=self._adapter,
            query=query,
            values=params,
        )

    def query(self, query: Union[QueryBuilder, Type[E]]) -> SelectQuery[E]:
        if issubclass(query, Schema):
            query = QueryBuilder(query)
        return SelectQuery(adapter=self._adapter, query=query)

    async def get(self, schema: Type[E], pk: Union[Any, Tuple[Any]]) -> E:
        query = QueryBuilder(schema).where(schema.pk == pk)
        return await self.query(query).one()

    async def get_by(self, schema: Type[E], where: ExprLike) -> E:
        query = QueryBuilder(schema).where(where)
        return await self.query(query).one_or_none()

    def insert(self, entity: E) -> InsertObjectQuery[E]:
        return InsertObjectQuery(
            adapter=self._adapter,
            entity=entity,
        )

    def insert_all(
            self, schema: Type[E], values: Iterable[Mapping],
            batch_size: int = None,
    ) -> InsertAllQuery:
        return InsertAllQuery(
            adapter=self._adapter,
            schema=schema,
            values=values,
            batch_size=batch_size,
        )

    def update(self, entity: E, **values) -> UpdateObjectQuery[E]:
        return UpdateObjectQuery(
            adapter=self._adapter,
            entity=entity,
            values=values,
        )

    def update_all(
            self,
            schema: Type[E],
            values: Mapping,
            where: ExprLike = None,
            returning: Union[Field, Sequence[Field]] = None,
    ) -> UpdateAllQuery:
        return UpdateAllQuery(
            adapter=self._adapter,
            schema=schema,
            values=values,
            where=where,
            returning=returning,
        )

    def delete(self, entity: E) -> DeleteObjectQuery:
        return DeleteObjectQuery(
            adapter=self._adapter,
            entity=entity,
        )

    def delete_all(
            self, schema: Type[E],
            where: ExprLike = None,
    ) -> DeleteAllQuery:
        return DeleteAllQuery(
            adapter=self._adapter,
            schema=schema,
            where=where,
        )

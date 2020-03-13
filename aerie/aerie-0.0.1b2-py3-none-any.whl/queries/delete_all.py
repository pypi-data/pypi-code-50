from typing import Generic, Type, TypeVar

from aerie.expressions import ExprLike
from aerie.protocols import Adapter
from aerie.queries.base import AwaitableQuery
from aerie.schemas import Schema

T = TypeVar('T', bound=Schema)


class DeleteAllQuery(Generic[T], AwaitableQuery):
    def __init__(
            self,
            adapter: Adapter,
            schema: Type[T],
            where: ExprLike = None,
    ):
        self._adapter = adapter
        self._schema = schema
        self._where = where

    async def execute(self) -> None:
        await self._adapter.delete_all(
            schema=self._schema,
            where=self._where,
        )

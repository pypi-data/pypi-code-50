from typing import Generic, TypeVar

from aerie.protocols import Adapter
from aerie.queries.base import AwaitableQuery
from aerie.schemas import Schema, State

T = TypeVar('T', bound=Schema)


class DeleteObjectQuery(Generic[T], AwaitableQuery):
    def __init__(self, adapter: Adapter, entity: T):
        self._adapter = adapter
        self._entity = entity

    async def execute(self) -> T:
        schema = type(self._entity)

        await self._adapter.delete_all(
            schema=schema,
            where=schema.pk == self._entity.pk,
        )
        self._entity.__meta__.state = State.DELETED
        return self._entity

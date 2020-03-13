from typing import Generic, TypeVar

from aerie.protocols import Adapter
from aerie.queries.base import AwaitableQuery
from aerie.schemas import Schema, State

T = TypeVar('T', bound=Schema)


class InsertObjectQuery(Generic[T], AwaitableQuery):

    def __init__(self, adapter: Adapter, entity: T):
        self._adapter = adapter
        self._entity = entity

    async def execute(self) -> T:
        schema = type(self._entity)
        value = schema.deconstruct(self._entity)
        # remove pk field from value if they are nulls
        for field in schema.pk:
            if value[field.source_name] is None:
                del value[field.source_name]

        result = await self._adapter.insert_all(
            schema=schema,
            values=[value],
            returning=[*schema.pk],
        )

        self._entity.pk = [result[0][field.source_name] for field in schema.pk]
        self._entity.__meta__.state = State.LOADED
        return self._entity

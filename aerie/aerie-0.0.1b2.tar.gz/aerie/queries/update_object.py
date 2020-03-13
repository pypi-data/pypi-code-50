from typing import Generic, Mapping, TypeVar

from aerie.exceptions import DeletedEntity
from aerie.protocols import Adapter
from aerie.queries.base import AwaitableQuery
from aerie.schemas import Schema, State

T = TypeVar('T', bound=Schema)


class UpdateObjectQuery(Generic[T], AwaitableQuery):
    def __init__(self, adapter: Adapter, entity: T, values: Mapping):
        self._adapter = adapter
        self._entity = entity
        self._values = values

    async def execute(self) -> T:
        schema = type(self._entity)

        # quick checks
        if self._entity.__meta__.state == State.DELETED:
            raise DeletedEntity(
                'Entity (pk=%s, schema=%s) has been previously deleted '
                'thus cannot be updated.' % (self._entity.pk, schema.__name__),
                self._entity,
            )

        result = await self._adapter.update_all(
            schema=schema,
            values=self._values,
            where=schema.pk == self._entity.pk,
            returning=[
                schema.__meta__.fields[name]
                for name in self._values.keys()
            ]
        )

        for column, value in result[0].items():
            field = schema.__meta__.fields.by_source_name(column)
            setattr(self._entity, field.attr_name, value)

        return self._entity

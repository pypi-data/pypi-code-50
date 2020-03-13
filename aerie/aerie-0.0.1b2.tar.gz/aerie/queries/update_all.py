from typing import (Generic, Mapping, Sequence, Type, TypeVar, Union)

from aerie.expressions import ExprLike
from aerie.fields import Field
from aerie.protocols import Adapter
from aerie.queries.base import AwaitableQuery
from aerie.schemas import Schema

T = TypeVar('T', bound=Schema)


class UpdateAllQuery(Generic[T], AwaitableQuery):
    def __init__(
            self,
            adapter: Adapter,
            schema: Type[T],
            values: Mapping,
            where: ExprLike = None,
            returning: Union[Field, Sequence[Field]] = None,
    ):
        self._schema = schema
        self._adapter = adapter
        self._where = where
        self._values = values
        self._returning = returning

    async def execute(self) -> Sequence[Mapping]:
        return await self._adapter.update_all(
            schema=self._schema,
            values=self._values,
            where=self._where,
            returning=self._returning,
        )

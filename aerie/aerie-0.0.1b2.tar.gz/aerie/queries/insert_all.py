from typing import Dict, Generic, Iterable, Mapping, Type, TypeVar, Union

from aerie.collections import Collection
from aerie.protocols import Adapter
from aerie.queries.base import AwaitableQuery
from aerie.schemas import Schema

T = TypeVar('T', bound=Schema)


class InsertAllQuery(Generic[T], AwaitableQuery):
    def __init__(
            self,
            adapter: Adapter,
            schema: Type[T],
            values: Union[Mapping, Iterable[Mapping]],
            batch_size: int = None,
    ):
        self._schema = schema
        self._adapter = adapter
        self._batch_size = batch_size
        if isinstance(values, Dict):
            values = [values]
        self._values = Collection(values)

    async def execute(self) -> None:
        await self._adapter.insert_all(
            self._schema,
            self._values,
            self._batch_size,
        )

from __future__ import annotations

import enum
from typing import (AsyncGenerator, List, Literal, Mapping, Protocol, Sequence,
                    TYPE_CHECKING, Type, TypeVar, Union, Any)

from .expressions import ExprLike
from .query import QueryBuilder
from .schemas import Schema

if TYPE_CHECKING:
    from .schemas import Metadata, Schema
    from .fields import Field


class SchemaLike(Protocol):
    __meta__: Metadata


class OnConflict(enum.Enum):
    IGNORE = 'ignore'
    UPDATE = 'update'


E = TypeVar('E', bound=Schema)
MAP_TO = TypeVar('MAP_TO')


class Queryable(Protocol):
    def to_expr(self):
        raise NotImplementedError()


class Adapter(Protocol[E]):

    def insert_all(
            self,
            schema: Type[E],
            values: Sequence[Mapping],
            batch_size: int = None,
            on_conflict: Literal[OnConflict.IGNORE, OnConflict.UPDATE] = None,
            conflict_target: Field = None,
            replace_fields: Sequence[Field] = None,
            returning: Union[Field, Sequence[Field]] = None,
    ):
        """Insert an multiple entities at once into the data store."""
        raise NotImplementedError()

    async def update_all(
            self,
            schema: Type[E],
            values: Mapping,
            where: ExprLike = None,
            returning: Union[Field, Sequence[Field]] = None,
    ) -> List[Mapping]:
        """Update all entities matched by `filters` clause."""
        raise NotImplementedError()

    async def delete_all(
            self, schema: Type[E], where: ExprLike = None,
    ) -> None:
        """Delete all entities matched by `filters` clause."""
        raise NotImplementedError()

    async def fetch_all(
            self,
            query: Any,
            values: Mapping = None,
    ) -> List[Mapping]:
        raise NotImplementedError()

    def iterate(
            self, query: Any, values: Mapping = None,
    ) -> AsyncGenerator[Mapping, None]:
        raise NotImplementedError()

    async def execute(
            self,
            query: Any,
            values: Union[Mapping, Sequence[Mapping]] = None
    ):
        raise NotImplementedError()

    async def exists(self, query: Any) -> bool:
        raise NotImplementedError()

    async def count(self, query: Any) -> int:
        raise NotImplementedError()

    def to_string(self, query: QueryBuilder) -> str:
        raise NotImplementedError()

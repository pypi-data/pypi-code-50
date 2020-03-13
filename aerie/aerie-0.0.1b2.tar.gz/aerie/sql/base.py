from typing import Generic, TypeVar

from aerie.schemas import Schema

T = TypeVar('T', bound=Schema)


class SQLAdapter(Generic[T]):
    pass

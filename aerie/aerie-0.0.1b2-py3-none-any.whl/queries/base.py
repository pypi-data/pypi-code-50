from __future__ import annotations

from typing import Any

from aerie.protocols import Adapter


class AwaitableQuery:
    async def execute(self) -> Any:
        raise NotImplementedError()

    def __await__(self):
        return self.execute().__await__()


class BaseQuery(AwaitableQuery):
    _adapter: Adapter

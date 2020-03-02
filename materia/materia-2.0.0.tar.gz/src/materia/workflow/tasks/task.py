from __future__ import annotations
import materia
from typing import Any, Iterable, Optional

__all__ = ["Task"]


class Task:
    def __init__(
        self,
        handlers: Optional[Iterable[materia.Handler]] = None,
        name: Optional[str] = None,
    ) -> None:
        self.handlers = handlers or []
        self.name = name or ""
        self.requirements = ([], {})

    def requires(self, *args: Task, **kwargs: Task) -> None:
        self.requirements = (args, kwargs)

    def run(self, **kwargs: Any) -> Any:
        raise NotImplementedError

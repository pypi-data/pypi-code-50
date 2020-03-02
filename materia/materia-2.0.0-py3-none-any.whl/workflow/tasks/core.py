from __future__ import annotations
import functools
import subprocess
from typing import Any, Callable, Iterable, Optional

from .task import Task
from ..handlers import Handler

__all__ = ["FunctionTask", "InputTask", "ShellCommand"]


class FunctionTask(Task):
    def __init__(
        self,
        f: Callable,
        handlers: Optional[Iterable[Handler]] = None,
        name: Optional[str] = None,
    ) -> None:
        super().__init__(handlers=handlers, name=name)
        self.f = f

    def run(self, **kwargs) -> None:
        return self.f(**kwargs)


class InputTask(Task):
    def __init__(
        self,
        value: Any,
        handlers: Optional[Iterable[Handler]] = None,
        name: Optional[str] = None,
    ) -> None:
        super().__init__(handlers=handlers, name=name)
        self.value = value

    def run(self) -> Any:
        return self.value


class ShellCommand(Task):
    def __init__(
        self,
        command: str,
        handlers: Optional[Iterable[Handler]] = None,
        name: Optional[str] = None,
    ) -> None:
        super().__init__(handlers=handlers, name=name)
        self.command = command

    def run(self) -> None:
        subprocess.call(self.command.split())


def task(
    f: Callable = None,
    handlers: Optional[Iterable[Handler]] = None,
    name: Optional[str] = None,
) -> FunctionTask:
    # FIXME: this is incomptabile with materia.Workflow.run(thread=False) (i.e. with multiprocessing) because FunctionTask cannot be serialized!
    if f is None:
        return functools.partial(task, handlers=handlers, name=name)

    return FunctionTask(f=f, handlers=handlers, name=name)

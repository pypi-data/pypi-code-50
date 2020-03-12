from dataclasses import dataclass
from typing import Callable


@dataclass
class Stage:
    name: str
    callback: Callable
    priority: int = 100

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def __call__(self, *args, **kwargs):
        return self.callback(*args, **kwargs) or {}

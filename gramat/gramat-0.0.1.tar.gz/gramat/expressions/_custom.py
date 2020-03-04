from __future__ import annotations

from typing import List, Callable

from ._expression import Expression
from ._expression import EvalContext


class CustomExp(Expression):

    def __init__(self, custom_eval: Callable[[EvalContext], bool]):
        self.custom_eval = custom_eval

    def eval(self, ctx: EvalContext) -> bool:
        return self.custom_eval(ctx)

    @property
    def children(self) -> List[Expression]:
        return []

    def optimize(self) -> CustomExp:
        return self

    def __str__(self) -> str:
        return f'Custom<{self.custom_eval}>'

from __future__ import annotations

from typing import List

from ._expression import Expression
from ._expression import EvalContext


class TrueExp(Expression):

    def eval(self, ctx: EvalContext) -> bool:
        return True

    @property
    def children(self) -> List[Expression]:
        return []

    def optimize(self) -> Expression:
        return self

    def __str__(self) -> str:
        return 'True'

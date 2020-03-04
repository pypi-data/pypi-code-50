from __future__ import annotations

from typing import List, Optional

from ._expression import Expression
from ._expression import EvalContext


class ReferenceExp(Expression):

    def __init__(self, name: str):
        self.name = name
        self.target: Optional[Expression] = None

    def eval(self, ctx: EvalContext) -> bool:
        if self.target is None:
            raise self.error(f'rule not resolved: {self.name}')

        return self.target.eval(ctx)

    @property
    def children(self) -> List[Expression]:
        return []

    def optimize(self) -> Expression:
        if self.target is None:
            raise self.error('missing target')
        return self.target

    def __str__(self) -> str:
        return f'Reference<{self.name}>'

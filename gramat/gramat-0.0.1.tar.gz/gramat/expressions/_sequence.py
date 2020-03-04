from __future__ import annotations

from typing import List

from ._true import TrueExp
from ._expression import Expression
from ._expression import EvalContext


class SequenceExp(Expression):

    def __init__(self, items: List[Expression]):
        self.items = items

    def eval(self, ctx: EvalContext) -> bool:
        pos0 = ctx.source.position

        for item in self.items:
            if not item.eval(ctx):
                ctx.source.position = pos0
                return False

        return True

    @property
    def children(self) -> List[Expression]:
        return list(self.items)

    def optimize(self) -> Expression:
        if len(self.items) == 0:
            return TrueExp()
        elif len(self.items) == 1:
            return self.items[0].optimize()

        for i, item in enumerate(self.items):
            self.items[i] = item.optimize()

        return self

    def __str__(self) -> str:
        return f'Sequence<{len(self.items)} item(s)>'

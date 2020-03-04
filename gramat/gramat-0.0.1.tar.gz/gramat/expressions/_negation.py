from __future__ import annotations

from typing import List

from ._expression import Expression
from ._expression import EvalContext


class NegationExp(Expression):

    def __init__(self, expression: Expression):
        self.expression = expression

    def eval(self, ctx: EvalContext) -> bool:
        pos0 = ctx.source.position

        if self.expression.eval(ctx):
            ctx.source.position = pos0
            return False

        ctx.source.move_next()
        return True

    @property
    def children(self) -> List[Expression]:
        return [self.expression]

    def optimize(self) -> Expression:
        self.expression = self.expression.optimize()

        # Double negation optimization
        if isinstance(self.expression, NegationExp):
            return self.expression.expression

        return self

    def __str__(self) -> str:
        return f'Negation<{self.expression}>'

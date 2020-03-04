from __future__ import annotations

from typing import List

from ._expression import Expression
from ._expression import EvalContext


class OptionalExp(Expression):

    def __init__(self, expression: Expression):
        self.expression = expression

    def eval(self, ctx: EvalContext) -> bool:
        pos0 = ctx.source.position

        if not self.expression.eval(ctx):
            ctx.source.position = pos0

        return True

    @property
    def children(self) -> List[Expression]:
        return [self.expression]

    def optimize(self) -> Expression:
        self.expression = self.expression.optimize()

        # Double optional
        if isinstance(self.expression, OptionalExp):
            self.expression = self.expression.expression

        # TODO check for optionals wrapping repetitions with min=0

        return self

    def __str__(self) -> str:
        return f'Optional<{self.expression}>'

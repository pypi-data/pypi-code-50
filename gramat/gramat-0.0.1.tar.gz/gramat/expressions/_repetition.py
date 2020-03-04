from __future__ import annotations

from typing import List, Optional

from ._expression import Expression
from ._expression import EvalContext


class RepetitionExp(Expression):

    def __init__(
            self,
            expression: Expression,
            separator: Optional[Expression] = None,
            min_count: Optional[int] = None,
            max_count: Optional[int] = None):
        self.expression = expression
        self.separator = separator
        self.min_count = min_count
        self.max_count = max_count

    def eval(self, ctx: EvalContext) -> bool:
        pos0 = ctx.source.position
        hits = 0
        expect_more = False

        while self.expression.eval(ctx):
            if self.separator is not None:
                if self.separator.eval(ctx):
                    expect_more = True
                else:
                    expect_more = False
                    break

            hits += 1

            if self.max_count is not None and hits >= self.max_count:
                break

        if expect_more:
            ctx.source.position = pos0
            return False
        elif self.min_count is not None and hits < self.min_count:
            ctx.source.position = pos0
            return False

        return True

    @property
    def children(self) -> List[Expression]:
        children = [self.expression]

        if self.separator is not None:
            children.append(self.separator)

        return children

    def optimize(self) -> Expression:
        self.expression = self.expression.optimize()

        if self.separator is not None:
            self.separator = self.separator.optimize()

        return self

    def __str__(self) -> str:
        # TODO add min and max
        return f'Repetition<{self.expression},{self.separator}>'

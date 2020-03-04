from __future__ import annotations

from typing import List

from ._expression import Expression
from ._expression import Match
from ._expression import EvalContext


class RuleExp(Expression):

    def __init__(
            self,
            name: str,
            expression: Expression,
            soft: bool = False):
        self.name = name
        self.expression = expression
        self.soft = soft

    def eval(self, ctx: EvalContext) -> bool:
        pos0 = ctx.source.position

        match = Match(self, ctx.source.position)

        ctx.push_match(match)

        result = self.expression.eval(ctx)

        match.result = result
        match.end = ctx.source.position

        ctx.pop_match()

        pos_f = ctx.source.position

        if result and pos0 != pos_f:
            ctx.right = self
            ctx.right_position_0 = pos0
            ctx.right_position_f = pos_f
            ctx.wrongs = []
        else:
            # if loc_0 > ctx.right_location:
            ctx.wrongs.append(self)

        if not result:
            if ctx.error_position is None or pos_f > ctx.error_position:
                ctx.error_position = pos_f
                ctx.error_expressions = [self]
            elif pos_f == ctx.error_position:
                ctx.error_expressions.append(self)

        return result

    @property
    def children(self) -> List[Expression]:
        return [self.expression]

    def optimize(self) -> RuleExp:
        self.expression = self.expression.optimize()

        if self.soft:
            return self.expression

        return self

    def __str__(self) -> str:
        return f'Rule<{self.name}>'

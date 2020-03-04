from __future__ import annotations

from typing import List

from ._expression import Expression
from ._expression import EvalContext


def eval_char_literal(ctx: EvalContext, unicode: int):
    c = ctx.source.peek()

    if c is None or ord(c) != unicode:
        return False

    ctx.source.move_next()
    return True


class CharLiteralExp(Expression):

    def __init__(self, unicode: int):
        self.unicode = unicode

    def eval(self, ctx: EvalContext) -> bool:
        return eval_char_literal(ctx, self.unicode)

    @property
    def children(self) -> List[Expression]:
        return []

    def optimize(self) -> CharLiteralExp:
        return self

    def __str__(self) -> str:
        return f'CharLiteral<{self.unicode}>'

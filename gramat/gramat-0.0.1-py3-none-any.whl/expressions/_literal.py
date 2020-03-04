from __future__ import annotations

from typing import List

from . import CharLiteralExp
from ._expression import Expression
from ._expression import EvalContext


class LiteralExp(Expression):

    def __init__(self, text: str):
        self.text = text

    def eval(self, ctx: EvalContext) -> bool:
        pos0 = ctx.source.position

        for expected_char in self.text:
            actual_char = ctx.source.peek()

            if actual_char is None or actual_char != expected_char:
                ctx.source.position = pos0
                return False

            ctx.source.move_next()

        return True

    @property
    def children(self) -> List[Expression]:
        return []

    def optimize(self) -> Expression:
        if len(self.text) == 1:
            return CharLiteralExp(ord(self.text))
        return self

    def __str__(self) -> str:
        escaped = self.text.replace('\n', '\\n').replace('\r', '\\r')
        return f'Literal<{escaped}>'

from __future__ import annotations

from typing import List

from ._expression import Expression
from ._expression import EvalContext


def eval_char_range(ctx: EvalContext, begin_unicode: int, end_unicode: int):
    c = ctx.source.peek()

    if c is None:
        return False

    unicode = ord(c)

    if begin_unicode <= unicode <= end_unicode:
        ctx.source.move_next()
        return True

    return False


class CharRangeExp(Expression):

    def __init__(self, begin_unicode: int, end_unicode: int):
        self.begin_unicode = begin_unicode
        self.end_unicode = end_unicode

    def eval(self, ctx: EvalContext) -> bool:
        return eval_char_range(ctx, self.begin_unicode, self.end_unicode)

    @property
    def children(self) -> List[Expression]:
        return []

    def optimize(self) -> CharRangeExp:
        return self

    def __str__(self) -> str:
        return f'CharRange<{self.begin_unicode},{self.end_unicode}>'

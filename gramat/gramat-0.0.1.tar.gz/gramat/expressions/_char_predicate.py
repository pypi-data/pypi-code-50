from __future__ import annotations

from typing import List

from ._char_literal import CharLiteralExp, eval_char_literal
from ._char_range import CharRangeExp, eval_char_range
from ._expression import Expression
from ._expression import EvalContext

LIT = 1
RAN = 2


class CharPredicateExp(Expression):

    def __init__(self):
        self._items: List[tuple] = []

    def append_literal(self, char: str):
        self._items.append(
            (LIT, ord(char),)
        )

    def append_range(self, begin_char: str, end_char: str):
        self._items.append(
            (RAN, ord(begin_char), ord(end_char),)
        )

    def eval(self, ctx: EvalContext) -> bool:
        pos0 = ctx.source.position

        for item in self._items:
            if item[0] == LIT and eval_char_literal(ctx, item[1]):
                return True
            elif item[0] == RAN and eval_char_range(ctx, item[1], item[2]):
                return True

            ctx.source.position = pos0

        return False

    @property
    def children(self) -> List[Expression]:
        return []

    def optimize(self) -> Expression:
        if len(self._items) == 1:
            item = self._items[0]

            if item[0] == LIT:
                return CharLiteralExp(item[1])
            elif item[0] == RAN:
                return CharRangeExp(item[1], item[2])
            else:
                raise self.error(f'Unknown type: {item[0]}')

        return self

    def __str__(self) -> str:
        return f'CharPredicate<>'

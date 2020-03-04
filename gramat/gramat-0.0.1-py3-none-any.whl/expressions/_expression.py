from __future__ import annotations

from typing import List, Optional

from gramat.errors import GramatError
from gramat.parsing.location import Area
from gramat.parsing.source import Source


class Element:

    pass


class Match:

    def __init__(self, rule: 'RuleExp', begin: int):
        self.rule = rule
        self.begin = begin
        self.end: Optional[int] = None
        self.result: Optional[bool] = None
        self.items: List[Match] = []


class EvalContext:

    def __init__(self, source: Source):
        self.source = source
        self.match_stack: List[Match] = []
        self.matches: List[Match] = []
        self.indentation = 0  # TODO remove this value

        self.error_position = None
        self.error_expressions = None

        self.right = None
        self.right_position_0 = None
        self.right_position_f = None
        self.wrongs = []

    def push_match(self, match: Match):
        self.match_stack.append(match)

    def pop_match(self):
        match = self.match_stack.pop()

        if len(self.match_stack) > 0:
            lst = self.match_stack[-1].items
        else:
            lst = self.matches

        lst.append(match)


class Expression(Element):

    parent: Optional[Expression] = None

    area: Optional[Area] = None

    _debug = False

    def error(self, message: str) -> GramatError:
        if self.area is None:
            return GramatError(message)
        return self.area.error(message)

    def eval(self, ctx: EvalContext) -> bool:
        raise NotImplementedError()

    @property
    def children(self) -> List[Expression]:
        raise NotImplementedError()

    def optimize(self) -> Expression:
        raise NotImplementedError()

    def __str__(self) -> str:
        raise NotImplementedError()

    def debug(self):
        if self._debug:
            return

        self._debug = True

        for child in self.children:
            child.debug()

        eval0 = self.eval

        def eval_debug(ctx: EvalContext):
            indentation = ' ' * ctx.indentation

            print(
                f'{indentation}{self} '
                f'= ... ({ctx.source.location.short_desc})')

            ctx.indentation += 1

            result = eval0(ctx)

            ctx.indentation -= 1

            print(
                f'{indentation}{self} '
                f'= {result} ({ctx.source.location.short_desc})')

            return result

        setattr(self, 'eval', eval_debug)

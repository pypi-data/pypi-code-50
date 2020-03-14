import ast
from typing import List

from flake8_plugin_utils import Visitor

from .errors import UnnecessaryBackslashEscapingError


class StringsVisitor(Visitor):
    lines: List[str]

    def _is_escaped_char(self, character: str) -> bool:
        repr_c = repr(character)
        return repr_c[1] == '\\' and repr_c[2] != '\\'

    def visit_Str(self, node: ast.Str) -> None:  # noqa: N802
        if '\\' not in node.s:
            return
        if node.s[-1] == '\\':
            return
        if any(self._is_escaped_char(c) for c in node.s):
            return
        if self.lines[node.lineno - 1][node.col_offset] == 'r':
            return
        self.error_from_node(UnnecessaryBackslashEscapingError, node)

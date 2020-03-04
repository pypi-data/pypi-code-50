from __future__ import annotations

from typing import Dict

from gramat.errors import GramatError
from gramat.expressions import Expression


class Grammar:

    def __init__(self):
        self.rules: Dict[str, Expression] = {}

    def get_rule(self, name: str) -> Expression:
        expression = self.rules.get(name, None)

        if expression is None:
            raise GramatError(f'Rule not found: {name}')

        return expression

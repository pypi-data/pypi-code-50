from typing import Type

from flake8_plugin_utils import Plugin
from flake8_plugin_utils.plugin import TConfig, Visitor

from .visitor import StringsVisitor


class StringsPlugin(Plugin):
    name = 'Strings'
    version = '0.0.0'
    visitors = [StringsVisitor]

    def _create_visitor(self, visitor_cls: Type[Visitor[TConfig]]) -> Visitor[TConfig]:
        visitor = visitor_cls()
        visitor.lines = self._lines
        return visitor

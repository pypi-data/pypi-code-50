import os
import sys
import ast

from ast import AST
from typing import Union

from .base import TableMeta
from .table import Table

class NodeVistor(ast.NodeVisitor):
    def __init__(self, module):
        self.module = module
        self.tables = []
        super().__init__()

    def visit_ClassDef(self, node: ast.FunctionDef):
        if isinstance(getattr(self.module, node.name), TableMeta):
            # instance
            self.tables.append(getattr(self.module, node.name)())
        self.generic_visit(node)

    def visit_Assign(self, node: ast.Assign):
        self._get_table_from_assign_node(*node.targets)
        self.generic_visit(node)

    def _get_table_from_assign_node(self, *names:ast.Name):
        for name in names:
            if getattr(self.module, name.id, None) and isinstance(getattr(self.module, name.id), Table):
                self.tables.append(getattr(self.module, name.id))

    def visit_AnnAssign(self, node:ast.AnnAssign) -> None:
        self._get_table_from_assign_node(node.target)
        self.generic_visit(node)

class SrcTables(object):
    def __init__(self, src_file):
        self._tables = []

        # load module 
        self.src_file = src_file
        abs_path = os.path.abspath(os.path.expanduser(src_file))

        path, ext = os.path.splitext(abs_path)
        module_name = os.path.basename(path)
        module_dir = os.path.dirname(path)

        sys.path.append(module_dir)
        self._src_module = __import__(module_name)
        self.vistor = NodeVistor(self._src_module)
        tree = ast.parse(open(abs_path).read())
        self.vistor.visit(tree)

    @property
    def tables(self):
        return self.vistor.tables

        
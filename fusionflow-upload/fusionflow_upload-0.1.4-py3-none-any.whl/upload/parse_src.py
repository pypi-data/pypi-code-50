import os
import sys
import ast
from functools import partial
import warnings


from .base import TableMeta, PartialTable
from .table import Table
from .utils import get_module_configs


class NodeVistor(ast.NodeVisitor):
    def __init__(self, module):
        self.module = module
        self.tables = []
        super().__init__()

    def visit_FunctionDef(self, node: ast.FunctionDef):
        for sub_node in node.body:
            # TODO: find class node and extract base name
            # need register all table name in module to judge
            # if base is subclass of any instance of ``TableMeta``
            ...
        self.generic_visit(node)

    def visit_ClassDef(self, node: ast.ClassDef):
        # class in function body not included
        if getattr(self.module, node.name, None) and \
                   isinstance(getattr(self.module, node.name), TableMeta):
            # instance
            self.tables.append(getattr(self.module, node.name)())
        self.generic_visit(node)

    def visit_Assign(self, node: ast.Assign):
        """assignment can be ``cls.attribute``

        :param node: parsed node
        :type node: ast.Assign
        """
        for target in node.targets:
            if isinstance(target, ast.Name):
                self._get_table_from_assign_node(target)
        self.generic_visit(node)

    def _get_table_from_assign_node(self, *names: ast.Name):
        for name in names:
            tmp_value = getattr(self.module, name.id, None)
            if tmp_value and isinstance(tmp_value, (Table, PartialTable)):
                self.tables.append(getattr(self.module, name.id))

    def visit_AnnAssign(self, node: ast.AnnAssign) -> None:
        self._get_table_from_assign_node(node.target)  # type: ignore
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
        self.visitor = NodeVistor(self._src_module)
        tree = ast.parse(open(abs_path).read())
        self.visitor.visit(tree)

        # collect configures
        self.configs = get_module_configs(self._src_module)
        errors = {}
        # add config
        for idx, table in enumerate(self.visitor.tables):
            # get missing parameters
            if isinstance(table, partial):
                # missed contains in configs
                found = {}
                # already missed
                missed = table.missing.copy()

                for miss_param in table.missing:
                    if miss_param not in self.configs:
                        # default native datetime timezone,
                        # will removed in the future
                        if miss_param == "timezone":
                            warnings.warn("""implicit native datetime timezone setting is support
                                    in the future, set it explicitly later
                                    currently as GMT+08(PRC), because of
                                    our users mainly in Asia/Shanghai
                                    """, PendingDeprecationWarning)
                            missed.remove(miss_param)
                            found["timezone"] = "GMT+08"
                        else:
                            errors.setdefault(table, []).append(miss_param)
                    else:
                        found.update({miss_param: self.configs[miss_param]})
                        missed.remove(miss_param)

                if not missed:
                    # only instantiate it, if not errors happens till now
                    self.visitor.tables[idx] = table(**found)

        if errors:
            raise ValueError("""parameters missing:\n""".join(
                                "{table}:\t{params}\n".format(
                                    table=table, params=", ".join(params)
                                    )
                                for table, params in errors.items()
                            ))

    @property
    def tables(self):
        return self.visitor.tables

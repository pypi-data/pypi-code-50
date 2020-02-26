from __future__ import annotations
from nltk import tree
from alanbootstrap.utils import constants

import os
import json
import typing


class AST(tree.Tree):
    """
    Base class for AST nodes.
    """
    def __init__(self, name, children):
        self.complexity = None
        self.data = dict()
        super(AST, self).__init__(name, children=children)

    def get_type(self) -> str:
        raise NotImplementedError

    def preorder(self, parent=False, max_len=-1, is_root=True) -> typing.List:
        """
        Flatten AST by pre-order transversal.
        :param parent boolean or AST, default=False
            If parent is True or AST, return list of (AST, parent) tuples by pre-order transversal.
            Otherwise return list of AST only.
        :param max_len int, default=-1
            The maximum number of nodes in the tree. If larger than this number, then ignore the nodes at the end.
            If max_len is negative, keep all the nodes.
        """
        if len(self) == 0:
            if parent:
                return [(self, parent if isinstance(parent, AST) else None)]
            else:
                return [self]

        if parent:
            res = [(self, parent if isinstance(parent, AST) else None)]
        else:
            res = [self]

        for child in self:
            if parent:
                res.extend(child.preorder(parent=self, is_root=False))
            else:
                res.extend(child.preorder(is_root=False))

        if is_root and 0 <= max_len < len(res):
            res = res[:max_len]
        return res

    @classmethod
    def from_shared_ast_json_file(cls, file_path, data_keys=None):
        with open(file_path, 'r') as fp:
            shared_ast_json = json.load(fp)

        return [
            AST.from_shared_ast_json(json_, data_keys=data_keys) for json_ in shared_ast_json[constants.SHARED_AST_DATA]
        ]

    @classmethod
    def from_shared_ast_json(cls, sast_json, data_keys=None):
        sast_str = sast_json[constants.SHARED_AST]

        sast_str = sast_str.replace('\t', '')
        sast_str = sast_str.replace('\n', '')

        ast = AST.from_shared_ast(sast_str)

        if constants.SHARED_AST_RB_COMPLEXITY in sast_json:
            ast.complexity = sast_json[constants.SHARED_AST_RB_COMPLEXITY]

        if data_keys is not None:
            keys_in_json = list(filter(
                lambda key_: key_ in sast_json,
                data_keys
            ))

            for key_ in keys_in_json:
                ast.data[key_] = sast_json[key_]

        return ast

    @classmethod
    def from_shared_ast(cls, sast_str):
        sast_str = sast_str.strip()
        if sast_str.startswith("<"):
            # table, column, or value
            # remove <>
            sast_str = sast_str.replace('<', '').replace('>', '')
            # parse as table, column and value accordingly
            if sast_str.startswith(constants.SHARED_AST_TABLE):
                name = sast_str.replace(constants.SHARED_AST_TABLE + ': ', '')
                return Table(name)
            if sast_str.startswith(constants.SHARED_AST_Column):
                column_table = sast_str.replace(constants.SHARED_AST_Column + ': ', '')
                if '.' in column_table:
                    table, column = column_table.split('.', maxsplit=1)
                    return Column(column, table_name=table)
                else:
                    return Column(column_table)
            if sast_str.startswith(constants.SHARED_AST_VALUE):
                name = sast_str.replace(constants.SHARED_AST_VALUE + ': ', '')
                return Value(name)

        elif sast_str == constants.SHARED_AST_STAR:
            # kleene star star
            return Star()

        elif sast_str.endswith(')'):
            # rules
            rule_name, rest_ast = sast_str.split('(', maxsplit=1)
            # remove the tailing close parenthese
            rest_ast = rest_ast[:len(rest_ast)-1]
            # split by comma
            rest_ast_str_list = AST.split_shared_ast_list_str_(rest_ast)

            children = [AST.from_shared_ast(rest_ast_) for rest_ast_ in rest_ast_str_list]

            return Rule(rule_name, children)
        else:
            raise ValueError("unknown str: " + sast_str)

    @classmethod
    def split_shared_ast_list_str_(cls, sast_str):
        res = list()

        stack = list()
        head = 0
        for i in range(len(sast_str)):
            cur_char = sast_str[i]
            if cur_char == "(":
                stack.append(cur_char)
            elif cur_char == ")":
                # assume input is valid
                stack.pop(-1)
            elif cur_char == ",":
                if len(stack) == 0:
                    # a valid AST node string segment
                    res.append(sast_str[head:i].strip())
                    head = i+1

        if head < len(sast_str):
            res.append(sast_str[head:])
        return res


class Table(AST):

    def __init__(self, name):
        self.name = name
        super(Table, self).__init__(name + "|TBL", list())

    def get_type(self) -> str:
        return constants.AST_TABLE


class Column(AST):

    def __init__(self, name, table_name=None):
        self.table_name = table_name
        self.name = name
        if table_name is not None:
            super(Column, self).__init__(table_name + "." + name + "|COL", list())
        else:
            super(Column, self).__init__(name + "|COL", list())

    def get_type(self) -> str:
        return constants.AST_COLUMN

class Value(AST):

    def __init__(self, name):
        self.name = name
        super(Value, self).__init__(name + "|VAL", list())

    def get_type(self) -> str:
        return constants.AST_VALUE


class Star(AST):

    def __init__(self):
        super(Star, self).__init__('STAR', list())

    def get_type(self) -> str:
        return constants.AST_STAR


class Rule(AST):

    def __init__(self, name: str, children: typing.List):
        super(Rule, self).__init__(name, children)

    def get_type(self) -> str:
        return self.label()


def collect_unique_ast_types(asts: typing.Sequence[AST]):
    flat_asts = [ast_.preorder() for ast_ in asts]

    type_sets = [
        set(
            [node_.get_type() for node_ in ast_]
        ) for ast_ in flat_asts
    ]

    types = set()
    for ast_types in type_sets:
        types = types.union(ast_types)

    return types

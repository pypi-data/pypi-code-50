from ast import parse, Import, FunctionDef, Assign, Call, Num, Attribute, Name, Expr, NodeVisitor, For
import warnings
import math


class IllegalStatementExc(Exception):
    def __init__(self, msg=None, lineno=None):
        super().__init__(self, msg)
        self.lineno = lineno
        self.msg = msg


class IllegalImportExc(IllegalStatementExc):
    pass


class IllegalCallExc(IllegalStatementExc):
    pass


class IllegalFuncionDefExc(IllegalStatementExc):
    pass


class IllegalExprExc(IllegalStatementExc):
    pass


class IllegalAssignmentExc(IllegalStatementExc):
    pass


class IllegalStatementTypeExc(IllegalStatementExc):
    pass

class Code:

    def __init__(self, code_str):
        """
        Container for code

        Args:
            code_str(str): Code in string representation
        """

        self.code_str = code_str

    @property
    def code_lines(self):
        """Returns code as list (each line is a list element)"""

        return self.code_str.split("\n")

    @property
    def code_tree(self):
        """Returns ast root node"""
        return parse(self.code_str)

    def print_code_lines(self):
        """Prints code with line numbers"""
        for i, line in enumerate(self.code_lines):
            print("{}: {}".format(i + 1, line))


class CodeChecker(NodeVisitor):

    def __init__(self, allowed_imports=None, allowed_calls=None, allowed_names=None, allowed_aliases=None,
                 allowed_FunctionDefs=None):
        """
        Checker for illegal statements in code

        Args:
            allowed_imports(list): List of allowed imports
            allowed_calls(list): List of allowed calls
            allowed_names(list): List of allowed names (e.g. function names not covered in methods of allowed aliases)
            allowed_aliases(list): List of allowed module/class/function aliases
            allowed_FunctionDefs(list): List of allowed names for Function definition

        Attributes:
            allowed_imports(list): List of allowed imports
            allowed_calls(list): List of allowed calls
            allowed_names(list): List of allowed names (e.g. function names not covered in methods of allowed aliases)
            allowed_aliases(list): List of allowed module/class/function aliases
            allowed_node_types(list): List of node ast node types (Classes) - defaults to Import, FunctionDef, Assign,
            Call and Expr
            allowed_FunctionDefs(list): List of allowed names for Function definition
        """
        super().__init__()

        if allowed_imports is None:
            self.allowed_imports = []
        else:
            self.allowed_imports = allowed_imports

        if allowed_calls is None:
            self.allowed_calls = []
        else:
            self.allowed_calls = allowed_calls

        if allowed_names is None:
            self.allowed_names = []
        else:
            self.allowed_names = allowed_names

        if allowed_aliases is None:
            self.allowed_aliases = []
        else:
            self.allowed_aliases = allowed_aliases

        if allowed_FunctionDefs is None:
            self.allowed_FunctionDefs = []
        else:
            self.allowed_FunctionDefs = allowed_FunctionDefs

        self.allowed_node_types = [Import, FunctionDef, Assign, Call, Expr, For]

        # self.__error_log__ = []

    def check_code(self, code):
        """Checks if the code is valid

        Args:
            code(Code): Code object to analyze

        Returns:
            tuple: consisting of:

                * bool: True if code is valid
                * list: Error log
        """

        print(code.code_str)
        # self.clear_error_logs()
        __error_log__ = []
        # 1st pass - check for illegal node types
        try:
            self.first_pass(code)
        except IllegalStatementTypeExc as e:
            __error_log__.append({"line": e.lineno, "error": e.msg})
        except SyntaxError or IllegalStatementTypeExc as e:
            __error_log__.append({"error": "syntax error", "line": e.lineno})

        # 2nd pass - check for illegal statements
        try:
            self.visit(code.code_tree)
        except IllegalStatementExc as e:
            __error_log__.append({"line": e.lineno, "error": e.msg})
        except SyntaxError as e:
            __error_log__.append({"error": "syntax error", "line": e.lineno})

        error_log = []
        if len(__error_log__) > 0:
            valid = False
            # append code line contents
            for log in __error_log__:
                line = log["line"]
                error_log.append("CodeChecker found {} in line {}: {}".format(log["error"], line, code.code_lines[line-1]))

        else:
            valid = True

        return valid, error_log

    def first_pass(self, code):
        """Check if nodes are in allowed node types

        Args:
            code(Code):
        """

        for node in code.code_tree.body:
            if type(node) in self.allowed_node_types:
                pass
            else:
                line = node.lineno
                error = "illegal node type \"{}\"".format(type(node))
                raise IllegalStatementTypeExc(msg=error, lineno=line)
                #warnings.warn(error)
                # self.__error_log__.append({"line": line, "error": error})

    def generic_visit(self, node):
        # print(type(node).__name__)
        NodeVisitor.generic_visit(self, node)
        # try:
        #     NodeVisitor.generic_visit(self, node)
        # except IllegalStatementExc as e:
        #     self.__error_log__.append({"line": e.lineno, "error": e.msg})

    def visit_Import(self, node):
        # self.import_errors = []
        line = node.lineno
        for name in node.names:
            if name.name not in self.allowed_imports:
                raise IllegalImportExc("illegal import \"{}\"".format(name.name), line)
                # error = "illegal import \"{}\"".format(name.name)
                # # warnings.warn(error)
                # self.__error_log__.append({"line": line, "error": error})
        self.generic_visit(node)

    def visit_Call(self, node):
        # self.call_errors = []
        func = node.func
        line = node.lineno
        if type(func) == Name:
            func_id = ""
            call = func.id
        else:  # type == Attribute
            func_id = func.value.id
            call = func_id + "." + func.attr
        if call in self.allowed_calls or func_id in self.allowed_aliases:
            pass
        else:
            error = "illegal call to \"{}\"".format(call)
            raise IllegalCallExc(msg=error, lineno=line)
            # warnings.warn(error)
            # self.__error_log__.append({"line": line, "error": error})
        self.generic_visit(node)

    def visit_FunctionDef(self, node):
        line = node.lineno
        if node.name not in self.allowed_FunctionDefs:
            error = "illegal function definition \"{}\"".format(node.name)
            raise IllegalFuncionDefExc(msg=error, lineno=line)
            # warnings.warn(error)
            # self.__error_log__.append({"line": line, "error": error})
        self.generic_visit(node)

    def visit_Expr(self, node):
        line = node.lineno
        if type(node.value) == Call:
            if type(node.value.func) == Name:
                if node.value.func.id in self.allowed_calls:
                    pass
                else:
                    error = "illegal call to \"{}\"".format(node.value.func.id)
                    raise IllegalExprExc(msg=error, lineno=line)
                    # self.__error_log__.append({"line": line, "error": error})
            elif type(node.value.func) == Attribute:
                try:
                    name_space = node.value.func.value.id
                    attr = node.value.func.attr
                except AttributeError:
                    name_space = node.value.func.value.value.id
                    attr = node.value.func.value.attr
                if name_space in self.allowed_aliases:
                    pass
                else:
                    error = "illegal call to \"{}.{}\"".format(name_space, attr)
                    raise IllegalCallExc(msg=error, lineno=line)
                    # self.__error_log__.append({"line": line, "error": error})
        else:
            error = "illegal Expr of type {}".format(type(node.value))
            raise IllegalCallExc(msg=error, lineno=line)
            # self.__error_log__.append({"line": line, "error": error})
        self.generic_visit(node)

    def visit_Assign(self, node):
        line = node.lineno
        if type(node.value) == Num:  # this is the expected assignment for a constant definition
            pass
        elif type(node.value) == Name:  # this could be assignment to another variable, but could also be a function
            if node.value.id in self.allowed_names:
                pass
            else:
                error = "illegal name \"{}\"".format(node.value.id)
                raise IllegalAssignmentExc(msg=error, lineno=line)
                # warnings.warn(error)
                # self.__error_log__.append({"line": line, "error": error})
        elif type(node.value) == Attribute:  # e.g. np.pi
            attr_id = node.value.value.id
            if attr_id in self.allowed_aliases:
                pass
            else:
                error = "illegal parent name for attribute \"{}\"".format(attr_id)
                raise IllegalAssignmentExc(msg=error, lineno=line)
                # warnings.warn(error)
                # self.__error_log__.append({"line": line, "error": error})

        self.generic_visit(node)
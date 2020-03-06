# vim: expandtab tabstop=4 shiftwidth=4

from collections import Counter

import astroid

from pylint.checkers import BaseChecker
from pylint.interfaces import IAstroidChecker

def decorator_names(node):
    if node.decorators is None:
        return []

    names = []

    for decorator_node in node.decorators.nodes:
        if type(decorator_node) is astroid.node_classes.Call:
            names.append(decorator_node.func.name)
        elif type(decorator_node) is astroid.node_classes.Name:
            names.append(decorator_node.name)
        else:
            pass # don't care about other types

    return names

def parameter_keys(node):
    if node.decorators is None:
        return []

    keys = []

    for decorator_node in node.decorators.nodes:
        if 'func' in dir(decorator_node) and decorator_node.func.name == 'parameter':
            for keyword in decorator_node.keywords:
                if keyword.arg == 'key':
                    keys.append(keyword.value.value)

    return keys

def has_duplicate_param_keys(keys):
    counter = Counter(keys)

    for count in counter.values():
        if count > 1:
            return True

    return False

def command_before_parameters(names):
    found_parameter = False

    for name in names:
        if name == 'parameter':
            found_parameter = True
        elif name == 'command' and found_parameter == True:
            return False

    return True

class BeergardenCommandChecker(BaseChecker):
    __implements__ = IAstroidChecker

    name = 'beergarden-command-checker'
    priority = -1
    msgs = {
        'E5501': (
            'Parameter decorator key does not match function parameter name',
            'decorator-key-parameter-name-mismatch',
            'Parameter decorator keys must match function parameter names.'
        ),
        'E5502': (
            'Parameter decorator without command decorator',
            'parameter-without-command-decorator',
            'Parameter decorator must be preceeded by a command decorator.'
        ),
        'E5503': (
            'Command decorator after parameter decorator',
            'parameter-before-command-decorator',
            'Command decorator must come before parameter decorator'
        ),
        'E5504': (
            'Duplicate key in parameter decorator',
            'duplicate-parameter-keys',
            'Key must be unique in a function parameter decorator.'
        ),
    }

    def __init__(self, linter=None):
        super(BeergardenCommandChecker, self).__init__(linter)

    def visit_functiondef(self, node):
        deco_names = decorator_names(node)

        if 'command' not in deco_names and 'parameter' not in deco_names:
            return # not applicable

        if 'parameter' in deco_names and 'command' not in deco_names:
            self.add_message('parameter-without-command-decorator', node=node)
            return

        if not command_before_parameters(deco_names):
            self.add_message('parameter-before-command-decorator', node=node)
            return

        param_keys = parameter_keys(node)

        if has_duplicate_param_keys(param_keys):
            self.add_message('duplicate-parameter-keys', node=node)
            return

        function_params = set([ arg.name for arg in node.args.args ])

        if 'self' in function_params:
            function_params.remove('self')

        if function_params != set(param_keys):
            self.add_message('decorator-key-parameter-name-mismatch', node=node)

'''
This is the top-level module for sschema.
'''

import types

import jsonschema


class SSchemaError(Exception):
    def __init__(self, msg):
        super().__init__(msg)


def make_format_checker(modules):
    '''Makes a format checker for use in jsonschema validation. Takes a list of
    modules, each of which must have a top-level "check" (which checks a
    format) and a constant "FORMAT_NAME" (the name of the format to check).
    From this list of modules, we create and return a format checker object.'''
    format_checker = jsonschema.FormatChecker()
    for module in modules:
        func = module.check
        name = module.FORMAT_NAME
        # Manually decorate the format checker with our format.
        format_checker.checks(name)(func)
    return format_checker


def make_resolver(schema, items):
    '''Makes a resolver for use in jsonschema validation. Takes a schema (a
    required argument of RefResolver.__init__ and either:

    - a list of modules, each of which has a top-level "handler" (a handler
      function) and a constant "HANDLER_NAME" (the name of the handler prefix).
    - a list of tuples of the form (function, name), where function is a
      handler function and name is a handler prefix.

    From this we create and return a RefResolver object.'''
    handlers = {}
    for item in items:
        if isinstance(item, types.ModuleType):
            func = item.handler
            name = item.HANDLER_NAME
        elif isinstance(item, tuple) or isinstance(item, list):
            if len(item) != 2:
                raise SSchemaError(
                    "handler tuple/list %s doesn't have length 2" % item)
            func, name = item
        else:
            raise SSchemaError(
                'item %s is not a module or a handler tuple/list' % item)
        handlers[name] = func
    resolver = jsonschema.RefResolver.from_schema(schema, handlers=handlers)
    return resolver

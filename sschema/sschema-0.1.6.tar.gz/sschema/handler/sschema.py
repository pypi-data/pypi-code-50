'''
A resolver that searches a list of include paths for YAML files matching the
given name. The include paths must be set prior to validation.
'''

import functools
import pkg_resources
import os

import yaml


DEFAULT_HANDLER_NAME = 'sschema'


def _handler(name, include_paths, uri):
    '''Handles an URI of form {name}://'''
    scheme = '{}://'.format(name)
    assert(uri.startswith(scheme))
    uri = uri[len(scheme):]

    for base in include_paths:
        path = os.path.join(base, uri)
        try:
            f = open(path, 'r')
        except FileNotFoundError:
            continue
        else:
            with f:
                return yaml.safe_load(f)
    raise FileNotFoundError('{} handler could not find path "{}" in any of {}'.format(name, uri, include_paths))


def _make_handler(include_paths, name):
    '''Returns an include handler and name (for use with make_resolver) that
    uses the give include paths.'''
    return (functools.partial(_handler, name, include_paths), name)


def make_default_handler():
    '''Returns a default handler, which uses the common schemas defined in
    sschema as the include path.'''
    schema_path = pkg_resources.resource_filename('sschema', 'schema')
    return _make_handler([schema_path], DEFAULT_HANDLER_NAME)


def make_handler(include_paths, name):
    '''Returns an include handler and name (for use with make_resolver) that
    uses the given include paths.'''
    if name == DEFAULT_HANDLER_NAME:
        raise ValueError('Handler name "{}" is reserved for internal use'.format(name))
    return _make_handler(include_paths, name)

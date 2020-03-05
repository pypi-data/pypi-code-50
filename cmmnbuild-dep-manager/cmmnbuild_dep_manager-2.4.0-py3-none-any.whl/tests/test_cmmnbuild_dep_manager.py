from contextlib import contextmanager
import logging
import pathlib
import types
import unittest.mock
import sys

import pytest

import cmmnbuild_dep_manager as cbdm
from cmmnbuild_dep_manager.resolver import Resolver


class SimpleResolver(Resolver):
    dependency_variable = '__test_resolver_deps__'
    description = 'The test resolver which does nothing'

    @classmethod
    def is_available(cls):
        return True

    def __init__(self, dependencies):
        pass

    def save_jars(self, dir):
        pass

    @classmethod
    def get_help(cls, classnames, class_info):
        raise ValueError('No help available from this testable resolver')


@pytest.fixture
def simple_resolver():
    with unittest.mock.patch(
            'cmmnbuild_dep_manager.resolver.resolvers',
            return_value=[SimpleResolver]):
        yield


@contextmanager
def tmp_mod(name, dependencies=None, version=None):
    """
    Generate a temporary module that is suitable for testing dependency
    resolution with.

    """
    mod = types.ModuleType('a_cmmnbuild_test_module')
    if dependencies is not None:
        mod.__test_resolver_deps__ = dependencies
    if version is not None:
        mod.__version__ = version
    sys.modules[name] = mod

    try:
        yield mod
    finally:
        sys.modules.pop(name)


def test_no_such_module(caplog, simple_resolver):
    cbdm.Manager('this_mod_doesnt_exist')
    assert caplog.record_tuples == [
        ("cmmnbuild_dep_manager", logging.INFO,
         'Package "this_mod_doesnt_exist" is not yet set up - '
         'installing and resolving JARs'),
        ("cmmnbuild_dep_manager", logging.ERROR,
         'this_mod_doesnt_exist not found'),
    ]


def test_module_missing_special_resolver_attr(caplog, simple_resolver):
    with tmp_mod('a_cmmnbuild_test_module'):
        cbdm.Manager('a_cmmnbuild_test_module')

    warning = (
        "cmmnbuild_dep_manager", logging.ERROR,
        'module a_cmmnbuild_test_module does not declare '
        '__test_resolver_deps__, which is needed for SimpleResolver '
        '(The test resolver which does nothing) ')
    assert warning in caplog.record_tuples


def test_module_dependencies_no_version(caplog, simple_resolver):
    with tmp_mod('a_cmmnbuild_test_module', dependencies=['j1', 'j2']):
        cbdm.Manager('a_cmmnbuild_test_module')
    warning = (
        "cmmnbuild_dep_manager", logging.ERROR,
        "module 'a_cmmnbuild_test_module' has no attribute '__version__'")
    assert warning in caplog.record_tuples


@contextmanager
def no_pre_installed_modules():
    """
    Moves the modules.json file that may exist to a temporary location for
    the duration of testing.

    """
    mods = pathlib.Path(cbdm.__file__).parent / 'modules.json'
    tmp_mods = pathlib.Path(str(mods) + '.tmp')
    must_move = mods.exists()
    if must_move:
        mods.replace(tmp_mods)
    try:
        yield
    finally:
        if must_move:
            tmp_mods.replace(mods)


@pytest.fixture
def mocked_mgr():
    """
    A fixture that provides a clean manager and resolver for mocked testing of
    module installation.

    """
    mock_resolver = unittest.mock.Mock(
        __name__='mock_resolver',
        dependency_variable='__test_resolver_deps__',
        description="the mock resolver",
    )

    mock_resolvers = unittest.mock.patch(
        'cmmnbuild_dep_manager.resolver.resolvers',
        return_value=[mock_resolver])

    resolver = mock_resolver
    with mock_resolvers, no_pre_installed_modules():
        manager = cbdm.Manager()
        yield manager, resolver


def test_module_dependencies(mocked_mgr):
    mgr, m_resolver = mocked_mgr

    mod1 = tmp_mod(
        'mod1', version='1.2.3', dependencies=['java_dep1', 'java_dep2'])

    with mod1:
        mgr.install('mod1')

    m_resolver.assert_called_once_with(
        ['java_dep1', 'java_dep2'])


def test_multi_module_dependencies(mocked_mgr):
    mgr, m_resolver = mocked_mgr

    mod1 = tmp_mod(
        'mod1', version='1.2.3', dependencies=['java_dep1', 'java_dep2'])
    mod2 = tmp_mod(
        'mod2', version='1.2.3', dependencies=['java_dep2', 'java_dep3'])

    with mod1, mod2:
        mgr.install('mod1')
        m_resolver.reset_mock()
        mgr.install('mod2')

    m_resolver.assert_called_once_with(
        ['java_dep1', 'java_dep2', 'java_dep2', 'java_dep3'])

from contextlib import contextmanager
import json
import logging
import sys
import types
import typing
import unittest.mock

import entrypoints

from cmmnbuild_dep_manager.cmmnbuild_dep_manager import Manager, PKG_MODULES_JSON


@contextmanager
def fake_entrypoints(target_entrypoints: typing.Dict[str, typing.List[str]]):
    def new_get_group_all(group_name):
        if group_name not in target_entrypoints:
            raise RuntimeError(
                'Unexpected arguments to entrypoints.get_group_all')
        return target_entrypoints[group_name]

    new_entrypoints = unittest.mock.Mock(side_effect=new_get_group_all)
    with unittest.mock.patch('entrypoints.get_group_all', new_entrypoints):
        yield


@contextmanager
def tmp_modules_content(modules_content):
    existing = None
    if PKG_MODULES_JSON.exists():
        with PKG_MODULES_JSON.open('rt') as fh:
            existing = fh.read()
    with PKG_MODULES_JSON.open('wt') as fh:
        json.dump(modules_content, fh)
    try:
        yield
    finally:
        if existing is not None:
            with PKG_MODULES_JSON.open('wt') as fh:
                fh.write(existing)


class FakePkgMgr:
    def __init__(self):
        #: A mapping of package names to fake module instance.
        self.pkgs = {}

        #: A mapping from package name to the registered entrypoint.
        self.entry_points: typing.Dict[str, entrypoints.EntryPoint] = {}

    @classmethod
    @contextmanager
    def fake_pkg(cls, name, version, entrypoint):
        self = cls()
        self.add_module(name, version, entrypoint)
        with self:
            yield

    def add_module(self, name, version, entrypoint: str = None):
        mod = self.pkgs[name] = types.ModuleType(name)
        mod.__version__ = version
        if entrypoint:
            self.entry_points[name] = entrypoints.EntryPoint.from_string(
                entrypoint, name)

    def __enter__(self):
        for pkg, mod in self.pkgs.items():
            # Note this will replace any that already exist, so some caution
            # needed.
            sys.modules[pkg] = mod

        self.ep_ctx = fake_entrypoints(
            {'cmmnbuild_dep_manager': list(self.entry_points.values())})
        self.ep_ctx.__enter__()

    def __exit__(self, type, value, traceback):
        for pkg in self.pkgs:
            sys.modules.pop(pkg)
        self.ep_ctx.__exit__(type, value, traceback)


def test_pkg_needs_install(caplog):
    with FakePkgMgr.fake_pkg("fake_cmmnbuild_pkg", "1.2.3", entrypoint="1.2.3"):
        mgr = Manager()
        r = mgr._load_modules()

    assert r == {'fake_cmmnbuild_pkg': ""}
    assert caplog.record_tuples == []


def test_pkg_needs_install_bad_entrypoint(caplog):
    # Note that the version of the module and the version in the entry-point
    # differ.
    with FakePkgMgr.fake_pkg("fake_cmmnbuild_pkg", "1.2.3", entrypoint="1.2.4"):
        mgr = Manager()
        r = mgr._load_modules()

    assert r == {'fake_cmmnbuild_pkg': ""}
    assert caplog.record_tuples == []


def test_pkg_already_installed(caplog):
    with FakePkgMgr.fake_pkg("fake_cmmnbuild_pkg", "1.2.3", entrypoint="1.2.3"):
        with tmp_modules_content({'fake_cmmnbuild_pkg': '1.2.3'}):
            mgr = Manager()
            r = mgr._load_modules()

    assert r == {'fake_cmmnbuild_pkg': "1.2.3"}
    assert caplog.record_tuples == []


def test_pkg_needs_update(caplog):
    # Note that the version of the module and the version in the entry-point
    # differ.
    with FakePkgMgr.fake_pkg("fake_cmmnbuild_pkg", "1.2.3", entrypoint="1.2.3"):
        with tmp_modules_content({'fake_cmmnbuild_pkg': '1.2.2'}):
            mgr = Manager()
            r = mgr._load_modules()

    assert r == {'fake_cmmnbuild_pkg': ""}
    assert caplog.record_tuples == [
        ('cmmnbuild_dep_manager', logging.WARN,
         'fake_cmmnbuild_pkg is being updated from 1.2.2 to 1.2.3')]


def test_pkg_no_update_bad_entrypoint(caplog):
    # Note that the version of the module and the version in the entry-point
    # differ.
    with FakePkgMgr.fake_pkg("fake_cmmnbuild_pkg", "1.2.3", entrypoint="1.2.4"):
        with tmp_modules_content({'fake_cmmnbuild_pkg': '1.2.3'}):
            mgr = Manager()
            r = mgr._load_modules()

    assert r == {'fake_cmmnbuild_pkg': ""}
    assert caplog.record_tuples == [
        ('cmmnbuild_dep_manager', logging.WARN,
         'fake_cmmnbuild_pkg is being updated from 1.2.3 to 1.2.4')]

"""
This code wraps the vendored appdirs module to so the return values are
compatible for the current pip code base.

The intention is to rewrite current usages gradually, keeping the tests pass,
and eventually drop this after all usages are changed.
"""

from __future__ import absolute_import

import os

from pip._vendor import appdirs as _appdirs

from pip._internal.utils.typing import MYPY_CHECK_RUNNING

if MYPY_CHECK_RUNNING:
    from typing import List


def user_cache_dir(appname):
    # type: (str) -> str
    return _appdirs.user_cache_dir(appname, appauthor=False)


def user_config_dir(appname, roaming=True):
    # type: (str, bool) -> str
    return _appdirs.user_config_dir(appname, appauthor=False, roaming=roaming)


def user_data_dir(appname, roaming=False):
    # type: (str, bool) -> str
    return _appdirs.user_data_dir(appname, appauthor=False, roaming=roaming)


def site_config_dirs(appname):
    # type: (str) -> List[str]
    dirval = _appdirs.site_config_dir(appname, appauthor=False, multipath=True)
    if _appdirs.system not in ["win32", "darwin"]:
        return dirval.split(os.pathsep)
    return [dirval]

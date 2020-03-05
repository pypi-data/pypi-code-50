import shutil

import pytest

from cmmnbuild_dep_manager.cmmnbuild_dep_manager import PKG_MODULES_JSON


TMP_PKG_MODULES_JSON = (
        PKG_MODULES_JSON.parent / ("_test_" + PKG_MODULES_JSON.name))
LIB_DIR = PKG_MODULES_JSON.parent / 'lib'
TMP_LIB_DIR = PKG_MODULES_JSON.parent / '_test_lib'


@pytest.fixture(autouse=True, scope="session")
def autoclean_modules_json():
    # NOTE: Runs one-startup and one teardown (scope=session).
    # Each test should still make sure that it tidies up properly for the
    # sake of test consistency - this fixture simply ensures that the pre-test
    # state is preserved after testing.

    if LIB_DIR.exists():
        if TMP_LIB_DIR.exists():
            raise RuntimeError(
                f'Testing already in progress - {TMP_LIB_DIR} exists already')
        LIB_DIR.rename(TMP_LIB_DIR)

    if PKG_MODULES_JSON.exists():
        if TMP_PKG_MODULES_JSON.exists():
            raise RuntimeError(
                f'Testing already in progress - {TMP_PKG_MODULES_JSON} exists already')
        PKG_MODULES_JSON.rename(TMP_PKG_MODULES_JSON)

    try:
        yield
    finally:
        shutil.rmtree(LIB_DIR)
        PKG_MODULES_JSON.unlink()
        if TMP_PKG_MODULES_JSON.exists():
            TMP_PKG_MODULES_JSON.rename(PKG_MODULES_JSON)
        if TMP_LIB_DIR.exists():
            TMP_LIB_DIR.rename(LIB_DIR)

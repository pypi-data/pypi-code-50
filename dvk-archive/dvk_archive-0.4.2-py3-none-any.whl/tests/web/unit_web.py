from dvk_archive.tests.web.test_basic_connect import run_all as b_connect
from dvk_archive.tests.web.test_heavy_connect import run_all as h_connect


def test_web():
    """
    Runs web tests.
    """
    h_connect()
    b_connect()

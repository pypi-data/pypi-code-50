from dvk_archive.tests.file.test_dvk_handler import TestDvkHandler
from dvk_archive.tests.file.test_dvk_directory import TestDvkDirectory
from dvk_archive.tests.file.test_dvk import run_all as test_dvk


def test_file():
    """
    Runs all file tests.
    """
    test_dvk()
    test_dvk_directory = TestDvkDirectory()
    test_dvk_directory.run_all()
    test_dvk_handler = TestDvkHandler()
    test_dvk_handler.run_all()

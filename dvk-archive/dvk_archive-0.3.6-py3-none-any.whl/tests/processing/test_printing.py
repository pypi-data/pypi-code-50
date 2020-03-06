from pathlib import Path
from dvk_archive.processing.printing import truncate_path


def test_truncate_path():
    """
    Tests the truncate_path function
    """
    assert truncate_path() == ""
    base_path = Path()
    sub = base_path.joinpath("sub")
    other = base_path.joinpath("kjskjld")
    assert truncate_path(sub) == str(sub.absolute())
    assert truncate_path(sub, other) == str(sub.absolute())
    assert truncate_path(sub, base_path) == ".../sub"


def run_all():
    """
    Tests all functions of the printing.py module
    """
    test_truncate_path()

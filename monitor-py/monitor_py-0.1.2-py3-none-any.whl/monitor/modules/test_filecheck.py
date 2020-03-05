from monitor.modules import filecheck as fc
import pytest

def test_root():
    with pytest.raises(OSError):
        fc.check_files()
import pytest
import atmopy

def test_version():
    """ Tests atmopy current version """
    expected_version = "0.1.0"
    current_version = atmopy.__version__
    assert current_version == expected_version

"""
To test utility functions module.
"""
from . import utils


def test_greet():
    assert utils.greet() == 'Hello World!'

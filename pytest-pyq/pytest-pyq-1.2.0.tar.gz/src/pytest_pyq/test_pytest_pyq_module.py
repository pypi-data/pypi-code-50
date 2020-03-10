import pytest


@pytest.fixture(scope='module')
def module(q_module):
    q_module.a = 42

    return q_module


def test_module1(module):
    assert module.a == 42
    module.b = 100


def test_module2(module):
    assert module.a == 42
    assert module.b == 100
    del module.b

def test_module3(module):
    assert module.a == 42
    with pytest.raises(AttributeError):
        module.b

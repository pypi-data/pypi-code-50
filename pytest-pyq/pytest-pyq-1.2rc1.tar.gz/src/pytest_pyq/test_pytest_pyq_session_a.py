import pytest


@pytest.fixture(scope='session')
def session(q_session):
    q_session.a = 42

    return q_session


def test_session_a1(session):
    assert session.a == 42
    session.b = 100


def test_session_a2(session):
    assert session.a == 42
    assert session.b == 100
    del session.b

def test_session_a3(session):
    assert session.a == 42
    with pytest.raises(AttributeError):
        session.b

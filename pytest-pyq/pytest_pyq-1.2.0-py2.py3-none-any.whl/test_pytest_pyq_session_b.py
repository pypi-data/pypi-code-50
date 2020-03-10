import pytest


def test_session_b(q_session):
    assert q_session.a == 42
    with pytest.raises(AttributeError):
        q_session.b

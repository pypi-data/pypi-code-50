import contextlib

import flask_restx


@contextlib.contextmanager
def open_file(filename, mode='r'):
    with open(filename, mode) as stream:
        yield stream


def test_open_file(fs):
    f = 'foo.txt'
    fs.create_file(f, contents='foo')

    with open_file(f) as stream:
        assert 'foo' == stream.read()

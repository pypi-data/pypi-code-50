import io
from contextlib import contextmanager

from autofile import auto_detect


@contextmanager
def open(file, buffering=-1, errors=None, newline=None, closefd=True, opener=None):
    encoding = auto_detect.file_encoding(file)
    with io.open(file, mode='rt', buffering=buffering, encoding=encoding, errors=errors,
                 newline=newline, closefd=closefd, opener=opener) as file_object:
        yield file_object

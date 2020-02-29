import csv
from pathlib import Path
from contextlib import contextmanager


class ReaderProxy:

    def __init__(self, reader, dialect=None, has_header=False):
        self.reader = reader
        self.has_header = has_header
        self.dialect = dialect

    def iter(self):
        for index, row in enumerate(self.reader):
            yield index, row


@contextmanager
def reader(filepath, *args, **kwargs):
    with Path(filepath).open(mode='r') as _file:
        delimiters = kwargs.get("delimiters")
        sample = _file.read(1024)
        _file.seek(0)
        snf = csv.Sniffer()
        dialect = snf.sniff(sample, delimiters=delimiters)
        has_header = snf.has_header(sample)
        reader = csv.reader(_file, dialect)
        yield ReaderProxy(reader, dialect=dialect, has_header=has_header)


@contextmanager
def writer(filepath, mode='w', **kwargs):
    with Path(filepath).open(mode=mode) as _file:
        writer = csv.writer(_file, **kwargs)
        yield writer

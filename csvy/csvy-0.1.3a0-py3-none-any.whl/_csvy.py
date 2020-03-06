import csv
from collections import namedtuple
from pathlib import Path
from contextlib import contextmanager

def normalize_name(name, index):
    name_chars = [c for c in name.lower() if c in ' _-abcdefghijklmnopqrstuvwxyz0123456789']

    _name = ''.join(name_chars)
    _name = _name.strip()

    if not _name:
        return f"column_{index}"

    _name = _name.replace(" ", "_")
    _name = _name.replace("-", "_")

    if _name[0] not in 'abcdefghijklmnopqrstuvwxyz':
        _name = f"col{_name}"

    return _name


def filter_duplicates(headers):
    src = set()
    return_headers = []
    for index, header in enumerate(headers):
        if header in src:
            new_header_name = f"{header}_{index}"
            return_headers.append(new_header_name)
            src.add(new_header_name)
        else:
            return_headers.append(header)
    return return_headers


def build_named_tuple(headers):
    new_headers = filter_duplicates([normalize_name(h, i) for i, h in enumerate(headers)])
    return namedtuple('CsvRow', new_headers)


def pass_thru(*args):
    return args

class ReaderProxy:

    def __init__(self, reader, dialect=None, has_header=False):
        self.reader = reader
        self.has_header = has_header
        self.dialect = dialect

    def iter(self, skip_header=True, namedtuple=True):
        CsvRow = pass_thru
        for index, row in enumerate(self.reader):
            if index == 0 and self.has_header and namedtuple:
                CsvRow = build_named_tuple(row)
            if index == 0 and self.has_header and skip_header:
                continue
            yield index, CsvRow(*row)


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
    with Path(filepath).open(mode=mode, newline='') as _file:
        writer = csv.writer(_file, **kwargs)
        yield writer

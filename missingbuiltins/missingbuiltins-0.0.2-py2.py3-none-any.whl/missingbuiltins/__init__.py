__author__ = """John Bjorn Nelson"""
__email__ = 'jbn@abreka.com'
__version__ = '0.0.2'

import json
from pathlib import Path
from typing import Union, Any, Iterable, Tuple


def jsonl_load(path: Union[str, Path], object_hook=dict):
    """
    Yield the JSON document loaded from each line in the given file.

    :param path: the path to the json-lines file
    :param object_hook: argument to json.loads that determines how objects
        get created (i.e., you may want to use OrderedDict)
    """
    with Path(path).open() as fp:
        for line in fp:
            yield json.loads(line, object_hook=dict)


def jsonl_dump(path: Union[str, Path], items):
    """
    Save a given iterable of items to a json-lines file.

    :param path: the path to the json-lines file
    :param items: an iterator of JSON-serializable documents to write
    :return: the total number of objects read
    """
    n = 0

    with Path(path).open("w") as fp:
        for item in items:
            fp.write(json.dumps(item) + "\n")
            n += 1

    return n


def chunker(items: Iterable[Any], k: int) -> Iterable[Tuple[Any, ...]]:
    """
    Yields a sequence of k-tuple (or less) sized chunks from given items.

    :param items: an iterable of objects to group
    :param k: the maximum size of the group
    """
    chunk = []

    for item in items:
        chunk.append(item)

        if len(chunk) == k:
            yield tuple(chunk)
            chunk = []

    if chunk:
        yield tuple(chunk)

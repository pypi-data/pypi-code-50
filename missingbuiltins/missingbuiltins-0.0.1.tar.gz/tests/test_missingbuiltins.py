#!/usr/bin/env python

import pytest
from collections import OrderedDict
from missingbuiltins import chunker, jsonl_dump, jsonl_load
from random import randint


def test_chunker():
    items = [1, 2, 3, 4, 5, 6]

    assert list(chunker([], 3)) == []
    assert list(chunker(items, 3)) == [(1, 2, 3), (4, 5, 6)]
    assert list(chunker(items, 4)) == [(1, 2, 3, 4), (5, 6)]


def test_jsonl_utils(tmpdir):
    items = []

    for i in range(100):
        k = randint(0, 100)
        items.append(OrderedDict([("i", i), (str(k), k)]))

    def add_field(d):
        d = d.copy()
        d['x'] = 100
        return d

    output_path = tmpdir / "items.jsonl"
    jsonl_dump(str(output_path), items, extractor=add_field)

    got = list(jsonl_load(str(output_path), OrderedDict))
    assert all('x' in item for item in got)

    for item in got:
        del item['x']
    assert items[0] == got[0]

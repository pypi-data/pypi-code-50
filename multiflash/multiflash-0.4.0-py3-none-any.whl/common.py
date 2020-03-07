# Copyright 2020 John Reese
# Licensed under the MIT License

import re
from typing import List, Union

FIND_NUMBERS_RE = re.compile(r"\d+")
NATURAL_SPLIT_RE = re.compile(r"(\d+)")


def find_numbers(value: str) -> List[int]:
    values = [m.group() for m in FIND_NUMBERS_RE.finditer(value)]
    return [int(v) for v in values if v]


def natural_sort(key: str) -> List[Union[int, str]]:
    parts = [p.strip() for p in NATURAL_SPLIT_RE.split(key) if p]
    return [int(part) if part.isdigit() else part for part in parts]

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from datetime import datetime
from pathlib import Path
from typing import Callable, Dict, List, Optional


def diff_lines(
        lines_1: List[str],
        lines_2: List[str],
        filter_func: Callable[[str], bool] = None
) -> List[str]:
    len_1 = len(lines_1)
    len_2 = len(lines_2)
    len_min = min(len_1, len_2)
    diff = []
    for i in range(len_min):
        a = lines_1[i]
        b = lines_2[i]
        if filter_func and \
                filter_func(a) and \
                filter_func(b):
            continue
        if a != b:
            diff.append(f"{a.strip()} → {b.strip()}")
    if len_1 > len_min:
        for i in range(len_min, len_1):
            diff.append(lines_1[i])
    if len_2 > len_min:
        for i in range(len_min, len_2):
            diff.append(lines_2[i])
    return diff


def diff_text(
        text_1: str,
        text_2: str,
        filter_func: Callable[[str], bool] = None
) -> List[str]:
    lines_1 = text_1.splitlines(keepends=True)
    lines_2 = text_2.splitlines(keepends=True)
    return diff_lines(lines_1, lines_2, filter_func)


def interpolate_text(
        text: str,
        expressions: Dict[str, str]
) -> str:
    for k, v in expressions.items():
        text = text.replace(k, v)
    return text


def timestamp() -> str:
    return datetime.utcnow().isoformat()


def write_text_file(
        text: str,
        path: Path,
        diff_show_len: int = 5,
        diff_func: Callable[[str, str, Optional[Callable[[str], bool]]], List[str]] = None,
        filter_func: Callable[[str], bool] = None,
        log_func: Callable[[str], None] = None
) -> None:
    if not path.parent.exists():
        path.parent.mkdir(parents=True, exist_ok=True)
    if diff_func and path.exists():
        orig_text = path.read_text()
        diff = diff_func(orig_text, text, filter_func)
        diff_len = len(diff)
        if diff_len == 0:
            if log_func:
                log_func(f"No relevant changes found, skipping {path.name}.")
            return
        if log_func:
            log_func(f"Found {diff_len} change(s) to {path.name}.")
            for i in range(min(diff_len, diff_show_len)):
                log_func(f".. {diff[i]}")
    path.write_text(text)

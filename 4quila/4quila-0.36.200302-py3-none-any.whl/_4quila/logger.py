#!/usr/bin/python3
# -*- coding: utf-8 -*-
import inspect
from .common import format_frame, format_stacks, logger

def error(content, expands=None):
    info(content, expands=expands, depth=2)
    raise Exception("_4")


def info(content, expands=None, depth=1):
    expand_lines = []
    if expands:
        for expand_index, expand in enumerate(expands):
            try:
                expand_lines.append("[%s] = %s" % (expand_index, expand))
                for expand_field in dir(expand):
                    if expand_field.startswith("__") and expand_field.endswith("__"):
                        continue
                    expand_lines.append(
                        "[%s].%s->%s"
                        % (expand_index, expand_field, getattr(expand, expand_field))
                    )
            except Exception:
                continue

    logger.info(
        "\n".join(
            ["", ">>> %s >>>>" % content,]
            + list(format_stacks())
            + list(format_frame(inspect.stack()[depth].frame))
            + expand_lines
            + ["<<< %s <<<<" % content,]
        )
    )

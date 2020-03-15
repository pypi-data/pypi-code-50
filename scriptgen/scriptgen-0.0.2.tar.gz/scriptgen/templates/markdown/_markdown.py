#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from scriptgen import BlockBuilder, StringBuilder, timestamp


def markdown_autogen() -> StringBuilder:
    return markdown_comment(f"Auto-generated: {timestamp()}", padded=False)


def markdown_code_block(language: str = None) -> StringBuilder:
    language = language if language else ""
    bb = BlockBuilder(
        indent_len=0,
        header=f"```{language}{StringBuilder.new_line}",
        footer=f"```{StringBuilder.new_line}"
    )
    return bb


def markdown_comment(
        *args: str,
        padded: bool = True) -> StringBuilder:
    sb = StringBuilder()
    if args:
        if padded:
            sb.nl()
        for arg in args:
            sb.wl(f"[//]: # ({arg})")
        if padded:
            sb.nl()
    return sb


def markdown_inline(
        value: str,
        decorator: str = None) -> str:
    decorator = decorator if decorator else ""
    return f"{decorator}{value}{decorator[::-1]}"

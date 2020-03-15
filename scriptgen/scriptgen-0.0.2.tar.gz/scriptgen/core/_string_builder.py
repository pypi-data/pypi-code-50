#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from __future__ import annotations
from enum import Enum, auto
from os import linesep
from typing import List, Union


class IndentType(Enum):
    SPACES = auto()
    TABS = auto()


class StringBuilder:

    indent_tab: str = "\t"
    new_line: str = linesep

    default_indent_len: int = 0
    default_indent_space_len: int = 4
    default_indent_type: IndentType = IndentType.SPACES
    default_rstrip: bool = False

    def __init__(
            self,
            indent_len: int = None,
            indent_space_len: int = None,
            indent_type: IndentType = None,
            rstrip: bool = None
    ) -> None:
        indent_len = indent_len if indent_len is not None else StringBuilder.default_indent_len
        indent_space_len = indent_space_len if indent_space_len is not None else StringBuilder.default_indent_space_len
        indent_type = indent_type if indent_type is not None else StringBuilder.default_indent_type
        rstrip = rstrip if rstrip is not None else StringBuilder.default_rstrip
        self.indent_len = indent_len
        self.indent_space_len: int = indent_space_len
        self.indent_type: IndentType = indent_type
        self.rstrip: bool = rstrip
        self.strings: List[Union[str, StringBuilder]] = []

    def __str__(self) -> str:
        return self.build()

    @property
    def indent(self) -> str:
        return self._indent

    @property
    def indent_space(self) -> str:
        return self._indent_space

    @property
    def indent_space_len(self) -> int:
        return self._indent_space_len

    @indent_space_len.setter
    def indent_space_len(
            self,
            value: int
    ) -> None:
        self._indent_space_len = value
        self._indent_space = " " * value

    @property
    def indent_type(self) -> IndentType:
        return self._indent_type

    @indent_type.setter
    def indent_type(
            self,
            value: IndentType
    ) -> None:
        self._indent_type = value
        if IndentType.SPACES == value:
            self._indent = self.indent_space
        elif IndentType.TABS == value:
            self._indent = self.indent_tab

    def build(
            self,
            rstrip: bool = None
    ) -> str:
        if self.strings:
            rstrip = self.rstrip if rstrip is None else rstrip
            indent = self.indent * self.indent_len
            strings = [str(string) for string in self.strings]
            lines = "".join(strings)
            text = "".join([f"{indent}{line}" for line in lines.splitlines(keepends=True)])
            if rstrip:
                text = text.rstrip()
            return text
        return ""

    def clear(self) -> None:
        self.strings.clear()

    def nl(self) -> None:
        self.strings.append(self.new_line)

    def wb(
            self,
            string_builder: StringBuilder,
            rstrip: bool = None
    ) -> None:
        rstrip = self.rstrip if rstrip is None else rstrip
        string_builder.rstrip = rstrip
        self.strings.append(string_builder)

    def wt(
            self,
            text: str,
            addtl_indent_len: int = 0
    ) -> None:
        self.strings.append(f"{self.indent * addtl_indent_len}{text}")

    def wts(
            self,
            texts: List[str],
            addtl_indent_len: int = 0
    ) -> None:
        for text in texts:
            self.wt(text, addtl_indent_len)

    def wl(
            self,
            line: str,
            addtl_indent_len: int = 0
    ) -> None:
        self.strings.append(f"{self.indent * addtl_indent_len}{line}{self.new_line}")

    def wls(
            self,
            lines: List[str],
            addtl_indent_len: int = 0
    ) -> None:
        for line in lines:
            self.wl(line, addtl_indent_len)


class BlockBuilder(StringBuilder):

    default_indent_len: int = 1

    def __init__(
            self,
            header: str = "",
            footer: str = "",
            indent_len: int = None,
            indent_space_len: int = None,
            indent_type: IndentType = None,
            rstrip: bool = None
    ) -> None:
        indent_len = indent_len if indent_len is not None else BlockBuilder.default_indent_len
        StringBuilder.__init__(
            self,
            indent_len=indent_len,
            indent_space_len=indent_space_len,
            indent_type=indent_type,
            rstrip=rstrip
        )
        self.header: str = header
        self.footer: str = footer

    def build(
            self,
            rstrip: bool = None
    ) -> str:
        rstrip = self.rstrip if rstrip is None else rstrip
        contents = StringBuilder.build(self, rstrip)
        return "".join([self.header, contents, self.footer])

# -*- coding: utf-8 -*-
"""
pyFuckery - test_parser.py
Created on 2/19/17.

Tests for the AST parser
"""
# Stdlib
import logging
import os

import lark

# Custom code
from fuckery import parser

import tests.common as t_common

# Logging config
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s [%(levelname)s] %(message)s [%(filename)s:%(funcName)s]')
log = logging.getLogger(__name__)


class TestParser:  # XXX CamelCase

    def test_simple_tree(self):
        bf = '[->+<]'
        t = parser.parse_program(s=bf)
        assert isinstance(t, lark.Tree)
        r = t.pretty()
        assert isinstance(r, str)
        assert 'program' in r
        assert 'loop' in r
        assert 'expression' in r

    def test_commented_add_program(self):
        test_bf = '[->+<]'
        fn = 'add.bf'
        buf = t_common.get_fn_contents(fn=fn)
        bf = buf.decode()
        t = parser.parse_program(s=bf)
        ts = t.pretty()
        e = parser.parse_program(s=test_bf)
        es = e.pretty()
        assert ts == es

    def test_hello_world_parse(self):
        fn = 'hello_world.bf'
        buf = t_common.get_fn_contents(fn=fn)
        bf = buf.decode()
        t = parser.parse_program(s=bf)
        assert isinstance(t, lark.Tree)
        r = t.pretty()
        assert isinstance(r, str)
        assert 'program' in r
        assert 'loop' in r
        assert 'expression' in r

#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
pyFuckery - constants.py
Created on 2/12/17.

Constants used by fuckery.
"""
#: Brainfuck tokens
#: Brainfuck PTR INC token
SYM_PTR_INC = '>'
#: Brainfuck PTR DEC token
SYM_PTR_DEC = '<'
#: Brainfuck DATA INC token
SYM_DATA_INC = '+'
#: Brainfuck DATA INC token
SYM_DATA_DEC = '-'
#: Brainfuck IO output token
SYM_IO_OUTPUT = '.'
#: Braifuck IO input token
SYM_IO_INPUT = ','
#: Brainfuck jump forward token
SYM_JMP_FWD = '['
#: Brainfuck jump backward token
SYM_JMP_BACKWARD = ']'

SYM_PROGRAM = 'program'
SYM_LOOP = 'loop'
SYM_ACTIONS = 'actions'
SYM_EXPRESSIONS = 'expression'

# Default VM configuration
#: Default memotry sizen
DEFAULT_MEMORY_SIZE = 30000
MEMORY_MIN_VALUE = 0
MEMORY_MAX_VALUE = 255

# EBNF Grammer for Brainfuck

IGNORE_REGEX = f'\\{SYM_PTR_DEC}\\{SYM_PTR_INC}\\{SYM_DATA_DEC}\\{SYM_DATA_INC}' \
    f'\\{SYM_IO_INPUT}\\{SYM_IO_OUTPUT}\\{SYM_JMP_FWD}\\{SYM_JMP_BACKWARD}'

# Credit where credit is due - largely influenced by from
# https://webcache.googleusercontent.com/search?q=cache:cdkXLzIKMA0J:https://groups.google.com/a/cdglabs.org/d/topic
# /ohm/Jvwx1jvPOqY+&cd=8&hl=en&ct=clnk&gl=us
# which was inspired by https://www.researchgate.net/publication/255592935_Implementing_Brainfuck_in_COLA_Version_2
GRAMMAR = f'''

{SYM_PROGRAM}: {SYM_EXPRESSIONS}*

{SYM_LOOP}: JMP_FWD {SYM_EXPRESSIONS}* JMP_BCK

{SYM_ACTIONS}: PTR_DEC | PTR_INC | DATA_DEC | DATA_INC | IO_INPUT | IO_OUTPUT

{SYM_EXPRESSIONS}: {SYM_ACTIONS} | {SYM_LOOP}

PTR_DEC: "{SYM_PTR_DEC}"
PTR_INC: "{SYM_PTR_INC}"
DATA_DEC: "{SYM_DATA_DEC}"
DATA_INC: "{SYM_DATA_INC}"
IO_INPUT: "{SYM_IO_INPUT}"
IO_OUTPUT: "{SYM_IO_OUTPUT}"
JMP_FWD: "{SYM_JMP_FWD}"
JMP_BCK: "{SYM_JMP_BACKWARD}"
COMMENT: /[^{IGNORE_REGEX}]+/
%ignore COMMENT
'''

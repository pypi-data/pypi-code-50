# Functions to convert two's complement integer to gray code and vice versa.
#
# Copyright (c) 2020 Heikki Orsila <heikki.orsila@iki.fi>
#
# See https://en.wikipedia.org/wiki/Gray_code for details about gray codes.
#
# Example:
#
# import graycode
#
# graycode.tc_to_gray_code(2) == 3
# graycode.gray_code_to_tc(3) == 2

from typing import List


def gen_gray_codes(n: int) -> List[int]:
    assert n > 0
    if n == 1:
        return [0, 1]
    shorter_gray_codes = gen_gray_codes(n - 1)
    bitmask = 1 << (n - 1)
    gray_codes = list(shorter_gray_codes)
    for gray_code in reversed(shorter_gray_codes):
        gray_codes.append(bitmask | gray_code)
    return gray_codes


def _find_msb(x: int) -> int:
    if x < 0:
        raise AssertionError('x must be a non-negative integer')
    elif x == 0:
        return -1
    msb = 0
    while x >= 256:
        x >>= 8
        msb += 8
    if x >= 16:
        x >>= 4
        msb += 4
    while x > 1:
        x >>= 1
        msb += 1
    return msb


def gray_code_to_tc(g: int) -> int:
    """gray_code_to_tc(g) converts gray code integer g to two's complement
    integer. Raises ValueError if g < 0.
    """
    x = g
    mask = x >> 1
    while mask > 0:
        x ^= mask
        mask >>= 1
    return x


def tc_to_gray_code(x: int) -> int:
    """tc_to_gray_code(x) converts two's complement integer x to gray code
    integer. Raises ValueError if x < 0.
    """
    if x < 0:
        raise AssertionError('x must be non-negative')
    return x ^ (x >> 1)

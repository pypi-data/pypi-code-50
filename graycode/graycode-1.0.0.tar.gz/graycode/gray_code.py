# Functions to convert two's complement integer to gray code and vice versa.
#
# Copyright (c) 2020 Heikki Orsila <heikki.orsila@iki.fi>
#
# See https://en.wikipedia.org/wiki/Gray_code for details about gray codes.
#
# Example:
#
# >>> import gray_code
# >>> tc_to_gray_code(2) == 3
# >>> gray_code_to_tc(3) == 2

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
    msb = _find_msb(g)
    if msb < 0:
        return 0
    xor = 0
    bit = msb
    x = 0
    while bit >= 0:
        shifted_bit = (1 << bit) & g
        x |= shifted_bit ^ xor
        xor = (xor ^ shifted_bit) >> 1
        bit -= 1
    return x


def _itgc(x: int, bit: int) -> int:
    mask = (1 << bit)
    shifted_bit = (mask & x)
    if bit == 0:
        return shifted_bit
    if shifted_bit == 0:
        return shifted_bit | _itgc(x, bit - 1)
    else:
        submask = mask - 1
        return shifted_bit | _itgc(submask - (x & submask), bit - 1)


def tc_to_gray_code(x: int) -> int:
    """tc_to_gray_code(x) converts two's complement integer x to gray code
    integer. Raises ValueError if x < 0.
    """
    msb = _find_msb(x)
    if msb < 0:
        return 0
    return _itgc(x, msb)

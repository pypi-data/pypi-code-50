# -*- coding: UTF-8 -*-

import string
import random

__SHORT_NAME_SIZE = 6
__ASCII_CHARACTER = string.ascii_letters + string.digits


def generate(length=__SHORT_NAME_SIZE):
    return ''.join(random.sample(__ASCII_CHARACTER, length))

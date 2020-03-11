"""
SRC path appender for local use of pykrete
Author: Shai Bennathan - shai.bennathan@gmail.com
(C) 2020
"""

import sys
from os.path import dirname


def print_path():
    """prints sys.path"""
    print(str(sys.path))


sys.path.append(dirname(__file__) + '\\src')
print_path()

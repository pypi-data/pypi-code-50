#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .utils import *
from .timelogger import Timer

try:
    from .version import version
except ImportError:
    version = 'git.development'
__version__ = version

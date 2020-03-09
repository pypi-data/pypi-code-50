from .version import __version__  # noqa
import os
import sys

sys.path.append(os.path.dirname(__file__))

from agilicus_api import *  # noqa

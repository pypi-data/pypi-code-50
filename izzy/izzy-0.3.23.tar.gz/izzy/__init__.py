
from .classification import *
from .datasets import *
from .defaults import *
from .eda import *
from .features import *
from .io import *
from .misc import *
from .regression import *
from .tests import *
from .version import __version__
from .viz import *

from . import datasets


# TODO pandas.modin for speedup? Make this an option
__all__ = []
__all__.extend(datasets.__all__)

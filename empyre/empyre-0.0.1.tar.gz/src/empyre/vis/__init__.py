# -*- coding: utf-8 -*-
# Copyright 2020 by Forschungszentrum Juelich GmbH
# Author: J. Caron
#
"""Subpackage containing functionality for visualisation of multidimensional fields."""

from . import colors
from .plot2d import *
from .decorators import *
from .tools import *


__all__ = ['colors']
__all__.extend(plot2d.__all__)
__all__.extend(decorators.__all__)
__all__.extend(tools.__all__)


del decorators
del plot2d
del tools

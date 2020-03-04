# -*- coding: utf-8 -*-
# Copyright 2020 by Forschungszentrum Juelich GmbH
# Author: J. Caron
#
"""Subpackage containing container classes for multidimensional fields and ways to create them."""

from .field import *
from .shapes import *
from .vectors import *


__all__ = []
__all__.extend(field.__all__)
__all__.extend(shapes.__all__)
__all__.extend(vectors.__all__)


del field
del shapes
del vectors

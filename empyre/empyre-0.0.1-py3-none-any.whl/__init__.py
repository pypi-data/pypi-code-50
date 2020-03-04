# -*- coding: utf-8 -*-
# Copyright 2020 by Forschungszentrum Juelich GmbH
# Author: J. Caron
#
"""Subpackage containing functionality for visualisation of multidimensional fields."""

from . import fields
from . import io
from . import models
from . import reconstruct
from . import vis
from .version import version as __version__
from .version import git_revision as __git_revision__

import logging
_log = logging.getLogger(__name__)
_log.info(f'Imported EMPyRe V-{__version__} GIT-{__git_revision__}')
del logging


__all__ = ['fields', 'io', 'models', 'reconstruct', 'vis']


del version

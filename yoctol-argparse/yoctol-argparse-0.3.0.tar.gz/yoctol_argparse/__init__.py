from .__version__ import (
    __title__,
    __version__,
    __description__,
    __author__,
)

from .actions import IdValuePair, IdKwargs
from .formatters import YoctolFormatter
from .parser import YoctolArgumentParser
from .types import (
    int_in_range,
    float_in_range,
    path,
    filepath,
    dirpath,
)

# just for import sugar
from argparse import (
    FileType,
    Namespace,
    Action,
    ONE_OR_MORE,
    OPTIONAL,
    REMAINDER,
    SUPPRESS,
    ZERO_OR_MORE,
)

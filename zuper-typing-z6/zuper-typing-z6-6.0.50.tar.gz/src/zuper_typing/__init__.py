__version__ = "6.0.50"

from zuper_commons.logs import ZLogger

logger = ZLogger(__name__)
logger.info(f"zuper-typing {__version__}")

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    # noinspection PyUnresolvedReferences
    from dataclasses import dataclass

    # noinspection PyUnresolvedReferences
    from typing import Generic

    raise Exception()
else:
    # noinspection PyUnresolvedReferences
    from .monkey_patching_typing import my_dataclass as dataclass

    # noinspection PyUnresolvedReferences
    from .monkey_patching_typing import ZenericFix as Generic

from .debug_print_ import *
from .subcheck import *
from .annotations_tricks import *
from .my_dict import *
from .aliases import *
from .get_patches_ import *
from .zeneric2 import *
from .structural_equalities import *

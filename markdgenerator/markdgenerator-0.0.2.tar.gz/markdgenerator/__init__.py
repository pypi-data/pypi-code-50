from .__about__ import (
    __title__,
    __summary__,
    __version__,
    __author__,
    __email__,
)
from markdgenerator.pandoc import PandocMdGenerator
from markdgenerator.config import NEWLINE
import logging

logging_level = logging.INFO
logging.basicConfig(
    level=logging_level,
    format="%(asctime)s [%(levelname)s]: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

__all__ = [
    "__title__",
    "__summary__",
    "__version__",
    "__author__",
    "__email__",
    "PandocMdGenerator",
    "NEWLINE"
]
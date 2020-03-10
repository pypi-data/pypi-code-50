from ._version import get_versions
from .parser import Parser

__version__ = get_versions()["version"]
del get_versions

__all__ = [Parser]

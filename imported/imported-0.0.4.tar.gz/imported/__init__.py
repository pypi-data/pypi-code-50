"""imported module."""
from inspect import getmembers, ismodule
from types import ModuleType
from typing import Dict, Optional, Union


__version__ = '0.0.4'

version_types = Union[str, int, float]


def get_version(m: ModuleType) -> Optional[version_types]:
    """Get conventional version attribute from module, if any."""
    VERSION_ATTRS = ['__version__', 'VERSION', 'version', ]
    for v in VERSION_ATTRS:
        if hasattr(m, v):
            return getattr(m, v)
    return None


def has_version(m: ModuleType) -> bool:
    """Check if module has a convential version attribute."""
    if get_version(m):
        return True
    return False


def get_imported(context: dict, limit: int = 0,
                 depth: int = 0) -> Dict[str, Optional[version_types]]:
    """Create list of imported modules in given context.

    Only outputs modules from given context that have
    conventional version attributes.
    Context is typically globals() or locals().
    """
    imports = {}
    try:
        for name, val in context.items():
            if ismodule(val):
                if depth < limit:
                    imports.update(
                        get_imported(dict(getmembers(val)), limit, depth + 1))
                f = getattr(val, '__file__', name)
                if has_version(val) and f not in imports.values():
                    n = getattr(val, '__name__', name)
                    imports.update({n: f})
    except AttributeError:
        pass
    return imports


def get_imports(context: dict, limit: int = 0) -> str:
    """Create string list of imported modules in given context.

    Only outputs modules from given context that have
    conventional version attributes.
    Context is typically globals() or locals().
    """
    imports = get_imported(context, limit)
    return ",".join(sorted(set(imports.keys())))

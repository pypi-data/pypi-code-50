"""
Functions for working with XDG paths.

The :func:`setenv` function sets all XDG single directory environment variables to their values.


"""
import os

import xdg


__all__ = [
    "setenv",
]


def setenv():
    """
    Set all XDG single directory environment variables (:ev:`XDG_DATA_HOME`, :ev:`XDG_CONFIG_HOME`, :ev:`XDG_CACHE_HOME`, :ev:`XDG_RUNTIME_DIR`)

    This function needs to be called only once.


    .. warning:: As per XDG specifications, :ev:`XDG_RUNTIME_DIR` can be **None**.


    Parameters
    ----------
    None:

    Returns
    -------
    dict:
        Returns a dictionnary of XDG environment variable name and value.

    Example
    -------

    .. code-block:: python

        from torxtools import xdgutils
        from torxtools import pathutils
        xdgutils.setenv()
        assert pathutils.expandpath('~/.config') == pathutils.expandpath(os.environ["XDG_CONFIG_HOME"])

    See Also
    --------
    `XDG Base Directory Specification <https://specifications.freedesktop.org/basedir-spec/basedir-spec-latest.html>`__

    """
    rv = {}
    for k in ["XDG_DATA_HOME", "XDG_CACHE_HOME", "XDG_CONFIG_HOME", "XDG_RUNTIME_DIR"]:
        if k not in os.environ:
            if xdg.__dict__[k]:
                os.environ[k] = str(xdg.__dict__[k])
        rv[k] = os.environ.get(k)
    return rv

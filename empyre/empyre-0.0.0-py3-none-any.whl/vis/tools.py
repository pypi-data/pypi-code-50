# -*- coding: utf-8 -*-
# Copyright 2020 by Forschungszentrum Juelich GmbH
# Author: J. Caron
#
"""This module provides helper functions to the vis module."""


import os
import glob
import shutil
import logging
from numbers import Number
from contextlib import contextmanager

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

from ..fields.field import Field


__all__ = ['new', 'savefig', 'calc_figsize', 'use_style', 'copy_mpl_stylesheets']
_log = logging.getLogger(__name__)


def new(nrows=1, ncols=1, mode='image', figsize=None, textwidth=None, width_scale=1, aspect=None, **kwargs):
    R"""Convenience function for the creation of a new subplot grid (wraps `~matplotlib.pyplot.subplots`).

    If you use the `textwidth` parameter, plot sizes are fitting into publications with LaTeX. Requires two stylesheets
    `empyre-image` and `empyre-plot` corresponding to its two `mode` settings. Those stylesheets use
    `constrained_layout=True` to achieve well behaving plots without much whitespace around. This function should work
    fine for a small number of images (e.g. 1, 2x2, etc.), for more fine grained control, the contexts can be used
    directly if they are installed corretly, or use width_scale to build the images separately (e.g. 2 adjacent with
    width=0.5). For images, it is assumed that most images are square (and therefore `aspect=1`).

    Parameters
    ----------
    nrows : int, optional
        Number of rows of the subplot grid, by default 1
    ncols : int, optional
        Number of columns of the subplot grid, by default 1
    mode : {'image', 'plot'}, optional
        Mode of the new subplot grid, by default 'image'. Both modes have dedicated matplotlib styles which are used
        and which are installed together with EMPyRe. The 'image' mode disables axis labels and ticks, mainly intended
        to be used with `~matplotlib.pyplot.imshow` with `~empyre.vis.decorators.scalebar`, while the 'plot'
        mode should be used for traditional plots like with `~matplotlib.pyplot.plot` or `~matplotlib.pyplot.scatter`.
    figsize : (float, float), optional
        Width and height of the figure in inches, defaults to rcParams["figure.figsize"], which depends on the chosen
        stylesheet. If set, this will overwrite all other following parameters.
    textwidth : float, optional
        The textwidth of your LaTeX document in points, which you can get py using "\the\textwidth". If this is not None
        (the default), this will be used to define the figure size if it is not set explicitely.
    width_scale : float, optional
        Only meaningful if `textwidth` is set. If it is, `width_scale` will be a scaling factor for the figure width.
        Example: if you set this to 0.5, your figure will span half of the textwidth. Default is 1.
    aspect : float, optional
        Aspect ratio of the figure height relative to the figure width. If None (default), the aspect is set to be 1
        for `mode=image` and to 'golden' for `mode=plot`, which adjusts the aspect to represent the golden ratio of
        0.6180... If `ncols!=nrows`, it often makes sense to use `aspect=nrows/ncols` here.

    Returns
    -------
    fig : :class:`~matplotlib.figure.Figure`
        The constructed figure.
    axes : axes.Axes object or array of Axes objects.
        axes can be either a single Axes object or an array of Axes objects if more than one subplot was created.
        The dimensions of the resulting array can be controlled with the squeeze keyword argument.

    Notes
    -----
    additional kwargs are passed to `~matplotlib.pyplot.subplots`.

    """
    _log.debug('Calling new')
    assert mode in ('image', 'plot'), "mode has to be 'image', or 'plot'!"
    if figsize is None and textwidth is not None:  # Only then is all this necessary:
        if aspect is None:
            aspect = 'golden' if mode == 'plot' else 1  # Both image modes have 'same' as default'!
        elif isinstance(aspect, Field):
            dim_uv = [d for d in aspect.dim if d != 1]
            assert len(dim_uv) == 2, f"Couldn't find fields aspect ({len(dim_uv)} squeezed dimensions, has to be of 2)!"
            aspect = dim_uv[0]/dim_uv[1]  # height/width
        else:
            assert isinstance(aspect, Number), 'aspect has to be None, a number or a field instance squeezable to 2D!'
        figsize = calc_figsize(width_scale=width_scale, aspect=aspect, textwidth=textwidth)
    if mode == 'image':
        with use_style('empyre-image'):
            return plt.subplots(nrows=nrows, ncols=ncols, figsize=figsize, **kwargs)
    else:  # mode == 'plot':
        with use_style('empyre-plot'):
            return plt.subplots(nrows=nrows, ncols=ncols, figsize=figsize, **kwargs)


def savefig(fname, **kwargs):
    """Utility wrapper around :func:`~matplotlib.pyplot.savefig` to save the current figure.

    Parameters
    ----------
    fname : str or PathLike or file-like object
        Path to the file wherein the figure should be saved.

    Notes
    -----
    Uses the 'empyre-save' stylesheet (installed together with EMPyRe to control the saving behaviour. Any kwargs are
    passed to :func:`~matplotlib.pyplot.savefig`.

    """
    _log.debug('Calling savefig')
    with use_style('empyre-save'):
        plt.savefig(fname, **kwargs)


def calc_figsize(textwidth, width_scale=1, aspect=1):
    R"""Helper function to calculate the figure size from various parameters. Useful for publications via LaTeX.

    Parameters
    ----------
    textwidth : float
        The textwidth of your LaTeX document in points, which you can get py using "\the\textwidth".
    width_scale : float, optional
        Scaling factor for the figure width. Example: if you set this to 0.5, your figure will span half of the
        textwidth. Default is 1.
    aspect : float, optional
        Aspect ratio of the figure height relative to the figure width. If None (default), the aspect is set to be 1
        for `mode=image` and to 'golden' for `mode=plot`, which adjusts the aspect to represent the golden ratio of
        0.6180...

    Returns
    -------
    figsize: (float, float)
        The determined figure size

    Notes
    -----
    Based on snippet from Florian Winkler.

    """
    _log.debug('Calling calc_figsize')
    GOLDEN_RATIO = (1 + np.sqrt(5)) / 2   # Aesthetic ratio!
    INCHES_PER_POINT = 1.0 / 72.27  # Convert points to inch, LaTeX constant, apparently...
    textwidth_in = textwidth * INCHES_PER_POINT  # Width of the text in inches
    fig_width = textwidth_in * width_scale  # Width in inches
    if aspect == 'golden':
        fig_height = fig_width / GOLDEN_RATIO
    elif isinstance(aspect, Number):
        fig_height = textwidth_in * aspect
    else:
        raise ValueError(f"aspect has to be either a number, 'same' or 'golden'! Was {aspect}!")
    fig_size = [fig_width, fig_height]  # Both in inches
    return fig_size


@contextmanager
def use_style(stylename):
    """Context that uses a matplotlib stylesheet. Can fall back to local mpl stylesheets if necessary!

    Parameters
    ----------
    stylename : str
        A style specification.

    Yields
    -------
    context
        Context manager for using style settings temporarily.

    """
    try:  # Try to load the style directly (works if it is installed somewhere mpl looks for it):
        with plt.style.context(stylename) as context:
            yield context
    except OSError:  # Stylesheet not found, use local ones:
        mplstyle_path = os.path.join(os.path.dirname(__file__), 'mplstyles', f'{stylename}.mplstyle')
        with plt.style.context(mplstyle_path) as context:
            yield context


def copy_mpl_stylesheets():
    """Copy matplotlib styles to the users matplotlib config directory. Useful if you want to utilize them elsewhere.

    Notes
    -----
    You might need to restart your Python session for the stylesheets to be recognized/found!

    """
    # Find matplotlib styles:
    user_stylelib_path = os.path.join(mpl.get_configdir(), 'stylelib')
    vis_dir = os.path.dirname(__file__)
    style_files = glob.glob(os.path.join(vis_dir, 'mplstyles', '*.mplstyle'))
    # Copy them to the local matplotlib styles folder:
    if not os.path.exists(user_stylelib_path):
        os.makedirs(user_stylelib_path)
    for style_path in style_files:
        _, fname = os.path.split(style_path)
        dest = os.path.join(user_stylelib_path, fname)
        shutil.copy(style_path, dest)

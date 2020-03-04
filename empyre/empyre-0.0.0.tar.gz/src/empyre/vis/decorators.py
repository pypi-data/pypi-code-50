# -*- coding: utf-8 -*-
# Copyright 2020 by Forschungszentrum Juelich GmbH
# Author: J. Caron
#
"""This module provides functions that decorate exisiting `matplotlib` plots."""


import logging
from collections.abc import Iterable

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import patheffects
from matplotlib.patches import Circle
from matplotlib.offsetbox import TextArea, AnchoredOffsetbox
from mpl_toolkits.axes_grid1.anchored_artists import AnchoredSizeBar
from mpl_toolkits.axes_grid1.inset_locator import inset_axes

from . import colors
from .tools import use_style
from ..fields.field import Field


__all__ = ['scalebar', 'colorwheel', 'annotate', 'quiverkey', 'coords', 'colorbar']

_log = logging.getLogger(__name__)


def scalebar(axis=None, unit='nm', loc='lower left', **kwargs):
    """Add a scalebar to the axis.

    Parameters
    ----------
    axis : :class:`~matplotlib.axes.AxesSubplot`, optional
        Axis to which the scalebar is added, by default None, which will pick the last used axis via `gca`.
    unit: str, optional
        String that determines the unit of the scalebar, defaults to 'nm'.
    loc : str or pair of floats, optional
        The location of the scalebar, defaults to 'lower left'. See `matplotlib.legend` for possible settings.

    Returns
    -------
    aoffbox : :class:`~matplotlib.offsetbox.AnchoredOffsetbox`
        The box containing the scalebar.

    Notes
    -----
    Additional kwargs are passed to `mpl_toolkits.axes_grid1.anchored_artists.AnchoredSizeBar`.

    """
    _log.debug('Calling scalebar')
    if axis is None:  # If no axis is set, find the current or create a new one:
        axis = plt.gca()
    # Transform axis borders (1, 1) to data borders to get number of pixels in y and x:
    transform = axis.transData
    bb0 = axis.transLimits.inverted().transform((0, 0))
    bb1 = axis.transLimits.inverted().transform((1, 1))
    data_extent = (int(abs(bb1[1] - bb0[1])), int(abs(bb1[0] - bb0[0])))
    # Calculate bar length:
    bar_length = data_extent[1] / 4  # 25% of the data width!
    thresholds = [1, 5, 10, 50, 100, 500, 1000]
    for t in thresholds:  # For larger grids (real images), multiples of threshold look better!
        if bar_length > t:  # Round down to the next lowest multiple of t:
            bar_length = (bar_length // t) * t
    # Set parameters for scale bar:
    label = f'{bar_length:g} {unit}'
    # Set defaults:
    kwargs.setdefault('borderpad', 0.2)
    kwargs.setdefault('pad', 0.2)
    kwargs.setdefault('sep', 5)
    kwargs.setdefault('color', 'w')
    kwargs.setdefault('size_vertical', data_extent[0]*0.01)
    kwargs.setdefault('frameon', False)
    kwargs.setdefault('label_top', True)
    kwargs.setdefault('fill_bar', True)
    # Create scale bar:
    scalebar = AnchoredSizeBar(transform, bar_length, label, loc, **kwargs)
    scalebar.txt_label._text._color = 'w'  # Overwrite AnchoredSizeBar color!
    # Set stroke patheffect:
    effect_txt = [patheffects.withStroke(linewidth=2, foreground='k')]
    scalebar.txt_label._text.set_path_effects(effect_txt)
    effect_bar = [patheffects.withStroke(linewidth=3, foreground='k')]
    scalebar.size_bar._children[0].set_path_effects(effect_bar)
    # Add scale bar to axis and return:
    axis.add_artist(scalebar)
    return scalebar


def colorwheel(axis=None, cmap=None, ax_size='20%', loc='upper right', **kwargs):
    """Add a colorwheel to the axis on the upper right corner.

    Parameters
    ----------
    axis : :class:`~matplotlib.axes.Axes`, optional
        Axis to which the colorwheel is added, by default None, which will pick the last used axis via `gca`.
    cmap : str or `matplotlib.colors.Colormap`, optional
        The Colormap that should be used for the colorwheel, defaults to `None`, which chooses a map specified by
        `.colors.CMAP_CIRCULAR_DEFAULT`. Needs to be a :class:`~.colors.Colormap3D`.
    ax_size : str or float, optional
        String or float determining the size of the inset axis used, defaults to `20%`.
    loc : str or pair of floats, optional
        The location of the colorwheel, defaults to 'upper right'. See `matplotlib.legend` for possible settings.

    Returns
    -------
    axis : :class:`~matplotlib.image.AxesImage`
        The colorwheel image that was created.

    Notes
    -----
    Additional kwargs are passed to :class:`~.colors.Colormap3D.plot_colorwheel` of the :class:`~.colors.Colormap3D`.

    """
    _log.debug('Calling colorwheel')
    if axis is None:  # If no axis is set, find the current or create a new one:
        axis = plt.gca()
    ins_axes = inset_axes(axis, width=ax_size, height=ax_size, loc=loc)
    ins_axes.axis('off')
    if cmap is None:
        cmap = colors.CMAP_CIRCULAR_DEFAULT
    plt.sca(axis)  # Set focus back to parent axis!
    return cmap.plot_colorwheel(axis=ins_axes, **kwargs)


def annotate(label, axis=None, loc='upper left'):
    """Add an annotation to the axis on the upper left corner.

    Parameters
    ----------
    label : string
        The text of the annotation.
    axis : :class:`~matplotlib.axes.AxesSubplot`, optional
        Axis to which the annotation is added, by default None, which will pick the last used axis via `gca`.
    loc : str or pair of floats, optional
        The location of the annotation, defaults to 'upper left'. See `matplotlib.legend` for possible settings.

    Returns
    -------
    aoffbox : :class:`~matplotlib.offsetbox.AnchoredOffsetbox`
        The box containing the annotation.

    """
    _log.debug('Calling annotate')
    if axis is None:  # If no axis is set, find the current or create a new one:
        axis = plt.gca()
    # Create text:
    txt = TextArea(label, textprops={'color': 'w'})
    txt.set_clip_box(axis.bbox)
    txt._text.set_path_effects([patheffects.withStroke(linewidth=2, foreground='k')])
    # Pack into and add AnchoredOffsetBox:
    aoffbox = AnchoredOffsetbox(loc=loc, pad=0.5, borderpad=0.1, child=txt, frameon=False)
    axis.add_artist(aoffbox)
    return aoffbox


def quiverkey(quiv, field, axis=None, unit='', loc='lower right', **kwargs):
    """Add a quiver key to an axis.

    Parameters
    ----------
    quiv : Quiver instance
        The quiver instance returned by a call to quiver.
    field : `Field` or ndarray
        The vector data as a `Field` or a numpy array (in the latter case, `vector=True` and `scale=1` are assumed).
    axis : :class:`~matplotlib.axes.AxesSubplot`, optional
        Axis to which the quiverkey is added, by default None, which will pick the last used axis via `gca`.
    unit: str, optional
        String that determines the unit of the quiverkey, defaults to ''.
    loc : str or pair of floats, optional
        The location of the quiverkey, defaults to 'lower right'. See `matplotlib.legend` for possible settings.

    Returns
    -------
    qk: Quiverkey
        The generated quiverkey.

    Notes
    -----
    Additional kwargs are passed to `matplotlib.pyplot.quiverkey`.

    """
    _log.debug('Calling quiverkey')
    if axis is None:  # If no axis is set, find the current or create a new one:
        axis = plt.gca()
    if not isinstance(field, Field):  # Try to convert input to Field if it is not already one:
        field = Field(data=np.asarray(field), scale=1, vector=True)
    length = field.amp.data.max()
    shift = 1 / field.squeeze().dim[1]  # equivalent to one pixel distance in axis coords!
    label = f'{length:.3g} {unit}'
    if loc in ('upper right', 1):
        X, Y, labelpos = 0.95-shift, 0.95-shift/4, 'W'
    elif loc in ('upper left', 2):
        X, Y, labelpos = 0.05+shift, 0.95-shift/4, 'E'
    elif loc in ('lower left', 3):
        X, Y, labelpos = 0.05+shift, 0.05+shift/4, 'E'
    elif loc in ('lower right', 4):
        X, Y, labelpos = 0.95-shift, 0.05+shift/4, 'W'
    else:
        raise ValueError('Quiverkey can only be placed in one of the corners (number 1 - 4 or associated strings)!')
    # Set defaults:
    kwargs.setdefault('coordinates', 'axes')
    kwargs.setdefault('facecolor', 'w')
    kwargs.setdefault('edgecolor', 'k')
    kwargs.setdefault('labelcolor', 'w')
    kwargs.setdefault('linewidth', 1)
    kwargs.setdefault('clip_box', axis.bbox)
    kwargs.setdefault('clip_on', True)
    # Plot:
    qk = axis.quiverkey(quiv, X, Y, U=1, label=label, labelpos=labelpos, **kwargs)
    qk.text.set_path_effects([patheffects.withStroke(linewidth=2, foreground='k')])
    return qk


def coords(axis=None, coords=('x', 'y'), loc='lower left', **kwargs):
    """Add coordinate arrows to an axis.

    Parameters
    ----------
    axis : :class:`~matplotlib.axes.AxesSubplot`, optional
        Axis to which the coordinates are added, by default None, which will pick the last used axis via `gca`.
    coords : tuple or int, optional
        Tuple of strings determining the labels, by default ('x', 'y'). Can also be `2` or `3` which expands to
        ('x', 'y') or ('x', 'y', 'z'). The length of `coords` determines the number of arrows (2 or 3).
    loc : str, optional
        [description], by default 'lower left'

    Returns
    -------
    ins_axes : :class:`~matplotlib.axes.Axes`
        The created inset axes containing the coordinates.

    """
    _log.debug('Calling coords')
    if axis is None:  # If no axis is set, find the current or create a new one:
        axis = plt.gca()
    ins_ax = inset_axes(axis, width='5%', height='5%', loc=loc, borderpad=2.2)
    if coords == 3:
        coords = ('x', 'y', 'z')
    elif coords == 2:
        coords = ('x', 'y')
    effects = [patheffects.withStroke(linewidth=2, foreground='k')]
    kwargs.setdefault('fc', 'w')
    kwargs.setdefault('ec', 'k')
    kwargs.setdefault('head_width', 0.6)
    kwargs.setdefault('head_length', 0.7)
    kwargs.setdefault('linewidth', 1)
    kwargs.setdefault('width', 0.2)
    if len(coords) == 3:
        ins_ax.arrow(x=0.5, y=0.5, dx=-1.05, dy=-0.75, clip_on=False, **kwargs)
        ins_ax.arrow(x=0.5, y=0.5, dx=0.96, dy=-0.75, clip_on=False, **kwargs)
        ins_ax.arrow(x=0.5, y=0.5, dx=0, dy=1.35, clip_on=False, **kwargs)
        ins_ax.annotate(coords[0], xy=(0, 0), xytext=(-1.0, 0.3), path_effects=effects, color='w')
        ins_ax.annotate(coords[1], xy=(0, 0), xytext=(1.7, 0.3), path_effects=effects, color='w')
        ins_ax.annotate(coords[2], xy=(0, 0), xytext=(0.8, 1.5), path_effects=effects, color='w')
        ins_ax.add_artist(Circle((0.5, 0.5), 0.12, fc='w', ec='k', linewidth=1, clip_on=False))
    elif len(coords) == 2:
        ins_ax.arrow(x=-0.5, y=-0.5, dx=1.5, dy=0, clip_on=False, **kwargs)
        ins_ax.arrow(x=-0.5, y=-0.5, dx=0, dy=1.5, clip_on=False, **kwargs)
        ins_ax.annotate(coords[0], xy=(0, 0), xytext=(1.3, -0.05), path_effects=effects, color='w')
        ins_ax.annotate(coords[1], xy=(0, 0), xytext=(-0.1, 1.1), path_effects=effects, color='w')
        ins_ax.add_artist(Circle((-0.5, -0.5), 0.12, fc='w', ec='k', linewidth=1, clip_on=False))
    ins_ax.axis('off')
    plt.sca(axis)
    return coords


def colorbar(im, fig=None, cbar_axis=None, axes=None, position='right', pad=0.02, thickness=0.03, label=None,
             constrain_ticklabels=True, ticks=None, ticklabels=None):
    """Creates a colorbar, aligned with figure axes.

    Parameters
    ----------
    im : matplotlib object, mappable
        Mappable matplotlib object.
    fig : matplotlib.figure object, optional
        The figure object that contains the matplotlib axes and artists, by default None, which will pick the last used
        figure via `gcf`.
    axes : matplotlib.axes or list of matplotlib.axes
        The axes object(s), where the colorbar is drawn, by default None, which will pick the last used axis via `gca`.
        Only provide those axes, which the colorbar should span over.
    position : str, optional
        The position defines the location of the colorbar. One of 'top', 'bottom', 'left' or 'right' (default).
    pad : float, optional
        Defines the spacing between the axes and colorbar axis. Is given in figure fraction.
    thickness : float, optional
        Thickness of the colorbar given in figure fraction.
    label : string, optional
        Colorbar label, defaults to None.
    constrain_ticklabels : bool, optional
        Allows to slightly shift the outermost ticklabels, such that they do not exceed the cbar axis, defaults to True.
    ticks : list, np.ndarray, optional
        List of cbar ticks, defaults to None.
    ticklabels : list, np.ndarray, optional
        List of cbar ticklabels, defaults to None.

    Returns
    -------
    cbar : :class:`~matplotlib.Colorbar`
        The created colorbar.

    Notes
    -----
    Based on a modified snippet by Florian Winkler. Note that this function TURNS OFF constrained layout, therefore it
    should be the final command before finishing or saving a figure. The colorbar will be outside the original bounds
    of your constructed figure. If you set the size, e.g. with `~empyre.vis.tools.new`, make sure to account for the
    additional space by setting the `width_scale` to something smaller than 1 (e.g. 0.9).

    """
    _log.debug('Calling colorbar')
    assert position in ('left', 'right', 'top', 'bottom'), "position has to be 'left', 'right', 'top' or 'bottom'!"
    if fig is None:  # If no figure is set, find the current or create a new one:
        fig = plt.gcf()
    fig.canvas.draw()  # Trigger a draw so that a potential constrained_layout is executed once!
    fig.set_constrained_layout(False)  # we don't want the layout to change after this point!
    if axes is None:  # If no axis is set, find the current or create a new one:
        axes = plt.gca()
    if not isinstance(axes, Iterable):
        axes = (axes,)  # Make sure it is an iterable (e.g. tuple)!
    # Save previously active axis for later:
    previous_axis = plt.gca()
    if cbar_axis is None:  # Construct a new cbar_axis:
        x_coords, y_coords = [], []
        # Find bounds of all individual axes:
        for ax in np.ravel(axes):  # ravel needed for arrays of axes:
            points = ax.get_position().get_points()
            x_coords.extend(points[:, 0])
            y_coords.extend(points[:, 1])
        # Find outer bounds of plotting area:
        left, right = min(x_coords), max(x_coords)
        bottom, top = min(y_coords), max(y_coords)
        # Determine where the colorbar will be placed:
        if position == 'right':
            bounds = [right+pad, bottom, thickness, top-bottom]
        elif position == 'left':
            bounds = [left-pad-thickness, bottom, thickness, top-bottom]
        if position == 'top':
            bounds = [left, top+pad, right-left, thickness]
        elif position == 'bottom':
            bounds = [left, bottom-pad-thickness, right-left, thickness]
        cbar_axis = fig.add_axes(bounds)
    # Create the colorbar:
    with use_style('empyre-image'):
        if position in ('left', 'right'):
            cb = plt.colorbar(im, cax=cbar_axis, orientation='vertical')
            cb.ax.yaxis.set_ticks_position(position)
            cb.ax.yaxis.set_label_position(position)
        elif position in ('top', 'bottom'):
            cb = plt.colorbar(im, cax=cbar_axis, orientation='horizontal')
            cb.ax.xaxis.set_ticks_position(position)
            cb.ax.xaxis.set_label_position(position)
        # Colorbar label
        if label is not None:
            cb.set_label(f'{label}')
        # Set ticks and ticklabels (if specified):
        if ticks:
            cb.set_ticks(ticks)
        if ticklabels:
            cb.set_ticklabels(ticklabels)
        # Constrain tick labels (if wanted):
        if constrain_ticklabels:
            if position == 'top' or position == 'bottom':
                t = cb.ax.get_xticklabels()
                t[0].set_horizontalalignment('left')
                t[-1].set_horizontalalignment('right')
            elif position == 'left' or position == 'right':
                t = cb.ax.get_yticklabels()
                t[0].set_verticalalignment('bottom')
                t[-1].set_verticalalignment('top')
    # Set focus back from colorbar to previous axis and return colorbar:
    plt.sca(previous_axis)
    return cb

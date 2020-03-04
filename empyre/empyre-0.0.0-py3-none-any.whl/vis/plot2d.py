# -*- coding: utf-8 -*-
# Copyright 2019 by Forschungszentrum Juelich GmbH
# Author: J. Caron
#
"""This module provides a functions for 2D plots that often wrap functions from `maptlotlib.pyplot`."""


import logging

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
from PIL import Image

from . import colors
from .tools import use_style
from ..fields.field import Field


__all__ = ['imshow', 'contour', 'colorvec', 'cosine_contours', 'quiver']

_log = logging.getLogger(__name__)


DIVERGING_CMAPS = ['PiYG', 'PRGn', 'BrBG', 'PuOr', 'RdGy', 'RdBu', 'RdYlBu', 'RdYlGn',
                   'Spectral', 'coolwarm', 'bwr', 'seismic',  # all divergent maps from matplotlib!
                   'balance', 'delta', 'curl', 'diff', 'tarn']  # all divergent maps from cmocean!
# TODO: add seaborn and more?


def imshow(field, axis=None, cmap=None, **kwargs):
    """Display an image on a 2D regular raster. Wrapper for `matplotlib.pyplot.imshow`.

    Parameters
    ----------
    field : `Field` or ndarray
        The image data as a `Field` or a numpy array (in the latter case, `vector=False` and `scale=1` are assumed).
    axis : `matplotlib.axes.Axes` object, optional
        The axis to which the image should be added, by default None, which will pick the last use axis via `gca`.
    cmap : str or `matplotlib.colors.Colormap`, optional
        The Colormap that should be used for the display, either as a string or object, by default None, which will pick
        `cmocean.cm.balance` if available. `imshow` will automatically detect if a divergent colormap is used and will
        make sure that zero is pinned to the symmetry point of the colormap (this is done by creating a new colormap
        with custom range under the hood).

    Returns
    -------
    axis : `matplotlib.axes.Axes`
        The plotting axis.

    Notes
    -----
    Additional kwargs are passed to `matplotlib.pyplot.imshow`.
    Uses the `empyre-image` stylesheet settings for plotting (and axis creation if none exists, yet).
    Fields are squeezed before plotting, so non-2D fields work as long as their superfluous dimensions have length 1.

    """
    _log.debug('Calling imshow')
    if not isinstance(field, Field):  # Try to convert input to Field if it is not already one:
        field = Field(data=np.asarray(field), scale=1, vector=False)
    assert not field.vector, 'Can only plot scalar fields!'
    # Get squeezed data and make sure it's 2D scalar:
    squeezed_field = field.squeeze()
    assert len(squeezed_field.dim) == 2, 'Cannot plot more than 2 dimensions!'
    # Determine colormap and related important properties and flags:
    if cmap is None:
        try:
            import cmocean
            cmap = cmocean.cm.balance
        except ImportError:
            _log.info('cmocean.balance not found, fallback to rRdBu!')
            cmap = plt.get_cmap('RdBu_r')  # '_r' for reverse!
    elif isinstance(cmap, str):  # make sure we have a Colormap object (and not a string):
        cmap = plt.get_cmap(cmap)
    if cmap.name.replace('_r', '') in DIVERGING_CMAPS:  # 'replace' also matches reverted cmaps!
        # Symmetric colormap only has zero at symmetry point if mappable has symmetric bounds (from - to + limit)!
        vmin = kwargs.get('vmin', squeezed_field.data.min()-1E-30)
        vmax = kwargs.get('vmax', squeezed_field.data.max()+1E-30)
        vmin, vmax = np.min([vmin, 0]), np.max([0, vmax])  # Ensure zero is present!
        kwargs.setdefault('vmin', vmin)
        kwargs.setdefault('vmax', vmax)
        limit = np.max(np.abs([vmin, vmax]))
        # Calculate the subset of colors for the range vmin to vmax (often not full range of 2*limit):
        start = 0.5 + vmin/(2*limit)  # 0 for symmetric bounds, >0: unused colors at lower end!
        end = 0.5 + vmax/(2*limit)  # 1 for symmetric bounds, <1: unused colors at upper end!
        cmap_colors = cmap(np.linspace(start, end, 256))  # New color indices with symmetry color at 0.5!
        # Use calculated colors to create custom (asymmetric) colormap with symmetry color (often white) at zero:
        cmap = LinearSegmentedColormap.from_list('custom', cmap_colors)
    # Set extent in data coordinates (left, right, bottom, top) to kwargs (if not set explicitely):
    dim_v, dim_u, s_v, s_u = *squeezed_field.dim, *squeezed_field.scale
    kwargs.setdefault('extent', (0, dim_u * s_u, 0, dim_v * s_v))
    # Plot with the empyre style context:
    with use_style('empyre-image'):  # Only works on axes created WITHIN context!
        if axis is None:  # If no axis is set, find the current or create a new one:
            axis = plt.gca()
        return axis.imshow(squeezed_field, cmap=cmap, **kwargs)


def contour(field, axis=None, **kwargs):
    """Plot contours. Wrapper for `matplotlib.pyplot.contour`.

    Parameters
    ----------
    field : `Field` or ndarray
        The contour data as a `Field` or a numpy array (in the latter case, `vector=False` and `scale=1` are assumed).
    axis : `matplotlib.axes.Axes` object, optional
        The axis to which the contour should be added, by default None, which will pick the last use axis via `gca`.

    Returns
    -------
    axis : `matplotlib.axes.Axes`
        The plotting axis.

    Notes
    -----
    Additional kwargs are passed to `matplotlib.pyplot.contour`.
    Uses the `empyre-image` stylesheet settings for plotting (and axis creation if none exists, yet).
    Fields are squeezed before plotting, so non-2D fields work as long as their superfluous dimensions have length 1.

    """
    _log.debug('Calling contour')
    if not isinstance(field, Field):  # Try to convert input to Field if it is not already one:
        field = Field(data=np.asarray(field), scale=1, vector=False)
    assert not field.vector, 'Can only plot scalar fields!'
    # Get squeezed data and make sure it's 2D scalar:
    squeezed_field = field.squeeze()
    assert len(squeezed_field.dim) == 2, 'Cannot plot more than 2 dimensions!'
    # Create coordinates (respecting the field scale, +0.5: pixel center!):
    vv, uu = (np.indices(squeezed_field.dim) + 0.5) * np.asarray(squeezed_field.scale)[:, None, None]
    # Set kwargs defaults without overriding possible user input:
    kwargs.setdefault('levels', [0.5])
    kwargs.setdefault('colors', 'k')
    kwargs.setdefault('linestyles', 'dotted')
    kwargs.setdefault('linewidths', 2)
    # Plot with the empyre style context:
    with use_style('empyre-image'):  # Only works on axes created WITHIN context!
        if axis is None:  # If no axis is set, find the current or create a new one:
            axis = plt.gca()
            axis.set_aspect('equal')
        return axis.contour(uu, vv, squeezed_field.data, **kwargs)


def colorvec(field, axis=None, **kwargs):
    """Plot an image of a 2D vector field with up to 3 components by color encoding the vector direction.

    In-plane directions are encoded via hue ("color wheel"), making sure that all in-plane directions are isoluminant
    (i.e. a greyscale image would result a homogeneously medium grey image). Out-of-plane directions are encoded via
    brightness with upwards pointing vectors being white and downward pointing vectors being black. The length of the
    vectors are encoded via saturation, with full saturation being fully chromatic (in-plane) or fully white/black
    (up/down). The center of the "color sphere" desaturated in a medium gray and encodes vectors with length zero.

    Parameters
    ----------
    field : `Field` or ndarray
        The image data as a `Field` or a numpy array (in the latter case, `vector=True` and `scale=1` are assumed).
    axis : `matplotlib.axes.Axes` object, optional
        The axis to which the image should be added, by default None, which will pick the last use axis via `gca`.

    Returns
    -------
    axis : `matplotlib.axes.Axes`
        The plotting axis.

    Notes
    -----
    Additional kwargs are passed to `matplotlib.pyplot.imshow`.
    Uses the `empyre-image` stylesheet settings for plotting (and axis creation if none exists, yet).
    Fields are squeezed before plotting, so non-2D fields work as long as their superfluous dimensions have length 1.
    Even though squeezing takes place, `colorvec` "remembers" the original orientation of the slice! This is important
    if you want to plot a slice that should not represent the xy-plane. The colors chosen will respect the original
    orientation of your slice, e.g. a vortex in the xz-plane will include black and white colors (up/down) if the
    `Field` object given as the `field` parameter has `dim=(128, 1, 128)`. If you want to plot a slice of a 3D vector
    with 3 components and make use of this functionality, make sure to not use an integer as an index, as that will
    drop the dimension BEFORE it is passed to `colorvec`, which will have no way of knowing which dimension was dropped.
    Instead, make sure to use a slice of length one (example with `dim=(128, 128, 128)`):
    >>> colorvec(field[:, 15, :])  # Wrong! Shape: (128, 128), interpreted as xy-plane!
    >>> colorvec(field[:, 15:16, :])  # Right! Shape: (128, 1, 128), passed as 3D to `colorvec`, squeezed internally!

    """
    _log.debug('Calling colorvec')
    if not isinstance(field, Field):  # Try to convert input to Field if it is not already one:
        field = Field(data=np.asarray(field), scale=1, vector=True)
    assert field.vector, 'Can only plot vector fields!'
    assert len(field.dim) <= 3, 'Unusable for vector fields with dimension higher than 3!'
    assert len(field.dim) == field.ncomp, ('Assignment of vector components to dimensions is ambiguous!'
                                           f'`ncomp` ({field.ncomp}) must match `len(dim)` ({len(field.dim)})')
    # Get squeezed data and make sure it's 2D scalar:
    squeezed_field = field.squeeze()
    assert len(squeezed_field.dim) == 2, 'Cannot plot more than 2 dimensions!'
    # Extract vector components (fill 3rd component with zeros if field.comp is only 2):
    comp = squeezed_field.comp
    x_comp = comp[0]
    y_comp = comp[1]
    z_comp = comp[2] if (squeezed_field.ncomp == 3) else np.zeros(squeezed_field.dim)
    # Calculate image with color encoded directions:
    rgb = colors.CMAP_CIRCULAR_DEFAULT.rgb_from_vector(np.stack((x_comp, y_comp, z_comp), axis=0))
    # Set extent in data coordinates (left, right, bottom, top) to kwargs (if not set explicitely):
    dim_v, dim_u, s_v, s_u = *squeezed_field.dim, *squeezed_field.scale
    kwargs.setdefault('extent', (0, dim_u * s_u, 0, dim_v * s_v))
    # Plot with the empyre style context:
    with use_style('empyre-image'):  # Only works on axes created WITHIN context!
        if axis is None:  # If no axis is set, find the current or create a new one:
            axis = plt.gca()
        return axis.imshow(Image.fromarray(rgb), **kwargs)


def cosine_contours(field, axis=None, gain='auto', cmap=None, **kwargs):
    """Plots the cosine of the (amplified) field. Wrapper for `matplotlib.pyplot.imshow`.

    Parameters
    ----------
    field : `Field` or ndarray
        The contour data as a `Field` or a numpy array (in the latter case, `vector=False` and `scale=1` are assumed).
    axis : `matplotlib.axes.Axes` object, optional
        The axis to which the contour should be added, by default None, which will pick the last use axis via `gca`.
    gain : float or 'auto', optional
        Gain factor with which the `Field` is amplified before taking the cosine, by default 'auto', which calculates a
        gain factor that would produce roughly 4 cosine contours.
    cmap : str or `matplotlib.colors.Colormap`, optional
        The Colormap that should be used for the display, either as a string or object, by default None, which will pick
        `colors.cmaps['transparent_black']` that will alternate between regions with alpha=0, showing layers below and
        black contours.

    Returns
    -------
    axis : `matplotlib.axes.Axes`
        The plotting axis.

    Notes
    -----
    Additional kwargs are passed to `matplotlib.pyplot.imshow`.
    Uses the `empyre-image` stylesheet settings for plotting (and axis creation if none exists, yet).
    Fields are squeezed before plotting, so non-2D fields work as long as their superfluous dimensions have length 1.

    """
    _log.debug('Calling cosine_contours')
    if not isinstance(field, Field):  # Try to convert input to Field if it is not already one:
        field = Field(data=np.asarray(field), scale=1, vector=False)
    assert not field.vector, 'Can only plot scalar fields!'
    # Get squeezed data and make sure it's 2D scalar:
    squeezed_field = field.squeeze()
    assert len(squeezed_field.dim) == 2, 'Cannot plot more than 2 dimensions (Squeezing did not help)!'
    # Determine colormap and related important properties and flags:
    if cmap is None:
        cmap = colors.cmaps['transparent_black']
    # Calculate gain if 'auto' is selected:
    if gain == 'auto':
        gain = 4 * 2*np.pi / (squeezed_field.amp.data.max() + 1E-30)  # 4: roughly 4 contours!
        gain = round(gain, -int(np.floor(np.log10(abs(gain)))))  # Round to last significant digit!
        _log.info(f'Automatically calculated a gain of: {gain}')
    # Calculate the contours:
    contours = np.cos(gain * squeezed_field)  # Range: [-1, 1]
    contours += 1  # Shift to positive values
    contours /= 2  # Rescale to [0, 1]
    # Set extent in data coordinates (left, right, bottom, top) to kwargs (if not set explicitely):
    dim_v, dim_u, s_v, s_u = *squeezed_field.dim, *squeezed_field.scale
    kwargs.setdefault('extent', (0, dim_u * s_u, 0, dim_v * s_v))
    # Plot with the empyre style context:
    with use_style('empyre-image'):  # Only works on axes created WITHIN context!
        if axis is None:  # If no axis is set, find the current or create a new one:
            axis = plt.gca()
        return axis.imshow(contours, cmap=cmap, **kwargs)


def quiver(field, axis=None, color_angles=False, cmap=None, n_bin='auto', bin_with_mask=True, **kwargs):
    """Plot a 2D field of arrows. Wrapper for `matplotlib.pyplot.imshow`.

    Parameters
    ----------
    field : `Field` or ndarray
        The vector data as a `Field` or a numpy array (in the latter case, `vector=True` and `scale=1` are assumed).
    axis : `matplotlib.axes.Axes` object, optional
        The axis to which the image should be added, by default None, which will pick the last use axis via `gca`.
    color_angles : bool, optional
        Switch that turns on color encoding of the arrows, by default False. Encoding works the same as for the
        `colorvec` function (see for details). If False, arrows are uniformly colored white with black border. In both
        cases, the amplitude is encoded via the transparency of the arrow.
    cmap : str or `matplotlib.colors.Colormap`, optional
        The Colormap that should be used for the arrows, either as a string or object, by default None. Will only be
        used if `color_angles=True`.
    n_bin : float or 'auto', optional
        Number of entries along each axis over which the average is taken, by default 'auto', which automatically
        determines a bin size resulting in roughly 16 arrows along the largest dimension. Usually sensible to leave
        this on to not clutter the image with too many arrows (also due to performance). Can be turned off by setting
        `n_bin=1`. Uses the `..fields.field.Field.bin` method.
    bin_with_mask : bool, optional
        If True (default) and if `n_bin>1`, entries of the constructed binned `Field` that averaged over regions that
        were outside the `..fields.field.Field.mask` will not be assigned an arrow and stay empty instead. This prevents
        errouneous "fade-out" effects of the arrows that would occur even for homogeneous objects.

    Returns
    -------
    quiv : Quiver instance
        The quiver instance that was created.

    Notes
    -----
    Additional kwargs are passed to `matplotlib.pyplot.quiver`.
    Uses the `empyre-image` stylesheet settings for plotting (and axis creation if none exists, yet).
    Fields are squeezed before plotting, so non-2D fields work as long as their superfluous dimensions have length 1.
    Even though squeezing takes place, `quiver` "remembers" the original orientation of the slice and which dimensions
    were squeezed! See `colorvec` for  more information and an example (the same principles apply here, too).
    The transparency of the arrows denotes the 3D(!) amplitude, if you see dots in the plot, that means the amplitude
    is not zero, but simply out of the current plane!

    """
    _log.debug('Calling quiver')
    if not isinstance(field, Field):  # Try to convert input to Field if it is not already one:
        field = Field(data=np.asarray(field), scale=1, vector=True)
    assert field.vector, 'Can only plot vector fields!'
    assert len(field.dim) <= 3, 'Unusable for vector fields with dimension higher than 3!'
    assert len(field.dim) == field.ncomp, ('Assignment of vector components to dimensions is ambiguous!'
                                           f'`ncomp` ({field.ncomp}) must match `len(dim)` ({len(field.dim)})')
    # Get squeezed data and make sure it's 2D scalar:
    squeezed_field = field.squeeze()
    assert len(squeezed_field.dim) == 2, 'Cannot plot more than 2 dimensions (Squeezing did not help)!'
    # Determine binning size if necessary:
    if n_bin == 'auto':
        n_bin = int(np.max((1, np.max(squeezed_field.dim) / 16)))
    # Save old limits in case binning has to use padding:
    u_lim = squeezed_field.dim[1] * squeezed_field.scale[1]
    v_lim = squeezed_field.dim[0] * squeezed_field.scale[0]
    # Bin if necessary:
    if n_bin > 1:
        field_mask = squeezed_field.mask  # Get mask BEFORE binning!
        squeezed_field = squeezed_field.bin(n_bin)
        if bin_with_mask:  # Excludes regions where in and outside are binned together!
            mask = (field_mask.bin(n_bin) == 1)
            squeezed_field *= mask
    # Extract normalized vector components (fill 3rd component with zeros if field.comp is only 2):
    normalised_comp = (squeezed_field / squeezed_field.amp.data.max()).comp
    amplitude = squeezed_field.amp.data / squeezed_field.amp.data.max()
    x_comp = normalised_comp[0].data
    y_comp = normalised_comp[1].data
    z_comp = normalised_comp[2].data if (field.ncomp == 3) else np.zeros(squeezed_field.dim)
    # Create coordinates (respecting the field scale, +0.5: pixel center!):
    vv, uu = (np.indices(squeezed_field.dim) + 0.5) * np.asarray(squeezed_field.scale)[:, None, None]
    # Calculate the arrow colors:
    if color_angles:  # Color angles according to calculated RGB values (only with circular colormaps):
        _log.debug('Encoding angles')
        if cmap is None:
            cmap = colors.CMAP_CIRCULAR_DEFAULT
        rgb = cmap.rgb_from_vector(np.asarray((x_comp, y_comp, z_comp))) / 255
        rgba = np.concatenate((rgb, amplitude[..., None]), axis=-1)
        kwargs.setdefault('color', rgba.reshape(-1, 4))
    else:  # Color amplitude with numeric values, according to cmap, overrides 'color':
        _log.debug('Encoding amplitudes')
        if cmap is None:
            cmap = colors.cmaps['transparent_white']
        C = amplitude  # Numeric values, used with cmap!
    # Check which (if any) indices were squeezed to find out which components are passed to quiver:  # TODO: TEST!!!
    squeezed_indices = np.flatnonzero(np.asarray(field.dim) == 1)
    if not squeezed_indices:  # Separate check, because in this case squeezed_indices == []:
        u_comp = x_comp
        v_comp = y_comp
    elif squeezed_indices[0] == 0:  # Slice of the xy-plane with z squeezed:
        u_comp = x_comp
        v_comp = y_comp
    elif squeezed_indices[0] == 1:  # Slice of the xz-plane with y squeezed:
        u_comp = x_comp
        v_comp = z_comp
    elif squeezed_indices[0] == 2:  # Slice of the zy-plane with x squeezed:
        u_comp = y_comp
        v_comp = z_comp
    # Set specific defaults for quiver kwargs:
    kwargs.setdefault('edgecolor', colors.cmaps['transparent_black'](amplitude).reshape(-1, 4))
    kwargs.setdefault('scale', 1/np.max(squeezed_field.scale))
    kwargs.setdefault('width', np.max(squeezed_field.scale))
    kwargs.setdefault('clim', (0, 1))
    kwargs.setdefault('pivot', 'middle')
    kwargs.setdefault('units', 'xy')
    kwargs.setdefault('scale_units', 'xy')
    kwargs.setdefault('minlength', 0.05)
    kwargs.setdefault('headlength', 2)
    kwargs.setdefault('headaxislength', 2)
    kwargs.setdefault('headwidth', 2)
    kwargs.setdefault('minshaft', 2)
    kwargs.setdefault('linewidths', 1)
    # Plot with the empyre style context:
    with use_style('empyre-image'):  # Only works on axes created WITHIN context!
        if axis is None:  # If no axis is set, find the current or create a new one:
            axis = plt.gca()
        axis.set_xlim(0, u_lim)
        axis.set_ylim(0, v_lim)
        axis.set_aspect('equal')
        if color_angles:
            return axis.quiver(uu, vv, np.asarray(u_comp), np.asarray(v_comp), cmap=cmap, **kwargs)
        else:
            return axis.quiver(uu, vv, np.asarray(u_comp), np.asarray(v_comp), C, cmap=cmap, **kwargs)

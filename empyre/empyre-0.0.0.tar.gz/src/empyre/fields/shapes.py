# -*- coding: utf-8 -*-
# Copyright 2020 by Forschungszentrum Juelich GmbH
# Author: J. Caron
#


import logging

import numpy as np

from .field import Field


__all__ = ['create_shape_slab', 'create_shape_disc', 'create_shape_ellipse', 'create_shape_ellipsoid',
           'create_shape_sphere', 'create_shape_filament', 'create_shape_voxel']

_log = logging.getLogger(__name__)


# TODO: TEST!!!


def create_shape_slab(dim, center=None, width=None, scale=1):
    """Creates a Field object with the shape of a slab as a scalar field in arbitrary dimensions.

    Attributes
    ----------
    dim : tuple
        The dimensions of the grid.
    center : tuple, optional
        The center of the slab in pixel coordinates.
    width : tuple, optional
        The width of the slab in pixel coordinates.
    scale: tuple of float
        Scaling along the dimensions of the underlying data.

    """
    _log.debug('Calling __init__')
    if center is None:
        center = tuple([d/2 for d in dim])
    if width is None:
        width = tuple([d/2 for d in dim])
    assert len(dim) == len(center) == len(width), 'Parameters dim, center and width must have the same dimensions!'
    data = np.zeros(dim)
    bounds = ()
    for i in range(len(dim)):
        start = int(np.floor(center[i] - width[i]/2))
        stop = int(np.ceil(center[i] + width[i]/2))
        bounds += (slice(start, stop),)
    data[bounds] = 1
    return Field(data=data, scale=scale, vector=False)


def create_shape_disc(dim, center=None, radius=None, height=None, axis=0, scale=1):
    """Creates a Field object with the shape of a cylindrical disc in 2D or 3D.

    Attributes
    ----------
    dim : tuple
        The dimensions of the grid.
    center : tuple, optional
        The center of the disc in pixel coordinates.
    radius : float, optional
        The radius of the disc in pixel coordinates.
    height : float, optional
        The height of the disc in pixel coordinates. Unused if only 2D.
    axis : int, optional
        The orientation of the discs orthogonal axis. Only used in 3D case with z-axis as default.
    scale: tuple of float
        Scaling along the dimensions of the underlying data.

    """
    _log.debug('Calling __init__')
    assert len(dim) in (2, 3), 'Disc can only be build in 2 or 3 dimensions!'
    # Find indices of the disc plane axes:
    idx_uv = [0, 1, 2]
    if len(dim) == 3:  # 3D:
        idx_uv.remove(axis)
    else:  # 2D:
        idx_uv.remove(2)
    # Find default values:
    if center is None:
        center = tuple([d/2 for d in dim])
    if radius is None:
        radius = np.max((dim[idx_uv[0]], dim[idx_uv[1]])) / 4
    if height is None and len(dim) == 3:  # only used for 3D!
        height = dim[axis] / 2
        assert height > 0, 'Height has to be a positive scalar value!'
    assert len(dim) == len(center), 'Parameters dim and center must have the same dimensions!'
    assert radius > 0, 'Radius has to be a positive scalar value!'
    coords = np.indices(dim) + 0.5  # 0.5 to get to pixel/voxel center!
    coords = coords - np.asarray(center)[(slice(None),) + (None,)*len(dim)]  # [:, None, None, None]
    data = np.where(np.hypot(coords[idx_uv[0]], coords[idx_uv[1]]) <= radius, 1, 0)
    if len(dim) == 3:  # 3D: Implement bounds above and below the disc:
        height_shape = np.zeros_like(data)
        bounds = [slice(None)] * 3  # i.e.: [:, :, :]
        start = int(np.floor(center[axis] - height/2))
        stop = int(np.ceil(center[axis] + height/2))
        bounds[axis] = slice(start, stop)  # replace with actual bounds along disc symmetry axis
        height_shape[tuple(bounds)] = 1
        data *= height_shape
    return Field(data=data, scale=scale, vector=False)


def create_shape_ellipse(dim, center=None, width=None, height=None, axis=0, scale=1):
    """Creates a Field object with the shape of an ellipse in 2D or 3D.

    Attributes
    ----------
    dim : tuple
        The dimensions of the grid.
    center : tuple, optional
        The center of the ellipse in pixel coordinates.
    width : tuple, optional
        The two half axes of the ellipse in pixel coordinates.
    height : float, optional
        The height of the ellipse in pixel coordinates. Unused if only 2D.
    axis : int, optional
        The orientation of the ellipses orthogonal axis. Only used in 3D case with z-axis as default.
    scale: tuple of float
        Scaling along the dimensions of the underlying data.

    """
    _log.debug('Calling __init__')
    assert len(dim) in (2, 3), 'Ellipse can only be build in 2 or 3 dimensions!'
    # Find indices of the disc plane axes:
    idx_uv = [0, 1, 2]
    if len(dim) == 3:  # 3D:
        idx_uv.remove(axis)
    else:  # 2D:
        idx_uv.remove(2)
    # Find default values:
    if center is None:
        center = tuple([d/2 for d in dim])
    if width is None:
        dim_uv = (dim[idx_uv[0]], dim[idx_uv[1]])
        width = (np.max(dim_uv)*1/3, np.min(dim_uv)*2/3)
    if height is None and len(dim) == 3:  # only used for 3D!
        height = dim[axis] / 2
    assert len(dim) == len(center), 'Parameters dim and center must have the same dimensions!'
    assert len(width) == 2, 'Width has to contain the two half axes!'
    coords = np.indices(dim) + 0.5  # 0.5 to get to pixel/voxel center!
    coords = coords - np.asarray(center)[(slice(None),) + (None,)*len(dim)]  # [:, None, None, None]
    distance = np.hypot(coords[idx_uv[1]] / (width[1]/2), coords[idx_uv[0]] / (width[0]/2))
    data = np.where(distance <= 1, 1, 0)
    if len(dim) == 3:  # 3D: Implement bounds above and below the disc:
        height_shape = np.zeros_like(data)
        bounds = [slice(None)] * 3  # i.e.: [:, :, :]
        start = int(np.floor(center[axis] - height/2))
        stop = int(np.ceil(center[axis] + height/2))
        bounds[axis] = slice(start, stop)  # replace with actual bounds along disc symmetry axis
        height_shape[tuple(bounds)] = 1
        data *= height_shape
    return Field(data=data, scale=scale, vector=False)


def create_shape_ellipsoid(dim, center=None, width=None, scale=1):
    """Creates a Field object with the shape of an ellipsoid in arbitrary dimensions.

    Attributes
    ----------
    dim : tuple
        The dimensions of the grid.
    center : tuple, optional
        The center of the ellipsoid in pixel coordinates.
    width : tuple, optional
        The half axes of the ellipsoid in pixel coordinates.
    scale: tuple of float
        Scaling along the dimensions of the underlying data.

    """
    _log.debug('Calling __init__')
    if center is None:
        center = tuple([d/2 for d in dim])
    if width is None:
        width = tuple([d/2 for d in dim])
    assert len(dim) == len(center) == len(width), 'Parameters dim, center and width must have the same dimensions!'
    coords = np.indices(dim) + 0.5  # 0.5 to get to pixel/voxel center!
    coords = coords - np.asarray(center)[(slice(None),) + (None,)*len(dim)]  # [:, None, None, None]
    distance = np.sqrt([(coords[i] / (width[i]/2))**2 for i in range(len(dim))])
    data = np.where(distance <= 1, 1, 0)
    return Field(data=data, scale=scale, vector=False)


def create_shape_sphere(dim, center=None, radius=None, scale=1):
    """Creates a Field object with the shape of a sphere in arbitrary dimensions.

    Attributes
    ----------
    dim : tuple
        The dimensions of the grid.
    center : tuple, optional
        The center of the sphere in pixel coordinates.
    width : tuple, optional
        The half axes of the sphere in pixel coordinates.
    scale: tuple of float
        Scaling along the dimensions of the underlying data.

    """
    _log.debug('Calling __init__')
    if center is None:
        center = tuple([d/2 for d in dim])
    if radius is None:
        radius = np.max(dim) / 4
    assert len(dim) == len(center), 'Parameters dim and center must have the same dimensions!'
    assert radius > 0, 'Radius has to be a positive scalar value!'
    coords = np.indices(dim) + 0.5  # 0.5 to get to pixel/voxel center!
    coords = coords - np.asarray(center)[(slice(None),) + (None,)*len(dim)]  # [:, None, None, None]
    distance = np.sqrt([coords[i]**2 for i in range(len(dim))])
    data = np.where(distance <= radius, 1, 0)
    return Field(data=data, scale=scale, vector=False)


def create_shape_filament(dim, pos=None, axis=0, scale=1):
    """Creates a Field object with the shape of a filament in arbitrary dimension.

    Parameters
    ----------
    dim : tuple
        The dimensions of the grid.
    pos : tuple, optional
        The position of the filament in pixel coordinates. Has to be a tuple of len(dim) - 1 and denotes the
        index positions along all axes aside from the specified `axis` along which the filament is placed.
    axis :  int, optional
        The orientation of the filament axis. Defaults to the first axis.
    scale: tuple of float
        Scaling along the dimensions of the underlying data.

    """
    _log.debug('Calling __init__')
    assert len(dim) > 1, 'Only usable for multidimensional Fields (at least 2 dimensions)!'
    if pos is None:
        pos = tuple([d/2 for d in dim])
    assert len(dim) == len(pos)-1, 'Position has to specify one less coordinates than dimensions!'
    data = np.zeros(dim)
    index = list(pos)
    index.insert(axis, slice(None))  # [:] for the filament axis! pos everywhere else!
    data[tuple(index)] = 1
    return Field(data=data, scale=scale, vector=False)


def create_shape_voxel(dim, pos=None, scale=1):
    """Creates a Field object with the shape of a single voxel in arbitrary dimension.

    Parameters
    ----------
    dim : tuple
        The dimensions of the grid.
    pos : tuple, optional
        The position of the voxel.
    scale: tuple of float
        Scaling along the dimensions of the underlying data.

    """
    _log.debug('Calling __init__')
    assert len(dim) > 1, 'Only usable for multidimensional Fields (at least 2 dimensions)!'
    if pos is None:
        pos = tuple([d/2 for d in dim])
    assert len(dim) == len(pos), 'Parameters dim and pos must have the same dimensions!'
    data = np.zeros(dim)
    data[pos] = 1
    return Field(data=data, scale=scale, vector=False)

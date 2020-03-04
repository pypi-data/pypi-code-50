# -*- coding: utf-8 -*-
# Copyright 2016 by Forschungszentrum Juelich GmbH
# Author: J. Caron
#


import logging
from numbers import Number

import numpy as np

from .field import Field


__all__ = ['create_vector_homog', 'create_vector_vortex', 'create_vector_skyrmion', 'create_vector_singularity']

_log = logging.getLogger(__name__)


def create_vector_homog(dim, phi=0, theta=None, scale=1):
    """Field subclass implementing a homogeneous vector field with 3 components in 2 or 3 dimensions.

    Attributes
    ----------
    dim : tuple
        The dimensions of the grid.
    phi : float
        The azimuthal angle. The default is 0, i.e., the vectors point in x direction.
    theta : float, optional
        The polar angle. If None (default), only two components will be created (corresponds to pi/2 in 3D, i.e., the
        vectors are in the xy plane).
    scale: tuple of float
        Scaling along the dimensions of the underlying data.

    """
    _log.debug('Calling __init__')
    assert len(dim) in (2, 3), 'Disc can only be build in 2 or 3 dimensions!'
    assert isinstance(phi, Number), 'phi has to be an angle in radians!'
    assert isinstance(theta, Number) or theta is None, 'theta has to be an angle in radians or None!'
    if theta is None:
        y_comp = np.ones(dim) * np.sin(phi)
        x_comp = np.ones(dim) * np.cos(phi)
        data = np.stack([x_comp, y_comp], axis=-1)
    else:
        z_comp = np.ones(dim) * np.cos(theta)
        y_comp = np.ones(dim) * np.sin(theta) * np.sin(phi)
        x_comp = np.ones(dim) * np.sin(theta) * np.cos(phi)
        data = np.stack([x_comp, y_comp, z_comp], axis=-1)
    return Field(data=data, scale=scale, vector=True)


def create_vector_vortex(dim, center=None, core_r=0, oop_r=None, axis=0, scale=1):
    # TODO: oop and core_r documentation!!! General description!
    # TODO: CHIRALITY
    """Field subclass implementing a vortex vector field with 3 components in 2 or 3 dimensions.

    Attributes
    ----------
    dim : tuple
        The dimensions of the grid.
    center : tuple (N=2 or N=3), optional
        The vortex center, given in 2D `(v, u)` or 3D `(z, y, x)`, where the perpendicular axis is discarded
        (determined by the `axis` parameter). Is set to the center of the field of view if not specified.
        The vortex center should be between two pixels to avoid singularities.
    axis :  int, optional
        The orientation of the vortex axis. The default is 0 and corresponds to the z-axis. Is ignored if dim is
        only 2D. To invert chirality, multiply the resulting Field object by -1.  # TODO: WRONG?

    """
    _log.debug('Calling create_vector_vortex')
    assert len(dim) in (2, 3), 'Vortex can only be build in 2 or 3 dimensions!'
    # Find indices of the vortex plane axes:
    idx_uv = [0, 1, 2]
    if len(dim) == 3:  # 3D:
        idx_uv.remove(axis)
    else:  # 2D:
        idx_uv.remove(2)
    # 2D dimensions:
    dim_uv = tuple([dim[i] for i in idx_uv])
    # Find default values:
    if center is None:
        center = tuple([dim[i] / 2 for i in idx_uv])
    elif len(center) == 3:  # if a 3D-center is given, just take the relevant coordinates:
        center = list(center)
        del center[axis]
        center = tuple(center)
    # Create vortex plane (2D):
    coords_uv = np.indices(dim_uv) + 0.5  # 0.5 to get to pixel/voxel center!
    coords_uv = coords_uv - np.asarray(center, dtype=float)[:, None, None]  # Shift by center!
    phi = np.arctan2(coords_uv[0], coords_uv[1]) - np.pi / 2
    rr = np.hypot(coords_uv[0], coords_uv[1])
    rr_clip = np.clip(rr - core_r, a_min=0, a_max=None)  # negative inside core_r (clipped to 0), positive outside!
    if oop_r is None:
        w_comp = np.zeros(dim_uv)
    else:
        w_comp = 1 - 2/np.pi * np.arcsin(np.tanh(np.pi*rr_clip/oop_r))  # orthogonal: 1 inside, towards 0 outside!
    v_comp = np.ones(dim_uv) * np.sin(phi) * np.sqrt(1 - w_comp)
    u_comp = np.ones(dim_uv) * np.cos(phi) * np.sqrt(1 - w_comp)
    if len(dim) == 3:  # Expand to 3D:
        w_comp = np.expand_dims(w_comp, axis=axis)
        v_comp = np.expand_dims(v_comp, axis=axis)
        u_comp = np.expand_dims(u_comp, axis=axis)
        reps = [1, 1, 1]  # repetitions for tiling
        reps[axis] = dim[axis]  # repeat along chosen axis
        w_comp = np.tile(w_comp, reps)
        v_comp = np.tile(v_comp, reps)
        u_comp = np.tile(u_comp, reps)
    if axis == 0:  # z-axis
        z_comp = w_comp
        y_comp = -v_comp
        x_comp = -u_comp
    elif axis == 1:  # y-axis
        z_comp = v_comp
        y_comp = w_comp
        x_comp = u_comp
    elif axis == 2:  # x-axis
        z_comp = -v_comp
        y_comp = -u_comp
        x_comp = w_comp
    else:
        raise ValueError(f'{axis} is not a valid argument for axis (has to be 0, 1 or 2)')
    data = np.stack([x_comp, y_comp, z_comp], axis=-1)
    return Field(data=data, scale=scale, vector=True)


def create_vector_skyrmion(dim, center=None, phi_0=0, skyrm_d=None, wall_d=None, axis=0, scale=1):
    """Create a 3-dimensional magnetic Bloch or Neel type skyrmion distribution.

    Parameters
    ----------
    dim : tuple
        The dimensions of the grid.
    center : tuple (N=2 or N=3), optional
        The source center, given in 2D `(v, u)` or 3D `(z, y, x)`, where the perpendicular axis
        is discarded. Is set to the center of the field of view if not specified.
        The center has to be between two pixels.
    phi_0 : float, optional
        Angular offset switching between Neel type (0 [default] or pi) or Bloch type (+/- pi/2)
        skyrmions.
    skyrm_d : float, optional
        Diameter of the skyrmion. Defaults to half of the smaller dimension perpendicular to the
        skyrmion axis if not specified.
    wall_d : float, optional
        Diameter of the domain wall of the skyrmion. Defaults to `skyrm_d / 4` if not specified.
    axis :  {'z', '-z', 'y', '-y', 'x', '-x'}, optional # TODO: NUMBERS!! See vortex
        The orientation of the skyrmion axis. The default is 'z'. Negative values invert skyrmion
        core direction.

    Returns
    -------
    amplitude : tuple (N=3) of :class:`~numpy.ndarray` (N=3)
        The magnetic distribution as a tuple of the 3 components in
        `x`-, `y`- and `z`-direction on the 3-dimensional grid.

    Notes
    -----
        To avoid singularities, the source center should lie between the pixel centers (which
        reside at coordinates with _.5 at the end), i.e. integer values should be used as center
        coordinates (e.g. coordinate 1 lies between the first and the second pixel).

        Skyrmion wall width is dependant on exchange stiffness  A [J/m] and anisotropy K [J/m³]
        The out-of-plane magnetization at the domain wall can be described as:
        Mz = -Ms * tanh(x/w)  # TODO: Instead ROMER paper
        w = sqrt(A/K)

    """

    def _theta(r):
        theta_1 = + np.arcsin(np.tanh((r + skyrm_d/2)/(wall_d/2)))
        theta_2 = - np.arcsin(np.tanh((r - skyrm_d/2)/(wall_d/2)))
        theta = theta_1 + theta_2
        theta /= np.abs(theta).max() / np.pi
        return theta

    _log.debug('Calling create_vector_skyrmion')
    assert len(dim) in (2, 3), 'Skyrmion can only be build in 2 or 3 dimensions!'
    # Find indices of the skyrmion plane axes:
    idx_uv = [0, 1, 2]
    if len(dim) == 3:  # 3D:
        idx_uv.remove(axis)
    else:  # 2D:
        idx_uv.remove(2)
    # 2D dimensions:
    dim_uv = tuple([dim[i] for i in idx_uv])
    # Find default values:
    if skyrm_d is None:
        skyrm_d = np.min(dim_uv) / 2
    if wall_d is None:
        wall_d = skyrm_d / 4
    if center is None:
        center = tuple([dim[i] / 2 for i in idx_uv])
    elif len(center) == 3:  # if a 3D-center is given, just take the relevant coordinates:
        center = list(center)
        del center[axis]
        center = tuple(center)
    # Create skyrmion plane (2D):
    coords_uv = np.indices(dim_uv) + 0.5  # 0.5 to get to pixel/voxel center!
    coords_uv = coords_uv - np.asarray(center, dtype=float)[:, None, None]  # Shift by center!
    rr = np.hypot(coords_uv[0], coords_uv[1])
    phi = np.arctan2(coords_uv[0], coords_uv[1]) - phi_0
    theta = _theta(rr)
    w_comp = np.cos(theta)
    v_comp = np.sin(theta) * np.sin(phi)
    u_comp = np.sin(theta) * np.cos(phi)
    # Expansion to 3D if necessary and component shuffling:
    if len(dim) == 3:  # Expand to 3D:
        w_comp = np.expand_dims(w_comp, axis=axis)
        v_comp = np.expand_dims(v_comp, axis=axis)
        u_comp = np.expand_dims(u_comp, axis=axis)
        reps = [1, 1, 1]  # repetitions for tiling
        reps[axis] = dim[axis]  # repeat along chosen axis
        w_comp = np.tile(w_comp, reps)
        v_comp = np.tile(v_comp, reps)
        u_comp = np.tile(u_comp, reps)
    if axis == 0:  # z-axis
        z_comp = w_comp
        y_comp = -v_comp
        x_comp = -u_comp
    elif axis == 1:  # y-axis
        z_comp = v_comp
        y_comp = w_comp
        x_comp = u_comp
    elif axis == 2:  # x-axis
        z_comp = -v_comp
        y_comp = -u_comp
        x_comp = w_comp
    else:
        raise ValueError(f'{axis} is not a valid argument for axis (has to be 0, 1 or 2)')
    data = np.stack([x_comp, y_comp, z_comp], axis=-1)
    return Field(data=data, scale=scale, vector=True)


def create_vector_singularity(dim, center=None, scale=1):
    """Create a 3-dimensional magnetic distribution of a homogeneous magnetized object.

    Parameters
    ----------
    dim : tuple
        The dimensions of the grid.
    center : tuple (N=2 or N=3), optional
        The source center, given in 2D `(v, u)` or 3D `(z, y, x)`, where the perpendicular axis
        is discarded. Is set to the center of the field of view if not specified.
        The source center has to be between two pixels.
    axis :  {'z', '-z', 'y', '-y', 'x', '-x'}, optional  # TODO: NUMBERS!
        The orientation of the source axis. The default is 'z'. Negative values invert the source
        to a sink.  # TODO: wat...?
    # TODO: scale!

    Returns
    -------
    amplitude : tuple (N=3) of :class:`~numpy.ndarray` (N=3)
        The magnetic distribution as a tuple of the 3 components in
        `x`-, `y`- and `z`-direction on the 3-dimensional grid.

    Notes
    -----
        To avoid singularities, the source center should lie between the pixel centers (which
        reside at coordinates with _.5 at the end), i.e. integer values should be used as center
        coordinates (e.g. coordinate 1 lies between the first and the second pixel).

    """  # TODO: What does negating do here? Senke / Quelle (YES IT DOES!)? swell and sink? ISSUE! INVITE PEOPLE!!!
    _log.debug('Calling create_vector_singularity')
    # Find default values:
    if center is None:
        center = tuple([d / 2 for d in dim])
    assert len(dim) == len(center), f"Length of dim ({len(dim)}) and center ({len(center)}) don't match!"
    # Setup coordinates, shape is (c, z, y, x), if 3D, or (c, y, x), if 2D (c: components):
    coords = np.indices(dim) + 0.5  # 0.5 to get to pixel/voxel center!
    center = np.asarray(center, dtype=float)
    bc_shape = (len(dim,),) + (1,)*len(dim)  # Shape for broadcasting, (1,1,1,3) for 3D, (1,1,2) for 2D!
    coords = coords - center.reshape(bc_shape)  # Shift by center (append 1s for broadcasting)!
    rr = np.sqrt(np.sum([coords[i]**2 for i in range(len(dim))], axis=0))
    data = coords / (rr + 1E-30)  # Normalise amplitude (keep direction), rr (z,y,x) is broadcasted to data (c,z,y,x)!
    data = data.T  # (c,z,y,x) -> (x,y,z,c)
    return Field(data=data, scale=scale, vector=True)

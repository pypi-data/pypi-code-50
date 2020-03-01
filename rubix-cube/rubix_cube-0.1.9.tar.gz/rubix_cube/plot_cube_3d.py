# -*- coding: utf-8 -*-
"""3-D Rubix :class:`Rubix Cube <rubix_cube.cube.Cube>` plot rendering Module.

Module Description
==================

    *   :func:`plot_cube_3D` method for plotting the 
        :class:`Rubix Cube <rubix_cube.cube.Cube>` on a 
        :class:`matplotlib Axes <matplotlib.axes.Axes>`.

Module Contents
===============

.. moduleauthor:: David Grethlein <djg329@drexel.edu>

"""

import os
import sys
import json

import warnings

from typing import List, Tuple, Dict

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

from matplotlib.axes import Axes
from mpl_toolkits.mplot3d import Axes3D

from itertools import product, combinations

from .cube import Cube


def is_3d_axes(ax : plt.Axes) -> bool:
    """Simply checks if the current object being examined is an instance of the
    :class:`matplotlib Axes <matplotlib.axes.Axes>` parameterized to be a 3-D
    plotting
    
    Args:
        ax (plt.Axes): Object to be tested if it is a 
            :class:`plt.Axes <matplotlib.axes.Axes>`
    
    Return:
        ``True`` if object is an instance of 
        :class:`matplotlib Axes <matplotlib.axes.Axes>` initialized to be a
        3-D projection. ``False`` otherwise.

        .. code-block::
           :name: is_3d_axes
           :linenos:
           :caption: Tests if the given object ``ax`` is a 3-D projection
                or not.

           if isinstance(ax, plt.Axes)
           and ax.name == '3d':
               return True
           else:
               return False

    """

    if isinstance(ax, plt.Axes)\
    and ax.name == '3d':
        return True
    else:
        return False


def plot_cube_3D(ax : plt.Axes , cube : Cube):
    """Plots the :class:`Rubix Cube <rubix_cube.cube.Cube>` on an interactive
    3-D :class:`matplotlib Axes <matplotlib.axes.Axes>` with non-visible faces
    from the current orientation being displayed in visible reflections.
    
    Args:
        ax (plt.Axes): The :class:`matplotlib Axes <matplotlib.axes.Axes>`
            on which the plotting will be done.
        cube (Cube): :class:`Rubix Cube <rubix_cube.cube.Cube>` that will be 
            plotted in a 3-D projection.
    
    """

    # Ensures arguments are valid
    if is_3d_axes(ax)\
    and isinstance(cube , Cube)\
    and cube.is_well_formed():

        # draw cube
        r = [-1, 1]
        for s, e in combinations(np.array(list(product(r, r, r))), 2):
            if np.sum(np.abs(s-e)) == r[1]-r[0]:
                ax.plot3D(*zip(s, e), color="b")






# -*- coding: utf-8 -*-
"""2-D :class:`Rubix Cube <Cube>` plot rendering Module.

Module Description
==================

    *   :func:`plot_cube_2D` method for plotting the :class:`Rubix Cube <Cube>`
        on a :class:`matplotlib Axes <matplotlib.axes.Axes>`.

        .. figure:: ./../../misc/plot_cube_2D.png
           :name: plot_cube_2d_img
           :align: center
           :width: 75%
           
           All 6 faces of the :class:`Rubix Cube <Cube>` are visible in this 2D
           rendering.

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

from .cube import Cube


FACE_COORDS = {'FRONT_FACE' : (-150,50),
               'LEFT_FACE'  : (-450,50),
               'RIGHT_FACE' : (150,50),
               'BACK_FACE'  : (450,50),
               'UP_FACE'    : (-150,350),
               'DOWN_FACE'  : (-150,-250)}


def plot_cube_2D(ax : plt.Axes , cube : Cube):
    """Plots the :class:`Rubix Cube <Cube>` on a 
    :class:`matplotlib Axes <matplotlib.axes.Axes>` on a flattened 2-D
    representation.

    Args:
        ax (plt.Axes): The :class:`matplotlib Axes <matplotlib.axes.Axes>`
            on which the plotting will be done.
        cube (Cube): :class:`Rubix Cube <Cube>` that will be plotted in a
            flattened 2-D representation of all 6 sides.

    Returns:
        None.

    """

    # Ensures the arguments are well-formed.
    if cube.is_well_formed()\
    and isinstance(ax , plt.Axes):

        for face_name in cube.faces:

            # Grabs the local coordinates for each face
            face_local_coords = FACE_COORDS[face_name]

            # Grabs the face values for filling in the plot for each tile
            # in the 2-D representation.
            face_values = cube.faces[face_name]

            #print(f"{face_name} : ")

            for row_idx , row in enumerate(face_values):

                for col_idx , color_val in enumerate(row):

                    tile_coords = (face_local_coords[0] + 100*col_idx,
                                   face_local_coords[1] - 100*row_idx)

                    #print(f"\t[{row_idx},{col_idx}] : {tile_coords}")

                    rect = patches.Rectangle(xy=tile_coords,
                                             width=100,
                                             height=100,
                                             facecolor=color_val,
                                             lw=2,
                                             edgecolor='black')

                    ax.add_patch(rect)




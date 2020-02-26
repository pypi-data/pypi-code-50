# -*- coding: utf-8 -*-
"""
| ----------------------------------------------------------------------------------------------------------------------
| Date                : September 2018
| Copyright           : (C) 2018 by Ann Crabbé (KU Leuven)
| Email               : ann.crabbe@kuleuven.be
| Acknowledgements    : Translated from VIPER Tools 2.0 (UC Santa Barbara, VIPER Lab).
|                       Dar Roberts, Kerry Halligan, Philip Dennison, Kenneth Dudley, Ben Somers, Ann Crabbé
|
| This program is free software; you can redistribute it and/or modify it under the terms of the GNU
| General Public License as published by the Free Software Foundation; either version 3 of the
| License, or any later version.
| ----------------------------------------------------------------------------------------------------------------------
"""
import numpy as np


class ShadeNormalisation:
    """
    Do a simple shade normalization on an existing MESMA fraction image: the shade fraction is removed and the other
    fractions are normalized to sum to one.
    """

    def __init__(self):
        pass

    @staticmethod
    def execute(mesma_fraction_image: np.array, shade_band: int = -1) -> np.array:
        """
        Execute shade normalisation. The return value is a normalized fraction image, with one band less as the input.

        :param mesma_fraction_image: Fraction image of the output of the MESMA algorithm.
        :param shade_band: Band number with the shade fraction (set to None in case no shade band given).
        :return: Normalised fraction image.
        """

        n_bands = len(mesma_fraction_image)

        if mesma_fraction_image.ndim <= 2 or n_bands < 3:
            raise Exception('MESMA Fractions Image must have at least 3 bands (i.e. based on at least 3-EM models)')

        non_shade_bands = list(range(n_bands))
        if shade_band is not None:
            non_shade_bands.pop(shade_band)

        with np.errstate(divide='ignore', invalid='ignore'):
            new_fraction_image = mesma_fraction_image[non_shade_bands] / \
                                 np.sum(mesma_fraction_image[non_shade_bands], axis=0)[np.newaxis, :, :]
            new_fraction_image[np.isnan(new_fraction_image)] = 0

        return new_fraction_image


""" MODIFICATION HISTORY:
2005-10 [IDL] Written by Kerry Halligan
2018-09 [Python] Ported to QGIS/Python by Ann Crabbé, incl. significant re-write of code
"""

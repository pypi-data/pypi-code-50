# -*- coding: utf-8 -*-
"""
| ----------------------------------------------------------------------------------------------------------------------
| Date                : February 2019
| Copyright           : (C) 2018 by Ann Crabbé (KU Leuven)
| Email               : ann.crabbe@kuleuven.be
|
| This program is free software; you can redistribute it and/or modify it under the terms of the GNU
| General Public License as published by the Free Software Foundation; either version 3 of the
| License, or any later version.
| ----------------------------------------------------------------------------------------------------------------------
"""
import numpy as np
from mesma.scripts.shade_normalisation import ShadeNormalisation


class HardClassification:
    """
    Do a simple hard classification on an existing MESMA fraction image.
    """

    def __init__(self):
        pass

    @staticmethod
    def execute(mesma_fraction_image: np.array, shade_band: int = -1) -> np.array:
        """
        Execute the hard classification. The return value single band image indicating the dominant class.

        :param mesma_fraction_image: Fraction image of the output of the MESMA algorithm.
        :param shade_band: Band number with the shade fraction (set to None in case no shade band given).
        :return: Hard classified image with values reflecting the dominant band.
        """

        normalized_image = ShadeNormalisation().execute(mesma_fraction_image, shade_band)
        classified_image = np.int16(np.argmax(normalized_image, axis=0))
        return classified_image


""" MODIFICATION HISTORY:
2005-10 [IDL] Written by Kerry Halligan
2018-09 [Python] Ported to QGIS/Python by Ann Crabbé, incl. significant re-write of code
"""

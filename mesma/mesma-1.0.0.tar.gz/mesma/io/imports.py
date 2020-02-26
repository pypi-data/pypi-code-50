# -*- coding: utf-8 -*-
"""
| ----------------------------------------------------------------------------------------------------------------------
| Date                : July 2018
| Copyright           : (C) 2018 by Ann Crabbé (KU Leuven)
| Email               : ann.crabbe@kuleuven.be
|
| This program is free software; you can redistribute it and/or modify it under the terms of the GNU
| General Public License as published by the Free Software Foundation; either version 3 of the
| License, or any later version.
| ----------------------------------------------------------------------------------------------------------------------
"""
import numpy as np
from osgeo import gdal
from mesma.io import check_path
from mesma.sitepackages.qps.speclib.spectrallibraries import SpectralLibrary


def import_library(path):
    """ Browse for a spectral library and return it along the list of spectra names from the header.
    :param str path: the absolute path to the spectral library
    :return: float32 numpy array [#good bands x #spectra] + string array with spectra names [#spectra]
    """
    check_path(path)
    spectral_library = SpectralLibrary.readFrom(path)

    if not spectral_library or len(spectral_library) == 0:
        raise Exception("Spectral Library with path {} is empty.".format(path))

    return spectral_library


def import_image(path):
    """ Browse for a spectral image and return it without bad bands.
    :param path: the absolute path to the image
    :return: float32 numpy array [#good bands x #rows x #columns]
    """
    check_path(path)

    gdal.UseExceptions()
    try:
        data = gdal.Open(path)
        array = data.ReadAsArray()
        gbl = data.GetMetadataItem('bbl', 'ENVI')
        if gbl is not None:
            gbl = np.asarray(gbl[1:-1].split(","), dtype=int)
            gbl = np.where(gbl == 1)[0]
            array = array[gbl, :, :]
    except Exception as e:
        raise Exception(str(e))

    if array is None or len(array) == 0:
        raise Exception("Image with path {} is empty.".format(path))

    return array


def import_band_names(path):
    """ Browse for the spectral image's band names and return them as a list.
    :param path: the absolute path to the spectral library
    :return: string list of band names
    """
    check_path(path)

    gdal.UseExceptions()
    try:
        data = gdal.Open(path)
        band_names = data.GetMetadataItem('band_names', 'ENVI')
        if band_names:
            band_names = band_names[1:-1].split(",")
            band_names = [x.strip().lower() for x in band_names]
        else:
            raise Exception("The image has no band names. This is not a MESMA Fractions image.")

    except Exception as e:
        raise Exception(str(e))

    try:
        shade_band_index = band_names.index("shade_fraction")
    except ValueError:
        shade_band_index = None

    return band_names, shade_band_index


def detect_reflectance_scale_factor(array):
    """ Determine the reflectance scale factor [1, 1000 or 10 000] by looking for the largest value in the array.
    :param array: the array for which the reflectance scale factor is to be found
    :return: the reflectance scale factor [int]
    """
    limit = np.nanmax(array)
    if limit < 1:
        return 1
    if limit < 1000:
        return 1000
    if limit < 10000:
        return 10000
    else:
        raise ValueError("Image has values larger than 10000. Cannot process.")

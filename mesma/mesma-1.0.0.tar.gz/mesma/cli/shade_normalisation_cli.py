# -*- coding: utf-8 -*-
"""
| ----------------------------------------------------------------------------------------------------------------------
| Shade Normalisation Command Line Interface. Available when installing viper with pip. Type 'viper-shade -h' for help.
|
| Date                : February 2019
| Copyright           : (C) 2018 by Ann Crabbé (KU Leuven)
| Email               : ann.crabbe@kuleuven.be
|
| This program is free software; you can redistribute it and/or modify it under the terms of the GNU
| General Public License as published by the Free Software Foundation; either version 3 of the
| License, or any later version.
| ----------------------------------------------------------------------------------------------------------------------
"""
import os
import argparse
from mesma.scripts.shade_normalisation import ShadeNormalisation
from mesma.io.imports import import_band_names
from mesma.io.operators import ShadeNormalisationOperator, CLIProgressBar
from mesma.sitepackages.hubdc.applier import Applier, ApplierInputRaster, ApplierOutputRaster


def create_parser():
    """ The parser for the CLI command parameters. """
    parser = argparse.ArgumentParser(description=str(ShadeNormalisation.__doc__))

    # image
    parser.add_argument('image', metavar='fraction image',
                        help='the mesma output image ending on _fractions')

    # output
    parser.add_argument('-o', '--output', metavar='\b',
                        help="output image file (default: in same folder with extension '_normalized')")

    return parser


def run_shade_normalisation(args):
    """
    Documentation: viper-shade -h
    """

    # Shade band present?
    band_names, shade_band_index = import_band_names(args.image)

    if not shade_band_index:
        print("No band found with the name 'shade_fraction'. Already normalized or not a MESMA Fractions image.")
        return

    # Get output name
    if args.output is None:
        basename, extension = os.path.splitext(args.image)
        output = basename + '_normalised' + extension
    else:
        output = args.output

    # set up the applier
    applier = Applier()
    applier.controls.setProgressBar(CLIProgressBar())
    applier.inputRaster.setRaster(key='raster', value=ApplierInputRaster(filename=args.image))
    applier.outputRaster.setRaster(key='fractions', value=ApplierOutputRaster(filename=output))

    # apply shade normalisation
    applier.apply(operatorType=ShadeNormalisationOperator, band_names=band_names, shade_band=shade_band_index)


def main():
    """ Function called by CLI. """
    parser = create_parser()
    run_shade_normalisation(parser.parse_args())

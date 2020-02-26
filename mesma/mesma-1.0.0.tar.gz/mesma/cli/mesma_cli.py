# -*- coding: utf-8 -*-
"""
| ----------------------------------------------------------------------------------------------------------------------
| MESMA Command Line Interface. Available when installing viper with pip. Type 'viper-mesma -h' for help.
|
| Date                : September 2018
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
import numpy as np
import time
import datetime
from mesma.scripts.mesma import MesmaCore, MesmaModels
from mesma.io.imports import import_library, detect_reflectance_scale_factor, import_image
from mesma.io.operators import MesmaOperator, CLIProgressBar
from mesma.sitepackages.hubdc.applier import Applier, ApplierInputRaster, ApplierOutputRaster


def create_parser():
    """ The parser for the CLI command parameters. """
    parser = argparse.ArgumentParser(description=str(MesmaCore.__doc__))

    # library
    parser.add_argument('library', metavar='library',
                        help='spectral library file')
    parser.add_argument('class_name', metavar='class',
                        help='metadata header with the spectrum classes')
    parser.add_argument('-l', '--complexity-level', metavar='\b', nargs='+', type=int, default=[2, 3],
                        help='the complexity levels for unmixing. e.g. 2 3 4 for 2-, 3- and 4-EM models (default: 2 3)')
    parser.add_argument('-r', '--reflectance-scale-library', metavar='\b', type=int,
                        help='library reflectance scale factor (default: derived from data as 1, 1 000 or 10 000)')
    parser.add_argument('-f', '--fusion-threshold', metavar='\b', type=float, default=0.007,
                        help='Models with a higher number of classes (e.g. 4-EM vs. 3-EM models) are only chosen when '
                             'the decrease in RMSE is larger than this threshold (default: 0.007)')

    # constraints
    parser.add_argument('-u', '--unconstrained', action='store_true', default=False,
                        help='run mesma without constraints (default off)')
    parser.add_argument('--min-fraction', metavar='\b', type=float, default=-0.05,
                        help='minimum allowable endmember fraction (default -0.05), use -9999 to set no constraint')
    parser.add_argument('--max-fraction', metavar='\b', type=float, default=1.05,
                        help='maximum allowable endmember fraction (default 1.05), use -9999 to set no constraint')
    parser.add_argument('--min-shade-fraction', metavar='\b', type=float, default=0.00,
                        help='minimum allowable shade fraction (default 0.00), use -9999 to set no constraint')
    parser.add_argument('--max-shade-fraction', metavar='\b', type=float, default=0.80,
                        help='maximum allowable shade fraction (default 0.80), use -9999 to set no constraint')
    parser.add_argument('--max-rmse', metavar='\b', type=float, default=0.025,
                        help='maximum allowable RMSE (default 0.025), use -9999 to set no constraint')
    parser.add_argument('--residual-constraint', action='store_true', default=False,
                        help='use a residual constraint (default off)')
    parser.add_argument('--residual-constraint-values', metavar='\b', type=float, nargs="+", default=(0.025, 7),
                        help='two values (residual threshold, number of bands): the number of consecutive bands that '
                             'the residual values are allowed to exceed the given threshold (default: 0.025 7)')

    # image
    parser.add_argument('image', metavar='image',
                        help='image file (singular)')
    parser.add_argument('-s', '--reflectance-scale-image', metavar='\b', type=int,
                        help='image reflectance scale factor (default: derived from data as 1, 1 000 or 10 000)')

    # non-photometric shade
    parser.add_argument('-a', '--shade', metavar='\b',
                        help='non-photometric shade, saved as library file with one spectrum')
    parser.add_argument('-t', '--reflectance-scale-shade', metavar='\b', type=int,
                        help='shade reflectance scale factor (default: derived from data as 1, 1 000 or 10 000)')

    # output
    parser.add_argument('-o', '--output', metavar='\b',
                        help="output image file (default: in same folder as image with extension '_mesma_datetime'")
    parser.add_argument('-d', '--residuals-image', action='store_true', default=False,
                        help='create a residual image as output (default off)')

    # advanced algorithms
    parser.add_argument('--spectral-weighing', action='store_true', default=False,
                        help='use spectral weighing algorithm (default off)')
    parser.add_argument('--band-selection', action='store_true', default=False,
                        help='use band selection algorithm (default off)')
    parser.add_argument('--band-selection-values', metavar='\b', type=float, nargs="+", default=(0.99, 0.01),
                        help='two values: correlation threshold and correlation decrease (default: 0.99 0.01)')

    return parser


def run_mesma(args):
    """
    Documentation: viper-mesma -h
    """

    # MESMA timestamp
    timestamp = datetime.datetime.fromtimestamp(time.time())

    # browse for the library
    spectral_library = import_library(args.library)

    if spectral_library is None or spectral_library.featureCount() == 0:
        return

    library = np.array([np.array(x.values()['y'])[np.where(x.bbl())[0]] for x in spectral_library.profiles()]).T

    # divide the library by the reflectance scale
    if args.reflectance_scale_library:
        library = library / args.reflectance_scale_library
    else:
        scale = detect_reflectance_scale_factor(library)
        library = library / scale
        print('Library reflectance scale factor: ' + str(scale))

    # get class_list
    class_list = np.asarray([x.metadata(args.class_name) for x in spectral_library.profiles()], dtype=str)
    class_list = np.asarray([x.lower() for x in class_list])
    unique_classes = np.unique(class_list)
    n_classes = len(unique_classes)

    # get complexity level and create models
    if max(args.complexity_level) > n_classes + 1 or min(args.complexity_level) < 2:
        print("Complexity level(s) should be between 2 and '" + str(n_classes) + ".")
        return

    models_object = MesmaModels()
    models_object.setup(class_list)
    if 2 not in args.complexity_level:
        models_object.select_level(state=False, level=2)
    else:
        args.complexity_level.remove(2)
    if 3 not in args.complexity_level:
        models_object.select_level(state=False, level=3)
    else:
        args.complexity_level.remove(3)
    for level in args.complexity_level:
        models_object.select_level(state=True, level=level)
        for i in np.arange(n_classes):
            models_object.select_class(state=True, index=i, level=level)
    print("Total number of models: " + str(models_object.total()))

    # get image
    image = import_image(args.image)  # check image is readable
    if args.reflectance_scale_image is None:
        reflectance_scale_image = detect_reflectance_scale_factor(image)
        print('Image reflectance scale factor: ' + str(reflectance_scale_image))
    else:
        reflectance_scale_image = args.reflectance_scale_image
    n_bands = image.shape[0]

    if n_bands != library.shape[0]:
        print('The image and library have different number of bands. MESMA not possible.')
        return

    # set default output name(s)
    if args.output is None:
        dt_string = timestamp.strftime('%Y%m%dT%H%M%S')
        path_no_extension = os.path.splitext(args.image)[0]
        output = path_no_extension + '_mesma_' + dt_string
    else:
        output = args.output

    # non-photometric shade
    if args.shade is not None:
        shade_library = import_library(args.shade)

        if shade_library.featureCount() != 1:
            print("Library not readable or has more than one spectrum.")
            return

        shade = np.array([np.array(x.values()['y'])[np.where(x.bbl())[0]] for x in shade_library.profiles()]).T

        if shade.size != 0 and shade.shape[0] != library.shape[0]:
            print('The library and shade spectrum have different number of bands. MESMA not possible.')
            return

        # divide the shade by the reflectance scale
        if args.reflectance_scale_shade:
            shade = shade / args.reflectance_scale_shade
        else:
            scale = detect_reflectance_scale_factor(shade)
            shade = shade / scale
            print('Shade reflectance scale factor: ' + str(scale))
    else:
        shade = None

    # band selection/spectral weighing cannot be combined with a residuals image or residual constraint
    if args.spectral_weighing and args.residual_constraint:
        print('Spectral Weighing cannot be combined with a constraint on the residuals. Residual constraint ignored.')
        residual_constraint = False
    elif args.band_selection and args.residual_constraint:
        print('Band Selection cannot be combined with a constraint on the residuals. Residual constraint ignored.')
        residual_constraint = False
    elif args.residual_constraint:
        residual_constraint = True
    else:
        residual_constraint = False

    if args.spectral_weighing and args.residuals_image:
        print('Spectral Weighing cannot be combined with a residuals output image. Residual image ignored.')
        residual_image = False
    elif args.band_selection and args.residuals_image:
        print('Band Selection cannot be combined with a residuals output image. Residual image ignored.')
        residual_image = False
    elif args.residuals_image:
        residual_image = True
    else:
        residual_image = False

    # get the constraints
    if args.unconstrained:
        constraints = (-9999, -9999, -9999, -9999, -9999, -9999, -9999)
    elif residual_constraint is False:
        constraints = (args.min_fraction, args.max_fraction, args.min_shade_fraction, args.max_shade_fraction,
                       args.max_rmse, -9999, -9999)
    else:
        if args.residual_constraint_values[1] > n_bands:
            print("The number of bands specified for the residual constraint cannot exceed the number of bands in the "
                  "image (" + str(n_bands) + "). You specified: " + str(args.residual_constraint_values[1]))
            return
        else:
            constraints = (args.min_fraction, args.max_fraction, args.min_shade_fraction, args.max_shade_fraction,
                           args.max_rmse, args.residual_constraint_values[0], args.residual_constraint_values[1])

    # set up applier
    applier = Applier()
    applier.controls.setProgressBar(CLIProgressBar())
    applier.inputRaster.setRaster(key='raster', value=ApplierInputRaster(filename=args.image))
    applier.outputRaster.setRaster(key='models', value=ApplierOutputRaster(filename=output))
    applier.outputRaster.setRaster(key='fractions', value=ApplierOutputRaster(filename=output + '_fractions'))
    applier.outputRaster.setRaster(key='rmse', value=ApplierOutputRaster(filename=output + '_rmse'))

    if residual_image:
        applier.outputRaster.setRaster(key='residuals', value=ApplierOutputRaster(filename=output + '_residuals'))

    # apply MESMA
    applier.apply(operatorType=MesmaOperator,
                  image_scale=reflectance_scale_image,
                  library=library,
                  look_up_table=models_object.return_look_up_table(),
                  em_per_class=models_object.em_per_class,
                  unique_classes=models_object.unique_classes,
                  constraints=constraints,
                  shade_spectrum=shade,
                  fusion_value=args.fusion_threshold,
                  use_band_weighing=args.spectral_weighing,
                  use_band_selection=args.band_selection,
                  bands_selection_values=tuple(args.band_selection_values),
                  lib_name=os.path.basename(args.library),
                  residual_image=residual_image)


def main():
    """ Function called by CLI. """
    parser = create_parser()
    run_mesma(parser.parse_args())

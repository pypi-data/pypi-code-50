# -*- coding: utf-8 -*-
"""
| ----------------------------------------------------------------------------------------------------------------------
| Ear-Masa-Cob Command Line Interface. Available when installing viper with pip. Type 'viper-emc -h' for help.
|
| Date                : August 2018
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
import os
import argparse
import numpy as np
import time
from spectral_libraries.scripts.ear_masa_cob import EarMasaCob
from spectral_libraries.scripts.square_array import SquareArray
from spectral_libraries.io import imports, exports
from qgis.core import QgsField
from qgis.PyQt.QtCore import QVariant


def create_parser():
    """ The parser for the CLI command parameters. """
    parser = argparse.ArgumentParser(description=str(EarMasaCob.__doc__))

    # library
    parser.add_argument('library', metavar='spectral library', help='spectral library input file')
    parser.add_argument('sp_class', metavar='class', help='metadata header with the spectrum classes')
    parser.add_argument('-r', '--reflectance-scale', metavar='\b', type=int,
                        help='in case L: reflectance scale factor (default: derived from data as 1, 1 000 or 10 000)')

    # square array
    parser.add_argument('-q', '--square', metavar='\b', help='square array file')
    parser.add_argument('-s', '--save-square', action='store_true', default=False,
                        help='save the square array as an intermediate result (default: off)')

    # output
    parser.add_argument('-o', '--output', metavar='\b',
                        help="output library (default: same name as input library with suffix '_emc.sli'")

    return parser


def run_emc(args):
    """
    Documentation: viper-emc -h
    """

    library, names, classes = imports.import_library_as_array(args.library, spectra_names=True, metadata=args.sp_class)

    if args.square is None:

        scale = args.reflectance_scale if args.reflectance_scale else imports.detect_reflectance_scale_factor(library)
        library = library / args.reflectance_scale
        print('Reflectance scale factor: ' + str(scale))

        start = time.time()
        square = SquareArray().execute(library=library, out_angle=True)
        duration = np.float16(time.time() - start)

        if args.save_square:
            exports.save_square_to_envi(square, outfile_path=os.path.splitext(args.library)[0] + '_sq.sqr', reset=False,
                                        spectra_names=names, ngb=library.shape[0], duration=duration,
                                        library_name=os.path.basename(args.library), constraints=(-0.05, 1.05, 0.025))

    else:
        square, spectra_names_square = imports.import_square(args.square)

        if not np.array_equal(names, spectra_names_square):
            print("Library and Square Array have a different set of endmembers.")
            return

        # Check a Spectral Angle, RMSE and Constraints band are given
        bands = list(square.keys())
        if 'spectral angle' not in bands:
            print("No 'Spectral Angle' band found in the square array.")
            return
        if 'rmse' not in bands:
            print("No 'RMSE' band found in the square array.")
            return
        if 'constraints' not in bands:
            print("No 'Constraints' band found in the square array")
            return

    # Run ear_masa_cob.py
    result = EarMasaCob().execute(spectral_angle_band=square['spectral angle'], rmse_band=square['rmse'],
                                  constraints_band=square['constraints'], class_list=classes)

    # Output
    if args.output:
        output_file = args.output
    else:
        output_file = os.path.splitext(args.library)[0] + '_emc.sli'

    # append metadata to spectral library
    spectral_library = imports.import_library(args.library)

    spectral_library.startEditing()
    spectral_library.addAttribute(QgsField(name="EAR", type=QVariant.Double))
    spectral_library.addAttribute(QgsField(name="MASA", type=QVariant.Double))
    spectral_library.addAttribute(QgsField(name="InCOB", type=QVariant.Int))
    spectral_library.addAttribute(QgsField(name="OutCOB", type=QVariant.Int))
    spectral_library.addAttribute(QgsField(name="COBI", type=QVariant.Double))
    spectral_library.commitChanges()

    # add extra attribute data
    fields = spectral_library.fields()
    ear_index = fields.indexFromName("EAR")
    masa_index = fields.indexFromName("MASA")
    cob_in_index = fields.indexFromName("InCOB")
    cob_out_index = fields.indexFromName("OutCOB")
    cob_ratio_index = fields.indexFromName("COBI")
    profiles = spectral_library.profiles()
    spectral_library.startEditing()
    for (profile, ear, masa, ci, co, cr) in zip(profiles, result[0], result[1], result[2], result[3], result[4]):
        spectral_library.changeAttributeValue(profile.id(), ear_index, ear)
        spectral_library.changeAttributeValue(profile.id(), masa_index, masa)
        spectral_library.changeAttributeValue(profile.id(), cob_in_index, ci)
        spectral_library.changeAttributeValue(profile.id(), cob_out_index, co)
        spectral_library.changeAttributeValue(profile.id(), cob_ratio_index, cr)

    # Export to new library
    spectral_library.exportProfiles(output_file)


def main():
    """ Function called by CLI. """
    parser = create_parser()
    run_emc(parser.parse_args())


if __name__ == '__main__':
    main()

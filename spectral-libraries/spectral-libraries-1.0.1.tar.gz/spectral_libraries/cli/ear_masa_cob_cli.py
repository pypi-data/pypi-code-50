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
from vipertools.scripts.ear_masa_cob import EarMasaCob
from vipertools.scripts.square_array import SquareArray
from vipertools.io import imports, exports
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

    spectral_library = imports.import_library(args.library)

    if spectral_library is None or spectral_library.featureCount() == 0:
        return

    spectra_names = [x.name().strip() for x in spectral_library.profiles()]

    if args.sp_class not in spectral_library.fieldNames():
        print("{} not found in metadata header.".format(args.sp_class))
        print("Classes found: {}".format(spectral_library.fieldNames()))
        return

    class_list = np.asarray([x.metadata(args.sp_class) for x in spectral_library.profiles()], dtype=str)
    class_list = np.asarray([x.lower() for x in class_list])

    if args.square is None:

        library = np.asarray([x.values()['y'] for x in spectral_library.profiles()]).T

        if args.reflectance_scale:
            library = library / args.reflectance_scale
        else:
            scale = imports.detect_reflectance_scale_factor(library)
            library = library / scale
            print('Reflectance scale factor: ' + str(scale))

        start = time.time()
        square = SquareArray().execute(library=library, out_angle=True)
        duration = np.float16(time.time() - start)

        if args.save_square:
            exports.save_square_to_envi(square, outfile_path=os.path.splitext(args.library)[0] + '_sq.sqr', reset=False,
                                        spectra_names=spectra_names, ngb=library.shape[0], duration=duration,
                                        library_name=os.path.basename(args.library), constraints=(-0.05, 1.05, 0.025))

    else:
        square, spectra_names_square = imports.import_square(args.square)

        if square is None:
            return

        if not np.array_equal(spectra_names, spectra_names_square):
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
                                  constraints_band=square['constraints'], class_list=class_list)

    # Output
    if args.output:
        output_file = args.output
    else:
        output_file = os.path.splitext(args.library)[0] + '_emc.sli'

    # append metadata to spectral library
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
    cobi_index = fields.indexFromName("InCOB")
    cobo_index = fields.indexFromName("OutCOB")
    cobr_index = fields.indexFromName("COBI")
    profiles = spectral_library.profiles()
    spectral_library.startEditing()
    for (profile, ear, masa, ci, co, cr) in zip(profiles, result[0], result[1], result[2], result[3], result[4]):
        spectral_library.changeAttributeValue(profile.id(), ear_index, ear)
        spectral_library.changeAttributeValue(profile.id(), masa_index, masa)
        spectral_library.changeAttributeValue(profile.id(), cobi_index, ci)
        spectral_library.changeAttributeValue(profile.id(), cobo_index, co)
        spectral_library.changeAttributeValue(profile.id(), cobr_index, cr)

    # Export to new library
    spectral_library.exportProfiles(output_file)


def main():
    """ Function called by CLI. """
    parser = create_parser()
    run_emc(parser.parse_args())


if __name__ == '__main__':
    main()

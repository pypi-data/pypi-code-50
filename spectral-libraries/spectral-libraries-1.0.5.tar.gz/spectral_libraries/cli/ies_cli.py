# -*- coding: utf-8 -*-
"""
| ----------------------------------------------------------------------------------------------------------------------
| IES Command Line Interface. Available when installing viper with pip. Type 'viper-ies -h' for help.
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
from spectral_libraries.scripts.ies import Ies
from spectral_libraries.scripts.square_array import SquareArray
from spectral_libraries.io import imports, exports


def create_parser():
    """ The parser for the CLI command parameters. """
    parser = argparse.ArgumentParser(description=str(Ies.__doc__))

    # library
    parser.add_argument('library', metavar='spectral library', help='spectral library input file')
    parser.add_argument('sp_class', metavar='class', help='metadata header with the spectrum classes')
    parser.add_argument('-r', '--reflectance-scale', metavar='\b', type=int,
                        help='in case L: reflectance scale factor (default: derived from data as 1, 1 000 or 10 000)')

    # square array
    parser.add_argument('-q', '--square', metavar='\b', help='square array file')
    parser.add_argument('-s', '--save-square', action='store_true', default=False,
                        help='save the square array as an intermediate result (default: off)')

    # forced endmembers
    parser.add_argument('-f', '--forced-selection', metavar='\b', nargs='+', type=int, help='numpy array with indices '
                        'of the library spectra that should be forcefully add to the selection')
    parser.add_argument('-g', '--forced-step', metavar='\b', type=int, help='insert forced endmembers after this step')

    # output
    parser.add_argument('-o', '--output', metavar='\b',
                        help="output library (default: same name as input library with suffix '_ies.sli'")

    return parser


def run_ies(args):
    """
    Documentation: viper-ies -h
    """
    library, names, classes = imports.import_library_as_array(args.library, spectra_names=True, metadata=args.sp_class)
    class_unique, class_list = np.unique(classes, return_inverse=True)

    if len(class_unique) == 1:
        print('IES requires more than one class, please select another column')
        return

    if args.forced_selection is not None:
        forced_list = np.array(args.forced_selection, dtype=int)
        forced_location = args.forced_step
        if len(forced_list) == 0:
            print('No endmembers selected to forcefully add to the ies process.')
            return
        if max(forced_list) >= len(names):
            print('Forced library selection indexes too big.')
            return
        if min(forced_list) < 0:
            print('Forced library selection indexes too small.')
    else:
        forced_list = None
        forced_location = None

    if args.square is None:
        scale = args.reflectance_scale if args.reflectance_scale else imports.detect_reflectance_scale_factor(library)
        library = library / scale
        print('Reflectance scale factor: ' + str(scale))

        start = time.time()
        square = SquareArray().execute(library=library)
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

        bands = list(square.keys())
        if 'rmse' not in bands:
            print("No 'RMSE' band found in the square array.")
            return
        if 'constraints' not in bands:
            print("No 'Constraints' band found in the square array")
            return

    # continue for both options
    ies_selection, ies_metadata = Ies().execute(rmse_band=square['rmse'], class_list=class_list,
                                                constraints_band=square['constraints'],
                                                forced_list=forced_list, forced_location=forced_location,
                                                summary=True)
    if ies_selection is None:
        return

    # Output
    output_file = args.output if args.output else '{}_ies.sli'.format(os.path.splitext(args.library)[0])

    # write output library and metadata file
    spectral_library = imports.import_library(args.library)
    profiles_list = list(spectral_library.profiles())
    fid_attribute_index = profiles_list[0].fieldNameIndex('fid')
    fid_list = [profiles_list[x].attributes()[fid_attribute_index] for x in ies_selection]

    ies_library = spectral_library.speclibFromFeatureIDs(fid_list)
    ies_library.exportProfiles(path=output_file)

    exports.save_ies_metadata(ies_metadata, args.library, os.path.splitext(output_file)[0] + '_summary.txt',
                              forced_list, forced_location, args.sp_class, classes, names, ies_selection)


def main():
    """ Function called by CLI. """
    parser = create_parser()
    run_ies(parser.parse_args())


if __name__ == '__main__':
    main()

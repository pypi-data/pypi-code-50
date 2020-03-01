#!/usr/bin/env python3
#
# Copyright (c) 2018 Linaro Limited
# Copyright (c) 2018..2020 Bobby Noelte
# SPDX-License-Identifier: Apache-2.0

import sys
import time
import argparse
from pathlib import Path
from pprint import pprint

##
# Make relative import work also with __main__
if __package__ is None or __package__ == '':
    # use current directory visibility
    from edtsdb.database import EDTSDb
else:
    # use current package visibility
    from .edtsdb.database import EDTSDb

##
# @brief Get EDTS database prepared for cogeno use.
# @return Extended device tree database.
def edts(cogeno, force_extract = False):
    if not hasattr(cogeno, '_edtsdb'):
        # Make the EDTS database a hidden attribute of the generator
        cogeno._edtsdb = None

        cogeno.options_add_argument('-d', '--dts', metavar='FILE',
            dest='dts_file', action='store',
            type=lambda x: cogeno.options_is_valid_file(x),
            help='Load the device tree specification from FILE.')
        cogeno.options_add_argument('-b', '--bindings', nargs='+', metavar='DIR',
            dest='bindings_paths', action='store',
            type=lambda x: cogeno.options_is_valid_directory(x),
            help='Use bindings from bindings DIR for device tree extraction.' +
                 ' We allow multiple')
        cogeno.options_add_argument('-e', '--edts', metavar='FILE',
            dest='edts_file', action='store',
            help='Write or read EDTS database to/ from FILE.')

    if getattr(cogeno, '_edtsdb') is not None and force_extract is False:
        return cogeno._edtsdb

    # EDTS database file
    if cogeno.option('edts_file'):
        edts_file = cogeno.option('edts_file')
    else:
        cogeno.error(
            "No path defined for the extended device tree database file.", 2)
    edts_file = Path(edts_file)
    # DTS compiled file
    if cogeno.option('dts_file'):
        dts_file = cogeno.option('dts_file')
    else:
        cogeno.error(
            "No path defined for the device tree specification file.", 2)
    dts_file = Path(dts_file)
    if not dts_file.is_file() and not edts_file.is_file():
        cogeno.error(
            "Device tree specification file '{}' not found/ no access.".
            format(dts_file), 2)
    # Bindings
    bindings_paths = []
    if cogeno.option('bindings_paths'):
        paths = cogeno.option('bindings_paths')
        if not isinstance(paths, list):
            paths = [paths]
        if isinstance(paths[0], list):
            paths = [item for sublist in paths for item in sublist]
        for path in paths:
            try:
                path = Path(path).resolve()
            except FileNotFoundError:
                # Python 3.4/3.5 will throw this exception
                # Python >= 3.6 will not throw this exception
                path = Path(path)
            if path.is_dir():
                bindings_paths.append(path)
            elif path.is_file():
                bindings_paths.append(path.parent)
            else:
                print("edtsdatabase.py: Unknown bindings path", path, "- ignored")
    if len(bindings_paths) == 0 and not edts_file.is_file():
        cogeno.error("No path defined for the device tree bindings.", 2)

    # Check whether extraction is necessary
    if edts_file.is_file():
        # EDTS file must be newer than the DTS compiler file
        dts_date = dts_file.stat().st_mtime
        edts_date = edts_file.stat().st_mtime
        if dts_date > edts_date:
            extract = True
        else:
            extract = False
    else:
        extract = True

    cogeno.log('s{}: access EDTS {} with lock {}'
               .format(cogeno.cogeno_state(),
                       str(edts_file), cogeno.lock_file()))

    # Try to get a lock to access the database file
    # If we do not get the lock for 10 seconds an
    # exception is thrown.
    try:
        with cogeno.lock().acquire(timeout = 10):
            if extract:
                # Do not log here as log also requests the global lock
                log_msg = 's{}: extract EDTS {} from {} with bindings {}' \
                         .format(cogeno.cogeno_state(),
                                 str(edts_file),
                                 str(dts_file),
                                 bindings_paths)
                if edts_file.is_file():
                    # Remove old file
                    edts_file.unlink()
                    unlink_wait_count = 0
                    while edts_file.is_file():
                        # do dummy access to wait for unlink
                        time.sleep(1)
                        unlink_wait_count += 1
                        if unlink_wait_count > 5:
                            cogeno.error(
                                "Generated extended device tree database file '{}' no unlink."
                                .format(edts_file), frame_index = 2)
                # Create EDTS database by extraction
                cogeno._edtsdb = EDTSDb()
                cogeno._edtsdb.extract(dts_file, bindings_paths)
                # Store file to be reused
                cogeno._edtsdb.save(edts_file)
            else:
                # Do not log here as log also requests the global lock
                log_msg = 's{}: load EDTS {}' \
                         .format(cogeno.cogeno_state(),
                                 str(edts_file))
                if not edts_file.is_file():
                    cogeno.error(
                        "Generated extended device tree database file '{}' not found/ no access."
                         .format(edts_file), frame_index = 2)
                cogeno._edtsdb = EDTSDb()
                cogeno._edtsdb.load(edts_file)
    except cogeno.lock_timeout():
        # Something went really wrong - we did not get the lock
        cogeno.error(
            "Generated extended device tree database file '{}' no access."
            .format(edts_file), frame_index = 2)
    except:
        raise

    cogeno.log(log_msg)

    return cogeno._edtsdb


##
# @brief Extended DTS database for standalone usage.
#
class EDTSDatabase(EDTSDb):

    @staticmethod
    def is_valid_directory(parser, arg):
        try:
            path = Path(arg).resolve()
        except:
            path = Path(arg)
        if not path.is_dir():
            parser.error('The directory {} does not exist!'.format(path))
        else:
            # File directory exists so return the directory
            return str(path)

    @staticmethod
    def is_valid_file(parser, arg):
        try:
            path = Path(arg).resolve()
        except:
            path = Path(arg)
        if not path.is_file():
            parser.error('The file {} does not exist!'.format(path))
        else:
            # File exists so return the file
            return str(path)

    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)

    def callable_main(self, argv):
        self._parser = argparse.ArgumentParser(
                    description='Extended Device Tree Specification Database.')
        self._parser.add_argument('-l', '--load', metavar='FILE',
            dest='load_file', action='store',
            type=lambda x: EDTSDatabase.is_valid_file(self._parser, x),
            help='Load the input from FILE.')
        self._parser.add_argument('-s', '--save', metavar='FILE',
            dest='save_file', action='store',
            type=lambda x: EDTSDatabase.is_valid_file(self._parser, x),
            help='Save the database to Json FILE.')
        self._parser.add_argument('-i', '--export-header', metavar='FILE',
            dest='export_header', action='store',
            type=lambda x: EDTSDatabase.is_valid_file(self._parser, x),
            help='Export the database to header FILE.')
        self._parser.add_argument('-e', '--extract', metavar='FILE',
            dest='extract_file', action='store',
            type=lambda x: EDTSDatabase.is_valid_file(self._parser, x),
            help='Extract the database from dts FILE.')
        self._parser.add_argument('-b', '--bindings', nargs='+', metavar='DIR',
            dest='bindings_dirs', action='store',
            type=lambda x: EDTSDatabase.is_valid_directory(self._parser, x),
            help='Use bindings from bindings DIR for extraction.' +
                 ' We allow multiple')
        self._parser.add_argument('-p', '--print',
            dest='print_it', action='store_true',
            help='Print EDTS database content.')

        args = self._parser.parse_args(argv)

        if args.load_file is not None:
            self.load(args.load_file)
        if args.extract_file is not None:
            self.extract(args.extract_file, args.bindings_dirs)
        if args.save_file is not None:
            self.save(args.save_file)
        if args.export_header is not None:
            self.export_header(args.export_header)
        if args.print_it:
            pprint(self._edts)

        return 0



def main():
    EDTSDatabase().callable_main(sys.argv)

if __name__ == '__main__':
    main()


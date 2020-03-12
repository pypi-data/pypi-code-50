""" Snitch entry point """

import logging as log
import sys
import argparse

from PyQt5.QtWidgets import QApplication

from .ui.controller import Controller
from . import LOG_LEVELS, DEFAULT_LOG_LEVEL, DEFAULT_LOG_FILE, __version__

def main():
    parser = argparse.ArgumentParser(prog='snitch', )
    parser.add_argument('--version', action='version', version='%(prog)s {}'.format(__version__))
    parser.add_argument('-v', '--verbosity',
        choices=LOG_LEVELS, default=DEFAULT_LOG_LEVEL,
        help='Set the logging verbosity level. ')
    parser.add_argument('-l', '--log-file',
        default=DEFAULT_LOG_FILE,
        help='The log file location. '
            'Default is in the user temp directory.')
    parser.add_argument('-f', '--file',
        help='The test case file. '
            'If this option is used, the GUI is not started and the test case is run automatically.')
    args = parser.parse_args()

    file_handler = log.FileHandler(args.log_file)
    stream_handler = log.StreamHandler(sys.stdout)
    log.basicConfig(handlers=(file_handler, stream_handler),
                    level=args.verbosity,
                    format='%(asctime)s.%(msecs)03d:%(levelname)-8s:%(module)-12s# %(message)s',
                    datefmt='%Y%m%d-%H%M%S'
                    )
    APP = QApplication(sys.argv)
    WIN = Controller()
    if args.file:
        # run test case
        print("Loading test case: {}".format(args.file))
        return_code = -1
        if WIN.load(args.file):
            print("Playing test case...")
            results = WIN.playback(include_snapshots=True)
            print("Results: {}/{} matching screenshots".format(
                results.count(True),
                len(results)
            ))
            print("Saving results...")
            WIN.save_result(args.file)

            return_code = results.count(False)
            log.info("Return code set to %s after event replay.", return_code)
        else:
            print("Error loading test case, aborting.")

        APP.quit()
        sys.exit(return_code)
    else:
        WIN.show()
        sys.exit(APP.exec())

if __name__ == '__main__':
    main()

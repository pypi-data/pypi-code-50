import logging

from argparse import ArgumentParser

from .exception import DudendasArgumentException

logger = logging.getLogger("dudendas")


def parse_arguments():
    parser = ArgumentParser(
        prog="Dudendas",
        description="A tool for collecting words from Duden."
    )
    parser.add_argument("-v", "--debug", action="store_true",
                        help="Print debug information.")
    parser.add_argument("-q", "--quiet", action="store_true",
                        help="Print errors and warnings only.")
    parser.add_argument("-f", "--file", type=str, required=True,
                        help="File to dump fetched content into.")
    parser.add_argument("keywords", type=str, nargs='+',
                        help="Keywords to search for.")

    args = parser.parse_args()

    if args.debug and args.quiet:
        msg = 'Cannot be quiet in debug mode.'
        raise DudendasArgumentException(msg)

    return args

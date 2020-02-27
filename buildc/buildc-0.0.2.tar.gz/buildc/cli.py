import sys
from optparse import OptionParser


def parse_cmd_line():
    parser = OptionParser()
    parser.add_option(
        "--force",
        action="store_true",
        help="overwite output directly if it exists",
        default=False,
    )
    options, args = parser.parse_args()
    if len(args) == 0:
        print("Usage: {} -- command".format(sys.argv[0]))
        exit(1)
    return options, args

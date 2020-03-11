"""
CLI wrapper for SYNAW tools.
"""

####################################################################################################
# global imports
####################################################################################################
from argparse import ArgumentParser
from datetime import datetime
import logging
from sys import argv, version

from synaw_tools.template import TemplateTool
from synaw_tools.util import AliasedSubParsersAction, exit_clean, get_logger

####################################################################################################
# config
####################################################################################################

# log level (CRITICAL, ERROR, WARNING, INFO, DEBUG, NOTSET)
DEFAULT_LOG_LEVEL = logging.ERROR


####################################################################################################
# command handlers
####################################################################################################
def template_tool(args):
    logger = get_logger()
    logger.debug("Running template_tool...")
    TemplateTool().template(args.input_vars_file, args.template_file, args.output_file,
                            args.elements_to_raise)


####################################################################################################
# entripoint
####################################################################################################
def main():
    """
    Entrypoint for CLI tooling.

    :return: cli return code
    """

    parser = ArgumentParser(description='Python tooling for SYNAW.')
    parser.add_argument('-v', '--verbose', action='count', dest="verbosity")

    parser.register('action', 'parsers', AliasedSubParsersAction)
    subparsers = parser.add_subparsers(title='tool',
                                       metavar="TOOL",
                                       description='available tools',
                                       help='tool description')

    template_tool_parser = subparsers.add_parser('template_tool',
                                                 aliases=("t", "template"),
                                                 help="fill config templates")
    template_tool_parser.set_defaults(func=template_tool)
    template_tool_parser.add_argument('-V', '--config-verbosity', default="1",
                                      action='count', dest="config_verbosity",
                                      help="leading comment symbols to show")
    template_tool_parser.add_argument('--comment-str', default="#",
                                      help="the string to start a comment (example: '#')")
    template_tool_parser.add_argument('-i', '--input-vars-file', default=[], nargs='+',
                                      help="an input variable file (yaml or json)")
    template_tool_parser.add_argument('-f', '--template-file', default=["-"], nargs='+',
                                      help="a template input file ('-' for stdin)")
    template_tool_parser.add_argument('-o', '--output-file', default=["-"], nargs='+',
                                      help="an output file ('-' for stdout)")
    template_tool_parser.add_argument('-e', '--elements-to-raise', default=[], nargs='+',
                                      help="the list of element to raise")

    args = parser.parse_args()

    if args.verbosity is None:
        logging.basicConfig(level=DEFAULT_LOG_LEVEL)
    elif args.verbosity >= 3:
        logging.basicConfig(level=logging.DEBUG)
    elif args.verbosity >= 2:
        logging.basicConfig(level=logging.INFO)
    elif args.verbosity >= 1:
        logging.basicConfig(level=logging.WARNING)
    else:
        logging.basicConfig(level=DEFAULT_LOG_LEVEL)

    main_logger = logging.getLogger("main")
    main_logger.debug("Logger ready.")
    main_logger.debug("Using Python: %s", version)

    main_logger.debug("Parsing arguments...")
    main_logger.debug("Arguments: %s", str(argv))

    main_logger.debug("Setting starting timestamp...")
    timestamp_start = datetime.now()
    main_logger.info("Start: %s", timestamp_start.isoformat())

    main_logger.debug("Entering subcommand...")
    args.func(args)
    main_logger.debug("Setting ending timestamp...")
    timestamp_end = datetime.now()
    main_logger.info("End: %s (duration: %s)",
                     timestamp_end.isoformat(),
                     str(timestamp_end - timestamp_start))

    exit_clean(logger=main_logger)


if __name__ == "__main__":
    main()

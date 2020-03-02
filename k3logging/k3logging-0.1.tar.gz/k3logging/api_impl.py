'''
k3logging.api_impl

Created on 2 Mar 2020
Author: Joachim Kestner <joachim.kestner@khoch3.de>
'''

import logging

def _trace(msg, *args, **kwargs):
    root = logging.getLogger()
    if len(root.handlers) == 0:
        logging.basicConfig()
    root.trace(msg, *args, **kwargs)
    
def enable_trace_logging():
    logging.TRACE = logging.DEBUG - 5
    logging.addLevelName(logging.TRACE, "TRACE")
    logging.setLoggerClass(K3Logger)
    logging.trace = _trace


class K3Logger(logging.getLoggerClass()):
    
    def trace(self, msg, *args, **kwargs):
        if self.isEnabledFor(logging.TRACE):
            logging.log(logging.TRACE, msg, *args, **kwargs)


def set_parser_log_arguments(parser):
    parser.add_argument("-v", "--verbose", action="store_true", help="Enable info logging")
    parser.add_argument("-vv", "--extra_verbose", action="store_true", help="Enable debug logging")
    if hasattr(logging, "TRACE"):
        parser.add_argument("-vvv", "--super_verbose", action="store_true", help="Enable trace logging")

def eval_parser_log_arguments(args, msgFormat="{asctime} {levelname}:  {message}"):
    if args.verbose:
        logging.basicConfig(level=logging.INFO, format=msgFormat, style="{")
    elif args.extra_verbose:
        logging.basicConfig(level=logging.DEBUG, format=msgFormat, style="{")
    elif hasattr(logging, "TRACE") and args.super_verbose:
        logging.basicConfig(level=logging.TRACE, format=msgFormat, style="{")
    else:
        logging.basicConfig(level=logging.WARN, format=msgFormat, style="{")

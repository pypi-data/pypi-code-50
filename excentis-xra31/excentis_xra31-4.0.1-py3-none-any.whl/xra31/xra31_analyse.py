#!/usr/bin/env python3
"""
Command-line interface to :class:`~excentis.xra31.analysis.Analysis`.
"""

# pylint: disable=invalid-name
# pylint: disable=logging-format-interpolation
# pylint: disable=logging-not-lazy

import argparse
import logging
import os
import pathlib
import sys

from excentis import xra31

# Arguments
parser = argparse.ArgumentParser(
    description="Access XRA-31 capture files.  "
    "The commands can be combined, and files won't be deleted unless "
    "downloading succeeds.")

parser.add_argument("address",
                    metavar="XRA-31",
                    help="XRA-31 hostname or IP address")
parser.add_argument("-f",
                    "--filename",
                    metavar="directory/remote.pcap",
                    help="capture filename on the XRA-31.  "
                    "If missing, the latest capture is downloaded",
                    type=str)

parser.add_argument("-q",
                    "--quiet",
                    action="store_true",
                    help="don't print progress messages")
parser.add_argument("-v",
                    "--verbose",
                    action="count",
                    help="print debugging messages")
parser.add_argument("--version",
                    action="store_true",
                    help="print client version and server release")

parser_commands = parser.add_argument_group("commands")
parser_commands.add_argument("--download",
                             action="store_true",
                             help="store captures locally")
parser_commands.add_argument("--delete",
                             action="store_true",
                             help="remove captures from the XRA-31")

parser_options = parser.add_argument_group("command options")
parser_options.add_argument("-o",
                            "--output",
                            metavar="local.pcap",
                            help="local download location",
                            type=str)
parser_options.add_argument(
    "-r",
    "--rolling",
    action="store_true",
    help="treat filename as a full rolling file capture")
parser_options.add_argument(
    "-a",
    "--append",
    action="store_true",
    help="append capture to an existing file; requires download")
parser_options.add_argument("-c",
                            "--compress",
                            action="store_true",
                            help="compress the downloaded capture file (gzip)")


def main():
    args = parser.parse_args()

    # Logging
    logger = logging.getLogger(pathlib.Path(sys.argv[0]).name)
    logging.basicConfig(
        format="[%(asctime)s][%(name)s][%(levelname)s]: %(message)s")
    if args.verbose:
        logging.root.setLevel(logging.DEBUG)
        if args.verbose > 1:
            xra31.tracer.setLevel(logging.DEBUG)
        else:
            xra31.tracer.setLevel(logging.WARNING)
    elif not args.quiet:
        logger.setLevel(logging.INFO)

    # Connect
    try:
        client = xra31.connect(address=args.address)
    except xra31.exceptions.Xra31VersionException as error:
        logger.error("Could not connect to an XRA-31 at \"{}\": {}.".format(
            args.address, str(error)))
        sys.exit(1)
    except xra31.exceptions.Xra31Exception as error:
        logger.error("Could not connect to an XRA-31 at \"{}\"."
                     " Please verify the host.{}{}: {}".format(
                         args.address, os.linesep,
                         type(error).__name__, str(error)))
        sys.exit(1)

    logger.info("Connected to " + str(client))

    if args.verbose:
        client.logger.setLevel(logging.DEBUG)
    elif not args.quiet:
        client.logger.setLevel(logging.INFO)

    # Version
    if args.version:
        logger.info("Client version " + client.version)
        logger.info("XRA-31 release " + client.server_version)

    # Commands
    if args.filename:
        parts = args.filename.rsplit('/', 1)
        if len(parts) > 1 and parts[0]:
            filename = parts[1]
            directory = parts[0]
        else:
            filename = parts[0]
            directory = ""
    else:
        directory = client.capture.output.directory
        filename = client.capture.filename

    if args.download:
        logger.info("Download capture {}/{}".format(directory, filename))
        try:
            client.analysis.download(directory=directory,
                                     filename=filename,
                                     output=args.output,
                                     append=args.append,
                                     rolling=args.rolling,
                                     compress=args.compress,
                                     verbose=not args.quiet)
        except xra31.exceptions.Xra31FileNotFoundException as error:
            logger.error("Could not download {}/{} from {}: {}".format(
                directory, filename, args.address, str(error)))
            sys.exit(1)

    if args.delete:
        logger.info("Delete capture {}/{}".format(directory, filename))
        try:
            client.analysis.delete(directory=directory,
                                   filename=filename,
                                   rolling=args.rolling,
                                   verbose=not args.quiet)
        except xra31.exceptions.Xra31FileNotFoundException as error:
            logger.error("Could not delete {}/{} from {}: {}".format(
                directory, filename, args.address, str(error)))
            sys.exit(1)

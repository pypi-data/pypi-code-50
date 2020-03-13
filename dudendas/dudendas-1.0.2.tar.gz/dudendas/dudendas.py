import json
import logging

from .arguments import parse_arguments
from .exception import DudendasArgumentException
from .logging import setup_logger
from .search import DudenSearch

logger = logging.getLogger("dudendas")


def get_words(keyword):
    msg = "Searching keyword '%s'."
    logger.debug(msg, keyword)

    search = DudenSearch(keyword)
    search.parse_results()
    words = search.parse_words(group=keyword)

    msg = "Got %d words with keyword '%s'."
    logger.info(msg, len(words), keyword)

    return words


def main():
    setup_logger(logger)

    try:
        args = parse_arguments()
    except DudendasArgumentException as e:
        msg = 'Failed to parse arguments: ' + str(e)
        logger.error(msg)
        exit(1)

    if args.debug:
        logger.setLevel(logging.DEBUG)
        msg = 'Application is running in debug mode.'
        logger.debug(msg)
    elif args.quiet:
        logger.setLevel(logging.WARNING)

    logger.info('Starting Dudendas.')

    dumpfile = args.file
    keywords = args.keywords

    try:
        words = set()

        for keyword in keywords:
            new_words = get_words(keyword)
            words.update(new_words)

        with open(dumpfile, "w") as f:
            json.dump([w.serialize() for w in words], f, indent="\t")

    except KeyboardInterrupt:
        msg = 'Received keyboard interrupt.'
        logger.info(msg)
        exit(1)

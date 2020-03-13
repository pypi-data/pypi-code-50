from functools import lru_cache
from argparse import ArgumentParser
import logging
import logging.config
import yaml
import miniscule


@lru_cache(maxsize=1)
def read_config(path=None):
    try:
        return miniscule.read_config(path)
    except FileNotFoundError:
        return None


def _init_logging(config=None):
    config = config or read_config()
    if config is None:
        return
    path = config.get("log_config")
    if path is None:
        return

    with open(path, "r") as handle:
        log_config = yaml.load(handle.read(), Loader=yaml.SafeLoader)
        logging.config.dictConfig(log_config)


def _create_parser():
    parser = ArgumentParser()
    return parser


PARSER = _create_parser()
SUBPARSERS = PARSER.add_subparsers()


def main():
    _init_logging()
    settings, remainder = PARSER.parse_known_args()
    if hasattr(settings, "fn"):
        settings.fn(settings, remainder)
    else:
        PARSER.print_help()

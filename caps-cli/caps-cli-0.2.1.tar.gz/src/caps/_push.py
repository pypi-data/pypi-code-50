import yaml
import json
import logging
from caps import _utils, _transform_data


def push(yaml_file_path):
    transformed_json = _transform_data.create_json(yaml_file_path)
    logging.info(json.dumps(transformed_json))


def _main():
    _utils.init_logger()
    logging.info("Running from main")
    logging.info("Hmm, no one has put code in _push.py's main function. Quitting")


if __name__ == "__main__":
    try:
        _main()
    except Exception as e:
        logger.exception(e)
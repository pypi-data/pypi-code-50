import yaml
import json
import logging
from caps import _utils, _metadata_schema, _transform_data


def validate(metadata_file_path):
    try:
        _metadata_schema.validate_file(metadata_file_path)
    except FileNotFoundError:
        logging.error("Could not fine \"" + metadata_file_path + "\" please for typos in path name")
        quit()

def push(yaml_file_path):
    transformed_json = _transform_data.create_json(yaml_file_path)
    logging.info(json.dumps(transformed_json))


def _main():
    _utils.init_logger()
    logging.info("Running from main")
    logging.info("Hmm, no one has put code in _push.py's main function. Quitting")
import yaml
import json
import logging
from caps import _utils


def initialize(inputs=0, outputs=0, parameters=0):
    with open("./files/initialize_schema.json", "r") as fp:
        json_obj = json.load(fp)

    template_obj = {}
    if inputs > 0:
        template_obj["hasInput"] = []
        for _ in range(inputs):
            template_obj["hasInput"].append(json_obj["schema"]["DatasetSpecification"])

    if outputs > 0:
        template_obj["hasOutput"] = []
        for _ in range(outputs):
            template_obj["hasOutput"].append(json_obj["schema"]["DatasetSpecification"])

    if parameters > 0:
        template_obj["hasParameter"] = []
        for _ in range(parameters):
            template_obj["hasParameter"].append(json_obj["schema"]["Parameter"])

    try:
        with open("./insertion_template.json", "w") as fp:
            fp.write(json.dumps(template_obj))

        logging.info("Generated the insertion template file in the root directory")
    except Exception as e:
        logging.error(str(e))


def _main():
    _utils.init_logger()
    logging.info("Running from main")
    logging.info("Hmm, no one has put code in _initialize.py's main function. Quitting")


if __name__ == "__main__":
    try:
        _main()
    except Exception as e:
        logger.exception(e)
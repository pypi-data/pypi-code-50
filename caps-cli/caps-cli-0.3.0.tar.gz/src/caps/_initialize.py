import logging
from caps import _utils, _metadata_schema
import os


# class NoAliasDumper(yaml.Dumper):
#     def ignore_aliases(self, data):
#         return True


def initialize(inputs=0, outputs=0, parameters=0, dir=None, force=False):

    outp = ""
    name = None

    # Checks if directory is given. Uses cd if none given
    if dir is None:
        path = os.getcwd()
    else:
        path = dir

    # If user did not give a name in dir then we will proved a default one
    hasName = os.path.splitext(path)
    if len(hasName[1]) <= 0:
        path = os.path.join(path, "example_yaml.yaml")

    # Checks if file already exists
    if os.path.isfile(path):
        logging.warning("\"" + path + "\" already exists")
        if not force:
            logging.info("Aborting YAML Generation. Use flag -f to force override")
            quit()
        else:
            logging.info("Overriding existing file")
            os.remove(path)

    # Checks if directory exists and finds file
    stream = None
    try:
        stream = open(path, 'w+')
    except FileNotFoundError:
        logging.error("Path does not exist.")
        quit()

    # Creates human readable text from _metadata_schema.py
    outp += _metadata_schema.get_hr_metadata()
    outp += "\nhasInput:\n"
    for i in range(1, inputs + 1):
        outp += _metadata_schema.get_hr_inputs(i)
    outp += "hasOutput:\n"
    for o in range(1, outputs + 1):
        outp += _metadata_schema.get_hr_outputs(o)
    outp += "hasParameter:\n"
    for p in range(1, parameters + 1):
        outp += _metadata_schema.get_hr_parameters(p)

    stream.write(outp)


def _main():
    _utils.init_logger()
    logging.info("Running from main")
    logging.info("Hmm, no one has put code in _initialize.py's main function. Quitting")


if __name__ == "__main__":
    try:
        _main()
    except Exception as e:
        logging.exception(e)
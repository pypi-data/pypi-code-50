"""
Fill config templates.
"""

from jinja2 import Template
import yaml

from .util import get_logger
from .var import raise_elements, merge_elements


class TemplateTool:
    """
    Fill config templates.
    """
    def template(self, input_vars_files: dict = None,
                 template_files: str = None, output_files: dict = None,
                 elements_to_raise: list = None):
        """
        Fill template with merged and raised variables, then store to output file.

        :param logger: the logger
        :param input_vars_files: list of files with input vars
        :param template_files: the list of template files
        :param output_files: the list of output files
        :param elements_to_raise: the list of elements to raise
        :return: None
        """

        logger = get_logger()

        if elements_to_raise is None:
            elements_to_raise = []

        logger.debug("Starting templating...")
        logger.debug("input_vars_files: %s", input_vars_files)
        logger.debug("template_files: %s", template_files)
        logger.debug("output_files: %s", output_files)

        logger.debug("Initializing variables...")
        input_vars = {}
        template_lines = []
        output_lines = []

        logger.debug("Processing input vars files...")
        for input_vars_file in input_vars_files:
            logger.debug("Processing input vars file %s...", input_vars_file)
            with open(input_vars_file, 'r') as file_handle:
                logger.debug("Reading input vars from %s...", input_vars_file)
                new_vars = yaml.safe_load(file_handle)
                logger.debug("Merging existing and new vars...")
                input_vars = merge_elements(input_vars, new_vars)
        logger.info("Merged input vars: %s", input_vars)

        logger.debug("Processing elements to raise...")
        logger.debug("Copy existing input vars...")
        logger.debug("Raising elements %s...", elements_to_raise)
        input_vars = raise_elements(input_vars, elements_to_raise)
        logger.info("Raised elements: %s", input_vars)

        logger.debug("Processing template files...")
        for template_file in template_files:
            logger.debug("Processing template file %s...", template_file)
            with open(template_file, 'r') as file_handle:
                logger.debug("Reading template from %s...", template_file)
                template_lines.extend(file_handle.readlines())
            template_lines.append("\n")
        template_str = "".join(template_lines)
        logger.info("Read template file: %s", template_str)

        logger.debug("Filling templates...")
        template = Template(template_str)
        output_str = template.render(service_config=input_vars["service_config"])
        logger.info("Output string: \n%s", output_str)

        logger.debug("Processing output files...")
        for output_file in output_files:
            logger.debug("Processing output file %s...", output_file)
            with open(output_file, 'w') as file_handle:
                logger.debug("Reading template from %s...", output_file)
                file_handle.write(output_str)

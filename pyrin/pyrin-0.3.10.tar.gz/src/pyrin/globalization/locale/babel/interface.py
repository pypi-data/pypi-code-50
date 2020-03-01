# -*- coding: utf-8 -*-
"""
locale babel interface module.
"""

from pyrin.cli.params import HelpParamMixin


class BabelCLIHandlerBase(HelpParamMixin):
    """
    babel cli handler base class.
    all babel cli handlers must be subclassed from this.
    """

    def __init__(self, name):
        """
        initializes an instance of BabelCLIHandlerBase.

        :param str name: the handler name that should be registered
                         with. this name must be the exact name that
                         this handler must emmit to cli.
        """

        super().__init__(name)

    def _get_common_cli_options(self):
        """
        gets the list of common cli options.

        :rtype: list
        """

        return ['pybabel']

    # def _generate_common_cli_handler_options_metadata(self):
    #     """
    #     generates common cli handler options metadata.
    #
    #     :rtype: list[CLIHandlerOptionsMetadata]
    #     """
    #
    #     output_file = CLIHandlerOptionsMetadata('output_file', '--output-file')
    #
    #     options = [help_option, output_file]
    #
    #     return options

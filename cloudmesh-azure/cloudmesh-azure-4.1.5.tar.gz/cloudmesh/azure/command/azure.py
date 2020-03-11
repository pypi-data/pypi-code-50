from __future__ import print_function

from cloudmesh.common.console import Console
from cloudmesh.shell.command import PluginCommand
from cloudmesh.shell.command import command


class AzureCommand(PluginCommand):

    # noinspection PyUnusedLocal
    @command
    def do_azure(self, args, arguments):
        """
        ERROR: This command is not implemented!

        :param args:
        :param arguments:
        :return:
        """
        # """
        # ::
        #
        #   Usage:
        #         azure --file=FILE
        #         azure list
        #
        #   This command does some useful things.
        #
        #   Arguments:
        #       FILE   a file name
        #
        #   Options:
        #       -f      specify the file
        #
        # """
        # arguments.FILE = arguments['--file'] or None
        #
        # VERBOSE(arguments)
        #
        # m = Manager()
        #
        # if arguments.FILE:
        #     print("option a")
        #     m.list(path_expand(arguments.FILE))
        #
        # elif arguments.list:
        #     print("option b")
        #     m.list("just calling list without parameter")
        #
        Console.error("This command is not implemented!")
        return ""

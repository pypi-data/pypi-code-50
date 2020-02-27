import os
from importlib import import_module
from pvlv_commando.configurations.configuration import COMMANDS_DIR
from pvlv_commando.commando.command_descriptor import CommandDescriptor
from pvlv_commando.configurations.configuration import logger

from pvlv_commando.commando.auto_command_creation.start_command import StartCommand

"""
Format the command_dir string
COMMANDS_DIR in the cfg file, the dir of the commands folder, must end with / (example: 'pvlv/commands/')
"""
if COMMANDS_DIR.endswith('/'):
    commands_dir = COMMANDS_DIR[:-1]
else:
    commands_dir = COMMANDS_DIR


class Importer:

    @staticmethod
    def __build_class_name(command):
        """
        Build the class name from the command name
        :param command:
        :return:
        """
        spl = []
        for el in command.split('_'):
            spl.append(str(el.capitalize()))
        return ''.join(spl)

    @staticmethod
    def build_descriptor(module, command, command_descriptor_dir):
        """
        Build the command descriptor
        :param module:
        :param command:
        :param command_descriptor_dir:
        :return:
        """
        cd = CommandDescriptor()
        cd.module = module
        cd.name = command
        cd.read_command(command_descriptor_dir)
        return cd

    @staticmethod
    def __remove_ignored(directory):
        """
        :param directory: the directory name where do the lookup for the sub-folders
        :return the import_list with the names of the folders to import

        Remove the private folders from the import list
        """
        listdir = os.listdir(os.path.dirname(directory + '/'))
        import_list = []
        for el in listdir:
            if not el.startswith('_'):
                import_list.append(el)
        return import_list

    def import_commands(self):
        """
        Go throw all the folders in the project command folder and load all the modules and commands

        :return: the command_list that contain all the imported commands

        Every el of the command_list is a tuple that contain:
        - command_descriptor - the data that define the command get from command.json
        - imported_module - equal to from command import CommandClass
        - class_name - the name of the class inside the command file
        """
        global commands_dir
        command_list = []

        # convert the dir into a import path
        import_point = commands_dir.replace('/', '.')

        # List all the main modules
        for module in self.__remove_ignored(commands_dir):

            package = '{}.{}'.format(import_point, module)
            module_dir = '{}/{}'.format(commands_dir, module)

            # List all the commands inside the single module
            for command in self.__remove_ignored(module_dir):

                command_import_point = '.{}.{}'.format(command, command)
                command_dir = '/{}/{}'.format(command, command)

                imported_module = import_module(command_import_point, package=package)

                class_name = self.__build_class_name(command)

                """
                Read the command description file and create the class to store and access all the data
                Set data
                - package membership
                - command name
                - read the command file and extract all the other data
                """

                cd = self.build_descriptor(module, command, '{}/{}.json'.format(module_dir, command_dir))

                # append command (command_descriptor, module, class_name)
                command_list.append((cd, imported_module, class_name))
                logger.info('In module: <{}>, loaded: <{}>'.format(module, class_name))

        return command_list

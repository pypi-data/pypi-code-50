import os
from importlib import import_module
from pvlv_commando.configurations.configuration import COMMANDS_DIR
from pvlv_commando.commando.command_descriptor import CommandDescriptor
from pvlv_commando.configurations.configuration import logger

from pvlv_commando.commando.new_command.new_command import NewCommand

"""
Format the command_dir string
COMMANDS_DIR in the cfg file, the dir of the commands folder, must end with / (example: 'pvlv/commands/')
"""
if COMMANDS_DIR.endswith('/'):
    commands_dir = COMMANDS_DIR[:-1]
else:
    commands_dir = COMMANDS_DIR


def build_class_name(command):
    """
    Build the class name from the command name
    :param command:
    :return:
    """
    spl = []
    for el in command.split('_'):
        spl.append(str(el.capitalize()))
    return ''.join(spl)


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


def importer():
    global commands_dir
    command_list = []

    # convert the dir into a import path
    import_point = commands_dir.replace('/', '.')

    # List all the main modules
    for module in os.listdir(os.path.dirname(commands_dir + '/')):

        package = '{}.{}'.format(import_point, module)
        module_dir = '{}/{}'.format(commands_dir, module)

        # List all the commands inside the single module
        for command in os.listdir(os.path.dirname(module_dir + '/')):

            command_import_point = '.{}.{}'.format(command, command)
            command_dir = '/{}/{}'.format(command, command)

            imported_module = import_module(command_import_point, package=package)

            class_name = build_class_name(command)

            """
            Read the command description file and create the class to store and access all the data
            Set data
            - package membership
            - command name
            - read the command file and extract all the other data
            """

            cd = build_descriptor(module, command, '{}/{}.json'.format(module_dir, command_dir))

            # append command (command_descriptor, module, class_name)
            command_list.append((cd, imported_module, class_name))
            logger.info('In module: <{}>, loaded: <{}>'.format(module, class_name))

    return command_list

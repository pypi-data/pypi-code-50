import os
from pvlv_commando.commando.command_importer import (
    importer,
    build_descriptor,
)
from pvlv_commando.commando.command_descriptor import CommandDescriptor
from pvlv_commando.commando.command_structure_reader import read_command_structure
from pvlv_commando.manual.manual import Manual
from pvlv_commando.exceptions.permissions_exceptions import InsufficientPermissions
from pvlv_commando.exceptions.errors_exceptions import (
    CommandNotFound,
    CommandExecutionFail,
    ArgVoidNotAllowed,
    ParamNotFound,
    MaxHourlyUses,
    MaxDailyUses,
)
from pvlv_commando.configurations.configuration import logger


class Commando(object):
    """
    Commando class to handle commands in a easy way
    The exception handling must be done outside of this class
    """
    def __init__(self):
        """
        Load all the packages and commands should be done only once.
        For efficiency it must be put as a static class for all the project.
        """
        self.__command_list = importer()

        """
        Input data, to check run the command
        text: the message without the chat/str command invocation
        language: the language code for message response
        permissions: the user permission in the guild/chat
        hourly_executions: hourly number of uses of the command by the user
        daily_executions: daily number of uses of the command by the user
        """
        self.text = ''
        self.language = 'eng'
        self.permissions = 0
        self.hourly_executions = 0
        self.daily_executions = 0 

        """
        Structure of the command found
        Stored to be executed
        """
        self.__command_found = None
        self.__trigger = None
        self.__arg = None
        self.__params = {}

        # Builtin manual
        self.__is_manual = False
        self.__manual_descriptor = build_descriptor(
            'builtin', 'manual', os.path.dirname(os.path.realpath(__file__)) + '/manual/manual.json'
        )

        # Create the list of the commands descriptors that will be used in the manual command
        self.__command_descriptors = []
        for cd in self.__command_list:
            self.__command_descriptors.append(cd[0])  # class that contains json commands info

        logger.info('Commando Module Ready')

    def __check_command_integrity(self, command_descriptor: CommandDescriptor):
        """
        Check if the command has an allowed arg and params
        Do input validation of the arg and params
        """
        if self.__arg is None:
            if '' not in command_descriptor.handled_args_list():
                return ArgVoidNotAllowed(self.language)

        for key in self.__params.keys():
            if key not in command_descriptor.handled_params_list():
                raise ParamNotFound(self.language, key)

    def find_command(self, text: str, language: str, permissions: int):
        """
        :param text: the imput text
        :param language: the language of the chat
        :param permissions: the permission value of the user

        Find if there is a command in the text
        N.B.: YOU HAVE TO REMOVE THE COMMAND CHAR/STR TRIGGER AND SEND CLEAN TEXT
        - read command structure and save it in the class
        - check if the command is a built in type
        - if not check in the others commands
        - if the command is not found in commands raise not found exception
        """

        self.text = text
        self.language = language
        self.permissions = permissions

        self.__trigger, self.__arg, self.__params = read_command_structure(self.text)

        # Check build in commands
        if self.__trigger in self.__manual_descriptor.invocation_words:
            self.__is_manual = True
            return self.__manual_descriptor.name

        # Check in the others commands
        else:
            for command in self.__command_list:
                command_descriptor, module_import, class_name = command
                if self.__trigger in command_descriptor.invocation_words:
                    self.__command_found = command
                    return command_descriptor.name
            else:
                raise CommandNotFound(self.language, command=self.__trigger, arg=self.__arg, params=self.__params)

    def run_command(self, bot, max_chunk_len=1500):
        """
        Execute the command
        :param bot: the bot var, that will be passed to the command. Used to send message and perform actions.
        If you have multiple params to pass to the command use a tuple inside the bot or a dict
        :param max_chunk_len: the max len of the text
        :return: an eventual output that have to be sent in chat
        :exception: CommandNotFound: the command has not been found
        :exception: InsufficientPermissions: current user don't have permissions to run the code
        :exception: CommandExecutionFail: the command has fail to execute for some error inside che command code
        """

        command_descriptor, module_import, class_name = self.__command_found

        """
        If Manual Run Manual
        The manual is cut in chunks and return the chunks array
        This is made because some chats have a limit in message len, 
        to do this will be used max_chunk_len
        - rest is manual flag
        - build calss and run commands
        - reset permissions 
        - retur: an array of strings, where each string has the max len of the max_chunk_len
        
        if fail raise command exception
        """
        if self.__is_manual:
            logger.info('RUN: manual')

            self.__is_manual = False
            self.__check_command_integrity(self.__manual_descriptor)

            try:
                manual = Manual(
                    self.language,
                    self.__manual_descriptor,
                    self.__command_descriptors,
                    self.__arg,
                    self.__params,
                    max_chunk_len,
                    self.permissions
                )
                self.permissions = 0  # Reset permissions
                return manual.run()

            except Exception as exc:
                logger.error(exc)
                raise CommandExecutionFail(
                    self.language,
                    full_exception=exc,
                    command=self.__manual_descriptor,
                    arg=self.__arg,
                    params=self.__params
                )

        """
        Else run the standard module
        - check the permissions to run that command
        - check the max uses per day/hour of the command
        - check command integrity
        - get the class, built it and run it
        - return void string ''
        
        if fail raise command exception 
        """
        logger.info('RUN: ' + command_descriptor.name)

        if command_descriptor.permissions >= self.permissions:
            self.permissions = 0  # Reset permissions
            raise InsufficientPermissions(self.language)

        self.permissions = 0  # Reset permissions

        # check max uses per hour
        if command_descriptor.hourly_max_uses and self.hourly_executions > command_descriptor.hourly_max_uses:
            raise MaxHourlyUses(self.language, command_descriptor.hourly_max_uses, command_descriptor.daily_max_uses)

        # check max uses per day
        if command_descriptor.daily_max_uses and self.daily_executions > command_descriptor.daily_max_uses:
            raise MaxDailyUses(self.language, command_descriptor.daily_max_uses)

        self.__check_command_integrity(command_descriptor)
        command_class = getattr(module_import, class_name)

        try:
            command = command_class(bot, self.language, command_descriptor, self.__arg, self.__params)
            command.run()

        except Exception as exc:
            logger.error(exc)
            raise CommandExecutionFail(
                self.language,
                full_exception=exc,
                command=command_descriptor,
                arg=self.__arg,
                params=self.__params
            )

        return ''

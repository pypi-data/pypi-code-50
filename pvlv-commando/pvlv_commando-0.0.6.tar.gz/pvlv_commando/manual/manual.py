from .translations.manual_reply import (
    invocation,
    beta,
    handled_args,
    handled_params,
    command_mask,
    command_not_found,
    command_insufficient_permissions,
)


class Manual(object):
    """
    Builtin in manual
    """
    def __init__(self, language, command, commands_descriptor, arg, params, max_chunk_len, permissions):
        """
        :param language: language
        :param command: the man command descriptor
        :param commands_descriptor: the list of command descriptors
        :param arg: the args during command invocation
        :param params: the params during command invocations
        :param max_chunk_len: the max len on the str out, if exceed, cut in chunks
        :param permissions: int value of the user permission
        """

        self.language = language
        self.command = command
        self.commands_descriptor = commands_descriptor
        self.arg = arg
        self.max_chunk_len = max_chunk_len  # max len of a single message, limited by the
        self.permissions = permissions

        _vars = command.handled_params_list
        for param in params:
            name = '_{}'.format(param[0])
            setattr(self, name, param[1])

    def __build_title(self, com):
        """
        Build the title with in vocations words and beta command badge if is
        :param com: the command obj
        :return: the title section
        """
        _out = '**{}**\n{}\n'.format(com.name.upper(), com.description_by_language(self.language))
        if com.invocation_words:
            _out += '{}\n'.format(invocation(self.language, com.invocation_words))
        if com.beta_command:
            _out += '\n{}\n'.format(beta(self.language))
        return _out

    @staticmethod
    def __build_usage(title, dictionary):
        """
        Build the args o params section
        :param title: as str
        :param dictionary: the params or args already with the language needed
        :return: the section built
        """
        if dictionary:
            out = '\n{}\n'.format(title)
            for key in dictionary.keys():
                key_description = dictionary.get(key)
                out += '**{}** -- {}\n'.format(
                    key if key != '' else 'void',
                    key_description
                )
            return out
        else:
            return ''

    def __build_full_man(self, com):
        """
        Build the full man command of a single command
        :param com: the command obj
        :return: full man
        """

        out = self.__build_title(com)
        out += self.__build_usage(handled_args(self.language), com.handled_args_by_language(self.language))
        out += self.__build_usage(handled_params(self.language), com.handled_params_by_language(self.language))
        return out

    def __build_base_man(self, com):
        """
        Build the base man command of a single command
        :param com: the command obj
        :return: base man
        """

        if com.permissions <= self.permissions:
            return '{}\n'.format(self.__build_title(com))
        else:
            return ''

    def command_name(self):
        """
        Find the command in the arg and show the full manual
        :return: full manual of the command
        """
        com_found = None
        # search for the command
        for command in self.commands_descriptor:
            if self.arg in command.invocation_words:
                com_found = command

        if com_found:
            # check the permission to see the command
            if com_found.permissions <= self.permissions:
                return self.__build_full_man(com_found)
            else:
                return command_insufficient_permissions(self.language)

        return command_not_found(self.language)

    def void_arg(self):
        """
        Build the manual of the manual if the arg is leaved void
        :return: full manual
        """
        return self.__build_full_man(self.command)

    def all_commands(self):
        """
        Build the list of all commands with a simple description
        :return: simple description of commands
        """
        _out = ''
        for command in self.commands_descriptor:
            _out += self.__build_base_man(command)

        return _out

    def run(self):
        """
        Main function that will be called by the command innvocator
        :return: the text split in chunks
        """

        chose = {
            None: self.void_arg,
            'all': self.all_commands,
        }

        try:
            out = chose[self.arg]()
        except KeyError:
            out = self.command_name()

        return out

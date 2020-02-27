import json
from pvlv_commando.commando.modules.base_command_reader import BaseCommandReader


class CommandDescriptor(BaseCommandReader):

    def __init__(self):
        super().__init__()

        self.management_command = False  # can be used only by owner of the bot

        self.beta_command = False
        self.pro_command = 0  # payment command, set the level of pro 1, 2, 3, etc.
        self.dm_enabled = True  # can be used also in dm
        self.enabled_by_default = False  # this command is active by default
        self.permissions = 0  # permissions to use the command

        self.cost = 0  # the cost in bits of the command. This is useful to reflect the computational cost
        self.hourly_max_uses = False  # cause of the computational cost, False disabled
        self.daily_max_uses = False  # cause of the computational cost, False disabled

        self.__handled_args = {}
        self.__handled_args_list = []
        self.__handled_params = {}
        self.__handled_params_list = []

    def read_command(self, command_descriptor_dir):

        with open(command_descriptor_dir) as f:
            file = json.load(f)

        self.management_command = file.get('management_command', self.management_command)
        self.beta_command = file.get('beta_command', self.beta_command)
        self.pro_command = file.get('pro_command', self.pro_command)
        self.dm_enabled = file.get('dm_enabled', self.dm_enabled)
        self.enabled_by_default = file.get('enabled_by_default', self.enabled_by_default)
        self.permissions = file.get('permissions', self.permissions)

        self.cost = file.get('cost', self.cost)
        self.hourly_max_uses = file.get('hourly_max_uses', self.hourly_max_uses)
        self.daily_max_uses = file.get('daily_max_uses', self.daily_max_uses)

        self.invocation_words = file.get('invocation_words', self.invocation_words)

        # description is in superclass so must be private not protected
        self._description = file.get('description', self._description)
        self.__handled_args = file.get('handled_args', self.__handled_args)
        self.__handled_args_list = list(self.__handled_args.keys())
        self.__handled_params = file.get('handled_params', self.__handled_params)
        self.__handled_params_list = list(self.__handled_params.keys())

        self.examples = file.get('examples')

    @property
    def handled_args_list(self):
        return self.__handled_args_list

    @property
    def handled_params_list(self):
        return self.__handled_params_list

    @staticmethod
    def __read_value_by_language(language, dictionary):
        description = dictionary.get(language)
        if description is None:
            description = dictionary.get('eng')
            if description is None:
                raise Exception('There is not language descriptions in this command')
        return description

    def handled_args_by_language(self, language):
        result = {}
        for key in self.__handled_args.keys():
            result[key] = self.__read_value_by_language(language, self.__handled_args.get(key))
        return result

    def handled_params_by_language(self, language):
        result = {}
        for key in self.__handled_params.keys():
            result[key] = self.__read_value_by_language(language, self.__handled_params.get(key))
        return result

    def description_by_language(self, language):
        return self.__read_value_by_language(language, self.__description)

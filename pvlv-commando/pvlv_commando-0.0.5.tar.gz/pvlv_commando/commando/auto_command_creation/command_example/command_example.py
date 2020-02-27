class CommandName(object):

    def __init__(self, bot, language, command, arg, params):

        self.bot = bot  # bot entity to send messages, the one that you pass on run command
        self.language = language  # the language detected in the guild, to personalize responses
        self.command = command  # the command descriptor of the command

        self.arg = arg  # the detected arg

        """
        parameters will be initialized here
        You have to reserve the vars here that you need to use
        in _vars must be the same name as handled_params in the config json but without dash (-) 
        """
        self._param1 = None  # the detected parameters
        self._param2 = None

        for param in params:  # read the parameter from the params dict and save them in vars over here
            name = '_{}'.format(param[0])
            setattr(self, name, param[1])

    def run(self):
        print('Command has been run arg: {}'.format(self.arg))

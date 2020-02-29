import os


class StartCommand(object):

    def __init__(self, module_name, command_name):
        self.__module_name = module_name
        self.__command_name = command_name

        # the base directory folder of the command
        self.command_dir = 'commands/{}/{}'.format(module_name, command_name)
        self.__create_if_not_exist(self.command_dir)

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
    def __create_if_not_exist(directory):
        if not os.path.exists(os.path.dirname(directory)):
            os.makedirs(os.path.dirname(directory))

    def __copy_files(self, extension):
        file_creation_dir = '{}/{}.{}'.format(self.command_dir, self.__command_name, extension)
        full_copy_path = os.path.dirname(__file__)
        file_copy_dir = '{}/command_example/command_example.{}'.format(full_copy_path, extension)

        """
        Try to open the file, if the file do not exist create it.
        Copy the content form a default file
        Replace the class name with the right name
        """
        try:
            open(file_creation_dir)
        except FileNotFoundError:
            with open(file_creation_dir, "w") as f1:
                with open(file_copy_dir, "r") as f2:
                    f1.write(f2.read().replace('CommandName', self.__build_class_name(self.__command_name)))

    def create(self):

        translations_dir = '{}/{}/'.format(self.command_dir, 'translations')
        modules_dir = '{}/{}/'.format(self.command_dir, 'modules')
        self.__create_if_not_exist(translations_dir)
        self.__create_if_not_exist(modules_dir)

        self.__copy_files('json')
        self.__copy_files('py')

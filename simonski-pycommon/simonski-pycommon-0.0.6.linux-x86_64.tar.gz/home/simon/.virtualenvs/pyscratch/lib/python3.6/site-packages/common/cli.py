import os
import sys
import time
import socket
import struct
import sys
import uuid


class CLIMissingKeyError(BaseException):
    def __init__(self, *args, **kwargs):
        super(CLIMissingKeyError, self).__init__(args, kwargs)


class CLI:
    def __init__(self, argv=sys.argv):
        self.argv = argv

    def get_command(self) -> str:
        if len(self.argv) > 1:
            return self.argv[1]
        else:
            return None

    @staticmethod
    def read(prompt):
        return input(prompt)

    def index_of(self, key) -> int:
        index = 0
        while index < len(self.argv):
            if self.argv[index] == key:
                return index
            index += 1
        return -1

    def contains(self, key) -> bool:
        return self.index_of(key) > -1

    def get_or_die(self, key, error_message=None) -> str:
        v = self.get_or_default(key, None)
        if v is None:
            if error_message is None:
                print("Error, '" + key + "' is required.")
            else:
                print(error_message)

            sys.exit(1)
        else:
            return v

    def get_or_raise(self, key: str, error_message: str = None) -> str:
        """
        Requires a key/value or prints the error and raises a CLIMissingKeyError
        :param key:
        :param error_message:
        :return:
        """
        v = self.get_or_default(key, None)
        if v is None:
            if error_message is None:
                print("Error, '" + key + "' is required.")
            else:
                print(error_message)
            raise CLIMissingKeyError(error_message)

        else:
            return v

    def get_or_default(self, key, default_value) -> str:
        index = self.index_of(key)
        if index == -1:
            return default_value
        else:
            if index + 1 < len(self.argv):
                return self.argv[index + 1]
            else:
                # means we have the key (e.g -f) but not hte value (e.g. -f filename)
                #  (missing filename)
                return default_value

    def get_existing_filename_or_die(self, key) -> str:
        """
        returns the filename specified by the key, or dies
        """
        filename = self.get_or_default(key, None)
        if filename is None:
            print("Error, '" + key + "' is required.")
            sys.exit(1)
        elif not os.path.isfile(filename):
            print("'" + str(filename) + "' is not a file.")
            sys.exit(1)
        else:
            return filename


class Application:
    """

    An example app would be

    class App(Application):
        def __init__(self)
            self.__init__(prompt="foo")

        def on_command(self, args):
            print("command")

        def help_command(self, args):
            return "I am the help"

    app.process()
    or

    """

    def __init__(self, prompt=None):
        self.QUIT = False  #  when True, will quit the interactive mode
        if prompt is None:
            self.prompt = "> "
        else:
            self.prompt = prompt

    def set_prompt(self, prompt):
        self.prompt = prompt

    def get_prompt(self):
        return self.prompt

    @staticmethod
    def get_command_from_user_input(user_input):
        if len(user_input) > 1:
            command = user_input[1]
            remainder = user_input[2:]
        else:
            command = None
            remainder = None
        return command, remainder

    def get_func_or_none(self, fn_name):
        try:
            attr = getattr(self, fn_name)
            return attr
        except Exception as e:
            return None

    def process_interactive(self):
        quit = False
        while not self.QUIT:
            user_input = CLI.read(prompt=self.get_prompt())
            self.process(user_input)

    def process_line(self, user_input=None):
        command, remainder = self.get_command_from_user_input(user_input)
        if command is None:
            return self.on_usage()

        fn_name = "on_" + command.lower().replace("-", "_")

        # todo if the command is `help`, find the on_function_help and return that
        # OR is all that just rubbish and we should hard code and not be clever.. I never know.
        try:
            attr = self.get_func_or_none(fn_name)
            if attr is None:
                print("I don't know how to %s" % command)
                return False
            else:
                try:
                    return attr(command, remainder)
                except Exception as e:
                    print("Problem calling function '" + fn_name + "'")
                    print(e)
                    return False
        except Exception:
            print("Exception")

    def on_q(self, command=None, user_input=None):
        self.on_quit(user_input)

    def on_quit(self, command=None, user_input=None):
        self.QUIT = True

    def on_usage(self):
        print("Usage: TODO, implement 'on_usage' in your subclass.")
        return False

    def main(self):
        args = sys.argv
        if len(args) == 0:
            # no command, go interactive
            self.process_interactive()
        else:
            # supplied a command, execute and complete
            self.process_line(sys.argv)


class DemoApplication(Application):
    def __init__(self, prompt):
        super(DemoApplication, self).__init__(prompt=prompt)

    def on_anything(self, command: str, user_input: str):
        print("anything!")


if __name__ == "__main__":
    c = CLI()
    prompt = c.get_or_default("-prompt", "> ")
    app = DemoApplication(prompt)
    app.main()

from commands import Command, CommandFactory, register_command


class MyCommand(Command):
    def _validate(self):
        return True

    def _execute(self):
        pass


def test_register_command(command_request_data):
    register_command(command_request_data["command"])(MyCommand)
    command = CommandFactory.make_command(command_request_data)
    assert isinstance(command, MyCommand)

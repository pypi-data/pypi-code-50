import pytest

from commands import Command, CommandError, CommandFactory


class MyCommand(Command):
    def _validate(self):
        return True

    def _execute(self):
        pass


class TestCommandFactory:
    @pytest.fixture(autouse=True)
    def reset_registered_commands(self):
        CommandFactory._registered_commands = {}

    def test_make_command(self, command_request_data):
        CommandFactory.register_command(command_request_data["command"], MyCommand)
        command = CommandFactory.make_command(command_request_data)
        assert isinstance(command, MyCommand)

    def test_make_command__no_registered_command(self, command_request_data):
        with pytest.raises(CommandError):
            CommandFactory.make_command(command_request_data)

    def test_register_command__already_registered(self):
        CommandFactory.register_command("/mycommand", MyCommand)
        with pytest.raises(CommandError) as e:
            CommandFactory.register_command("/mycommand", MyCommand)

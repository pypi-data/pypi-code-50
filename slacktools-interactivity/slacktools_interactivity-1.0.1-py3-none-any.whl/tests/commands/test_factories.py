from interactivity import CommandFactory, CommandHandler


class MyCommand(CommandHandler):
    def _validate(self):
        return True

    def _execute(self):
        pass


class TestCommandFactory:
    def test(self, command_request_data):
        CommandFactory.register_handler(command_request_data["command"], MyCommand)
        handler = CommandFactory.make_handler(command_request_data)
        assert isinstance(handler, MyCommand)

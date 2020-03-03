from ..util.Logger import classLogger

class MissingOption(Exception):
    pass

@classLogger
class Optionizable:
    options = {}

    def __init__(self, options={}):
        self.options = options

    def getOption(self, name):
        if (not name in self.options):
            raise MissingOption("The option '" + name + "' is missing")

        return self.options[name]

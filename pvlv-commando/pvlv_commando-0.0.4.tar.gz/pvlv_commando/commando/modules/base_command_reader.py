class BaseCommandReader(object):

    def __init__(self):
        self.module = None  # the module where is member of
        self.name = None  # the name of the command

        self.invocation_words = []
        self._description = {}
        self.examples = ''

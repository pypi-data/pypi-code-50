class InvalidParamError(Exception):
    def __init__(self, param):
        self._param = param

    def __str__(self):
        return "Invalid parameter `{}`".format(self._param)


class TrellogyError(Exception):
    def __init__(self, message):
        self._message = message

    def __str__(self):
        return self._message


class NotEnoughParamsError(Exception):
    def __init__(self, key):
        self._key = key

    def __str__(self):
        return "Value for the key `{}` was not given.".format(self._key)

# Date: 22/09/2019 05:40
# Author: MaximRaduntsev

from dynaconf import settings


class MaxLongUsernameError(Exception):
    """
    Поле длинее, чем нужно
    """

    def __init__(self, name):
        """
        Ошибка длинного имени
        """
        self.name = name

    def __str__(self):
        """
        :return: str (Сообщение об ошибке)
        """
        return 'Name {} is too long: {} symbols, maximum allowed is {}'.format(
            self.name, len(self.name), settings.MAX_USERNAME_LENGTH)


class UnknownServerError(Exception):
    """
    Исключение - ошибка сервера
    """

    def __init__(self, text):
        self.text = text

    def __str__(self):
        return 'Unknown type of message: {}'.format(self.text)


class ResponseCodeError(Exception):
    """
    Исключение - ответ отсутствует среди списка ответов
    """

    def __init__(self, code):
        self.code = code

    def __str__(self):
        return 'Wrong response code: {}'.format(self.code)


class WrongActionError(Exception):
    """
    Неверное действие
    """

    def __init__(self, action):
        self.action = action

    def __str__(self):
        return 'Wrong action: {}'.format(self.action)


class MandatoryKeyError(Exception):
    def __init__(self, key):
        self.key = key

    def __str__(self):
        return 'Не хватает обязательного атрибута {}'.format(self.key)

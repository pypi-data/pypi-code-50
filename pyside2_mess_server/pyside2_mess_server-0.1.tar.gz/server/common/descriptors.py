#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from jim.errors import MaxLongUsernameError
from common.host_ping import host_ping
from log.client_log_config import logger
from dynaconf import settings


class AddressField:
    """
    Дескриптор для сокета
    """

    def __init__(self):
        super().__init__()
        self._addr = None
        self._port = None

    def __set__(self, instance, value):
        addr, port = value

        if not host_ping(addr):
            logger.critical(f'{addr}, Не верные параметры узла')
            raise ValueError(f'{addr}, Не верные параметры узла')

        if isinstance(port, int) and 1023 < port < 65537:
            self._port = port
        else:
            logger.critical('Порт должен быть от 1024 до 65536')
            raise ValueError('Порт должен быть от 1024 до 65536')

        instance.__dict__[self.name] = value

    def __set_name__(self, owner, name):
        # owner - <class '__main__.client'>
        # name - __name
        self.name = name


class ModeField:
    """
    Дескриптор выбора режима
    """

    def __init__(self, mode='r'):
        super().__init__()
        self._mode = mode

    def __set__(self, instance, value):
        # value - выбранный режим работы клиента
        # Проверим допустим ли выбранный режим работы клиента
        if value not in ('r', 'w'):
            logger.critical(f'Указан недопустимый режим работы {value}, '
                            f'допустимые режимы: r - чтение, w - запись')
            exit(1)

        instance.__dict__[self.name] = value

    def __set_name__(self, owner, name):
        # owner - <class '__main__.Server'>
        # name - mode
        self.name = name

    def __get__(self, inst, inst_type=None):
        return self._mode


class LoginField:
    """
    Дескриптор имени клиента
    """

    def __set__(self, instance, value):

        if len(value) > settings.MAX_USERNAME_LENGTH:
            logger.critical(
                f'Имя больше {settings.MAX_USERNAME_LENGTH} символов')
            raise MaxLongUsernameError(value)

        if not isinstance(value, str):
            logger.critical(f'Имя {value} не строка')
            raise TypeError

        instance.__dict__[self.name] = value

    def __set_name__(self, owner, name):
        # owner - <class '__main__.client'>
        # name - __name
        self.name = name


class MaxLengthField:
    """Дескриптор ограничивающий размер поля"""

    def __init__(self, name, max_length):
        """
        :param name: имя поля
        :param max_length: максимальная длина
        """
        self.max_length = max_length
        self.name = '_' + name

    def __set__(self, instance, value):
        # если длина поля больше максимального значения
        if len(value) > self.max_length:
            # вызываем ошибку
            raise MaxLongUsernameError(self.name)
        # иначе записываем данные в поле
        setattr(instance, self.name, value)

    def __get__(self, instance, owner):
        # получаем данные поля
        return getattr(instance, self.name)

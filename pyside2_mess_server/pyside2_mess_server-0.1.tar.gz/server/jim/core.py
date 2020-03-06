#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date: 11.12.2019 21:19
# @Author: MaximRaduntsev

"""Утилиты для работы с протоколом."""

import time
from dynaconf import settings


class Message:
    """
    Класс сообщения. Отдает свои атрибуты как ключи из данных и без генерации
    ошибок
    """

    def __init__(self, data=None, **kwargs):
        if data:
            if isinstance(data, dict):
                data.update(kwargs)
            kwargs = data
        self.__raw = kwargs
        date_format = kwargs.pop('date_format', '%Y-%m-%d %H:%M:%S')
        self.__raw[settings.TIME] = time.strftime(date_format)

    def __str__(self):
        return str(self.__raw)

    @property
    def to_dict(self):
        """Словарь с данными"""
        return self.__raw

    @property
    def action(self):
        """Действие"""
        return self.__raw.get(settings.ACTION)

    @property
    def response(self):
        """Код ответа"""
        return self.__raw.get(settings.RESPONSE)

    @property
    def user(self):
        """Информация о клиенте"""
        try:
            return self.__raw[settings.USER].get(settings.ACCOUNT_NAME)
        except ValueError:
            return None
        except Exception:
            data = (settings.USER, settings.ACCOUNT_NAME,
                    settings.SENDER, settings.DESTINATION)
            for d in data:
                name = self.__raw.get(d)
                if name:
                    # print('name = ', name)
                    return name

    @property
    def public_key(self):
        """Ключ"""
        return self.__raw[settings.USER].get(settings.PUBLIC_KEY)

    @property
    def destination(self):
        """Получатель"""
        return self.__raw.get(settings.DESTINATION)

    @property
    def sender(self):
        """Отправитель"""
        return self.__raw.get(settings.SENDER)

    @property
    def error(self):
        return self.__raw.get(settings.ERROR)

    @property
    def text(self):
        """Переданный текст"""
        return self.__raw.get(settings.MESSAGE_TEXT)

    @classmethod
    def error_resp(cls, text, **kwargs):
        """
        Ошибка запроса пользователя
        """
        return cls(response=settings.BAD_REQUEST, error=text, **kwargs)

    @classmethod
    def error_request(cls, text, **kwargs):
        """
        Ошибка.
        """
        return cls(action=settings.ERROR, msg=text, **kwargs)

    @classmethod
    def success(cls, response=settings.OK, **kwargs):
        """
        Сообщение об успехе.
        """
        return cls(response=response, **kwargs)

    @classmethod
    def accepted(cls, response=settings.ACCEPTED, **kwargs):
        """
        Сообщение о разрешении действия.
        """
        return cls(response=response, **kwargs)

    @classmethod
    def forbidden(cls, response=settings.BAD_REQUEST, **kwargs):
        """
        Сообщение о запрете действия
        """
        return cls(response=response, **kwargs)

    @classmethod
    def presence(cls, logger, account_name, status, pubkey, **kwargs):
        """
        Презентационное сообщение
        """
        if status:
            user_name = {settings.ACCOUNT_NAME: account_name}
            # settings.STATUS: status}
            message = {settings.ACTION: settings.PRESENCE,
                       settings.STATUS: status,
                       settings.USER: user_name}
        else:
            user_name = {settings.ACCOUNT_NAME: account_name,
                         settings.PUBLIC_KEY: pubkey
                         }
            message = {settings.ACTION: settings.PRESENCE,
                       settings.USER: user_name or settings.ACCOUNT_NAME,
                       }
        info_msg = f'Сформировано {message} сообщение для ' \
                   f'пользователя {account_name}'
        logger.info(info_msg)
        return cls(message, **kwargs)

    @classmethod
    def exit_message(cls, logger, user=None, **kwargs):
        """
        Завершение сеанса
        """
        info_msg = 'Завершение работы по команде пользователя.'
        logger.info(info_msg)
        return cls(
            action=settings.QUIT,
            account_name=user or settings.ACCOUNT_NAME,
            **kwargs)


if __name__ == "__main__":
    print(settings.RESPONSE_OK)

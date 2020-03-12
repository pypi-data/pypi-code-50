# -*- coding: utf-8 -*-

"""

    Функции форматирования ошибок

"""
# встроенные модули
from typing import Tuple

ErrCode = Tuple[int, str]


def invalid_format(message: str = '') -> ErrCode:
    return -32600, f'Неправильный формат запроса: {message}.'


def empty_request(message: str = '') -> ErrCode:
    return -32601, 'Получен пустой запрос.'


def invalid_version(message: str = '') -> ErrCode:
    return -32602, 'Поддерживается только JSON-RPC 2.0.'


def no_method(message: str = '') -> ErrCode:
    return -32603, 'Не указан метод запроса.'


def unknown_method(message: str = '') -> ErrCode:
    return -32604, f'Неизвестный метод: "{message}".'


def no_arguments(message: str = '') -> ErrCode:
    return -32605, 'Не указаны аргументы вызова.'


def wrong_arguments_type(message: str = '') -> ErrCode:
    return -32606, 'Неправильно оформлены аргументы вызова метода.'


def no_secret_key(message: str = '') -> ErrCode:
    return -32607, 'Не предоставлен ключ авторизации.'


def internal_error(message: str = '') -> ErrCode:
    return -32608, 'Произошёл сбой при попытке обработать запрос.'


def not_found(message: str = '') -> ErrCode:
    return -32609, 'Данные по запросу не найдены.'


def access_denied(message: str = '') -> ErrCode:
    return -32602, 'Отказано в доступе.'

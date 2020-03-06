# Date: 02.12.2019 20:36
# Author: MaximRaduntsev

import argparse
from dynaconf import settings


def create_parser(client=True):
    """
    Функция парсинга ключей. Парсер аргументов командной строки, возвращает кортеж из
    4 элементов: адрес сервера, порт, имя пользователя, пароль.
    Выполняет проверку на корректность номера порта.
    :return: список ключей
    """
    ip = settings.DEFAULT_CLIENT_IP if client else settings.DEFAULT_SERVER_IP

    parser = argparse.ArgumentParser()

    parser.add_argument(
        'ip',
        default=ip,
        type=str,
        nargs='?',
        help=f'Задать IP адресс, по умолчанию {ip}')
    parser.add_argument(
        'port',
        default=settings.DEFAULT_PORT,
        type=int,
        nargs='?',
        help=f'Установить PORT, по умолчанию {settings.DEFAULT_PORT}')
    parser.add_argument('name', default=None, type=str, nargs='?')
    parser.add_argument('password', default='', nargs='?')
    parser.add_argument('no_gui', action='store_true')

    return parser

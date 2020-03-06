import time
import traceback
from functools import wraps
from socket import socket

from log.client_log_config import *
from dynaconf import settings


class Log:
    """
    Декоратор логирования
    """
    __slots__ = 'params'

    def __init__(self, params):
        self.params = params

    def __call__(self, func):
        @wraps(func)
        def decorated(*args, **kwargs):
            result = func(*args, *kwargs)
            # сообщение в лог
            message = f'{time.asctime()} Вызван декоратор {Log.__name__} для {func.__name__}'
            if args:
                message += '\targs: {}'.format(args)
            if kwargs:
                message += '\tkwargs: {}'.format(kwargs)
            if result:
                message += '\tРезультат = {}'.format(result)

            message += f' из функции {traceback.format_stack()[0].strip().split()[-1]}'

            if self.params:
                # logger.debug(
                #     f'Была вызвана функция {func.__name__} c параметрами {args} , {kwargs}. ')
                self.params.info(message)
            return result

        return decorated


# @Log(logger)
# def simple_func(a=2, v=4):
#     print(f'Тестовая функция, {a, v}')
#     return a + v


# Функция проверки, что клиент авторизован на сервере
# Проверяет, что передаваемый объект сокета находится в списке клиентов. Если его там нет закрывает сокет
def login_required(func):
    """
    Функция проверки, что клиент авторизован на сервере.
    Проверяет, что передаваемый объект сокета находится в списке клиентов.
    Если его там нет закрывает сокет
    :param func:
    :return:
    """
    def checker(*args, **kwargs):
        # Если первый аргумент - экземпляр Server
        # А сокет в остальных аргументах
        # Импортить необходимо тут, иначе ошибка рекурсивного импорта.
        from server import Server
        if isinstance(args[0], Server):
            found = False
            for arg in args:
                if isinstance(arg, socket):
                    # Проверяем, что данный сокет есть в списке names класса MessageProcessor
                    for client in args[0].names:
                        if args[0].names[client] == arg:
                            found = True

            # Теперь надо проверить, что передаваемые аргументы не presence сообщение
            for arg in args:
                if isinstance(arg, dict):
                    if settings.ACTION in arg and arg[settings.ACTION] == settings.PRESENCE:
                        found = True
            # Если не не авторизован и не сообщение начала авторизации, то вызываем исключение.
            if not found:
                raise TypeError

        return func(*args, **kwargs)

    return checker


def main():
    # Очистим все обработчики событий
    logger.handlers = []

    # Создадим обработчит только для этого модуля
    fh = logging.FileHandler('log_storage/app.main.log', encoding='utf-8')
    fh.setLevel(logging.INFO)
    fh.setFormatter(formatter)
    logger.addHandler(fh)

    print("Запущен внутренний модуль логирования")
    # simple_func()


if __name__ == '__main__':
    main()

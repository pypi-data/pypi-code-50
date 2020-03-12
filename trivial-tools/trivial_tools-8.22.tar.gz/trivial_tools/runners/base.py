# -*- coding: utf-8 -*-
"""

    Инструменты запуска

"""
# встроенные модули
import time
from datetime import datetime
from functools import wraps
from typing import Callable, Union, Tuple, Any, Optional

# сторонние модули
from loguru import logger

# модули проекта
from trivial_tools.special.special import fail


def repeat_on_exceptions(repeats: int, case: Union[Exception, Tuple[Exception]],
                         delay: float = 1.0, verbose: bool = True) -> Callable:
    """Декоратор, заставляющий функцию повторить операцию при выбросе исключения.

    Инструмент добавлен для возможности повторной отправки HTTP запросов на серверах

    :param verbose: логгировать произошедшие исключения и выводить их на экран
    :param delay: время ожидания между попытками
    :param repeats: сколько раз повторить (0 - повторять бесконечно)
    :param case: при каком исключении вызывать повтор
    :return: возвращает фабрику декораторов
    """

    def decorator(func: Callable) -> Callable:
        """
        Декоратор
        """

        @wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            """
            Враппер
            """
            iteration = 0
            while True:
                try:
                    result = func(*args, **kwargs)
                    break
                except case as exc:
                    iteration += 1

                    if verbose:
                        logger.warning(f'{exc} в функции {func.__name__}'
                                       f' (итерация {iteration})')

                    if repeats and iteration > repeats:
                        fail(exc)

                    time.sleep(delay)

            return result

        return wrapper

    return decorator


def capture_exception_output(title: str) -> Optional[str]:
    """
    Перехватить описание ошибки из loguru
    """
    storage = []
    sink_id = logger.add(sink=lambda msg: storage.append(msg))
    logger.exception(title)
    logger.remove(sink_id)
    return storage[0] if storage else None


def _execute(config, handler: Callable, separator: str, given_logger) -> str:
    """
    Исполнить с логгированием
    """
    given_logger.add(
        config.LOGGER_FILENAME,
        level=config.LOGGER_LEVEL,
        rotation=config.LOGGER_ROTATION
    )
    given_logger.warning(separator)
    given_logger.info(config.START_MESSAGE)
    given_logger.info(config)

    # @@@@@@@@@@@@@@@@@@@@
    message = handler()
    # @@@@@@@@@@@@@@@@@@@@

    given_logger.info(message)
    return message


def init_daemon(config,
                given_logger,
                handler: Callable,
                complete_callback: Callable,
                post_mortem_callback: Callable,
                infinite: bool = False) -> None:
    """Стартовать скрипт с выбранными настройками.

    :param given_logger: сущность для логгирования вызовов
    :param complete_callback: вызвать по окончании
    :param post_mortem_callback: вызвать при выпадении исключения
    :param config: класс, атрибуты которого являются нашими настрояками
    :param handler: рабочая функция скрпта, которая будет выполнять всю полезную работу
    :param infinite: флаг бесконечного перезапуска скрипта при выбросе исключения
    """
    separator = '#' * 79

    while True:
        normal_stop = False
        time_start = datetime.now()

        # noinspection PyBroadException
        try:
            message = _execute(config, handler, separator, given_logger)

            if message == '<stop>':
                if config.DEBUG:
                    given_logger.warning('Остановка по команде скрипта')
                normal_stop = True
                break

        except KeyboardInterrupt:
            if config.DEBUG:
                given_logger.warning('Остановка по команде с клавиатуры')
            normal_stop = True
            break

        except Exception as err:
            post_mortem_callback(err)

        if not infinite:
            break

    duration = int((datetime.now() - time_start).total_seconds())
    complete_callback(duration, normal_stop)
    given_logger.warning(separator)

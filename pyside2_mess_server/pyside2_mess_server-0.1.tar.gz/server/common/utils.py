# Date: 20/09/2019 01:15
# Author: MaximRaduntsev

from dynaconf import settings
from datetime import datetime
import json

from common.decos import Log
from log.client_log_config import logger
log = Log(logger)


def write_bytes(dict_msg):
    """
    Функция принимает словарь, преобразует его в JSON-объект и кодирует объект в байты
    :param dict_msg: dict (Словарь с данными)
    :return: bytes (Байтовое представление JSON-объекта)
    """
    if isinstance(dict_msg, dict):
        byte_message = json.dumps(dict_msg).encode(settings.BASE_ENCODING)
        return byte_message
    raise TypeError


def read_bytes(byte_msg):
    """
    Функция декодировщик байтов в словарь
    :param byte_msg: bytes (Байтовое представление JSON-объекта)
    :return: dict (Словарь с данными)
    """
    if isinstance(byte_msg, bytes):
        dict_message = json.loads(byte_msg.decode(settings.BASE_ENCODING))
        if isinstance(dict_message, dict):
            return dict_message
        raise TypeError
    raise TypeError


@log
def send_message(sock, message):
    """
    Функция отправки сообщения
    :param sock: socket (Объект сокета)
    :param message: dict (Словарь сообщения)
    :return: None
    """
    sock.send(write_bytes(message))


@log
def get_message(sock):
    """
    Функция приема сообщения
    :param sock: socket (Объект сокета)
    :return: dict (Словарь сообщения)
    """
    return read_bytes(sock.recv(settings.MAX_PACKAGE_LENGTH))


def get_time():
    """
    Функция возвращает текущее время
    :return: str (HH:MM:SS)
    """
    return datetime.now().strftime("%H:%M:%S")

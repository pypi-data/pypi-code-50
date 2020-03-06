#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date: 20/09/2019 01:10
# @Author: MaximRaduntsev

from ui.client_gui_settings import UserNameDialog
from client_gui import ClientMainWindow
from client_db.client_data_services import ClientDatabase
import json
import os
import sys
import time
from socket import socket, AF_INET, SOCK_STREAM
from threading import Thread, Lock

from Crypto.PublicKey import RSA

from common.metaclasses import ClientVerifier
from log.client_log_config import logger
from jim.errors import UnknownServerError
from common.decos import Log
from common.utils import send_message, get_message
from common.descriptors import AddressField, LoginField
from common.arg_parser import create_parser
from jim.core import Message as Obj

from PySide2.QtCore import QObject, Signal
from PySide2.QtWidgets import QApplication, QMessageBox

from dynaconf import settings
import hashlib
import hmac
import binascii

client_app = QApplication(sys.argv)

sys.path.append('../')
log = Log(logger)

# Объект блокировки сокета и работы с базой данных
sock_lock = Lock()
database_lock = Lock()
QObjectType = type(QObject)


class QMetaVerifier(QObjectType, ClientVerifier):
    """
    Класс отвечает за связь с сервером
    """
    pass


class Client(Thread, QObject, metaclass=QMetaVerifier):
    # Сигналы новое сообщение и потеря соединения
    new_message = Signal(dict)
    all_users_up = Signal()
    connection_lost = Signal()

    address = AddressField()
    account_name = LoginField()

    def __init__(self, address: (str, int), database, username, passwd, keys):
        """Инициализация."""
        super(Client, self).__init__()
        # https: // wiki.qt.io / Qt_for_Python_Signals_and_Slots

        # Вызываем конструктор предка
        Thread.__init__(self)
        QObject.__init__(self)

        # Класс База данных - работа с базой
        self.database = database
        # Сокет для работы с сервером
        self.sock = None

        # self.address = address
        # Имя пользователя
        self.account_name = username
        # Пароль
        self.password = passwd
        # Набор ключей для шифрования
        self.keys = keys

        # Устанавливаем соединение:
        self.connected(address)

        # Обновляем таблицы известных пользователей и контактов
        try:
            self.user_list_update()
            self.contacts_list_update()
        except OSError as err:
            if err.errno:
                logger.critical(f'Потеряно соединение с сервером.', err)
                raise UnknownServerError('Потеряно соединение с сервером!')
            logger.error(
                'Timeout соединения при обновлении списков пользователей.')
        except json.JSONDecodeError:
            logger.critical(f'Потеряно соединение с сервером.')
            raise UnknownServerError('Потеряно соединение с сервером!')
            # Флаг продолжения работы транспорта.
        self.running = True

    def connected(self, address):
        """
        Соединение с сервером.
        Функция открывает сокет клиента
        """
        # Создаем сокет для общения с сервером
        self.sock = socket(AF_INET, SOCK_STREAM)
        # Таймаут необходим для освобождения сокета.
        self.sock.settimeout(5)

        # Соединяемся, 5 попыток соединения, флаг успеха ставим в True если
        # удалось
        connected = False
        for i in range(5):
            logger.info(f'Попытка подключения №{i + 1}')
            try:
                self.sock.connect(address)
            except (ConnectionRefusedError, OSError) as e:
                critical_msg = f'Сервер отклонил запрос на подключение, {e}'
                logger.critical(critical_msg)
                continue
            else:
                connected = True
                break
            finally:
                time.sleep(1)
        # Если соединится не удалось - исключение
        if not connected:
            logger.critical('Не удалось установить соединение с сервером')
            raise UnknownServerError(
                'Не удалось установить соединение с сервером')

        logger.debug('Установлено соединение с сервером')

        # Запускаем процедуру авторизации
        # Получаем хэш пароля
        pass_bytes = self.password.encode('utf-8')
        salt = self.account_name.lower().encode('utf-8')
        passwd_hash = hashlib.pbkdf2_hmac('sha512', pass_bytes, salt, 10000)
        passwd_hash_string = binascii.hexlify(passwd_hash)

        # Получаем публичный ключ и декодируем его из байтов
        pubkey = self.keys.publickey().export_key().decode('ascii')

        # Авторизируемся на сервере
        with sock_lock:
            presence = Obj.presence(
                logger, self.account_name, None, pubkey).to_dict
            # Отправляем серверу приветственное сообщение.
            try:
                send_message(self.sock, presence)
                ans = get_message(self.sock)
                # Если сервер вернул ошибку, бросаем исключение.
                if settings.RESPONSE in ans:
                    if ans[settings.RESPONSE] == settings.BAD_REQUEST:
                        raise UnknownServerError(ans[settings.ERROR])
                    elif ans[settings.RESPONSE] == settings.NETWORK_AUTHENTICATION_REQUIRED:
                        # Если всё нормально, то продолжаем процедуру
                        # авторизации.
                        ans_data = ans[settings.DATA]
                        hash = hmac.new(
                            passwd_hash_string, ans_data.encode('utf8'))
                        digest = hash.digest()
                        my_ans = settings.RESPONSE_NET_AUTH_REQUIRED
                        my_ans[settings.DATA] = binascii.b2a_base64(
                            digest).decode('ansi')
                        send_message(self.sock, my_ans)
                        self.check_response(get_message(self.sock))
            except (OSError, json.JSONDecodeError):
                raise UnknownServerError(
                    'Сбой соединения в процессе авторизации.')

    # @staticmethod
    def check_response(self, response):
        """
        Функция проверки данных от сервера
        """
        message = Obj(response)

        logger.debug(f'Разбор сообщения от сервера: {response}')
        request_code = message.response

        # Если это подтверждение чего-либо
        if settings.RESPONSE in message.to_dict:
            if request_code == settings.OK:
                info_msg = 'Успешное подключение'
                logger.info(info_msg)
                return
            elif request_code == settings.BAD_REQUEST:
                info_400 = f'{settings.BAD_REQUEST} : {message.error}'
                logger.critical(info_400)
                raise UnknownServerError(info_400)
            elif request_code == settings.RESET_CONTENT:
                self.user_list_update()
                self.contacts_list_update()
                self.all_users_up.emit()
            else:
                logger.error(
                    f'Принят неизвестный код подтверждения {request_code}')

        # Если это сообщение от пользователя добавляем в базу, даём сигнал о
        # новом сообщении
        elif settings.ACTION in message.to_dict and message.action == settings.MESSAGE \
                and settings.SENDER in message.to_dict \
                and settings.DESTINATION in message.to_dict and settings.MESSAGE_TEXT \
                in message.to_dict \
                and message.destination == self.account_name:
            logger.debug(
                f'Получено сообщение от пользователя {message.sender}:{message.text}')
            self.new_message.emit(message.to_dict)

    def contacts_list_update(self):
        """Функция обновляющая контакт - лист с сервера"""
        logger.info(
            f'Запрос контакт листа для пользователся {self.account_name}')
        req = {
            settings.ACTION: settings.GET_CONTACTS,
            settings.USER: self.account_name
        }
        logger.info(f'Сформирован запрос {req}')
        with sock_lock:
            send_message(self.sock, req)
            ans = get_message(self.sock)
        logger.info(f'Получен ответ {ans}')
        if settings.RESPONSE in ans and ans[settings.RESPONSE] == settings.ACCEPTED:
            for contact in ans[settings.LIST_INFO]:
                self.database.add_contact(contact)
        else:
            logger.error('Не удалось обновить список контактов.')

    def user_list_update(self):
        """Функция обновления таблицы известных пользователей."""
        logger.info(
            f'Запрос списка известных пользователей {self.account_name}')
        req = {
            settings.ACTION: settings.USERS_REQUEST,
            settings.ACCOUNT_NAME: self.account_name
        }
        with sock_lock:
            send_message(self.sock, req)
            ans = get_message(self.sock)
        if settings.RESPONSE in ans and ans[settings.RESPONSE] == settings.ACCEPTED:
            self.database.add_users(ans[settings.LIST_INFO])
        else:
            logger.error('Не удалось обновить список известных пользователей.')

    def key_request(self, user):
        """Функция запроса открытого ключа клиента с сервера."""
        logger.debug(f'Запрос публичного ключа для {user}')
        req = {
            settings.ACTION: settings.PUBLIC_KEY_REQUEST,
            settings.ACCOUNT_NAME: user
        }
        with sock_lock:
            send_message(self.sock, req)
            ans = get_message(self.sock)
        if settings.RESPONSE in ans and ans[settings.RESPONSE] == \
                settings.NETWORK_AUTHENTICATION_REQUIRED:
            return ans[settings.DATA]
        else:
            logger.error(f'Не удалось получить ключ собеседника{user}.')

    def add_contact(self, contact):
        """Функция сообщающая на сервер о добавлении нового контакта"""
        logger.debug(f'Создание контакта {contact}')
        req = {
            settings.ACTION: settings.ADD_CONTACT,
            settings.USER: self.account_name,
            settings.ACCOUNT_NAME: contact
        }
        with sock_lock:
            send_message(self.sock, req)
            self.check_response(get_message(self.sock))

    def remove_contact(self, contact):
        """Функция удаления клиента на сервере"""
        logger.debug(f'Удаление контакта {contact}')
        req = {
            settings.ACTION: settings.DEL_CONTACT,
            settings.USER: self.account_name,
            settings.ACCOUNT_NAME: contact
        }
        with sock_lock:
            send_message(self.sock, req)
            self.check_response(get_message(self.sock))

    def transport_shutdown(self):
        """Функция закрытия соединения, отправляет сообщение о выходе."""
        self.running = False
        message = Obj.exit_message(logger, self.account_name).to_dict
        with sock_lock:
            try:
                send_message(self.sock, message)
            except OSError:
                pass
        logger.debug('Транспорт завершает работу.')
        time.sleep(0.5)

    def send_mess(self, to, message):
        """Функция отправки сообщения на сервер"""
        message_dict = {
            settings.ACTION: settings.MESSAGE,
            settings.SENDER: self.account_name,
            settings.DESTINATION: to,
            settings.MESSAGE_TEXT: message
        }
        logger.debug(f'Сформирован словарь сообщения: {message_dict}')

        # Необходимо дождаться освобождения сокета для отправки сообщения
        with sock_lock:
            send_message(self.sock, message_dict)
            self.check_response(get_message(self.sock))
            logger.info(f'Отправлено сообщение для пользователя {to}')

    def run(self):
        """
        Инициализация сокета и сообщение серверу о нашем появлении
        """
        logger.debug('Запущен процесс - приёмник собщений с сервера.')
        while self.running:
            # Отдыхаем секунду и снова пробуем захватить сокет.
            # если не сделать тут задержку, то второй поток может достаточно долго ждать
            # освобождения сокета.
            time.sleep(1)
            message = None
            with sock_lock:
                try:
                    self.sock.settimeout(0.5)
                    message = get_message(self.sock)
                except OSError as err:
                    if err.errno:
                        logger.critical(f'Потеряно соединение с сервером.')
                        self.running = False
                        self.connection_lost.emit()
                # Проблемы с соединением
                except (ConnectionError, ConnectionAbortedError,
                        ConnectionResetError, json.JSONDecodeError, TypeError):
                    logger.critical(f'Потеряно соединение с сервером.')
                    self.running = False
                    self.connection_lost.emit()
                finally:
                    self.sock.settimeout(5)

            # Если сообщение получено, то вызываем функцию обработчик:
            if message:
                logger.debug(f'Принято сообщение с сервера: {message}')
                self.check_response(message)


if __name__ == '__main__':
    # Загрузка параметров командной строки, если нет параметров, то задаём
    # значения по умолчанию.
    parser = create_parser()
    client_name = parser.parse_args().name
    client_passwd = parser.parse_args().password

    # Если имя пользователя не было указано в командной строке то запросим его
    if not client_name or not client_passwd:
        start_dialog = UserNameDialog()
        client_app.exec_()
        # Если пользователь ввёл имя и нажал ОК, то сохраняем ведённое и
        # удаляем объект, инааче выходим
        if start_dialog.ok_pressed:
            client_name = start_dialog.ui.name_ledit.text()
            client_passwd = start_dialog.ui.pass_ledit.text()
        else:
            exit(0)

    # Записываем логи
    logger.info(
        f'Запущен клиент с парамертами: адрес сервера: {parser.parse_args().ip},'
        f' порт: {parser.parse_args().port}, имя пользователя: {client_name}')

    # Загружаем ключи с файла, если же файла нет, то генерируем новую пару.
    dir_path = os.path.dirname(os.path.realpath(__file__))
    key_file = os.path.join(dir_path, f'keys\\{client_name}.key')
    if not os.path.exists(key_file):
        keys = RSA.generate(2048, os.urandom)
        with open(key_file, 'wb') as key:
            key.write(keys.export_key())
    else:
        with open(key_file, 'rb') as key:
            keys = RSA.import_key(key.read())

    keys.publickey().export_key()

    # Создаём объект базы данных
    database = ClientDatabase(client_name)
    # Создаём объект - транспорт и запускаем транспортный поток
    try:
        sock = Client(
            (parser.parse_args().ip,
             parser.parse_args().port),
            database,
            client_name,
            client_passwd,
            keys)
    except UnknownServerError as error:
        message = QMessageBox()
        message.critical(start_dialog, 'Ошибка сервера', error.text)
        exit(1)
    sock.setDaemon(True)
    sock.start()

    # Удалим объект диалога за ненадобностью
    del start_dialog

    # client_app = QApplication(sys.argv)

    # Создаём GUI
    main_window = ClientMainWindow(database, sock, keys)
    main_window.make_connection(sock)
    main_window.setWindowTitle(f'Чат Программа alpha release - {client_name}')
    client_app.exec_()
    del client_app

    # Раз графическая оболочка закрылась, закрываем транспорт
    sock.transport_shutdown()
    sock.join()

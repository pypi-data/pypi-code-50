# Date: 20/09/2019 01:23
# Author: MaximRaduntsev
import binascii
import hmac
import json
import os
import sys
import threading
import time
from socket import socket, AF_INET, SOCK_STREAM
import select

from common.arg_parser import create_parser
from common.descriptors import AddressField
from common.metaclasses import ServerVerifier
from common.utils import send_message, get_message
from server_db.server_data_services import ServerStorage
from jim.core import Message as Obj

from dynaconf import settings

from common.decos import Log, login_required
from log.server_log_config import logger

from PySide2.QtWidgets import QApplication, QTableWidgetItem
from PySide2.QtCore import Qt, QTimer
from ui.server_gui import Main

log = Log(logger)
# Флаг что был подключён новый пользователь, нужен чтобы не мучать BD постоянными
# запросами на обновление
new_connection = False
conflag_lock = threading.Lock()


class Server(threading.Thread, metaclass=ServerVerifier):
    address = AddressField()
    """
    Основной класс сервера. Принимает содинения, словари - пакеты
    от клиентов, обрабатывает поступающие сообщения.
    Работает в качестве отдельного потока.
    """
    def __init__(self, address: (str, int), database):
        super().__init__()
        # База данных сервера
        self.database = database

        self.sock = None
        self.address = address
        # Список подключённых клиентов.
        self.clients = []
        # Список сообщений на отправку.
        self.messages = []

        # Сокеты
        self.listen_sockets = None
        self.error_sockets = None

        # Флаг продолжения работы
        self.running = True

        # Словарь содержащий сопоставленные имена и соответствующие им сокеты.
        self.names = dict()

    def connected(self):
        """
        Функция открывает сокет сервера
        """
        transport = socket(AF_INET, SOCK_STREAM)
        transport.bind(self.address)
        transport.settimeout(0.5)

        # Начинаем слушать сокет.
        self.sock = transport
        self.sock.listen(settings.get('MAX_CONNECTIONS'))

        info_msg = f'Запущен сервер ip: {self.address[0]}, port: {self.address[1]}. ' \
                   f'Если адрес не указан, принимаются соединения с любых адресов'
        logger.info(info_msg)

    def process_message(self, request):
        """
        Функция адресной отправки сообщения определённому клиенту. Принимает словарь сообщение,
        список зарегистрированых пользователей и слушающие сокеты. Ничего не возвращает.
        """
        message = Obj(request)
        if message.destination in self.names and self.names[message.destination] \
                in self.listen_sockets:
            try:
                send_message(self.names[message.destination], message.to_dict)
                info_msg = f'Отправлено сообщение пользователю {message.destination} ' \
                           f'от пользователя {message.sender}'
                logger.info(info_msg)
            except OSError:
                self.remove_client(message.destination)
        elif message.destination in self.names and self.names[message.destination] not in \
                self.listen_sockets:
            logger.error(
                f'Связь с клиентом {message.destination} была потеряна. Соединение закрыто, '
                f'доставка невозможна.')
            self.remove_client(self.names[message.destination])
            # raise ConnectionError
        else:
            critical_msg = f'Пользователь {message.destination} не зарегистрирован ' \
                           f'на сервере, отправка сообщения невозможна'
            logger.critical(critical_msg)

    @login_required
    def run_action(self, request, client):
        """
        Обработчик сообщений от клиентов, принимает словарь - сообщение
        от клиента, проверяет корректность, отправляет словарь-ответ в
        случае необходимости.
        """
        message = Obj(request)
        logger.info(f'Разбор сообщения от клиента : {message.to_dict}')
        # Если это сообщение о присутствии, принимаем и отвечаем
        if settings.ACTION in message.to_dict and message.action == settings.PRESENCE and \
                settings.TIME in message.to_dict and settings.USER in message.to_dict:
            # Если такой пользователь ещё не зарегистрирован, регистрируем, иначе
            # отправляем ответ и завершаем соединение.
            self.authorize_user(message, client)

        # Если это сообщение, то добавляем его в очередь сообщений. Ответ не
        # требуется.
        elif settings.ACTION in message.to_dict and message.action == settings.MESSAGE and \
                settings.DESTINATION in message.to_dict and settings.TIME in message.to_dict and \
                settings.SENDER in message.to_dict and \
                settings.MESSAGE_TEXT in message.to_dict and \
                self.names[message.sender] == client:
            if message.destination in self.names:
                self.database.process_message(
                    message.sender, message.destination)
                self.process_message(message.to_dict)
                try:
                    send_message(client, Obj.success(settings.OK).to_dict)
                except OSError:
                    self.remove_client(client)
            else:
                response = 'Пользователь не зарегистрирован на сервере.'
                try:
                    send_message(client, Obj.error_resp(response).to_dict)
                except OSError:
                    pass
            return

        # Если это запрос контакт-листа
        elif settings.ACTION in message.to_dict and message.action == settings.GET_CONTACTS and \
                settings.USER in message.to_dict and self.names[message.user] == client:
            response = settings.RESPONSE_ACCEPTED
            response[settings.LIST_INFO] = self.database.get_contacts(
                message.user)
            send_message(client, response)

        # Если это добавление контакта
        elif settings.ACTION in message.to_dict and message.action == settings.ADD_CONTACT and \
                settings.ACCOUNT_NAME in message.to_dict and settings.USER in message.to_dict and \
                self.names[message.user] == client:
            self.database.add_contact(message.user,
                                      message.to_dict[settings.ACCOUNT_NAME])
            send_message(client, Obj.success(settings.OK).to_dict)

        # Если это удаление контакта
        elif settings.ACTION in message.to_dict and message.action == settings.DEL_CONTACT and \
                settings.ACCOUNT_NAME in message.to_dict and settings.USER in message.to_dict and \
                self.names[message.user] == client:
            self.database.remove_contact(
                message.user, message.to_dict[settings.ACCOUNT_NAME])
            send_message(client, Obj.success(settings.OK).to_dict)

        # Если это запрос известных пользователей
        elif settings.ACTION in message.to_dict and message.action == settings.USERS_REQUEST and \
                settings.ACCOUNT_NAME in message.to_dict and self.names[message.user] == client:
            response = settings.RESPONSE_ACCEPTED
            response[settings.LIST_INFO] = [user[0]
                                            for user in self.database.users_list()]
            send_message(client, response)

        # Если клиент выходит
        elif settings.ACTION in message.to_dict and message.action == settings.QUIT and \
                settings.ACCOUNT_NAME in message.to_dict and self.names[message.user] == client:
            self.remove_client(client)

            # Если это запрос публичного ключа пользователя
        elif settings.ACTION in message.to_dict and \
                message.action == settings.PUBLIC_KEY_REQUEST and \
                settings.ACCOUNT_NAME in message.to_dict:
            response = settings.RESPONSE_NET_AUTH_REQUIRED
            response[settings.DATA] = self.database.get_pubkey(message.user)
            # может быть, что ключа ещё нет (пользователь никогда не логинился,
            # тогда шлём 400)
            if response[settings.DATA]:
                try:
                    send_message(client, response)
                except OSError:
                    self.remove_client(client)
            else:
                error_msg = 'Нет публичного ключа для данного пользователя'
                try:
                    send_message(client, Obj.error_resp(error_msg).to_dict)
                except OSError:
                    self.remove_client(client)
        else:
            error_msg = 'Действие недоступно'
            try:
                send_message(client, Obj.error_resp(error_msg).to_dict)
                return logger.error(error_msg)
            except OSError:
                self.remove_client(client)

    def write_responses(self, w_clients):
        """
        Функция отправки ответа сервера клиентам, от которых были запросы
        """
        for sock in self.messages:
            try:
                self.process_message(sock, w_clients)
            except Exception as e:
                error_msg = f'Связь с клиентом с именем {sock.destination} была потеряна, {e}'
                logger.critical(error_msg)
                self.database.user_logout(sock.destination)
                self.clients.remove(self.names[sock.destination])
                del self.names[sock.destination]
        self.messages.clear()

    def run(self):
        """
        Запуск основного цикла
        :return:
        """
        # Готовим сокет
        self.connected()

        while self.running:
            try:
                # Ждём подключения, если таймаут вышел, ловим исключение.
                client, addr = self.sock.accept()
            except OSError:
                pass
            else:
                info_msg = f'Получен запрос на соединение от {addr}'
                logger.info(info_msg)
                self.clients.append(client)

            r = []
            w = []
            e = []
            # Проверяем на наличие ждущих клиентов
            try:
                if self.clients:
                    r, self.listen_sockets, self.error_sockets = \
                        select.select(self.clients, self.clients, [], 0)
            except OSError as err:
                logger.error(f'Ошибка работы с сокетами: {err.errno}')
            # принимаем сообщения и если ошибка, исключаем клиента.
            if r:
                for sock in r:
                    try:
                        self.run_action(get_message(sock), sock)
                    except (OSError, json.JSONDecodeError, TypeError):
                        self.remove_client(sock)

    def remove_client(self, client):
        """
        Функция обработчик клиента с которым потеряна связь
        ищет клиента в словаре клиентов и удаляет его со списков и базы:
        :param client:
        :return:
        """
        logger.info(f'Клиент {client.getpeername()} отключился от сервера.')
        for name in self.names:
            if self.names[name] == client:
                self.database.user_logout(name)
                del self.names[name]
                break
        self.clients.remove(client)
        client.close()
        logger.debug('closed')

    def authorize_user(self, message: Obj, sock):
        """
        Функция авторизации пользователя на сервере
        :param message:
        :param sock:
        :return:
        """
        # Если имя пользователя уже занято то возвращаем 400
        if message.user in self.names.keys():
            error_msg = 'Имя пользователя уже занято'
            try:
                send_message(sock, Obj.error_resp(error_msg).to_dict)
            except OSError:
                pass
            self.clients.remove(sock)
            sock.close()
        # Проверяем что пользователь зарегистрирован на сервере.
        elif not self.database.check_user(message.user):
            error_msg = 'Пользователь не зарегистрирован'
            try:
                send_message(sock, Obj.error_resp(error_msg).to_dict)
            except OSError:
                pass
            self.clients.remove(sock)
            sock.close()
        else:
            # Иначе отвечаем 501 и проводим процедуру авторизации
            # Словарь - заготовка
            message_auth = settings.RESPONSE_NET_AUTH_REQUIRED
            # Набор байтов в hex представлении
            random_str = binascii.hexlify(os.urandom(64))
            # В словарь байты нельзя, декодируем (json.dumps -> TypeError)
            message_auth[settings.DATA] = random_str.decode('ascii')
            # Создаём хэш пароля и связки с рандомной строкой, сохраняем
            # серверную версию ключа
            hash = hmac.new(self.database.get_hash(message.user), random_str)
            digest = hash.digest()
            try:
                # Обмен с клиентом
                send_message(sock, message_auth)
                ans = get_message(sock)
            except OSError:
                sock.close()
                return
            client_digest = binascii.a2b_base64(ans[settings.DATA])
            # Если ответ клиента корректный, то сохраняем его в список
            # пользователей.
            if settings.RESPONSE in ans and ans[settings.RESPONSE] == \
                    settings.NETWORK_AUTHENTICATION_REQUIRED and \
                    hmac.compare_digest(digest, client_digest):
                self.names[message.user] = sock
                client_ip, client_port = sock.getpeername()
                try:
                    send_message(sock, Obj.success(settings.OK).to_dict)
                except OSError:
                    self.remove_client(message.user)
                # добавляем пользователя в список активных и если у него изменился открытый ключ
                # сохраняем новый
                self.database.user_login(message.user,
                                         client_ip, client_port,
                                         message.public_key)
            else:
                error_msg = 'Неверный пароль'
                try:
                    send_message(sock, Obj.error_resp(error_msg).to_dict)
                except OSError:
                    pass
                self.clients.remove(sock)
                sock.close()

    def service_update_lists(self):
        """
        Функция - отправляет сервисное сообщение 205 с требованием
        клиентам обновить списки
        :return:
        """
        for client in self.names:
            try:
                send_message(
                    self.names[client],
                    settings.RESPONSE_RESET_CONTENT)
            except OSError:
                self.remove_client(self.names[client])


def main():
    # Загрузка параметров командной строки, если нет параметров, то задаём
    # значения по умолчанию.
    parser = create_parser(False)
    gui_flag = False
    # Инициализация базы данных
    db = ServerStorage()

    address = (parser.parse_args().ip, parser.parse_args().port)
    # gui_flag = parser.parse_args().no_gui

    server = Server(address, db)
    server.daemon = True
    server.start()
    time.sleep(0.1)

    # Если  указан параметр без GUI то запускаем простенький обработчик
    # консольного ввода
    if gui_flag:
        while True:
            command = input('Введите exit для завершения работы сервера.')
            if command == 'exit':
                # Если выход, то завршаем основной цикл сервера.
                server.running = False
                server.join()
                break

    # Если не указан запуск без GUI, то запускаем GUI:
    else:
        # Создаём графическое окуружение для сервера:
        server_app = QApplication(sys.argv)
        main_window = Main(db, server)

        def display_table(f, table):
            # table.setFont(QFont("Helvetica", 10))
            row = f()
            table.setRowCount(len(row))
            column_count = table.columnCount()

            for i, data in enumerate(row):
                for j in range(column_count):
                    item = QTableWidgetItem()
                    item.setFlags(Qt.ItemIsEnabled | Qt.ItemIsSelectable)
                    item.setText(str(data[j]))
                    table.setItem(i, j, item)

        display_table(db.message_history, main_window.history_user_table)

        # Функция обновляющяя список подключённых, проверяет флаг подключения,
        # и если надо обновляет список
        def list_update():
            display_table(db.active_users_list, main_window.active_user_table)

        timer = QTimer()
        timer.timeout.connect(list_update)
        timer.start(1000)  # trigger every 1 s.

        # Запускаем GUI
        server_app.exec_()


if __name__ == '__main__':
    main()

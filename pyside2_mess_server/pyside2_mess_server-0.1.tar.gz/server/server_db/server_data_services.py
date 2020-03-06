# -*- coding: utf-8 -*-
# Date: 04.12.2019
# Author: MaximRaduntsev

import datetime
from server_db.models.server_models import User, UserHistory, \
    ActiveUser, LoginHistory, Contact
from server_db.data import session_factory

from pathlib import Path
from dynaconf import settings


class ServerStorage:
    """
    Класс - серверная база данных
    """

    def __init__(self):
        # Создаём движок базы данных
        db_def_name = Path(settings.get('DATABASES.SERVER.NAME'))
        session_factory.global_init(db_def_name)
        session_factory.create_tables()
        self.session = session_factory.create_session()

        # Если в таблице активных пользователей есть записи, то их необходимо удалить
        # Когда устанавливаем соединение, очищаем таблицу активных
        # пользователей
        if self.session.query(ActiveUser).count() > 0:
            self.session.query(ActiveUser).delete()
            self.session.commit()

    def get_user_by_name(self, username):
        """Возвращает объект пользователя по его имени."""
        user = self.session.query(User).filter(User.name == username.lower())
        return user.first() if user.count() else None

    def get_id_by_name(self, username):
        """
        Check client_name exist in clients table
        :param username:
        :return: record id if exist, -1 otherwise
        """
        user = self.session.query(User).filter(User.name == username).first()
        if user:
            return user.id
        else:
            exit(1)

    def get_user_by_like(self, query):
        """Возвращает объект пользователя по его имени."""
        users = self.session.query(
            User.name,
            User.last_login,
            UserHistory.sent,
            UserHistory.accepted).filter(
            User.id == UserHistory.id,
            User.name.ilike(f'%{query}%'))
        return users.all()

    def user_modify(self, username, new_username):
        """
        Функция изменения данных пользователя
        :param username:
        :param new_username:
        :return:
        """
        self.session.query(User).filter(
            User.name == username).update({'name': new_username})
        self.session.commit()

    def user_login(self, username, ip_address, port, key):
        """
        Функция выполняющяяся при входе пользователя, записывает в базу факт входа
        :param username:
        :param ip_address:
        :param port:
        :param key:
        :return:
        """
        # print(username, ip_address, port)
        # Запрос в таблицу пользователей на наличие там пользователя с таким именем
        # client = self.find_by_name(username)
        user = self.get_user_by_name(username)
        # Если имя пользователя уже присутствует в таблице, обновляем время
        # последнего входа
        if user:
            user.last_login = datetime.datetime.now()
            if user.pubkey != key:
                user.pubkey = key
        # Если нет, то генерируем исключение
        else:
            raise ValueError('Пользователь не зарегистрирован.')

        # Теперь можно создать запись в таблицу активных пользователей о факте
        # входа.
        new_active_user = ActiveUser(
            user.id, ip_address, port, datetime.datetime.now())
        self.session.add(new_active_user)

        # и сохранить в историю входов
        history = LoginHistory(
            user.id,
            datetime.datetime.now(),
            ip_address,
            port)
        self.session.add(history)

        # Сохрраняем изменения
        self.session.commit()

    def add_user(self, name, pass_hash):
        """
        Функция регистрации пользователя. Принимает имя и хэш пароля,
        создаёт запись в таблице статистики.
        :param name:
        :param pass_hash:
        :return:
        """
        user_row = User(name, pass_hash)
        self.session.add(user_row)
        self.session.commit()
        history_row = UserHistory(user_row.id)
        self.session.add(history_row)
        self.session.commit()

    def remove_user(self, name):
        """
        Функция удаляющая пользователя из базы
        :param name:
        :return:
        """
        user = self.get_user_by_name(name)
        self.session.query(ActiveUser).filter_by(user=user.id).delete()
        self.session.query(LoginHistory).filter_by(name=user.id).delete()
        self.session.query(Contact).filter_by(user=user.id).delete()
        self.session.query(Contact).filter_by(contact=user.id).delete()
        self.session.query(UserHistory).filter_by(user=user.id).delete()
        self.session.query(User).filter_by(name=name).delete()
        self.session.commit()

    def get_hash(self, name):
        """
        Функция возвращает хэш требуемго пользователя.
        :param name:
        :return:
        """
        user = self.get_user_by_name(name)
        return user.pass_hash

    def get_pubkey(self, name):
        """
        Функция возвращает публичный ключ пользователя
        :param name:
        :return:
        """
        user = self.get_user_by_name(name)
        return user.pubkey

    def check_user(self, name):
        """
        Функция проверки пользователя
        :param name:
        :return:
        """
        user = self.get_user_by_name(name)
        if user:
            return True
        else:
            return False

    def user_logout(self, username):
        """
        Функция фиксирующая отключение пользователя
        :param username:
        :return:
        """
        # Запрашиваем пользователя, что покидает нас
        # получаем запись из таблицы AllUsers
        user = self.get_user_by_name(username)
        # Удаляем его из таблицы активных пользователей.
        # Удаляем запись из таблицы ActiveUsers
        self.session.query(ActiveUser).filter_by(user=user.id).delete()

        # Применяем изменения
        self.session.commit()

    def process_message(self, sender, recipient):
        """
        Функция фиксирует передачу сообщения и делает соответствующие отметки в БД
        :param sender:
        :param recipient:
        :return:
        """
        # Получаем ID отправителя и получателя
        sender = self.get_id_by_name(sender)
        recipient = self.get_id_by_name(recipient)

        sender_row = self.session.query(
            UserHistory).filter_by(user=sender).first()
        sender_row.sent += 1
        recipient_row = self.session.query(
            UserHistory).filter_by(user=recipient).first()
        recipient_row.accepted += 1
        self.session.commit()

    def add_contact(self, user, contact):
        """
        Функция добавляет контакт для пользователя.
        :param user:
        :param contact:
        :return:
        """
        # Получаем ID пользователей
        user = self.get_user_by_name(user)
        contact = self.get_user_by_name(contact)

        # Проверяем что не дубль и что контакт может существовать (полю
        # пользователь мы доверяем)
        if not contact or self.session.query(Contact).filter_by(
                user=user.id, contact=contact.id).count():
            return

        # Создаём объект и заносим его в базу
        contact_row = Contact(user.id, contact.id)
        self.session.add(contact_row)
        self.session.commit()

    def remove_contact(self, user, contact):
        """
        Функция удаляет контакт из базы данных
        :param user:
        :param contact:
        :return:
        """
        # Получаем ID пользователей
        user = self.get_user_by_name(user)
        contact = self.get_user_by_name(contact)

        # Проверяем что контакт может существовать (полю пользователь мы
        # доверяем)
        if not contact:
            return

        # Удаляем требуемое
        self.session.query(Contact).filter(
            Contact.user == user.id,
            Contact.contact == contact.id
        ).delete()
        self.session.commit()

    def users_list(self):
        """
        Функция возвращает список известных пользователей со временем последнего входа.
        :return:
        """
        query = self.session.query(
            User.name,
            User.last_login,
        )
        # Возвращаем список кортежей
        return query.all()

    # Функция возвращает список активных пользователей
    def active_users_list(self):
        """
        Функция возвращает список активных пользователей
        Запрашиваем соединение таблиц и собираем кортежи имя, адрес, порт, время.
        :return:
        """
        query = self.session.query(
            User.id,
            User.name,
            ActiveUser.ip_address,
            ActiveUser.port,
            ActiveUser.login_time
        ).join(User)
        # Возвращаем список кортежей
        return query.all()

    def login_history(self, username=None):
        """
        Функция возвращающая историю входов по пользователю или всем пользователям
        :param username:
        :return:
        """
        # Запрашиваем историю входа
        query = self.session.query(User.name,
                                   LoginHistory.ip,
                                   LoginHistory.port,
                                   LoginHistory.date_time
                                   ).join(User)
        # Если было указано имя пользователя, то фильтруем по нему
        if username:
            query = query.filter(User.name == username)
        return query.all()

    def get_contacts(self, username):
        """
        Функция возвращает список контактов пользователя.
        :param username:
        :return:
        """
        # Запрашивааем указанного пользователя
        user = self.session.query(User).filter_by(name=username).one()

        # Запрашиваем его список контактов
        query = self.session.query(Contact, User.name). \
            filter_by(user=user.id). \
            join(User, Contact.contact == User.id)

        # выбираем только имена пользователей и возвращаем их.
        return [contact[1] for contact in query.all()]

    def message_history(self):
        """
        Функция возвращает количество переданных и полученных сообщений
        :return:
        """
        query = self.session.query(
            User.name,
            User.last_login,
            UserHistory.sent,
            UserHistory.accepted
        ).join(User)
        # Возвращаем список кортежей
        return query.all()


# Отладка
if __name__ == '__main__':
    test_db = ServerStorage()
    # test_db.user_login('1111', '192.168.1.113', 8080)
    # test_db.user_login('McG', '192.168.1.113', 8081)
    # print(test_db.users_list())
    # print(test_db.active_users_list())
    # # test_db.user_logout('McG')
    # # print(test_db.login_history('re'))
    # # test_db.add_contact('test2', 'test1')
    # # test_db.add_contact('test1', 'test3')
    # # test_db.add_contact('test1', 'test6')
    # # test_db.remove_contact('test1', 'test3')
    # test_db.process_message('McG', '1111')
    # print(test_db.message_history())

    # print(test_db.get_user_by_like('dd'))
    # print(test_db.get_user_by_name('ddd'))

    test_db.user_modify('yuyuy', 'new2020')

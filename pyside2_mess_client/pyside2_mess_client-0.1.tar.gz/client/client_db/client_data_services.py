#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date: 07.12.2019 20:46
# @Author: MaximRaduntsev

import datetime
from pathlib import Path
from dynaconf import settings

from client_db.models.client_models import ActiveUsers, MessageHistory, Contact
from client_db.data import session_factory


class ClientDatabase:
    """
    Класс - база данных сервера
    """

    def __init__(self, name):
        """
        Конструктор класса:
        """
        db_settings = settings.get(f'DATABASES.CLIENT')
        db_name = Path(db_settings.get('NAME', '').format(**{'user': name}))
        session_factory.global_init(db_name)
        session_factory.create_tables()
        self.session = session_factory.create_session()

        # Необходимо очистить таблицу контактов, т.к. при запуске они
        # подгружаются с сервера.
        self.session.query(Contact).delete()
        self.session.commit()

    def add_contact(self, contact):
        """
        Функция добавления контактов
        """
        if not self.session.query(Contact).filter_by(name=contact).count():
            contact_row = Contact(contact)
            self.session.add(contact_row)
            self.session.commit()

    def contacts_clear(self):
        """
        Функция очистки контактов
        """
        self.session.query(Contact).delete()

    def del_contact(self, contact):
        """
        Функция удаления контакта
        """
        self.session.query(Contact).filter_by(name=contact).delete()
        self.session.commit()

    def add_users(self, users_list):
        """
        Функция добавления известных пользователей.
        Пользователи получаются только с сервера, поэтому таблица очищается.
        """
        self.session.query(ActiveUsers).delete()
        for user in users_list:
            user_row = ActiveUsers(user)
            self.session.add(user_row)
        self.session.commit()

    def save_message(self, from_user, to_user, message):
        """
        Функция сохраняющяя сообщения
        :param from_user:
        :param to_user:
        :param message:
        :return:
        """
        message_row = MessageHistory(from_user, to_user, message)
        self.session.add(message_row)
        self.session.commit()

    def get_contacts(self):
        """
        Функция возвращающяя контакты
        :return:
        """
        return [contact[0]
                for contact in self.session.query(Contact.name).all()]

    def get_users(self):
        """
        Функция возвращающяя список известных пользователей
        :return:
        """
        return [user[0]
                for user in self.session.query(ActiveUsers.username).all()]

    def check_user(self, user):
        """
        Функция проверяющяя наличие пользователя в известных
        :param user:
        :return:
        """
        if self.session.query(ActiveUsers).filter_by(username=user).count():
            return True
        else:
            return False

    def check_contact(self, contact):
        """
        Функция проверяющяя наличие пользователя контактах
        :param contact:
        :return:
        """
        if self.session.query(Contact).filter_by(name=contact).count():
            return True
        else:
            return False

    def get_history(self, contact):
        """
        Функция возвращающая историю переписки
        :param contact:
        :return:
        """
        query = self.session.query(MessageHistory).filter_by(from_user=contact)
        return [(history_row.from_user,
                 history_row.to_user,
                 history_row.message,
                 history_row.date) for history_row in query.all()]


# отладка
if __name__ == '__main__':
    test_db = ClientDatabase('test1')
    for i in ['test3', 'test4', 'test5']:
        test_db.add_contact(i)
    test_db.add_contact('test4')
    test_db.add_users(['test1', 'test2', 'test3', 'test4', 'test5'])
    test_db.save_message(
        'test1',
        'test2',
        f'Привет! я тестовое сообщение от {datetime.datetime.now()}!')
    test_db.save_message(
        'test2',
        'test1',
        f'Привет! я другое тестовое сообщение от {datetime.datetime.now()}!')
    print(test_db.get_contacts())
    print(test_db.get_users())
    print(test_db.check_user('test1'))
    print(test_db.check_user('test10'))
    print(test_db.get_history('test2'))
    print(test_db.get_history(to_who='test2'))
    print(test_db.get_history('test3'))
    test_db.del_contact('test4')
    print(test_db.get_contacts())

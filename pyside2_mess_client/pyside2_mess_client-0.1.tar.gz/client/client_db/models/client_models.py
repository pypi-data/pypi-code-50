#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date: 10.12.2019 13:07
# @Author: MaximRaduntsev

import datetime
from sqlalchemy import Column, Integer, String, DateTime, Text
from client_db.data.sqlalchemybase import SqlAlchemyBase


class ActiveUsers(SqlAlchemyBase):
    """
    Класс - отображение таблицы известных пользователей.
    """
    __tablename__ = 'active_users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String, unique=True, sqlite_on_conflict_unique='IGNORE')

    def __init__(self, user):
        self.id = None
        self.username = user


class MessageHistory(SqlAlchemyBase):
    """
    Класс - отображение таблицы истории сообщений
    """
    __tablename__ = 'message_history'
    id = Column(Integer, primary_key=True)
    from_user = Column(String)
    to_user = Column(String)
    message = Column(Text)
    date = Column(DateTime)

    def __init__(self, from_user, to_user, message):
        self.id = None
        self.from_user = from_user
        self.to_user = to_user
        self.message = message
        self.date = datetime.datetime.now()


class Contact(SqlAlchemyBase):
    """
    Класс - отображение списка контактов
    """
    __tablename__ = 'contact'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, unique=True, sqlite_on_conflict_unique='IGNORE')

    def __init__(self, contact):
        self.id = None
        self.name = contact

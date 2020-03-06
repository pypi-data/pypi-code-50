#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date: 09.12.2019 11:14
# @Author: MaximRaduntsev

import datetime
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, func, Text
from server_db.data.sqlalchemybase import SqlAlchemyBase


class User(SqlAlchemyBase):
    """Класс - отображение таблицы всех пользователей."""
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, unique=True, sqlite_on_conflict_unique='IGNORE')
    last_login = Column(String)
    pass_hash = Column(String)
    pubkey = Column(Text)

    def __init__(self, username, pass_hash):
        self.id = None
        self.name = username
        self.last_login = datetime.datetime.now()
        self.pass_hash = pass_hash
        self.pubkey = None


# Экземпляр этого класса = запись в таблице ActiveUsers
class ActiveUser(SqlAlchemyBase):
    """Класс - отображение таблицы активных пользователей."""
    __tablename__ = 'active_user'
    id = Column(Integer, primary_key=True, autoincrement=True)
    user = Column(ForeignKey('user.id'), unique=True, sqlite_on_conflict_unique='IGNORE')
    ip_address = Column(String)
    port = Column(Integer)
    login_time = Column(DateTime)

    def __init__(self, user_id, ip_address, port, login_time):
        self.id = None
        self.user = user_id
        self.ip_address = ip_address
        self.port = port
        self.login_time = login_time


# Экземпляр этого класса = запись в таблице LoginHistory
class LoginHistory(SqlAlchemyBase):
    """Класс - отображение таблицы истории входов."""
    __tablename__ = 'login_history'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(ForeignKey('user.id', ondelete='CASCADE'))
    date_time = Column(DateTime, default=func.now(), onupdate=func.utc_timestamp())
    ip = Column(String)
    port = Column(Integer)

    def __init__(self, name, date, ip, port):
        self.id = None
        self.name = name
        self.date_time = date
        self.ip = ip
        self.port = port


class Contact(SqlAlchemyBase):
    """Класс - отображение таблицы контактов пользователей."""
    __tablename__ = 'contact'
    id = Column(Integer, primary_key=True)
    user = Column(ForeignKey('user.id'))
    contact = Column(ForeignKey('user.id'))

    def __init__(self, user, contact):
        self.id = None
        self.user = user
        self.contact = contact


class UserHistory(SqlAlchemyBase):
    """Класс - отображение таблицы истории действий."""
    __tablename__ = 'history'
    id = Column(Integer, primary_key=True)
    user = Column(ForeignKey(User.id))
    sent = Column(Integer)
    accepted = Column(Integer)

    def __init__(self, user):
        self.id = None
        self.user = user
        self.sent = 0
        self.accepted = 0

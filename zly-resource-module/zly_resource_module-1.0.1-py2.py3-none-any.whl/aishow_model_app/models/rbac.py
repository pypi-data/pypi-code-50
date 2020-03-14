# -*- coding: utf-8 -*-
from sqlalchemy import String, Integer, DateTime, Column, ForeignKey

from aishowapp.ext import db
from aishowapp.models import BaseDef

user_role = db.Table('user_role',
    db.Column('user_id', db.Integer, db.ForeignKey('users.id')),
    db.Column('role_id', db.Integer, db.ForeignKey('roles.id'))
)
role_permission = db.Table('role_permission',
    db.Column('permission_id', db.Integer, db.ForeignKey('permissions.id')),
    db.Column('role_id', db.Integer, db.ForeignKey('roles.id'))
)

class User(db.Model,BaseDef):

    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    username = db.Column(String(255))
    password = db.Column(String(255))
    token = db.Column(String(255))
    likes = db.Column(String(255))
    avatar = db.Column(String(255))
    introduction = db.Column(String(255))
    sex = db.Column(String(255))
    roles = db.relationship('Role', secondary=user_role, backref=db.backref('users', lazy='dynamic'))
    usersearch_id = db.relationship("UserSearch", backref='user')

class UserSearch(db.Model,BaseDef):

    __tablename__ = 'usersearch'

    id = db.Column(db.Integer, primary_key=True,)
    count = db.Column(Integer)
    time = db.Column(DateTime)
    conditions = db.Column(String(255))
    user_id = Column(ForeignKey('users.id'))

class Role(db.Model,BaseDef):

    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    r_name=db.Column(db.String(255))
    permissions = db.relationship('Permission', secondary=role_permission, backref=db.backref('roles', lazy='dynamic'))

class Permission(db.Model,BaseDef):

    __tablename__ = 'permissions'
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    p_name=db.Column(db.String(255))
    p_url=db.Column(db.String(255))
from datetime import datetime

from sqlalchemy import (
    Column, Integer, String,
    DateTime, Text, ForeignKey,
    Boolean)
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from sqlalchemy.ext.declarative import declarative_base

from ifile.db.sqlalchemy.session import get_session

Base = declarative_base()
metadata = Base.metadata


class MetaBase(object):
    create_at = Column(DateTime(timezone=True), server_default=func.now())
    update_at = Column(DateTime(timezone=True), server_default=func.now())

    def save(self, session=None):
        if session is None:
            session = get_session()
            with session.begin():
                session.add(self)
        else:
            session.add(self)
            session.flush()

    def update(self, **kwargs):
        self.update_at = func.now()

        for k, v in kwargs.items():
            setattr(self, k, v)


class File(Base, MetaBase):
    __tablename__ = "file"

    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    uuid = Column(String(100))
    md5 = Column(String(100))
    size = Column(Integer)
    path = Column(String(500))


class Host(Base, MetaBase):
    __tablename__ = "host"

    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    ip = Column(String(100))
    role = Column(String(50))
    is_register = Column(Boolean)
    last_alive_time = Column(DateTime)

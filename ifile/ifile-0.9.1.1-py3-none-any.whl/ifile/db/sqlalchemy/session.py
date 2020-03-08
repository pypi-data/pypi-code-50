from functools import wraps

import sqlalchemy.orm
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from ifile import setting as conf


_ENGINE = None
_MAKER = None


class Error(Exception):
    pass


class DBError(Error):
    """Wraps an implementation specific exception."""
    def __init__(self, inner_exception=None):
        self.inner_exception = inner_exception
        super(DBError, self).__init__(str(inner_exception))


def wrap_db_error(f):
    @wraps(f)
    def _wrap(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except Exception as e:
            raise DBError(e)
    return _wrap


def get_session(autocommit=True, expire_on_commit=False):
    """Return a SQLAlchemy session."""
    global _MAKER

    if _MAKER is None:
        engine = get_engine()
        _MAKER = get_maker(engine, autocommit, expire_on_commit)

    session = _MAKER()
    session.query = wrap_db_error(session.query)
    session.flush = wrap_db_error(session.flush)
    return session


def get_engine():
    """
    Return a SQLAlchemy engine.

    engine args - pool_recycle:
        prevents the pool from using a particular connection
        that has passed a certain age, and is appropriate for
        database backends such as MySQl.
    """
    global _ENGINE
    if _ENGINE is None:

        engine_args = {
            "echo": False,
            "convert_unicode": True,
            "pool_recycle": 3600,
        }

        _ENGINE = sqlalchemy.create_engine(
            conf.SQLALCHEMY_DATABASE_URI, **engine_args)

        _ENGINE.connect()
    return _ENGINE


def get_maker(engine, autocommit=True, expire_on_commit=False):
    """Return a SQLAlchemy sessionmaker using the given engine."""
    return sqlalchemy.orm.sessionmaker(bind=engine,
                                       autocommit=autocommit,
                                       expire_on_commit=expire_on_commit)

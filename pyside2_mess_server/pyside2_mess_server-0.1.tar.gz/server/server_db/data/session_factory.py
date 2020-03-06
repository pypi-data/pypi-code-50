import sqlalchemy
import sqlalchemy.orm
from sqlalchemy.orm import Session, Query

from server_db.db import db_folder
from server_db.data.sqlalchemybase import SqlAlchemyBase

__engine = None
__factory = None


def global_init(db_name: str):
    global __engine, __factory

    if __factory:
        return

    conn_str = 'sqlite:///' + db_folder.get_full_path(db_name)
    __engine = sqlalchemy.create_engine(conn_str, echo=False, pool_recycle=7200,
                                        connect_args={'check_same_thread': False})
    __factory = sqlalchemy.orm.sessionmaker(bind=__engine, query_cls=Query)


def create_tables():
    if not __engine:
        raise Exception("You have not called global_init()")

    # noinspection PyUnresolvedReferences
    SqlAlchemyBase.metadata.create_all(__engine)


def create_session() -> sqlalchemy.orm.Session:
    if not __factory:
        raise Exception("You have not called global_init()")

    session: Session = __factory()
    session.expire_on_commit = False
    return session


def drop_tables():
    SqlAlchemyBase.metadata.drop_all(__engine)

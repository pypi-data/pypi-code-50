from datetime import datetime
from ifile.db.sqlalchemy.session import get_session
from ifile.db.sqlalchemy.models import File, Host
from ifile.exception import FileAlreadyExist, NotFound


def add_file(name, session=None):
    if session is None:
        session = get_session()

    with session.begin():
        file_db = File(name=name)
        file_db.save(session=session)

        return file_db


def update_file(id, values, session=None):
    if session is None:
        session = get_session()

    with session.begin():
        file_db = session.query(File).filter(File.id == id).first()
        file_db.update(**values)
        file_db.save(session=session)

        return file_db


def get_files(session=None):
    if session is None:
        session = get_session()

    files = []

    with session.begin():
        files_db = session.query(File).all()

        for file_db in files_db:
            f = {
                "id": file_db.id,
                "uuid": file_db.uuid,
                "name": file_db.name,
                "md5": file_db.md5,
                "size": file_db.size,
                "path": file_db.path
            }
            files.append(f)

        return files


def get_file(id, session=None):
    if session is None:
        session = get_session()

    with session.begin():
        file_db = session.query(File).filter(File.id == id).first()

        if not file_db:
            raise NotFound("file not found, id: %s" % id)

        f = {
            "id": file_db.id,
            "uuid": file_db.uuid,
            "name": file_db.name,
            "md5": file_db.md5,
            "size": file_db.size,
            "path": file_db.path
        }

        return f


def destory_file(id, session=None):
    if session is None:
        session = get_session()

    with session.begin():
        file_db = session.query(File).filter(File.id == id).first()

        if file_db:
            session.query(File).filter(File.id == id).delete()


def add_host(name, ip, role, is_register=False, session=None):
    if session is None:
        session = get_session()

    with session.begin():
        host_db = session.query(Host).filter_by(name=name, ip=ip).first()

        if host_db is None:
            host_db = Host(name=name, ip=ip,
                           role=role, is_register=is_register)
            host_db.save(session=session)
        return host_db


def get_host(session=None, **kwargs):
    if session is None:
        session = get_session()

    with session.begin():
        host_db = session.query(Host).filter_by(**kwargs).first()

        return host_db


def get_hosts(session=None, **kwargs):
    if session is None:
        session = get_session()

    with session.begin():
        hosts_db = session.query(Host).filter_by(**kwargs).all()
        return hosts_db


def update_host_by_name(hostname, ip, session=None, **kwargs):
    if session is None:
        session = get_session()

    with session.begin():
        host_db = session.query(Host).filter_by(**kwargs).first()
        host_db.update(**kwargs)
        host_db.save(session=session)

        return host_db


def update_host(id, session=None, **kwargs):
    if session is None:
        session = get_session()

    with session.begin():
        host_db = session.query(Host).filter_by(id=id).first()
        host_db.update(**kwargs)
        host_db.save(session=session)

        return host_db

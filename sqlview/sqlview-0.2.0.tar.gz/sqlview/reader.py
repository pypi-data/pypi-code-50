from base64 import b64encode
from collections import namedtuple
from functools import partial
from pathlib import Path
import sqlite3


sqlite3.register_converter('BLOB', b64encode)
connect = partial(sqlite3.connect, detect_types=sqlite3.PARSE_DECLTYPES)


class Req:
    def __init__(self, db):
        self.db = db

    def exec(self, req):
        self.db.cur.execute(req)

    @property
    def fields(self):
        return [c[0] for c in self.db.cur.description]

    def __call__(self):
        for row in self.db.cur.fetchall():
            yield row


class Table:
    def __init__(self, db, name):
        self.db = db
        self.name = name

    def __iter__(self):
        req = Req(self.db)
        req.exec(f'SELECT * FROM {self.name}')
        fields = namedtuple(self.name, req.fields)
        for row in req():
            yield fields(*row)

    def __len__(self):
        req = Req(self.db)
        req.exec(f'SELECT COUNT(*) FROM {self.name}')
        return list(req())[0][0]


class DB:
    def __init__(self, path):
        if isinstance(path, Path):
            path = path.as_posix()
        self.cnx = connect(path)
        self.cur = self.cnx.cursor()
        self.get_tables()

    def get_tables(self):
        req = Req(self)
        req.exec('SELECT * FROM main.sqlite_master WHERE type="table"')
        tables = [
            Table(self, row[1])
            for row in req()
        ]

        for table in tables:
            setattr(self, table.name, table)

        self.tables = tables

    def __iter__(self):
        return iter(self.tables)

    def __len__(self):
        return len(self.tables)


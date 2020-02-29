from base64 import b64encode
from collections import namedtuple
import sqlite3


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

    def rows(self):
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
        sqlite3.register_converter('BLOB', b64encode)
        self.cnx = sqlite3.connect(path, detect_types=sqlite3.PARSE_DECLTYPES)
        self.cur = self.cnx.cursor()
        self._tables = []

    @property
    def tables(self):
        if not self._tables:
            req = Req(self)
            req.exec('SELECT * FROM main.sqlite_master WHERE type="table"')
            for row in req():
                name = row[1]
                table = Table(self, name)
                setattr(self, name, table)
                self._tables.append(table)
        return self._tables

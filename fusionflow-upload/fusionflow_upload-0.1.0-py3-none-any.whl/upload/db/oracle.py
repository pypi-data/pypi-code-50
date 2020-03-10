from . import DatabaseTable
import cx_Oracle
from cx_Oracle import connect, makedsn
from datetime import datetime, timedelta

from typing import Text
from ..parameter import Parameter

def general_outtype_type_cast(cursor, name, defaultType, size, precision, scale):
    """change oracle cursor default return value type
    `cx_Oracle types mapping https://cx-oracle.readthedocs.io/en/latest/user_guide/sql_execution.html#fetch-data-types`_
    :param cursor: cursor bind to 
    :type cursor: [type]
    :param name: [description]
    :type name: [type]
    :param defaultType: [description]
    :type defaultType: [type]
    :param size: [description]
    :type size: [type]
    :param precision: [description]
    :type precision: [type]
    :param scale: [description]
    :type scale: [type]
    """
    # LOB
    if defaultType == cx_Oracle.CLOB:
        return cursor.var(cx_Oracle.LONG_STRING, arraysize=cursor.arraysize)
    if defaultType == cx_Oracle.BLOB:
        return cursor.var(cx_Oracle.LONG_BINARY, arraysize=cursor.arraysize)

class OracleDatabaseTable(DatabaseTable):
    type_covert = {
        cx_Oracle.BLOB          : bytes,
        cx_Oracle.CLOB          : str,
        cx_Oracle.NCLOB         : str,
        cx_Oracle.BFILE         : bytes,
        cx_Oracle.STRING        : str,
        cx_Oracle.ROWID         : str,
        cx_Oracle.TIMESTAMP     : datetime,
        cx_Oracle.BINARY        : bytes,
        cx_Oracle.OBJECT        : object,
        cx_Oracle.NCHAR         : str,
        cx_Oracle.NUMBER        : float,
        cx_Oracle.NATIVE_FLOAT  : float,
        cx_Oracle.FIXED_CHAR    : str,
        cx_Oracle.DATETIME      : datetime,
        cx_Oracle.INTERVAL      : timedelta
        # not support currently
        #cx_Oracle.OBJECT
        #cx_Oracle.CURSOR
    }

    username = Parameter(str, positional=True)
    password = Parameter(str, positional=True)
    host = Parameter(str, positional=True, default="localhost")
    port = Parameter(int, positional=True, default=1521)
    sid = Parameter(str, positional=True, default='orcl')

    @property
    def dsn(self):
        return makedsn(self.host, self.port, self.sid)

    def extract(self):
        with connect(self.username, self.password, self.dsn) as connection:
            cursor = connection.cursor()
            cursor.outputtypehandler = general_outtype_type_cast 
            cursor.execute(self.sql_stmt)

            field_names = [f[0] for f in cursor.description]
            field_types = [f[1] for f in cursor.description]
            for row in cursor:
                yield [{'name':field_names[idx], 'value':col, 'type': self.type_covert[field_types[idx]]} 
                        for idx, col in enumerate(row)
                      ]

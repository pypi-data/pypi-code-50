import cx_Oracle
from urllib import parse


class OracleConnector:

    def __init__(self, connection_string):
        pcs = self._parse_connection_string(connection_string)
        dsn = self._make_dsn(pcs)
        self._connection, self._cursor = self._establish_db_connection(pcs, dsn)

    def select_clob(self, query, binds=None):
        if binds is None:
            binds = []

        self._cursor.execute(query, binds)
        clob = self._cursor.fetchone()
        return clob

    @staticmethod
    def _parse_connection_string(connection_string):
        res = parse.urlparse(connection_string)
        return {
            'user': res.username,
            'password': res.password,
            'host': res.hostname,
            'port': res.port,
            'service_name': res.path[1:]
        }

    @staticmethod
    def _make_dsn(parsed_connection_string):
        dsn = cx_Oracle.makedsn(host=parsed_connection_string['host'],
                                port=parsed_connection_string['port'],
                                service_name=parsed_connection_string['service_name'])
        return dsn

    @staticmethod
    def _establish_db_connection(parsed_connection_string, dsn):
        connection = cx_Oracle.connect(
            user=parsed_connection_string['user'],
            password=parsed_connection_string['password'],
            dsn=dsn,
            encoding='uft-8'
        )
        return connection, connection.cursor()

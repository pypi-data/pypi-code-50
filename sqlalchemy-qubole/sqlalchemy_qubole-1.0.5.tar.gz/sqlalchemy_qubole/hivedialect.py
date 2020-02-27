""" Qubole Hive Integration with SQLAlchemy
This uses Hive dialects referred pyhive and jaydebeapi for DBAPI (JDBC Driver based)"""

from __future__ import absolute_import
from __future__ import unicode_literals
import re
import datetime
import decimal
from decimal import Decimal
from dateutil.parser import parse
from sqlalchemy.databases import mysql
from sqlalchemy import processors
from sqlalchemy.engine import default
from sqlalchemy.sql import compiler
from sqlalchemy.sql.compiler import SQLCompiler
from sqlalchemy import types
from . import common


class QuboleHiveStringTypeBase(types.TypeDecorator):
    impl = types.String

    def process_bind_param(self, value, dialect):
        raise NotImplementedError("Writing to Hive not supported")


class QuboleHiveDate(QuboleHiveStringTypeBase):
    impl = types.DATE

    def process_result_value(self, value, dialect):
        return processors.str_to_date(value)

    def result_processor(self, dialect, coltype):
        def process(value):
            if isinstance(value, datetime.datetime):
                return value.date()
            elif isinstance(value, datetime.date):
                return value
            elif value is not None:
                return parse(value).date()
            else:
                return None

        return process

    def adapt(self, impltype, **kwargs):
        return self.impl


class QuboleHiveTimestamp(QuboleHiveStringTypeBase):
    impl = types.TIMESTAMP

    def process_result_value(self, value, dialect):
        return processors.str_to_datetime(value)

    def result_processor(self, dialect, coltype):
        def process(value):
            if isinstance(value, datetime.datetime):
                return value
            elif value is not None:
                return parse(value)
            else:
                return None

        return process

    def adapt(self, impltype, **kwargs):
        return self.impl


class QuboleHiveDecimal(QuboleHiveStringTypeBase):
    impl = types.DECIMAL

    def process_result_value(self, value, dialect):
        if value is not None:
            return decimal.Decimal(value)
        else:
            return None

    def result_processor(self, dialect, coltype):
        def process(value):
            if isinstance(value, Decimal):
                return value
            elif value is not None:
                return Decimal(value)
            else:
                return None

        return process

    def adapt(self, impltype, **kwargs):
        return self.impl


_type_map = {
    'boolean': types.Boolean,
    'tinyint': mysql.MSTinyInteger,
    'smallint': types.SmallInteger,
    'int': types.Integer,
    'bigint': types.BigInteger,
    'float': types.Float,
    'double': types.Float,
    'string': types.String,
    'varchar': types.String,
    'char': types.String,
    'date': QuboleHiveDate,
    'timestamp': QuboleHiveTimestamp,
    'binary': types.String,
    'array': types.String,
    'map': types.String,
    'struct': types.String,
    'uniontype': types.String,
    'decimal': QuboleHiveDecimal,
}


class QuboleHiveCompiler(SQLCompiler):
    def visit_concat_op_binary(self, binary):
        return "concat(%s, %s)" % (self.process(binary.left), self.process(binary.right))

    def visit_insert(self, *args, **kwargs):
        result = super(QuboleHiveCompiler, self).visit_insert(*args, **kwargs)
        regex = r'^(INSERT INTO) ([^\s]+) \([^\)]*\)'
        assert re.search(regex, result), "Unexpected visit_insert result: {}".format(result)
        return re.sub(regex, r'\1 TABLE \2', result)

    def visit_column(self, *args, **kwargs):
        result = super(QuboleHiveCompiler, self).visit_column(*args, **kwargs)
        dot_count = result.count('.')
        assert dot_count in (0, 1, 2), "Unexpected visit_column result {}".format(result)
        if dot_count == 2:
            result = result[result.index('.') + 1:]
        return result

    def visit_char_length_func(self, fn, **kw):
        return 'length{}'.format(self.function_argspec(fn, **kw))


class UniversalSet(object):
    def __contains__(self, item):
        return True


class QuboleHiveIdentifierPreparer(compiler.IdentifierPreparer):
    reserved_words = UniversalSet()

    def __init__(self, dialect):
        super(QuboleHiveIdentifierPreparer, self).__init__(
            dialect,
            initial_quote='`',
        )


class QuboleHiveTypeCompiler(compiler.GenericTypeCompiler):
    def visit_INTEGER(self, type_, **kw):
        return 'INT'

    def visit_NUMERIC(self, type_, **kw):
        return 'DECIMAL'

    def visit_CHAR(self, type_, **kw):
        return 'STRING'

    def visit_VARCHAR(self, type_, **kw):
        return 'STRING'

    def visit_NCHAR(self, type_, **kw):
        return 'STRING'

    def visit_TEXT(self, type_, **kw):
        return 'STRING'

    def visit_CLOB(self, type_, **kw):
        return 'STRING'

    def visit_BLOB(self, type_, **kw):
        return 'BINARY'

    def visit_TIME(self, type_, **kw):
        return 'TIMESTAMP'

    def visit_DATE(self, type_, **kw):
        return 'TIMESTAMP'

    def visit_DATETIME(self, type_, **kw):
        return 'TIMESTAMP'


class QuboleHiveDialect(default.DefaultDialect):
    name = 'QuboleHive'
    driver = 'jdbc'
    paramstyle = 'pyformat'
    preparer = QuboleHiveIdentifierPreparer
    statement_compiler = QuboleHiveCompiler
    supports_alter = False
    supports_pk_autoincrement = False
    supports_default_values = False
    supports_empty_insert = False
    supports_unicode_statements = True
    supports_unicode_binds = True
    returns_unicode_strings = True
    description_encoding = None
    supports_native_boolean = True
    type_compiler = QuboleHiveTypeCompiler

    @classmethod
    def dbapi(cls):
        return common.return_dbapi()

    def __init__(self, *args, **kwargs):
        super(QuboleHiveDialect, self).__init__(*args, **kwargs)
        common.check_env()

    def initialize(self, connection):
        super(QuboleHiveDialect, self).initialize(connection)

    def create_connect_args(self, url):
        return common.create_conn(url, dsi='hive')

    def get_schema_names(self, connection, **kw):
        return [row[0] for row in connection.execute('SHOW SCHEMAS')]

    def get_view_names(self, connection, schema=None, **kw):
        return self.get_table_names(connection, schema, **kw)

    def _get_table_columns(self, connection, table_name, schema):
        full_table = table_name
        if schema:
            full_table = schema + '.' + table_name
        rows = connection.execute('DESCRIBE {}'.format(full_table)).fetchall()
        return rows

    def has_table(self, connection, table_name, schema=None):
        self._get_table_columns(connection, table_name, schema)
        return True

    def get_columns(self, connection, table_name, schema=None, **kw):
        rows = self._get_table_columns(connection, table_name, schema)
        # remove whitespace
        rows = [[col.strip() if col else None for col in row] for row in rows]
        # remove empty rows and comment
        rows = [row for row in rows if row[0] and row[0] != '# col_name']
        result = []
        for (col_name, col_type, _comment) in rows:
            if col_name == '# Partition Information':
                break
            # Take out the more detailed type information
            col_type = re.search(r'^\w+', col_type).group(0)
            try:
                coltype = _type_map[col_type]
            except KeyError:
                coltype = types.NullType

            result.append({
                'name': col_name,
                'type': coltype,
                'nullable': True,
                'default': None,
            })
        return result

    def get_foreign_keys(self, connection, table_name, schema=None, **kw):
        # Hive has no support for foreign keys.
        return []

    def get_pk_constraint(self, connection, table_name, schema=None, **kw):
        # Hive has no support for primary keys.
        return []

    def get_indexes(self, connection, table_name, schema=None, **kw):
        rows = self._get_table_columns(connection, table_name, schema)
        # remove whitespace
        rows = [[col.strip() if col else None for col in row] for row in rows]
        # remove empty rows and comment
        rows = [row for row in rows if row[0] and row[0] != '# col_name']
        for i, (col_name, _col_type, _comment) in enumerate(rows):
            if col_name == '# Partition Information':
                break
        # Handle partition columns
        col_names = []
        for col_name, _col_type, _comment in rows[i + 1:]:
            col_names.append(col_name)
        if col_names:
            return [{'name': 'partition', 'column_names': col_names, 'unique': False}]
        else:
            return []

    def get_table_names(self, connection, schema=None, **kw):
        query = 'SHOW TABLES'
        if schema:
            query += ' IN ' + self.identifier_preparer.quote_identifier(schema)
        return [row[0] for row in connection.execute(query)]

    def do_rollback(self, dbapi_connection):
        # No transactions for Hive
        pass

    def _check_unicode_returns(self, connection, additional_tests=None):
        # UTF-8
        return True

    def _check_unicode_description(self, connection):
        # UTF-8
        return True


dialect = QuboleHiveDialect

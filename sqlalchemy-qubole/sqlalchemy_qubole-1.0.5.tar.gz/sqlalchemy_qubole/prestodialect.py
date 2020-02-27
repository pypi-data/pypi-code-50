""" Qubole Presto Integration with SQLAlchemy
This uses Presto dialects from pyhive and jaydebeapi for DBAPI (JDBC Driver based)"""

from __future__ import absolute_import
from __future__ import unicode_literals
from pyhive.sqlalchemy_presto import PrestoDialect, PrestoCompiler, PrestoIdentifierPreparer, PrestoTypeCompiler
from . import common


class QubolePrestoDialect(PrestoDialect):
    name = 'QubolePresto'
    driver = 'jdbc'
    paramstyle = 'pyformat'
    preparer = PrestoIdentifierPreparer
    statement_compiler = PrestoCompiler
    supports_alter = False
    supports_pk_autoincrement = False
    supports_default_values = False
    supports_empty_insert = False
    supports_unicode_statements = True
    supports_unicode_binds = True
    returns_unicode_strings = True
    description_encoding = None
    supports_native_boolean = True
    type_compiler = PrestoTypeCompiler

    @classmethod
    def dbapi(cls):
        return common.return_dbapi()

    def __init__(self, *args, **kwargs):
        super(QubolePrestoDialect, self).__init__(*args, **kwargs)
        common.check_env()

    def initialize(self, connection):
        super(QubolePrestoDialect, self).initialize(connection)

    def create_connect_args(self, url):
        return common.create_conn(url, dsi='presto')


dialect = QubolePrestoDialect

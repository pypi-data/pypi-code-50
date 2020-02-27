__version__ = '1.0.0'
from sqlalchemy.dialects import registry

registry.register("qubole", "sqlalchemy_qubole.prestodialect", "QubolePrestoDialect")
registry.register("qubole.presto", "sqlalchemy_qubole.prestodialect", "QubolePrestoDialect")
registry.register("qubole.hive", "sqlalchemy_qubole.hivedialect", "QuboleHiveDialect")
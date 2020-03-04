from abc import ABC, abstractmethod
from contextlib import closing
from os import getenv

import MySQLdb
import pandas as pd
import pandas_gbq

from . import consts


class Source(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def query(self, query: str, output_type: str = "pandas"):
        pass


class MySqlSource(Source):
    def __init__(self, database):
        super().__init__()
        
        self.host = getenv(f"MYSQL_{database}_HOST".upper())
        self.port = int(getenv(f"MYSQL_{database}_PORT".upper()))
        self.user = getenv(f"MYSQL_{database}_USER".upper())
        self.password = getenv(f"MYSQL_{database}_PASS".upper())
        self.db = database

    def query(self, query: str, output_type: str = "pandas"):
        connection = MySQLdb.connect(self.host, self.user, self.password, self.db, self.port, charset="utf8")
        return self._query_mysql(query, connection, output_type)

    @staticmethod
    def _query_mysql(
            query: str, connection: MySQLdb.Connection, output_type: str = "pandas"
    ) -> pd.DataFrame:
        cursor = connection.cursor()
        with closing(cursor):
            if output_type == "pandas":
                return pd.read_sql(query, con=connection)
            else:
                raise NotImplementedError


class GoogleBigQuerySource(Source):
    def __init__(self, dataset: str):
        super().__init__()

        self.project_id = getenv(f"GBQ_{dataset}_PROJECT_ID".upper(), "")

    def query(self, query: str, output_type: str = "pandas"):
        return self._query_gbq(query, self.project_id, output_type)

    @staticmethod
    def _query_gbq(
        query: str, project_id: str, output_type: str = "pandas"
    ) -> pd.DataFrame:
        if output_type == "pandas":
            return pandas_gbq.read_gbq(query=query, project_id=project_id)
        else:
            raise NotImplementedError


ENGINES = {
    consts.engines.MYSQL: MySqlSource
}

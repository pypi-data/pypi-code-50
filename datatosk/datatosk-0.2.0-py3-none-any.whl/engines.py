from abc import ABC, abstractmethod
from contextlib import closing
from os import getenv
from typing import Union, List

import MySQLdb  # type: ignore
import pandas as pd  # type: ignore
import pandas_gbq  # type: ignore

from . import consts


class Engine(ABC):

    """
    Abstract class from which all Engine classes inherit.
    
    Dervied classes must implement `__init__()` and `query()` methods.
    """

    @abstractmethod
    def __init__(self):
        """Inits Engine."""

    @abstractmethod
    def query(self, query: str, output_type: str = consts.output_types.PANDAS):
        """
        Abstract method which all classes which inherit from Engine must implement.

        Args:
            query: An query string for extracting data.
            output_type: type of an object which will be output from query operation.
        """


class MySQLEngine(Engine):

    """
    Class that enables to connect to MySQL database and retrieve data from it.

    Atributes:
        host: MySQL host needed to connect to database.
        port: MySQL port needed to connect to database.
        user: MySQL user needed to connect to database.
        password: MySQL password needed to connect to database.
        database: MySQL database needed to connect to database.
    """

    def __init__(self, database: str):
        """
        Inits MySQLEngine.
        
        Atributes:
            database: database name.
        """

        # TODO: As more use cases arise, move configuration to a separate module.

        super().__init__()

        self.host = getenv(f"MYSQL_{database}_HOST".upper())
        self.port = int(getenv(f"MYSQL_{database}_PORT".upper(), "3306"))
        self.user = getenv(f"MYSQL_{database}_USER".upper())
        self.password = getenv(f"MYSQL_{database}_PASS".upper())
        self.database = database

    def query(
        self, query: str, output_type: str = consts.output_types.PANDAS,
    ) -> Union[pd.DataFrame, list, dict]:
        """
        Fetches data from a MySQL.

        Args:
            query: query string for extracting data.
            output_type: type of an object which will be output from query operation.

        Raises:
            NotImplementedError: An error occurred when not supported `output_type`.
        """

        output_type_map = {
            consts.output_types.PANDAS: self._output_pandas,
            consts.output_types.LIST: self._output_list,
            consts.output_types.DICT: self._output_dict,
        }

        connection = MySQLdb.connect(
            self.host,
            self.user,
            self.password,
            self.database,
            self.port,
            charset="utf8",
        )

        try:
            return output_type_map[output_type](query, connection)
        except KeyError:
            raise NotImplementedError(
                f"possible output_types: {list(output_type_map.keys())}"
            )

    @staticmethod
    def _output_pandas(query: str, connection: MySQLdb.Connection) -> pd.DataFrame:
        """
        Outputs data from a MySQL query in pandas DataFrame object.

        Args:
            query: query string for extracting data.
            connection: MySQLdb.Connection object.

        Returns:
            pandas.DataFrame with queried data.
        """
        cursor = connection.cursor()
        with closing(cursor):
            return pd.read_sql(query, con=connection)

    @staticmethod
    def _output_list(query: str, connection: MySQLdb.Connection) -> list:
        """
        Outputs data from a MySQL query in a list.

        Args:
            query: query string for extracting data.
            connection: MySQLdb.Connection object.

        Returns:
            One element list if one column selected, otherwise nested list.
        """
        cursor = connection.cursor()
        with closing(cursor):
            cursor.execute(query)

            return [
                item[0] if len(item) == 1 else list(item) for item in cursor.fetchall()
            ]

    @staticmethod
    def _output_dict(query: str, connection: MySQLdb.Connection) -> List[dict]:
        """
        Outputs data from a MySQL query in a list of dicts.

        Args:
            query: query string for extracting data.
            connection: MySQLdb.Connection object.

        Returns:
            List of dictionaries in which keys are column names.
        """
        cursor = connection.cursor()
        with closing(cursor):
            cursor.execute(query)
            columns = [column[0] for column in cursor.description]

            return [dict(zip(columns, row)) for row in cursor.fetchall()]


class GoogleBigQueryEngine(Engine):

    """
    Class that enables to connect to GoogleBigQuery database 
    and retrieve data from it.

    Atributes:
        project_id: GBQ project_id needed to connect to database.
    """

    def __init__(self, dataset: str):
        """
        Inits GoogleBigQueryEngine.
        
        Atributes:
            project_id: project_id name.
        """

        super().__init__()

        self.project_id = getenv(f"GBQ_{dataset}_PROJECT_ID".upper(), "")

    def query(self, query: str, output_type: str = consts.output_types.PANDAS):
        """
        Fetches data from a GoogleBigQuery.
        
        Args:
            query: query string for extracting data.
            output_type: type of an object which will be output from query operation.
        
        Returns:
            Queried data from GBQ database in type specified in `output_type".
        """

        output_type_mapper = {
            consts.output_types.PANDAS: self._output_pandas,
            consts.output_types.LIST: self._output_list,
            consts.output_types.DICT: self._output_dict,
        }
        try:
            return output_type_mapper[output_type](query, self.project_id)
        except KeyError:
            raise NotImplementedError(
                f"possible output_types: {list(output_type_mapper.keys())}"
            )

    @staticmethod
    def _output_pandas(query: str, project_id: str) -> pd.DataFrame:
        """
        Outputs data from a GBQ query in pandas DataFrame object.

        Args:
            query: query string for extracting data.
            project_id: GBQ project_id string.

        Returns:
            pandas.DataFrame with queried data.
        """
        return pandas_gbq.read_gbq(query=query, project_id=project_id)

    @staticmethod
    def _output_list(query: str, project_id: str):
        """
        [TODO]

        Raises:
            NotImplementedError
        """
        raise NotImplementedError

    @staticmethod
    def _output_dict(query: str, project_id: str):
        """
        [TODO]

        Raises:
            NotImplementedError
        """

        raise NotImplementedError

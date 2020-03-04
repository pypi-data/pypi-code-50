"""table template for database table ingest
"""

from ..table import Table

from typing import Iterable
import inspect

class DatabaseException(Exception):
    pass

class DatabaseParamMissing(DatabaseException):
    """missing some parameters required for database
    
    :param DatabaseException: [description]
    :type DatabaseException: [type]
    """


class DatabaseTable(Table):
    """base database connection helper class,
    
    :param filters: sql conditional expression used in where sub-statement 
    :type Table: ``str``
    :param orderby: orderby fields list used in order by sub-statement
    :param type: ``str``
    :raises DatabaseParamMissing: missing requried keyword pass through __init__
    :raises NotImplementedError: impletement by sub class
    """
    # connection required information, username, passwd, db etc, fullname
    required_params = None        

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.kwargs = kwargs

        # select method to fetch data
        # sql statement or table name or raw function
        self.use_sql = False
        if "sql" in kwargs:
            self.use_sql = True
            self.sql = kwargs["sql"]
        
        self.use_table = False
        if "table_name" in kwargs:
            self.use_table = True
            self.filters = kwargs.get("filters", None)
            self.orderby = kwargs.get("orderby", None)
            self._table_name = kwargs["table_name"]
        # callback function to fetch data
        self.fetch = kwargs.get("callback", None)

        self._init()

    def _init(self):
        """check condition required for database tables
        """
        # run-time check, use table or sql to fetch data
        if self.use_sql and self.use_table:
            raise DatabaseException("""both sql and table keyword supplied""")
        
        # or implement execute directly
        if not (self.use_sql or self.use_table):
            if not inspect.isgeneratorfunction(self.fetch):
                raise DatabaseException("""one of table_name, sql or callabck keyword must pass in
                                        """)
    
    @property
    def sql_stmt(self):
        """sql statement used to fetch data,
        constructed from use_table or return directly is use_sql 
        is True
        """
        if self.use_sql:
            return self.sql
        
        stmt = "select * from %s" % self.table_name

        if self.filters:
            stmt += " where %s" % self.filters
        
        if self.orderby:
            stmt += " order by %s" %self.orderby

        return stmt
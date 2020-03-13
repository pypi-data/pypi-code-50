from typing import Callable

from . import engines


class Source:
    """
    Main interface of datatosk.

    Examples:
        >>> import datatosk
        >>> source = datatosk.Source.mysql(database="db")
        >>> source.query("SELECT * FROM table")
    """

    mysql: Callable  = engines.MySQLEngine
    gbq: Callable  = engines.GoogleBigQueryEngine

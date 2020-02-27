class SPLIWACAException(Exception):
    """Base SPLIWACA Exception type"""


class FunctionEndError(SPLIWACAException):
    """Raised when execution of a function hits an `END FUNCTION` statement.
    (it should always reach a RETURN statement first)"""


class SPLIWACATypeError(SPLIWACAException):
    """Raised when a typing mistake was made in SPLIWACA"""


class BadParamType(SPLIWACATypeError):
    """Raised when a function or procedure is passed arguments of the wrong type."""


class BadReturnType(SPLIWACATypeError):
    """Raised when a function or procedure returns a value of the wrong type."""


class InvalidTypeError(SPLIWACATypeError):
    """Raised when a type specifier is erroneous"""


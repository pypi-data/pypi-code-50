# Copyright © 2018-2020 Roel van der Goot
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#
"""Module types provided types that can be used in the Attribute constructor.
"""


class Type:
    """Abstract base class for supported database types."""

    # pylint: disable=too-few-public-methods

    @staticmethod
    def sql(value):
        """Converts value into sql value."""
        return value


class Boolean(Type):
    """Type for booleans."""

    # pylint: disable=too-few-public-methods

    name = 'BOOLEAN'


class DateTime(Type):
    """Type for date times."""

    # pylint: disable=too-few-public-methods

    name = 'TIMESTAMP'


class DateTimeTimeZone(Type):
    """Type for date times with time zone information."""

    # pylint: disable=too-few-public-methods

    name = 'TIMESTAMP WITH TIME ZONE'


class Float32(Type):
    """Type for 32 bit floating point numbers."""

    # pylint: disable=too-few-public-methods

    name = 'float'


class Float64(Type):
    """Type for 64 bit floating point numbers."""

    # pylint: disable=too-few-public-methods

    name = 'float8'


class Int32(Type):
    """Type for 32 bit signed integers."""

    # pylint: disable=too-few-public-methods

    name = 'INT'


class Int64(Type):
    """Type for 64 bit signed integers."""

    # pylint: disable=too-few-public-methods

    name = 'BIGINT'


class String(Type):
    """Type for strings."""

    # pylint: disable=too-few-public-methods

    name = 'TEXT'

    @staticmethod
    def sql(value):
        sql_value = value.replace("'", "''")
        return f"'{sql_value}'"


class Json(Type):
    """Type for json data."""

    # pylint: disable=too-few-public-methods

    name = 'JSONB'

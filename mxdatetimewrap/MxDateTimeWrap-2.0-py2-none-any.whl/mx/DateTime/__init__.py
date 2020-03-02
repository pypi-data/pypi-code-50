import datetime

from .mx_datetime import DateTime, DateTimeFrom, DateTimeType
from .mx_datetimedelta import DateTimeDelta, DateTimeDeltaFrom
from .mx_relativedatetime import (
    RelativeDateTime, RelativeDateTimeFrom, RelativeDateTimeDiff
)
from . import Feasts

__all__ = [
    'DateTime', 'DateTimeFrom', 'DateTimeType',
    'DateTimeDelta', 'DateTimeDeltaFrom',
    'RelativeDateTime', 'RelativeDateTimeFrom', 'RelativeDateTimeDiff'
    'now', 'DateTimeFromCOMDate', 'Feasts'
]


def now():
    return DateTime(datetime.datetime.now())

DateTimeFromCOMDate = 0

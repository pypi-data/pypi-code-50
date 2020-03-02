import re
import six
import datetime
import calendar

from .mx_datetimedelta import DateTimeDelta
from .mx_relativedatetime import RelativeDateTime


month_offset = (
    (0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334, 365),
    (0, 31, 60, 91, 121, 152, 182, 213, 244, 274, 305, 335, 366),
)


def cmp(x, y):
    """
    Replacement for built-in function cmp that was removed in Python 3

    Compare the two objects x and y and return an integer according to
    the outcome. The return value is negative if x < y, zero if x == y
    and strictly positive if x > y.
    """
    return (x > y) - (x < y)


def is_leap_year(year):
    return (year % 4 == 0) and ((year % 100 != 0) or (year % 400 == 0))

def calc_absdate(dt):
    year = dt.year - 1
    yearoffset = year * 365 + year / 4 - year / 100 + year / 400
    year = year + 1
    return (
        dt.day +
        month_offset[is_leap_year(dt.year)][dt.month - 1] +
        yearoffset
    )


def calc_abstime(dt):
    return (dt.hour * 3600 + dt.minute * 60) + dt.second


class DateTimeType(datetime.datetime):
    def __eq__(self, other):
        if isinstance(other, DateTime):
            return self.absdate == other.absdate and self.abstime == other.abstime
        elif isinstance(other, datetime.datetime):
            return self.absdate == calc_absdate(other) and self.abstime == calc_abstime(other)
        return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __lt__(self, other):
        if other is None or isinstance(other, float) or isinstance(other, six.integer_types):
            return False
        elif isinstance(self, DateTime) and isinstance(other, DateTimeDelta):
            return True
        try:
            return super(DateTimeType, self).__lt__(other)
        except TypeError:
            if isinstance(self, DateTime) and isinstance(other, DateTimeDelta):
                return True
        return True

    def __gt__(self, other):
        if other is None or isinstance(other, six.integer_types) or isinstance(other, six.integer_types):
            return True
        try:
            return other.__lt__(self)
        except AttributeError:
            return True

    def __le__(self, other):
        return self.__eq__(other) or self.__lt__(other)

    def __ge__(self, other):
        return self.__eq__(other) or self.__gt__(other)

    def __int__(self):
        epoch = datetime.datetime.utcfromtimestamp(0)
        delta = self - epoch
        return int(delta.total_seconds())


class DateTime(DateTimeType):
    def __new__(cls, year=0, month=1, day=1, hour=0, minute=0,
                second=0, microsecond=0, **kwargs):
        year_or_const = year
        if isinstance(year_or_const, datetime.datetime):
            t = year_or_const
            return super(DateTime, cls).__new__(
                cls, t.year, t.month, t.day, t.hour, t.minute, t.second,
                t.microsecond
            )
        elif isinstance(year_or_const, datetime.date):
            t = year_or_const
            return super(DateTime, cls).__new__(cls, t.year, t.month, t.day)
        year = max(year_or_const, 1)
        return super(DateTime, cls).__new__(
            cls, year, month, day, hour, minute, second, microsecond,
        )

    def to_datetime_obj(self):
        return datetime.datetime(
            year=self.year,
            month=self.month,
            day=self.day,
            hour=self.hour,
            minute=self.minute,
            second=self.second,
            microsecond=self.microsecond
        )

    def __add__(self, other):
        dt = self.to_datetime_obj()
        if isinstance(other, (int, float)):
            return self.__add__(DateTimeDelta(other))
        elif isinstance(other, RelativeDateTime):
            return other.datetime_add(self)
        return DateTime(self.to_datetime_obj() + other)

    def __sub__(self, other):
        if isinstance(other, (int, float)):
            return self.__add__(DateTimeDelta(-other))
        elif isinstance(other, datetime.timedelta):
            return self.to_datetime_obj() - other
        elif isinstance(other, datetime.datetime):
            delta = self.to_datetime_obj() - other
            return DateTimeDelta.__from_delta__(delta)
        raise TypeError('Dont know what to do with %s' % repr(other))

    def __copy__(self):
        return DateTime(
            self.year, self.month, self.day, self.hour, self.minute,
            self.second, self.microsecond
        )

    def __deepcopy__(self, memo):
        return self.__copy__()

    @property
    def date(self):
        # return super(DateTime, self).date()
        return self.strftime('%Y-%m-%d')

    @property
    def time(self):
        # return super(DateTime, self).time()
        return self.strftime('%H:%M:%S.%f')[:-4]

    @property
    def day_of_week(self):
        return self.weekday()

    @property
    def days_in_month(self):
        return calendar.monthrange(self.year, self.month)[1]

    @property
    def iso_week(self):
        return self.isocalendar()

    def tuple(self):
        return tuple(self.timetuple())

    def is_leap(self):
        return is_leap_year(self.year)

    @property
    def abstime(self):
        return calc_abstime(self)

    @property
    def absdate(self):
        return calc_absdate(self)

    @property
    def absdays(self):
        return self.absdate - 1 + self.abstime / 86400.0


class DateTimeFrom(object):
    FORMATS = [
        '%y%m%d',
        '%y%m%d %H',
        '%y%m%d %H:%M',
        '%y%m%d %H:%M:%S',
        '%Y%m%d',
        '%Y%m%d %H',
        '%Y%m%d %H:%M',
        '%Y%m%d %H:%M:%S',
        '%d.%m.%Y',
        '%d.%m.%Y %H',
        '%d.%m.%Y %H:%M',
        '%d.%m.%Y %H:%M:%S',
        '%Y-%m-%d',
        '%Y-%m-%d %H',
        '%Y-%m-%d %H:%M',
        '%Y-%m-%d %H:%M:%S',
        '%m/%d/%Y',
        '%m/%d/%Y %H',
        '%m/%d/%Y %H:%M',
        '%m/%d/%Y %H:%M:%S',
        '%m/%d/%Y %I %p',
        '%m/%d/%Y %I:%M %p',
        '%m/%d/%Y %I:%M:%S %p',
        '%H:%M:%S'
    ]

    TIME_STRING_F_RE = re.compile('\d{1,2}:\d{1,2}:\d{1,2}.\d{1,2}')

    def __new__(cls, *args, **kwargs):
        if args and kwargs:
            raise TypeError('Can only be called with args OR kwargs')
        if args:
            if len(args) == 1:
                if isinstance(args[0], six.string_types):
                    return DateTimeFrom.__fromstring(args[0])
                elif isinstance(args[0], (DateTime)):
                    return args[0]
                elif isinstance(args[0], (datetime.datetime)):
                    return DateTime(args[0])
                elif isinstance(args[0], datetime.time):
                    return DateTime(
                        datetime.datetime.combine(datetime.date.min, args[0])
                    )
                elif isinstance(args[0], datetime.date):
                    return DateTime(
                        datetime.datetime.combine(args[0], datetime.time.min)
                    )
                else:
                    return (
                        DateTime(datetime.date.min) +
                        RelativeDateTime(year=1970) +
                        DateTimeDelta(seconds=args[0])
                    )
            else:
                return DateTime(*args)
        else:
            return DateTime(**kwargs)

    @classmethod
    def __fromstring(cls, s, first_attempt=True):
        for f in DateTimeFrom.FORMATS:
            try:
                return DateTime.strptime(s, f)
            except ValueError:
                pass
        if first_attempt and cls.TIME_STRING_F_RE.match(s):
            return cls.__fromstring(s.split('.')[0], first_attempt=False)
        raise ValueError('"%s" does not match any format' % s)

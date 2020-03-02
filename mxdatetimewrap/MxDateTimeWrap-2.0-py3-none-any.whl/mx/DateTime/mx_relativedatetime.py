import calendar
import math
import datetime
import six


class RelativeDateTime(object):
    def __init__(self,
                 years=0, months=0, days=0, hours=0, minutes=0, seconds=0,
                 year=None, month=None, day=None, hour=None, minute=None,
                 second=None):
        self.years = years
        self.months = months
        self.days = days
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

        self.year = year
        self.month = month
        self.day = day
        self.hour = hour
        self.minute = minute
        self.second = second

    def __add__(self, other):
        if isinstance(other, RelativeDateTime):
            return self.self_add(other)
        raise TypeError('Unknown class added: %r' % other)

    def get_base(self):
        from mx.DateTime import now
        return now()

    def __gt__(self, other):
        if isinstance(other, RelativeDateTime):
            base = self.get_base()
            return (base + self).__gt__(base + other)
        raise TypeError('Unknown comparison')

    def __lt__(self, other):
        if isinstance(other, RelativeDateTime):
            base = self.get_base()
            return (base + self).__lt__(base + other)
        raise TypeError('Unknown comparison')

    def __eq__(self, other):
        if isinstance(other, RelativeDateTime):
            base = self.get_base()
            return (base + self).__eq__(base + other)
        raise TypeError('Unknown comparison')

    def self_add(self, other):
        return RelativeDateTime(
            years=self.years + other.years,
            months=self.months + other.months,
            days=self.days + other.days,
            hours=self.hours + other.hours,
            minutes=self.minutes + other.minutes,
            seconds=self.seconds + other.seconds,
            year=(
                self.year + other.year
                if self.year and other.year
                else
                self.year or other.year
            ),
            month=(
                self.month + other.month
                if self.month and other.month
                else
                self.month or other.month
            ),
            day=(
                self.day + other.day
                if self.day and other.day
                else
                self.day or other.day
            ),
            hour=(
                self.hour + other.hour
                if self.hour and other.hour
                else
                self.hour or other.hour
            ),
            minute=(
                self.minute + other.minute
                if self.minute and other.minute
                else
                self.minute or other.minute
            ),
            second=(
                self.second + other.second
                if self.second and other.second
                else
                self.second or other.second
            ),
        )

    def datetime_add(self, dt):
        org_cls = dt.__class__

        months = self.months
        days = self.days
        hours = self.hours
        minutes = self.minutes
        seconds = self.seconds
        if self.year:
            while 1:
                try:
                    dt = dt.replace(year=self.year)
                except ValueError:
                    dt = dt + datetime.timedelta(1)
                else:
                    break
        if self.years:
            while 1:
                try:
                    dt = dt.replace(year=dt.year + self.years)
                except ValueError:
                    dt = dt + datetime.timedelta(1)
                else:
                    break
        if self.month is not None:
            months += -dt.month + self.month
        if self.day is not None:
            days += -dt.day + self.day
            if self.day < 0:
                days += calendar.monthrange(dt.year, dt.month)[1] + 1
        if self.hour is not None:
            hours += -dt.hour + self.hour
        if self.minute is not None:
            minutes += -dt.minute + self.minute
        if self.second is not None:
            seconds += -dt.second + self.second
        while months:
            if months > 0:
                num_days_in_current = calendar.monthrange(dt.year, dt.month)[1]
                dt = dt + datetime.timedelta(days=num_days_in_current)
                months -= 1
            else:
                prevmonth = (dt.month - 1) or 12
                num_days_in_last = calendar.monthrange(dt.year, prevmonth)[1]
                dt = dt - datetime.timedelta(days=num_days_in_last)
                months += 1
        if days:
            dt = dt + datetime.timedelta(days=days)
        if hours:
            dt = dt + datetime.timedelta(hours=hours)
        if minutes:
            dt = dt + datetime.timedelta(minutes=minutes)
        if seconds:
            dt = dt + datetime.timedelta(seconds=seconds)
        try:
            return org_cls(dt)
        except Exception:
            raise ValueError('FUCK!')


class RelativeDateTimeFrom(object):
    def __new__(cls, *args, **kwargs):
        if args and kwargs:
            raise TypeError('Can only be called with args OR kwargs')
        if args:
            if len(args) == 1:
                if isinstance(args[0], six.string_types):
                    return RelativeDateTimeFrom.__fromstring(args[0])
                else:
                    return RelativeDateTime(seconds=args[0])
            else:
                return RelativeDateTime(*args)
        else:
            return RelativeDateTime(**kwargs)

    @classmethod
    def __fromstring(cls, s):
        # Just take the simple case, where all parameters are defined with :
        # as seperator, and we take from 2 to 4 parameters
        # if s.startswith('-'):
        #     def float_fun(val):
        #         return -float(val)
        #     s = s.lstrip('- ')
        # else:
        #     float_fun = float
        s = s.lstrip('- ')
        parts = s.split(':')[:4]
        args = [float(val) for val in parts]
        if len(args) < 3:
            args.append(0)
        if len(args) < 4:
            args = [0] + args
        kwargs = {
            'day': args[0] or None,
            'hour': args[1] or None,
            'minute': args[2] or None,
            'second': args[3] or None
        }
        return RelativeDateTime(**kwargs)


class RelativeDateTimeDiff(object):
    def __new__(cls, date1, date2):
        diff = date1 - date2
        if diff.days == 0:
            return RelativeDateTime()
        date1months = date1.year * 12 + (date1.month - 1)
        date2months = date2.year * 12 + (date2.month - 1)

        # Calculate the months difference
        diffmonths = date1months - date2months
        if diff.days > 0:
            years, months = divmod(diffmonths, 12)
        else:
            years, months = divmod(diffmonths, -12)
            years = -years
        date3 = date2 + RelativeDateTime(years=years, months=months)
        diff3 = date1 - date3
        days = date1.absdays - date3.absdays

        # Correction to ensure that all relative parts have the same sign
        while days * diff.days < 0:
            if diff.days > 0:
                diffmonths = diffmonths - 1
                years, months = divmod(diffmonths, 12)
            else:
                diffmonths = diffmonths + 1
                years, months = divmod(diffmonths, -12)
                years = -years
            date3 = date2 + RelativeDateTime(years=years, months=months)
            diff3 = date1 - date3
            days = date1.absdays - date3.absdays

        # Drop the fraction part of days
        if days > 0:
            days = int(math.floor(days))
        else:
            days = int(-math.floor(-days))

        return RelativeDateTime(years=years,
                                months=months,
                                days=days,
                                hours=diff3.hour,
                                minutes=diff3.minute,
                                seconds=diff3.second)

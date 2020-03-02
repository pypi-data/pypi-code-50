import datetime
import six


class DateTimeDelta(datetime.timedelta):
    def __new__(cls, days=0, hours=0, minutes=0, seconds=0):
        return super(DateTimeDelta, cls).__new__(
            cls,
            days,
            hours=hours,
            minutes=minutes,
            seconds=seconds
        )

    @classmethod
    def __from_delta__(cls, delta):
        return cls(seconds=delta.total_seconds())

    def days():
        doc = "All days, divide total_seconds"

        def fget(self):
            return self.total_seconds() / (3600.0 * 24.0)
        return locals()
    days = property(**days())

    def hours():
        doc = "All hours, divide total_seconds"

        def fget(self):
            return self.total_seconds() / 3600.0
        return locals()
    hours = property(**hours())

    def minutes():
        doc = "All minutes, divide total_seconds"

        def fget(self):
            return self.total_seconds() / 60.0
        return locals()
    minutes = property(**minutes())

    def seconds():
        doc = "All seconds, use total_seconds"

        def fget(self):
            return self.total_seconds()
        return locals()
    seconds = property(**seconds())

    def get_remainder(self, num, rem):
        if num < 0:
            return -self.get_remainder(-num, rem)
        return num % rem

    @property
    def hour(self):
        hours = int(self.hours)
        return self.get_remainder(hours, 24)

    @property
    def minute(self):
        minutes = int(self.minutes)
        return self.get_remainder(minutes, 60)

    @property
    def second(self):
        seconds = int(self.seconds)
        return self.get_remainder(seconds, 60)

    def strftime(self, fmt):
        from .mx_datetime import DateTime
        # DateTime(1900) is 1.1.1900 but we want 0.1.1900
        d = DateTime(1900) + self
        return d.strftime(fmt)


    def __eq__(self, other):
        try:
            return super(DateTimeDelta, self).__eq__(other)
        except (TypeError, NotImplementedError) as e:
            # Keeping this here to feel safe...
            if not isinstance(other, DateTimeDelta):
                return other.__eq__(self)
            raise e

    def __lt__(self, other):
        if not isinstance(other, DateTimeDelta):
            return other.__lt__(self)
        return super(DateTimeDelta, self).__lt__(other)

    def __gt__(self, other):
        return other.__lt__(self)

    def __add__(self, other):
        if isinstance(other, (int, float)):
            return self.__add__(DateTimeDelta(seconds=other))
        return DateTimeDelta.__from_delta__(
            super(DateTimeDelta, self).__add__(other)
        )

    def __sub__(self, other):
        if isinstance(other, (int, float)):
            return self.__add__(DateTimeDelta(-other))
        elif isinstance(other, datetime.timedelta):
            return DateTimeDelta.__from_delta__(
                super(DateTimeDelta, self).__sub__(other)
            )
        elif isinstance(other, datetime.datetime):
            raise TypeError('You cannot subtract date from delta')
        raise TypeError('Dont know what to do with %s' % repr(other))


class DateTimeDeltaFrom(object):
    def __new__(cls, *args, **kwargs):
        if args and kwargs:
            raise TypeError('Can only be called with args OR kwargs')
        if args:
            if len(args) == 1:
                if isinstance(args[0], six.string_types):
                    if args[0]:
                        return DateTimeDeltaFrom.__fromstring(args[0])
                    return DateTimeDelta(0)
                elif isinstance(args[0], DateTimeDelta):
                    return args[0]
                elif isinstance(args[0], datetime.timedelta):
                    return DateTimeDelta.__from_delta__(args[0])
                elif isinstance(args[0], datetime.time):
                    return DateTimeDelta(
                        hours=args[0].hour,
                        minutes=args[0].minute,
                        seconds=args[0].second
                    )
                else:
                    return DateTimeDelta(seconds=args[0])
            else:
                return DateTimeDelta(*args)
        else:
            return DateTimeDelta(**kwargs)

    @classmethod
    def __fromstring(cls, s):
        # Just take the simple case, where all parameters are defined with :
        # as seperator, and we take from 2 to 4 parameters
        if s.startswith('-'):
            def float_fun(val):
                return -float(val)
            s = s.lstrip('- ')
        else:
            float_fun = float
        parts = s.split(':')[:4]
        args = [float_fun(val or 0) for val in parts]
        if len(args) < 3:
            args.append(0)
        if len(args) < 4:
            args = [0] + args
        return DateTimeDelta(*args)

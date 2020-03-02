from datetime import datetime
from datetime import timedelta
from dateutil import parser

FMT_DATE = "{:%Y-%m-%d}"
FMT_DATETIME = "{:%Y-%m-%d %H:%M}"


class Date(datetime):
    def std_weekday(self):
        """
        Sunday = 1
        Saturday = 7

        """
        d = self.weekday() + 2
        if d == 8:
            return 1
        return d

    @classmethod
    def current(cls, date=None):
        if not date:
            return Date.from_datetime(datetime.now())
        if isinstance(date, str):
            return Date.from_datetime(parser.parse(date))
        raise Exception("Invalid date input!")

    @classmethod
    def from_datetime(cls, dt):
        return Date(
            dt.year, dt.month, dt.day, dt.hour, dt.minute, dt.second, dt.microsecond
        )

    def to_datetime(self):
        return datetime(
            self.year,
            self.month,
            self.day,
            self.hour,
            self.minute,
            self.second,
            self.microsecond,
        )

    @classmethod
    def parse(cls, datestr):
        return Date.from_datetime(parser.parse(datestr))

    def format(self, format_str=None):
        fmt = format_str if format_str else FMT_DATETIME
        return self.strftime(fmt)

    def days_to_end_of_week(self):
        week_day = self.std_weekday()
        return 7 - week_day

    def days_from_start_of_week(self):
        return self.std_weekday() - 1

    def start_of_week(self):
        """
        This will return the preceeding Sunday at 12:00:00 am.

        """
        bow = self - timedelta(days=self.days_from_start_of_week())
        return self.from_datetime(bow).start_of_day()

    def end_of_week(self):
        """
        This will return the following Sunday at 12:00:00 am.

        """
        eow = self + timedelta(days=self.days_to_end_of_week() + 1)
        return self.from_datetime(eow).start_of_day()

    def start_of_day(self, hour=0, minute=0):
        return self.replace(hour=hour, minute=minute, second=0, microsecond=0)


class Timer:
    def __init__(self, start_time):
        if isinstance(start_time, datetime):
            self.start_time = start_time
        elif isinstance(start_time, str):
            self.start_time = datetime.strptime(start_time, "%Y-%m-%d %H:%M:%S")
        else:
            self.start_time = start_time

    def get_lapsed_seconds(self):
        end_time = datetime.now()
        duration = end_time - self.start_time
        return duration.total_seconds()

    def get_formatted_lapsed_time(self):
        total_seconds = self.get_lapsed_seconds()
        seconds = int(total_seconds) % 60
        total_minutes = int(total_seconds) / 60
        minutes = int(total_minutes % 60)
        hours = int(int(total_minutes) / 60)
        return "{:0>2}:{:0>2}:{:0>2}".format(hours, minutes, seconds)

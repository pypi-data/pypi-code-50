# -*- coding:utf-8 -*-

# author: Cone
# datetime: 2020-01-13 10:35
# software: PyCharm
import re
from cone.patterns import instance
from datetime import datetime, timedelta


@instance
class TimeUtil:
    MINUTE = 60
    HOUR = 60 * MINUTE
    DAY = HOUR * 24
    WEEK = DAY * 7
    MONTH = DAY * 30
    YEAR = DAY * 365

    time_patterns = re.compile(r'is_(\d)?(seconds|minutes|hours|days|weeks|months|years)_ago')

    def is_time_ago(self, target_time,
                    cur_time: datetime = None,
                    formatter='%Y-%m-%d %H:%M:%S',
                    seconds=0,
                    minutes=0,
                    hours=0,
                    days=0,
                    weeks=0,
                    months=0,
                    years=0,
                    ):
        total_seconds = seconds + minutes * self.MINUTE + hours * self.HOUR + \
                        days * self.DAY + weeks * self.WEEK + months * self.MONTH + years * self.YEAR
        return cur_time or datetime.now() - datetime.strptime(target_time, formatter) > timedelta(seconds=total_seconds)

    def time_wrapper(self, unit, value):
        def wrapper(**kwargs):
            kwargs[unit] = value
            return self.is_time_ago(**kwargs)
        return wrapper

    def __getattr__(self, item):
        result = self.time_patterns.search(item)
        if result:
            value, unit = result.groups()
            return self.time_wrapper(unit, int(value) if value else 1)
        return super().__getattribute__(item)


if __name__ == '__main__':
    # print(Time.a)
    print(TimeUtil.is_1days_ago(target_time='2019-10-13 13:11:11'))


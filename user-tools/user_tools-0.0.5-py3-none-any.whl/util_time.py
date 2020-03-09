#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""Some functions related to json time operations."""
import time

NOW_TIME = time.time()


def format_time(timestamp=NOW_TIME, format_str='%Y-%m-%d %H:%M:%S'):
    """Format timestamp returns format_str time.

    timestamp(float): The timestamp to be formatted.
        Defaults to the current timestamp.
    format_str(str): Time format used to format time.
        Default is '%Y-%m-%d %H:%M:%S'
        Commonly used format codes:
            %Y  Year with century as a decimal number.
            %m  Month as a decimal number [01,12].
            %d  Day of the month as a decimal number [01,31].
            %H  Hour (24-hour clock) as a decimal number [00,23].
            %M  Minute as a decimal number [00,59].
            %S  Second as a decimal number [00,61].
            %z  Time zone offset from UTC.
            %a  Locale's abbreviated weekday name.
            %A  Locale's full weekday name.
            %b  Locale's abbreviated month name.
            %B  Locale's full month name.
            %c  Locale's appropriate date and time representation.
            %I  Hour (12-hour clock) as a decimal number [01,12].
            %p  Locale's equivalent of either AM or PM.
    """

    tmp_time = time.localtime(timestamp)
    return time.strftime(format_str, tmp_time)

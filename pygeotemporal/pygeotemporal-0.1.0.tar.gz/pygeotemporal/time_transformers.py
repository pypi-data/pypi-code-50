from datetime import datetime, timedelta

from pytz import timezone, utc


# CONVERT TO UTC FORMAT            FROM EXAMPLE FORMAT 2015-11-20 03:46:20
def time2utc(date_in, time_zone="America/Chicago"):
    date_out = timezone(time_zone).localize(datetime.strptime(date_in, "%Y-%m-%d %H:%M:%S")).astimezone(utc).strftime(
        "%Y-%m-%dT%H:%M:%SZ")

    return date_out


# convert year and julian day to date
def julian_day_to_month_day(year,julian_day):
    date = datetime(int(year), 1, 1) + timedelta(int(julian_day))

    return date


# convert calendar date month/day/2-digit-year to YYYY-MM-DDT00:00:00Z (assumes there is no time so all set to zero
def calendar_date2utc(date_in,time_zone="America/Chicago"):

    date_out = datetime.strptime(date_in + " 00:00:00", "%m/%d/%y %H:%M:%S").strftime("%Y-%m-%dT%H:%M:%SZ")

    return date_out

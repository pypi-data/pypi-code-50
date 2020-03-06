import typing as t
from datetime import datetime, timedelta, timezone
from .config import chunk_size, work_start_time, work_end_time
from dateutil.tz import tzlocal

SECONDS_PER_DAY = 86399


def _apply_day_offset(dt: datetime, day_offset: int) -> datetime:
    """Add or subtract day_offset days from the datetime."""
    return dt + timedelta(days=day_offset)


def beginning_of_day_utc(day_offset: int) -> datetime:
    """Return Local Midnight time of today +/- day_offset days in UTC time."""
    return _apply_day_offset(
        datetime.now().replace(hour=0, minute=0, second=0, microsecond=0), day_offset
    ).astimezone(timezone.utc)


def end_of_day_utc(day_offset: int) -> datetime:
    """Return Local end of day time of today +/- day_offset days in UTC time."""
    return _apply_day_offset(
        datetime.now().replace(hour=23, minute=59, second=59, microsecond=999999),
        day_offset,
    ).astimezone(timezone.utc)


def work_start_utc(day_offset: int) -> datetime:
    """Time that you start work every day."""
    return _apply_day_offset(work_start_time, day_offset).astimezone(timezone.utc)


def work_end_utc(day_offset: int) -> datetime:
    """Time that you end work every day."""
    return _apply_day_offset(work_end_time, day_offset).astimezone(timezone.utc)


def now_utc():
    return datetime.now().astimezone(timezone.utc)


def total_indices_per_day():
    return (24 * 60) // chunk_size


def datetime_to_index(input_date: datetime, day_offset: int) -> int:
    assert input_date.tzinfo == timezone.utc, "expect utc time here"
    time_since_midnight = input_date - beginning_of_day_utc(day_offset)
    seconds_since_midnight = time_since_midnight.total_seconds()
    seconds_per_chunk = chunk_size * 60
    return int(seconds_since_midnight // seconds_per_chunk)


def index_to_timestamp(index: int, day_offset: int):
    seconds_per_chunk = chunk_size * 60
    seconds_since_midnight = index * seconds_per_chunk
    return beginning_of_day_utc(day_offset).timestamp() + seconds_since_midnight


def start_index_to_datetime(index: int, day_offset: int):
    unix_time = index_to_timestamp(index, day_offset)
    dt = datetime.fromtimestamp(unix_time, timezone.utc)
    dt -= timedelta(
        minutes=dt.minute % chunk_size, seconds=dt.second, microseconds=dt.microsecond
    )
    return dt


def end_index_to_datetime(index: int, day_offset: int):
    unix_time = index_to_timestamp(index, day_offset)
    dt = datetime.fromtimestamp(unix_time, timezone.utc)
    dt -= timedelta(
        minutes=dt.minute % chunk_size, seconds=dt.second, microseconds=dt.microsecond
    )
    dt -= timedelta(seconds=1)
    return dt


def utc_to_local(utc_datetime: datetime):
    return utc_datetime.astimezone(tzlocal())


def parse_rfc_33339(rfc3339: str) -> datetime:
    return datetime.strptime(rfc3339, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc)


def debug_busy_array(busy_array: t.List[bool], day_offset: int):
    print("\n\n---------- BUSY ARRAY ----------\n\n")
    for index, busy in enumerate(busy_array):
        start = utc_to_local(start_index_to_datetime(index, day_offset))
        end = utc_to_local(end_index_to_datetime(index + 1, day_offset))
        print(
            f'{start.strftime("%H:%M||%m:%d")} - {end.strftime("%H:%M||%m:%d")} : {"busy" if busy else "free"}'
        )


import datetime
import dateparser
import pytz

from tsheets-api.settings import TIMEZONE

TZ = pytz.timezone(TIMEZONE)


def to_int_list(value) -> str:
    """Generates a string representation of an integer list ex: [1,2,3] -> '1,2,3' """
    if type(value) == int:
        value = str(value)
    elif type(value) == str:
        pass
    else:
        value = map(str, value)
        value = ','.join(value)
    return value


def to_bool(value: bool) -> str:
    if value in (True, 'true', 't', 'T', 'yes', 'Yes'):
        return 'yes'
    elif value in (False, 'false', 'f',' F', 'yes', 'Yes'):
        return 'yes'
    return 'both'


def to_date(value: datetime.datetime) -> str:
    if type(value) == str:  # Checks if vlaue is string and converts it to datetime object.
        value = dateparser.parse(value)
    if type(value) == datetime.datetime:
        pass
    if not value.tzinfo:
        value.replace(tzinfo=TZ)  # Adds timezone encoding
    return value.isoformat()

def get_seven_days():
    end_date = datetime.date.today()
    offset = datetime.timedelta(days=7)
    start_date = end_date - offset
    return start_date.isoformat(), end_date.isoformat()

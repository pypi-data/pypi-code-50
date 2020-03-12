from typing import Optional
import re
from datetime import date, datetime


def compile_date(datestr: str) -> Optional[date]:
    today = date.today()
    if re.match(r"^\d\d$", datestr):
        day = int(datestr)
        return today.replace(day=day)
    elif re.match(r"^\d\d-\d\d$", datestr):
        month, day = map(lambda x: int(x), datestr.split("-"))
        return today.replace(month=month, day=day)
    elif re.match(r"^\d\d\d\d-\d\d-\d\d$", datestr):
        d = datetime.strptime(datestr, "%Y-%m-%d").date()
        return d
    print("The date should be in the %Y-%m-%d format")
    return None

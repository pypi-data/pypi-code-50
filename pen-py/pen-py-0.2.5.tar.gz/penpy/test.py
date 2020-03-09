from dates import *
from datetime import datetime
from collections import OrderedDict

timeframe = TimeFrame({
    "mon:thu": "11:12-14:15",
    "sat": "10:23"
})


print(timeframe.get_closest(datetime.now()))
print(timeframe.get_next(datetime.now()))
import sys
if sys.platform != 'win32':
    raise Exception('xingapi requires 32bit working environment')

import win32com.client
from xingapi.xasession import Session
from xingapi.xaquery import Query
from xingapi.xareal import Real
from xingapi.res import *
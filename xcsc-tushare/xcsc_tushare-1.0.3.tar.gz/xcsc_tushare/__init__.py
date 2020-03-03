# -*- coding:utf-8 -*- 
import codecs
import os

__version__ = '1.0.0'
__author__ = 'tushare'



"""
for tushare xcsc_tushare api
"""
from xcsc_tushare.data_pro import (pro_api, pro_bar)

from xcsc_tushare.upass import (get_token, set_token)
"""
@Version: 1.0.0
@Author: qi.you
@File: __init__.py.py
@Time: 2020/3/9 11:24
@Describe: 引用RPA公共包
"""
import sys
import os
sys.path.append('%s\PythonPublicPackage'%os.path.abspath(os.path.join(sys.argv[0], "../..")))
sys.path.append('%s\PythonPublicPackage'%os.path.abspath(os.path.join(sys.argv[0], "../../..")))
a='%s\PythonPublicPackage'%os.path.abspath(os.path.join(sys.argv[0], "../.."))
b='%s\PythonPublicPackage'%os.path.abspath(os.path.join(sys.argv[0], "../../.."))
from GetCmd import getcmd
import settings
from GetOATData import GetCData,GetOATData
from Loggers import Loggers
from RecordCheck import recordcheck
from YDMPython3 import YDM,balance,YDM_error,YDM_L
from UploadEmail import uploademail
from SendMessage import SendMessage
from Futuaccount_Login import Futuaccount_Login
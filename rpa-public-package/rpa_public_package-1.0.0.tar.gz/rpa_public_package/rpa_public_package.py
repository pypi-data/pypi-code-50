"""
@Version: 1.0.0
@Author: qi.you
@File: rpa_public_package.py
@Time: 2020/3/9 10:27
@Describe: 引用RPA公共包
"""
import sys
import os
sys.path.append('%s\PythonPublicPackage'%os.path.abspath(os.path.join(sys.argv[0], "../..")))
sys.path.append('%s\PythonPublicPackage'%os.path.abspath(os.path.join(sys.argv[0], "../../..")))
from GetCmd import getcmd
import settings
from GetOATData import GetCData,GetOATData
from Loggers import Loggers
from RecordCheck import recordcheck
from YDMPython3 import YDM,balance,YDM_error,YDM_L
from GetCmd import getcmd
from UploadEmail import uploademail
from SendMessage import SendMessage
import settings
from Futuaccount_Login import Futuaccount_Login
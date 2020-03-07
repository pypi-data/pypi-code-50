#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import os
import socket
from m2controller import constShared
import logging
from m2controller import m2Const

################################################################################
# Configure logging
#DEBUG INFO WARNING ERROR CRITICAL
enableDetailedLogging = True
if enableDetailedLogging:
    loglevel = logging.DEBUG
else:
    loglevel = logging.ERROR
logdatefmt = "%Y-%m-%d %H:%M:%S"
logfmt = "%(asctime)s %(filename)s %(lineno)d %(levelname)s: %(message)s"


def getPkgFolder(): # end with /
    pkgpath = m2Const.__file__
    pkgpath = pkgpath[:-10] # "m2Const.py" length=10
    return pkgpath

def isRaspberryPi():
    unameRes = str(os.uname())
    if -1 == unameRes.find('raspberrypi') and -1 == unameRes.find('armv7l'):
        return False
    else:
        return True

def analyzeBleDevName(strBleDevName):
    if strBleDevName.__len__() == constShared.bleDevScanNameLen:
        # hwType, versionMajorMinor, device_name
        return strBleDevName[constShared.bleDevScanNameLen - 4],strBleDevName[constShared.bleDevScanNameLen - 2:constShared.bleDevScanNameLen],strBleDevName[0:constShared.bleDevScanNameLen-4]
    else:
        return '','',''
    
def bServerAlive():
    try:
        # see if we can resolve the host name -- tells us if there is
        # a DNS listening
        host = socket.gethostbyname("breakthru.xyz")
        # connect to the host -- tells us if the host is actually
        # reachable
        s = socket.create_connection((host, 80), 2)
        s.close()
        return True
    except:
        pass
    return False


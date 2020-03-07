#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# the plant is watered at programmable time and amount. Group study of the same plant growth rate is an interesting topic

from m2controller import m2controller
from m2controller import m2Const
import signal
import time
import sys
from datetime import datetime
import usrCfg
import ctypes
telemii = 0

def get_now_fSecondSinceMidNight():
    now = datetime.now()
    return (now - now.replace(hour=0, minute=0, second=0, microsecond=0)).total_seconds()

def HHMMSS_to_fSecond(hour,minute,fSecond):
    return (hour*60+minute)*60+fSecond

def second2HWunitTime(fSecond):
    return round(fSecond*10+0.5)
    
requestExit = False
def signal_handler(sig, frame):
    global requestExit
    print('user Ctrl-C')
    requestExit = True

signal.signal(signal.SIGINT, signal_handler)

def callbackfunc(telemetry):
    global telemii
    #print("time now is {} sec, ({})".format(telemetry['timeOneTenthSecInOneDay']/10,telemetry['u16_rd_ii']))
    if telemii%20 == 0:
        print(telemetry)
    telemii = telemii + 1

controller = m2controller.BleCtrller(m2Const.etDebian,mainCB=callbackfunc,BleMACaddrList=usrCfg.BleMACinfoList)
#if not controller.checkFWtype():
#    print("all FW type validated")
BleDevNameList = controller.getBleDevNameList()
for devii in range(len(BleDevNameList)):
    controller.requestBleDeviceWithName(BleDevNameList[devii])
    controller.connect() # establish hw connection
    if True: #True: False
        controller.flashActionResetFlashStorage()
        constVal = 0x80;
        T0 = get_now_fSecondSinceMidNight()
        print(T0)
        controller.flashActionSave2Flash(second2HWunitTime(T0+HHMMSS_to_fSecond( 0, 0, 4)),0x1+constVal,list(bytes(ctypes.c_int8(-128)))*m2Const.RcPWMchanNum)
        controller.flashActionSave2Flash(second2HWunitTime(T0+HHMMSS_to_fSecond( 0, 0, 6)),0x2+constVal,list(bytes(ctypes.c_int8(127)))*m2Const.RcPWMchanNum)
        controller.flashActionSave2Flash(second2HWunitTime(T0+HHMMSS_to_fSecond( 0, 0, 8)),0x3+constVal,list(bytes(ctypes.c_int8(-128)))*m2Const.RcPWMchanNum)
        controller.flashActionSave2Flash(second2HWunitTime(T0+HHMMSS_to_fSecond( 0, 0,10)),0x4+constVal,list(bytes(ctypes.c_int8(127)))*m2Const.RcPWMchanNum)
        controller.flashActionSave2Flash(second2HWunitTime(T0+HHMMSS_to_fSecond( 0, 0,12)),0,list(bytes(ctypes.c_int8(-128)))*m2Const.RcPWMchanNum)
        controller.flashActionEndOfSequence()
        controller.flashActionSetTimeOneTenthS(second2HWunitTime(get_now_fSecondSinceMidNight()))
    else:
        # this is hacking to verified sequence running after power cycle. we need to manually put here the time printed earlier, so as to run the same sequence
        controller.flashActionSetTimeOneTenthS(second2HWunitTime(86000.523273))
    controller.flashActionResetSequenceExecAndGo()

while True:
    time.sleep(0.01)
    
    controller.update()

    if requestExit:
        controller.stop()
        break

print("done")

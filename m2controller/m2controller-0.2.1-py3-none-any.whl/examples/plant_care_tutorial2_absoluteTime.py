#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# the plant is watered at programmable time and amount. Group study of the same plant growth rate is an interesting topic

from m2controller import m2controller
from m2controller import m2Const
import signal
import time
import sys
from datetime import datetime
from datetime import timedelta
import usrCfg
import ctypes

telemii = 0

def sec_to_hhmmss(sec): 
    return str(timedelta(seconds = sec))

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
    if telemii%30 == 0:
        print("now {}, act ID {}, next action at {}".format(sec_to_hhmmss(telemetry['timeOneTenthSecInOneDay']/10),telemetry['u16_rd_ii'],sec_to_hhmmss(telemetry['i32timeStampOneTenthS']/10)))
    telemii = telemii + 1

controller = m2controller.BleCtrller(m2Const.etDebian,mainCB=callbackfunc,BleMACaddrList=usrCfg.BleMACinfoList)
BleDevNameList = controller.getBleDevNameList()
for devii in range(len(BleDevNameList)):
    controller.requestBleDeviceWithName(BleDevNameList[devii])
    controller.connect() # establish hw connection

    if False: #True: False
        controller.flashActionResetFlashStorage()
        updateIntervalS = 60
        for iSec in range(0,86400,updateIntervalS): # working
            print("write cmd for {}".format(sec_to_hhmmss(iSec)))
            controller.flashActionSave2Flash(second2HWunitTime(iSec),round(iSec/updateIntervalS)%256,list(bytes(ctypes.c_int8((round(iSec/updateIntervalS)%2)*127))*m2Const.RcPWMchanNum))
        controller.flashActionEndOfSequence()
    controller.flashActionSetTimeOneTenthS(second2HWunitTime(get_now_fSecondSinceMidNight()))
    #controller.flashActionSetTimeOneTenthS(second2HWunitTime(69999))
    controller.flashActionResetSequenceExecAndGo()

    #photofilename = 'photo-{date:%Y-%m-%d-%H_%M_%S}.jpg'.format(date=datetime.datetime.now())
    #controller.take_a_photo(photofilename) #take photo, file name format:photo-year-,pmtj-day-hour-min-sec.jpg
while True:
    time.sleep(0.01)
    
    controller.update()

    if requestExit:
        controller.stop()
        break

print("done")

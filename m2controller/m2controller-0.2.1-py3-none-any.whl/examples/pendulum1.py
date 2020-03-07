#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from m2controller import m2controller
from m2controller import m2Const
import signal
import time
import datetime
import usrCfg
import pendulum2

requestExit = False

################################################################
# we want to use the same log file naming convention so that the data analysis module, pendulum2.py, can be agnostic to how we get the log data file 
################################################################
logfilename = "m2flightData%s.txt"%(datetime.datetime.fromtimestamp(time.time()).strftime('%Y%m%d_%H%M%S'))
dataLogfile = open(logfilename,"w") 

def signal_handler(sig, frame):
    global requestExit
    print('user Ctrl-C to exit program execution')
    requestExit = True
    
signal.signal(signal.SIGINT, signal_handler)

################################################################
# upon every measurement data becomes available at 20Hz rate, this "callback" function will be summoned 
################################################################
def callbackfunc(telemetry):
    strTimeStamp = datetime.datetime.fromtimestamp(time.time()).strftime('%H:%M:%S.%f')[:-3]
    dataStr = "%s,eam:%d,%d,%d, %d,%d,%d, %d,%d,%d, %2.1f,%2.1f,%2.1f\n"%(strTimeStamp,
        telemetry['m_fAccelHwUnit'][0],telemetry['m_fAccelHwUnit'][1],telemetry['m_fAccelHwUnit'][2],
        telemetry['m_fGyroHwUnit'][0], telemetry['m_fGyroHwUnit'][1], telemetry['m_fGyroHwUnit'][2], 
        telemetry['m_fMagHwUnit'][0],  telemetry['m_fMagHwUnit'][1],  telemetry['m_fMagHwUnit'][2], 
        telemetry['m_fRPYdeg'][0], telemetry['m_fRPYdeg'][1], telemetry['m_fRPYdeg'][2])
    ################################################################
    # we print the data string to the screen and save them into the log file
    ################################################################
    print(dataStr)
    dataLogfile.writelines(dataStr) 

################################################################
# initialize the controller, remember to set the field BleMACinfoList to be your device's MAC address
################################################################
# TODO: let's initialize the BleMACinfoList if not being set by user.
controller = m2controller.BleCtrller(m2Const.etDebian,mainCB=callbackfunc,BleMACaddrList=usrCfg.BleMACinfoList)
controller.connect()
    
while True:
    ################################################################
    # wait for measurement data created and sent from the pendulum measurement apparatus
    ################################################################
    controller.m_CommsTunnel_main.waitForNotifications(1.0)
    if requestExit:
        ################################################################
        # house keeping works here when we finish data logging
        ################################################################
        controller.stop()
        dataLogfile.close()
        break

################################################################
# data collection completed, now let's analyze the log data
################################################################
pendulum2.parseDataLogFile(logfilename)

#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from m2controller import m2controller
from m2controller import m2Const
from m2controller import constShared
import signal,sys
import time
import usrCfg
from datetime import datetime
requestExit = False

def signal_handler(sig, frame):
    global requestExit
    print('user Ctrl-C')
    requestExit = True
    
signal.signal(signal.SIGINT, signal_handler)

readii = 0
def callbackfunc(telemetry):
    global readii
    if readii == 10:
        if "m_fRPYdeg" in telemetry:
            print("{} RPY: {}".format(datetime.now().strftime("%H:%M:%S"),telemetry['m_fRPYdeg']))
        else:
            BtnStatus = telemetry['m_BtnStatus']
            print("{} debug BtnStatus: {}".format(datetime.now().strftime("%H:%M:%S"),BtnStatus))
        readii = 0
    else:
        readii = readii + 1
    
controller = m2controller.BleCtrller(m2Const.etDebian,
                                     mainCB = callbackfunc,
                                     sysCfgForcedUpdate = True,
                                     username = usrCfg.username,
                                     mqttpassword = usrCfg.mqttpassword)
if True:
    controller.requestBleDeviceWithName('experiment')
    controller.connect()
    print('one Time reading of Telemetry Data')
    DictTelemetry = controller.readTelemetryData()
    print("debug DictTelemetry: {}".format(DictTelemetry))
    
while True:
    #controller.set_wallpaper(constShared.emoPic_happy)
    #controller.SendCmdTransBlking()
    #time.sleep(1)
    
    controller.clearPreviousCmd()
    #controller.send_a_SMS("14086665581", "helloworld")
    #controller.take_a_photo("myphoto.jpg")
    for ii in range(m2Const.USR_GPIO_CNT):
        controller.setGPIOn(ii)
    for ii in range(m2Const.RcPWMchanNum):
        controller.setPWM_n_pm1(ii,0.7)
    controller.SendCmdTransBlking()
    
    time.sleep(1)
    for ii in range(m2Const.USR_GPIO_CNT):
        controller.resetGPIOn(ii)
    for ii in range(m2Const.RcPWMchanNum):
        controller.setPWM_n_pm1(ii,-0.7)
    controller.SendCmdTransBlking()
    time.sleep(1)
    
    controller.update()

    if requestExit:
        controller.stop()
        break



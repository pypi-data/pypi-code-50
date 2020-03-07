#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# code not finished
# the spider will make absolute turning angles based on earth magnetic north as true reference
from m2controller import m2controller
from m2controller import m2Const
import signal
import time
import numpy as np
import usrCfg

AbsoluteAzimuth = False # True
InitialAzimuthDegInAbsoluteMode = 0.0 # north facing initially
def setDanceStep(action,DurationS,param1=0.0,param2=0.0):
    return {'action':action,'DurationS':DurationS,'param1':param1,'param2':param2}

DanceSeq = []
DanceSeq.append(setDanceStep('idle',                    1.0))
DanceSeq.append(setDanceStep('goStraight_thr_pm1',      2.0, 0.4))
DanceSeq.append(setDanceStep('turnCW_thr0to1_angleDeg', 4.0, 0.6, 90.0))
DanceSeq.append(setDanceStep('goStraight_thr_pm1',      2.0, 0.4))
DanceSeq.append(setDanceStep('turnCCW_thr0to1_angleDeg',8.0, 0.6, 180.0))
DanceSeq.append(setDanceStep('goStraight_thr_pm1',      4.0, 0.4))
DanceSeq.append(setDanceStep('turnCW_thr0to1_angleDeg', 8.0, 0.6, 180.0))
DanceSeq.append(setDanceStep('goStraight_thr_pm1',      2.0, 0.4))
DanceSeq.append(setDanceStep('turnCCW_thr0to1_angleDeg',4.0, 0.6, 90.0))
DanceSeq.append(setDanceStep('goStraight_thr_pm1',      2.0, -0.4))

requestExit = False
def signal_handler(sig, frame):
    global requestExit
    print('user Ctrl-C')
    requestExit = True

signal.signal(signal.SIGINT, signal_handler)
        
def stopEverything():
    controller.motorHbridgeCtrl_pm1(m2Const.spiderPWMchSteer,0.0)
    controller.motorHbridgeCtrl_pm1(m2Const.spiderPWMchSpeed,0.0)
     
danceStepii = 0
currAzimuthIMUunwrappedRad = 0.0
targetAzimuthIMUunwrappedPi = None
bTargetConditionMet = False

def callbackfunc(telemetry):
    global danceStepii
    global currAzimuthIMUunwrappedRad
    global targetAzimuthIMUunwrappedPi
    global bTargetConditionMet
    
    if danceStepii >= len(DanceSeq):
        stopEverything()
        return
    if AbsoluteAzimuth:
        currAzimuthIMUpmPi = telemetry['m_iCompass_pm180deg']*np.pi/180
        if targetAzimuthIMUunwrappedPi is None:
            targetAzimuthIMUunwrappedPi = InitialAzimuthDegInAbsoluteMode
    else:
        currAzimuthIMUpmPi = telemetry['m_fRPYdeg'][2]*np.pi/180
        if targetAzimuthIMUunwrappedPi is None:
            targetAzimuthIMUunwrappedPi = 0.0
        
    currAzimuthIMUunwrappedRad = np.unwrap([currAzimuthIMUunwrappedRad,currAzimuthIMUpmPi])[1]
    
    currentDanceStep = DanceSeq[danceStepii] 
    action = currentDanceStep['action']
    param1 = currentDanceStep['param1']
    param2 = currentDanceStep['param2']
        
    if controller.secSinceTime0() > currentDanceStep['DurationS']:
        danceStepii += 1
        print("danceStep:%d"%danceStepii)
        bTargetConditionMet = False
        controller.setTime0()
        controller.saveCurrAzimuthIMU()
        if danceStepii == len(DanceSeq):
            stopEverything()
            return
        currentDanceStep = DanceSeq[danceStepii]
        action = currentDanceStep['action']
        param1 = currentDanceStep['param1']
        param2 = currentDanceStep['param2']
    
        if action == "turnCW_thr0to1_angleDeg":
            targetAzimuthIMUunwrappedPi -= (param2*np.pi/180)
        elif action == "turnCCW_thr0to1_angleDeg":
            targetAzimuthIMUunwrappedPi += (param2*np.pi/180)

    if action == "idle":
        stopEverything()
    elif action == "goStraight_thr_pm1":
        ErrDeg = controller.getErrFromSavedAzimuth()
        controller.motorHbridgeCtrl_pm1(m2Const.spiderPWMchSteer,param1-ErrDeg*proportionalCorrectionRate)
    elif action == "turnCW_thr0to1_angleDeg":
        if bTargetConditionMet:
            stopEverything()
            return
        if currAzimuthIMUunwrappedRad < targetAzimuthIMUunwrappedPi:
            bTargetConditionMet = True
            stopEverything()
        else:
            controller.motorHbridgeCtrl_pm1(0,param1)
            controller.motorHbridgeCtrl_pm1(1,-param1)
    elif action == "turnCCW_thr0to1_angleDeg":
        if bTargetConditionMet:
            stopEverything()
            return
        if currAzimuthIMUunwrappedRad > targetAzimuthIMUunwrappedPi:
            bTargetConditionMet = True
            stopEverything()
        else:
            controller.motorHbridgeCtrl_pm1(0,-param1)
            controller.motorHbridgeCtrl_pm1(1,param1)
    else:
        print("unhandled action type:%s"%action)

controller = m2controller.BleCtrller(m2Const.etInternetController,callbackfunc,None,None,0,usrCfg.InternetHostIPaddr,usrCfg.mqttPort,usrCfg.mqttusername,usrCfg.mqttpassword)
controller.connect()

controller.setTime0()

while True:
    time.sleep(0.1)
    if danceStepii >= len(DanceSeq):
        break
    if requestExit:
        break

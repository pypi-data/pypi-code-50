#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# 2-axis orthogonal step motor platform, carrying petri-dish.
# image captured by mobile phone equipped with external microscopic lens.
# multiple images stitched by python script.

from m2controller import m2controller
from m2controller import m2Const
from m2controller import constShared
import signal
import time
import usrCfg
import datetime
movementSteps = 5
waitSecStepperMove = 0.05
waitSecPhoto = 5
runAutoHome = True
requestExit = False
m_stepMotorStatus = [0] * constShared.StepMotorCnt

def waitTillMotorsMoveDone():
    while True:
        if isMotorsMoveDone():
            break
        else:
            time.sleep(waitSecStepperMove)
            
def isMotorsMoveDone():
    done = True
    for ii in range(constShared.StepMotorCnt):
        if m_stepMotorStatus[ii] == 1<<constShared.stepMotorStatusBit_etMotorBusy :
            done = False
            break
    return done
    
def signal_handler(sig, frame):
    global requestExit
    print('user Ctrl-C')
    requestExit = True

signal.signal(signal.SIGINT, signal_handler)

def sanityCheck():
    return False

def callbackfunc(telemetry):
    global m_stepMotorStatus
    m_stepMotorStatus = telemetry['m_stepMotorStatus']
    #print(m_stepMotorStatus)

iPhotoIndex = 0
photofilenamePreamble = 'p{date:%Y-%m-%d-%H_%M_%S}'.format(date=datetime.datetime.now())
def getPhotoFileName():
    global iPhotoIndex
    global photofilenamePreamble
    photoFilename = "%s_%d.jpg"%(photofilenamePreamble,iPhotoIndex)
    iPhotoIndex += 1
    print("take photo with name:%s"%photoFilename)
    return photoFilename

iLoopCnt = 0
iSMstep = 0
iSMsubstep = 0
def move2nextSMstate():
    global iSMstep,iSMsubstep
    iSMstep += 1
    iSMsubstep = 0

controller = m2controller.BleCtrller(m2Const.etLocalNet,callbackfunc,usrCfg.BleMACinfoList,None,usrCfg.RaspberrPiName,0,usrCfg.InternetHostIPaddr,None,None,None)
    
controller.connect()
time.sleep(1)
if sanityCheck():
    print("controller HW setting error")
else:
    # return to origin
    while True:
        if not runAutoHome:
            break
        bCmdGenerated = False
        bOriginReached = True
        if m_stepMotorStatus[0] == 0:
            bOriginReached = False
        else:
            if m_stepMotorStatus[0] != 1<<constShared.stepMotorStatusBit_etOriginReached:
                print("move to x-\n")
                controller.moveStepper_n(m2Const.stepMotorRollIndex, -128)
                bCmdGenerated = True
                bOriginReached = False
        if m_stepMotorStatus[1] == 0:
            bOriginReached = False
        else:
            if m_stepMotorStatus[1] != 1<<constShared.stepMotorStatusBit_etOriginReached:
                print("move to y-\n")
                controller.moveStepper_n(m2Const.stepMotorPitchIndex, -128)
                bCmdGenerated = True
                bOriginReached = False
        if bOriginReached:
            break
        if bCmdGenerated:
            controller.SendCmdTransBlking(False)
        waitTillMotorsMoveDone()
            
    while True:
        if requestExit:
            controller.stop()
            break
        controller.clearPreviousCmd()
        controller.setSeqID(iLoopCnt)
        iLoopCnt += 1
        print("step(%d,%d)"%(iSMstep,iSMsubstep))
        if iSMstep == 0:
            controller.take_a_photo(getPhotoFileName())
            controller.SendCmdTransBlking(False)
            time.sleep(waitSecPhoto)
            move2nextSMstate()
        elif iSMstep == 1:
            if iSMsubstep < movementSteps:
                controller.moveStepper_n(m2Const.stepMotorRollIndex, 127)
                controller.SendCmdTransBlking(False)
                iSMsubstep += 1
                time.sleep(waitSecStepperMove)
            else:
                move2nextSMstate()
        elif iSMstep == 2:
            controller.take_a_photo(getPhotoFileName())
            controller.SendCmdTransBlking(False)
            time.sleep(waitSecPhoto)
            move2nextSMstate()
        elif iSMstep == 3:
            if iSMsubstep < movementSteps:
                controller.moveStepper_n(m2Const.stepMotorPitchIndex, 127)
                controller.SendCmdTransBlking(False)
                iSMsubstep += 1
                time.sleep(waitSecStepperMove)
            else:
                move2nextSMstate()
        elif iSMstep == 4:
            controller.take_a_photo(getPhotoFileName())
            controller.SendCmdTransBlking(False)
            time.sleep(waitSecPhoto)
            move2nextSMstate()
        elif iSMstep == 5:
            if iSMsubstep < movementSteps:
                controller.moveStepper_n(m2Const.stepMotorRollIndex, -127)
                controller.SendCmdTransBlking(False)
                iSMsubstep += 1
                time.sleep(waitSecStepperMove)
            else:
                move2nextSMstate()
        elif iSMstep == 6:
            controller.take_a_photo(getPhotoFileName())
            controller.SendCmdTransBlking(False)
            time.sleep(waitSecPhoto)
            move2nextSMstate()
        else:
            controller.releaseSeqID()
            controller.SendCmdTransBlking(False)
            time.sleep(1)            
            print("congratulations, data collection campaign completed!")
            controller.stop()
            break;
                
        
        

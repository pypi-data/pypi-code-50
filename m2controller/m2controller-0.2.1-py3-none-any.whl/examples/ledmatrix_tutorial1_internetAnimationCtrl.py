#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# the spider walks following command from PC(ble direct connection) or internet(mqtt remote control)

from m2controller import m2controller
from m2controller import m2Const
import ledMatrixAnimation
import time
import usrCfg
import signal
import sys

requestExit = False
def signal_handler(sig, frame):
    global requestExit
    print('user Ctrl-C exit request')
    quit()
    
signal.signal(signal.SIGINT, signal_handler)

########################################################################################
# initialize the controller, the settings used by the initialization must be correctly configured beforehand
########################################################################################
controller = m2controller.BleCtrller(m2Const.etInternetController,
                                     BleMACaddrList=usrCfg.BleMACinfoList,
                                     RaspberrPiName=usrCfg.RaspberrPiName,
                                     mqttPort=usrCfg.mqttPort,
                                     mqttusername=usrCfg.mqttusername,
                                     mqttpassword=usrCfg.mqttpassword)
controller.requestBleDeviceWithName(0)
controller.connect()
time.sleep(1)

########################################################################################
# select one cartoon animation by assigning its string name to the variable
########################################################################################
animationIconName = 'mspacman' # "ghost_green", "mspacman", "mspacmanheart", "pacman", "pacmanL", "pacmanLheart", "yesJedMario", "ghost_orange", "ghost_pink", "ghost_red",
if animationIconName not in ledMatrixAnimation.IconChoice:
    sys.exit()
AnimationIndex = ledMatrixAnimation.IconChoice.index(animationIconName)

########################################################################################
# select one frame in the cartoon animation, save its value in a variable
########################################################################################
frameIndex = 0
if frameIndex >= len(ledMatrixAnimation.indexSameRGB[AnimationIndex]):
    frameIndex = len(ledMatrixAnimation.indexSameRGB[AnimationIndex]) - 1

########################################################################################
# give the choice of cartoon and frame to the SDK function as function input arguments 
########################################################################################
controller.show_LEDmatrixFrom2DListIndexAndRGB(
    ledMatrixAnimation.indexSameRGB[AnimationIndex][frameIndex],
    ledMatrixAnimation.RGBvalues[AnimationIndex][frameIndex])
########################################################################################
# optionally put other control command, such as servo or motor control in the same control command
########################################################################################
#controller.motorHbridgeCtrl_pm1(m2Const.spiderPWMchSteer,-1.0)

########################################################################################
# send out all the earlier configured settings, LED, servo, etc, to the hardware controller over cloud
########################################################################################
controller.SendCmdTransBlking(False,False)
#while not requestExit:
time.sleep(1)
if True:
    ########################################################################################
    # Optionally send out one more frame. The earlier data package contains the common pixels for all frames.
    # This data package contains the unique pixels for the selection frame.
    ########################################################################################
    frameIndex = 1
    controller.show_LEDmatrixFrom2DListIndexAndRGB(
        ledMatrixAnimation.indexSameRGB[AnimationIndex][frameIndex],
        ledMatrixAnimation.RGBvalues[AnimationIndex][frameIndex])
    controller.SendCmdTransBlking(False,False)
    time.sleep(1)
time.sleep(2) # we need to leave some time here otherwise the last command may be lost
########################################################################################
# Finally, do some housekeeping logic when we close the control link
########################################################################################
controller.stop()
sys.exit()


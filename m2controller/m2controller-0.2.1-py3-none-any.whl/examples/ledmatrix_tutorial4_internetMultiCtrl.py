#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# the spider walks following command from PC(ble direct connection) or internet(mqtt remote control)

from m2controller import m2controller
from m2controller import m2Const
from m2controller import readimage
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

if len(sys.argv) != 3:
    usage = 'usage: python3 '+sys.argv[0]+' ImageFileName BLEdeviceName' 
    print(usage)
    sys.exit()
ImageFileName = sys.argv[1]
BLEdeviceName = sys.argv[2]

[errMsg,indexSameRGB,RGBvalues] = readimage.icoImage2LEDmatrix2DindexAndRGB(ImageFileName)
if errMsg.__len__() != 0:
    print('bad image, abort LED matrix control')
    sys.exit()
else:
    ########################################################################################
    # initialize the controller, the settings used by the initialization must be correctly configured beforehand
    ########################################################################################
    controller = m2controller.BleCtrller(m2Const.etInternetController,None,None,None,usrCfg.RaspberrPiName,0,usrCfg.InternetHostIPaddr,usrCfg.mqttPort,usrCfg.mqttusername,usrCfg.mqttpassword)
    controller.connect()
    time.sleep(0.5)
    controller.setRaspberrPiName(usrCfg.RaspberrPiName)
    controller.requestBleDeviceWithName(BLEdeviceName)
    controller.show_LEDmatrixFrom2DListIndexAndRGB(indexSameRGB,RGBvalues)
    
    time.sleep(0.5) # we need to leave some time here otherwise the last command may be lost
    ########################################################################################
    # Finally, do some housekeeping logic when we close the control link
    ########################################################################################
    controller.stop()
    print('send completed, we can now go back to the previous page')
    sys.exit()


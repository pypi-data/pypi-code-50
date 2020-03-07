#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# the spider walks following command from PC(ble direct connection) or internet(mqtt remote control)

from m2controller import m2controller, constShared
from m2controller import m2Const
from m2controller import readimage
from m2controller import utils
import time
import usrCfg
import signal
import sys

PWMgpioBCM = [13,19,12]
PWMCnt = PWMgpioBCM.__len__()
hPwm = []
fLastServoCtrl = [0]*PWMCnt
fLastServoCtrlTimeS = [0]*PWMCnt

requestExit = False
def signal_handler(sig, frame):
    global requestExit
    print('user Ctrl-C exit request')
    requestExit = True
    controller.stop()
    raise SystemExit
    
def callbackfuncCloudCtl(telemetry):
    print("msg rcvd")
    ########################################################################################
    # select one cartoon animation by assigning its string name to the variable
    ########################################################################################
    if "m_iRequestBleDeviceName" in telemetry:
        controller.requestBleDeviceWithName(telemetry['m_iRequestBleDeviceName'])
        
    if "m_baUartTx" in telemetry and len(telemetry['m_baUartTx']) > 0:
        ledData = telemetry['m_baUartTx']
        controller.connect()
        ########################################################################################
        # give the choice of cartoon and frame to the SDK function as function input arguments 
        ########################################################################################
        controller.sendUart(ledData)

        ########################################################################################
        # send out all the earlier configured settings, LED, servo, etc, to the hardware controller over cloud
        ########################################################################################
        controller.SendCmdTransBlking(False,False)
    else:
        if "m_PWMctrl_pm127" in telemetry:
            #print(telemetry["m_PWMctrl_pm127"])
            controller.setPWM_n_from_bytes(telemetry["m_PWMctrl_pm127"])
            controller.SendCmdTransBlking(False)
    
    if controller.isRPi():
        baServoCtrl = telemetry['m_baServoCtrlRPi']
        for ii in range(PWMCnt):
            if baServoCtrl[ii] == constShared.INVALID_i8_RC_CTRL_CMD:
                continue
            if abs(fLastServoCtrl[ii] - baServoCtrl[ii]/127) > 0.05:
                #print(baServoCtrl[ii])
                #print(baServoCtrl[ii]/127)
                pctCtrl = m2controller.servo_pm1_toRPiGPIOpercentage(baServoCtrl[ii]/127)
                print("pmw @gpio{} set to {}".format(PWMgpioBCM[ii],pctCtrl))
                hPwm[ii].ChangeDutyCycle(pctCtrl)
                fLastServoCtrl[ii] = baServoCtrl[ii]/127
                fLastServoCtrlTimeS[ii] = time.time()
                print('set servo connected to BRM GPIO pin{} to \pm 1 value:{}'.format(PWMgpioBCM[ii],fLastServoCtrl[ii]))
            
    #while not requestExit:
    time.sleep(1)

signal.signal(signal.SIGINT, signal_handler)

########################################################################################
# initialize the controller, the settings used by the initialization must be correctly configured beforehand
########################################################################################
controller = m2controller.BleCtrller(m2Const.etInternetBridgeToBle,None,usrCfg.BleMACinfoList,callbackfuncCloudCtl,usrCfg.RaspberrPiName,0,usrCfg.mqttPort,usrCfg.mqttusername,usrCfg.mqttpassword)
controller.connect()
if controller.isRPi():
    import RPi.GPIO as GPIO   # Import the GPIO library.
    # use GPIO.setmode(GPIO.BCM) to use Broadcom SOC channel names.
    # BOARD Set Pi to use pin number when referencing GPIO pins.
    GPIO.setmode(GPIO.BCM)    
    for ii in range(PWMCnt):
        print('set BCM GPIO {}'.format(PWMgpioBCM[ii]))
        GPIO.setup(PWMgpioBCM[ii], GPIO.OUT)  # Set GPIO pin 12 to output mode.
        hPwm.append(GPIO.PWM(PWMgpioBCM[ii], 50))   # Initialize PWM on pwmPin 50Hz frequency
        initialServoPM1 = 0
        hPwm[ii].start(m2controller.servo_pm1_toRPiGPIOpercentage(initialServoPM1)) # Start PWM with center position
        fLastServoCtrl[ii] = initialServoPM1
        fLastServoCtrlTimeS[ii] = time.time()
    time.sleep(1.5)
    '''
    print(-1)
    for ii in range(PWMCnt):
        hPwm[ii].ChangeDutyCycle(m2controller.servo_pm1_toRPiGPIOpercentage(-1))
    time.sleep(2)
    print(0)
    for ii in range(PWMCnt):
        hPwm[ii].ChangeDutyCycle(m2controller.servo_pm1_toRPiGPIOpercentage(0))
    time.sleep(2)
    print(1)
    for ii in range(PWMCnt):
        hPwm[ii].ChangeDutyCycle(m2controller.servo_pm1_toRPiGPIOpercentage(1))
    time.sleep(2)
    print(0)
    for ii in range(PWMCnt):
        hPwm[ii].ChangeDutyCycle(m2controller.servo_pm1_toRPiGPIOpercentage(0))
    time.sleep(2)
    '''
    for ii in range(PWMCnt):
        hPwm[ii].ChangeDutyCycle(0)
for ii in range(3): # value 3 is because I use the first 3 devices in usrCfg definition for LED matrix purpose
    print('show default image in LEDmatrix{}'.format(ii))
    controller.requestBleDeviceWithName(ii)
    controller.connect()
    time.sleep(0.5)
    [errMsg,indexSameRGB,RGBvalues] = readimage.icoImage2LEDmatrix2DindexAndRGB(utils.getPkgFolder()+'examples/pacman0.ico')
    if errMsg.__len__() != 0:
        print(errMsg)
        print('bad image, abort LED matrix control')
        sys.exit(3)
    else:
        print(RGBvalues)
        controller.show_LEDmatrixFrom2DListIndexAndRGB(indexSameRGB,RGBvalues)
        ########################################################################################
        # Finally, do some housekeeping logic when we close the control link
        ########################################################################################
        time.sleep(0.5)

        
i=0
while True:
    if requestExit:
        print('user request exit, leave while loop now')
        break
    #controller.SendCmdTransBlking(False)
    time.sleep(0.1)
    if controller.isRPi():
        TimeNowS = time.time()
        for ii in range(PWMCnt):
            if TimeNowS - fLastServoCtrlTimeS[ii] > 2:
                hPwm[ii].ChangeDutyCycle(0)
    i+=1
########################################################################################
# Finally, do some housekeeping logic when we close the control link
########################################################################################
controller.stop()
sys.exit()


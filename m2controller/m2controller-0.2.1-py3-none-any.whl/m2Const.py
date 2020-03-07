#!/usr/bin/env python
# -*- coding: UTF-8 -*-
USR_GPIO_CNT = 8
USR_BTN_CNT = 6
RcPWMchanNum = 6

GPIOgroupCntStepMotor = 2

CHAR3_BYTE_LEN = 20
StepMotorCnt = 2

FC_STATUS_LEN = 20
FC_STATUS_EACH_AXIS_BYTE = 5
RPY_floatIntConversion = 2
LSB_DROP_ACC = 5
ACC_DYNAMIC_FS_RNG = 2.0 # // g. MPU6050_ACCEL_FS_2: \pm 2G
LSB_DROP_GYR = 0
GYRO_DYNAMIC_FS_RNG = 2000.0 # // deg/sec
LSB_DROP_MAG = 6
LSBcountPerGauss = 6842; # LIS3MDL, \pm 4Gauss full range
ByteIndex0Seq_n_Btn = 15
ByteIndex0ADC1_1tenthV = 16
ByteIndex0Compass = 17
ByteIndex0Tmpture = 18

MinMsIntervalForBleDirectCtrl = 20
MinMsIntervalForInternetCtrl = 500 # if py2app cmd update rate is faster than this duration, app may experience packet loss 
readApp2pyDataInterval_ms = 500
strApp2pyCmdFilename = "app2pyCmd"  
strPy2appJsonCmdFilename = "py2appJsonCmd"  

etAndroid = "android"
etDebian = "Debian"
etInternetBridgeToBle = "InternetBridgeToBle"
etInternetController = "InternetController" # Controller over internet
etLocalNet = "LocalNet" # socket communication
platformTypes = [etAndroid,etDebian,etInternetBridgeToBle,etInternetController,etLocalNet]

TOPIC_APP_INTERNET_MQTT_CTRL = "INTERNET_CTRL"
TOPIC_APP_INTERNET_MQTT_MetaCtrl = "INTERNET_META_CTRL"
strREQUEST_Telemetry = "requestTelemetry"; # in order to save internet traffic, we may turn off the Char4 notification, and request it as needed
TOPIC_APP_INTERNET_Char4_TELEMETRY = "INTERNET_TELEMETRY"
MinMsIntervalApp2SDKnotification = 500;

stepMotorRollIndex = 0
stepMotorPitchIndex = 1

socketServerPORT_pyPrintWindow = 28090
socketServerPORT_SDKpy2app = 28091 # app as server
socketServerPORT_SDKapp2py = 28092 # app as client

spiderPWMchSpeed = 1
spiderPWMchSteer = 0

# Input GPIO for stepper motor control
stepMotorEmergencyStopBtn = 0
stepMotorForceRunBtn = 1
stepMotor0_NegLim = 2
stepMotor0_PosLim = 3
stepMotor1_NegLim = 4
stepMotor1_PosLim = 5

ledmatrixSize = 16

LEDTxInterval_ms = 100

InternetHostIPaddr =  "breakthru.xyz"
mqttPort = 1883
adaptorID = 0


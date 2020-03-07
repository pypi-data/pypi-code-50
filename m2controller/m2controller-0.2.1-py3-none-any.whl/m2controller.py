#!/usr/bin/python3 
# -*- coding: UTF-8 -*-
## @package m2controller
#  Documentation for m2controller module.
#
#  More details...


from m2controller import m2Const
from m2controller import constShared
from m2controller import bleDataDecoder
from m2controller import telemetrySocketListeningServer
from m2controller import mqttutils
from m2controller import utils
from bluepy import btle
import time
import ctypes
import socket
import json
from queue import Queue
import traceback
import os, sys
import subprocess
import requests
from datetime import datetime
import logging
logfilename = utils.getPkgFolder() + 'history.txt';
logging.basicConfig(filename=logfilename, filemode='a', format=utils.logfmt, level=utils.loglevel, datefmt=utils.logdatefmt)
logging.info("system launch")


def servo_pm1ctrl_to_i8(pm1Val):
    if pm1Val > 1.0:
        pm1Val = 1.0
    if pm1Val < -1.0:
        pm1Val = -1.0
    val = round(pm1Val*127)
    if val > 127:
        val = 127
    if val < -127:
        val = -127
    return round(val)

def getMs():
    return int(round(time.time() * 1000))

def normalizeAngleTo_pm180deg(angleDeg):
    while angleDeg > 180:
        angleDeg -= 360
    while angleDeg < -180:
        angleDeg += 360
    return angleDeg

def servo_pm1_toRPiGPIOpercentage(fPM1):
    # 20ms Duty cycle
    # -1 ==> 5
    #  1 ==> 10
    if fPM1 > 1.0:
        return 10
    elif fPM1 < -1.0:
        return 5
    else:
        return (fPM1+1)*2.5+5.0
    
class BleCtrller:
    ## Documentation for constructor function.
    #  More details ...
    def __init__(self, 
        platformType = m2Const.etDebian,
        sysCfgForcedUpdate = False,
        mainCB = None,
        cbFuncCloudCtl=None, # in internet bridge mode, default callback is for BLE, additional callback for cloud ctrl
        RaspberrPiName = '',
        adaptorID = m2Const.adaptorID,
        hostIPaddr = m2Const.InternetHostIPaddr,
        mqttPort = m2Const.mqttPort,
        username = None,
        mqttpassword = None,
        bUseInternetMsgSynchronousCB=True):

        if platformType == m2Const.etDebian or platformType == m2Const.etInternetBridgeToBle:
            import pygame
        elif platformType == m2Const.etAndroid or platformType == m2Const.etInternetController or platformType == m2Const.etLocalNet:
            pass
        else:
            print("it's a bug! unsupported platform: {}".format(platformType))
            sys.exit(1)
            
        self._proc = None
        self.errorStatus = False
        self.m_platform = platformType
        
        sysCfgJsonPath = utils.getPkgFolder()+'sysCfg.json'
        if os.path.isfile(sysCfgJsonPath) and (not sysCfgForcedUpdate):
            with open(sysCfgJsonPath) as f:
                sysCfg = json.load(f)
        else:
            if utils.bServerAlive():
                downloadURL = 'http://BreakThru.xyz:3000/RESTgetCfg/'+username
                try:
                    sysCfg = requests.get(downloadURL).json()
                    with open(sysCfgJsonPath, "w") as write_file:
                        json.dump(sysCfg, write_file)
                except:
                    print("Crash: download sysCfg.json failure, {}".format(downloadURL))
                    sys.exit(1)
            else:
                print("we need to download file sysCfg.json from server, but ur internet or our server is down :-(")
            
        self.m_BleMACaddrList = sysCfg['MacList']
        self.m_BleDevNameList = sysCfg['hwList']
        self.m_fwTypeList = sysCfg['FWtype']
        '''
        if platformType == m2Const.etDebian or platformType == m2Const.etInternetBridgeToBle:
            self.m_fwTypeList = []
            for listii in range(len(self.m_BleMACaddrList)):
                # it takes more than 1 sec to scan because majority of time wasted in launching the binary program
                tic = datetime.now()
                hwtype = self.scanToGetFWtypeFromMAC(self.m_BleMACaddrList[listii])
                toc = datetime.now()
                print((toc-tic).total_seconds())
                self.m_fwTypeList.append(hwtype)
        elif platformType == m2Const.etAndroid or platformType == m2Const.etInternetController or platformType == m2Const.etLocalNet:
            self.m_fwTypeList = [None]*len(self.m_BleMACaddrList)
        else:
            print("it's a bug! unsupported platform: {}".format(platformType))
            sys.exit(1)
        '''
        self.m_currentBleDeviceIndex = None
        self.m_currentBleDeviceName = ''
        self.m_requestBleDeviceName = ''
        self.clearPreviousCmd()
        self.m_adaptorID = adaptorID
        self.m_hostIPaddr = hostIPaddr
        self.m_mqttPort = mqttPort
        self.m_username = username
        self.m_mqttpassword = mqttpassword
        self.__bUseInternetMsgSynchronousCB = bUseInternetMsgSynchronousCB

        #########################################
        # etAndroid: socket
        # etDebian: Bluepy
        # etInternetBridgeToBle: Bluepy
        # etInternet: mqtt
        # etLocalNet: socket
        self.m_CommsTunnel_main = "" 
        self.m_CommsTunnel_main_Connected = False 
        self.__char3WrFailCnt = 0
        #########################################
        
        #########################################
        # etAndroid: None
        # etDebian: None
        # etInternetBridgeToBle: mqtt
        # etInternet: None
        # etLocalNet: None
        self.m_CommsTunnel_aux = None
        self.m_CommsTunnel_aux_Connected = False 
        #########################################

        self.m_app2pyListeningServer = None
        self.hService = ""
        self.char1 = ""
        self.char3 = ""
        self.char4 = ""
        self.m_CBmain = mainCB
        self.m_CBaux = cbFuncCloudCtl
        self.m_setting = None
        self.m_decodedTelemetry = None
        self.requestExit = False
        
        # cmd python=>app/BLEdevice
        self.cmd_baUartTx = None
        self.cmd_MP3PLAY = None
        self.cmd_SENDSMS = None
        self.cmd_TAKEPHOTO = None
        self.cmd_SetWallpaper = None
        self.cmd_u8GPIO = 0
        self.cmd_u8SeqID = None
        self.cmd_i8StepperMovCnt = [0]*m2Const.StepMotorCnt
        self.GPIO_beingUsed = 0
        self.cmd_i8AarrServos = [0]*m2Const.RcPWMchanNum
        self.Servo_beingUsed = 0
        self.LastCmdSentTimeMs = getMs()
        self.baLastBLEbinaryPkt = None
        self.m_startTimeS = None
        self.m_savedAzimuthIMUpm180deg = None
        self.m_mqttQueue = None
        self.m_bPygame_mixer_init_done = False
        self.__forceCtrlCmd = []
        self.m_baServoCtrlRPi = [constShared.INVALID_i8_RC_CTRL_CMD]*constShared.RPiPwmCtlCnt
        self.m_RaspberrPiName = RaspberrPiName
        self.m_bRPi = False
        try:
            if os.uname().nodename == 'raspberrypi':
                self.m_bRPi = True
        except:
            pass
        self.__hwTypeRd = ''
        self.versionMajorMinor = ''
        self.device_name = ''
    
    def getBleDevNameList(self):
        return self.m_BleDevNameList
     
    def checkFWtype(self):
        for devii in range(len(self.m_BleMACaddrList)):
            if not self.isFWtypeCorrect(self.m_BleMACaddrList[devii],self.m_fwTypeList[devii]):
                print('device with MAC address {} is expected to be of type "{}", but actual hardware mismatch!"\n'.format(usrCfg.BleMACinfoList[devii][0],usrCfg.BleMACinfoList[devii][1]))
                sys.exit(1)
        return False
        
    def flashActionSave2Flash(self,i32timeStampOneTenthS=0,u8GPIOctrl=0,i8PWMctrl=[0]*m2Const.RcPWMchanNum):
        self.__forceCtrlCmd = [constShared.FC_CTRL_MSG_PREAMBLE_TYPE_FLASHACTION0,constShared.FC_CTRL_MSG_PREAMBLE_TYPE_FLASHACTION1,constShared.flashaction_etActionSave2Flash];
        self.__forceCtrlCmd.extend(list(bytes(ctypes.c_int32(i32timeStampOneTenthS))))
        self.__forceCtrlCmd.extend(list(bytes(ctypes.c_uint8(u8GPIOctrl))))
        #self.__forceCtrlCmd.extend([0, 0])
        self.__forceCtrlCmd.extend(i8PWMctrl)
        self.__forceCtrlCmd.extend([0]*(m2Const.CHAR3_BYTE_LEN-len(self.__forceCtrlCmd)))
        print(self.__forceCtrlCmd)
        self.SendCmdTransBlking()
        time.sleep(0.1)
        
    def flashActionEndOfSequence(self):
        self.__forceCtrlCmd = [constShared.FC_CTRL_MSG_PREAMBLE_TYPE_FLASHACTION0,constShared.FC_CTRL_MSG_PREAMBLE_TYPE_FLASHACTION1,constShared.flashaction_etEndOfSequence];
        self.__forceCtrlCmd.extend([0]*(m2Const.CHAR3_BYTE_LEN-len(self.__forceCtrlCmd)))
        self.SendCmdTransBlking()
        time.sleep(0.1)

    def flashActionResetSequenceExecAndGo(self):
        self.__forceCtrlCmd = [constShared.FC_CTRL_MSG_PREAMBLE_TYPE_FLASHACTION0,constShared.FC_CTRL_MSG_PREAMBLE_TYPE_FLASHACTION1,constShared.flashaction_etResetExecGo];
        self.__forceCtrlCmd.extend([0]*(m2Const.CHAR3_BYTE_LEN-len(self.__forceCtrlCmd)))
        self.SendCmdTransBlking()
        time.sleep(0.1)

    def flashActionResetFlashStorage(self):
        self.__forceCtrlCmd = [constShared.FC_CTRL_MSG_PREAMBLE_TYPE_FLASHACTION0,constShared.FC_CTRL_MSG_PREAMBLE_TYPE_FLASHACTION1,constShared.flashaction_etResetFlashStorage];
        self.__forceCtrlCmd.extend([0]*(m2Const.CHAR3_BYTE_LEN-len(self.__forceCtrlCmd)))
        self.SendCmdTransBlking()
        time.sleep(0.1)
        
    def flashActionSetTimeOneTenthS(self,timeOneTenthS):
        self.__forceCtrlCmd = [constShared.FC_CTRL_MSG_PREAMBLE_TYPE_FLASHACTION0,constShared.FC_CTRL_MSG_PREAMBLE_TYPE_FLASHACTION1,constShared.flashaction_etSetTimeOneTenthS];
        self.__forceCtrlCmd.extend(list(bytes(ctypes.c_int32(timeOneTenthS))))
        self.__forceCtrlCmd.extend([0]*(m2Const.CHAR3_BYTE_LEN-len(self.__forceCtrlCmd)))
        self.SendCmdTransBlking()
        time.sleep(0.1)
        
    def isRPi(self):
        return self.m_bRPi
    
    def setRaspberrPiName(self,RaspberrPiName):
        self.get = RaspberrPiName
        
    def setRPiServo(self,index,value):
        if index < 0 or index >= constShared.RPiPwmCtlCnt:
            print('RPi computer has only {} servo control ports, acceptable value is 0 to {}'.format(constShared.RPiPwmCtlCnt,constShared.RPiPwmCtlCnt-1))
            return
        if value > 127 or value < -128:
            print('input value should be within -128 to 127')
            return
        else:
            self.m_baServoCtrlRPi[index] = value
            
    #return True if system in Error
    def chkSafeStatus(self):
        if self.errorStatus:
            print ("m2ctrl system in error, return")
            return True
        else:
            return False
    
    def getPlatformType(self):
        return self.m_platform
    
    def saveCurrAzimuthIMU(self):
        if self.m_decodedTelemetry is None:
            print("m2ctrl no telemetry estimate available, maybe BLE not connected?")
        self.m_savedAzimuthIMUpm180deg = self.m_decodedTelemetry['m_fRPYdeg'][2]

    def saveCurrIMUfRPYdeg(self):
        if self.m_decodedTelemetry is None:
            print("m2ctrl no telemetry estimate available, maybe BLE not connected?")
        self.m_savedIMUfRPYdeg = self.m_decodedTelemetry['m_fRPYdeg']
    
    def getErrFromSavedAzimuth(self):
        if self.m_decodedTelemetry is None:
            print("m2ctrl no telemetry estimate available, maybe BLE not connected?")
            return None
        if self.m_savedAzimuthIMUpm180deg is None:
            print("m2ctrl no referenece azimuth set by function saveCurrAzimuthIMU")
            return None
        ErrDeg = self.m_decodedTelemetry['m_fRPYdeg'][2] - self.m_savedAzimuthIMUpm180deg
        return normalizeAngleTo_pm180deg(ErrDeg) 

    def getErrFromSavedIMUfRPYdeg(self):
        res = [];
        for ii in range(3):
            res.append(self.m_decodedTelemetry['m_fRPYdeg'][ii]-self.m_savedIMUfRPYdeg[ii])
        return res
        
    def getAbsErrFromSavedAzimuth(self):
        return abs(self.getErrFromSavedAzimuth())

    def getAbsErrFromSavedIMUfRPYdeg(self):
        res = [];
        for ii in range(3):
            res.append(abs(self.m_decodedTelemetry['m_fRPYdeg'][ii]-self.m_savedIMUfRPYdeg[ii]))
        return res
    
    def getMaxAbsErrFromSavedIMUfRPYdeg(self):
        return max(self.getAbsErrFromSavedIMUfRPYdeg())
    
    def stop(self):
        self.requestExit = True
        if self.m_platform == m2Const.etAndroid or self.m_platform == m2Const.etDebian or self.m_platform == m2Const.etInternetController:
            self.m_CommsTunnel_main.disconnect()
            self.m_CommsTunnel_main_Connected = False
        elif self.m_platform == m2Const.etLocalNet:
            self.m_app2pyListeningServer.request_exit()
            self.m_CommsTunnel_main_Connected = False
        elif self.m_platform == m2Const.etInternetBridgeToBle:
            self.m_CommsTunnel_main.disconnect()
            self.m_CommsTunnel_main_Connected = False
            self.m_CommsTunnel_aux.disconnect()
            self.m_CommsTunnel_aux_Connected = False 
        else:
            print("unhandled stop()")
            pass
    
    def preprocessInternetCtrlCmd(self,ctrlDataDict):
        if 'm_RaspberrPiName' in ctrlDataDict and self.isRPi():
            if ctrlDataDict['m_RaspberrPiName'] != self.m_RaspberrPiName:
                for ii in range(len(ctrlDataDict['m_baServoCtrlRPi'])):
                    ctrlDataDict['m_baServoCtrlRPi'][ii] = constShared.INVALID_i8_RC_CTRL_CMD
        return ctrlDataDict
    
    # this function is used by both synchronous and asynchronous 
    def __mqttMsgProcess(self,strTopic,strMsg):
        try:
            if self.m_platform == m2Const.etInternetBridgeToBle:
                if strTopic == (m2Const.TOPIC_APP_INTERNET_MQTT_CTRL+self.m_username):
                    ctrlCmdDict = json.loads(strMsg)
                    ctrlCmdDict = self.preprocessInternetCtrlCmd(ctrlCmdDict)
                    self.m_CBaux(ctrlCmdDict)
                elif strTopic == (m2Const.TOPIC_APP_INTERNET_Char4_TELEMETRY+self.m_username):
                    if self.m_currentBleDeviceIndex is not None:
                        self.m_decodedTelemetry = bleDataDecoder.decodeRawBleTelemetry(strMsg,self.m_fwTypeList[self.m_currentBleDeviceIndex])
                    if self.m_CBmain is not None:
                        self.m_CBmain(self.m_decodedTelemetry)
        except Exception:
            print(traceback.format_exc())
                
    def mqttSynchronousCallback(self,strTopic,strMsg):
            # synchronous mqtt msg handling
            self.__mqttMsgProcess(strTopic,strMsg)
    
    def update(self,updateNotification=True):
        # asynchronous mqtt msg handling
        if self.m_mqttQueue is None or self.__bUseInternetMsgSynchronousCB:
            pass
        else:
            if self.m_platform == m2Const.etInternetBridgeToBle:
                msg = None
                while not self.m_mqttQueue.empty(): # If more than 1 msg pending, get the last one and ignore the earlier ones 
                    _client, _userdata, msg = self.m_mqttQueue.get()
                if msg is not None:
                    strTopic = msg.topic
                    strMsg = msg.payload.decode("utf-8").strip()
                    self.__mqttMsgProcess(strTopic,strMsg)
        if updateNotification:
            if self.m_CommsTunnel_main_Connected:
                try:
                    self.m_CommsTunnel_main.waitForNotifications(1.0)
                except:
                    logging.info("waitForNotifications crash")
                    self.m_CommsTunnel_main_Connected = False
                
    # if MAC address provided, only analyze the particular device
    # if no MAC address provided, scan and analyze all devices found      
    def bleMacToName(self, mac = None, searchTimeoutS = 3):
        executablePath = utils.getPkgFolder()+'binaryHelper/'
        if utils.isRaspberryPi():
            executablePath = executablePath + 'blescanRPi'
        else:
            executablePath = executablePath + 'blescan_x86_64'
        popenCmd = [executablePath]
        if mac is not None:
            popenCmd.append('-m')
            popenCmd.append(mac)
        if searchTimeoutS is not None:
            popenCmd.append('-s')
            popenCmd.append(str(searchTimeoutS))
        self._proc = subprocess.Popen(popenCmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        while True:
            rc = self._proc.poll()
            time.sleep(0.5)
            if rc is not None:
                bytesOut,  err = self._proc.communicate()
                if err.__len__() > 0:
                    print("BLE scan failed with Err Msg: {}".format(err))
                    input()
                    return [],[]
                else:
                    MacNameList = str(bytesOut).split(',')[:-1]
                    if (MacNameList.__len__() % 2) != 0:
                        print("Mac & devicename # doesn't match: {}".format(MacNameList))
                        input()
                        return [],[]
                    MacList = []
                    NameList = []
                    for ii in range(int(MacNameList.__len__()/2)):
                        MacList.append(MacNameList[ii*2+0])
                        NameList.append(MacNameList[ii*2+1])
                    return MacList,NameList
                break
        return ""
        
    
    def getDevices(self, macFilter=None, nameFilter=None, searchTimeoutS=10):
        executablePath = utils.getPkgFolder()+'binaryHelper/'
        if utils.isRaspberryPi():
            executablePath = executablePath + 'blescanRPi'
        else:
            executablePath = executablePath + 'blescan_x86_64'
        popenCmd = [executablePath]
        if macFilter is not None:
            if isinstance(macFilter, str) and macFilter.__len__() > 0:
                popenCmd.append('-m')
                popenCmd.append(macFilter)
        if nameFilter is not None:
            if isinstance(nameFilter, str) and nameFilter.__len__() > 0:
                popenCmd.append('-n')
                popenCmd.append(nameFilter)
        if searchTimeoutS is not None:
            popenCmd.append('-s')
            popenCmd.append(searchTimeoutS)
        self._proc = subprocess.Popen(popenCmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        while True:
            rc = self._proc.poll()
            time.sleep(0.5)
            if rc is not None:
                bytesOut,  err = self._proc.communicate()
                if err.__len__() > 0:
                    print("BLE scan failed with Err Msg: {}".format(err))
                    input()
                    return [],[]
                else:
                    MacNameList = str(bytesOut).split(',')[:-1]
                    if (MacNameList.__len__() % 2) != 0:
                        print("Mac & devicename # doesn't match: {}".format(MacNameList))
                        input()
                        return [],[]
                    MacList = []
                    NameList = []
                    for ii in range(int(MacNameList.__len__()/2)):
                        MacList.append(MacNameList[ii*2+0])
                        NameList.append(MacNameList[ii*2+1])
                    print(MacList)
                    print(NameList)
                    return MacList,NameList
                break
        return [],[]

            
    # connect if not already connected, also need to make sure the BLE target is the one we want    
    def connect(self):
        if self.chkSafeStatus():
            return
        if self.m_platform == m2Const.etAndroid or self.m_platform == m2Const.etLocalNet:
            # open socket before data transmission
            if self.m_CommsTunnel_main_Connected: # already connected
                return
            if self.m_CBmain is not None:
                if self.m_currentBleDeviceIndex is not None:
                    self.m_app2pyListeningServer = telemetrySocketListeningServer.telemListeningServer(self.m_CBmain,self.m_fwTypeList[self.m_currentBleDeviceIndex])
                    self.m_app2pyListeningServer.runAsThread()
            self.m_CommsTunnel_main_Connected = True
        elif self.m_platform == m2Const.etDebian:
            self.__connectBle(False)
        elif self.m_platform == m2Const.etInternetController:
            self.__connectInternet()
        elif self.m_platform == m2Const.etInternetBridgeToBle:
            self.__connectInternet()
            self.__connectBle(False)
        else:
            print('unsupported platform type:'+self.m_platform+'\n')
            pass
    
    
    def deviceName2Index(self,requested_name_In_hwList):
        try:
            return self.m_BleDevNameList.index(requested_name_In_hwList)
        except:
            print('ur selected device name "{}" cannot be found in the hWlist field of ur sysCfg.json'.format(requested_name_In_hwList))
            print("consider using sysCfgForcedUpdate=True when creating BleCtrller object, once is enough")
            return None
        
    def requestBleDeviceWithName(self,requested_name_In_hwList):
        if self.deviceName2Index(requested_name_In_hwList) is None:
            self.m_requestBleDeviceName = ''
        else:
            self.m_requestBleDeviceName = requested_name_In_hwList
    
    def scanToGetFWtypeFromMAC(self,MACaddr):
        MacList,NameList = self.bleMacToName(MACaddr)
        if len(NameList) != 1:
            print('Fatail Err: expect to find 1 device. now: {},{}), stop connecting to BLE device\n'.format(MacList,NameList))
            return None
        hwTypeRd, versionMajorMinor, device_name = utils.analyzeBleDevName(NameList[0])
        return hwTypeRd
        
    def isFWtypeCorrect(self,MacAddr,fwType):
        if self.m_CommsTunnel_main_Connected:
            self.stop()
        MacList,NameList = self.bleMacToName(MacAddr)
        if len(NameList) != 1:
            print('Fatail Err: expect to find 1 device. now: {},{}), stop connecting to BLE device\n'.format(MacList,NameList))
            return False
        hwTypeRd, versionMajorMinor, device_name = utils.analyzeBleDevName(NameList[0])
        if hwTypeRd == fwType:
            return True
        else:
            return False
        
    # void return    
    # attribute m_CommsTunnel_main_Connected is set if connected
    def __connectBle(self,bCheckFwType=False): # use scan to check FW type can cause huge system delay, use with attention 
        if not self.m_requestBleDeviceName:
            # empy device name means we don't want to make the connection now
            return
        if self.m_CommsTunnel_main_Connected:
            # BLE connected
            if not self.m_requestBleDeviceName: # keep the current BLE connection
                print("you need to call function requestBleDeviceWithName and set name of the device you want to control before connect")
                sys.exit(1)
            else:
                if self.m_currentBleDeviceName == self.m_requestBleDeviceName: # keep the current BLE connection unchanged
                    return
                else:
                    self.m_CommsTunnel_main.disconnect()
                    self.m_CommsTunnel_main_Connected = False
                    self.m_currentBleDeviceIndex = None
                    if not self.m_requestBleDeviceName: # not emtry string
                        logging.warn("warning: request to connect a Ble Device with emtpy Name?")
                        return
                    else:
                        self.m_currentBleDeviceIndex = self.deviceName2Index(self.m_requestBleDeviceName) # exit program if requested device name doesn't exist
                        if self.m_currentBleDeviceIndex is None:
                            logging.warn("warning1: requested Ble Device Name {} doesn't exist in sysCfg.json list {}".format(self.m_requestBleDeviceName,self.m_BleDevNameList))
                            return
        else:
            self.m_currentBleDeviceIndex = self.deviceName2Index(self.m_requestBleDeviceName)
            if self.m_currentBleDeviceIndex is None:
                logging.warn("warning2: requested Ble Device Name {} doesn't exist in sysCfg.json list {}".format(self.m_requestBleDeviceName,self.m_BleDevNameList))
                return
        if bCheckFwType:
            MacList,NameList = self.bleMacToName(self.m_BleMACaddrList[self.m_currentBleDeviceIndex])
            if len(NameList) != 1:
                print('Fatail Err: expect to find 1 device. now: {},{}), stop connecting to BLE device\n'.format(MacList,NameList))
                return
            self.__hwTypeRd, self.versionMajorMinor, self.device_name = utils.analyzeBleDevName(NameList[0])
            if self.__hwTypeRd != self.m_fwTypeList[self.m_currentBleDeviceIndex]:
                print('Fatail Err: user set HW type({}) differs from readback HW type({}), stop connecting to BLE device\n'.format(self.__hwTypeSet,self.__hwTypeRd))
                return
        try:
            CommsTunnel = btle.Peripheral(self.m_BleMACaddrList[self.m_currentBleDeviceIndex],btle.ADDR_TYPE_PUBLIC,self.m_adaptorID)
            CommsTunnel.setDelegate(DelegateIfc(self.m_CBmain,self.m_fwTypeList[self.m_currentBleDeviceIndex]))
            self.hService = CommsTunnel.getServiceByUUID(btle.UUID("0000fff0-0000-1000-8000-00805f9b34fb"))
            self.char1 = self.hService.getCharacteristics(btle.UUID("0000fff1-0000-1000-8000-00805f9b34fb"))[0]
            self.char3 = self.hService.getCharacteristics(btle.UUID("0000fff3-0000-1000-8000-00805f9b34fb"))[0]
            self.char4 = self.hService.getCharacteristics(btle.UUID("0000fff4-0000-1000-8000-00805f9b34fb"))[0]
            if self.m_CBmain is not None:
                CommsTunnel.writeCharacteristic(self.char4.valHandle+1, bytes([0x1,0x0]))
            self.m_CommsTunnel_main = CommsTunnel
            self.m_currentBleDeviceName = self.m_requestBleDeviceName
            self.m_CommsTunnel_main_Connected = True
            logging.info("btle connect success")
            #print('btle connected')
        except:
            self.m_CommsTunnel_main_Connected = False
            logging.info("btle connect crash")
            logging.info(traceback.format_exc())
            
    def __connectInternet(self):
        if self.m_platform == m2Const.etAndroid or self.m_platform == m2Const.etDebian or self.m_platform == m2Const.etInternetController or self.m_platform == m2Const.etLocalNet:
            if self.m_CommsTunnel_main_Connected:
                return
        elif self.m_platform == m2Const.etInternetBridgeToBle:
            if self.m_CommsTunnel_aux_Connected:
                return
        else:
            print("unsupported playform:"+self.m_platform+"\n")  
        
        if self.__bUseInternetMsgSynchronousCB:
            CommsTunnel = mqttutils.MQTTClientProxy(None,self.m_hostIPaddr,self.m_mqttPort,
                                                           self.m_username, self.m_mqttpassword, self.mqttSynchronousCallback,"MQTTClientProxy")
        else:
            self.m_mqttQueue = Queue();
            CommsTunnel = mqttutils.MQTTClientProxy(self.m_mqttQueue,self.m_hostIPaddr,self.m_mqttPort,
                                                       self.m_username, self.m_mqttpassword, None,"MQTTClientProxy")
        CommsTunnel.connect()
        if self.m_platform == m2Const.etInternetBridgeToBle:
            CommsTunnel.subscribe(m2Const.TOPIC_APP_INTERNET_MQTT_CTRL+self.m_username)
        else:
            CommsTunnel.subscribe(m2Const.TOPIC_APP_INTERNET_Char4_TELEMETRY)
        CommsTunnel.runAsThread()
        if self.m_platform == m2Const.etInternetBridgeToBle:
            self.m_CommsTunnel_aux = CommsTunnel
            self.m_CommsTunnel_aux_Connected = True
        else:
            self.m_CommsTunnel_main = CommsTunnel
            self.m_CommsTunnel_main_Connected = True


    def requestInternetTelemetry(self):
        if self.m_platform == m2Const.etInternetController:
            self.__SendInternetCmdTrans(m2Const.TOPIC_APP_INTERNET_MQTT_MetaCtrl,m2Const.strREQUEST_Telemetry)
            
    def listAllBleServices(self):
        print ("m2ctrl all Services...")
        for svc in self.dev.services:
            print(str(svc))
    
    def clearPreviousCmd(self):
        # these two command will be ignored by android if control value stays unchanged. 
        # another benefit is to avoid a single shot command gets missed.
        #self.cmd_SENDSMS = None
        #self.cmd_TAKEPHOTO = None
        self.cmd_u8GPIO = 0
        self.cmd_i8AarrServos = bytearray(m2Const.RcPWMchanNum)
        self.cmd_i8StepperMovCnt = bytearray(m2Const.StepMotorCnt)
        self.cmd_u8SeqID = 0
        self.m_iRequestBleDeviceName = ''
        self.cmd_TAKEPHOTO = None
    
    def __getCtrlDictionaryData(self):
        dictionarydata = None
        if not self.chkSafeStatus():
            if self.cmd_MP3PLAY is None:
                dictionarydata = {'m_MP3PLAY':["",""]}
            else:
                dictionarydata = {'m_MP3PLAY':[self.cmd_MP3PLAY["MP3fileRelativePath"],self.cmd_MP3PLAY["playmode"]]}
            
            if self.cmd_SENDSMS is None:
                dictionarydata['m_SENDSMS'] = ["",""]
            else:
                dictionarydata['m_SENDSMS'] = [self.cmd_SENDSMS["strPhoneNum"],self.cmd_SENDSMS["strSmsContent"]]

            if self.cmd_baUartTx is None:
                dictionarydata['m_baUartTx'] = []
            else:
                dictionarydata['m_baUartTx'] = self.cmd_baUartTx
            
            if self.cmd_TAKEPHOTO is None:
                dictionarydata['m_TAKEPHOTO'] = ["",""]
            else:
                dictionarydata['m_TAKEPHOTO'] = [self.cmd_TAKEPHOTO["strPhotoFileName"]]

            if self.cmd_SetWallpaper is None:
                dictionarydata['m_iWallpaper'] = [constShared.emoPic_Invalid]
            else:
                dictionarydata['m_iWallpaper'] = [self.cmd_SetWallpaper["iWallpaper"]]
            
            listData = [self.cmd_u8GPIO, self.GPIO_beingUsed]  
            dictionarydata['m_SeqID'] = listData
            
            if self.cmd_u8SeqID is None:
                dictionarydata['m_SeqID'] = ["",""]
            else:
                dictionarydata['m_SeqID'] = [self.cmd_u8SeqID, 1]
                
            dictionarydata['m_requestBleDeviceName'] = self.m_requestBleDeviceName
            
            stepperMask = 0
            if self.cmd_i8StepperMovCnt[m2Const.stepMotorRollIndex] != 0:
                stepperMask += 1<<m2Const.stepMotorRollIndex
            if self.cmd_i8StepperMovCnt[m2Const.stepMotorPitchIndex] != 0:
                stepperMask += 1<<m2Const.stepMotorPitchIndex
            listData = [self.cmd_i8StepperMovCnt[m2Const.stepMotorRollIndex], self.cmd_i8StepperMovCnt[m2Const.stepMotorPitchIndex], stepperMask]  
            dictionarydata['m_StepperCtrl'] = listData
            
            listData = [];
            for ii in range(m2Const.RcPWMchanNum):
                listData.append(self.cmd_i8AarrServos[ii])
            listData.append(self.Servo_beingUsed)
            dictionarydata['m_PWMctrl_pm127'] = listData
            
            dictionarydata['m_baServoCtrlRPi'] = self.m_baServoCtrlRPi
            
            dictionarydata['m_RaspberrPiName'] = self.m_RaspberrPiName
            
        return dictionarydata
    
    # return False if command is successfully sent out
    def SendCmdTransBlking(self, bIgnoreIdenticalCmd=True, bBlk=True):
        if self.chkSafeStatus():
            return True
        if self.requestExit:
            return True
        else:
            #if not self.m_CommsTunnel_main_Connected:
            #    logging.info("m2ctrl main not connected, attempt to connect")
            #    self.connect()
            
            if not self.m_CommsTunnel_main_Connected:
                return True
            
            if bBlk:
                while True:
                    if self.m_platform == m2Const.etDebian or self.m_platform == m2Const.etInternetBridgeToBle:
                        MinTxMsInterval = m2Const.MinMsIntervalForBleDirectCtrl;
                    else:
                        MinTxMsInterval = m2Const.MinMsIntervalForInternetCtrl;
                    
                    if getMs()-self.LastCmdSentTimeMs > MinTxMsInterval:
                        break
                    else:
                        time.sleep(0.01) #10ms
                if bIgnoreIdenticalCmd:
                    if self.__isNewBleCmd(self.__getBleCmdContent(True)):
                        self.__sendCmdUnconditional()
                        return False
                    else:
                        #print("ignore repeated cmd")
                        return True
                else:
                    self.__sendCmdUnconditional()
                    return False
            else:
                if getMs()-self.LastCmdSentTimeMs < m2Const.MinMsIntervalForInternetCtrl:
                    #print("m2ctrl ignore overly frequent cmd")
                    return True
                else:
                    if bIgnoreIdenticalCmd:
                        if self.__isNewBleCmd(self.__getBleCmdContent(True)):
                            self.__sendCmdUnconditional()
                            return False
                        else:
                            #print("ignore repeated cmd")
                            return True
                    else:
                        self.__sendCmdUnconditional()
                        return False

    def __sendCmdUnconditional(self):
        self.LastCmdSentTimeMs = getMs()
        if self.m_platform == m2Const.etAndroid or self.m_platform == m2Const.etLocalNet:
            self.__socketSendStr(self.__getCtrlJson())
        elif self.m_platform == m2Const.etDebian or self.m_platform == m2Const.etInternetBridgeToBle:
            # direct control BLE, in PC ubuntu or RPi
            self.__SendBleCmdTrans(self.__getBleCmdContent())
        elif self.m_platform == m2Const.etInternetController:
            self.__SendInternetCmdTrans(m2Const.TOPIC_APP_INTERNET_MQTT_CTRL+self.m_username,self.__getCtrlJson())
        self.cmd_MP3PLAY = None # avoid start MP3 play twice, press & release key 
    
    def __getCtrlJson(self):
        jsondata = json.dumps(self.__getCtrlDictionaryData())
        '''
text_file = open("json.txt", "w")
n = text_file.write(jsondata)
text_file.close()
        '''
        return jsondata
        
    def __socketSendStr(self,strSent):
        # create a socket
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # connect to server
        if self.m_platform == m2Const.etAndroid or self.m_platform == m2Const.etLocalNet:
            if self.m_platform == m2Const.etAndroid:
                host = '127.0.0.1' # server address
            elif self.m_platform == m2Const.etLocalNet:
                host = self.m_hostIPaddr
            else:
                print("m2ctrl laughable coding bug drgwerhsdndhrh")
                quit()
            port = m2Const.socketServerPORT_SDKpy2app # server port
            s.connect((host, port))
            s.send(strSent.encode('ASCII'))
            # close the connection
            s.close()
        else:
            print("m2ctrl unsupported Socket Transmission")
                
    def __getBleCmdContent(self,bPeekOnly=False):
        # bPeekOnly: we may want to check the payload to be transmitted, instead of actually send them out. That's peek mode
        cmdBytes = bytearray(m2Const.CHAR3_BYTE_LEN)
        if len(self.__forceCtrlCmd) > 0:
            cmdBytes[:] = self.__forceCtrlCmd
            if not bPeekOnly:
                self.__forceCtrlCmd = b''
        else:
            cmdBytes[0] = 0;
            cmdBytes[1] = 0xFF;
            cmdBytes[constShared.FC_CTRL_BLE_MSGTYPE_LEN+constShared.etRoll_PwmCH] = self.cmd_i8AarrServos[0];
            cmdBytes[constShared.FC_CTRL_BLE_MSGTYPE_LEN+constShared.etPitchPwmCH] = self.cmd_i8AarrServos[1];
            cmdBytes[constShared.FC_CTRL_BLE_MSGTYPE_LEN+constShared.etThrotPwmCH] = self.cmd_i8AarrServos[2];
            cmdBytes[constShared.FC_CTRL_BLE_MSGTYPE_LEN+constShared.etRudd_PwmCH] = self.cmd_i8AarrServos[3];
            cmdBytes[constShared.FC_CTRL_BLE_MSGTYPE_LEN+constShared.etAUX1_PwmCH] = self.cmd_i8AarrServos[4];
            cmdBytes[constShared.FC_CTRL_BLE_MSGTYPE_LEN+constShared.etAUX2_PwmCH] = self.cmd_i8AarrServos[5];
            cmdBytes[constShared.FC_CTRL_BLE_MSGTYPE_LEN+constShared.etAUX4_CH] = self.cmd_i8StepperMovCnt[m2Const.stepMotorRollIndex];
            cmdBytes[constShared.FC_CTRL_BLE_MSGTYPE_LEN+constShared.etAUX5_CH] = self.cmd_i8StepperMovCnt[m2Const.stepMotorPitchIndex];
            cmdBytes[13] = self.cmd_u8GPIO;
        return cmdBytes
    
    def __isNewBleCmd(self,bytearrayData):
        if bytearrayData == self.baLastBLEbinaryPkt:
            return False
        else:
            return True
        
    def __SendBleCmdTrans(self,bytearrayData):
        if self.chkSafeStatus():
            return
        self.baLastBLEbinaryPkt = bytearrayData
        try:
            self.char3.write(bytearrayData)
            logging.info("char3.write")
        except:
            self.__char3WrFailCnt = self.__char3WrFailCnt + 1
            time.sleep(2)
            self.m_CommsTunnel_main.disconnect()
            logging.info("char3.write crash for {} times".format(self.__char3WrFailCnt))
            if self.__char3WrFailCnt > 3:
                self.m_CommsTunnel_main_Connected = False 
                self.__char3WrFailCnt = 0
    
    def __SendInternetCmdTrans(self,strTOPIC,bytearrayData):
        if self.chkSafeStatus():
            return
        self.baLastBLEbinaryPkt = bytearrayData
        self.m_CommsTunnel_main.publish(strTOPIC,bytearrayData)
        #print(" sent")

    def playMP3withID(self,MP3ID):
        if self.m_platform == m2Const.etDebian:
            if not self.m_bPygame_mixer_init_done:
                pygame.mixer.init()
                self.m_bPygame_mixer_init_done = True
            thunder1 = pygame.mixer.Sound("./resources/thundersoundeffect.ogg")
            thunder1.play()
        elif self.m_platform == m2Const.etAndroid or self.m_platform == m2Const.etInternetController or self.m_platform == m2Const.etLocalNet:
            self.cmd_MP3PLAY = {"MP3fileRelativePath":MP3ID,"playmode":"PLAY_RES"};
        else:
            print("m2ctrl unhandled platform definition")
            return ""
                
    def playMP3file(self,MP3fileRelativePath,bRepeatedly = False):
        if self.m_platform == m2Const.etDebian:
            if not self.m_bPygame_mixer_init_done:
                pygame.mixer.init()
                self.m_bPygame_mixer_init_done = True
            thunder1 = pygame.mixer.Sound("./resources/thundersoundeffect.ogg")
            thunder1.play()
        elif self.m_platform == m2Const.etAndroid or self.m_platform == m2Const.etLocalNet:
            if bRepeatedly:
                self.cmd_MP3PLAY = {"MP3fileRelativePath":MP3fileRelativePath,"playmode":"REPEATEDPLAY"};
            else:
                self.cmd_MP3PLAY = {"MP3fileRelativePath":MP3fileRelativePath,"playmode":"PLAY"};
        elif self.m_platform == m2Const.etInternetController:
            print("MP3 play not supported in %s mode"%self.m_platform)
        else:
            print("m2ctrl unhandled platform definition")
            return ""

    def stopMP3(self):
        if self.m_platform == m2Const.etDebian:
            # TODO: add pygame sound play
            pass
        elif self.m_platform == m2Const.etAndroid or self.m_platform == m2Const.etLocalNet:
            self.cmd_MP3PLAY = {"MP3fileRelativePath":"","playmode":"STOP"};
        elif self.m_platform == m2Const.etInternetController:
            print("MP3 stop cmd not supported in %s mode"%self.m_platform)
        else:
            print("m2ctrl unhandled platform definition")
            return ""
    
    def __getoneUartTransForOneColor(self,indexSameRGB,RGBvalue):
        oneUartTrans = list(bytearray(constShared.PROTOCOL_PREAMBLE));
        byteCnt = len(RGBvalue)+len(indexSameRGB);
        oneUartTrans.extend(list(bytes(ctypes.c_uint16(byteCnt))))
        oneUartTrans.extend(RGBvalue)
        oneUartTrans.extend(indexSameRGB)
        return oneUartTrans
    
    def getLEDmatrixByteListFromIndexAndRGB(self,indexSameRGB_2Dlist,RGBvalues_2Dlist):
        list1D = []; #[different color][LED index in this color]
        for iiColor in range(len(indexSameRGB_2Dlist)): # one Trans for each color
            list1D.extend(self.__getoneUartTransForOneColor(indexSameRGB_2Dlist[iiColor],RGBvalues_2Dlist[iiColor]))

        # send special transaction to ardrino to show all the LED RGB settings
        TxCtrlCmd = bytearray(12)
        iBeginByteForCtrlCmd = 0
        for iibyte in range(len(constShared.PROTOCOL_PREAMBLE)):
            TxCtrlCmd[iBeginByteForCtrlCmd+iibyte] = constShared.PROTOCOL_PREAMBLE[iibyte];
        beginningByte = iBeginByteForCtrlCmd+len(constShared.PROTOCOL_PREAMBLE);
        TxCtrlCmd[beginningByte] = 5;
        TxCtrlCmd[beginningByte+1] = 0;
        beginningByte += constShared.PROTOCOL_LENBYTES;
        for iibyte in range(beginningByte, beginningByte+5):
            TxCtrlCmd[iibyte] = 0;
            
        list1D.extend(TxCtrlCmd)
        return list1D
    
    def sendUart(self,ByteList):
        iPayloadByteSerialSent = 0;
        while True: # send multiple BLE ctrl cmds
            iBeginByteForBleCmd = 0;
            self.__forceCtrlCmd = bytearray(m2Const.CHAR3_BYTE_LEN)
            self.__forceCtrlCmd[0] = constShared.FC_CTRL_MSG_PREAMBLE_TYPE_SEND_UART0;
            self.__forceCtrlCmd[1] = constShared.FC_CTRL_MSG_PREAMBLE_TYPE_SEND_UART1;
            iBeginByteForBleCmd = 2
            # uart data from sdk programming
            for byteii in range(constShared.FC_CTRL_BLE_MSGTYPE_LEN, m2Const.CHAR3_BYTE_LEN):
                self.__forceCtrlCmd[byteii] = ByteList[iPayloadByteSerialSent];
                iPayloadByteSerialSent+=1;
                if iPayloadByteSerialSent >= len(ByteList):
                    for remainByteii in range(byteii + 1, m2Const.CHAR3_BYTE_LEN):
                        self.__forceCtrlCmd[remainByteii] = 0;
                    break;
            self.SendCmdTransBlking()
            time.sleep(0.1)
            if iPayloadByteSerialSent >= len(ByteList):
                break;

    
    # in etDebian mode, the SendCmdTransBlking is called automatically   
    def show_LEDmatrixFrom2DListIndexAndRGB(self,indexSameRGB_2Dlist,RGBvalues_2Dlist):
        ByteList = self.getLEDmatrixByteListFromIndexAndRGB(indexSameRGB_2Dlist,RGBvalues_2Dlist)
        if self.m_platform == m2Const.etAndroid or self.m_platform == m2Const.etInternetController or self.m_platform == m2Const.etLocalNet:
            # remote LED matrix, sending over internet
            self.cmd_baUartTx = ByteList
            self.SendCmdTransBlking()
        elif self.m_platform == m2Const.etDebian or self.m_platform == m2Const.etInternetBridgeToBle:
            # local connected LED matrix, sending over serial port
            self.sendUart(ByteList)
        else:
            print("m2ctrl unsupported platform for show_LEDmatrixFrom2DListIndexAndRGB: %s"%self.m_platform)
                    
    def send_a_SMS(self,strPhoneNum,strSmsContent):
        if self.m_platform == m2Const.etAndroid:
            self.cmd_SENDSMS = {"strPhoneNum":strPhoneNum,"strSmsContent":strSmsContent};
        elif self.m_platform == m2Const.etDebian:
            print("m2ctrl SMS not supported in platform type: %s"%self.m_platform)
        elif self.m_platform == m2Const.etInternetController:
            print("m2ctrl SMS not supported in %s mode"%self.m_platform)
        else:
            print("m2ctrl unsupported platform for send_a_SMS: %s"%self.m_platform)
        
    def take_a_photo(self,strPhotoFileName):
        if self.m_platform == m2Const.etAndroid or self.m_platform == m2Const.etInternetController or self.m_platform == m2Const.etLocalNet:
            self.cmd_TAKEPHOTO = {'strPhotoFileName':strPhotoFileName}
        elif self.m_platform == m2Const.etDebian:
            print("m2ctrl photo not supported in platform type: %s"%self.m_platform)
        else:
            print("m2ctrl unsupported platform for take_a_photo: %s"%self.m_platform)

    def set_wallpaper(self,iWallpaper):
        if self.m_platform == m2Const.etAndroid or self.m_platform == m2Const.etLocalNet:
            self.cmd_SetWallpaper = {'iWallpaper':iWallpaper}
        elif self.m_platform == m2Const.etDebian:
            print("m2ctrl wallpaper not supported in platform type: %s"%self.m_platform)
        elif self.m_platform == m2Const.etInternetController:
            self.cmd_SetWallpaper = {'iWallpaper':iWallpaper}
        else:
            print("m2ctrl unsupported platform for set_wallpaper: %s"%self.m_platform)
        
    def setSeqID(self,SeqID):
        self.cmd_u8SeqID = SeqID

    def releaseSeqID(self):
        self.cmd_u8SeqID = None 
        
    def setGPIOn(self,n):
        if n < 0 or n >= m2Const.USR_GPIO_CNT:
            print("m2ctrl GPIO %d doesn't exist"%n)
            pass
        else:
            self.cmd_u8GPIO |= (1<<n)
            self.GPIO_beingUsed |= (1<<n)

    def resetGPIOn(self,n):
        if n < 0 or n >= m2Const.USR_GPIO_CNT:
            print("m2ctrl GPIO %d doesn't exist"%n)
            pass
        else:
            self.cmd_u8GPIO &= ~(1<<n)
            self.GPIO_beingUsed |= (1<<n)

    def moveStepper_n(self,n,stepCnt):
        if n < 0 or n >= m2Const.StepMotorCnt:
            print("m2ctrl Step motor %d(0-indexed) doesn't exist"%n)
            pass
        else:
            if stepCnt > 127 or stepCnt < -128:
                print("m2ctrl input Step motor movement steps(%d) must be within -128 to 127"%stepCnt)
                return None
            self.cmd_i8StepperMovCnt[n:n+1] = ctypes.c_int8(stepCnt)
            for GPIOii in range(n*m2Const.GPIOgroupCntStepMotor,(n+1)*m2Const.GPIOgroupCntStepMotor):
                self.GPIO_beingUsed |= (1<<GPIOii)

    def setPWM_n_from_bytes(self,iPWMctrl):
        if len(iPWMctrl) < m2Const.RcPWMchanNum:
            for ii in range(m2Const.RcPWMchanNum-len(iPWMctrl)):
                iPWMctrl.append(0)
        for ii in range(m2Const.RcPWMchanNum):
            if iPWMctrl[ii] < 0:
                iPWMctrl[ii] = iPWMctrl[ii] + 256
            #PWMctrl_bytes.append(bytes(ctypes.c_int8(iPWMctrl[ii])))
        self.cmd_i8AarrServos = iPWMctrl

    def setPWM_n_pm1(self,n,pm1Val=0):
        if n < 0 or n >= m2Const.RcPWMchanNum:
            print("m2ctrl m2ctrl Servo %d doesn't exist, only [0 to %d]"%(n,m2Const.RcPWMchanNum-1))
            pass
        else:
            if pm1Val > 1.0 or pm1Val < -1.0:
                print("m2ctrl m2ctrl acceptable Servo ctrl input range [-1,1]")
                return
            else:
                self.cmd_i8AarrServos[n:n+1] = ctypes.c_int8(servo_pm1ctrl_to_i8(pm1Val))
                self.Servo_beingUsed |= (1<<n)
                #print("PwmCh(%d):%d"%(n,self.cmd_i8AarrServos[n]))

    def motorHbridgeCtrl_pm1(self,index0to2, speed_pm1):
        if index0to2 < 0 or index0to2 > 2:
            print('m2ctrl motorHbridgeCtrl index can only be in the range of [0,2]')
            return
        if speed_pm1 > 1.0 or speed_pm1 < -1.0:
            print('m2ctrl motorHbridgeCtrl speed_pm1 can only be in the range of [-1,1]')
            return
        self.setPWM_n_pm1(index0to2*2,speed_pm1)
        
    def centerServo_n(self,n):
        if n < 0 or n >= m2Const.RcPWMchanNum:
            print("m2ctrl Servo %d doesn't exist, only [0 to %d]"%(n,m2Const.RcPWMchanNum-1))
            pass
        else:
            self.cmd_i8AarrServos[n] = 0
            self.Servo_beingUsed |= (1<<n)
            
    def __handleTelemetryDataPkg(self):
        if self.m_CBmain is None:
            defaultTelemDataProcess(self.m_decodedTelemetry)
        else:
            self.m_CBmain(self.m_decodedTelemetry)

    def readSettingData(self):
        if self.m_platform == m2Const.etDebian:
            self.m_setting = bleDataDecoder.decodeNVsetting(self.char1.read())
            return self.m_setting
        elif self.m_platform == m2Const.etAndroid or self.m_platform == m2Const.etLocalNet:
            print("m2ctrl In android platform, we use app to configure this setting")
        elif self.m_platform == m2Const.etInternetController:
            print("m2ctrl read Setting not supported now, to be added later")
        else:
            print("m2ctrl unhandled platform definition")
            return None

    def readTelemetryData(self):
        self.connect()
        if self.m_platform == m2Const.etDebian:
            if self.m_currentBleDeviceIndex is not None:
                fwType = self.m_fwTypeList[self.m_currentBleDeviceIndex]
                self.m_decodedTelemetry = bleDataDecoder.decodeRawBleTelemetry(self.char4.read(),fwType)
        elif self.m_platform == m2Const.etInternetController or self.m_platform == m2Const.etLocalNet or self.m_platform == m2Const.etAndroid:
            print("functionality to be completed")
            return None
        else:
            print("m2ctrl unhandled platform definition")
            return None
        self.__handleTelemetryDataPkg()
        return self.m_decodedTelemetry
  
    def setTime0(self):
        self.m_startTimeS = time.time()
        
    def secSinceTime0(self):
        return time.time() - self.m_startTimeS

class DelegateIfc(btle.DefaultDelegate):
    def __init__(self, callback = None, etFWtype = constShared.fwImage_generic):
        btle.DefaultDelegate.__init__(self)
        if callback:
            self.m_CBmain = callback
        else:
            self.m_CBmain = None
        self.__etFWtype = etFWtype

    def handleNotification(self, cHandle, data):
        if self.m_CBmain is None:
            defaultTelemDataProcess(self.m_decodedTelemetry,self.__etFWtype)
        else:
            self.m_CBmain(bleDataDecoder.decodeRawBleTelemetry(data,self._DelegateIfc__etFWtype))
        
def defaultTelemDataProcess(telemetry,etFWtype):
    '''
    print("\nseqID(%d)------------------------------------------------------------------"%telemetry['SeqID'])
    print("x/y/z:\tRPY(deg)\tAccel(mG)\tGyro(dps)\tMag(mGauss)")
    for ii in range(3):
        print("axis%d: %8.2f\t\t%8.2f\t%8.2f\t%8.2f"%(ii,telemetry['fRPYdeg'][ii],telemetry['fAccel_mG'][ii],telemetry['fGyro_dps'][ii],telemetry['fMag_mGauss'][ii]))
    GPIOinput = telemetry['GPIOinput']
    print("GPIO status %d %d %d %d %d %d"%(GPIOinput&(1<<0)==0,GPIOinput&(1<<1)==0,GPIOinput&(1<<2)==0,GPIOinput&(1<<3)==0,GPIOinput&(1<<4)==0,GPIOinput&(1<<5)==0)) 
    print("Battery: %3.2f(V)\tCompass:%d(deg)\ttemperature:%3.2f(Deg)"%(telemetry['BatteryVolt'],telemetry['CompassDeg'],telemetry['temperatureDeg']))
    '''
    pass

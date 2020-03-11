from ctypes import *
from ctypes.wintypes import *
from enum import Enum
import time
import platform
import sys

name="TModule"

#print(platform.architecture())
is64bit = sys.maxsize > 2**32
if is64bit :
    dllName="AnapassTModule.dll"
else :
    dllName="AnapassTModule32.dll"

try:
    Load_DLL = WinDLL(dllName)
except OSError as err:
    print("OS error: {0}".format(err))
    print("Load DLL from CurrentFolder " + "(./" + dllName + ")")
    Load_DLL = WinDLL('./' + dllName)

print("Load DLL " + dllName)

#TDEVICE_API TED_RESULT TSys_WinInit();
TSys_WinInit = Load_DLL['TSys_WinInit']
TSys_WinInit.restype=c_int;

#TDEVICE_API TDEVICE_HDL TDevice_Create(const TED_CHAR* fileName);
TDevice_Create=Load_DLL['TDevice_Create']
TDevice_Create.restype=c_void_p
TDevice_Create.argtypes=[c_char_p]

#TDEVICE_API TED_RESULT TDevice_Destroy(TDEVICE_HDL hdl);
TDevice_Destroy=Load_DLL['TDevice_Destroy']
TDevice_Destroy.restype=c_int;
TDevice_Destroy.argtypes=[c_void_p]

#TDEVICE_API TED_RESULT TDevice_Connect(TDEVICE_HDL hdl); 
TDevice_Connect = Load_DLL['TDevice_Connect']
TDevice_Connect.restype=c_int;
TDevice_Connect.argtypes=[c_void_p]

#TDEVICE_API TED_RESULT TDevice_Disconnect(TDEVICE_HDL hdl);
TDevice_Disconnect = Load_DLL['TDevice_Disconnect']
TDevice_Disconnect.restype=c_int;
TDevice_Disconnect.argtypes=[c_void_p]

#TDEVICE_API TED_RESULT TDevice_IsConnect(TDEVICE_HDL hdl);
TDevice_IsConnect = Load_DLL['TDevice_IsConnect']
TDevice_IsConnect.restype=c_int;
TDevice_IsConnect.argtypes=[c_void_p]

#TDEVICE_API TED_RESULT TDevice_SendTxtCmd(TDEVICE_HDL hdl, const TED_CHAR* cmd,  /*OUT*/ TED_CHAR* resp, TED_INT respMaxSize, TED_INT respDurMileSecond);
TDevice_SendTxtCmd = Load_DLL['TDevice_SendTxtCmd']
TDevice_SendTxtCmd.restype=c_int;
TDevice_SendTxtCmd.argtypes=[c_void_p, c_char_p, c_char_p, c_int, c_int]

#TDEVICE_API TED_RESULT TDevice_ReadRegValue(TDEVICE_HDL hdl, TED_REGADDR regAddr, TED_INT level2Offset, TED_INT readCnt, /*OUT*/ TED_REGVALUE* regValue);
TDevice_ReadRegValue = Load_DLL['TDevice_ReadRegValue']
TDevice_ReadRegValue.restype=c_int;
TDevice_ReadRegValue.argtypes=[c_void_p, c_char, c_int, c_int, c_char_p]

TSys_WinInit()

def convert_ctype(x):
   return x.encode('utf-8')

#
# class TDevice
#
class TDevice :

    TMonitor=1
    
    __DeviceHandle = c_void_p(0)  # private member variable

    def __init__(this, deviceType):

        if deviceType == TDevice.TMonitor :
            this.__DeviceHandle = TDevice_Create(convert_ctype('TMonitor://localhost'))
        else :
            this.__DeviceHandle = c_void_p(0)

    def __del__(this):
        #print("TDevice::~TDevice")
        TDevice_Destroy(this.__DeviceHandle)
     
    def Connect(this) :
        ret = TDevice_Connect(this.__DeviceHandle)
        if ret==0 :
            bflag = True
        else :
            bflag = False;
        return bflag

    def Disonnect(this) :
        return TDevice_Disconnect(this.__DeviceHandle)

    def ReadReg(this, regAddr, level2Offset, readCount, regValueArray) :
        ret = TDevice_ReadRegValue(this.__DeviceHandle, regAddr, level2Offset, readCount, regValueArray)
        if ret==0 :
            bflag = True
        else :
            bflag = False;
        return bflag



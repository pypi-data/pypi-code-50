from ctypes import *
from ctypes.wintypes import *
from enum import Enum
import time
import platform
import sys
import pkg_resources  # part of setuptools
import enum
import struct

PackageName="anapass-python"
ModuleName="TModule"
version = pkg_resources.require(PackageName)[0].version

DisplayName="[" + PackageName + ":" + ModuleName + "] "


print("--------------------------------------------------------------------------------")
print(DisplayName + version)


#print(platform.architecture())
is64bit = sys.maxsize > 2**32
if is64bit :
    dllName="AnapassTModule.dll"
else :
    dllName="AnapassTModule32.dll"

print(DisplayName + "Try:  Loading DLL (" + dllName + ")")
try:
    Load_DLL = WinDLL(dllName)
except OSError as err:
    print("OS error: {0}".format(err))
    print("Load DLL from CurrentFolder " + "(./" + dllName + ")")
    Load_DLL = WinDLL('./' + dllName)

print(DisplayName + "Success:  Loading DLL (" + dllName + ")")

print(DisplayName + "Try:  Loading Symbol ")
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

#TDEVICE_API TED_RESULT TDevice_SendCtrlCmd(TDEVICE_HDL hdl, const TED_CHAR* cmd,  /*OUT*/ TED_CHAR* resp, TED_INT respMaxSize, TED_INT respDurMileSecond);
TDevice_SendCtrlCmd = Load_DLL['TDevice_SendCtrlCmd']
TDevice_SendCtrlCmd.restype=c_int;
TDevice_SendCtrlCmd.argtypes=[c_void_p, c_char_p, c_char_p, c_int, c_int]

#TDEVICE_API TED_RESULT TDevice_ReadRegValue(TDEVICE_HDL hdl, TED_REGADDR regAddr, TED_INT byteOffset, TED_INT readCnt, /*OUT*/ TED_REGVALUE* regValue);
TDevice_ReadRegValue = Load_DLL['TDevice_ReadRegValue']
TDevice_ReadRegValue.restype=c_int;
TDevice_ReadRegValue.argtypes=[c_void_p, c_char, c_int, c_int, c_char_p]

#TDEVICE_API TED_RESULT TDevice_ReadRegValue1Byte(TDEVICE_HDL hdl, TED_REGADDR regAddr, TED_INT byteOffset, /*OUT*/TED_REGVALUE* regValue);
TDevice_ReadRegValue1Byte = Load_DLL['TDevice_ReadRegValue1Byte']
TDevice_ReadRegValue1Byte.restype=c_int;
TDevice_ReadRegValue1Byte.argtypes=[c_void_p, c_char, c_int, c_char_p]

#TDEVICE_API TED_RESULT TDevice_WriteRegValue(TDEVICE_HDL hdl, TED_REGADDR regAddr, TED_INT byteOffset, TED_INT writeCnt,  TED_REGVALUE* regValue);
TDevice_WriteRegValue = Load_DLL['TDevice_WriteRegValue']
TDevice_WriteRegValue.restype=c_int;
TDevice_WriteRegValue.argtypes=[c_void_p, c_char, c_int, c_int, c_char_p]

#TDEVICE_API TED_RESULT TDevice_WriteRegValue1Byte(TDEVICE_HDL hdl, TED_REGADDR regAddr, TED_INT byteOffset, TED_REGVALUE regValue);
TDevice_WriteRegValue1Byte = Load_DLL['TDevice_WriteRegValue1Byte']
TDevice_WriteRegValue1Byte.restype=c_int;
TDevice_WriteRegValue1Byte.argtypes=[c_void_p, c_char, c_int, c_char]

#TDEVICE_API TED_RESULT TDevice_CatchPowerInfo(TDEVICE_HDL hdl, /*OUT*/struct TED_POWER_INFO* p_pwrinfo, TED_INT timeOut /*milisec */)
TDevice_CatchPowerInfo = Load_DLL['TDevice_CatchPowerInfo']
TDevice_CatchPowerInfo.restype=c_int;
TDevice_CatchPowerInfo.argtypes=[c_void_p, c_char_p, c_int]


print(DisplayName + "Success:  Loading Symbol ")


print(DisplayName + "Try: System Init")
TSys_WinInit()
print(DisplayName + "Success: System Init")
print("--------------------------------------------------------------------------------")
print("")


class TString :
    def __init__(this, str):
        this.__String = str

    def ToCTypeString(this) :
        return this.__String.encode('utf-8')

    #static method
    def ConvertToCTypeStrng(x) :
        return x.encode('utf-8')

    
#
# enu class TDevType
#


class TPower :

    class Type(enum.IntEnum) :
        VBAT1=0
        ELVSS=1
        VDD1=2
        VCI1=3
        VBAT2=4
        VDD2=5
        VCI2=6

    def __init__(this):
        this.No = 0
        this.Avail=[0 for _ in range(10)]
        this.Value1=[0 for _ in range(10)]
        this.Voltage=[0.0 for _ in range(10)]
        this.Current=[0.0 for _ in range(10)]
        this.Range1=[0.0 for _ in range(10)]
        this.Range2=[0.0 for _ in range(10)]
#
# class TDevice
#
class TDevice :

    class Type(enum.Enum) : 
        T4 = enum.auto()
        T5 = enum.auto()

    
    def __init__(this, deviceType):
        #print(DisplayName +"TRY: create " + deviceType.name )
        if deviceType == TDevice.Type.T4  or deviceType == TDevice.Type.T5 :
            this.__DeviceHandle = TDevice_Create(TString.ConvertToCTypeStrng('TMonitor://localhost'))
        else :
            this.__DeviceHandle = c_void_p(0)
        #print(DisplayName +"Success: create " + deviceType.name )
        this.__DeviceType = deviceType

        #struct TED_POWER_INFO {
        #    TED_S32 no;
        #    TED_S32 available[10];
        #    TED_S32 value1[10];
        #    TED_FLOAT fV[10];
        #    TED_FLOAT fA[10];
        #    TED_FLOAT fRange1[10];
        #    TED_FLOAT fRange2[10];dir

        #};

        this.__PowerStructFmt = 'i'    #    TED_S32 no;    
        this.__PowerStructFmt+='10i'   # TED_S32 available[10];
        this.__PowerStructFmt+='10i'   # TED_S32 value[10];
        this.__PowerStructFmt+='10f'   # TED_FLOAT fV[10];
        this.__PowerStructFmt+='10f'   # TED_FLOAT fV[10];
        this.__PowerStructFmt+='10f'   # TED_FLOAT fRange1[10];
        this.__PowerStructFmt+='10f'   # TED_FLOAT fRange2[10];
        
        # arg=list(range(61))

        this.__PowerStructData = struct.pack(this.__PowerStructFmt, 0,
                           0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                           0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                           0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
                           0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
                           0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
                           0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
                           )

    def __del__(this):
        #print("TDevice::~TDevice")
        TDevice_Destroy(this.__DeviceHandle)

    def GetName(this) :
        return this.__DeviceType.name
     
    def Connect(this) :
        ret = TDevice_Connect(this.__DeviceHandle)
        if ret==0 :
            bflag = True
        else :
            bflag = False;
        return bflag

    def Disonnect(this) :
        return TDevice_Disconnect(this.__DeviceHandle)
    
    def SendTxtCmd(this, cmd) :
        ret = TDevice_SendTxtCmd(this.__DeviceHandle, TString.ConvertToCTypeStrng(cmd), c_char_p(0), 0, 0)
        if ret==0 :
            bflag = True
        else :
            bflag = False;
        return bflag

    #private methond
    def __SendCtrlCmd(this, cmd) :  
        ret = TDevice_SendCtrlCmd(this.__DeviceHandle, TString.ConvertToCTypeStrng(cmd), c_char_p(0), 0, 0)
        if ret==0 :
            bflag = True
        else :
            bflag = False;
        return bflag

    def Reset(this) :
        return this.__SendCtrlCmd('RESET')

    def Next(this) :
        return this.__SendCtrlCmd('NEXT')

    def Back(this) :
        return this.__SendCtrlCmd('BACK')

    def ReadReg(this, regAddr, byteOffset, readCount, regValueList) :
        regValueInt = 0
        regValueByteArray=bytes(readCount)
        ret = TDevice_ReadRegValue(this.__DeviceHandle, regAddr, byteOffset, readCount, regValueByteArray)
        if ret==0 :
            for idx, regValueByte in enumerate(regValueByteArray) :
                regValueInt = regValueByte
                regValueInt &= 0xFF
                regValueList[idx] = regValueInt
            bflag = True
        else :
            bflag = False;
        return bflag

    def ReadReg1Byte(this, regAddr, byteOffset) :
        regValueArray=bytes(1)
        ret = TDevice_ReadRegValue1Byte(this.__DeviceHandle, regAddr, byteOffset, regValueArray)
        if ret==0 :
            regValue = regValueArray[0]
            regValue &= 0xFF
        else :
            regValue = -1
        return regValue

    def WriteReg(this, regAddr, byteOffset, writeCount, regValueList) :
        ret = TDevice_WriteRegValue(this.__DeviceHandle, regAddr, byteOffset, writeCount, bytes(regValueList))
        if ret==0 :
            bflag = True
        else :
            bflag = False;
        return bflag

    def WriteReg1Byte(this, regAddr, byteOffset, regValue) :
        ret = TDevice_WriteRegValue1Byte(this.__DeviceHandle, regAddr, byteOffset, c_char(regValue))
        if ret==0 :
            bflag = True
        else :
            bflag = False;
        return bflag

    def WriteCtrlReg(this, regAddr) :
        return this.WriteReg1Byte(regAddr, 0, 1)

    def CatchPower(this, powerInfo) :

        ret = TDevice_CatchPowerInfo(this.__DeviceHandle,  this.__PowerStructData, 1000)

        result= struct.unpack(this.__PowerStructFmt, this.__PowerStructData)

        resIdx=0
        
        powerInfo.No = result[resIdx] 
        resIdx += 1

        for i in range(10) :
            powerInfo.Avail[i] = result[i+resIdx]
        resIdx += 10

        for i in range(10) :
            powerInfo.Value1[i] = result[i+resIdx]
        resIdx += 10

        for i in range(10) :
            powerInfo.Voltage[i] = result[i+resIdx]
        resIdx += 10

        for i in range(10) :
            powerInfo.Current[i] = result[i+resIdx]
        resIdx += 10

        for i in range(10) :
            powerInfo.Range1[i] = result[i+resIdx]
        resIdx += 10

        for i in range(10) :
            powerInfo.Range2[i] = result[i+resIdx]
        resIdx += 10

        if ret==0 :
            bflag = True
        else :
            bflag = False;
        return bflag


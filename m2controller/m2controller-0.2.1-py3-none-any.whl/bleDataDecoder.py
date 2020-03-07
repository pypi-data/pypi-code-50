#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from m2controller import m2Const, constShared

def decodeNVsetting(byteArr):
    NVsetting = {
        "CH0dutyCycleMode":(byteArr[0]&(0x1<<0))>0,
        "CH1dutyCycleMode":(byteArr[0]&(0x1<<1))>0,
        "CH2dutyCycleMode":(byteArr[0]&(0x1<<2))>0,
        "CH3dutyCycleMode":(byteArr[0]&(0x1<<3))>0,
        "CH4dutyCycleMode":(byteArr[0]&(0x1<<4))>0,
        "CH5dutyCycleMode":(byteArr[0]&(0x1<<5))>0,
        "CH01_merged2be_H_bridge":(byteArr[1]&(0x1<<0))>0,
        "CH23_merged2be_H_bridge":(byteArr[1]&(0x1<<1))>0,
        "CH45_merged2be_H_bridge":(byteArr[1]&(0x1<<2))>0,
    };    
    return NVsetting

def decodeRawBleTelemetry(byteArr,fwType):
    for ii in range(len(byteArr)):
            if byteArr[ii] < 0:
                byteArr[ii] = byteArr[ii] + 256
                
    SeqID = byteArr[m2Const.ByteIndex0Seq_n_Btn] & 0x3
    GPIOdata = (byteArr[m2Const.ByteIndex0Seq_n_Btn] & 0xFC) >> 2
    BtnStatus = []
    for ii in range(m2Const.USR_BTN_CNT):
        BtnStatus.append((GPIOdata>>ii)&0x1 != 0)
    fVoltage = byteArr[m2Const.ByteIndex0ADC1_1tenthV] / 10.0
    fTemperatureDeg = byteArr[m2Const.ByteIndex0Tmpture]/10
                
    if fwType == constShared.fwImage_compass or fwType == constShared.fwImage_generic:
        fRPYdeg=[0,0,0]
        fAccelHwUnit=[0,0,0]
        fGyroHwUnit=[0,0,0]
        fMagHwUnit=[0,0,0]
        for ii in range(3):
            byte0 = ii*m2Const.FC_STATUS_EACH_AXIS_BYTE;
            i16byteArr = bytearray([0x0, 0x0]);
            i16byteArr[0] = ((byteArr[byte0+0]&0x03) << 6);
            piece0 = ((byteArr[byte0+0]&0xFC) >> 2);
            piece1 = ((byteArr[byte0+1]&0x03) << 6);
            i16byteArr[1] = (piece0 + piece1);
            i16value = int.from_bytes(i16byteArr, byteorder='little', signed=True)
            i16value = i16value >> 6;
            fRPYdeg[ii] = (i16value/m2Const.RPY_floatIntConversion);
    
            i16byteArr[0] = ((byteArr[byte0+1]&0x0C) << 4);
            piece0 = ((byteArr[byte0+1]&0xF0) >> 4);
            piece1 = ((byteArr[byte0+2]&0x0F) << 4);
            i16byteArr[1] = (piece0 + piece1);
            i16value = int.from_bytes(i16byteArr, byteorder='little', signed=True)
            i16value = i16value >> (6-m2Const.LSB_DROP_ACC-1);
            fAccelHwUnit[ii] = i16value;
    
            i16byteArr[0] = ((byteArr[byte0+2]&0x30) << 2);
            piece0 = ((byteArr[byte0+2]&0xC0) >> 6);
            piece1 = ((byteArr[byte0+3]&0x3F) << 2);
            i16byteArr[1] = (piece0 + piece1);
            i16value= int.from_bytes(i16byteArr, byteorder='little', signed=True)
            i16value = i16value >> (6-m2Const.LSB_DROP_GYR-3);
            fGyroHwUnit[ii] = i16value;
    
            i16byteArr[0] = ((byteArr[byte0+3]&0xC0));
            i16byteArr[1] = byteArr[byte0+4];
            i16value = int.from_bytes(i16byteArr, byteorder='little', signed=True)
            i16value = i16value >> (6-m2Const.LSB_DROP_MAG);
            fMagHwUnit[ii] = i16value;
            
        iCompass_pm180deg = byteArr[m2Const.ByteIndex0Compass] * 2 -180
        telemetry = {
            "m_BtnStatus":BtnStatus,
            "m_SeqID":SeqID,
            "m_fAccelHwUnit":fAccelHwUnit,
            "m_fGyroHwUnit":fGyroHwUnit,
            "m_fMagHwUnit":fMagHwUnit,
            "m_fPhoneRPYdeg":[0.0,0.0,0.0],
            "m_fRPYdeg":fRPYdeg,
            "m_fTemperatureDeg":fTemperatureDeg,
            "m_fVoltage":fVoltage,
            "m_iCompass_pm180deg":iCompass_pm180deg,
            };
    elif fwType == constShared.fwImage_stepMotor:
        telemetry = {
            "m_BtnStatus":BtnStatus,
            "m_SeqID":SeqID,
            "m_fTemperatureDeg":fTemperatureDeg,
            "m_fVoltage":fVoltage,
            "m_stepMotorStatus":byteArr[0:constShared.StepMotorCnt]
            };        
    elif fwType == constShared.fwImage_cmdSeq:
        timeOneTenthSecInOneDay = int.from_bytes(byteArr[0:4], byteorder='little')
        i32timeStampOneTenthS = int.from_bytes(byteArr[4:8], byteorder='little')
        u16_rd_ii = int.from_bytes(byteArr[8:10], byteorder='little')
        telemetry = {
            "m_BtnStatus":BtnStatus,
            "m_SeqID":SeqID,
            "m_fTemperatureDeg":fTemperatureDeg,
            "m_fVoltage":fVoltage,
            "timeOneTenthSecInOneDay":timeOneTenthSecInOneDay,
            "i32timeStampOneTenthS":i32timeStampOneTenthS,
            "u16_rd_ii":u16_rd_ii
            };
    else:
        telemetry = None
        print("bleDataDecoder missing handling for FW type: {}".format(fwType))
    return telemetry

#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# do NOT modify this file, use generateSharedConstDef.py to produce this file
emoPic_Invalid = 0;
emoPic_angry = 1;
emoPic_cry = 2;
emoPic_disappoint = 3;
emoPic_happy = 4;
emoPic_kiss = 5;
emoPic_surprise = 6;
emoPic_blank = 7;
emoPic_number = 8;
FC_CTRL_MSG_PREAMBLE_LEN = 2;
FC_CTRL_MSG_PREAMBLE_TYPE_TX0 = 0x0;
FC_CTRL_MSG_PREAMBLE_TYPE_TX1 = 0xFF;
FC_CTRL_MSG_PREAMBLE_TYPE_SETNAME0 = 0x55;
FC_CTRL_MSG_PREAMBLE_TYPE_SETNAME1 = 0xAA;
FC_CTRL_MSG_PREAMBLE_TYPE_SET_PID0 = 0x17;
FC_CTRL_MSG_PREAMBLE_TYPE_SET_PID1 = 0x88;
FC_CTRL_MSG_PREAMBLE_TYPE_SEND_UART0 = 0x20;
FC_CTRL_MSG_PREAMBLE_TYPE_SEND_UART1 = 0x17;
FC_CTRL_MSG_PREAMBLE_TYPE_FLASHACTION0 = 0x31;
FC_CTRL_MSG_PREAMBLE_TYPE_FLASHACTION1 = 0x41;
flashaction_etActionSave2Flash = 1; # must be the first entry
flashaction_etEndOfSequence = 2;
flashaction_etResetExecGo = 3;
flashaction_etResetFlashStorage = 4;
flashaction_etSetTimeOneTenthS = 5; # must be the last entry
# 5 bytes: first 3 bytes arbitrary RGB setting(in a rare case it can be M2R). next 2 bytes in real data can never be identical
PROTOCOL_PREAMBLE = b"M2Rbb";
PROTOCOL_LENBYTES = 2;
FC_CTRL_BLE_MSGTYPE_LEN = 2;
FC_CTRL_MSG_PREAMBLE_TYPE_TX = bytearray([FC_CTRL_MSG_PREAMBLE_TYPE_TX0, FC_CTRL_MSG_PREAMBLE_TYPE_TX1]);
FC_CTRL_MSG_PREAMBLE_TYPE_TX = bytearray([FC_CTRL_MSG_PREAMBLE_TYPE_SETNAME0, FC_CTRL_MSG_PREAMBLE_TYPE_SETNAME1]);
FC_CTRL_MSG_PREAMBLE_TYPE_TX = bytearray([FC_CTRL_MSG_PREAMBLE_TYPE_SET_PID0, FC_CTRL_MSG_PREAMBLE_TYPE_SET_PID1]);
FC_CTRL_MSG_PREAMBLE_TYPE_TX = bytearray([FC_CTRL_MSG_PREAMBLE_TYPE_SEND_UART0, FC_CTRL_MSG_PREAMBLE_TYPE_SEND_UART1]);
FC_CTRL_MSG_SET_PID_Byte0_forValue = 4;

# step motor control and status report settings
StepMotorCnt = 2;
stepMotorRollIndex = 0;
stepMotorPitchIndex = 1;
stepMotorStatusBit_etEmergencyStopped = 0;
stepMotorStatusBit_etOriginReached = 1;
stepMotorStatusBit_etRngLimitReached = 2;
stepMotorStatusBit_etJobCompleted = 3;
stepMotorStatusBit_etMotorBusy = 4;

# 2640 to host Char4 message type definition
telemetryType_etGenericCtrl = 0;
telemetryType_etStepperMotorCtrl = 1;
telemetryType_etHwIfcReading = 2;
etRoll_PwmCH = 0;
etPitchPwmCH = 1;
etThrotPwmCH = 2;
etRudd_PwmCH = 3;
etAUX1_PwmCH = 4;
etAUX2_PwmCH = 5;
etAUX4_CH = 6;
etAUX5_CH = 7;
etAUX6_CH = 8;
etAUX7_CH = 9;
etFlightModeCH = 10;
etGPIO_CTRL_BYTE = 11;
INVALID_i8_RC_CTRL_CMD = -128;
# Hardware PWM available on GPIO12, GPIO13, GPIO18, GPIO19
# https://www.raspberrypi.org/documentation/usage/gpio/README.md
# GPIO18 used for WS2812 PWM ctrl
RPiPwmCtlCnt = 3;
fwImage_compass = 'v';
fwImage_stepMotor = 's';
fwImage_cmdSeq = 'h';
fwImage_generic = 'g';

bleDevScanNameLen = 17;

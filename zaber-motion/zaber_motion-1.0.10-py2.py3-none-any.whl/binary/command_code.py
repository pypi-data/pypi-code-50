﻿# ===== THIS FILE IS GENERATED FROM A TEMPLATE ===== #
# ============== DO NOT EDIT DIRECTLY ============== #
from enum import Enum


class CommandCode(Enum):
    """
    Named constants for all Zaber Binary protocol commands.
    """

    RESET = 0
    HOME = 1
    RENUMBER = 2
    STORE_CURRENT_POSITION = 16
    RETURN_STORED_POSITION = 17
    MOVE_TO_STORED_POSITION = 18
    MOVE_ABSOLUTE = 20
    MOVE_RELATIVE = 21
    MOVE_AT_CONSTANT_SPEED = 22
    STOP = 23
    SET_ACTIVE_AXIS = 25
    SET_SERVO_CHANNEL = 25
    SET_AXIS_DEVICE_NUMBER = 26
    SET_POSITION = 26
    SET_AXIS_INVERSION = 27
    SET_ON_TIME = 27
    SET_AXIS_VELOCITY_PROFILE = 28
    SET_AXIS_VELOCITY_SCALE = 29
    LOAD_EVENT_INSTRUCTION = 30
    RETURN_EVENT_INSTRUCTION = 31
    SET_CALIBRATION_MODE = 33
    SET_JOYSTICK_CALIBRATION_MODE = 33
    READ_OR_WRITE_MEMORY = 35
    RESTORE_SETTINGS = 36
    SET_MICROSTEP_RESOLUTION = 37
    SET_RUNNING_CURRENT = 38
    SET_HOLD_CURRENT = 39
    SET_DEVICE_MODE = 40
    SET_HOME_SPEED = 41
    SET_START_SPEED = 41
    SET_TARGET_SPEED = 42
    SET_ACCELERATION = 43
    SET_MAXIMUM_POSITION = 44
    SET_CURRENT_POSITION = 45
    SET_MAXIMUM_RELATIVE_MOVE = 46
    SET_HOME_OFFSET = 47
    SET_ALIAS_NUMBER = 48
    SET_LOCK_STATE = 49
    RETURN_DEVICE_ID = 50
    RETURN_FIRMWARE_VERSION = 51
    RETURN_POWER_SUPPLY_VOLTAGE = 52
    RETURN_SETTING = 53
    RETURN_STATUS = 54
    ECHO_DATA = 55
    RETURN_FIRMWARE_BUILD = 56
    RETURN_CURRENT_POSITION = 60
    RETURN_SERIAL_NUMBER = 63
    SET_PARK_STATE = 65
    SET_PERIPHERAL_ID = 66
    RETURN_DIGITAL_INPUT_COUNT = 67
    READ_DIGITAL_INPUT = 68
    READ_ALL_DIGITAL_INPUTS = 69
    RETURN_DIGITAL_OUTPUT_COUNT = 70
    READ_DIGITAL_OUTPUT = 71
    READ_ALL_DIGITAL_OUTPUTS = 72
    WRITE_DIGITAL_OUTPUT = 73
    WRITE_ALL_DIGITAL_OUTPUTS = 74
    RETURN_ANALOG_INPUT_COUNT = 75
    READ_ANALOG_INPUT = 76
    RETURN_ANALOG_OUTPUT_COUNT = 77
    MOVE_INDEX = 78
    SET_INDEX_DISTANCE = 79
    SET_CYCLE_DISTANCE = 80
    SET_FILTER_HOLDER_ID = 81
    RETURN_ENCODER_COUNT = 82
    RETURN_CALIBRATED_ENCODER_COUNT = 83
    RETURN_CALIBRATION_TYPE = 84
    RETURN_CALIBRATION_ERROR = 85
    SET_PERIPHERAL_SERIAL_NUMBER = 86
    FORCE_ABSOLUTE = 87
    FORCE_OFF = 88
    RETURN_ENCODER_POSITION = 89
    SET_AUTO_REPLY_DISABLED_MODE = 101
    SET_MESSAGE_ID_MODE = 102
    SET_HOME_STATUS = 103
    SET_HOME_SENSOR_TYPE = 104
    SET_AUTO_HOME_DISABLED_MODE = 105
    SET_MINIMUM_POSITION = 106
    SET_KNOB_DISABLED_MODE = 107
    SET_KNOB_DIRECTION = 108
    SET_KNOB_MOVEMENT_MODE = 109
    SET_KNOB_JOG_SIZE = 110
    SET_KNOB_VELOCITY_SCALE = 111
    SET_KNOB_VELOCITY_PROFILE = 112
    SET_ACCELERATION_ONLY = 113
    SET_DECELERATION_ONLY = 114
    SET_MOVE_TRACKING_MODE = 115
    SET_MANUAL_MOVE_TRACKING_DISABLED_MODE = 116
    SET_MOVE_TRACKING_PERIOD = 117
    SET_CLOSED_LOOP_MODE = 118
    SET_SLIP_TRACKING_PERIOD = 119
    SET_STALL_TIMEOUT = 120
    SET_DEVICE_DIRECTION = 121
    SET_BAUDRATE = 122
    SET_PROTOCOL = 123
    CONVERT_TO_ASCII = 124

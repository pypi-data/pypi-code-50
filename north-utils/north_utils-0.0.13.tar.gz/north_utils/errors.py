from typing import Optional


class Error(Exception):
    code = 0
    message = 'Success'

    def __init__(self, message: Optional[str]=None):
        Exception.__init__(self, message if message is not None else self.message)


class Timeout(Error):
    code = 1
    message = 'Timeout'


class InvalidCommand(Error):
    code = 2
    message = 'Invalid command name'


class InvalidArgument(Error):
    code = 3
    message = 'Invalid command argument'


class InvalidSeparator(Error):
    code = 4
    message = 'Invalid command separator'


class TooManyArguments(Error):
    code = 5
    message = 'Too many command arguments'


class CommandNotFound(Error):
    code = 6
    message = 'Command not found'


class InvalidArguments(Error):
    code = 7
    message = 'Invalid arguments'


class InvalidAxis(Error):
    code = 8
    message = 'Invalid axis'


class InvalidPosition(Error):
    code = 9
    message = 'Invalid position'


class InvalidVelocity(Error):
    code = 10
    message = 'Invalid velocity'


class InvalidAcceleration(Error):
    code = 11
    message = 'Invalid acceleration'


class AxisMoving(Error):
    code = 12
    message = 'Axis moving'


class EepromRead(Error):
    code = 13
    message = 'EEPROM read failed'


class EepromWrite(Error):
    code = 14
    message = 'EEPROM write failed'


class AxisFeatureUnavailable(Error):
    code = 15
    message = 'Axis feature unavailable'


class ModbusTimeout(Error):
    code = 16
    message = 'Modbus message timeout'


class ModbusInvalidResponse(Error):
    code = 17
    message = 'Invalid modbus response'


class InvalidTemperatureController(Error):
    code = 18
    message = 'Invalid temperature controller'


class InvalidJoint(Error):
    code = 19
    message = 'Invalid joint'


class InvalidCrc(Error):
    code = 20
    message = 'Invalid CRC'


class Homing(Error):
    code = 21
    message = 'Homing'


class InvalidFirstChar(Error):
    code = 22
    message = 'Invalid first character'


class InvalidElbowBias(Error):
    code = 23
    message = 'Invalid elbow bias'


class InvalidComPort(Error):
    code = 24
    message = 'Invalid com port'


class SimulatedFeatureUnavailable(Error):
    code = 25
    message = 'Feature is not available when simulating'


class InvalidAddress(Error):
    code = 26
    message = 'Invalid address'


class HomingError(Error):
    code = 27
    message = 'Error while homing'


class HomeRequired(Error):
    code = 28
    message = 'Home required'


class I2CError(Error):
    code = 29
    message = 'i2c Error'


class NoCoresAvailable(Error):
    code = 30
    message = 'No available cores'

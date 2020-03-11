# Copyright (c) 2019 Gunakar Pvt Ltd
# All rights reserved.

# Redistribution and use in source and binary forms, with or without
# modification, are permitted (subject to the limitations in the disclaimer
# below) provided that the following conditions are met:

#      * Redistributions of source code must retain the above copyright notice,
#      this list of conditions and the following disclaimer.

#      * Redistributions in binary form must reproduce the above copyright
#      notice, this list of conditions and the following disclaimer in the
#      documentation and/or other materials provided with the distribution.

#      * Neither the name of the Gunakar Pvt Ltd/Plezmo nor the names of its
#      contributors may be used to endorse or promote products derived from this
#      software without specific prior written permission.

#      * This software must only be used with Plezmo elements manufactured by
#      Gunakar Pvt Ltd.

#      * Any software provided in binary or object form under this license must not be
#      reverse engineered, decompiled, modified and/or disassembled.

# NO EXPRESS OR IMPLIED LICENSES TO ANY PARTY'S PATENT RIGHTS ARE GRANTED BY
# THIS LICENSE. THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND
# CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A
# PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR
# CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
# EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
# PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR
# BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER
# IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

from enum import Enum
from plezmo.elements.plezmo_element import PlezmoElementImpl, EventListenerWrapper
from plezmo.elements.element_types import PlezmoElementType
from ..utils.constants import Constants
from ..utils.logger import Logger
from ..utils.msg_helper import PlezmoMsg
from ..plezmo_exceptions.exceptions import *

class PlezmoMotorElement(PlezmoElementImpl):

    def __init__(self, name, mac, conn_handle, device_manager):
        super(PlezmoMotorElement, self).__init__(name, PlezmoElementType.MOTOR, mac, conn_handle, device_manager)

    def start(self, speed, direction):
        """ Rotate the motor by number of RPMs in given direction
        Parameters
        ----------
        speed : MotorSpeed
            Speed of motor. Valid values are MotorSpeed.SLOW, MotorSpeed.MEDIUM and MotorSpeed.HIGH
        direction: MotorDirection
            Direction of rotation (clockwise or anticlockwise)
        """
        on_off_state = 0x01
        cmd_data = [0x30, 0x00]
        cmd_data.extend(PlezmoMsg.uint8_to_bytes(on_off_state))
        cmd_data.extend(PlezmoMsg.uint8_to_bytes(speed.value))
        cmd_data.extend(PlezmoMsg.uint8_to_bytes(direction.value))
        command = PlezmoMsg.generate_command(Constants.MSG_TYPE_COMMAND, cmd_data)
        self.send_cmd(command)

    def start_with_rpm(self, rpm, direction):
        """ Rotate the motor by number of RPMs in given direction
        Parameters
        ----------
        rpm : int
            Number of rotations per minute (RPM)
        direction: MotorDirection
            Direction of rotation (clockwise or anticlockwise)
        """

        if rpm > 220 or rpm < 11:
            raise ValueError()

        on_off_state = 0x01
        cmd_data = [0x30, 0x00]
        cmd_data.extend(PlezmoMsg.uint8_to_bytes(on_off_state))
        cmd_data.extend(PlezmoMsg.uint8_to_bytes(rpm))
        cmd_data.extend(PlezmoMsg.uint8_to_bytes(direction.value))
        command = PlezmoMsg.generate_command(Constants.MSG_TYPE_COMMAND, cmd_data)
        self.send_cmd(command)

    def rotate(self, num_rotations, direction):
        """ Rotate the motor by rotation type in given direction
        Parameters
        ----------
        num_rotations : MotorRotation
            QUARTER, HALF, ONE etc
        direction: MotorDirection
            Direction of rotation (clockwise or anticlockwise)
        """

        cmd_data = [0x31, 0x00]
        cmd_data.extend(PlezmoMsg.uint8_to_bytes(direction.value))
        cmd_data.extend(PlezmoMsg.uint8_to_bytes(num_rotations.value))
        command = PlezmoMsg.generate_command(Constants.MSG_TYPE_COMMAND, cmd_data)
        self.send_cmd(command)

    def stop(self):
        on_off_state = 0x02
        cmd_data = [0x30, 0x00]
        cmd_data.extend(PlezmoMsg.uint8_to_bytes(on_off_state))
        command = PlezmoMsg.generate_command(Constants.MSG_TYPE_COMMAND, cmd_data)
        self.send_cmd(command)

    def on_motor_stalled(self, listener):
        # event id for motor = 0x0B
        num_bytes_to_match = 1
        mask_before_match = [0xFF]
        self.add_listener(Constants.EVENT_MOTOR, EventListenerWrapper(listener, num_bytes_to_match, mask_before_match, [Constants.MOTOR_EVENT_STALL]))

class MotorEvent(Enum):
    STALL = 1
    @staticmethod
    def from_bytes(data):
        # not checking data right now as there is only one event
        return MotorEvent.STALL

class MotorDirection(Enum):
    CLOCKWISE = 2
    ANTICLOCKWISE = 3

class MotorRotation(Enum):
    QUARTER = 1
    HALF = 2
    ONE = 4
    TWO = 8
    THREE = 12

class MotorSpeed(Enum):
    HIGH = 100
    MEDIUM = 50
    SLOW = 25

class PlezmoMotor:
    def __init__(self, plezmoApi):
        self.plezmoApi = plezmoApi
        self._logger = Logger()

    def start(self, elementName, speed, direction):
        """start(elementName: String, speed: MotorSpeed, direction: MotorDirection)
        Start the motor at specified speed and direction

        :param elementName: Name of the element
        :param speed: Speed of motor. Valid values are MotorSpeed.SLOW, MotorSpeed.MEDIUM and MotorSpeed.HIGH
        :param direction: Direction of rotation. Valid vlaues are MotorDirection.CLOCKWISE and MotorDirection.ANTICLOCKWISE
        """
        # find element by name
        element = self.plezmoApi.getElementByName(elementName)
        if element == None:
            self._logger.error("Element {} not found".format(elementName))
            raise ElementNotFoundException(elementName)
        # execute command
        element.start(speed, direction)

    def startWithRPM(self, elementName, speed, direction):
        """startWithRPM(elementName: String, speed: int, direction: MotorDirection)
        Start the motor at specified speed and direction

        :param elementName: Name of the element
        :param speed: Speed of motor. Valid values are between 20 and 220 (inclusive)
        :param direction: Direction of rotation. Valid vlaues are MotorDirection.CLOCKWISE and MotorDirection.ANTICLOCKWISE
        """
        # find element by name
        element = self.plezmoApi.getElementByName(elementName)
        if element == None:
            self._logger.error("Element {} not found".format(elementName))
            raise ElementNotFoundException(elementName)
        # execute command
        element.start_with_rpm(speed, direction)

    def stop(self, elementName):
        """stop(elementName: String)
        Stop the motor

        :param elementName: Name of the element
        """
        # find element by name
        element = self.plezmoApi.getElementByName(elementName)
        if element == None:
            self._logger.error("Element {} not found".format(elementName))
            raise ElementNotFoundException(elementName)
        # execute command
        element.stop()

    def rotate(self, elementName, numRotations, direction):
        """rotate(elementName: String, numRotations: MotorRotation, direction: MotorDirection)
        Rotate the motor in pecified direction for specified number of rotations

        :param elementName: Name of the element
        :param numRotations: Number of rotations. Valid values are MotorRotation.QUARTER, MotorRotation.HALF, MotorRotation.ONE, MotorRotation.TWO and MotorRotation.THREE
        :param direction: Direction of rotation. Valid vlaues are MotorDirection.CLOCKWISE and MotorDirection.ANTICLOCKWISE
        """
        # find element by name
        element = self.plezmoApi.getElementByName(elementName)
        if element == None:
            self._logger.error("Element {} not found".format(elementName))
            raise ElementNotFoundException(elementName)
        # execute command
        element.rotate(numRotations, direction)

    def onStall(self, elementName, handler):
        """onStall(elementName: String, handler: FunctionName)
        Handle the stall event of Motor

        :param: elementName: Name of the Motor
        :param handler: Name of the handler function - must be defined before this call
        """
        # find element by name
        element = self.plezmoApi.getElementByName(elementName)
        if element == None:
            self._logger.error("Element {} not found".format(elementName))
            raise ElementNotFoundException(elementName)
        # execute command
        element.on_motor_stalled(handler)
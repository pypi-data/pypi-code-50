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

from plezmo.elements.plezmo_element import PlezmoElementImpl, PlezmoElement, EventListenerWrapper 
from plezmo.elements.element_types import PlezmoElementType 
from ..utils.logger import Logger 
from ..utils.constants import Constants 
from ..utils.msg_helper import PlezmoMsg 
from ..plezmo_exceptions.exceptions import *

class PlezmoMotionImpl(PlezmoElementImpl):

    def __init__(self, name, mac, conn_handle, device_manager):
        super(PlezmoMotionImpl, self).__init__(name, PlezmoElementType.MOTION, mac, conn_handle, device_manager)
        self._logger = Logger()

    def get_angle(self, direction):
        cmd_data = [0x76, 0]
        cmd_data.extend(PlezmoMsg.uint8_to_bytes(direction.value))
        command = PlezmoMsg.generate_command(Constants.MSG_TYPE_COMMAND, cmd_data)
        response = self.send_cmd(command)
        if response[0] == 0:
            return PlezmoMsg.bytes_to_signed_int(response[1:3])
        else:
            return response[0]

    def get_accelerometer_data(self, direction):
        cmd_data = [0x77, 0x00]
        cmd_data.extend(PlezmoMsg.uint8_to_bytes(direction.value))
        command = PlezmoMsg.generate_command(Constants.MSG_TYPE_COMMAND, cmd_data)
        response = self.send_cmd(command)
        if response[0] == 0:
            return PlezmoMsg.bytes_to_int32(response[1:5])
        else:
            return response[0]

    def set_tilt_threshold(self, threshold):
        cmd_data = [0x75, 0]
        cmd_data.extend(PlezmoMsg.uint8_to_bytes(0x01))
        cmd_data.extend(PlezmoMsg.uint8_to_bytes(threshold))
        command = PlezmoMsg.generate_command(Constants.MSG_TYPE_COMMAND, cmd_data)
        self.send_cmd(command)

    def set_flat_threshold(self, threshold):
        cmd_data = [0x75, 0]
        cmd_data.extend(PlezmoMsg.uint8_to_bytes(0x00))
        cmd_data.extend(PlezmoMsg.uint8_to_bytes(threshold))
        command = PlezmoMsg.generate_command(Constants.MSG_TYPE_COMMAND, cmd_data)
        self.send_cmd(command)

    def on_motion(self, motion_type, listener):
        num_bytes_to_match = 2
        mask_before_match = [0xff, 0x0]
        value_to_match = PlezmoMsg.uint8_to_bytes(motion_type.value)
        value_to_match.append(0x00)
        self.add_listener(2, EventListenerWrapper(listener, num_bytes_to_match, mask_before_match, value_to_match))

    def on_tilt(self, direction, listener):
        num_bytes_to_match = 2
        mask_before_match = [0xff, 0x0]
        value_to_match = PlezmoMsg.uint8_to_bytes(direction.value)
        value_to_match.append(0x00)
        self.add_listener(2, EventListenerWrapper(listener, num_bytes_to_match, mask_before_match, value_to_match))

    def on_step(self, listener):
        num_bytes_to_match = 2
        mask_before_match = [0xff, 0x0]
        value_to_match = [0x09, 0x00]
        self.add_listener(2, EventListenerWrapper(listener, num_bytes_to_match, mask_before_match, value_to_match))

    def on_flat(self, listener):
        num_bytes_to_match = 2
        mask_before_match = [0xff, 0x0]
        value_to_match = [0x06, 0x00]
        self.add_listener(2, EventListenerWrapper(listener, num_bytes_to_match, mask_before_match, value_to_match))

    def wait_for_motion(self, motion_type):
        num_bytes_to_match = 2
        mask_before_match = [0xff, 0x0]
        value_to_match = PlezmoMsg.uint8_to_bytes(motion_type.value)
        value_to_match.append(0x00)
        self.wait_for_event(2, num_bytes_to_match, mask_before_match, value_to_match)

    def wait_for_tilt(self, direction):
        num_bytes_to_match = 2
        mask_before_match = [0xff, 0x0]
        value_to_match = PlezmoMsg.uint8_to_bytes(direction.value)
        value_to_match.append(0x00)
        self.wait_for_event(2, num_bytes_to_match, mask_before_match, value_to_match)

    def wait_for_step(self):
        num_bytes_to_match = 2
        mask_before_match = [0xff, 0x0]
        value_to_match = [0x09, 0x00]
        self.wait_for_event(2, num_bytes_to_match, mask_before_match, value_to_match)

    def wait_for_flat(self):
        num_bytes_to_match = 2
        mask_before_match = [0xff, 0x0]
        value_to_match = [0x06, 0x00]
        self.wait_for_event(2, num_bytes_to_match, mask_before_match, value_to_match)

class Tilt(Enum):
    LEFT = 1
    RIGHT = 2
    FRONT = 3
    BACK = 4

class Movement(Enum):
    START = 5
    STOP = 7

class Axis(Enum):
    LEFT_TO_RIGHT = 2
    FRONT_TO_BACK = 3

class Acceleration(Enum):
    X = 0
    Y = 1
    Z = 2
    RESULTANT = 3

class PlezmoMotion(PlezmoElement):

    def getAngle(self, elementName, direction):
        """getAngle(elementName: String, direction: Axis) :int
        Get the angle of motion sensor in specified direction

        :param elementName: Name of the element
        :param direction: Valid values are Axis.LEFT_TO_RIGHT and Axis.FRONT_TO_BACK

        :rtype: int
        """
        # find element by name
        element = self.plezmoApi.getElementByName(elementName)
        if element == None:
            self._logger.error("Element {} not found".format(elementName))
            raise ElementNotFoundException(elementName)
        # execute command
        return element.get_angle(direction)

    def getAccelerometerData(self, elementName, direction):
        """getAccelerometerData(elementName: String, direction: Acceleration) :int 
        Get the acceleration of motion sensor along specified axis

        :param elementName: Name of the element
        :param direction: Acceleration. Valid values are Acceleration.X, Acceleration.Y, Acceleration.Z and Acceleration.RESULTANT

        :rtype: int
        """
        # find element by name
        element = self.plezmoApi.getElementByName(elementName)
        if element == None:
            self._logger.error("Element {} not found".format(elementName))
            raise ElementNotFoundException(elementName)
        # execute command
        return element.get_accelerometer_data(direction)

    def setTiltThreshold(self, elementName, threshold):
        """setTiltThreshold(elementName: String, value: int)
        Set the angle above which motion sensor will trigger a 'Tilt' event
        
        :param elementName: Name of the element
        :param value: Value of the tilt threshold.
        """
        # find element by name
        element = self.plezmoApi.getElementByName(elementName)
        if element == None:
            self._logger.error("Element {} not found".format(elementName))
            raise ElementNotFoundException(elementName)
        # execute command
        return element.set_tilt_threshold(threshold)

    def setFlatThreshold(self, elementName, threshold):
        """setFlatThreshold(elementName: String, value: int)
        Set the angle below which motion sensor will trigger a 'Flat' event

        :param elementName: Name of the element
        :param value: Value of the tilt threshold.
        """
        # find element by name
        element = self.plezmoApi.getElementByName(elementName)
        if element == None:
            self._logger.error("Element {} not found".format(elementName))
            raise ElementNotFoundException(elementName)
        # execute command
        return element.set_flat_threshold(threshold)

    def onMotion(self, elementName, handler, motionType):
        """onMotion(elementName: String, handler: FunctionName, motionType: Movement)
        Handle the movement event of a motion sensor

        :param elementName: Name of the element
        :param handler: Name of the handler function - must be defined before this call
        :param motionType: Type of movement Valid values are Movement.START and Movement.STOP

        """
        # find element by name
        element = self.plezmoApi.getElementByName(elementName)
        if element == None:
            self._logger.error("Element {} not found".format(elementName))
            raise ElementNotFoundException(elementName)
        # execute command
        element.on_motion(motionType, handler)

    def onTilt(self, elementName, handler, direction):
        """onTilt(elementName: String, handler: FunctionName, direction: Tilt)
        Handle the tilt event of a motion sensor

        :param elementName: Name of the element
        :param handler: Name of the handler function - must be defined before this call
        :param direction: Direction of the tilt. Valid values are Tilt.LEFT, Tilt.RIGHT, Tilt.FRONT and Tilt.BACK

        """
        # find element by name
        element = self.plezmoApi.getElementByName(elementName)
        if element == None:
            self._logger.error("Element {} not found".format(elementName))
            raise ElementNotFoundException(elementName)
        # execute command
        element.on_tilt(direction, handler)

    def onStep(self, elementName, handler):
        """onStep(elementName: String, handler: FunctionName)
        Handle the 'Step' event of a motion sensor

        :param elementName: Name of the element
        :param handler: Name of the handler function - must be defined before this call

        """
        # find element by name
        element = self.plezmoApi.getElementByName(elementName)
        if element == None:
            self._logger.error("Element {} not found".format(elementName))
            raise ElementNotFoundException(elementName)
        # execute command
        element.on_step(handler)

    def onFlat(self, elementName, handler):
        """onFlat(elementName: String, handler: FunctionName)
        Handle the 'Flat' event of a motion sensor

        :param elementName: Name of the element
        :param handler: Name of the handler function - must be defined before this call

        """
        # find element by name
        element = self.plezmoApi.getElementByName(elementName)
        if element == None:
            self._logger.error("Element {} not found".format(elementName))
            raise ElementNotFoundException(elementName)
        # execute command
        element.on_flat(handler)

    def waitForMotion(self, elementName, motionType):
        """waitForMotion(elementName: String, eventType: Movement)
        Wait until the motion sensor triggers an event indicating start or stop movement

        :param elementName: Name of the element
        :param eventType: Type of motion. Valid values are Movement.START and Movement.STOP
        """
        # find element by name
        element = self.plezmoApi.getElementByName(elementName)
        if element == None:
            self._logger.error("Element {} not found".format(elementName))
            raise ElementNotFoundException(elementName)
        # execute command
        element.wait_for_motion(motionType)

    def waitForTilt(self, elementName, direction):
        """waitForTilt(elementName: String, direction: Tilt)
        Wait until the motion sensor triggers a tilt event specified by direction


        :param elementName: Name of the element
        :param direction: Direction. Valid values are Tilt.LEFT, Tilt.RIGHT, Tilt.FRONT and Tilt.BACK
        """
        # find element by name
        element = self.plezmoApi.getElementByName(elementName)
        if element == None:
            self._logger.error("Element {} not found".format(elementName))
            raise ElementNotFoundException(elementName)
        # execute command
        element.wait_for_tilt(direction)

    def waitForStep(self, elementName):
        """waitForStep(elementName: String)
        Wait until the motion sensor triggers a step event

        :param elementName: Name of the element

    	"""  
        # find element by name
        element = self.plezmoApi.getElementByName(elementName)
        if element == None:
            self._logger.error("Element {} not found".format(elementName))
            raise ElementNotFoundException(elementName)
        # execute command
        element.wait_for_step()

    def waitForFlat(self, elementName):
        """waitForFlat(elementName: String)
        Wait until the motion sensor triggers a the event 'Flat'

        :param elementName: Name of the element

    	"""
        # find element by name
        element = self.plezmoApi.getElementByName(elementName)
        if element == None:
            self._logger.error("Element {} not found".format(elementName))
            raise ElementNotFoundException(elementName)
        # execute command
        element.wait_for_flat()
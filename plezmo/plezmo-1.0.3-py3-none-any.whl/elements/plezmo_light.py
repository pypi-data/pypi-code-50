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

class PlezmoLightImpl(PlezmoElementImpl):

    def __init__(self, name, mac, conn_handle, device_manager):
        super(PlezmoLightImpl, self).__init__(name, PlezmoElementType.LIGHT, mac, conn_handle, device_manager)
        self._logger = Logger()

    def turn_on(self, color, brightness):
        cmd_data = [0x49, 0x00]
        cmd_data.extend(color.get_bytes())
        cmd_data.extend(Percentage.get_bytes(brightness))
        command = PlezmoMsg.generate_command(Constants.MSG_TYPE_COMMAND, cmd_data)
        self.send_cmd(command)

    def set_state(self, value):
        cmd_data = [0x41, 0x00]
        cmd_data.extend(PlezmoMsg.uint8_to_bytes(value.value))
        command = PlezmoMsg.generate_command(Constants.MSG_TYPE_COMMAND, cmd_data)
        self.send_cmd(command)

    def set_color(self, color):
        cmd_data = [0x42, 0x00]
        cmd_data.extend(color.get_bytes())
        command = PlezmoMsg.generate_command(Constants.MSG_TYPE_COMMAND, cmd_data)
        self.send_cmd(command)

    def set_brightness(self, brightness):
        cmd_data = [0x44, 0x00]
        cmd_data.extend(Percentage.get_bytes(brightness))
        command = PlezmoMsg.generate_command(Constants.MSG_TYPE_COMMAND, cmd_data)
        self.send_cmd(command)

    def get_state(self):
        cmd_data = [0x48, 0x00]
        command = PlezmoMsg.generate_command(Constants.MSG_TYPE_COMMAND, cmd_data)
        response = self.send_cmd(command)
        if response[0] == 0:
            return response[1]
        else:
            return response[0]

    def get_brightness(self):
        cmd_data = [0x45, 0x00]
        command = PlezmoMsg.generate_command(Constants.MSG_TYPE_COMMAND, cmd_data)
        response = self.send_cmd(command)
        if response[0] == 0:
            return PlezmoMsg.bytes_to_int(response[1:2])
        else:
            return response[0]

    def get_color(self):
        cmd_data = [0x43, 0x00]
        command = PlezmoMsg.generate_command(Constants.MSG_TYPE_COMMAND, cmd_data)
        response = self.send_cmd(command)
        if response[0] == 0:
            return LightColor.from_bytes(response[1:4])
        else:
            return response[0]

    def fade_in(self, brightness, color, speed):
        cmd_data = [0x46, 0x00]
        cmd_data.extend(color.get_bytes())
        cmd_data.extend(Percentage.get_bytes(brightness))
        cmd_data.extend(PlezmoMsg.uint8_to_bytes(speed.value))
        command = PlezmoMsg.generate_command(Constants.MSG_TYPE_COMMAND, cmd_data)
        self.send_cmd(command)

    def fade_out(self, speed):
        cmd_data = [0x47, 0x00]
        cmd_data.extend(PlezmoMsg.uint8_to_bytes(speed.value))
        command = PlezmoMsg.generate_command(Constants.MSG_TYPE_COMMAND, cmd_data)
        self.send_cmd(command)

class LightState(Enum):
    ON = 1
    OFF = 0
    @staticmethod
    def from_bytes(data):
        if data[0] == 1:
            return LightState.ON
        else:
            return LightState.OFF

class LightFadeSpeed(Enum):
    SLOW = 4
    MEDIUM = 2
    FAST = 1

class Percentage():
    def __init__(self, val):
        self.value = val

    @staticmethod
    def get_bytes(val):
        return [val.value]

class LightColor():
    def __init__(self, val):
        self.value = val

    def get_bytes(self):
        hex_string = self.value[1:] # remove leading #
        hex_data = []
        hex_data.append(int("0x" + hex_string[0:2], 16))
        hex_data.append(int("0x" + hex_string[2:4], 16))
        hex_data.append(int("0x" + hex_string[4:6], 16))
        return hex_data

    @staticmethod
    def from_bytes(data):
        hex_string = "#"
        part = format(data[0], 'x')
        if len(part) == 1:
            part = "0" + part
        hex_string += part
        part = format(data[1], 'x')
        if len(part) == 1:
            part = "0" + part
        hex_string += part
        part = format(data[2], 'x')
        if len(part) == 1:
            part = "0" + part
        hex_string += part
        return hex_string.replace('0x', '')

class PlezmoLight(PlezmoElement):

    def turnOn(self, elementName, color, brightness):
        """turnOn(elementName: String, color: LightColor, brightness: Percentage)
        Turn light on on specified color and brightness

        :param elementName: Name of the element
        :param color: Color of the light e.g. LightColor('#FF0000')
        :param brightness: Percentage brightness value between 0 to 100 (inclusive) e.g. Percentage(100)

        """
        # find element by name
        element = self.plezmoApi.getElementByName(elementName)
        if element == None:
            self._logger.error("Element {} not found".format(elementName))
            raise ElementNotFoundException(elementName)
        # execute command
        return element.turn_on(color, brightness)

    def setState(self, elementName, value):
        """setState(elementName: String, value: LightState)
        Change the state of light to LightState.On or LightState.Off

        :param elementName: Name of the element
        :param value: Value of the state to set. Valid values are LightState.ON and LightState.OFF

        """
        # find element by name
        element = self.plezmoApi.getElementByName(elementName)
        if element == None:
            self._logger.error("Element {} not found".format(elementName))
            raise ElementNotFoundException(elementName)
        # execute command
        return element.set_state(value)

    def setColor(self, elementName, color):
        """setColor(elementName: String, color: LightColor)
        Set the color of light to specified value

        :param elementName: Name of the element
        :param color:  Color of the light e.g. LightColor('#FF0000')

        """
        # find element by name
        element = self.plezmoApi.getElementByName(elementName)
        if element == None:
            self._logger.error("Element {} not found".format(elementName))
            raise ElementNotFoundException(elementName)
        # execute command
        return element.set_color(color)

    def setBrightness(self, elementName, brightness):
        """setBrightness(elementName: String, brightness: Percentage)
        Set the brightness of light to specified value

        :param elementName: Name of the element
        :param brightness: Percentage brightness value between 0 to 100 (inclusive) e.g. Percentage(100)

        """
        # find element by name
        element = self.plezmoApi.getElementByName(elementName)
        if element == None:
            self._logger.error("Element {} not found".format(elementName))
            raise ElementNotFoundException(elementName)
        # execute command
        return element.set_brightness(brightness)

    def getState(self, elementName):
        """getState(elementName: String): int
        Get the state of light. Returns 0 if 'OFF' or 1 if 'ON'

        :param elementName: Name of the element
        :rtype: int
        """
        # find element by name
        element = self.plezmoApi.getElementByName(elementName)
        if element == None:
            self._logger.error("Element {} not found".format(elementName))
            raise ElementNotFoundException(elementName)
        # execute command
        return element.get_state()

    def getBrightness(self, elementName):
        """getBrightness(elementName: String): int
        Get the brightness of light. Returns value between 0 to 100 (inclusive)

        :rtype: int
        """
        # find element by name
        element = self.plezmoApi.getElementByName(elementName)
        if element == None:
            self._logger.error("Element {} not found".format(elementName))
            raise ElementNotFoundException(elementName)
        # execute command
        return element.get_brightness()

    def getColor(self, elementName):
        """getColor(elementName: Strint): String
        Get the color of light. Returns color

        :rtype: str
        """
        # find element by name
        element = self.plezmoApi.getElementByName(elementName)
        if element == None:
            self._logger.error("Element {} not found".format(elementName))
            raise ElementNotFoundException(elementName)
        # execute command
        return element.get_color()
    def fadeIn(self, elementName, brightness, color, speed):
        """fadeIn(elementName: String, brightness: Percentage, color: LightColor, speed: LightFadeSpeed) 
        Fade in the light in specified speed to specified color and brightness

        :param elementName: Name of the element
        :param brightness: Percentage brightness value between 0 to 100 (inclusive) e.g. Percentage(100)
        :param color: Color of the light e.g. LightColor('#FF0000')
        :param speed: Speed of fade out. Valid values are LightFadeSpeed.SLOW, LightFadeSpeed.MEDIUM, LightFadeSpeed.FAST

        """
        # find element by name
        element = self.plezmoApi.getElementByName(elementName)
        if element == None:
            self._logger.error("Element {} not found".format(elementName))
            raise ElementNotFoundException(elementName)
        # execute command
        return element.fade_in(brightness, color, speed)

    def fadeOut(self, elementName, speed):
        """fadeOut(elementName: String, speed: LightFadeSpeed)
        Fade out the light in specified speed

        :param elementName: Name of the element
        :param speed: Speed of fade out. Valid values are LightFadeSpeed.SLOW, LightFadeSpeed.MEDIUM, LightFadeSpeed.FAST

        """
        # find element by name
        element = self.plezmoApi.getElementByName(elementName)
        if element == None:
            self._logger.error("Element {} not found".format(elementName))
            raise ElementNotFoundException(elementName)
        # execute command
        return element.fade_out(speed)

        


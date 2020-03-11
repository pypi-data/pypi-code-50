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

class PlezmoColorSensorElement(PlezmoElementImpl):

    def __init__(self, name, mac, conn_handle, device_manager):
        super(PlezmoColorSensorElement, self).__init__(name, PlezmoElementType.COLOR, mac, conn_handle, device_manager)
        self._logger = Logger()

    def get_color(self):
        cmd_data = [0x1A, 0x00]
        command = PlezmoMsg.generate_command(Constants.MSG_TYPE_COMMAND, cmd_data)
        response = self.send_cmd(command)
        if response[0] == 0:
            self._logger.debug("Got color {}".format(response[1:4]))
            return ColorSensorColor.to_hex_str(response[1:4])
        else:
            self._logger.error("Failed to get color, error code {}".format(response[0]))
            return response[0]

    def get_light_value_percent(self):
        cmd_data = [0x1B, 0x00]
        command = PlezmoMsg.generate_command(Constants.MSG_TYPE_COMMAND, cmd_data)
        response = self.send_cmd(command)
        if response[0] == 0:
            self._logger.debug("Got light percentage {}".format(response[1]))
            return PlezmoMsg.bytes_to_int(response[1:3])
        else:
            self._logger.error("Failed to get light pc, error code {}".format(PlezmoMsg.bytes_to_int(response[1:3])))
            return response[0]

    def get_light_value_lux(self):
        cmd_data = [0x1D, 0x00]
        command = PlezmoMsg.generate_command(Constants.MSG_TYPE_COMMAND, cmd_data)
        response = self.send_cmd(command)
        if response[0] == 0:
            self._logger.debug("Got light lux {}".format(PlezmoMsg.bytes_to_int(response[1:3])))
            return PlezmoMsg.bytes_to_int(response[1:3])
        else:
            self._logger.error("Failed to get light lux, error code {}".format(response[0]))
            return response[0]

    def set_light_threshold_percent(self, threshold):
        cmd_data = [0x1C, 0x00]
        cmd_data.extend(PlezmoMsg.uint16_to_bytes(threshold))
        command = PlezmoMsg.generate_command(Constants.MSG_TYPE_COMMAND, cmd_data)
        response = self.send_cmd(command)
        if response[0] == 0:
            self._logger.info("Light threshold percent successfully set")
        return response[0]

    def set_light_threshold_lux(self, threshold):
        cmd_data = [0x1E, 0x00]
        cmd_data.extend(PlezmoMsg.uint16_to_bytes(threshold))
        command = PlezmoMsg.generate_command(Constants.MSG_TYPE_COMMAND, cmd_data)
        response = self.send_cmd(command)
        if response[0] == 0:
            self._logger.info("Light threshold lux successfully set")
        return response[0]

    def get_light_component_value_in_lux(self, light_component):
        cmd_data = [0x1F, 0x00]
        cmd_data.extend(PlezmoMsg.uint8_to_bytes(light_component.value))
        command = PlezmoMsg.generate_command(Constants.MSG_TYPE_COMMAND, cmd_data)
        response = self.send_cmd(command)
        if response[0] == 0:
            return PlezmoMsg.bytes_to_int(response[1:3])
        else:
            return response[0]

    def on_any_color(self, listener):
        # event id for color change = 6
        # add a listener against event id 6
        num_bytes_to_match = 0
        self.add_listener(Constants.EVENT_COLOR, EventListenerWrapper(listener, num_bytes_to_match))

    def on_color_change(self, color, listener):
        # event id for color change = 6
        # add a listener against event id 6
        num_bytes_to_match = 6
        mask_before_match = [0x00, 0x00, 0x00, 0xff, 0xff, 0xff]
        padded_value_to_match = [0x00, 0x00, 0x00] # this comes from json file (static param)
        padded_value_to_match.extend(PlezmoColorSensorColorMapping.getValue(color))
        self.add_listener(Constants.EVENT_COLOR, EventListenerWrapper(listener, num_bytes_to_match, mask_before_match, padded_value_to_match))

    def on_light_event(self, event_type, listener):
        # event id for darkness/brightness detect = 4
        # add a listener against event id 4
        num_bytes_to_match = 1
        mask_before_match = [0xFF]
        self.add_listener(Constants.EVENT_LIGHT, EventListenerWrapper(listener, num_bytes_to_match, mask_before_match, [event_type.value]))

    def wait_for_color_to_change_to(self, to_color):
        num_bytes_to_match = 6
        mask_before_match = [0x0, 0x0, 0x0, 0xff, 0xff, 0xff]
        padded_value_to_match = [0x00, 0x00, 0x00]
        padded_value_to_match.extend(PlezmoColorSensorColorMapping.getValue(to_color))
        self.wait_for_event(6, num_bytes_to_match, mask_before_match, padded_value_to_match)

    def wait_for_color_change(self):
        self.wait_for_event(6, 0)

    def wait_for_light_event(self, event_type):
        num_bytes_to_match = 1
        mask_before_match = [0xff]
        self.wait_for_event(4, num_bytes_to_match, mask_before_match, [event_type.value])

class LightComponent(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3
    CLEAR = 4

class ColorSensorLightState(Enum):
    BRIGHT = 1
    DARK = 2
    UNKNOWN = -1
    @staticmethod
    def from_bytes(data_bytes):
        if data_bytes == [0x01]:
            return ColorSensorLightState.DARK
        elif data_bytes == [0x02]:
            return ColorSensorLightState.BRIGHT
        else:
            return ColorSensorLightState.UNKNOWN

class ColorSensorColor(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3
    YELLOW = 4
    WHITE = 5
    PINK = 6
    ORANGE = 7
    UNKNOWN = -1

    @staticmethod
    def from_bytes(data_bytes):
        return PlezmoColorSensorColorMapping.from_bytes(data_bytes)

    @staticmethod
    def to_hex_str(data):
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


class PlezmoColorSensorColorMapping():
    RED_HEX = [0xFF, 0x00, 0x00]
    GREEN_HEX = [0x00, 0xFF, 0x00]
    BLUE_HEX = [0x00, 0x00, 0xFF]
    YELLOW_HEX = [0xFF, 0xFF, 0x00]
    WHITE_HEX = [0xFF, 0xFF, 0xFF]
    PINK_HEX = [0xFF, 0xC0, 0xCB]
    ORANGE_HEX = [0xFA, 0x96, 0x1E]

    @staticmethod
    def getValue(enum):
        if enum == ColorSensorColor.RED:
            return PlezmoColorSensorColorMapping.RED_HEX
        if enum == ColorSensorColor.GREEN:
            return PlezmoColorSensorColorMapping.GREEN_HEX
        if enum == ColorSensorColor.BLUE:
            return PlezmoColorSensorColorMapping.BLUE_HEX
        if enum == ColorSensorColor.YELLOW:
            return PlezmoColorSensorColorMapping.YELLOW_HEX
        if enum == ColorSensorColor.WHITE:
            return PlezmoColorSensorColorMapping.WHITE_HEX
        if enum == ColorSensorColor.PINK:
            return PlezmoColorSensorColorMapping.PINK_HEX
        if enum == ColorSensorColor.ORANGE:
            return PlezmoColorSensorColorMapping.ORANGE_HEX

    @staticmethod
    def from_bytes(data_bytes):
        if PlezmoColorSensorColorMapping.RED_HEX == data_bytes:
            return ColorSensorColor.RED
        elif PlezmoColorSensorColorMapping.GREEN_HEX == data_bytes:
            return ColorSensorColor.GREEN
        elif PlezmoColorSensorColorMapping.BLUE_HEX == data_bytes:
            return ColorSensorColor.BLUE
        elif PlezmoColorSensorColorMapping.YELLOW_HEX == data_bytes:
            return ColorSensorColor.YELLOW
        elif PlezmoColorSensorColorMapping.PINK_HEX == data_bytes:
            return ColorSensorColor.PINK
        elif PlezmoColorSensorColorMapping.WHITE_HEX == data_bytes:
            return ColorSensorColor.WHITE
        else:
            return ColorSensorColor.UNKNOWN


class PlezmoColor(PlezmoElement):

    def onColorChange(self, elementName, handler, color):
        """onColorChange(elementName: String, handler: FunctionName, color: ColorSensorColor)
        Handle the event when color sensor detects specified color 

        :param elementName: Name of the element
        :param handler: Name of the handler function - must be defined before this call
        :param color: Color to be detected. Valid values are ColorSensorColor.RED, ColorSensorColor.GREEN, ColorSensorColor.BLUE, ColorSensorColor.YELLOW, ColorSensorColor.WHITE and ColorSensorColor.PINK 
        """
        # find element by name
        element = self.plezmoApi.getElementByName(elementName)
        if element == None:
            self._logger.error("Element {} not found".format(elementName))
            raise ElementNotFoundException(elementName)
        # execute command
        element.on_color_change(color, handler)

    def onAnyColor(self, elementName, handler):
        """onAnyColor(elementName: String, handler: FunctionName)
        Handle the event when color sensor detects change in color

        :param elementName: Name of the element
        :param handler: Name of the handler function - must be defined before this call
        """
        # find element by name
        element = self.plezmoApi.getElementByName(elementName)
        if element == None:
            self._logger.error("Element {} not found".format(elementName))
            raise ElementNotFoundException(elementName)
        # execute command
        element.on_any_color(handler)

    def onLightEvent(self, elementName, handler, eventType):
        """onLightEvent(elementName: String, handler: FunctionName, eventType: ColorSensorLightState)
        Handle the event when color sensor detects change in ambient light

        :param elementName: Name of the element
        :param handler: Name of the handler function - must be defined before this call
        :param eventType: Type of change. Valid values are ColorSensorLightState.BRIGHT and ColorSensorLightState.DARK
        """
        # find element by name
        element = self.plezmoApi.getElementByName(elementName)
        if element == None:
            self._logger.error("Element {} not found".format(elementName))
            raise ElementNotFoundException(elementName)
        # execute command
        element.on_light_event(eventType, handler)

    def setLightThresholdPercent(self, elementName, value):
        """setLightThresholdPercent(elementName: String, value: int)
        Set the value of ambient light percentage above which color sensor should trigger the 'Bright' event

        :param elementName: Name of the element
        :param value: Value of the threshold. Valid values between 5 and 98
        """
        # find element by name
        element = self.plezmoApi.getElementByName(elementName)
        if element == None:
            self._logger.error("Element {} not found".format(elementName))
            raise ElementNotFoundException(elementName)
        # execute command
        return element.set_light_threshold_percent(value)

    def setLightThresholdLux(self, elementName, value):
        """setLightThresholdLux(elementName: String, value: int)
        Set the value of ambient light in lux above which color sensor should trigger the 'Bright' event

        :param elementName: Name of the element
        :param value: Value of the threshold. Valid values are between 10 and 31000
        """
        # find element by name
        element = self.plezmoApi.getElementByName(elementName)
        if element == None:
            self._logger.error("Element {} not found".format(elementName))
            raise ElementNotFoundException(elementName)
        # execute command
        return element.set_light_threshold_lux(value)

    def getColor(self, elementName):
        """getColor(elementName: String): String
        Get the value of color infront of the sensor Set the font size on the display to specified value

        :param elementName: Name of the element
        :rtype: ColorSensorColor
        """
        # find element by name
        element = self.plezmoApi.getElementByName(elementName)
        if element == None:
            self._logger.error("Element {} not found".format(elementName))
            raise ElementNotFoundException(elementName)
        # execute command
        return element.get_color()

    def getLightValuePercent(self, elementName):
        """getLightValuePercent(elementName: String): int
        Get the value of ambient light in percentage 

        :param elementName: Name of the element
        :rtype: int
        """
        # find element by name
        element = self.plezmoApi.getElementByName(elementName)
        if element == None:
            self._logger.error("Element {} not found".format(elementName))
            raise ElementNotFoundException(elementName)
        # execute command
        return element.get_light_value_percent()

    def getLightValueLux(self, elementName):
        """getLightValueLux(elementName: String): int
        Get the value of ambient light in lux

        :param elementName: Name of the element
        :rtype: int
        """
        # find element by name
        element = self.plezmoApi.getElementByName(elementName)
        if element == None:
            self._logger.error("Element {} not found".format(elementName))
            raise ElementNotFoundException(elementName)
        # execute command
        return element.get_light_value_lux()

    def getLightComponentValueInLux(self, elementName, lightComponent):
        """getLightComponentValueInLux(elementName: String, lightComponent: LightComponent): int
        Get the value of the specified component in light in lux

        :param elementName: Name of the element
        :param lightComponent: Component whose value is to be fetched. Valid values are LightComponent.RED, LightComponent.GREEN, LightComponent.BLUE, LightComponent.CLEAR
        :rtype: int
        """
        # find element by name
        element = self.plezmoApi.getElementByName(elementName)
        if element == None:
            self._logger.error("Element {} not found".format(elementName))
            raise ElementNotFoundException(elementName)
        # execute command
        return element.get_light_component_value_in_lux(lightComponent)

    def waitForColorToChangeTo(self, elementName, toColor):
        """waitForColorToChangeTo(elementName: String, color: ColorSensorColor)
        Wait until the color sensor detects the specified color

        :param elementName: Name of the element
        :param color: Color to be detected. Valid values are ColorSensorColor.RED, ColorSensorColor.GREEN, ColorSensorColor.BLUE, ColorSensorColor.YELLOW, ColorSensorColor.WHITE and ColorSensorColor.PINK
        """
        # find element by name
        element = self.plezmoApi.getElementByName(elementName)
        if element == None:
            self._logger.error("Element {} not found".format(elementName))
            raise ElementNotFoundException(elementName)
        # execute command
        element.wait_for_color_to_change_to(toColor)

    def waitForColorChange(self, elementName):
        """waitForColorChange(elementName: String)
        Wait until the color sensor detects a change in color 

        :param elementName: Name of the element
        """
        # find element by name
        element = self.plezmoApi.getElementByName(elementName)
        if element == None:
            self._logger.error("Element {} not found".format(elementName))
            raise ElementNotFoundException(elementName)
        # execute command
        element.wait_for_color_change()

    def waitForLightEvent(self, elementName, eventType):
        """waitForLightEvent(elementName: String, eventType: ColorSensorLightState)
        Wait until the color sensor detects the specified change in ambient light 

        :param elementName: Name of the element
        :param eventType: Type of change. Valid values are ColorSensorLightState.BRIGHT and ColorSensorLightState.DARK
        """
        # find element by name
        element = self.plezmoApi.getElementByName(elementName)
        if element == None:
            self._logger.error("Element {} not found".format(elementName))
            raise ElementNotFoundException(elementName)
        # execute command
        element.wait_for_light_event(eventType)
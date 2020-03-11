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

class PlezmoDisplayImpl(PlezmoElementImpl):
    MAX_DISPLAY_LENGTH = 14
    def __init__(self, name, mac, conn_handle, device_manager):
        super(PlezmoDisplayImpl, self).__init__(name, PlezmoElementType.DISPLAY, mac, conn_handle, device_manager)
        self._logger = Logger()

    def show_image(self, image_name):
        cmd_data = [0x51, 0x00]
        cmd_data.extend(PlezmoMsg.uint8_to_bytes(0))
        cmd_data.extend(PlezmoMsg.uint8_to_bytes(0))
        cmd_data.extend(PlezmoMsg.uint8_to_bytes(image_name.value))
        command = PlezmoMsg.generate_command(Constants.MSG_TYPE_COMMAND, cmd_data)
        self.send_cmd(command)

    def show_text(self, line, alignment, text):
        cmd_data = [0x52, 0x00]
        cmd_data.extend(PlezmoMsg.uint8_to_bytes(line.value))
        cmd_data.extend(PlezmoMsg.uint8_to_bytes(alignment.value))
        str = PlezmoMsg.str_to_bytes(text, PlezmoDisplayImpl.MAX_DISPLAY_LENGTH)
        self._logger.debug("Converted str is {}".format(str))
        cmd_data.extend(str)
        command = PlezmoMsg.generate_command(Constants.MSG_TYPE_COMMAND, cmd_data)
        self.send_cmd(command)

    def clear_display(self):
        cmd_data = [0x53, 0x00]
        cmd_data.extend(PlezmoMsg.uint8_to_bytes(0))
        command = PlezmoMsg.generate_command(Constants.MSG_TYPE_COMMAND, cmd_data)
        self.send_cmd(command)

    def paint_background_color(self, color):
        cmd_data = [0x54, 0x00]
        cmd_data.extend(PlezmoMsg.uint8_to_bytes(color.value))
        command = PlezmoMsg.generate_command(Constants.MSG_TYPE_COMMAND, cmd_data)
        self.send_cmd(command)

    def set_text_color(self, color):
        cmd_data = [0x55, 0x00]
        cmd_data.extend(PlezmoMsg.uint8_to_bytes(color.value))
        command = PlezmoMsg.generate_command(Constants.MSG_TYPE_COMMAND, cmd_data)
        self.send_cmd(command)

    def set_font_size(self, font_size):
        cmd_data = [0x5A, 0x00]
        cmd_data.extend(PlezmoMsg.uint8_to_bytes(font_size.value))
        command = PlezmoMsg.generate_command(Constants.MSG_TYPE_COMMAND, cmd_data)
        self.send_cmd(command)

class PlezmoDisplay(PlezmoElement):

    def showImage(self, elementName, imageName):
        """showImage(elementName: String, imageName: DisplayImage)
        Show the specified image on the display

        :param elementName: Name of the element
        :param imageName: DisplayImage
        """
        # find element by name
        element = self.plezmoApi.getElementByName(elementName)
        if element == None:
            self._logger.error("Element {} not found".format(elementName))
            raise ElementNotFoundException(elementName)
        # execute command
        return element.show_image(imageName)

    def showText(self, elementName, line, alignment, text):
        """showText(elementName: String, line: DisplayLine, alignment: TextAlignment, text: String)
        Show the specified text at specified location on the display

        :param elementName: Name of the element
        :param line: Line on which the text is to be displayed. 
            Valid values are DisplayLine.ONE, DisplayLine.TWO and DisplayLine.THREE for medium font and DisplayLine.ONE, DisplayLine.TWO, DisplayLine.THREE, DisplayLine.FOUR and DisplayLine.FIVE for small font
        :param alignment: Alignment of the text. 
            Valid values are TextAlignment.LEFT, TextAlignment.CENTER and TextAlignment.RIGHT
        :param text: The text to be displayed.
        """
        # find element by name
        element = self.plezmoApi.getElementByName(elementName)
        if element == None:
            self._logger.error("Element {} not found".format(elementName))
            raise ElementNotFoundException(elementName)
        # execute command
        return element.show_text(line, alignment, text)

    def clearDisplay(self, elementName):
        """clearDisplay(elementName: String)
        Clear the display

        :param elementName: Name of the element
        """
        # find element by name
        element = self.plezmoApi.getElementByName(elementName)
        if element == None:
            self._logger.error("Element {} not found".format(elementName))
            raise ElementNotFoundException(elementName)
        # execute command
        return element.clear_display()

    def paintBackgroundColor(self, elementName, color):
        """paintBackgroundColor(elementName: String, color: DisplayBackground)
        Paint the display in specified color

        :param elementName: Name of the element
        :param color: Valid values are DisplayBackground.RED, DisplayBackground.GREEN, DisplayBackground.BLUE, DisplayBackground.YELLOW, DisplayBackground.WHITE, DisplayBackground.BLACK, DisplayBackground.CYAN
        """
        # find element by name
        element = self.plezmoApi.getElementByName(elementName)
        if element == None:
            self._logger.error("Element {} not found".format(elementName))
            raise ElementNotFoundException(elementName)
        # execute command
        return element.paint_background_color(color)

    def setTextColor(self, elementName, color):
        """setTextColor(elementName: String, color: DisplayBackground)
        Set the text color on the display to specified color

        :param elementName: Name of the element
        :param color: Valid values are DisplayBackground.RED, DisplayBackground.GREEN, DisplayBackground.BLUE, DisplayBackground.YELLOW, DisplayBackground.WHITE, DisplayBackground.BLACK, DisplayBackground.CYAN
        """
        # find element by name
        element = self.plezmoApi.getElementByName(elementName)
        if element == None:
            self._logger.error("Element {} not found".format(elementName))
            raise ElementNotFoundException(elementName)
        # execute command
        return element.set_text_color(color)

    def setFontSize(self, elementName, font_size):
        """setFontSize(elementName: String, fontSize: FontSize)
        Set the font size on the display to specified value

        :param elementName: Name of the element
        :param fontSize: Valid values are FontSize.SMALL and FontSize.MEDIUM
        """
        # find element by name
        element = self.plezmoApi.getElementByName(elementName)
        if element == None:
            self._logger.error("Element {} not found".format(elementName))
            raise ElementNotFoundException(elementName)
        # execute command
        return element.set_font_size(font_size)

class TextAlignment(Enum):
    LEFT = 0
    CENTER = 1
    RIGHT = 2

class DisplayBackground(Enum):
    RED = 0
    GREEN = 1
    BLUE = 2
    YELLOW = 3
    WHITE = 4
    BLACK = 5
    CYAN = 6
    MAGENTA = 7

class FontSize(Enum):
    SMALL = 0
    MEDIUM = 1

class DisplayImage(Enum):
    GRINNING_FACE = 50
    SAVOURING_FOOD = 1
    FACE_WITH_TONGUE = 2
    TEARS_OF_JOY = 3
    SCARED_FACE = 4
    FROWNING_FACE = 5
    CRYING_FACE = 6
    POUTING_FACE = 7
    THUMBS_UP = 8
    THUMBS_DOWN = 9
    FISTED_HAND = 10
    PEDESTRIAN_WALKING = 11
    RUNNER = 12
    BICYCLIST = 13
    MUSICAL_NOTES = 14
    KEYBOARD = 15
    SAXOPHONE = 16
    TRUMPET = 17
    VIOLIN = 18
    GUITAR = 19
    DRUM = 20
    PLAY = 21
    STOP = 22
    PREVIOUS = 23
    NEXT = 24
    CLOCKWISE = 25
    ANTICLOCKWISE = 26
    UP = 27
    LEFT = 28
    DOWN = 29
    RIGHT = 30
    SUNNY = 31
    CLOUDY = 32
    LOCK = 33
    UNLOCK = 34
    TROPHY = 35
    MEDAL = 36
    ALARM_CLOCK = 37
    BIRTHDAY_CAKE = 38
    BULLSEYE = 39
    INBOX = 40
    DINNER_PLATE = 41
    WARNING = 42
    DANGER = 43
    STOP_SIGN = 44
    CHILDREN_CROSSING = 45
    NO_PEDESTRIANS = 46
    CHECK_MARK = 47
    CROSS_MARK = 48
    NO_ENTRY = 49
    PLEZMO = 0
    CUSTOM_IMAGE_0 = 100
    CUSTOM_IMAGE_1 = 101
    CUSTOM_IMAGE_2 = 102
    CUSTOM_IMAGE_3 = 103
    CUSTOM_IMAGE_4 = 104
    CUSTOM_IMAGE_5 = 105
    CUSTOM_IMAGE_6 = 106
    CUSTOM_IMAGE_7 = 107
    CUSTOM_IMAGE_8 = 108
    CUSTOM_IMAGE_9 = 109

class DisplayLine(Enum):
    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5


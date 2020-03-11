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

class PlezmoDistanceImpl(PlezmoElementImpl):

    def __init__(self, name, mac, conn_handle, device_manager):
        super(PlezmoDistanceImpl, self).__init__(name, PlezmoElementType.DISTANCE, mac, conn_handle, device_manager)
        self._logger = Logger()

    def set_distance_threshold_cm(self, value):
        cmd_data = [0x91, 0x00]
        cmd_data.extend(PlezmoMsg.uint8_to_bytes(value))
        command = PlezmoMsg.generate_command(Constants.MSG_TYPE_COMMAND, cmd_data)
        self.send_cmd(command)

    def get_distance_cm(self):
        cmd_data = [0x90, 0x00]
        command = PlezmoMsg.generate_command(Constants.MSG_TYPE_COMMAND, cmd_data)
        response = self.send_cmd(command)
        if response[0] == 0:
            return PlezmoMsg.bytes_to_signed_int(response[1:3])
        else:
            return response[0]

    def on_distance_event(self, event_type, listener):
        num_bytes_to_match = 1
        mask_before_match = [0xff]
        value_to_match = PlezmoMsg.uint8_to_bytes(event_type.value)
        self.add_listener(8, EventListenerWrapper(listener, num_bytes_to_match, mask_before_match, value_to_match))

    def wait_for_distance_event(self, event_type):
        num_bytes_to_match = 1
        mask_before_match = [0xff]
        value_to_match = PlezmoMsg.uint8_to_bytes(event_type.value)
        self.wait_for_event(8, num_bytes_to_match, mask_before_match, value_to_match)

class DistanceEvent(Enum):
    NEAR = 1
    FAR = 2

class PlezmoDistance(PlezmoElement):

    def setDistanceThresholdCM(self, elementName, value):
        """setDistanceThresholdCM(elementName: String, value: int)
        Wait until the distance sensor triggers specified event

        :param elementName: Name of the element
        :param value: Value in centimeters. If sensor detects an object at a distance less than this value, a 'NEAR' event is triggered. Valid values are between 3 and 97 (inclusive)

        """
        # find element by name
        element = self.plezmoApi.getElementByName(elementName)
        if element == None:
            self._logger.error("Element {} not found".format(elementName))
            raise ElementNotFoundException(elementName)
        # execute command
        return element.set_distance_threshold_cm(value)

    def getDistanceCM(self, elementName):
        """getDistanceCM(elementName: String): int
        Get the distance in centimeters from sensor. If there is no object within the sensor's range, -1 is returned

        :param elementName: Name of the element
        :rtype: int
        """
        # find element by name
        element = self.plezmoApi.getElementByName(elementName)
        if element == None:
            self._logger.error("Element {} not found".format(elementName))
            raise ElementNotFoundException(elementName)
        # execute command
        return element.get_distance_cm()

    def onDistanceEvent(self, elementName, handler, eventType):
        """onDistanceEvent(elementName: String, handler: FunctionName, eventType: DistanceEvent)
        Handle the event of a distance sensor

        :param elementName: Name of the element
        :param handler: Name of the handler function - must be defined before this call,
        :param eventType: Type of event. Valid values are DistanceEvent.NEAR and DistanceEvent.FAR

        """
        # find element by name
        element = self.plezmoApi.getElementByName(elementName)
        if element == None:
            self._logger.error("Element {} not found".format(elementName))
            raise ElementNotFoundException(elementName)
        # execute command
        element.on_distance_event(eventType, handler)

    def waitForDistanceEvent(self, elementName, eventType):
      # find element by name
        element = self.plezmoApi.getElementByName(elementName)
        if element == None:
            self._logger.error("Element {} not found".format(elementName))
            raise ElementNotFoundException(elementName)
        # execute command
        element.wait_for_distance_event(eventType)



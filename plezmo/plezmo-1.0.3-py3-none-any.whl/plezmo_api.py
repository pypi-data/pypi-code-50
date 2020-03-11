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
from sys import platform
import time
import traceback

from plezmo.utils.logger import Logger
from plezmo.utils.command_helper import CmdHelper
from plezmo.utils.serial_ports import *
from plezmo.connectivity import PlezmoAdapter
from plezmo.events.event_dispatcher import EventDispatcher
from plezmo.plezmo_exceptions.exceptions import *
from plezmo.elements.element_types import PlezmoElementType

class PlezmoApi:
    """Provides element management functionality (connect, disconnect, find connected element,
    discover elements)
    """
    def __init__(self):
        self._logger = Logger()

    def init(self, eventThreadpoolSize = 10):
        """init(eventThreadpoolSize: int)
        Initialize bluetooth communication and data structures

        :param eventThreadpoolSize: Size of threadpool that handles event threads. Default size is 10. This should be sufficient for most use cases. Increase this value if you have more than 10 long running event handlers (that take more than few seconds to execute).
        """
        # initialize device manager
        plezmo_adapter_port = self._getPlezmoAdapterPort();
        if plezmo_adapter_port == None:
            self._logger.error("Plezmo wireless adapter not found")
            raise PlezmoAdapterNotFoundException()

        self.device_manager = PlezmoAdapter(str(plezmo_adapter_port))
        try:
            self.device_manager.open()
        except:
            self._logger.error("Failed to initialize Plezmo wireless adapter. Please check following:\n- Plezmo wireless adapter is plugged in and it is detected by the operating system.\n- Plezmo wireless adapter has firmware version >= 1.0.1. Use Plezmo app to upgrade the adapter to latest version.\n- Make sure that Plezmo app is not running when python program is executed.")
            raise PlezmoInvalidStateException("Failed to initialize Plezmo wireless adapter")
        # initialize command helper
        CmdHelper.create_instance(self.device_manager)
        # initialize event dispatcher
        EventDispatcher.create_instance(eventThreadpoolSize)

    def setEventInterceptor(self, eventInterceptor):
        """setEventInterceptor(eventInterceptor: Function name)
        Set event interceptor for all Plezmo events. This intercentpr function will
        be called for every event that occurs for connected elements. e.g. color sensor
        color changes, distance sensor NEAR/FAR events etc.

        :param eventInterceptor: Function that will be called for each Plezmo event
        """
        CmdHelper.get_instance().set_event_interceptor(eventInterceptor)

    def connect(self, elementName, elementType, timeoutSec = 30):
        """connect(elementName: String, elementType: PlezmoElementType, timeoutSec: int)
        Connect to Plezmo element with given name and element type. If the element cannot be found
        (it is not advertising) or connection fails due to any bluetooth error ConnectionFailedException
        is thrown

        :param elementName: Name of the element to connect. Names are case sensitive.
        :param elementType: Type of element e.g. PlezmoElementType.DISTANCE, PlezmoElementType.MOTOR
        :param timeoutSec: Connection timeout in seconds. If element cannot be connected before timeout, ConnectionFailedException is thrown
        """
        try:
            element = self.device_manager.connect(elementName, elementType, timeoutSec)
            # Send start command to element to start sensing or accepting commands
            element.init()
            # Sleep is required because some element need initialized time
            # before any command can be sent
            time.sleep(1)
            return element
        except:
            self._logger.error("Failed to connect to element {}. Please check element name and type.".format(elementName))
            raise ConnectionFailedException(elementName)

    def connectByMac(self, mac, elementType, timeoutSec = 30):
        """connectByMac(mac: String, elementType: PlezmoElementType, timeoutSec: int)
        Connect to Plezmo element with given name and element type. If the element cannot be found
        (it is not advertising) or connection fails due to any bluetooth error ConnectionFailedException
        is thrown

        :param mac: MAC address of the element to connect (e.g. 1A:2B:3C:4D:5E:6F)
        :param elementType: Type of element e.g. PlezmoElementType.DISTANCE, PlezmoElementType.MOTOR
        :param timeoutSec: Connection timeout in seconds. If element cannot be connected before timeout, ConnectionFailedException is thrown
        """
        try:
            element = self.device_manager.connect_by_mac(mac, elementType, timeoutSec)
            # Send start command to element to start sensing or accepting commands
            element.init()
            # Sleep is required because some element need initialized time
            # before any command can be sent
            time.sleep(1)
            return element
        except:
            self._logger.error("Failed to connect with element {}".format(mac))
            traceback.print_exc()
            raise ConnectionFailedException(mac)

    def disconnect(self, elementName):
        """disconnect(elementName: String)
        Disconnect an already connected element. If the element is not already connected
        ElementNotFoundException is thrown

        :param elementName: Name of the element to disconnect. Names are case sensitive.
        """
        elem = self.device_manager.get_element_by_name(elementName)
        if elem != None:
            self.device_manager.disconnect(elem.conn_handle)
            time.sleep(0.2) # wait for disconnect event to come back
        else:
            self._logger.error("Element to disconnect not found. The element may be disconnected already {}".format(elementName))
            raise ElementNotFoundException(elementName)

    def getDiscoveredElements(self, timeout = 5):
        """getDiscoveredElements(timeout: int)
        Discover elements that are advertising. Elements need to be woken up before
        calling this API.

        :param timeout: Time in seconds for which discovery needs to be run

        :rtype: dict Element MAC address is the key of the dictionary
        """
        elements = self.device_manager.discover_elements(timeout)
        converted_elements = []
        for mac in elements:
            elem = elements[mac]
            converted_elements.append({"mac": mac, "type": PlezmoElementType(elem["type"]), "name": elem["name"]})
        return converted_elements
    
    def getConnectedElements(self):
        """getConnectedElements()
        Get already connected elements.

        :rtype: dict Element MAC address is the key of the dictionary
        """
        elements = self.device_manager.get_connected_elements()
        converted_elements = []
        for name in elements:
            elem = elements[name]
            converted_elements.append({"mac": elem.mac, "type": elem.type, "name": elem.name})
        return converted_elements

    def close(self):
        """close()
        Uninitializes bluetooth communication
        """
        self.device_manager.close()

    def getElementByName(self, elementName):
        """getElementByName(elementName: String)
        Find connected element by it's name

        :param elementName: Name of the element

        :rtype: PlezmoElement
        """
        return self.device_manager.get_element_by_name(elementName)

    def _getPlezmoAdapterPort(self):
        DONGLE_PIDS = [0x521A, 0xC00A]
        DONGLE_VIDS = [0x1915]
        port_list = serial_ports()
        for p in port_list:
            try:
                self._logger.debug("Got port {} pid = {}, vid = {}".format(p, hex(p.pid), hex(p.vid)))
                if DONGLE_PIDS.index(p.pid) >= 0 and DONGLE_VIDS.index(p.vid) >= 0:
                    self._logger.info("Detected Plezmo wireless adapter {}".format(p))
                    if platform == "win32":
                        return p.device.upper()
                    else:
                        return p.device
            except:
                self._logger.debug("Not Plezmo wireless adapter")
        return None

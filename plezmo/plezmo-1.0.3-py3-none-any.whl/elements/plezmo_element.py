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
from threading import Lock
try:
    from Queue import Queue # python 2.7
except:
    from queue import Queue # python 3.7
from collections import deque

from ..utils.command_helper import CmdHelper, CmdSync
from ..utils.logger import Logger
from ..utils.constants import Constants
from ..events.event_dispatcher import EventDispatcher
from ..plezmo_exceptions.exceptions import CommandFailedException

# custom services and characteristics for plezmo element
# 5D 4E 00 01 AC 86 4F 8C 99 23 8B 7C 13 33 70 B9 = 1 NUS service
# 5D 4E 00 02 AC 86 4F 8C 99 23 8B 7C 13 33 70 B9 = 2 TX char
# 5D 4E 00 03 AC 86 4F 8C 99 23 8B 7C 13 33 70 B9 = 3 RX char

# 5D 4E FE 59 AC 86 4F 8C 99 23 8B 7C 13 33 70 B9 = 65113 service
# 5D 4E 00 13 AC 86 4F 8C 99 23 8B 7C 13 33 70 B9 = 19 char1

# 5D 4E 00 20 AC 86 4F 8C 99 23 8B 7C 13 33 70 B9 = 32 service
# 5D 4E 00 22 AC 86 4F 8C 99 23 8B 7C 13 33 70 B9 = 34 char1
# 5D 4E 00 21 AC 86 4F 8C 99 23 8B 7C 13 33 70 B9 = 33 char2
# 5D 4E 00 23 AC 86 4F 8C 99 23 8B 7C 13 33 70 B9 = 35 char3

class PlezmoElementImpl(object):
    START_CMD = [0x63, 0x05, 0x00]
    ABORT_CMD = [0x63, 0x03, 0x00]
    INDICATE_CMD = [0x63 ,0x01, 0x00]
    NUS_TX_CHAR_NUM = 0x0002 # characteristic to send all commands
    NUS_RX_CHAR_NUM = 0x0003 # characteristic to receive command reply, events
    def __init__(self, name, type, mac, conn_handle, device_manager):
        self.name = name
        self.mac = mac
        self.type = type
        self.conn_handle = conn_handle
        self._device_manager = device_manager
        self._logger = Logger()
        self._listeners = dict()
        self._command_queue = deque()
        self._command_listeners_queue = deque()
        self._cmd_lock = Lock()

    def indicate(self):
        self.send_cmd(self.INDICATE_CMD)

    def init(self):
        self.send_cmd(self.START_CMD)

    def abort(self):
        self.send_cmd(self.ABORT_CMD, is_immediate = True, flush_queue = True)

    def on_double_tap(self, listener):
        # event id for common motion event = 12
        # add a listener against event id 12
        self.add_listener(Constants.EVENT_COMMON_MOTION, EventListenerWrapper(listener, 1, [0xFF,], [Constants.COMMON_EVENT_DOUBLE_TAPPED,]))

    def on_flip_event(self, flip_direction, listener):
        # event id for common motion event = 12
        # add a listener against event id 12
        self.add_listener(Constants.EVENT_COMMON_MOTION, EventListenerWrapper(listener, 1, [0xFF,], [flip_direction.value,]))

    def send_cmd(self, cmd_data, is_immediate = False, flush_queue = False):
        self._logger.debug("Sending cmd")
        cmd_sync = CmdSync(self.NUS_RX_CHAR_NUM, cmd_data[1])
        try:
            self._cmd_lock.acquire()
            # flush the queue if required e.g. in case of ABORT command
            if flush_queue == True:
                self._logger.info("Clearing command queue")
                self._command_listeners_queue.clear()
                self._command_queue.clear()
            # add command listener to the queue
            # add command to the queue. it is essential that listener and the command are
            # added atomically to these queues

            # if is_immediate flag is set, run this command before any other queued commands
            if is_immediate:
                self._command_listeners_queue.appendleft(cmd_sync)
                self._command_queue.appendleft(cmd_data)
            else:
                # otherwise queue normally at the end
                self._command_listeners_queue.append(cmd_sync)
                self._command_queue.append(cmd_data)
        finally:
            self._cmd_lock.release()
        if len(self._command_queue) == 1 or is_immediate == True:
            self._logger.debug("This is the only command in the queue or is immediate is set to true, sending it now")
            self.check_next_command()
        response = cmd_sync.wait()
        self._logger.debug("Got response {}".format(response))
        # check if response code is success (0) or not. I element returned error,
        # raise it as exception
        if len(response) > 0 and response[0] != 0:
            self._logger.error("Received error from element {}".format(response))
            raise CommandFailedException("Received error from element")
        return response

    def add_listener(self, event_id, listener_wrapper):
        if listener_wrapper != None:
            listener_list = self._listeners.get(event_id)
            if listener_list == None:
                listener_list = list()
                self._listeners[event_id] = listener_list
            listener_list.append(listener_wrapper)

    def wait_for_event(self, event_id, num_bytes_to_match, mask_before_match = None, value_to_match = None):
        # create lock object
        lockListener = WaitForLock()
        # add listener
        self.add_listener(event_id, EventListenerWrapper(lockListener, num_bytes_to_match, mask_before_match, value_to_match, True))
        # block till we get the desired event
        self._logger.debug("Added wait for listener, now waiting for event")
        lockListener.wait()

    def handle_event(self, msg):
        self._logger.debug("Handle event called {} for element {}, listeners {}".format(msg.id, self.name, self._listeners))
        # get listeners against event id
        listener_wrappers = self._listeners.get(msg.id)
        if listener_wrappers == None:
            self._logger.debug("No listener found for event {}".format(msg.id))
        else:
            self._logger.debug("Got {} listeners for event".format(len(listener_wrappers)))
            # call all listeners one by one
            for lw in listener_wrappers:
                EventDispatcher.get_instance().add_task(self._handle_event_internal, listener_wrappers, lw, msg)

    def _handle_event_internal(self, listener_wrappers, lw, msg):
        # remove listener before calling it so that it does not get
        # called again until it is finished executing
        # remove listener only if its a event listener (and not wait_for listener)
        if lw.is_blocking == False:
            listener_wrappers.remove(lw)
        # call listener function
        try:
            if lw.accept(msg.data) == True:
                # call the user supplied handler function
                # if listener represents a lock waiting for the event, notify it (wait for function)
                # if listener is a function, just call it (user listener case)
                if lw.is_blocking == True:
                    lw.listener_or_lock.notify()
                    # wait for handler should be called only once
                    listener_wrappers.remove(lw)
                else:
                    lw.listener_or_lock()
        finally:
            # add listener again only if its a event listener (and not wait_for listener)
            if lw.is_blocking == False:
                listener_wrappers.append(lw)

    def handle_command_reply(self, msg):
        self._logger.debug("Handle command reply called {} for element {}".format(msg.id, self.name))
        # get listeners against event id
        try:
            self._cmd_lock.acquire()
            # check if this is intended reply, just peek, don't pop from queue
            cmd_sync = self._command_listeners_queue[0]
            if cmd_sync.cmd_id == msg.id:
                cmd_sync = self._command_listeners_queue.popleft()
            else:
                self._logger.error("Got unexpected reply cmd = {}, ignoring".format(msg.id))
        finally:
            self._cmd_lock.release()
        cmd_sync.notify(msg.data)
        self.check_next_command()

    def check_next_command(self):
        self._logger.debug("Getting next command from queue")
        try:
            self._cmd_lock.acquire()
            cmd_data = self._command_queue.popleft()
        except Exception as e:
            self._logger.debug("Error from check command, queue possibly empty {}".format(e))
            return
        finally:
            self._cmd_lock.release()
        self._device_manager.send_cmd(self.conn_handle, self.NUS_TX_CHAR_NUM, cmd_data)
        self._logger.debug("Command sent for conn handle {}".format(self.conn_handle))

    def get_versions(self):
        return {"BOOTLOADER":self._device_manager.read_element_value(self.conn_handle,0x2A26), "APPLICATION": self._device_manager.read_element_value(self.conn_handle,0x2A28), "HARDWARE":self._device_manager.read_element_value(self.conn_handle,0x2A27)}

class Flip(Enum):
    UP = 5
    DOWN = 6

class CommonMotionEvent(Enum):
    FLIP_UP = 5
    FLIP_DOWN = 6
    DOUBLE_TAP = 7
    UNKNOWN = -1

    @staticmethod
    def from_bytes(data_bytes):
        if data_bytes[0] == CommonMotionEvent.FLIP_UP.value:
            return CommonMotionEvent.FLIP_UP
        elif data_bytes[0] == CommonMotionEvent.FLIP_DOWN.value:
            return CommonMotionEvent.FLIP_DOWN
        elif data_bytes[0] == CommonMotionEvent.DOUBLE_TAP.value:
            return CommonMotionEvent.DOUBLE_TAP
        else:
            return CommonMotionEvent.UNKNOWN


class EventListenerWrapper(object):
    def __init__(self, listener_or_lock, num_bytes_to_match, mask_before_match = None, value_to_match = None, is_blocking = False):
        self.listener_or_lock = listener_or_lock
        self.num_bytes_to_match = num_bytes_to_match
        self.mask_before_match = mask_before_match
        self.value_to_match = value_to_match
        self.is_blocking = is_blocking
        self._logger = Logger()
    def accept(self, data):
        self._logger.debug("Got event data {}".format(data))
        # extract num_bytes_to_match
        if self.num_bytes_to_match == 0:
            # no need to check data
            return True

        if len(data) < self.num_bytes_to_match:
            self._logger.error("Received data length {} is smaller than expected {}".format(len(data), num_bytes_to_match))
            return False
        sub_data = data[0:self.num_bytes_to_match]
        self._logger.debug("Sub data is {}".format(sub_data))
        self._logger.debug("Mask is {}".format(self.mask_before_match))
        # apply mask_before_match
        masked_data = []
        for i in range(0, len(sub_data)):
            masked_data.append(sub_data[i] & self.mask_before_match[i])
        self._logger.debug("Masked data is {}".format(masked_data))
        self._logger.debug("Value to match is {}".format(self.value_to_match))
        # check value_to_match
        if masked_data == self.value_to_match:
            return True
        else:
            return False

class PlezmoElement(object):
    def __init__(self, plezmoApi):
        self.plezmoApi = plezmoApi
        self._logger = Logger()
    def onDoubleTap(self, elementName, handler):
        """onDoubleTap(elementName: String, handler: FunctionName)
        Handle the 'Double Tap' event of a Plezmo Element

        :param elementName: Name of the Plezmo Element
        :param handler: Name of the handler function - must be defined before this call
        """
        # find element by name
        element = self.plezmoApi.getElementByName(elementName)
        if element == None:
            self._logger.error("Element {} not found".format(elementName))
            raise ElementNotFoundException(elementName)
        # execute command
        element.on_double_tap(handler)

    def onFlipEvent(self, elementName, handler, flipDirection):
        """onFlipEvent(elementName: String, handler: FunctionName, flipDirection: Flip)
        Handle the 'Flip' events of a Plezmo Element

        :param elementName: Name of the Plezmo Element
        :param handler: Name of the handler function - must be defined before this call
        :param: flipDirection: The direction of the flip event. Valid values are Flip.UP, Flip.DOWN
        """
        # find element by name
        element = self.plezmoApi.getElementByName(elementName)
        if element == None:
            self._logger.error("Element {} not found".format(elementName))
            raise ElementNotFoundException(elementName)
        # execute command
        element.on_flip_event(flipDirection, handler)

class WaitForLock(object):
    def __init__(self):
        self.response_q = Queue()
        self._logger = Logger()

    def wait(self):
        self.data = self.response_q.get()

    def notify(self):
        self._logger.debug("Inside notify()")
        self.response_q.put(True)
        self._logger.debug("Added to queue")
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

from .logger import Logger
try:
    from Queue import Queue # python 2.7
except:
    from queue import Queue # python 3.7
from .constants import Constants
from .msg_helper import PlezmoMsg

class CmdSync(object):
    def __init__(self, char_uuid, cmd_id):
        self.data = None
        self.char_uuid = char_uuid
        self.response_q = Queue()
        self.cmd_id = cmd_id
        self._logger = Logger()

    def wait(self, timeout = 30):
        self.data = None
        self.data = self.response_q.get(timeout = timeout)
        return self.data

    def notify(self, data=None):
        self._logger.debug("Inside notify()")
        self.response_q.put(data)
        self._logger.debug("Added to queue")

class CmdHelper(object):
    _instance = None
    def __init__(self, device_manager):
        self._logger = Logger()
        self.cmdSync = dict()
        self.device_manager = device_manager
        self.event_interceptor = None

    def set_event_interceptor(self, event_interceptor):
        self.event_interceptor = event_interceptor

    def handle_notification(self, conn_handle, char_uuid, data):
        self._logger.debug("Handling notification conn {}, char {}".format(conn_handle, char_uuid.value))
        self._logger.debug("data {}".format(data))
        msg = PlezmoMsg.from_bytes(data)
        if msg.msg_type == Constants.MSG_TYPE_REPLY:
            # two byte command response
            self._logger.debug("Handling command response for cmd {}".format(msg.id))
            plezmo_element = self.device_manager.get_element(conn_handle)
            if plezmo_element != None:
                plezmo_element.handle_command_reply(msg)
            else:
                self._logger.error("Plezmo element not found for conn_handle {}".format(conn_handle))
        elif msg.msg_type == Constants.MSG_TYPE_EVENT:
            self._logger.debug("Handling event id {}, data {}".format(msg.id, msg.data))
            plezmo_element = self.device_manager.get_element(conn_handle)
            if plezmo_element != None:
                plezmo_element.handle_event(msg)
            else:
                self._logger.error("Plezmo element not found for conn_handle {}".format(conn_handle))

            if self.event_interceptor != None and plezmo_element != None:
                self.event_interceptor.handle_event(plezmo_element.name, plezmo_element.type, msg.id, msg.data)

    @staticmethod
    def create_instance(device_manager):
        if CmdHelper._instance == None:
            CmdHelper._instance = CmdHelper(device_manager)
    @staticmethod
    def get_instance():
        return CmdHelper._instance
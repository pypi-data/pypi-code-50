import threading
import logging
from socket import timeout
from pyzabbix.sender import ZabbixSender, ZabbixMetric

import tracker_master.config as CFG

from tracker_master.app_master.master import TrackerMaster
from tracker_master.model.Message import Message
from tracker_master.model.Slave import MonitoringName
from tracker_master.zbx_client import Fields


class Notifier:

    def __init__(self):
        self.listeners = list()

    def receive_message(self, msg):
        for listener in self.listeners:
            listener.receive_message(msg)

    def add_listener(self, listener):
        assert isinstance(listener, MessageListener)
        self.listeners.append(listener)


class MessageListener:

    def receive_message(self, msg):
        pass


class ZabbixNotifier(MessageListener):

    def __init__(self, tracker_master):
        assert isinstance(tracker_master, TrackerMaster)
        self.host_name = tracker_master.get_master().get_uniq_master_name()
        self.sender = ZabbixSender(CFG.zbx_sender_url())
        assert isinstance(tracker_master, TrackerMaster)
        self.tracker_master = tracker_master
        self.logger = logging.getLogger(ZabbixNotifier.__name__)

    def receive_message(self, msg):
        assert isinstance(msg, Message)
        slave = self.tracker_master.get_slave(msg.hw_id)
        device_name = Fields.ZBX_SLAVE_NAME_PREF + str(slave.zbx_slave_number)
        msg_key_name = device_name + '.' + msg.type.name.lower()
        charge_key_name = device_name + '.' + MonitoringName.CHARGE.value

        packet = [
            ZabbixMetric(self.host_name, msg_key_name, 1),
            ZabbixMetric(self.host_name, charge_key_name, msg.charge)
        ]
        sending_thread = threading.Thread(target=self.send_to_zabbix(packet))
        sending_thread.start()

    def send_to_zabbix(self, packet):
        try:
            self.logger.debug('Send packet: %s' % packet)
            resp = self.sender.send(packet)
            self.logger.debug('Response: %s' % resp)
        except timeout:
            # now just lost the data
            pass




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

import sys
import time
import logging
try:
    from Queue import Queue # python 2.7
except:
    from queue import Queue # python 3.7

from plezmo_ble_driver_py.observers import *

from plezmo.plezmo_exceptions.exceptions import *
from plezmo.elements.plezmo_element import PlezmoElement
from plezmo.elements.element_factory import ElementFactory
from plezmo.utils.logger import Logger
from plezmo.utils.command_helper import CmdHelper

from plezmo_ble_driver_py import config
config.__conn_ic_id__ = "NRF52"
from plezmo_ble_driver_py.ble_driver import BLEDriver, BLEAdvData, BLEEvtID, BLEEnableParams, BLEGapTimeoutSrc, BLEUUID, BLEGattStatusCode, BLEUUIDBase, BLEConfigConnGap, BLEConfigConnGatt, BLEConfig, BLEConfigGapRoleCount
from plezmo_ble_driver_py.ble_adapter import BLEAdapter, EvtSync

MAX_CONNECTIONS = 14
CFG_TAG = 1
PLEZMO_MTU = 23

class PlezmoAdapter(BLEDriverObserver, BLEAdapterObserver):
    BASE_UUID = BLEUUIDBase([0x5d, 0x4e, 0x00, 0x00, 0xac, 0x86, 0x4f, 0x8c, 0x99, 0x23, 0x8b, 0x7c, 0x13, 0x33, 0x70, 0xb9])
    _is_connecting = False

    def __init__(self, serial_port):
        self._logger = Logger()
        driver = BLEDriver(serial_port = serial_port, auto_flash = False)
        self._logger.debug('Driver created')
        adapter = BLEAdapter(driver)
        self.init(adapter)

    def init(self, adapter):
        super(PlezmoAdapter, self).__init__()
        self.adapter = adapter
        self.conn_q = Queue()
        self.discovery_q = Queue()
        self.adapter.observer_register(self)
        self.adapter.driver.observer_register(self)
        self.element_map = dict()
        self.element_map_by_name = dict()
        self.target_device_addr_type = None
        self.evt_sync = EvtSync(['connected', 'disconnected', 'sec_params',
                                'auth_status', 'conn_sec_update'])

    def open(self):
        config.__conn_ic_id__ = "NRF52"
        self.adapter.driver.open()

        # set BLE config before enabling
        gap_cfg = BLEConfigConnGap(conn_count = MAX_CONNECTIONS)
        gap_cfg.tag = CFG_TAG
        self.adapter.driver.ble_cfg_set(BLEConfig.conn_gap, gap_cfg)

        role_count_cfg = BLEConfigGapRoleCount(central_role_count = MAX_CONNECTIONS)
        self.adapter.driver.ble_cfg_set(BLEConfig.role_count, role_count_cfg)

        gatt_cfg = BLEConfigConnGatt(att_mtu = PLEZMO_MTU)
        gatt_cfg.att_mtu = self.adapter.default_mtu
        gatt_cfg.tag = CFG_TAG
        self.adapter.driver.ble_cfg_set(BLEConfig.conn_gatt, gatt_cfg)

        self.adapter.driver.ble_enable()
        self.adapter.driver.ble_vs_uuid_add(PlezmoAdapter.BASE_UUID)

    def close(self):
        self.adapter.close()

    def connect(self, element_name, element_type, connect_timeout = 10):
        if self._is_connecting == True:
            raise PlezmoInvalidStateException()
        self._logger.info("Connecting to element {} of type {}".format(element_name, element_type))
        self._element_name = element_name
        self._element_type = element_type
        self.adapter.driver.ble_gap_scan_start()
        self._logger.debug("Scan started before connect")
        self.verify_stable_connection()
        try:
            plezmo_element = self.conn_q.get(timeout = connect_timeout)
        except Exception as e:
            self._logger.error("Element not found in {} seconds".format(connect_timeout))
            self.adapter.driver.ble_gap_scan_stop()
            raise e

        att_mtu = self.adapter.att_mtu_exchange(plezmo_element.conn_handle, PLEZMO_MTU)

        self.adapter.service_discovery(plezmo_element.conn_handle)
        self.enable_notifications(plezmo_element.conn_handle)
        self.element_map[plezmo_element.conn_handle] = plezmo_element
        self.element_map_by_name[plezmo_element.name] = plezmo_element
        return plezmo_element
    
    def connect_by_mac(self, mac, element_type, connect_timeout = 5):
        if self._is_connecting == True:
            raise PlezmoInvalidStateException("Another connection in progress")
        self._logger.info("Connecting to element by mac {}".format(mac))
        discovered_elem = self.discovered_elements.get(mac)
        self._element_type = element_type
        if discovered_elem == None or discovered_elem["type"] != element_type.value:
            raise ValueError("Element details not available, run discover_elements() first.")
        else:
            self._element_name = discovered_elem["name"]
            self.target_device_addr_type = discovered_elem["peer_addr"]
            self.adapter.connect(discovered_elem["peer_addr"])
            self.verify_stable_connection()
            try:
                plezmo_element = self.conn_q.get(timeout = 10)
                self.target_device_addr_type = None
            except Exception as e:
                self._logger.error("Element not found in {} seconds".format(10))
                self.target_device_addr_type = None
                raise e
            att_mtu = self.adapter.att_mtu_exchange(plezmo_element.conn_handle)

            self.adapter.service_discovery(plezmo_element.conn_handle)
            self.enable_notifications(plezmo_element.conn_handle)
            self.element_map[plezmo_element.conn_handle] = plezmo_element
            self.element_map_by_name[plezmo_element.name] = plezmo_element
            return plezmo_element


    def get_element(self, conn_handle):
        return self.element_map.get(conn_handle)

    def get_element_by_name(self, name):
        return self.element_map_by_name.get(name)

    def get_connected_elements(self):
        return self.element_map_by_name

    def discover_elements(self, scan_timeout = 5):
        self._element_name = None
        self._element_type = None
        self.discovered_elements = {}
        self.adapter.driver.ble_gap_scan_start()
        self._logger.info("Scan started")
        try:
            self.discovery_q.get(timeout = scan_timeout)
        finally:
            #self.adapter.driver.ble_gap_scan_stop()
            return self.discovered_elements

    def enable_notifications(self, conn_handle):
        entry = self.adapter.db_conns[conn_handle]
        self._logger.debug("Enabling notifications for conn handle {}".format(conn_handle))
        if entry:
            for s in entry.services:
                chars = s.chars
                for c in chars:
                    if c.char_props.indicate == 1 or c.char_props.notify == 1:
                        if c.uuid.base.type == 2:
                            self._logger.debug("Enabling notification for custom char {}".format(c.uuid))
                            uuid_obj = BLEUUID(c.uuid.value, PlezmoAdapter.BASE_UUID)
                            self.adapter.enable_notification(conn_handle, uuid_obj)
                        else:
                            self._logger.debug("Enabling notification for standard char {}".format(c.uuid))
                            self.adapter.enable_notification(conn_handle, c.uuid)

    def disconnect(self, conn_handle):
        self.adapter.disconnect(conn_handle)
        self.evt_sync.wait('disconnected')

    def on_gap_evt_connected(self, ble_driver, conn_handle, peer_addr, role, conn_params):
        self._logger.info('New connection: {}'.format(conn_handle))
        self.evt_sync.notify(evt = 'connected', data = (conn_handle,peer_addr))

    def verify_stable_connection(self, timeout=15): 
        #ble_gap_scan_start has default scan timeperiod of 10 seconds. So conn_timeout of 10 seconds has higher probability of causing a race condition where ble_gap_scan_stop is called when scanning is not active.
        """ Verify connection event, and verify that unexpected disconnect
         events are not received.
        Returns:
            True if connected, else False.
        """
        conn_handle, peer_addr = self.evt_sync.wait('connected', timeout=timeout)
        if self.adapter.conn_in_progress == True:
            conn_handle, peer_addr = self.evt_sync.wait('connected')
        retries = 2
        while retries:
            if self.evt_sync.wait('disconnected', timeout=1) is None:
                break
            # logger.warning("Received unexpected disconnect event, "
            #                "trying to re-connect to: {}".format())
            time.sleep(1)
            self.adapter.connect(address = self.target_device_addr_type, tag = 1)
            conn_handle, peer_addr = self.evt_sync.wait('connected')
            retries -= 1
        else:
            if self.evt_sync.wait('disconnected', timeout=1) is not None:
                raise Exception("Failure - Connection failed due to 0x3e")
        logger.info("Successfully Connected")
        address_string  = "".join("{0:02X}".format(b) for b in peer_addr.addr)
        mac = ':'.join(address_string[i:i+2] for i in range(0, len(address_string), 2))
        connected_element = ElementFactory.create_element(self._element_name, self._element_type, mac, conn_handle, self)
        self.conn_q.put(connected_element)

    def on_gap_evt_disconnected(self, ble_driver, conn_handle, reason):
        self._logger.info('Disconnected: {} {}'.format(conn_handle, reason))
        self.evt_sync.notify(evt = 'disconnected', data = conn_handle)
        try:
            elem = self.element_map.get(conn_handle)
            if elem != None:
                del self.element_map[conn_handle]
                del self.element_map_by_name[elem.name]
            else:
                self._logger.info("Element to disconnect not found {}".format(conn_handle))
        except:
            self._logger.info("Error in deleting map key for {}".format(conn_handle))

    def on_gap_evt_timeout(self, ble_driver, conn_handle, src):
        if src == BLEGapTimeoutSrc.scan:
            ble_driver.ble_gap_scan_start()

    def on_gap_evt_adv_report(self, ble_driver, conn_handle, peer_addr, rssi, adv_type, adv_data):
        dev_name_list = None
        mfg_data = None
        element_type = None
        is_plezmo_element = False
        if BLEAdvData.Types.complete_local_name in adv_data.records:
            dev_name_list = adv_data.records[BLEAdvData.Types.complete_local_name]

        elif BLEAdvData.Types.short_local_name in adv_data.records:
            dev_name_list = adv_data.records[BLEAdvData.Types.short_local_name]

        else:
            self.continue_scan()
            return

        if BLEAdvData.Types.manufacturer_specific_data in adv_data.records:
            mfg_data = adv_data.records[BLEAdvData.Types.manufacturer_specific_data]
            if(mfg_data[0] == 0x96 and mfg_data[1] == 0x06):
                is_plezmo_element = True
                element_type = mfg_data[2]

        dev_name        = "".join(chr(e) for e in dev_name_list)
        address_string  = "".join("{0:02X}".format(b) for b in peer_addr.addr)
        self._logger.debug('Received advertisement report, address: 0x{}, device_name: {}, element_type {}, is_plezmo {}'.format(address_string,
                                                                                    dev_name, element_type, is_plezmo_element))

        if self._element_name != None and self._element_type != None:
            # this is connect mode
            if (is_plezmo_element == True and dev_name == self._element_name and element_type == self._element_type.value):
                self.target_device_addr_type = peer_addr
                self.adapter.connect(peer_addr, tag = 1)
                return
        else:
            # this is discover mode
            if is_plezmo_element == True and element_type != None:
                mac = ':'.join(address_string[i:i+2] for i in range(0, len(address_string), 2))
                self.discovered_elements[mac] = {"name":dev_name, "mac": mac, "type":element_type, "peer_addr":peer_addr}
        self.continue_scan()

    def on_notification(self, ble_adapter, conn_handle, uuid, data):
        self._logger.debug('Received notification: conn_handle={}, {} = {}'.format(conn_handle, uuid, data))
        CmdHelper.get_instance().handle_notification(conn_handle, uuid, data)

    def on_att_mtu_exchanged(self, ble_driver, conn_handle, att_mtu):
        self._logger.debug('ATT MTU exchanged: conn_handle={} att_mtu={}'.format(conn_handle, att_mtu))

    def on_gattc_evt_exchange_mtu_rsp(self, ble_driver, conn_handle, **kwargs):
        self._logger.debug('ATT MTU exchange response: conn_handle={}'.format(conn_handle))

    def send_cmd(self, conn_handle, char_num, cmd_data):
        uuid_obj = BLEUUID(char_num, PlezmoAdapter.BASE_UUID)
        self._logger.debug("cmd data {}, conn handle {}".format(cmd_data, conn_handle))
        self.adapter.write_req(conn_handle, uuid_obj, cmd_data)

    def read_element_value(self, conn_handle, uuid):
        status, data = self.adapter.read_req(conn_handle, BLEUUID(uuid))
        data1 = "".join(chr(e) for e in data)
        return data1
    
    def continue_scan(self):
        # Continue scan fails if scan is not in progress
        # Catch and ignore the exception
        try:
            self.adapter.driver.ble_gap_scan_continue()
        except:
            self._logger.debug("Failed to continue scan")

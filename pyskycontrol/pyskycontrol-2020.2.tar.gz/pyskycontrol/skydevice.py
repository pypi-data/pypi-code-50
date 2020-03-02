import datetime
import logging
import re
from time import sleep

import requests
from pyskycontrol import Helper

from .const import commands, urls, app_states

_LOGGER = logging.getLogger(__name__)


class SkyDevice:
    """Sky Control Class"""

    def __init__(self, device):
        """
        Create a new Sky TV instance.
        """
        self.device_name = device["name"]
        self.device_ip = device["ip"]
        self.device_port = device["port"]
        self.device_mac = device["mac"]
        self.device_manufacturer = device["manufacturer"]
        self.device_device_id = device["device_id"]
        self.device_model = device["model"]
        self.device_version_number = device["version_number"]
        self.device_xml_url = device["xml_url"]
        self.device_control_url = device["control_url"]
        self.device_scpd_url = device["scpd_url"]
        self.device_service_type = device["service_type"]
        self.device_state = None
        self.channels = {}
        self.channel_list = []
        self.program = {}

    def get_status(self):
        """Send soap command to the Sky Q box to get status"""
        sleep(4)
        self.device_state = 'STOPPED'
        test = Helper.request(request_type="GET",
                              response_type="JSON",
                              target=self.device_ip,
                              request_url=urls["info_url"])

        if test["activeStandby"] != True:
            command = "GetTransportInfo"
            response = Helper.soap_request(command, self.device_control_url)
            self.device_state = response.find('CurrentTransportState').string

        return self.device_state

    def channel_epg(self):
        """Get the Sky EPG"""
        request = Helper.request(request_type="GET",
                                 response_type="JSON",
                                 target=self.device_ip,
                                 request_url=urls["channel_epg"])

        for channel in request['services']:
            if channel["t"] not in self.channel_list:
                self.channels.update({channel["t"]: channel})
                self.channel_list.append(channel["t"])
        self.channels.update(
            {'Recording': {'sid': '0', 't': 'Recording'}})
        self.channels.update(
            {'App': {'sid': '0', 't': 'App'}})
        self.channel_list.append('Recording')
        self.channel_list.append('App')
        return self.channel_list

    def current_program(self):
        """Get the current channel"""
        self.program.clear()
        ps = None
        prog_type = None
        ch = None
        channel = None
        desc = None
        command = "GetMediaInfo"

        response = Helper.soap_request(command, self.device_control_url)
        soap_result = response.find('CurrentURI').string

        if soap_result is None and self.device_state in app_states:
            self.program.update({'type': 'App'})
            self.program.update({"channel": 'App'})
        elif soap_result is None:
            return self.program
        elif 'xsi' in soap_result:
            self.program.update({'type': 'Channel'})
            ps = str(int(re.split('\\bxsi://\\b', soap_result)[-1], 16))
        elif 'pvr' in soap_result:
            self.program.update({'type': 'Recording'})
            ps = "P" + re.split('\\bfile://pvr/\\b', soap_result)[-1].lower()

        if self.program['type'] == 'Channel':
            d = datetime.datetime.now()
            d_date = d.strftime('%Y%m%d')
            response = Helper.request(request_type='GET',
                                      response_type='JSON',
                                      request_url=urls["chn_list"].format(d_date, ps))
            p_list = response["schedule"][0]["events"]
            current_epoch = Helper.epochtime(
                datetime.datetime.now().strftime('%d.%m.%Y %H:%M:%S'),
                None, 'to_epoch')
            for prog in p_list:
                if prog["st"] + prog["d"] > current_epoch:
                    ch = prog
                    break

            for cha in self.channels:
                if ps == self.channels[cha]["sid"]:
                    self.program.update(
                        {"channel": self.channels[cha]['t']})
                    break

        elif self.program['type'] == 'Recording':
            response = Helper.request(request_type='GET',
                                      response_type='JSON',
                                      target=self.device_ip,
                                      request_url=urls["rec_list"])
            p_list = response["pvrItems"]
            for rec in p_list:
                if rec["pvrid"] == ps:
                    if 'cn' in rec:
                        self.program.update({"channel": rec['cn']})
                    if 'osid' in rec:
                        ps = rec['osid']
                    break

        if ch is not None:
            if 't' in ch:
                self.program.update({"title": ch['t']})
            if 'sy' in ch and ':' in ch['sy']:
                s_t = ch['sy'].split(":")
                self.program.update({'series_title': s_t[0]})
            if 'seasonnumber' in ch and 'episodenumber' in ch:
                self.program.update({"season": ch['seasonnumber']})
                self.program.update({"episode": ch['episodenumber']})
                self.program.update({"source_type":  'TV'})
            else:
                self.program.update({"source_type": 'Video'})
            if 'programmeuuid' in ch:
                imageurl = urls['metadata_url'].format(
                    str(ch['programmeuuid']), str(ps))
                self.program.update({"imageurl": imageurl})

        _LOGGER.debug(self.program)
        return self.program

    def remote(self, command):
        """Send a button press to the sky box."""
        Helper.sendcommand(self.device_ip, command)

import array
import math
import socket
import time
import threading

import requests
from bs4 import BeautifulSoup

from .const import commands, port, urls


class Helper:
    """Helper class to comunicate with the devices."""

    def __init__(self):
        """Intialisation"""
        self.lock = threading.Lock()

    @staticmethod
    def sendcommand(host, command):
        """Send command to the Sky Q box"""
        self.lock.acquire()

        code = commands[command]
        cmd1 = int(math.floor(224 + (code / 16)))
        cmd2 = int(code % 16)
        command1 = array.array('B', [4, 1, 0, 0, 0, 0, cmd1, cmd2]).tostring()
        command2 = array.array('B', [4, 0, 0, 0, 0, 0, cmd1, cmd2]).tostring()

        s = socket.socket()
        s.connect((host, port))  # connect to Sky TV box
        reply = s.recv(12)  # Receive handshake
        s.send(reply)  # send handshake
        reply = s.recv(2)  # Receive 2 bytes
        s.send(reply)  # send 1 byte
        reply = s.recv(24)  # Receive 24 bytes

        s.send(command1)  # send command bytes part 1
        s.send(command2)  # send command bytes part 2

        s.close()  # close connection

        self.lock.release()

    @staticmethod
    def request(request_type, request_url, response_type=None, target=None, headers=None):
        """JSON Call to Sky Box"""
        json_url = request_url
        response = None
        if target is not None:
            json_url = urls["start"] + str(target) + str(request_url)

        if request_type == 'POST':
            response = requests.post(json_url, data=None, headers=headers)
        elif request_type == 'GET':
            response = requests.get(json_url, data=None, headers=headers)

        if response_type == 'JSON':
            json_data = response.json()
            return json_data
        else:
            return response

    @staticmethod
    def soap_request(command, ctrl_url):
        """Make a Soap request"""

        xml_body = """<?xml version="1.0" encoding="utf-8"?>
                <s:Envelope s:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/" xmlns:s="http://schemas.xmlsoap.org/soap/envelope/">
                <s:Body>
                <u:{} xmlns:u="urn:schemas-nds-com:service:SkyPlay:2">
                <InstanceID>0</InstanceID>
                </u:{}>
                </s:Body>
                </s:Envelope>""".format(command, command)

        headers = {
            "Content-Length": "{}".format(len(xml_body)),
            "SOAPACTION":
                "\"urn:schemas-nds-com:service:SkyPlay:2#{}\"".format(command),
            "Content-Type": "text/xml; char-set=utf-8"}

        xml_response = requests.post(
            url=ctrl_url, data=xml_body, headers=headers)
        return BeautifulSoup(xml_response.text, "lxml-xml")

    @staticmethod
    def epochtime(date_time, pattern, action):
        """ date/time conversion to epoch"""
        if action == 'to_epoch':
            pattern = '%d.%m.%Y %H:%M:%S'
            epochtime = int(time.mktime(
                time.strptime(str(date_time), pattern)))
            return epochtime
        elif action == 'from_epoch':
            date = datetime.fromtimestamp(int(date_time)).strftime(pattern)
            return date

    @staticmethod
    def get_sec(epoch):
        """Convert epoch time into total seconds."""
        clock = time.strftime('%H:%M:%S', time.localtime(epoch))
        h, m, s = clock.split(':')
        return int(h) * 3600 + int(m) * 60 + int(s)

    @staticmethod
    def xml(request):
        """Clean the xml response."""
        return BeautifulSoup(request.text, 'lxml-xml')

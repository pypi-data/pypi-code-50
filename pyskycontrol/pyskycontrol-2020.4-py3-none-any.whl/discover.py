import re
import socket
from typing import Dict

from pyskycontrol import Helper
from .const import msg, UDP_headers, urls, port


class Discover:
    """Discover Sky TV devices on the network."""

    def boxes(timeout=30):
        """
        Search for Sky Q Boxes on local network.
        """
        device = {}
        devices = {}

        # Set up UDP socket.
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM,
                          socket.IPPROTO_UDP)
        s.settimeout(timeout)
        s.sendto(msg.encode(), ('239.255.255.250', 1900))

        try:
            while True:
                data, addr = s.recvfrom(65507)
                data_text = data.decode("utf-8")
                url = re.search("(?P<url>https?://[^\s]+)",
                                data_text).group("url")
                if "Sky" in data_text:
                    if addr[0] not in device:
                        device[addr[0]] = []
                    device[addr[0]].append(url)
        except socket.timeout:
            pass

        compl = []
        for IP in device:
            for url in device[IP]:
                if IP in compl:
                    break
                else:
                    try:
                        request = Helper.request(
                            request_type='GET',
                            request_url=url,
                            headers=UDP_headers
                        )
                        response = Helper.xml(request)
                        base_url = response.find(
                            'URLBase').string[:-1]
                        for node in response.find_all('service'):
                            service = node.serviceType.string
                            ctrl_url = base_url + node.controlURL.string
                            scpd_url = base_url + node.SCPDURL.string

                            if "SkyPlay:2" in service and \
                                    "player_avt.xml" in scpd_url:
                                result = Helper.request(
                                    request_type='GET',
                                    response_type='JSON',
                                    target=IP,
                                    request_url=urls[
                                        "info_url"]
                                )
                                data = {'name': result["btID"],
                                        'ip': IP,
                                        'port': port,
                                        'mac': result["MACAddress"],
                                        'manufacturer': result["manufacturer"],
                                        'device_id': result["deviceID"],
                                        'model': result["hardwareModel"],
                                        'version_number': result["versionNumber"],
                                        'xml_url': url,
                                        'control_url': ctrl_url,
                                        'scpd_url': scpd_url,
                                        'service_type': service}
                                devices[IP] = data
                                compl.append(IP)
                    except:
                        pass

        return devices

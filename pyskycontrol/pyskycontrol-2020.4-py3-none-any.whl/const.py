urls = {
    "start": "http://",
    "status": ":9006/as/system/status",
    "info_url": ":9006/as/system/information",
    "rec_list": ":9006/as/pvr?limit=1000&offset=0",
    "rec_info": ":9006/as/pvr/details/{0}",
    "chn_list": "http://awk.epgsky.com/hawk/linear/schedule/{0}/{1}",
    "channel_epg": ":9006/as/services",
    "channel_info": "9006/as/service/details/{0}",
    "metadata_url": "https://images.metadata.sky.com/pd-image/{0}/16-9?sid={1}",
    'xml_base': 'https://www.xmltv.co.uk'
}

commands = {
    "power": 0,
    "select": 1,
    "backup": 2,
    "dismiss": 2,
    "channelup": 6,
    "channeldown": 7,
    "interactive": 8,
    "sidebar": 8,
    "help": 9,
    "services": 10,
    "search": 10,
    "tvguide": 11,
    "home": 11,
    "i": 14,
    "text": 15,
    "up": 16,
    "down": 17,
    "left": 18,
    "right": 19,
    "red": 32,
    "green": 33,
    "yellow": 34,
    "blue": 35,
    "0": 48,
    "1": 49,
    "2": 50,
    "3": 51,
    "4": 52,
    "5": 53,
    "6": 54,
    "7": 55,
    "8": 56,
    "9": 57,
    "play": 64,
    "pause": 65,
    "stop": 66,
    "record": 67,
    "fastforward": 69,
    "rewind": 71,
    "boxoffice": 240,
    "sky": 241
}
# UDP message.
msg = \
    'M-SEARCH * HTTP/1.1\r\n' \
    'HOST:239.255.255.250:1900\r\n' \
    'ST:upnp:rootdevice\r\n' \
    'MX:2\r\n' \
    'MAN:"ssdp:discover"\r\n' \
    '\r\n'
UDP_headers = {
    'USER-AGENT': 'SKY_skyplus',
    'CONTENT-TYPE': 'text/xml; charset="utf-8"'
}

xml_body = """<?xml version="1.0" encoding="utf-8"?>
                <s:Envelope s:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/" xmlns:s="http://schemas.xmlsoap.org/soap/envelope/">
                <s:Body>
                <u:{} xmlns:u="urn:schemas-nds-com:service:SkyPlay:2">
                <InstanceID>0</InstanceID>
                </u:{}>
                </s:Body>
                </s:Envelope>"""
port = 49160
search_timeout = 5
app_states = ['PLAYING', 'PAUSED_PLAYBACK']

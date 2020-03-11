# --*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*-+
# -*- coding: utf-8 -*-                            |
# @Time    : 2020/2/11 22:25                      *
# @Author  : Bob He                                |
# @FileName: get_ip.py                              *
# @Software: PyCharm                               |
# @Project : ddcmaker                          *
# @Csdn    ：https://blog.csdn.net/bobwww123       |
# @Github  ：https://www.github.com/NocoldBob      *
# --*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*-+

import time
import requests
import json
from ddcmaker.server import constant, getip_address as gp


def poststatus():
    url = constant.url0 + constant.type_link + constant.maker_dict[2]
    macaddr = gp.get_mac_address()
    while True:
        data_json2 = json.dumps({'macAddr': macaddr, 'onlineStatus': 1})
        headers = {'content-type': 'application/json;charset=UTF-8'}
        try:
            r_json=requests.post(url, data_json2, headers=headers)
            print(r_json)
        except:
            time.sleep(3)
            return poststatus
        time.sleep(10)


def poststatus_online():
    url = constant.url + constant.type_link + constant.maker_dict[2]
    macaddr = gp.get_mac_address()
    while True:
        data_json2 = json.dumps({'macAddr': macaddr, 'onlineStatus': 1})
        headers = {'content-type': 'application/json;charset=UTF-8'}
        try:
            r_json=requests.post(url, data_json2, headers=headers)
            print(r_json)
        except:
            time.sleep(3)
            return poststatus_online
        time.sleep(10)

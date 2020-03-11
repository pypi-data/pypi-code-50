# --*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*-+
# -*- coding: utf-8 -*-                            |
# @Time    : 2020/2/11 22:50                      *
# @Author  : Bob He                                |
# @FileName: getip_address.py                              *
# @Software: PyCharm                               |
# @Project : ddcmaker                          *
# @Csdn    ：https://blog.csdn.net/bobwww123       |
# @Github  ：https://www.github.com/NocoldBob      *
# --*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*-+

import socket
import requests
import re
import time
import json
import ddcmaker
version = ddcmaker.__version__


def get_mac_address():
    import uuid
    mac = uuid.UUID(int=uuid.getnode()).hex[-12:].upper()
    return '%s:%s:%s:%s:%s:%s' % (mac[0:2], mac[2:4], mac[4:6], mac[6:8], mac[8:10], mac[10:])


def get_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        try:
            s.connect(('www.baidu.com', 0))
        except:
            print("无法连接到外网！")
        ip = s.getsockname()[0]
    except:
        ip = "x.x.x.x"
    finally:
        s.close()
    return ip


def get_extranetip():
    #try:
    #    response = requests.get("http://" + str(time.localtime().tm_year) + ".ip138.com/ic.asp", timeout=2)
    #    ip = re.search(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", response.content.decode(errors='ignore')).group(0)
    #    if len(str(ip)) > 7:
    #        return ip
    #except Exception as e:
    try:
        ip = requests.get("http://members.3322.org/dyndns/getip", timeout=3).text.strip()
        # print(ip)
        if len(str(ip)) > 7:
            return ip
    except Exception as e:
        text = requests.get("http://txt.go.sohu.com/ip/soip", timeout=2).text
        ip = re.findall(r'\d+.\d+.\d+.\d+', text)[0]
        if len(str(ip)) > 7:
            return ip
        print("暂时无法发出外网请求！")


def getipadress():
    ip = get_ip()
    macaddr = get_mac_address()
    extranetip = get_extranetip()
    return ip, macaddr, extranetip


def postaddress(ip, macaddr, extranetip, url_json, typeint):
    #from ddcmaker import __version__ as version
    data_json = json.dumps(
        {'inIp': ip, 'macAddr': macaddr, 'exIp': extranetip, 'type': typeint, 'ddcmaker_version':version})  # dumps：将python对象解码为json数据,机器人的类型为0
    headers = {'content-type': 'application/json;charset=UTF-8'}
    print(data_json)
    r_json = requests.post(url_json, data_json, headers=headers)
    print(r_json)
    if r_json.status_code == 200:
        return ip
    elif r_json.status_code == 504:
        print("当前服务器接口不通")
        time.sleep(15)
    else:
        time.sleep(15)
        return postaddress(ip, macaddr, extranetip, url_json, typeint)


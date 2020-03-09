#!/usr/bin/python3.7
# encoding: utf-8

import json
import sys
import requests
import platform
import time
import base64
import rsa
from cdnutil import config
from cdnutil.Log import Logger
from cdnutil import basepy

logger = Logger(__name__).getLogger()
headers = {"content-type": "application/json"}

cdnAccTk = None
lastTouchTime = 0
firstTouchTime = 0
def iniAreaClusterNo():
    """
    初始化区域码
    :return: 返回区域码
    """
    #url = "http://127.0.0.1:80/monitor"
    url = config.getPropertyValue("iap_cluster_id_req_url")
    result = None
    if basepy.getPyVer().startswith("2"):
        result = requests.get(url)
    else:
        result = requests.get(url = url)

    logger.info("url = {}, result = {}".format(url, result))
    if result is None or result.text is None:
        logger.warning("result is none")
        return None
    logger.info("url = {}, result = {}".format(url, result.text))
    if json.loads(result.text).get("status").find("ok") != -1:
        return json.loads(result.text).get("cluster_id")

    return None


def str2key(s):
    """
    @author liangzhi from https://www.cnblogs.com/masako/p/7660418.html
    :param s:
    :return:
    """
    # 对字符串解码
    b_str = base64.b64decode(s)

    if len(b_str) < 162:
        return None

    hex_str = ''
    isPy2 = basepy.getPyVer().startswith("2")

    # 按位转换成16进制
    for x in b_str:
        if isPy2:
            h = hex(ord(x))[2:]
        # python3.7用法
        else:
            h = hex(x)[2:]
        h = h.rjust(2, '0')
        hex_str += h

    logger.info("hex_str:" + hex_str)
    # 找到模数和指数的开头结束位置
    m_start = 29 * 2
    e_start = 159 * 2
    m_len = 128 * 2
    e_len = 3 * 2

    modulus = hex_str[m_start:m_start + m_len]
    exponent = hex_str[e_start:e_start + e_len]

    return modulus, exponent


def base64str(message, key):
    """
   @author liangzhi from https://www.cnblogs.com/masako/p/7660418.html
   :param s:
   :return:
   """
    modulus = int(key[0], 16)
    exponent = int(key[1], 16)
    rsa_pubkey = rsa.PublicKey(modulus, exponent)
    crypto = rsa.encrypt(message.encode(), rsa_pubkey)
    b64str = base64.b64encode(crypto)
    return b64str
	
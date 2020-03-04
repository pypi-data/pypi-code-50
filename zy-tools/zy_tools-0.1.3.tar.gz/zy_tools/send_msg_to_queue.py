# !/usr/bin/env python
# _*_coding: utf-8 _*_
# @Time: 2019/10/9 9:53
# @Author: "John"
import base64
import json
import requests
import urllib3

urllib3.disable_warnings()


def send_msg_2_queue(msg, queue_name, service_address):
    """

    :param msg: 消息内容，需要 String 或者 json.dumps(object)
    :param queue_name:
    :param service_address:
    :return:
    """
    data = {
        "message": base64.b64encode(msg.encode('utf-8')).decode("utf-8"),
        "queueName": queue_name,
        "priority": 8,
        "delaySeconds": ""
    }

    s = requests.session()
    s.verify = False
    s.trust_env = False
    s.headers = {"Content-type": "application/json; charset=UTF-8", "Accept": "application/json"}

    response = s.post(service_address, data=json.dumps(data).encode('utf-8'))
    if not json.loads(response.text).get("error_code"):
        return 1

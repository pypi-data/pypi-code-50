#!/usr/bin/python
# -*- coding: UTF-8 -*-
import time
import hmac
import hashlib
import base64
import urllib, json
from urllib.request import Request, urlopen

class Dingtalk:

    _secret = ""
    _access_token = ""
    _send_api = "https://oapi.dingtalk.com/robot/send?access_token="
    _headers = {"Content-Type": "application/json"}

    """
    初始化，创建群机器人时获取secret及access_token

    secret: 加签串，验签方式保证接口安全
    access_token: 访问token
    """
    def __init__(self, secret="", access_token=""):
        self._secret = secret
        self._access_token = access_token
    
    """
    获取时间戳及签名串
    """
    def _get_timestamp_sign(self):

        timestamp = int(round(time.time() * 1000))
        secret_enc = bytes(self._secret, 'utf-8')
        string_to_sign = '{}\n{}'.format(timestamp, self._secret)
        string_to_sign_enc = bytes(string_to_sign, 'utf-8')

        hmac_code = hmac.new( secret_enc, string_to_sign_enc, digestmod=hashlib.sha256).digest()
        sign = urllib.parse.quote_plus(base64.b64encode(hmac_code))

        return timestamp, sign

    """
    生成消息发送URL
    """
    def _get_dingtalk_send_api(self):
        timestramp, sign = self._get_timestamp_sign()
        return "{}{}&timestamp={}&sign={}".format(self._send_api, self._access_token, timestramp, sign)

    """
    发送文本消息

    message: 要发送的文本内容
    atMobiles: 需at提醒的钉钉用户手机号列表
    isAtall: 是否at提醒所有群用户
    """
    def send_text(self, message, atMobiles=[], isAtAll=False):
        raw = {"msgtype": "text", "text": {"content": message}, "at": {"atMobiles": atMobiles, "isAtAll": isAtAll}}
        return self._send_message(raw)
    
    """
    发送MarkDown文本消息

    message: 要发送的文本内容
    atMobiles: 需at提醒的钉钉用户手机号列表
    isAtall: 是否at提醒所有群用户
    """
    def send_markdown(self, title, content, atMobiles=[], isAtAll=False):
        raw = {"msgtype": "markdown", "markdown": {"title": title, "text": content}, "at": {"atMobiles": atMobiles, "isAtAll": isAtAll}}
        return self._send_message(raw)

    """
    发送图文链接

    title: 图文链接标题
    content: 图文摘要
    picUrl: 图文中图片链接
    messageUrl: 图文链接目标地址
    """
    def send_link(self, title, content, picUrl, messageUrl):
        raw = {"msgtype": "link", "link": {"text": content, "title": title, "picUrl": picUrl, "messageUrl": messageUrl}}
        return self._send_message(raw)
        
    
    """
    发送ActionCard消息

    title: 信息标题
    content: 信息内容
    btns: 按钮组信息，支持一个按钮和多个按钮；title-按钮方案，actionURL-点击按钮触发的URL
    btnOrientation: 0-按钮竖直排列，1-按钮横向排列
    hideAvatar: 0-正常发消息者头像，1-隐藏发消息者头像
    """
    def send_action_card(self, title, content, btns=[], btnOrientation="0", hideAvatar="0"):
        raw = {
                "msgtype": "actionCard",
                "actionCard": {
                    "title": title,
                    "text": content,
                    "hideAvatar": hideAvatar,
                    "btnOrientation": btnOrientation
                }
            }

        if len(btns) == 1:
            raw["actionCard"]["singleTitle"] = btns[0]["title"]
            raw["actionCard"]["singleURL"] = btns[0]["actionURL"]
        else:
            raw["actionCard"]['btns'] = btns

        return self._send_message(raw)

    """
    发送feed链接组

    links: feed组
        title: 信息标题
        picURL: 信息图片URL
        messageURL: 信息目标链接地址
    """
    def send_feed_card(self, links=[]):
        raw = {
                "msgtype": "feedCard",
                "feedCard": {
                    "links": links
                }
            }
        return self._send_message(raw)

    """
    消息体发送

    json_data: 所要发送的消息体
    """
    def _send_message(self, json_data={}):
        url = self._get_dingtalk_send_api()
        data = bytes(json.dumps(json_data), "utf-8")
        request = Request(url, headers={"Content-Type": "application/json"}, data=data)
        response = urlopen(request)
        html = response.read().decode("utf-8")
        result = json.loads(html)
        
        return result['errcode'], result["errmsg"]



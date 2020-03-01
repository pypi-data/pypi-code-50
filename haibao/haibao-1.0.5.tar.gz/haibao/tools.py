# -*- encoding: utf-8 -*-
import requests
import json


__method__ = ['getAddressByIp', 'getSampleAddressByTp', 'getUserAgent', 'sendBuyFreeCool', 'getFreeCool']
__author__ = u'seal'


def getMethod():
    return __method__


def getAddressByIp(ip):
    """
    通过ip地址获取归属地以及其他详细信息
    """
    if not isinstance(ip, str) and not isinstance(ip, unicode):
        raise ValueError('ipaddress must be str')
    headers = {'User-Agent': 'Mozilla/5.0'}
    url = 'https://sp0.baidu.com/8aQDcjqpAAV3otqbppnN2DJv/api.php?query={}&resource_id=6006'.format(ip)
    try:
        html = requests.get(url=url, headers=headers).text
        data = json.loads(html)
    except Exception as e:
        return 'time error'
    return data


def getSampleAddressByIp(ip):
    """
    通过ip地址获取归属地
    """
    data = getAddressByIp(ip)
    if isinstance(data, dict):
        try:
            data = data['data'][0]['location']
        except:
            return 'time error'
    return data


def getUserAgent():
    """
    返回一个User-Agent
    """
    return 'Mozilla/5.0'


def sendBuyFreeCool(cookie, thread=5, threadEvery=200):
    """
    给coolgay发送购买免费套餐信息
    """
    url = 'https://coolgay.online/user/buy'
    data = {
        'shop': '3',
        'autorenew': '1',
        'disableothers': '1',
    }
    headers = {
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'cache-control': 'no-cache',
        'content-length': '42',
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Cookie": cookie,
        "Host": "coolgay.online",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3970.5 Safari/537.36",
    }
    from threading import Thread
    def send(t):
        i=0
        while i<t:
            try:
                html = requests.post(url=url, data=data, headers=headers, timeout=10).text
                print json.loads(html)['msg']
            except:
                pass
            i += 1
    
    for i in range(thread):
        t = Thread(target=send, args=(threadEvery,))
        t.start()
        print i


def getFreeCool(username, password):
    return u'to be continued'


def getBaiduVerifyCode(short_url=None):
    url = 'https://api.newday.me/share/disk/query/'
    data = {
        'share_id': short_url,
        'share_point': '90.5343828201294:103.57572078704834',
        'share_link': 'https://pan.baidu.com/share/init?surl='+short_url,
        'mode': 'script',
        'version': '0.3.7',
        'browser': 'chrome',
    }
    headers = {
        'Host': 'api.newday.me',
        'User-Agent': 'Mozilla/5.0',
    }
    html = requests.post(headers=headers, url=url, data=data).text
    return html

def qiniuyun_message(tel):
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'cache-control': 'no-cache',
        'content-length': '79',
        'content-type': 'application/json;charset=UTF-8',
        'cookie': '',
        'origin': 'https://portal.qiniu.com',
        'pragma': 'no-cache',
        'referer': 'https://portal.qiniu.com/signup',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.100 Safari/537.36',
    }
    url = 'https://portal.qiniu.com/api/gaea/verification/sms/send'
    data = {
        'operation': '1',
        'is_voice': 'false',
        'mobile_number': tel,
        'captcha_type': '2',
    }
    html = requests.post(url=url, headers=headers,  json=data).text
    return html

def message_bang(tel):
    qiniuyun_message(tel)

if __name__ == '__main__':
    pass
    


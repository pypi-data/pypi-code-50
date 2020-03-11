# -*- coding: UTF-8 -*
from __future__ import print_function

import hashlib
import json
import random
import time

__version__ = "1.0.0"


class IRApiBase(object):
    apiurl = None

    @classmethod
    def md5(clz, src):
        if type(src) == type(u''):
            src = src.encode('utf8')
        return hashlib.md5(src).hexdigest()

    @classmethod
    def md5sign(clz, data, key):
        l = ['%s=%s' % (k, v) for (k, v) in data.items() if v]
        l.sort()
        s = '&'.join(l)
        s = '%s&key=%s' % (s, key)
        ms = IRApiBase.md5(s).upper()
        return ms

    @classmethod
    def nonce_str(clz):
        return IRApiBase.md5('%s%s' % (time.time(), random.randint(100000, 999999)))[0:24]

    def doapi(self, apiname, data):
        import requests
        if isinstance(data, dict):
            if 'noncestr' not in data:
                data['noncestr'] = IRApiBase.nonce_str()
            if 'sign' not in data:
                data['sign'] = IRApiBase.md5sign(data, self.appkey)
                #             data = json.dumps(data)
        r = requests.request('post', url='%s%s' % (self.apiurl, apiname), data=data)
        r.raise_for_status()
        res = json.loads(r.content)
        return res


class IRIRApi(IRApiBase):
    def __init__(self, appid, appkey, apiurl=None, *args, **kwargs):
        object.__init__(self, *args, **kwargs)
        self.appid = appid
        self.appkey = appkey
        if apiurl:
            self.apiurl = apiurl
        if not self.apiurl:
            raise ValueError("Has not apiurl")

    def doapi(self, apiname, data):
        if isinstance(data, dict):
            if 'appid' not in data:
                data['appid'] = self.appid
        return IRApiBase.doapi(self, apiname, data)

    def sendCode(self, phone, code):
        return self.doapi('sendSMSCode', {'phones': phone, 'code': code})['code'] == 0

    def sendNoti(self, phones, content, sign_name='', template_code=''):
        if type(phones) == list:
            phones = ','.join(phones)
        return self.doapi('sendSMSNoti', {'phones': phones, 'content': content, 'sign_name': sign_name, 'template_code': template_code})['code'] == 0

    def sendWS(self, data, tag, filterdic=None):
        return self.doapi('sendWS', {'datajson': json.dumps(data), 'tag': tag, 'filterjson': json.dumps(filterdic) if filterdic else None})

    def transLang(self, **param):
        return self.doapi('transLang', param)


def main():
    import argparse
    try:
        import urlparse as parse
    except:
        from urllib import parse

    parser = argparse.ArgumentParser(add_help=True)
    parser.add_argument('-u', '--apiurl', help='the API base url', required=True)
    parser.add_argument('-a', '--appid', help='the APPID', required=True)
    parser.add_argument('-k', '--appkey', help='the APPKEY', required=True)
    parser.add_argument('-i', '--apiname', help='the api name', required=True)
    parser.add_argument('-d', '--data', help='the json data')
    args = parser.parse_args()

    api = IRIRApi(appid=args.appid, appkey=args.appkey, apiurl=args.apiurl)
    data = args.data
    param = parse.parse_qs(data)
    data = {
        k: v[0] for k, v in param.items()
    }
    r = api.doapi(args.apiname, data=data)

    print(json.dumps(r, ensure_ascii=False))
    if r.get('msg'):
        print('\033[41;30m%s\033[0m' % (r['msg']))
    exit(r.get('code'))


if __name__ == '__main__':
    main()

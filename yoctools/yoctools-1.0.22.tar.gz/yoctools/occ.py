import sys
import json
import time
from requests_toolbelt import MultipartEncoder

try:
    raw_input = raw_input
except NameError:
    raw_input = input

try:
    from component import *
    from tools import *
    from log import logger
except:
    from yoctools.component import *
    from yoctools.tools import *
    from yoctools.log import logger


def get_url(cmd, text):
    timestamp = time.strftime('%Y-%m-%d_%H:%M:%S', time.localtime(time.time()))
    md5 = MD5(cmd + timestamp + text)
    return '%s?timestamp=%s&sign=%s' % (cmd, timestamp, md5)


authorization = ''
login_time = 0


class OCC:
    def __init__(self, host=None):
        if host:
            self.host = host
        else:
            self.host = 'occ.t-head.cn'
            self.host = 'pre.occ.t-head.cn'

    def logout(self):
        global authorization, login_time
        authorization = ''
        login_time = 0

    def login(self):
        global authorization, login_time

        if authorization and time.time() - login_time < 25 * 50:
            return
        username = ''
        password = ''
        config_file = os.path.expanduser('~/.yocrc')
        conf = yaml_load(config_file)
        if conf == None:
            conf = {}
        if 'username' in conf:
            username = conf['username']
        else:
            username = raw_input('Input occ login username: ')

        if 'password' in conf:
            password = conf['password']
        else:
            password = raw_input('Input user password: ')

        cmd = '/api/base/auth/login'
        body = {
            "name": username,
            "password": password
        }
        js, _ = self.request(cmd, body)
        if 'userToken' in js:
            authorization = js['userToken']
            login_time = time.time()

    def upload(self, version, type, filename):
        global authorization, login_time
        cmd = '/api/resource/component/upload'

        m = MultipartEncoder(
            fields={
                'version': version.upper(),
                'type': type,
                'file': (os.path.basename(filename), open(filename, 'rb'))
            }
        )
        headers = {
            'Content-Type': m.content_type,
            'Authorization': authorization,
        }

        js, error = self.request(cmd, m.to_string(), headers, sign=False)
        if error == -2:
            self.logout()
            self.login()
            js, error = self.request(cmd, m, headers, sign=False)
        return error

    def yocGetInfo(self, name):
        cmd = '/api/resource/component/getInfo'
        body = {}
        js, _ = self.request(cmd, body)

    def getComponentPage(self, pageIndex, components):
        pageSize = 100
        cmd = '/api/resource/component/getList'
        body = {
            "type": "",
            "name": "",
            "pageIndex": pageIndex,
            "pageSize": pageSize,
        }

        js, _ = self.request(cmd, body)
        # logger.debug(json.dumps(js, indent=4))

        if 'packages' in js:
            for p in js['packages']:
                pack = Component()
                pack.loader_json(p)
                components.add(pack)
                # pack.show()

            return len(js['packages']) == pageSize

    def yocComponentList(self, chipId):
        idx = 1
        packs = ComponentGroup()
        while self.getComponentPage(idx, packs):
            idx += 1

        return packs

    def request(self, url, body, headers=None, sign=True):
        if sign:
            body = json.dumps(body)
            url = get_url(url, body)

        connection = http.HTTPSConnection(self.host)

        try:
            if not headers:
                headers = {"Content-type": "application/json"}
            connection.request('POST', url, body, headers)
            response = connection.getresponse()
            if response.status == 200:
                text = response.read()
                js = json.loads(text)

                if js['code'] != 0:
                    logger.error(js['msg'])
                return js['result'], js['code']
        except Exception as e:
            logger.error(str(e))

        return {}, -1


if __name__ == "__main__":
    occ = OCC()
    occ.login()

    occ.yocComponentList('')
    # occ.upload("master", 'common', 'netmgr.zip')
    # occ.upload('master', 'common', 'setup.py')


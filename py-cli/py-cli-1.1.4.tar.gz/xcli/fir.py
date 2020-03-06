# -*- coding: UTF-8 -*-

import json

import requests
from androguard.core.bytecodes.apk import APK

from xcli import PyCliConfig, apks


class FirToken:
    token = ''
    application_id = ''

    def __init__(self, t: str, app_id: str):
        self.token = t
        self.application_id = app_id


class FirCertEntry:
    class CertMeta:
        key = ''
        token = ''
        upload_url = ''

        def __init__(self, cert_json: json):
            self.key = cert_json['key']
            self.token = cert_json['token']
            self.upload_url = cert_json['upload_url']

    type = ''
    short = ''
    icon: CertMeta
    binary: CertMeta

    prefix = ''

    def __init__(self, result_json):
        self.type = result_json['type']
        self.short = result_json['short']

        cert_json = result_json['cert']

        self.icon = self.CertMeta(cert_json['icon'])
        self.binary = self.CertMeta(cert_json['binary'])
        self.prefix = cert_json['prefix']


# 获取 fir 的上传凭证
def validate(token: FirToken):
    params = {'type': 'android',
              'bundle_id': token.application_id,
              'api_token': token.token}

    response_result = requests.post('http://api.jappstore.com/apps', data=params)

    # 拿到cert实体
    cert_json = json.loads(response_result.content)
    if 'code' in cert_json:
        raise RuntimeError('[ERROR]: fir认证失败：%d：%s' % (cert_json['code'], cert_json['errors']['exception']))

    return FirCertEntry(cert_json)


# 上传到fir
def publish(fir_cert: FirCertEntry, manifest: apks.Manifest):
    file = {'file': open(manifest.deploy_abspath, 'rb')}
    params = {
        "key": fir_cert.binary.key,
        "token": fir_cert.binary.token,
        "x:name": manifest.app_name,
        "x:version": manifest.version_name,
        'x:build': manifest.version_code,
        "x:changelog": manifest.change_log
    }

    requests.packages.urllib3.disable_warnings()
    req = requests.post(fir_cert.binary.upload_url, files=file, data=params, verify=False)

    update_result = json.loads(req.content)

    return update_result['is_completed']


def test_fir_publish():
    config = PyCliConfig()

    _UPDATE_FILE_PATH = '/Users/handy/datum/workspace/t/EmptyApp/app/build/outputs/apk/release/app-release.apk'
    apk = APK(_UPDATE_FILE_PATH)

    fir_cert = validate(FirToken(config.fir_token, apk.get_package()))

    manifest = apks.Manifest(apk)
    manifest.deploy_abspath = _UPDATE_FILE_PATH
    _is_completed = publish(fir_cert, manifest)

    print('[INFO]: test_fir_publish: %s' % _is_completed)

# -*- coding: UTF-8 -*-
import threading
from os import path, environ

from oss2 import Auth

from lang.xio import Properties

__title__ = 'py-cli'
__version__ = '1.1.4'


class PyCliConfig(object):
    """
    PyCli配置，其配置文件保存在~/.pycli

    endpoint=http://oss-cn-hangzhou.aliyuncs.com
    access_key_id=<your oss access key id>
    access_key_secret=<your oss access key secret>
    bucket=apk-res
    fir_token=<fir.in token>
    """
    __instance_lock = threading.Lock()

    props = {}

    endpoint = 'http://oss-cn-hangzhou.aliyuncs.com'
    access_key_id = ''
    access_key_secret = ''
    bucket = 'apk-res'
    fir_token = ''

    auth: Auth = None

    def __init__(self):
        self.props = Properties(path.join(environ['HOME'], '.pycli')).dict()

        self.access_key_id = self.props.get('access_key_id')
        self.access_key_secret = self.props.get('access_key_secret')
        self.bucket = self.props.get('bucket')
        self.endpoint = self.props.get('endpoint')
        self.fir_token = self.props.get('fir_token')

    def __new__(cls, *args, **kwargs):
        if not hasattr(PyCliConfig, "_instance"):
            with PyCliConfig.__instance_lock:
                if not hasattr(PyCliConfig, "_instance"):
                    PyCliConfig._instance = object.__new__(cls)
        return PyCliConfig._instance


def load_config():
    return PyCliConfig()


__all__ = ['__title__', '__version__', 'PyCliConfig']

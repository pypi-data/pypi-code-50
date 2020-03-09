# -*- coding: UTF-8 -*-
import os
import sys
import threading
from os import path, environ
from getopt import getopt

from oss2 import Auth

from lang.io import Properties

__title__ = 'py-cli'
__version__ = '1.2.1'

__PYCLI_PATH = path.abspath(path.join(path.dirname(os.getcwd()), '.'))
__LIBS_PATH = path.join(__PYCLI_PATH, 'libs')

OPT_DEPLOY = 'deploy'
OPT_ENCRYPT = 'encrypt'
OPT_CHANNEL = 'channel'


class ArgOpts(object):
    operate = OPT_DEPLOY

    project_path = ''
    app_module = ''
    output_path = ''

    def __init__(self):
        self.operate = sys.argv[1]

        opts, args = getopt(sys.argv[2:],
                            'hp:m:c:o:v',
                            ['help', 'project=' 'module=', 'channel=', 'output=', 'version'])
        if opts:
            for opt, arg in opts:
                if opt in ("-p", "--project"):
                    if arg:
                        self.project_path = arg

                elif opt in ("-m", "--module"):
                    if arg:
                        self.app_module = arg
                    else:
                        raise RuntimeError('[ERROR]: Usage: pycli -m <your project path> | --project="your project path"')

                elif opt in ("-c", "--channel"):
                    self.safety_flag = True

                elif opt in ("-v", "--version"):
                    print(__version__)
                    sys.exit(0)

                elif opt in ("-h", "--help"):
                    print_usage()
                    sys.exit(0)

        if len(self.project_path) <= 0:
            cwd_path = os.getcwd()
            if path.exists(path.join(cwd_path, self.app_module, 'build.gradle')):
                project_path = cwd_path

            else:
                raise RuntimeError('\n[ERROR]: 当前目录非Android工程目录，请指定编译目录！！！')
        if not self.app_module:
            self.app_module = 'app'


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

        self.fir_token = self.props.get('token')

    def __new__(cls, *args, **kwargs):
        if not hasattr(PyCliConfig, "_instance"):
            with PyCliConfig.__instance_lock:
                if not hasattr(PyCliConfig, "_instance"):
                    PyCliConfig._instance = object.__new__(cls)
        return PyCliConfig._instance


def load_config():
    return PyCliConfig()


def get_pycli_path():
    return __PYCLI_PATH


def get_libs_path():
    return __LIBS_PATH


def print_usage():
    print('Usage: python -m <app_module>')


__all__ = ['__title__', '__version__', 'OPT_DEPLOY', 'PyCliConfig', 'ArgOpts']

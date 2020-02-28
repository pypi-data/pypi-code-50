# encoding=utf8
# -*- coding: utf-8 -*-

from .config import g_config
from .env import *
from .stream import *
from .batch import *
from .pipeline import *
from .udf import *
from .base_db import *
from .converters import *
from .with_params import *
from .ipython_magic_command import *

print("""
Use one of the following commands to start using PyAlink:
 - useLocalEnv(parallelism, flinkHome=None, config=None)
 - useRemoteEnv(host, port, parallelism, flinkHome=None, localIp="localhost", config=None)
Call resetEnv() to reset environment and switch to another.
""")

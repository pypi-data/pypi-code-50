#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Project      : mi.
# @File         : __init__.py
# @Time         : 2020-03-04 14:45
# @Author       : yuanjie
# @Email        : yuanjie@xiaomi.com
# @Software     : PyCharm
# @Description  : 


import os
import re
from pathlib import Path
from .zk import Config

zk_cfg = Config.zk_cfg

dev = False if re.search('.c3_|.c4_', os.environ.get('DOCKER_JOBNAME', '')) else True
prd = Path('/home/work').exists()

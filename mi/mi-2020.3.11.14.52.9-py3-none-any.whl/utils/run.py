#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Project      : Python.
# @File         : run
# @Time         : 2020-03-11 14:15
# @Author       : yuanjie
# @Email        : yuanjie@xiaomi.com
# @Software     : PyCharm
# @Description  : 


if __name__ == '__main__':
    # import os
    # import socket
    #
    # me = socket.gethostname() == 'yuanjie-Mac.local'
    #
    # uvicorn = "uvicorn" if me else "/opt/soft/python3/bin/uvicorn"
    #
    # main_file = __file__.split('/')[-1].split('.')[0]
    #
    # # --reload测试环境
    # os.system(f"uvicorn app:app --reload --host 0.0.0.0 --port 8000")
    from zk import Config

    print(Config.zk_cfg)

#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import sys
import argparse

APP_DESC = """
X ATP API
Interface test program for X automated test platform
"""
print(APP_DESC)

if len(sys.argv) == 1:
    sys.argv.append('--help')
parser = argparse.ArgumentParser()
parser.add_argument('-p', '--port', type=int, default=80, help="X-ATP main service port number")
parser.add_argument('ip', metavar='IP', nargs='+', help="X-ATP main service ip address (127.0.0.1)")
args = parser.parse_args()
# X-ATP service ip
ip = args.ip[0]
# X-ATP service port
port = args.port

# 其他执行逻辑
print('IP地址', ip)
print('端口号', port)

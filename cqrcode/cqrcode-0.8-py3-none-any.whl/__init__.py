# coding: utf-8 
# !/usr/bin/python
"""
@File       :   __init__.py.py
@Author     :   jiaming
@Modify Time:   2020/3/8 22:46    
@Contact    :   https://blog.csdn.net/weixin_39541632
@Version    :   1.0
@Desciption :   None
"""

from cqrcode.view.GUI_welcome import hello

while True:
    x = input('请输入 s 启动...\n')
    if x == 's' or x == 'S':
        hello()

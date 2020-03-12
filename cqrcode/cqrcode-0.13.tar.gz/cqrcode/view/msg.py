# coding: utf-8 
# !/usr/bin/python
"""
@File       :   msg.py
@Author     :   jiaming
@Modify Time:   2019/12/17 15:03    
@Contact    :   https://blog.csdn.net/weixin_39541632
@Version    :   1.0
@Desciption :   提示框脚本
"""
from tkinter import messagebox


def showMsg(title='', message=''):
    messagebox.showinfo(title=title, message=message)


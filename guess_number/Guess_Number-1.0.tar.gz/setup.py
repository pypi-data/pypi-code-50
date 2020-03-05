#coding=utf-8
from distutils.core import setup

setup(
    name = 'Guess_Number',  # 对外我们模块的名字
    version = '1.0',
    description = '这是一个猜数字的游戏',
    author= 'LiFengqi',
    author_email= 'lifengqi_gx@163.com',
    py_modules = ['Guess_Number.guess_Number']   # 要发布的模块
)
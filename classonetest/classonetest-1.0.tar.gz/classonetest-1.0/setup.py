#coding=utf-8
from distutils.core import setup


setup(
    name='classonetest',     # 对外我们模块的名字
    version='1.0', # 版本号
    description='这是第一个对外发布的模块，测试哦',    #描述
    author='classone', # 作者
    author_email='819129084@qq.com',
    py_modules=['classonetest.upload01','classonetest.dump02']    # 要发布的模块
)

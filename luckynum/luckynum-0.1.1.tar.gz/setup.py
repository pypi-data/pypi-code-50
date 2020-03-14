#-*- coding:utf-8 -*-

#############################################
# File Name: setup.py
# Author: MoonKight
# Mail: 919024219@qq.com
# Created Time:  2020-3-15
#############################################


from setuptools import setup, find_packages

setup(
    name = "luckynum",
    version = "0.1.1",
    keywords = ("pip", "MoonKight"),
    description = "to get a luckynum",
    long_description = "to get a luckynum for u baby",
    license = "MIT Licence",

    author = "MoonKnight",
    author_email = "919024219@qq.com",

    packages = find_packages(),
    include_package_data = True,
    platforms = "any",
    py_modules=['luckynum'],
    install_requires = []
)
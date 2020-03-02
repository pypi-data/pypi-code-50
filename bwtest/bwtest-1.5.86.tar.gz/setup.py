#!/usr/bin/env python
#-*- coding:utf-8 -*-

#############################################
# File Name: bwsetup.py
# Author: Leon
# Mail: skyrecca@163.com
# Created Time:  2019-8-12 16:16:16
#############################################

from setuptools import setup, find_packages            #这个包没有的可以pip一下
import glob
import os

print ( find_packages('bw'),)
print("-"*50)

dirlst2 = glob.glob(r".\bw\helper\*.*")
dirfmtls2 = [ i.replace('\\','/').replace('bw/helper/','')  for i in dirlst2]

print(dirfmtls2)
dirlst = glob.glob(r".\bw\helper\*\*.*")
dirfmtls = [ i.replace('\\','/').replace('bw/helper/','')  for i in dirlst]

dirfmtls.extend(dirfmtls2)
# print(dirfmtls)
print('-'*50)

setup(
    name = "bwtest",      #这里是pip项目发布的名称
    version = "1.5.86",  #版本号，数值大的会优先被pip
#  package_dir={'':'bw'},
    packages = find_packages(),

    keywords = ["pip", "bw","financial analyze"],
    description = "A fast backtest framework",
    long_description = "only support python 3.7 windows 64bit ",
    license = "Apache 2.0",
    python_requires='>=3.7.0',
    
    # include_package_data=True,
    package_data={
        # '':'*.*',
        'bw.helper':dirfmtls,
        'bw.csdk': ['./*.dll','./*.pyd','./*.so','./*.exe'], 
        },

    exclude_package_data ={
        '':['setup.py']},

    url = "http://www.gushi.com/",     
    author = "Leon",
    author_email = "skyrecca@163.com",


    platforms = "windows",
    install_requires = ["pandas>=0.24","six","arrow"]          #这个项目需要的第三方库
)

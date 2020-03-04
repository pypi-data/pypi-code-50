#!/usr/bin/env python
# -*- coding: utf-8 -*-


from setuptools import setup, find_packages

VERSION = '0.0.2'

tests_require = []

install_requires = []

setup(name='command_line', # 模块名称
      url='https://github.com/PM-yanmao/command_line',  # 项目包的地址
      author="PM-Yanmao",  # Pypi用户名称
      author_email='pm.yanmao@gmail.com',  # Pypi用户的邮箱
      keywords=('python','command_line','pip','cmd'),
      description='A command_line module for Python to create a command line quickly',
      license='MIT',  # 开源许可证类型
      version=VERSION, 
      install_requires=install_requires,
      tests_require=tests_require,
      test_suite='runtests.runtests',
      extras_require={'test': tests_require},
      platforms="any",
      entry_points={ 'nose.plugins': [] },
      packages=find_packages(),
)

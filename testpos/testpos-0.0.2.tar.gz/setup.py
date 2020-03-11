# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

VERSION = '0.0.2'

tests_require = []

install_requires = []

setup(name='testpos', # 模块名称
      url='http://pypi.org',  # 项目包的地址
      author="leevv",  # Pypi用户名称
      author_email='lwtaurus@163.com',  # Pypi用户的邮箱
      keywords='test',
      description='Test',
      license='MIT',  # 开源许可证类型
      classifiers=[
          'Operating System :: OS Independent',
          'Topic :: Software Development',
          'Programming Language :: Python :: 3.8',
          'Programming Language :: Python :: Implementation :: PyPy'
      ],

      version=VERSION, 
      install_requires=install_requires,
      tests_require=tests_require,
      test_suite='runtests.runtests',
      extras_require={'test': tests_require},

      entry_points={ 'nose.plugins': [] },
      packages=find_packages(),
)
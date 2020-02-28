from setuptools import setup, find_packages
import codecs
import os


def read(fname):
    return codecs.open(os.path.join(os.path.dirname(__file__), fname)).read()


long_desc = """
PingAn API 
===============

xcsc_tushare stock data api

"""


setup(
    name='xcsc_tushare',
    version='1.0.0',
    description='Tushare_Xiangcai Securities version',

    # 程序的详细描述
    long_description=long_desc,
    url='https://www.xcsc.com',
    keywords='Financial Data',

    # 程序的所属分类列表
    classifiers=[
        'Development Status :: 4 - Beta',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'License :: OSI Approved :: BSD License'
    ],

    # 需要处理的包目录（包含__init__.py的文件夹）
    packages=['xcsc_tushare'],

  #安装的依赖
    install_requires=[
        'pandas>=0.16.0',
        'requests>=2.0.0',
        'lxml>=3.8.0',
        'simplejson>=3.16.0',
        'beautifulsoup4>=0.0.1'
    ],
    include_package_data=True,
)

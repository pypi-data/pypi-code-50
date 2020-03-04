# -*- coding: utf-8 -*-
"""
    Setup file for Pandas-ETL.
    Use setup.cfg to configure your project.
"""
import sys

from pkg_resources import VersionConflict, require
from setuptools import setup

try:
    require("setuptools>=38.3")
except VersionConflict:
    print("Error: version of setuptools is too old (<38.3)!")
    sys.exit(1)


if __name__ == "__main__":
    setup(name='etlpy',
      packages=['etlpy'],
      version='0.0.1',
      license='MIT',
      description='ETL Utilities using Python Pandas',
      author='Neel Puniwala',
      author_email='neelpuniwala1996@gmail.com',
      url='https://github.com/neelpuniwala/Pandas-ETL',
      download_url='https://github.com/neelpuniwala/Pandas-ETL/archive/v0.1-alpha.tar.gz',
      keywords=['Pandas','ETL','Data Engineering'],
      install_requires=['pymysql','pymssql','psycopg2','cx_Oracle','pyhive','cassandra-driver','pyarrow'])

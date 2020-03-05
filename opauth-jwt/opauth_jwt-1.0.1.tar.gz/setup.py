#!/usr/bin/env python
"""
打包命令:python setup.py sdist
推送工具:pip install twine
推送命令:twine upload dist/压缩包
"""
from setuptools import setup, find_packages
PACKAGE = "opauth_jwt"
NAME = "opauth_jwt"
DESCRIPTION = "描述"
AUTHOR = "ruoxing"
AUTHOR_EMAIL = "15085751956@163.com"
URL = f"""https://github.com/{AUTHOR}"""
VERSION = __import__(NAME).__version__
setup(
    name=PACKAGE,
    version=VERSION,
    keywords=("deppon", "ruoxing", "jwt"),
    description=DESCRIPTION,
    long_description="长长的描述",
    license="MIT Licence",
    url=URL,
    author="ruoxing",
    author_email=f"""{AUTHOR_EMAIL}""",
    packages=find_packages(),
    include_package_data=True,
    platforms="any",
    install_requires=["django", "requests", "pyjwt"]
)

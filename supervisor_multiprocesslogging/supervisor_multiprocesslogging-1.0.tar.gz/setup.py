# -*- coding: utf-8 -*-
# @Time : 2020-03-03 16:55
# @Author : xzr
# @File : setup.py
# @Software: PyCharm
# @Contact : xzregg@gmail.com
# @Desc :


from setuptools import setup, find_packages

setup(
        name="supervisor_multiprocesslogging",
        version="1.0",
        keywords=["supervisor_multiprocesslogging", "supervisor_multiprocesslogging"],
        description="",
        long_description="",
        license="MIT Licence",

        url="",
        author="xzregg",
        author_email="xzregg@gmail.com",

        packages=find_packages(),
        include_package_data=True,
        platforms="any",
        requires =['supervisor'],
        #install_requires=['supervisor'],

        scripts=[],
        entry_points={
                'console_scripts': [
                        'supervisord_multiprocesslogging = supervisor_multiprocesslogging:main',
                        'supervisord = supervisor_multiprocesslogging:main'
                ]
        }
)

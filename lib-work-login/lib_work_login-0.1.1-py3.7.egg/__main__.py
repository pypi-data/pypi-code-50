#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Main file for entry points"""

__author__ = "Justin Furuness"
__credits__ = ["Justin Furuness"]
__Lisence__ = "MIT"
__maintainer__ = "Justin Furuness"
__email__ = "jfuruness@gmail.com"
__status__ = "Development"


from .work_login import Work_Login

def main():
    Work_Login().login()

def configure():
    Work_Login().configure()

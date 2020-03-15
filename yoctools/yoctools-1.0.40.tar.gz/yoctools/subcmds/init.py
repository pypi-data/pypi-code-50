# -*- coding:utf-8 -*-
#
# Copyright (C) 2015-2020 Alibaba Group Holding Limited


from __future__ import print_function

from yoctools import *


class Init(Command):
    common = True
    helpSummary = "Initialize yoc workspace in the current directory"
    helpUsage = """
%prog
"""
    helpDescription = """
Initialize yoc workspace in the current directory.
"""
    def Execute(self, opt, args):
        conf = Configure()
        conf.save()

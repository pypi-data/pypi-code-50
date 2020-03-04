# -*- coding:utf-8 -*-
#
# Copyright (C) 2015-2020 Alibaba Group Holding Limited


from __future__ import print_function

from yoctools import *
import os


class Rename(Command):
    common = True
    helpSummary = "component rename"
    helpUsage = """
%prog [<component>...]
"""
    helpDescription = """
component rename.
"""

    def Execute(self, opt, args):
        yoc = YoC()
        if len(args) == 2:
            component = yoc.components.get(args[0])
            if component:
                if component.rename(args[1]):
                    print("component `%s` -> `%s` success." % (args[0], args[1]))
                else:
                    print("component rename fail.")
            else:
                print("component `%s` not found." % args[0])


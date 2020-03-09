# -*- coding:utf-8 -*-
#
# Copyright (C) 2015-2020 Alibaba Group Holding Limited


from __future__ import print_function

from yoctools import *


class Format(Command):
    common = True
    helpSummary = "Format component package.yaml file"
    helpUsage = """
%prog [<component>...]
"""
    helpDescription = """
Format component package.yaml file
"""

    def Execute(self, opt, args):
        yoc = YoC()

        count = len(args)
        for component in yoc.components:
            if component.name in args or count == 0:
                print("formating package: %s" % component.name)
                component.load_package()
                component.pack.save()


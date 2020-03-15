# -*- coding:utf-8 -*-
#
# Copyright (C) 2015-2020 Alibaba Group Holding Limited


from __future__ import print_function

from yoctools import *


class Search(Command):
    common = True
    helpSummary = "Search component"
    helpUsage = """
%prog <component name>
"""
    helpDescription = """
Search s projects
"""

    def _Options(self, p):
        p.add_option('-u', '--upgrade',
                     dest='upgrade', action='store_true',
                     help='upgrade component')

    def Execute(self, opt, args):
        if len(args) != 1:
            self.Usage()

        yoc = YoC()
        if opt.upgrade or yoc.occ_components == None:
            yoc.gitee_update()

        for component in yoc.occ_components:
            if component.name.find(args[0]) >= 0:
                component.show()

# -*- coding:utf-8 -*-
#
# Copyright (C) 2015-2020 Alibaba Group Holding Limited


from __future__ import print_function

from yoctools import *


class List(Command):
    common = True
    helpSummary = "List component"
    helpUsage = """
%prog [-a] [<component>...]
"""
    helpDescription = """
List all projects; pass '.' to list the project for the cwd.
"""

    def _Options(self, p):
        p.add_option('-a', '--all',
                     dest='show_all', action='store_true',
                     help='show the complete list of commands')
        p.add_option('-u', '--upgrade',
                     dest='upgrade', action='store_true',
                     help='upgrade component')

    def Execute(self, opt, args):
        yoc = YoC()
        if opt.upgrade:
            yoc.gitee_update()

        if opt.show_all:
            if not yoc.occ_components:
                yoc.gitee_update()
            # yoc.occ_update()
            yoc.occ_components.show()
        else:
            yoc.list()

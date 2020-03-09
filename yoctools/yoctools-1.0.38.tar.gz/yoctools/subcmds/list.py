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

        p.add_option('-b', '--board',
                     dest='board', action='store_true',
                     help='list all board component')

        p.add_option('-s', '--solution',
                     dest='solution', action='store_true',
                     help='list all soution component')

        p.add_option('-c', '--chip',
                     dest='chip', action='store_true',
                     help='list all chip component')

        p.add_option('-m', '--common',
                     dest='common', action='store_true',
                     help='list all common component')

    def Execute(self, opt, args):
        yoc = YoC()
        if opt.upgrade:
            yoc.gitee_update()


        if opt.show_all:
            if not yoc.occ_components:
                yoc.gitee_update()
            group = yoc.occ_components
        else:
            group = yoc.components
            for c in group:
                c.load_package()

        show = opt.board or opt.chip or opt.common or opt.solution
        for c in group:
            if show:
                if opt.board and c.type == 'board':
                    c.show()
                if opt.chip and c.type == 'chip':
                    c.show()
                if opt.common and c.type == 'common':
                    c.show()
                if opt.solution and c.type == 'solution':
                    c.show()
            else:
                c.show()

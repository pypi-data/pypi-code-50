# -*- coding:utf-8 -*-
#
# Copyright (C) 2015-2020 Alibaba Group Holding Limited


from __future__ import print_function

from yoctools import *


class Depend(Command):
    common = True
    helpSummary = "List component dependencies"
    helpUsage = """
%prog [-a] [<component>...]
"""
    helpDescription = """
List all projects; pass '.' to list the project for the cwd.
"""

    # def _Options(self, p):
    #     p.add_option('-a', '--all',
    #                  dest='show_all', action='store_true',
    #                  help='show the complete list of commands')
    #     p.add_option('-u', '--upgrade',
    #                  dest='upgrade', action='store_true',
    #                  help='upgrade component')

    def Execute(self, opt, args):
        yoc = YoC()

        count = len(args)
        for component in yoc.components:
            if component.name in args or count == 0:
                self.show(yoc, component)


    def show(self, yoc, component):
        component.load_package()
        component.show()
        depend = yoc.check_depend(component)
        if len(depend) > 0:
            print("    depends:")
            depend.show(8)
        depend_on = yoc.check_depend_on(component)
        if len(depend_on) > 0:
            print("    depends on:")
            depend_on.show(8)
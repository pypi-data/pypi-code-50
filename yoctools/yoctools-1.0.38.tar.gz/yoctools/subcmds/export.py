# -*- coding:utf-8 -*-
#
# Copyright (C) 2015-2020 Alibaba Group Holding Limited


from __future__ import print_function

from yoctools import *
import os
import shutil

class Export(Command):
    common = True
    helpSummary = "component export"
    helpUsage = """
%prog <component> [<component> <component> ...] <dest path>
"""
    helpDescription = """
component export.
"""

    def Execute(self, opt, args):
        if len(args) < 2:
            self.Usage()

        yoc = YoC()
        componentList = args[:-1]
        destPath = args[-1]

        for component in yoc.components:
            if component.name in componentList:
                component.load_package()
                depend = yoc.check_depend(component)
                for d in depend:
                    self.component_export(d, destPath)
                self.component_export(component, destPath)
        yoc.conf.save(os.path.join(destPath, '.yoc'))


    def component_export(self, component, path):
        if component.type in ['common', 'chip']:
            p = 'components'
        elif component.type == 'board':
            p = 'boards'
        elif component.type == 'solution':
            p = 'solutions'
        if p:
            dest = os.path.join(path, p, component.name)
            print("export `%s` to %s" % (component.name, dest))
            shutil.copytree(component.path, dest)

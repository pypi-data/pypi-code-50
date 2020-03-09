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
            old_name = args[0]
            new_name = args[1]
            component = yoc.components.get(old_name)
            if component:
                dep_on = yoc.check_depend_on(component)
                if component.rename(new_name):
                    for c in dep_on:
                        for v in c.pack.depends:
                            if old_name in v:
                                c.pack.depends.remove(v)
                        c.pack.depends.append({component.name: component.version})
                        c.pack.save()
                        print("component %s package.yaml is upgraded." % c.name)
                    print("component `%s` -> `%s` success." % (old_name, new_name))
                else:
                    print("component rename fail.")
            else:
                print("component `%s` not found." % old_name)


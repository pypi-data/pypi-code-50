# -*- coding:utf-8 -*-
#
# Copyright (C) 2015-2020 Alibaba Group Holding Limited


from __future__ import print_function
from yoctools import *


class Upload(Command):
    common = True
    helpSummary = "upload compoent to OCC"
    helpUsage = """
%prog [<component>...]
"""
    helpDescription = """
upload compoent to OCC
"""

    def _Options(self, p):
        p.add_option('-g', '--git',
                     dest='update_git', action='store_true',
                     help='upload code to git repo')

    def Execute(self, opt, args):
        yoc = YoC()
        count = len(args)
        if opt.update_git:
            repo = RepoGitee(yoc.conf.gitee_token)
            for component in yoc.components:
                if component.name in args or count == 0:
                    component.load_package()
                    ssh_url = repo.create_project(
                        component.name, component.json_dumps())
                    if ssh_url:
                        component.upload()

        else:
            if count == 0:
                yoc.uploadall()
            else:
                for name in args:
                    yoc.upload(name)

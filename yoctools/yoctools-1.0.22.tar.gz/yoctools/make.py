#! /bin/env python

# -*- coding: UTF-8 -*-

import os
import sys

try:
    from tools import *
    from log import logger
    from yoc import YoC
except:
    from yoctools.tools import *
    from yoctools.log import logger
    from yoctools.yoc import YoC

try:
    import SCons.Script as SCons
except:
    import scons
    for path in scons.__path__:
        sys.path.append(path)
        import SCons.Script as SCons


SCons.AddOption('--verbose', dest='verbose', default=True,
                action='store_false',
                help='verbose command line output')

class Make(object):
    def __init__(self):
        self.yoc = YoC()
        self.build_env = self.yoc.genBuildEnv()

    def library(self, name, src, **parameters):
        self.build_env.library(name, src, **parameters)

    def library_yaml(self):
        package_file = self.build_env.env.GetBuildPath('package.yaml')
        conf = yaml_load(package_file)
        if conf and 'name' in conf:
            component = self.yoc.components.get(conf['name'])
            self.build_env.build_component(component)

    def build_component(self, component):
        new_file = False
        file_name = os.path.join(component.path, 'SConscript')
        if not os.path.exists(file_name):
            file_name = genSConcript(component.path)
            new_file = True
        if os.path.isfile(file_name):
            SCons.SConscript(file_name, exports={"env": self.build_env.env.Clone()}, variant_dir='out/' + component.name, duplicate=0)
            if new_file:
                os.remove(file_name)

    def build_components(self, components=None):
        if components != None:
            # 可以编译指定的组件
            for c in components:
                component = self.yoc.components.get(c)
                if component:
                    self.build_component(component)
        else:
            # 默认编译所有需要的组件
            for component in self.build_env.solution.components:
                self.build_component(component)

    def build_image(self):
        self.build_env.build_image()


    def install(self):
        self.build_env.install()


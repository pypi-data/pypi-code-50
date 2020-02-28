#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import os
import sys
import json
import shutil

try:
    from tools import *
    from component import *
    from builder import *
    from occ import *
    from log import logger
    from solution import *
except:
    from yoctools.tools import *
    from yoctools.component import *
    from yoctools.builder import *
    from yoctools.occ import *
    from yoctools.log import logger
    from yoctools.solution import *


class YoC:
    def __init__(self):
        self.occ = None
        self.occ_components = None
        self.yoc_path = ''
        self.yoc_version_base = 'v7.2'
        self.yoc_version_id = 0

        # scanning .yoc file directory
        v = current_pwd()
        while v != '/':
            f = os.path.join(v, '.yoc')
            if os.path.exists(f):
                conf = yaml_load(f)
                if 'yoc_version' in conf:
                    self.yoc_version_base = conf['yoc_version']
                if 'commit' in conf:
                    self.yoc_version_id = int(conf['commit'])

                self.yoc_path = v
                break
            v = os.path.dirname(v)

        if self.yoc_path == '':
            self.yoc_path = current_pwd()
            v = os.path.join(self.yoc_path, '.yoc')
            write_file('yoc_version: v7.2\ncommit: 0\n', v)

        logger.info('YoC path: ' + self.yoc_path)

        self.components = ComponentGroup()

        def scan_directory(path):
            filename = os.path.join(path, 'package.yaml')
            if os.path.isfile(filename):
                pack = Component(filename)

                if pack.version == '':
                    pack.version = self.yoc_version_base + '.%d' % self.yoc_version_id

                if pack.type in ['solution']:
                    if pack.path != current_pwd():
                        return

                if not self.components.add(pack):
                    pre_component = self.components.get(pack.name)
                    logger.error('component `%s` is multiple (%s : %s)' % (pack.name, pre_component.path, pack.path))
                    exit(0)

        # scanning yoc all components
        for path in ['components', 'boards']:
            walk_path = os.path.join(self.yoc_path, path)
            for dirpath, sub_path, _ in os.walk(walk_path):
                for name in sub_path:
                    scan_directory(os.path.join(dirpath, name))
        scan_directory(current_pwd())

        self.components.calc_depend()

    def depend_update(self):
        # add lost component
        comps = []
        for _, component in self.components.items():
            comps.append(component)
        for component in comps:
            for dep in component.depends:
                print(dep)
                if not self.components.get(dep):
                    self.add_component(dep)

        self.components.calc_depend()


    def getSolution(self):
        solution = Solution()
        solution.set_solution(self.components)
        return solution


    def genBuildEnv(self):
        solution = self.getSolution()
        return Builder(solution)

    def add_component(self, name):
        self.occ_update()
        if self.components.get(name) == None:
            component = self.occ_components.get(name)
            if component:
                for dep in component.depends:
                    self.add_component(dep['name'])
                self.components.add(component)

            return component


    def remove_component(self, name):
        component = self.components.get(name)
        if component:
            if not component.depends_on:                     # 如果没有组件依赖它
                for dep in component.depends:
                    p = self.components.get(dep)
                    if p:
                        if name in p.depends_on:
                            del p.depends_on[name]
                        self.remove_component(dep)

                shutil.rmtree(component.path)
                self.components.remove(component)
                self.components.calc_depend()
                return True
            else:
                logger.info("remove fail, %s depends on:" % component.name)
                for dep in component.depends_on:
                    logger.info('  ' + dep.name)
                return False


    def save_version(self):
        pass
        # v = os.path.join(self.yoc_path, '.yoc')
        # self.yoc_version_id += 1
        # write_file('yoc_version: v7.2\ncommit: %d\n' % self.yoc_version_id, v)


    def upload(self, name):
        component = self.components.get(name)
        if component:
            if not os.path.isdir(os.path.join(component.path, '.git')):
                if self.occ == None:
                    self.occ = OCC()
                self.occ.login()
                zip_file = component.zip(self.yoc_path)
                if self.occ.upload(component.version, component.type, zip_file) == 0:
                    print("component upload success: " + component.name)
                else:
                    print("component upload fail: " + component.name)
                # self.save_version()


    def uploadall(self):
        if self.occ == None:
            self.occ = OCC()
        self.occ.login()
        for _, component in self.components.items():
            zip_file = component.zip(self.yoc_path)
            # self.occ.upload(version_inc(component.version, 1), component.type, zip_file)
            if self.occ.upload(component.version, component.type, zip_file) == 0:
                print("component upload success: " + component.name)
            else:
                print("component upload fail: " + component.name)


    def update(self):
        for _, component in self.components.items():
            component.download(self.yoc_path)
        for _, component in self.components.items():
            if component.type == 'solution':
                genSConstruct(self.components, component.path)


    def occ_update(self):
        if self.occ == None:
            self.occ = OCC()
            self.occ_components = self.occ.yocComponentList('614193542956318720')
            for _, component in self.occ_components.items():
                component.path = os.path.join(self.yoc_path, component.path)


    def list(self):
        for _, component in self.components.items():
            component.show()
            print(component.name)
            if component.depends:
                print('  ', 'depends:')
                for v in component.depends:
                    print('    -', v)
            if component.includes:
                print('  ', 'include:')
                for p in component.includes:
                    print('    -', p)
            if component.depends_on:
                print('  ', 'depends_on:')
                for p in component.depends_on:
                    print('    -', p.name)


def usage():
    print("Usage:")
    print("  yoc <command> [options]\n")
    print("Commands:")
    print("  install                     Install component.")
    print("  uninstall                   Uninstall component.")
    print("  list                        List all packages")
    print("  update                      update all packages")
    print("  upload                      update all packages")
    print("  variable                    show variable")
    print("")

    print("General Options:")
    print("  -h, --help                  Show help.")


def main():
    argc = len(sys.argv)
    if argc < 2:
        usage()
        exit(0)

    if sys.argv[1] == 'list':
        yoc = YoC()
        yoc.occ_update()
        yoc.occ_components.show()
    elif sys.argv[1] == 'lo':
        yoc = YoC()
        yoc.list()
    elif sys.argv[1] in ['install', 'download']:
        if argc >= 3:
            yoc = YoC()
            yoc.add_component(sys.argv[2])
            yoc.update()
            print("%s download Success!" % sys.argv[2])
    elif sys.argv[1] in ['uninstall', 'remove']:
        if argc >= 3:
            yoc = YoC()
            if yoc.remove_component(sys.argv[2]):
                yoc.update()
                print("%s uninstall Success!" % sys.argv[2])
    elif sys.argv[1] == 'update':
        yoc = YoC()
        yoc.update()
    elif sys.argv[1] == 'upload':
        yoc = YoC()
        if argc >= 3:
            yoc.upload(sys.argv[2])
        if argc == 2:
            yoc.uploadall()
    elif sys.argv[1] == 'test':
        yoc = YoC()
        yoc.genBuildEnv()
    elif sys.argv[1] == 'depend':
        yoc = YoC()
        yoc.depend_update()

    elif sys.argv[1] == 'sdk':
        yoc = YoC()
        solution = yoc.getSolution()
        solution.install()

    elif sys.argv[1] == 'variable':
        yoc = YoC()
        solution = yoc.getSolution()
        if argc >= 3:
            var = solution.variables.get(sys.argv[2])
            print(var)
        else:
            for k, v in solution.variables.items():
                print("%-10s = %s" % (k, v))
    elif sys.argv[1] == 'show':
        yoc = YoC()
        solution = yoc.getSolution()
        solution.show()
        for c in solution.components:
            c.show()
            c.info(4)


if __name__ == "__main__":
    yoc = YoC()
    solution = yoc.getSolution()
    solution.show()
    for c in solution.components:
        c.show()
        c.info(4)

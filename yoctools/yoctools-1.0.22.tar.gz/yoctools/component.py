# -*- coding: UTF-8 -*-

import os
import sys
import json
# import git
import zipfile
import re
import shutil


try:
    from tools import *
    from log import logger
    from package import *
except:
    from yoctools.tools import *
    from yoctools.log import logger
    from yoctools.package import *


class Component:
    def __init__(self, filename=''):
        self.name = ''
        self.path =  os.path.dirname(filename)
        self.type = 'common'
        self.version = 'master'
        self.depends = []
        self.description = ''
        self.version = ''
        self.license = ''
        self.historyVersion = {}
        self.updated = ''
        self.repo_url = ''
        self.repo = None
        self.yoc_version = ''
        self.source_file = []
        self.defconfig = {}
        self.build_config = None
        self.hw_info = None

        self.depends_on = []  # 该组件被哪个组件依赖

        if self.path:
            self.load_package()


    def loader_json(self, js):
        self.js = js
        self.name = js['name']
        self.depends = js['depends']
        self.description = js['description']
        self.version = js['versions']
        self.license = js['license']
        self.repo_url = js['aboutURL']
        self.updated = js['updated']

        for ver in js['historyVersion']:
            self.historyVersion[ver['version']] = ver['url']

        if self.type == "common":
            self.path = 'components/' + self.name
        elif self.type == 'chip':
            self.path = 'chip/' + self.name
        elif self.type == 'board':
            self.path = 'boards/' + self.name
        elif self.type == 'solution':
            self.path = 'solutions/' + self.name
        else:
            self.path = 'components/' + self.name


    def download(self, yoc_path=''):
        if self.repo_url:
            if (not os.path.exists(self.path)) or (not os.path.isdir(os.path.join(self.path, '.git'))):
                print('git clone %s (%s)...' % (self.name, self.version))
                # self.repo = git.Repo.init(self.path)
                # origin = self.repo.create_remote(name='origin', url=http2git(self.repo_url))
                # origin.fetch()

                # self.repo.create_head(self.version, origin.refs.master)  # create local branch "master" from remote "master"
                # self.repo.heads.master.set_tracking_branch(origin.refs.master)  # set local "master" to track remote "master
                # self.repo.heads.master.checkout()  # checkout local "master" to working tree
        elif self.version in self.historyVersion.keys():
            zip_url = self.historyVersion[self.version]
            filename = http_get(zip_url, os.path.join(yoc_path, '.cache'))
            zipf = zipfile.ZipFile(filename)
            if self.path != '.':
                zipf.extractall('components/')
            else:
                zipf.extractall('.')


    def zip(self, path):
        zipName = os.path.join(path, '.cache', self.name + '-' + self.version + '.zip')
        if os.path.exists(zipName):
            os.remove(zipName)
        zip_path(self.path, zipName)

        return zipName


    def show(self, indent=0):
        if os.path.isdir(self.path):
            status = '*'
        else:
            status = ' '

        s1 = self.name + ' (' + self.version + ')'
        size = len(s1)

        text1, text2 = string_strip(self.description, 80)
        print("%s%s %s %s - %s" % (' '*indent, status, s1, ' ' * (40 - size), text1))
        while text2:
            text1, text2 = string_strip(text2, 80)
            print(' ' * 46 + text1)


    def info(self, indent=0):
        for f in self.source_file:
            print('%s%s' % (' '*indent, f))


    def load_package(self):
        filename = os.path.join(self.path, 'package.yaml')

        pack = Package(filename)

        if os.path.basename(self.path) != pack.name:
            logger.warning("component `%s`, but the directory is `%s`." % (pack.name, filename))

        if self.repo:
            self.version = self.repo.active_branch.name

        self.name = pack.name
        self.type = pack.type
        self.description = pack.description
        self.yoc_version = pack.yoc_version
        self.source_file = pack.source_file
        self.build_config = pack.build_config
        self.defconfig = pack.defconfig
        self.installs = pack.install
        self.hw_info = pack.hw_info

        self.depends = []
        for d in pack.depends:
            if type(d) == dict:
                for k, _ in d.items():
                    self.depends.append(k)
            else:
                self.depends.append(d)

    def variable_convert(self, varList):
        # include
        incs = []
        for inc in self.build_config.include:
            inc = varList.convert(inc)
            if inc != None:
                path = os.path.join(self.path, inc)
                if not (os.path.isdir(path) and os.path.exists(path)):
                    logger.warning('%s is not exists or not directory.' % path)

            if path not in incs:
                incs.append(path)
        self.build_config.include = incs

        # libpath
        libpaths = []
        for var in self.build_config.libpath:
            var = varList.convert(var)
            if var != None:
                path = os.path.join(self.path, var)
                if not (os.path.isdir(path) and os.path.exists(path)):
                    logger.warning('%s is not exists or not directory.' % path)

            if path not in libpaths:
                libpaths.append(path)
        self.build_config.libpath = libpaths

        # libs
        libs = []
        for lib in self.build_config.libs:
            lib = varList.convert(lib)
            if lib != None and lib not in libs:
                libs.append(lib)
        self.build_config.libs = libs

        # sources
        sources = []
        for s in self.source_file:
            fn = varList.convert(s)
            if fn != None:
                sources.append(fn)
        self.source_file = sources

        if self.hw_info.ld_script:
            ld_script = varList.convert(self.hw_info.ld_script)
            if ld_script:
                self.hw_info.ld_script = os.path.join(self.path, ld_script)

        # install
        installs = []
        for ins in self.installs:
            srcs = []
            for src in ins['source']:
                srcs.append(varList.convert(src))
            installs.append({
                'dest': varList.convert(ins['dest']),
                'source': srcs,
            })
        self.installs = installs

    def getDependList(self, components):
        deps = []
        def ccc(comp):
            if comp not in deps and comp != self:
                deps.append(comp)
            for dep in comp.depends:
                c = components.get(dep)
                if c:
                    ccc(c)

        ccc(self)
        return deps

    def install(self, dest):
        for ins in self.installs:
            path = os.path.join(dest, ins['dest'])
            if not os.path.exists(path):
                os.makedirs(path)

            for src in ins['source']:
                src = os.path.join(self.path, src)
                for s in glob.iglob(src):
                    fn = os.path.basename(s)
                    ds = os.path.join(path, fn)
                    # print(ds, s)
                    shutil.copy2(s, ds)


class ComponentGroup:
    def __init__(self):
        self.components = {}

    def add(self, component):
        not_exists = component.name not in self.components
        if not_exists:
            self.components[component.name] = component
        return not_exists


    def size(self):
        return len(self.components)


    def get(self, name):
        if name in self.components:
            return self.components[name]

    def remove(self, name):
        if name in self.components:
            del self.components[name]

    def show(self):
        for _, component in self.components.items():
            component.show()

    def items(self):
        return self.components.items()

    def download(self, name):
        if name in self.components:
            component = self.components[name]
            if component:
                component.download()


    def calc_depend(self):
        for _, component in self.components.items():
            component.depends_on = []
        for _, component in self.components.items():
            for dep in component.depends:
                p = self.get(dep)
                if p:
                    p.depends_on.append(component)


def string_strip(text, size):
    L = 0
    R = ''
    i = 0
    for c in text:
        if c >= '\u4E00' and c <= '\u9FA5':
            # print(c)
            L += 2
        else:
            # print('  ', c)
            L += 1
        R += c
        i += 1
        if L >= size:
            break
    return R, text[i:]


def version_compr(a, b):
    if b[:2] == '>=':
        return a >= b[2:]
    if b[:1] == '>':
        return a > b[1:]
    return a == b


if __name__ == "__main__":
    c = Component('../solutions/helloworld')
    # c = Component('../components/aos')
    # c.show()
    for k, v in c.__dict__.items():
        if not v:
            continue
        if k in ['build_config']:
            print(k)
            for kk, vv, in v.__dict__.items():
                print("  ", kk, ":", vv)
        elif k in ['defconfig']:
            print(k)
            for k1, v1 in v.items():
                print("  ", k1, ":", v1)

        else:
            print(k, str(v))
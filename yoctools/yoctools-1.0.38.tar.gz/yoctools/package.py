# -*- coding:utf-8 -*-
#
# Copyright (C) 2015-2020 Alibaba Group Holding Limited


from __future__ import print_function
import json
import shutil
import glob

from .tools import *
from .log import logger


desc_width = 50


class HardwareInfo:
    def __init__(self, dic):
        self.cpu_id = ''
        self.vendor_name = ''
        self.cpu_name = ''
        self.arch_name = ''
        self.chip_name = ''
        self.board_name = ''
        self.ld_script = ''
        self.flash_program = ''

        self.cpu_list = {}

        for k, v in dic.items():
            if k in ['cpu_id', 'cpu_name', 'arch_name', 'chip_name', 'vendor_name', 'board_name', 'ld_script', 'flash_program'] and v:
                self.__dict__[k] = v
            else:
                if type(v) == dict:
                    self.cpu_list[k] = v

    def __str__(self):
        text = ''
        for k, v in self.__dict__.items():
            if text:
                text += ', '
            text += k + ': ' + str(v)
        return text

    def merge(self, info, force=False):
        for k, v in self.__dict__.items():
            if force and info.__dict__[k]:
                self.__dict__[k] = info.__dict__[k]
            elif not v and info.__dict__[k]:
                self.__dict__[k] = info.__dict__[k]

    def out(self):
        text = ''

        if len(self.cpu_list) > 0:
            for name, cpu in self.cpu_list.items():
                if len(cpu) > 0:
                    text += '  %s:\n' % name
                    for k, v in cpu.items():
                        text += '    {}: {}\n'.format(k, v)
        else:
            for k in ['cpu_id', 'arch_name', 'vendor_name', 'chip_name', 'cpu_name', 'board_name', 'ld_script']:
                if self.__dict__[k]:
                    text += '  {}: {}\n'.format(k, self.__dict__[k])

        if self.flash_program:
            text += '  flash_program: {}\n'.format(self.flash_program)

        if text:
            text = 'hw_info:\n' + text

        return text


class build_config:
    def __init__(self, dic):
        self.include = []
        self.internal_include = []
        self.libs = []
        self.libpath = []
        self.cflag = ''
        self.cxxflag = ''
        self.asmflag = ''
        self.ldflag = ''
        self.define = []

        for k, v in dic.items():
            if v:
                self.__dict__[k] = v

    def out(self):
        text = ''
        for k in ['cflag', 'cxxflag', 'asmflag', 'ldflag']:
            value = self.__dict__[k]
            if value:
                if len(value) < 60:
                    text += "  %s: '%s'\n" % (k, value)
                else:
                    text += '  %s: >\n' % k
                    vv = ''
                    for v in value.split(' '):
                        vv += v + ' '
                        if len(vv) > 60:
                            text += '    ' + vv.strip() + '\n'
                            vv = ''
                    if vv:
                        text += '    ' + vv.strip() + '\n'

        if len(self.define) > 0:
            define_text = ''
            for k in self.define:
                if type(k) == dict:
                    for a, b in k.items():
                        define_text += '    - {}: {}\n'.format(a, b)
                        break
                elif k:
                    define_text += '    - {}\n'.format(k)
            if define_text:
                text += '  define:\n' + define_text

        for k in ['include', 'internal_include', 'libs', 'libpath']:
            if len(self.__dict__[k]) > 0:
                value_text = ''
                for value in self.__dict__[k]:
                    if value:
                        value_text += '    - %s\n' % value
                if value_text:
                    text += '  %s:\n%s' % (k, value_text)

        if text:
            text = 'build_config:\n' + text

        return text


class Package(object):
    def __init__(self, filename):
        self.filename = filename
        self.name = ''
        self.description = ''
        self.type = ''
        self.tag = ''
        self.yoc_version = ''
        self.version = ''
        self.keywords = {}
        self.author = {}
        self.license = ''
        self.homepage = ''
        self.yoc_version = ''
        self.depends = {}
        self.build_config = build_config({})
        self.defconfig = {}
        self.source_file = []
        self.install = []
        self.export = []
        self.hw_info = HardwareInfo({})

        self.load(filename)

    def load(self, filename):
        conf = yaml_load(filename)

        for k, v in conf.items():
            if v:
                if k == 'build_config':
                    v = build_config(v)
                if k in ['board', 'chip', 'solution', 'hw_info']:
                    self.__dict__['hw_info'] = HardwareInfo(v)
                elif k == 'lib':
                    self.__dict__['libs'] = v
                elif k == 'def_config':
                    self.__dict__['defconfig'] = v
                else:
                    self.__dict__[k] = v

        if self.type in ['board', 'chip', 'solution']:
            if self.type not in conf and 'hw_info' not in conf:
                logger.error('%s component must set `%s` field' %
                             (filename, self.type))
                exit(-1)

        if not self.name:
            logger.error('%s `name` cannot be empty!' % filename)
            exit(-1)

        if self.type not in ['solution', 'common', 'board', 'chip']:
            logger.error(
                '%s `type` must be "solution" or "common" or "board" or "chip".' % filename)
            exit(-1)


    def show(self):
        for k, v in self.__dict__.items():
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

    def save(self):
        text = '''
## 第一部分： 基础信息
{name}{version}{description}{type}
{tag}{keywords}{homepage}{yoc_version}{author}{license}
## 第二部分：依赖信息
#           指定该组件依赖的组件及版本，版本支持条件比较，支持：>=v1.0, >v1.0, ==v1.0, <=v1.0, <v1.0, v1.0
#           未指定条件时，默认为 ==，如 v1.0 与 ==v1.0
# depends:                                 # <可选项> 该组件依赖其他的组件，合理的依赖才能保证组件能编译、使用
#   - minilibc: v7.2.0
#   - aos: >=v7.2.0
{depends}
## 第三部分：板级信息
# hw_info:                                 # 对 solution、board、chip 三个字段的改进，统称为 hw_info 字段
#   cpu_id: cpu0
#   cpu_name: CK804EF
#   vendor_name: t-head
#   chip_name: chip_pangu                  # <可选项> 指定芯片组件名,未设置时，使用depends中 chip 第一个组件
#   board_name: pangu_cpu0                 # <可选项> 指定开发板组件名，未设置时，使用depends中 board 第一个组件
#   ld_script: configs/gcc_eflash.ld       # <可选项> 连接时使用 LD 脚本，当选把未设置时，使用对应的 board 的 LD 脚本
#   flash_program: bin/flash_program.elf   # <可选项> 芯片全局烧写程序
#   cpu0:
#     cpu_name: CK804EF                    # <必选项> 该芯片使用的 CPU 型号
#     ld_script: configs/gcc_eflash.ld     # <必选项> 连接时使用 LD 脚本
#     flash_program: bin/flash_program.elf # <可选项> 该CPU对应烧写程序，未指定时使用全局烧写程序
#   cpu1:
#     cpu_name: CK804EF                    # <必选项> 该芯片使用的 CPU 型号
#     ld_script: configs/gcc_eflash.ld     # <可选项> 连接时使用 LD 脚本
#     flash_program: bin/flash_program.elf # <可选项> 该CPU对应烧写程序，未指定时使用全局烧写程序

## solution component
# hw_info:
#   cpu_id: cpu0
#   board_name: pangu_cpu0
#   cpu_name: CK805EF
#   vendor_name: csky
#   chip_name: 'chip_pangu'
#   ld_script: configs/gcc_eflash.ld.S

## board component
# hw_info:
#   chip_name: chip_pangu
#   ld_script: configs/gcc_eflash.ld

## chip component (单处理器)
# hw_info:
#   cpu_name: CK804EF
#   ld_script: configs/gcc_eflash.ld
#   flash_program: bin/flash_program.elf

## chip component(多处理器)
# hw_info:
#   cpu0:
#     cpu_name: CK804EF                    # <必选项> 该芯片使用的 CPU 型号
#     ld_script: configs/gcc_eflash.ld     # <必选项> 连接时使用 LD 脚本
#     flash_program: bin/flash_program.elf # <可选项> 该CPU对应烧写程序，未指定时使用全局烧写程序
#   cpu1:
#     cpu_name: CK804EF                    # <必选项> 该芯片使用的 CPU 型号
#     ld_script: configs/gcc_eflash.ld     # <必选项> 连接时使用 LD 脚本
#     flash_program: bin/flash_program.elf # <可选项> 该CPU对应烧写程序，未指定时使用全局烧写程序
#   flash_program: bin/flash_program.elf   # <可选项> 芯片全局烧写程序
{hw_info}
## 第四部分：编译连接信息
# build_config:                            # <可选项> 编译配置项
#   include:                               # <可选项> 编译时，影响编译器的-I 参数 ,全局有效
#     - src                                #        include 只能是该软件包下的目录，不能使用外部目录
#   internal_include:                      # <可选项> 编译时，影响编译器的-I 参数 ,组件内有效
#     - include
#   cflag: ''                              # <可选项> C 编译器所需要要的编译参数
#   cxxflag: ''                            # <可选项> CXX 编译器所需要要的编译参数
#   asmflag: ''                            # <可选项> 汇编器所需要要参数
#   define:                                # <可选项> 宏定义, 增加编译器的-D 选项,如：
#     XXX: 1                               #   -DXXX=1
#     AAA: 1                               #   -DAAA
#     STR: "abc"                           #   -DSTR=\"abc\"
#   libs:                                  # 该组件中支持的二进制静态库,如：libxxx.a, libyyy.a
#     - xxx                                #   -lxxx
#     - yyy                                #   -lyyy
#   libpath:                               # 指定静态库所在的路径（相对于该组件路径）
#     - libs                               #   -Llibs
{build_config}
# source_file:                             # <可选项> 指定参与编译的源代码文件，支持通配符，采用相对路径
#   - src/*.c                              # 例：组件 src 目录下所有的扩展名为 c 的源代码文件
{source_file}
## 第五部分：配置信息
# def_config:                              # 组件的可配置项
#   CONFIG_DEBUG: y
#   CONFIG_PARAM_NOT_CHECK: y
#   CONFIG_CLI: y
{def_config}
## 第六部分：安装信息
# install:
#   - dest: include/                       # 安装的目的路径 dest是相当路径，通常是相对于YoC SDK 安装目录
#     source:                              # 安装源列表
#      - src/*.h                           # 支持通配符，相对路径
{install}
## 第七部分：导出部分
{export}'''

        text = text.format(
            name=self.text_out('name', self.name,
                               '# <必选项> 包名称 （符合C语言变量命名规则），长度少于等于64字节'),
            version=self.text_out('version', self.version),
            description=self.text_out(
                'description', self.description, '# <必选项> 建议至少20字以上'),
            tag=self.text_out('tag', self.tag, "# <可选项> 组件分类，缺省值： ''"),
            yoc_version=self.text_out('yoc_version', self.yoc_version),
            keywords=self.keywords_out(),
            author=self.author_out(),
            license=self.text_out(
                'license', self.license, '# <可选项> 源代码的许可证，要确保所有代码、文件的许可证不冲突。如：MIT，Apache license v2.0，BSD'),
            homepage=self.text_out('homepage', self.homepage),
            type=self.text_out(
                'type', self.type, '# <可选项> 组件类型，为：solution, chip, board, common，缺省值 common'),
            depends=self.depends_out(),
            source_file=self.fsource_file_out(),
            install=self.install_out('install', self.install),
            export=self.install_out('export', self.export),
            hw_info=self.hw_info.out(),
            build_config=self.build_config.out(),
            def_config=self.def_config_out()
        )
        # print(text)
        # return
        try:
            with open(self.filename, 'w') as f:
                f.write(text)
            return True
        except:
            print("Generate %s file failed." % self.filename)

    def text_out(self, k, v, desc=''):
        k_len = len(k)
        if type(v) != str:
            v = str(v)
        v_len = string_len(v)
        if desc:
            desc = ' ' * (desc_width - k_len - v_len - 1) + desc
        if v:
            return '{}: {} {}'.format(k, v, desc).strip() + '\n'
        return ''

    def author_out(self):
        text = ''
        if self.author:
            if type(self.author) == str:
                text = self.text_out('author', self.author, '# <可选项> 原作者信息')
            else:
                text = 'author:' + ' ' * (desc_width - 5) + '# <可选项> 原作者信息\n'
                for k, v in self.author.items():
                    text += '  {}: {}\n'.format(k, v)


        return text

    def dict_out(self, k, v):
        text = ''
        if len(v) > 0:
            text = '%s:\n' % k
            for s in v:
                text += '  - {}\n'.format(s)
        return text

    def keywords_out(self):
        text = ''
        if len(self.keywords) > 0:
            text = 'keywords:' + ' ' * \
                (desc_width - 7) + '# <可选项> 标签，会影响到组件被搜索的效果，合理的标签很重要\n'
        for k in self.keywords:
            text += '  - %s\n' % k

        return text

    def depends_out(self):
        text = ''
        if len(self.depends) > 0:
            text = 'depends:\n'
            for d in self.depends:
                for k, v in d.items():
                    text += '  - {}: {}\n'.format(k, v)
                    break

        return text

    def fsource_file_out(self):
        text = ""
        if len(self.source_file) > 0:
            text = 'source_file:\n'
            for src in self.source_file:
                text += '  - "%s"\n' % src

        return text

    def install_out(self, key, item):
        text = ''
        if len(item) > 0:
            text = '%s:\n' % key
            for ins in item:
                text += '  - dest: "%s"\n    source:\n' % ins['dest']
                for src in ins['source']:
                    text += '      - "%s"\n' % src

        return text

    def def_config_out(self):
        text = ''
        if len(self.defconfig) > 0:
            text = 'def_config:\n'
            for k, v in self.defconfig.items():
                text += '  {}: {}\n'.format(k, v)

        return text

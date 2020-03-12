#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import configparser
from common.logger import log


def get_ini_sections(ini_file):
    """获取指定文件下的所有section"""
    cf = configparser.ConfigParser()
    if os.path.exists(ini_file):
        cf.read(ini_file, encoding='utf-8')
        return cf.sections()
    else:
        log.error('function:get_ini_sections wrong! file:%s' % ini_file)
        return False


def get_ini_options(ini_file, section):
    """获取指定section下的所有option"""
    cf = configparser.ConfigParser()
    if os.path.exists(ini_file):
        cf.read(ini_file, encoding='utf-8')
        secs = cf.sections()
        if section.lower() in secs:
            return cf.options('%s' % section.lower())
        else:
            log.warn('function:get_ini_options wrong!maybe section:%s not in this file %s.' % (section, ini_file))
            return False
    else:
        log.warn('function:get_ini_options wrong!maybe inifile:%s not exists.' % ini_file)
        return False


def get_ini_option_val(ini_file, section, option):
    """获取执行section下option的值"""
    cf = configparser.ConfigParser()
    if os.path.exists(ini_file):
        cf.read(ini_file, encoding='utf-8')
        secs = cf.sections()
        if section.lower() in secs:
            opts = cf.options(section.lower())
            if option.lower() in opts:
                return cf.get(section, option.lower())
            else:
                log.warn('function:get_ini_option_val wrong!maybe option:%s not in this file.' % option)
                return False
        else:
            log.warn('function:get_ini_option_val wrong!maybe section:%s not in this file.' % section)
            return False
    else:
        log.warn('function:get_ini_option_val wrong!maybe inifile:%s not exists.' % ini_file)
        return False


def set_ini_option_val(ini_file, section, option, value):
    """修改某个option的val"""
    cf = configparser.ConfigParser()
    if os.path.exists(ini_file):
        cf.read(ini_file, encoding='utf-8')
        secs = cf.sections()
        if section in secs:
            opts = cf.options('%s' % section)
            if option in opts:
                content = open(ini_file, 'w')
                cf.set('%s' % section, '%s' % option, value)
                cf.write(content)
                content.close()
                return True
            else:
                log.warn('function:set_ini_option_val wrong!maybe option:%s not in this file.' % option)
                return False
        else:
            log.warn('function:set_ini_option_val wrong!maybe section:%s not in this file.' % section)
            return False
    else:
        log.warn('function:set_ini_option_val wrong!maybe inifile:%s not exists.' % ini_file)
        return False


if __name__ == '__main__':
    from configobj import ConfigObj

    path = r'D:\360_work\tools_study\Py+Selenium\skylar_auto_test\case_logReport\report_clientlog.ini'
    co = ConfigObj(path)
    log.info("co['dishes_exam']")

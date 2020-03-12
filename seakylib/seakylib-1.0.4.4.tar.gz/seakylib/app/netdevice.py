#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Seaky
# @Date:   2019/8/20 10:15

from ..func.base import MyClass, func_done
from ..func.mrun import MrunArgParse
from ..func.parser import ArgParseClass
from ..probe.miko.connect import BaseDevice
from ..probe.snmp import Snmp


class NetDeviceClass(MyClass):
    def __init__(self, ip=None, *args, **kwargs):
        '''
        :param ip:
        :param miko_param:
        :param snmp_param:
        :param args:
        :param kwargs:
            func_auto_param:  补齐miko_param/snmp_param参数
        '''
        MyClass.__init__(self, *args, **kwargs)
        self.ip = ip
        self.init_conn()

    def _complete_param(self):
        '''
        在初始化前，修改某些参数
        :return:
        '''
        return True, func_done()

    def init_conn(self):
        is_ok, result = self._complete_param()
        assert is_ok, result
        self.miko_param = self.kwargs.get('miko_param')
        self.snmp_param = self.kwargs.get('snmp_param')
        self.snmp_timeout = self.kwargs.get('snmp_timeout', 10)
        self.cli_timeout = self.kwargs.get('cli_timeout', 10)
        if isinstance(self.miko_param, dict):
            if self.ip:
                self.miko_param.update({'ip': self.ip})
            self.kwargs.update(self.miko_param)
            if self.kwargs.get('log'):
                self.kwargs['log'] = self.log
            self.cli = BaseDevice(timeout=self.cli_timeout, **self.kwargs)
            if not self.ip:
                self.ip = self.cli.ip
        if isinstance(self.snmp_param, dict):
            if self.ip:
                self.snmp_param.update({'ip': self.ip})
            self.kwargs.update(self.snmp_param)
            if self.kwargs.get('log'):
                self.kwargs['log'] = self.log
            self.snmp = Snmp(timeout=self.snmp_timeout, **self.kwargs)
            if not self.ip:
                self.ip = self.snmp.ip
        return True, func_done()

    def do(self):
        funcs = {'comware': self.do_comware,
                 'vrp': self.do_vrp,
                 'ios': self.do_ios,
                 'iosxe': self.do_iosxe,
                 'iosxr': self.do_iosxr,
                 'nxos': self.do_nxos,
                 'dnos': self.do_dnos,
                 'ftos': self.do_ftos,
                 'powerconnect': self.do_powerconnect,
                 'ibmnos': self.do_ibmnos,
                 'ruijie': self.do_ruijie,
                 'junos': self.do_junos,
                 }
        return funcs[self.cli.os]()

    def do_comware(self):
        return False, 'no code.'

    def do_vrp(self):
        return False, 'no code.'

    def do_ios(self):
        return False, 'no code.'

    def do_iosxe(self):
        return False, 'no code.'

    def do_iosxr(self):
        return False, 'no code.'

    def do_nxos(self):
        return False, 'no code.'

    def do_dnos(self):
        return False, 'no code.'

    def do_ftos(self):
        return False, 'no code.'

    def do_ibmnos(self):
        return False, 'no code.'

    def do_powerconnect(self):
        return False, 'no code.'

    def do_ruijie(self):
        return False, 'no code.'

    def do_junos(self):
        # {'os': 'junos', 'ip': '95.3-1.124.252'}
        return False, 'no code.'


class NeteaseDeviceClass(NetDeviceClass):
    def __init__(self, *args, **kwargs):
        NetDeviceClass.__init__(self, *args, **kwargs)


class NetDeviceArgParse(ArgParseClass):
    def __init__(self, *args, **kwargs):
        ArgParseClass.__init__(self, *args, **kwargs)
        self.add_base()

    def add_device(self, group='Single Device'):
        self.add('--ip', required=True, help='目标IP', group=group)
        self.add('--os', default='', help='目标系统', group=group)
        self.add('--snmp_timeout', default=10, type=int, help='snmp超时, 10s', group=group)
        self.add('--cli_timeout', default=10, type=int, help='cli超时, 10s', group=group)


class MultiNetDeviceArgParse(MrunArgParse):
    def __init__(self, *args, **kwargs):
        MrunArgParse.__init__(self, *args, **kwargs)

    def add_multi_device(self, group='Multi Device'):
        self.add('--limit', type=int, default=100000, help='任务限制', group=group)
        self.add('--ips', default='', help='指定ip组', group=group)
        self.add('--os', default='', help='指定os', group=group)

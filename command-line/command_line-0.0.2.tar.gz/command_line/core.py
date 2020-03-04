#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time :2020/3/4 13:42
# @Author : Yanmao
# @File : command.py
# @desc : 命令行

class Cmd(object):
    def __init__(self, cmd_dict, tip='>>', args=False):
        self.cmd_dict = cmd_dict
        self.args = args
        self.tip = tip
        self.check()

    def get(self):
        '''
        Get a command from user
        '''
        self.command = input(self.tip)

    def check(self):
        '''
        Check the args
        '''
        if not isinstance(self.cmd_dict, dict):
            raise TypeError('cmd_dict must be dict')
        for name, func in self.cmd_dict.items():
            if not isinstance(name, str):
                raise TypeError('command name must be str')
        if not isinstance(self.tip, str):
            raise TypeError('tip must be str')
        if not isinstance(self.args, bool):
            raise TypeError('args must be bool')

    def run(self):
        '''
        Run command
        '''
        if self.command is None:
            raise TypeError('you did not have any command')
        right_list = list()
        right_num = 0
        if not self.args:
            self.cmd_dict[self.command]()
        else:
            for command, func in self.cmd_dict.items():
                if command in self.command and (
                        '2' + self.command).strip(command)[0] == ' ' or '2':
                    func(
                        self.get_arg(command), self.get_text)
                    break
            else:
                for command in right_list:
                    if self.command.strip(command)[0] == ' ' or '':
                        self.cmd_dict[command](
                            self.get_arg(
                                right_list,
                                right_list.index(command)))
                        break

    def get_arg(self, indict_command):
        '''
        Get args
        '''
        no_command = self.command.strip(indict_command)
        no_command = no_command[1:len(no_command)]
        try:
            arg = no_command[:no_command.index(' ')]
        except ValueError as e:
            arg = None
        try:
            text = no_command[no_command.index(' ') + 1:]
        except ValueError as e:
            text = None
        self.__text = text
        return arg

    def get_text(self):
        '''
        Get text
        '''
        return self.__text

    def add(self, command, func):
        '''
        Add a new command
        '''
        self.cmd_dict[command] = func

    def del_command(self, command):
        '''
        Del a command
        '''
        del self.cmd_dict[command]

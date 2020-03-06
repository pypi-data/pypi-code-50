# -*- coding: UTF-8 -*-

import os


class Properties:
    """
    读取Properties 文件类
    """

    def __init__(self, file_name):
        with open(file_name, 'r', encoding='utf-8') as pro_file:
            for line in pro_file:
                if line.find('=') > 0:
                    array = line.replace('\n', '').split('=')
                    self.__dict__[array[0].strip()] = array[1].strip()

    def dict(self):
        return self.__dict__


def test_properties():
    p = Properties(os.path.join(os.environ['HOME'], '.pycli'))
    print(p.dict())

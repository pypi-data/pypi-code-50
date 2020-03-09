#!/usr/bin/env python
# -*- coding:utf-8 _*-  
"""
@license : Copyright(C), WAYZ
@author  : Bruce Liu
@time    : 2020/2/5 17:00
@contact : bruce.liu@wayz.ai
"""
from unittest import TestCase

from cad.aes_util import AESUtil


class TestAESUtil(TestCase):
    aes_util = AESUtil('123')

    def test_1(self):
        data = {
            'al': 123,
            'sk': "12dasfw4r"
        }

        en = self.aes_util.encrypt(data)
        print(en)
        de = self.aes_util.decrypt(en)
        print(de)

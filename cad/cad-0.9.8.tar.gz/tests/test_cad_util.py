#!/usr/bin/env python
# -*- coding:utf-8 _*-  
"""
@license : Copyright(C), WAYZ
@author  : Bruce Liu
@time    : 2020/2/4 10:39
@contact : bruce.liu@wayz.ai
"""
from cad.cad_util import CadUtil
from unittest import TestCase

ak_list = [
    '958c6d6b8ee85d9e',
    '51b8125330a72b59',
]


class TestCadUtil(TestCase):
    def test_get_ak(self):
        """

        :return:
        """
        client = CadUtil()
        for ak in ak_list:
            data = client.get(ak)
            self.assertIsInstance(data, dict)
            print(data)

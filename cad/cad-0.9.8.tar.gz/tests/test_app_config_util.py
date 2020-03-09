#!/usr/bin/env python
# -*- coding:utf-8 _*-  
"""
@license : Copyright(C), WAYZ
@author  : Bruce Liu
@time    : 2020/1/22 16:25
@contact : bruce.liu@wayz.ai
"""
from unittest import TestCase

from cad.app_config_util import AppConfigUtil

ak = '958c6d6b8ee85d9e'
sk = 'e201737ee515c7b8'


class TestAppConfigUtil(TestCase):
    def test_get_dict_success(self):
        """

        :return:
        """
        instance = AppConfigUtil(2)
        res = instance.check(ak, sk)
        self.assertEqual(res, True)
        res = instance.check(ak, sk, auth_code='234')
        self.assertEqual(res, True)
        res = instance.check(ak, '123')
        self.assertEqual(res, False)
        res = instance.check(ak, None)
        self.assertEqual(res, True)

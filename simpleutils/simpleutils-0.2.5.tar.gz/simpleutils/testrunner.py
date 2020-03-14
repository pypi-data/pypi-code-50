# -*- coding: utf-8 -*-
"""
Created on 2017-5-7

@author: cheng.li
"""

import sys
import unittest
from typing import List
from typing import Type
from simpleutils.logger import CustomLogger


class TestRunner:
    """
    simple test runner wrapper for python unit tests
    """

    def __init__(self,
                 test_cases: List[Type[unittest.TestCase]],
                 logger: CustomLogger):
        """
        Convenient unittests runner for unittests
        :param test_cases: List[Type[unittest.TestCase]]
        :param logger: CustomLogger
        """
        self.suite = unittest.TestSuite()
        self.logger = logger
        for case in test_cases:
            tests = unittest.TestLoader().loadTestsFromTestCase(case)
            self.suite.addTests(tests)

    def run(self):
        self.logger.info('Python ' + sys.version)
        res = unittest.TextTestRunner(verbosity=3).run(self.suite)
        if len(res.errors) >= 1 or len(res.failures) >= 1:
            sys.exit(-1)
        else:
            sys.exit(0)

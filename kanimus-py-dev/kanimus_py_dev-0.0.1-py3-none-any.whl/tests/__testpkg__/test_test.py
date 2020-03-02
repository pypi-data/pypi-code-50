import unittest
from hamcrest import *
from __testpkg__ import test as test_module

class test(unittest.TestCase):
    def test_if_none_then_return_test_string(self):
        actual = test_module.test()
        expected = 'Test package.'

        assert_that(actual, is_(equal_to(expected)), reason='No empty hello with None name.')

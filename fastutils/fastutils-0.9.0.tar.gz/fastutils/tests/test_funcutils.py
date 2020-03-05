# -*- coding: utf-8 -*-
import unittest
from fastutils.funcutils import get_inject_params
from fastutils.funcutils import call_with_inject


class TestFuncutils(unittest.TestCase):
    def test01(self):
        def s(a, b):
            return a + b
        data = {
            "a": 1,
            "b": 2,
            "c": 3,
        }
        params = get_inject_params(s, data)
        assert params["a"] == 1
        assert params["b"] == 2

        result = call_with_inject(s, data)
        assert result == 3

    def test02(self):
        def s(a, b=2):
            return a + b
        data = {
            "a": 1,
            "c": 3,
        }
        params = get_inject_params(s, data)
        assert params["a"] == 1
        assert params["b"] == 2

        result = call_with_inject(s, data)
        assert result == 3

    def test03(self):
        def s(a, b=2):
            return a + b
        data = {
            "a": 1,
            "c": 2,
        }
        params = get_inject_params(s, data)
        assert params["a"] == 1
        assert params["b"] == 2

        result = call_with_inject(s, data)
        assert result == 3

if __name__ == "__main__":
    unittest.main()

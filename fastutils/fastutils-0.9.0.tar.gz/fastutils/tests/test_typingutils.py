# -*- coding: utf-8 -*-
import unittest
import os
import binascii
import base64
import codecs
import typing
from fastutils.typingutils import smart_cast

class TestStrUtils(unittest.TestCase):

    def test01(self):
        assert smart_cast(int, "12") == 12
        assert smart_cast(float, "12.34") == 12.34
        assert smart_cast(bool, "true") == True
        assert smart_cast(bytes, "6869") == b"hi"
        assert smart_cast(list, "1,2,3") == ["1", "2", "3"]
        assert smart_cast(typing.List, "[1, 2, 3]") == [1, 2, 3]
        assert smart_cast(dict, """{"a": "a", "b": "b"}""") == {"a": "a", "b": "b"}
        assert smart_cast(typing.Mapping, """{"a": "a", "b": "b"}""") == {"a": "a", "b": "b"}
        assert smart_cast(str, b"hello") == "hello"


    def test03(self):
        assert smart_cast(bool, "True") is True
        assert smart_cast(bool, "False") is False
        assert smart_cast(bool, "1") is True
        assert smart_cast(bool, "0") is False
        assert smart_cast(bool, "y") is True
        assert smart_cast(bool, "n") is False
        assert smart_cast(bool, "yes") is True
        assert smart_cast(bool, "no") is False
        assert smart_cast(bool, 1) is True
        assert smart_cast(bool, 0) is False
        assert smart_cast(bool, True) is True
        assert smart_cast(bool, False) is False
        assert smart_cast(bool, 1.1) is True
        assert smart_cast(bool, 0.0) is False

    def test04(self):
        assert smart_cast(int, 1) == 1
        assert smart_cast(int, 0) == 0
        assert smart_cast(int, "1") == 1
        assert smart_cast(int, "0") == 0

    def test05(self):
        assert smart_cast(str, "a") == "a"
        assert smart_cast(str, "测试") == "测试"
        assert smart_cast(str, 1) == "1"
        assert smart_cast(str, True) == "True"
        assert smart_cast(str, False) == "False"
        assert smart_cast(str, "测试".encode("utf-8")) == "测试"
        assert smart_cast(str, "测试".encode("gbk")) == "测试"

    def test06(self):
        assert smart_cast(bytes, "a") == b"a"
        assert smart_cast(bytes, b"a") == b"a"
        assert smart_cast(bytes, "测试") == "测试".encode("utf-8")
        assert smart_cast(bytes, "YQ==") == b"a"
        assert smart_cast(bytes, "YWI=") == b"ab"
        assert smart_cast(bytes, "6162") == b"ab"

    def test07(self):
        s = os.urandom(16)
        t1 = binascii.hexlify(s).decode()
        t2 = base64.encodebytes(s).decode()
        t3 = base64.urlsafe_b64encode(s).decode()
        assert smart_cast(bytes, t1) == s
        assert smart_cast(bytes, t2) == s
        assert smart_cast(bytes, t3) == s

    def test08(self):
        assert smart_cast(dict, {"a": "a"})["a"] == "a"
        assert smart_cast(dict, """{"a": "a"}""")["a"] == "a"
        assert smart_cast(dict, [("a", "a")])["a"] == "a"

    def test09(self):
        assert smart_cast(list, [1, 2, 3])[0] == 1
        assert smart_cast(list, """[1, 2, 3]""")[0] == 1
        assert smart_cast(list, """1 , 2 , 3""")[0] == "1"

# -*- coding: utf-8 -*-
import unittest
import os
import time
import datetime
import uuid
import decimal
from fastutils.jsonutils import simple_json_dumps
from PIL import ImageGrab

class TestListUtils(unittest.TestCase):
    def test01(self):
        data = {
            "t1": datetime.datetime.now(),
            "t2": datetime.date(2019, 12, 7),
            "t3": datetime.time(21, 35, 1),
            "uid": uuid.uuid4(),
            "p1": 3.45,
            "p2": decimal.Decimal(1) / decimal.Decimal(7),
            "p3": (1, 2, 3),
            "p4": [1, 2, 3, 4],
            "t1": os.urandom(1024),
            "e1": RuntimeError("RuntimeError"),
            "e2": ZeroDivisionError("ZeroDivisionError"),
            "e4": Exception("Exception"),
        }
        result = simple_json_dumps(data)
        assert result

    def test02(self):
        im = ImageGrab.grab()
        data = {
            "ts": time.time(),
            "image": im,
        }
        result = simple_json_dumps(data)
        assert result

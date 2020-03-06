# -*- coding: utf-8 -*-
import os, unittest
from datetime import datetime
from shutil import copyfile

from chappie.utils.date_finder import find_dates


class TestFileManager(unittest.TestCase):
    def setUp(self):
        """ """

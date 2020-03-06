#!/usr/bin/env python
# coding: utf-8

import os
import json
import pprint

from xml.etree import ElementTree

from tests.common import TestCase
from tests.common import BASEDIR


from clocwalk.libs.core.update_mysql import Upgrade
from clocwalk.libs.core.option import init

class TTestCase(TestCase):

    def setUp(self):
        pass

    def test_start(self):
        init()
        up = Upgrade()
        up.start()



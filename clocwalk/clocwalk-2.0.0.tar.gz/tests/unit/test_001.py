#!/usr/bin/env python
# coding: utf-8

import os
import json
import pprint

from xml.etree import ElementTree

from tests.common import TestCase
from tests.common import BASEDIR

from clocwalk.libs.core.data import kb
from clocwalk.libs.analyzer.mvn import start
from clocwalk.libs.analyzer.mvn import recursive_online
from clocwalk.libs.detector.cvecpe import cpe_parse

"""
pip install jieba pyltp
"""

product_white_list = [
    'windows', 'android', 'acrobat_dc', 'nx-os', 'junos'
]

vendor_white_list = [
    'google', 'microsoft', 'adobe', 'linux', 'hp', 'cisco', 'oracle', 'f5', 'foxitsoftware', 'wireshark', 'mozilla',
    'ibm', 'gnu', 'intel', 'juniper', 'dlink', 'sqlite', 'amd', 'amazon', 'apple', 'arm', 'asus',
]

class TTestCase(TestCase):

    def setUp(self):
       pass

    def test_start(self):
        cve_2019 = os.path.join(BASEDIR, 'json', 'nvdcve-1.1-2019.json')
        with open('2019.txt', 'wb') as op:
            with open(cve_2019, 'rb') as fp:
                json_obj = json.load(fp)
                obj_list = []
                for _ in json_obj['CVE_Items']:
                    if not _['configurations']['nodes']:
                        continue

                    cve = _['cve']['CVE_data_meta']['ID']
                    description = _['cve']['description']['description_data'][0]['value']
                    if 'cpe_match' not in _['configurations']['nodes'][0]:
                        if 'children' in _['configurations']['nodes'][0]:
                            if 'cpe_match' in _['configurations']['nodes'][0]['children'][0]:
                                cpe_match = _['configurations']['nodes'][0]['children'][0]['cpe_match']
                    else:
                        cpe_match = _['configurations']['nodes'][0]['cpe_match']

                    for item in cpe_match:
                        vendor, product, version, update = cpe_parse(item['cpe23Uri'])
                        if vendor in vendor_white_list:
                            break
                        op.write(('{0}$$$$$${1}\n'.format(vendor, product)).encode('utf-8'))
                        break



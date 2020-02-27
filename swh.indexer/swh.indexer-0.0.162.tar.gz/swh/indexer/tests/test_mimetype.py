# Copyright (C) 2017-2018  The Software Heritage developers
# See the AUTHORS file at the top-level directory of this distribution
# License: GNU General Public License version 3, or any later version
# See top-level LICENSE file for more information

import pytest
import unittest

from typing import Any, Dict

from swh.indexer.mimetype import (
    MimetypeIndexer, MimetypeRangeIndexer, compute_mimetype_encoding
)

from swh.indexer.tests.utils import (
    CommonContentIndexerTest, CommonContentIndexerRangeTest,
    BASE_TEST_CONFIG, fill_storage, fill_obj_storage, filter_dict,
)


class BasicTest(unittest.TestCase):
    def test_compute_mimetype_encoding(self):
        """Compute mimetype encoding should return results"""
        for _input, _mimetype, _encoding in [
                ('du français'.encode(), 'text/plain', 'utf-8'),
                (b'def __init__(self):', 'text/x-python', 'us-ascii')]:

            actual_result = compute_mimetype_encoding(_input)
            self.assertEqual(actual_result, {
                'mimetype': _mimetype,
                'encoding': _encoding
            })


CONFIG = {
    **BASE_TEST_CONFIG,
    'tools': {
        'name': 'file',
        'version': '1:5.30-1+deb9u1',
        'configuration': {
            "type": "library",
            "debian-package": "python3-magic"
        },
    },
}  # type: Dict[str, Any]


class TestMimetypeIndexer(CommonContentIndexerTest, unittest.TestCase):
    """Mimetype indexer test scenarios:

    - Known sha1s in the input list have their data indexed
    - Unknown sha1 in the input list are not indexed

    """
    legacy_get_format = True

    def get_indexer_results(self, ids):
        yield from self.idx_storage.content_mimetype_get(ids)

    def setUp(self):
        self.indexer = MimetypeIndexer(config=CONFIG)
        self.indexer.catch_exceptions = False
        self.idx_storage = self.indexer.idx_storage
        fill_storage(self.indexer.storage)
        fill_obj_storage(self.indexer.objstorage)

        self.id0 = '01c9379dfc33803963d07c1ccc748d3fe4c96bb5'
        self.id1 = '688a5ef812c53907562fe379d4b3851e69c7cb15'
        self.id2 = 'da39a3ee5e6b4b0d3255bfef95601890afd80709'

        tool = {k.replace('tool_', ''): v
                for (k, v) in self.indexer.tool.items()}

        self.expected_results = {
            self.id0: {
                'id': self.id0,
                'tool': tool,
                'mimetype': 'text/plain',
                'encoding': 'us-ascii',
            },
            self.id1: {
                'id': self.id1,
                'tool': tool,
                'mimetype': 'text/plain',
                'encoding': 'us-ascii',
            },
            self.id2: {
                'id': self.id2,
                'tool': tool,
                'mimetype': 'application/x-empty',
                'encoding': 'binary',
            }
        }


RANGE_CONFIG = dict(list(CONFIG.items()) + [('write_batch_size', 100)])


class TestMimetypeRangeIndexer(
        CommonContentIndexerRangeTest, unittest.TestCase):
    """Range Mimetype Indexer tests.

    - new data within range are indexed
    - no data outside a range are indexed
    - with filtering existing indexed data prior to compute new index
    - without filtering existing indexed data prior to compute new index

    """
    def setUp(self):
        super().setUp()
        self.indexer = MimetypeRangeIndexer(config=RANGE_CONFIG)
        self.indexer.catch_exceptions = False
        fill_storage(self.indexer.storage)
        fill_obj_storage(self.indexer.objstorage)

        self.id0 = '01c9379dfc33803963d07c1ccc748d3fe4c96bb5'
        self.id1 = '02fb2c89e14f7fab46701478c83779c7beb7b069'
        self.id2 = '103bc087db1d26afc3a0283f38663d081e9b01e6'
        tool_id = self.indexer.tool['id']

        self.expected_results = {
            self.id0: {
                'encoding': 'us-ascii',
                'id': self.id0,
                'indexer_configuration_id': tool_id,
                'mimetype': 'text/plain'},
            self.id1: {
                'encoding': 'us-ascii',
                'id': self.id1,
                'indexer_configuration_id': tool_id,
                'mimetype': 'text/x-python'},
            self.id2: {
                'encoding': 'us-ascii',
                'id': self.id2,
                'indexer_configuration_id': tool_id,
                'mimetype': 'text/plain'}
        }


def test_mimetype_w_no_tool():
    with pytest.raises(ValueError):
        MimetypeIndexer(config=filter_dict(CONFIG, 'tools'))


def test_mimetype_range_w_no_tool():
    with pytest.raises(ValueError):
        MimetypeRangeIndexer(config=filter_dict(CONFIG, 'tools'))

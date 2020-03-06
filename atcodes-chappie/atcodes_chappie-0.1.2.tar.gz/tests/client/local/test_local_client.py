# -*- coding: utf-8 -*-
import os, unittest
from chappie.client.local import LocalClient

class TestLocalClient(unittest.TestCase):
    def setUp(self):
        """ """
        self.client = LocalClient()
        self.client.folder = "/tmp/"
        self.params_dict = {
            "Service": 'local'
        }
        self.params_dict = self.client.upload_file(b'test', 'chappie-test/', 'test.txt', self.params_dict)

    def test_file_upload(self):
        """Test upload of file data"""

        self.assertIsInstance(self.params_dict, dict)
        self.assertEqual(self.params_dict.get('Filename'), '/tmp/chappie-test/test.txt')
        self.assertEqual(self.params_dict.get('Service'), 'local')

    def test_file_download(self):
        """Test download of file data"""
        # params_dict = self.client.upload_file(b'test', '/tmp/chappie-test/', 'test.txt', self.params_dict)

        filedata = self.client.download_file(self.params_dict)
        self.assertIsInstance(filedata, bytes)
        self.assertEqual(filedata.decode(), 'test')

        self.params_dict["Filename"] = "non_existent_file.txt"
        filedata = self.client.download_file(self.params_dict)
        self.assertIsInstance(filedata, bytes)
        self.assertEqual(filedata.decode(), '')

    def test_get_url(self):
        """Test get file access url"""
        # params_dict = self.client.upload_file(b'test', '/tmp/chappie-test/', 'test.txt', self.params_dict)

        url = self.client.get_url(self.params_dict)
        self.assertGreater(len(url), 0)

        self.params_dict = {}
        url = self.client.get_url(self.params_dict)
        self.assertEqual(len(url), 0)

    def test_delete_file(self):
        """Test file delete"""
        # params_dict = self.client.upload_file(b'test', '/tmp/chappie-test/', 'test.txt', self.params_dict)

        return_params = self.client.delete_file(self.params_dict)
        self.assertIsInstance(return_params, dict)

        # return false if file is missing - the params needs to be cleaned up
        status = self.client.delete_file(self.params_dict)
        self.assertIsInstance(return_params, dict)

        # return true if Filename is missing - because there is nothing to do
        self.params_dict = {}
        status = self.client.delete_file(self.params_dict)
        self.assertIsInstance(return_params, dict)

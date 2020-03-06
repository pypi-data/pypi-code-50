# -*- coding: utf-8 -*-
import os, unittest
from io import BytesIO
from chappie.client.aws import S3Client

class TestS3Client(unittest.TestCase):
    def setUp(self):
        """ """
        self.client = S3Client()
        self.client.bucket = "bucket-test-w37ryifgckcbjqiu4yrf78qy3874yr8cwfc"

        self.params_dict = {
            "Service": 's3'
        }
        file_obj = BytesIO(b'test')
        self.params_dict = self.client.upload_file(file_obj, 'chappie-test/tmp/', 'test.txt', self.params_dict)

    def test_file_upload(self):
        """Test upload of file data"""

        self.assertIsInstance(self.params_dict, dict)
        self.assertEqual(self.params_dict.get('Bucket'), self.client.bucket)
        self.assertEqual(self.params_dict.get('Key'), 'chappie-test/tmp/test.txt')

    def test_file_download(self):
        """Test download of file data"""

        filedata = self.client.download_file(self.params_dict)

        self.assertIsInstance(filedata, bytes)
        self.assertEqual(filedata.decode(), 'test')

    def test_get_url(self):
        """Test get file access url"""

        url = self.client.get_url(self.params_dict)
        self.assertGreater(len(url), 0)

    def test_delete_file(self):
        """Test file delete"""

        status = self.client.delete_file(self.params_dict)



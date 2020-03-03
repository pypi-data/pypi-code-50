#!/usr/bin/env python
"""Testing aws.py"""
########################################################################
# File: aws_test.py
#  executable: aws_test.py
#
# Author: Andrew Bailey
# History: 03/27/19 Created
########################################################################

import os
import tempfile
import unittest

import boto3
from moto import mock_s3
from py3helpers.aws import AwsS3
from py3helpers.utils import captured_output


class AwsTests(unittest.TestCase):
    """Test the functions in classification.py"""

    @classmethod
    def setUpClass(cls):
        super(AwsTests, cls).setUpClass()
        cls.HOME = '/'.join(os.path.abspath(__file__).split("/")[:-1])
        cls.test_file = os.path.join(cls.HOME, "test_files/test.fa")
        cls.mock = mock_s3()
        cls.mock.start()
        client = boto3.client("s3")
        client.create_bucket(Bucket='mybucket')
        client.upload_file(Filename=cls.test_file, Bucket="mybucket", Key="test.fa")
        client.upload_file(Filename=cls.test_file, Bucket="mybucket", Key="test/test.fa")
        cls.handle = AwsS3(profile_name=None)

    def test_bucket_exists(self):
        # We need to create the bucket since this is all in Moto's 'virtual' AWS account
        exists = self.handle.bucket_exists("mybucket")
        self.assertTrue(exists)
        not_exists = self.handle.bucket_exists("asdfljkasdf")
        self.assertFalse(not_exists)

    def test_download_file(self):
        with captured_output() as (_, _):
            with tempfile.TemporaryDirectory() as tempdir:
                public_s3_file = "mybucket/test.fa"
                dest = os.path.join(tempdir, os.path.basename(public_s3_file))
                if os.path.exists(dest):
                    os.remove(dest)
                location = self.handle.download_object(public_s3_file, tempdir)
                self.assertTrue(os.path.exists(location))

                fake_s3_file = "bailey-assembly-hubs/asdfsaf.txt"
                doesnt_exist = self.handle.download_object(fake_s3_file, tempdir)
                self.assertFalse(doesnt_exist)

    def test_multiprocess_download_objects(self):
        with captured_output() as (_, _):
            with tempfile.TemporaryDirectory() as tempdir:
                public_s3_file = "mybucket/test.fa"
                dest = os.path.join(tempdir, os.path.basename(public_s3_file))
                if os.path.exists(dest):
                    os.remove(dest)
                location = self.handle.multiprocess_download_files([public_s3_file, public_s3_file], tempdir)
                self.assertTrue(os.path.exists(location[0]))
                self.assertTrue(os.path.exists(location[1]))

                fake_s3_file = "bailey-assembly-hubs/asdfsaf.txt"
                doesnt_exist = self.handle.multiprocess_download_files([fake_s3_file, public_s3_file], tempdir)
                self.assertFalse(doesnt_exist[0])
                self.assertTrue(os.path.exists(doesnt_exist[1]))

    def test_create_and_delete_bucket(self):
        with captured_output() as (_, _):
            bucket_name = "py3helper-test"
            self.handle.create_bucket(bucket_name)
            self.assertTrue(self.handle.bucket_exists(bucket_name))
            self.handle.delete_bucket(bucket_name)
            self.assertFalse(self.handle.bucket_exists(bucket_name))

    def test_object_exists(self):
        with captured_output() as (_, _):
            public_s3_file = "mybucket/test.fa"
            self.assertTrue(self.handle.object_exists(public_s3_file))
            fake_s3_file = "bailey-assembly-hubs/asdfsaf.txt"
            self.assertFalse(self.handle.object_exists(fake_s3_file))

    def test_upload_and_delete_object(self):
        with captured_output() as (_, _):
            true_location = "mybucket/test.fa"
            location = self.handle.upload_object(self.test_file, "mybucket/")
            self.assertEqual(true_location, location)
            self.assertTrue(self.handle.object_exists(location))
            deleted = self.handle.delete_object(location)
            self.assertTrue(deleted)
            self.assertFalse(self.handle.object_exists(location))

    def test_split_name(self):
        with captured_output() as (_, _):
            test_name = "/asdf/asdf/asdf/sdf.txt"
            bucket, key = self.handle.split_name(test_name)
            self.assertEqual(bucket, "asdf")
            self.assertEqual(key, "asdf/asdf/sdf.txt")
            test_name = "asdf/asdf/asdf/sdf.txt"
            bucket, key = self.handle.split_name(test_name)
            self.assertEqual(bucket, "asdf")
            self.assertEqual(key, "asdf/asdf/sdf.txt")

    def test_list_objects_generator(self):
        with captured_output() as (_, _):
            gen = self.handle.list_objects_generator("mybucket")
            self.assertEqual(2, len([x for x in gen]))
            gen = self.handle.list_objects_generator("mybucket/test/", "fa")
            self.assertEqual(1, len([x for x in gen]))
            with self.assertRaises(AssertionError):
                self.handle.list_objects_generator("bailey-assembly-hubs/hubExamples/asdf").__next__()
                self.handle.list_objects_generator("hubExamples").__next__()

    def test_list_objects(self):
        with captured_output() as (_, _):
            bucket_path = "mybucket"
            objects = self.handle.list_objects(bucket_path)
            self.assertEqual(len(objects), 2)
            for object in objects:
                self.assertTrue(self.handle.object_exists(object))

            key_path = "mybucket/test/"
            objects = self.handle.list_objects(key_path)
            self.assertEqual(len(objects), 1)
            for object in objects:
                self.assertTrue(self.handle.object_exists(object))

    def test_folder_exists(self):
        with captured_output() as (_, _):
            bucket_path = "mybucket"
            exists = self.handle.folder_exists(bucket_path)
            self.assertTrue(exists)
            bucket_path = "mybucket/test"
            exists = self.handle.folder_exists(bucket_path)
            self.assertTrue(exists)
            exists = self.handle.folder_exists("fake/path")
            self.assertFalse(exists)
            exists = self.handle.folder_exists("bailey-assembly-hubs/hubExamples/asdf")
            self.assertFalse(exists)

    def test_list_buckets(self):
        with captured_output() as (_, _):
            self.assertIsInstance(self.handle.list_buckets(), list)

    @classmethod
    def tearDownClass(cls):
        cls.mock.stop()


if __name__ == '__main__':
    unittest.main()

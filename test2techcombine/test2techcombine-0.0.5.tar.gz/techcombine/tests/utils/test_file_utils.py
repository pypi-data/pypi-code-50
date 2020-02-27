import unittest
from unittest.mock import patch
from techcombine.utils import FileUtils

class FileUtilsTestCase(unittest.TestCase):

    filename = "7509cd4f-a253-40a7-841c-13fc47a2a20e.jpg"

    def test_generate_filename(self):
        filename = FileUtils.generate_filename("test.jpg")
        extension = filename[-3:]
        self.assertEqual(extension, 'jpg')

    @patch("techcombine.utils.FileUtils.generate_filename", return_value=filename)
    def test_upload_to_images(self, patch):
        result = FileUtils.upload_to_images('test', 'test.jpg')
        self.assertEqual(result, f"images\\{self.filename}")
        
    @patch("techcombine.utils.FileUtils.generate_filename", return_value=filename)
    def test_upload_to_payment(self, patch):
        result = FileUtils.upload_to_payment('test', 'test.jpg')
        self.assertEqual(result, f"payment_slips\\{self.filename}")

    @patch("techcombine.utils.FileUtils.generate_filename", return_value=filename)
    def test_upload_to_proof(self, patch):
        result = FileUtils.upload_to_proof('test', 'test.jpg')
        self.assertEqual(result, f"proofs_of_product\\{self.filename}")

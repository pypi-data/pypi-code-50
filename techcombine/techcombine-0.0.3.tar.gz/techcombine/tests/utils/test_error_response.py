from techcombine.utils import ErrorResponse
import unittest

class ErrorResponseTestCase(unittest.TestCase):
    def test_error_response(self):
        try:
            print(i)
        except NameError as errors:
            error = ErrorResponse.create(errors)
        self.assertEqual(error.status_code, 400)
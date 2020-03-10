from typing import Tuple, Any
from unittest import TestCase


class UtilsTestCase(TestCase):
    """An extended instance of TestCase specific for utils modules.

    Contains test-cases for the following modules:
        - response
        - extractor
    """

    def assertRaiseWithMessageOnResponse(
            self,
            expected_exception: BaseException or Tuple[BaseException, Any],
            expected_fail_method: callable,
            exception_message: str,
            message: str or None,
            data: dict or None,
            headers: dict or None
    ):
        """
        Assert the raised exception to be the expected exception provided,
        assert the exception message is equal to the exception message provided.

        :param expected_exception: instance of BaseException
        :param expected_fail_method: the function()/method() that will cause the exception error
        :param exception_message: the exception message specified
        :param message: the message that is set on the response
        :param data: the data that is set on the response
        :param headers: the headers that is set on the response
        :return: None
        """
        with self.assertRaises(expected_exception) as context:
            expected_fail_method(message, data, headers)
        self.assertEqual(exception_message, str(context.exception))

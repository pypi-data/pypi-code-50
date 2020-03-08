""" Unit tests for contact violations queries """
from utils_package.data_controller.scripts.email_controller.contact_violations_queries import ViolationsWriter
from unittest import TestCase
import random


class TestContactViolations(TestCase):
    """ Unit tests for contacts violations queries """

    def setUp(self):
        """ Set up class variables """
        self.violations_writer = ViolationsWriter()

    def test_create_new_record(self):
        """ Validates that a new record is created appropriately
        1. Generate test data
        2. Generate new record in the database
        3. Validate response
        """
        # 1. Generate test data
        record_dict = {
            'strViolationType': 'Test',
            'strViolationAddress': 'test_email%s@test.web' % str(random.randint(000,999)),
            'strIPAddress': '555.555.555.555'
        }

        # 2. Generate new record in the database
        response = self.violations_writer.insert_new_record(record_dict)
        self.assertIsNotNone(response)

        # 3. Validate response
        self.assertEqual(1, response[0])

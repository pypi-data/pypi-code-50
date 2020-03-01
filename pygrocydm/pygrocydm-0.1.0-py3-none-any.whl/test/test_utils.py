from datetime import datetime
from unittest import TestCase

import pygrocydm.utils as utils


class TestUtils(TestCase):
    def test_parse_date_valid(self):
        date_str = "2019-05-04T11:31:04.563Z"
        date_obj = utils.parse_date(date_str)

        assert isinstance(date_obj, datetime)

    def test_parse_date_no_data(self):
        date_str = None
        date_obj = utils.parse_date(date_str)

        assert date_obj is None

    def test_parse_int_valid(self):
        int_str = "2"
        int_number = utils.parse_int(int_str)

        assert isinstance(int_number, int)

    def test_parse_int_no_data(self):
        int_str = None
        int_number = utils.parse_int(int_str)

        assert int_number is None

    def test_parse_int_error(self):
        int_str = "string"
        int_number = utils.parse_int(int_str)

        assert int_number is None

    def test_parse_float_valid(self):
        float_str = "2.01"
        float_number = utils.parse_float(float_str)

        assert isinstance(float_number, float)

    def test_parse_float_no_data(self):
        float_str = None
        float_number = utils.parse_float(float_str)

        assert float_number is None

    def test_parse_float_error(self):
        float_str = "string"
        float_number = utils.parse_float(float_str)

        assert float_number is None

    def test_parse_bool_true_valid(self):
        bool_str = "1"
        bool_value = utils.parse_bool(bool_str)

        assert isinstance(bool_value, bool)

    def test_parse_bool_false_valid(self):
        bool_str = "0"
        bool_value = utils.parse_bool(bool_str)

        assert isinstance(bool_value, bool)

    def test_parse_bool_no_data(self):
        bool_str = None
        bool_value = utils.parse_bool(bool_str)

        assert bool_value is None

    def test_parse_bool_error(self):
        bool_str = "string"
        bool_value = utils.parse_bool(bool_str)

        assert bool_value is None

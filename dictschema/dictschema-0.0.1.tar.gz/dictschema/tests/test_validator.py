from unittest import TestCase

from dictschema.validator import _check_type, _check_keys, _check_func, validate_json
from dictschema.exceptions import SchemaInvalidationError


class TestTypes(TestCase):
    def test_types(self):
        class Foo:
            pass

        tests = [
            (str, "string"),
            (str, r"string"),
            (str, u"string"),
            (int, 4),
            (float, 4.0),
            (Foo, Foo()),
        ]

        for test in tests:
            self.assertEqual(_check_type(*test), True)

    def test_type_failures(self):
        class Foo:
            pass

        tests = [
            (str, 6),
            (str, 6.0),
            (int, 6.0),
            (int, "4"),
            (int, "hello"),
            (float, "4.0"),
            (float, "hello"),
            (Foo, "hello"),
        ]

        for test in tests:
            self.assertRaises(SchemaInvalidationError, _check_type, *test)


class TestKeys(TestCase):
    def test_keys(self):
        _check_keys(
            {"testa": "value", "testo": "value", "testu": "value"},
            {"testa": "eulav", "testo": "eulav", "testu": "eulav"},
        )

    def test_keys_missing(self):
        a = {"testa": "value", "testo": "value"}
        b = {"testa": "eulav", "testo": "eulav", "testu": "eulav"}

        self.assertRaises(SchemaInvalidationError, _check_keys, a, b)

    def test_keys_extra(self):
        a = {"testa": "value", "testo": "value", "testu": "value"}
        b = {"testa": "eulav", "testo": "eulav"}

        self.assertRaises(SchemaInvalidationError, _check_keys, a, b)


class TestFunc(TestCase):
    def test_valid(self):
        tests = [
            (lambda x: x > 50, 60),
            (lambda x: x > 10, 20),
            (lambda x: x == 50, 50),
            (lambda x: "hello" in x, "hello world"),
        ]
        for test in tests:
            self.assertEqual(_check_func(*test), True)

    def test_invalid(self):
        tests = [
            (lambda x: x < 50, 60),
            (lambda x: x == 10, 20),
            (lambda x: x > 50, 50),
            (lambda x: "hello" in x, "good bye"),
        ]
        for test in tests:
            self.assertRaises(SchemaInvalidationError, _check_func, *test)


class TestValidation(TestCase):
    def test_one_dimension_valid(self):
        schema = {"testa": str, "testo": str, "testu": str}
        data = {"testa": "value", "testo": "value", "testu": "value"}

        validate_json(schema, data, blowup_on_failure=True)

    def test_one_dimension_invalid(self):
        schema = {"testa": str, "testo": str, "testu": str}
        data = {"testa": "value", "testo": "value", "testu": 4}

        self.assertRaises(
            SchemaInvalidationError, validate_json, schema, data, blowup_on_failure=True
        )

    def test_two_dimension_valid(self):
        schema = {"testa": str, "testo": str, "testu": {"inner": str}}
        data = {"testa": "value", "testo": "value", "testu": {"inner": "dimension"}}

        validate_json(schema, data, blowup_on_failure=True)

    def test_two_dimension_invalid(self):
        schema = {"testa": str, "testo": str, "testu": {"inner": str}}
        data = {"testa": "value", "testo": "value", "testu": {"inner": 4}}

        self.assertRaises(
            SchemaInvalidationError, validate_json, schema, data, blowup_on_failure=True
        )

    def test_list_valid(self):
        schema = {"testa": str, "testo": str, "testu": [str]}
        data = {
            "testa": "value",
            "testo": "value",
            "testu": ["value", "value", "value"],
        }

        validate_json(schema, data, blowup_on_failure=True)

    def test_list_invalid(self):
        schema = {"testa": str, "testo": str, "testu": [str]}
        data = {"testa": "value", "testo": "value", "testu": ["value", "value", 4]}

        self.assertRaises(
            SchemaInvalidationError, validate_json, schema, data, blowup_on_failure=True
        )

    def test_dict_valid(self):
        schema = {"testa": str, "testo": str, "testu": dict}
        data = {
            "testa": "value",
            "testo": "value",
            "testu": {"value": "value", "nonesense": "value"},
        }

        validate_json(schema, data, blowup_on_failure=True)

    def test_dict_invalid(self):
        schema = {"testa": str, "testo": str, "testu": dict}
        data = {"testa": "value", "testo": "value", "testu": "value"}

        self.assertRaises(
            SchemaInvalidationError, validate_json, schema, data, blowup_on_failure=True
        )

#-*- coding: utf-8 -*-
from unittest import main, TestCase
from cambio import remove_class_instantiation_parameter
from cambio import remove_comments
from cambio import remove_imports
from cambio import declare_variable
from cambio import replace_class
from cambio import replace_variable_declaration

class TestRemovingComments(TestCase):
    def test_removing_comments(self):
        old_code = "# here's a comment\n\nprint('hello')"
        new_code = remove_comments(old_code)
        self.assertEqual(new_code.strip(), "print('hello')")

class TestRemovingImports(TestCase):
    def test_removing_imports(self):
        old_code = "from non_existent_package import non_existent_module\n\nfruit='apple'"
        code_without_imports = remove_imports(old_code)
        exec(code_without_imports.strip())

class TestDeclaringVariable(TestCase):
    def test_declaring_string(self):
        old_settings = "from sys import version_info\npython_version = version_info.major"
        new_settings = declare_variable(old_settings, "SECRET_KEY", '123456789')
        self.assertTrue(new_settings, "from sys import version_info\nSECRET_KEY = '12345678'\npython_version = version_info.major")

    def test_declaring_float(self):
        old_settings = "from sys import version_info\npython_version = version_info.major"
        new_settings = declare_variable(old_settings, "SECRET_NUMBER", 123456789)
        self.assertTrue(new_settings, "from sys import version_info\nSECRET_NUMBER = 12345678\npython_version = version_info.major")

class TestReplacingClass(TestCase):
    def test_replacing_class(self):
        old_code = "my_fruit = Apple(age=1)"
        new_code = replace_class(old_code, "Apple", "Orange")
        self.assertEqual(new_code, "my_fruit = Orange(age=1)")

    def test_conditionally_replacing_class(self):
        old_code = "fruits = [new Apple(old=False), new Apple(old=True)]"
        new_code = replace_class(old_code, "Apple", "Orange", lambda data : 'old=True' in data['text'])
        self.assertEqual(new_code, "fruits = [new Apple(old=False), new Orange(old=True)]")

class TestReplacingVariableDeclaration(TestCase):
    def test_replacing_variable_declaration(self):
        old_code = "HTTP_ORIGIN = 'http://localhost:8000'"
        new_code = replace_variable_declaration(old_code, 'HTTP_ORIGIN', 'http://localhost:4200')
        self.assertEqual(new_code, "HTTP_ORIGIN = 'http://localhost:4200'")

class TestRemovingClassInstantiationParameter(TestCase):
    def test_removing_when_only_one_parameter(self):
        old_code = "my_car = Car(age=10)\nyour_car = Car(age=2)"
        new_code = remove_class_instantiation_parameter(old_code, 'Car', 'age')
        self.assertEqual(new_code, 'my_car = Car()\nyour_car = Car()')

    def test_removing_when_multiple_parameter(self):
        old_code = "my_car = Car(age=10, make='Ford')\nyour_car = Car(year=2020, age=2)"
        new_code = remove_class_instantiation_parameter(old_code, 'Car', 'age')
        self.assertEqual(new_code, "my_car = Car(make='Ford')\nyour_car = Car(year=2020)")

    def test_removing_when_multiple_parameter(self):
        old_code = "my_car = Car(age=10, make='Ford')\nyour_car = Car(year=2020, age=2)"
        new_code = remove_class_instantiation_parameter(old_code, 'Car', 'age')
        self.assertEqual(new_code, "my_car = Car(make='Ford')\nyour_car = Car(year=2020)")

    def test_conditionally_removing_parameter(self):
        old_code = "bottle_1 = Wine(age=100)\nbottle_2 = Wine(age=1)"
        # removes all bottles under 10 years of age
        new_code = remove_class_instantiation_parameter(old_code, 'Wine', 'age', lambda age: age < 10)
        self.assertEqual(new_code, "bottle_1 = Wine(age=100)\nbottle_2 = Wine()")

if __name__ == '__main__':
    main()
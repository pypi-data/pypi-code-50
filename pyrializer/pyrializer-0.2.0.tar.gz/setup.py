# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pyrializer', 'pyrializer.types']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'pyrializer',
    'version': '0.2.0',
    'description': 'A Python object (de)serializer',
    'long_description': '# Pyrializer\n\nA Python object (de)serializer\n\n## Installation\n\n~~~\n$ pip install pyrializer\n~~~\n\n## Basic usage\n\nYou must define classes and describe what attributes and their types using\nclass attributes like this:\n\n~~~ python\nclass Person\n  name = str\n  age = int\n  gender = str\n~~~\n\nSee [Supported types](#supported-types) below.\n\n\n### Decoding from a serialized value\n\nDecoding an object maps a serialized value into a Python object:\n\n~~~ python\nfrom pyrializer import decode\n\npayload = {\n  \'name\': \'John Doe\',\n  \'age\': 52,\n  \'job\': {\n    \'name\': \'Software Engineer\',\n    \'salary\': 24000\n  },\n  \'hobbies\': [\'fishing\', \'skating\']\n}\n\nclass Job:\n  name = str\n  role = str\n  salary = int\n\nclass Address:\n  desc = str\n  city = str\n  country = str\n  zip = int\n\nclass Person:\n  name = str\n  age = int\n  job = Job\n  hobbies = [str]\n  address = Address\n\nperson = decode(Person, payload)\n\nperson.name          # John Doe\nperson.job.salary    # 24000\nperson.job.role      # None\nperson.hobbies[1]    # skating\nperson.address.city  # None\n~~~\n\n\n### Encoding to a serialized value\n\nEncoding an object transform a Python object into a serializable format that can\nbe easily exported to others formats, such as JSON:\n\n~~~ python\nfrom pyrializer import encode\n\nencode(Person, person) # --> { \'name\': \'John Doe\', ... }\n~~~\n\nAdditionaly, you can decorate the classes you want to (de)serialize with the\n```serializable``` decorator. This decorator extends the classes with two\nadditional methods:\n\n~~~ python\nfrom pyrializer import serializable\n\n@serializable\nclass Person:\n  ...\n\nperson = Person.decode(person_payload)\n\nperson.encode() # --> { \'name\': \'John Doe\', ... }\n~~~\n\n\n## Supported types\n\nHere is some examples of supported types\n\n| \\<type>       | JSON equivalent                               |\n|---------------|-----------------------------------------------|\n| `None`        | Any type                                      |\n| `str`         | String                                        |\n| `int`         | Integer                                       |\n| `float`       | Float                                         |\n| `bool`        | Boolean                                       |\n| `[]`          | Array of any type                             |\n| `ClassName`   | Object                                        |\n| _Custom type_ | Any. See [Custom types](#custom-types) below. |\n\nMore advanced examples:\n\n~~~ python\nclass Example:\n  array_of_array_of_ints = [ [ int ] ]  # [ [1,2], [3, 4], [], [5, 6] ]\n  whatever = None  # 42, False, AnotherObject(), etc...\n~~~\n\n\n## Custom types\n\nCustom types allows to decode values that have been previously encoded using a\nprimitive type and in a convenience format.\n\nSome examples include:\n- Unix timestamps: Dates encoded as integers\n- ISO-8601: Dates encoded as strings\n- Gender: Male or female encoded as booleans\n\nTo declare a Custom Type you need to create a class that inherit the `CustomType`\nand define two methods: `decode` and `encode`.\n\nFor example, the following snippets declares a custom type to decode an ISO-8601\ndate into a Python\'s datetime object and vice versa.\n\n~~~ python\nfrom json import loads\nfrom datetime import datetime\nfrom pyrializer import serializable\nfrom pyrializer.types import CustomType\n\nclass ISO_8601(CustomType):\n    def decode(self, fvalue):\n        return datetime.strptime(fvalue, \'%Y-%m-%dT%H:%M:%SZ\')\n\n    def encode(self, fvalue):\n        return datetime.strftime(fvalue, \'%Y-%m-%dT%H:%M:%SZ\')\n\n@serializable\nclass Person:\n    name = str\n    birthdate = ISO_8601  # here we use the custom type\n\njson_payload = json_loads(\'\'\'\n{\n    "name": "John Doe",\n    "birthdate": "1984-01-23T09:37:21Z"\n}\n\'\'\')\n\nperson = Person.decode(payload)\n\nprint(type(person.birthdate))  # <class \'datetime.datetime\'>\nprint(person.birthdate.year)   # 1984\n\nprint(person.encode())         # {\'name\': \'John Doe\', \'birthdate\': \'2000-01-23T09:37:21Z\'}\n~~~\n',
    'author': 'Alfonso Ruzafa',
    'author_email': 'alfonso.ruzafa@movo.me',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/superruzafa/pyrializer',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)

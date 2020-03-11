# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['groundwork_spreadsheets',
 'groundwork_spreadsheets.patterns',
 'groundwork_spreadsheets.patterns.ExcelValidationPattern']

package_data = \
{'': ['*'],
 'groundwork_spreadsheets.patterns.ExcelValidationPattern': ['assets/*']}

install_requires = \
['groundwork>=0.1.10', 'jsonschema', 'openpyxl']

setup_kwargs = {
    'name': 'groundwork-spreadsheets',
    'version': '0.4.3',
    'description': 'Patterns for reading writing spreadsheet documents',
    'long_description': 'groundwork-spreadsheets\n=======================\n\nGroundwork patterns to read and write spreadsheet documents. Excel 2010 (xlsx, xlsm) is supported at the moment.\nThe full documentation is available at https://groundwork-spreadsheets.readthedocs.io/\n\nFor more information regarding groundwork, see `here <https://groundwork.readthedocs.io.>`_.\n\n**ExcelValidationPattern**\n\n*   Uses the library `openpyxl <https://openpyxl.readthedocs.io/en/default/>`_\n*   Can read Excel 2010 files (xlsx, xlsm)\n*   Configure your sheet using a json file\n*   Auto detect columns by names\n*   Layout can be\n\n    *   column based: headers are in a single *row* and data is below\n    *   row based: headers are in a single *column* and data is right of the headers\n\n*   Define column types and verify cell values against them\n\n    *   Date\n    *   Enums (e.g. only  the values \'yes\' and \'no\' are allowed)\n    *   Floating point numbers with optional min/max check\n    *   Integer numbers with optional min/max check\n    *   String with optional regular expression pattern check\n\n*   Exclude data row/columns based on filter criteria\n*   Output is a dictionary of the following form ``row or column number`` -> ``header name`` -> ``cell value``\n*   Extensive logging of problems\n\nHere is how an example json config file looks like::\n\n    {\n        "sheet_config": "last",\n        "orientation": "column_based",\n        "headers_index_config": {\n            "row_index": {\n                "first": 1,\n                "last": "automatic"\n            },\n            "column_index": {\n                "first": "automatic",\n                "last": "severalEmptyCells:3"\n            }\n        },\n        "data_index_config": {\n            "row_index": {\n                "first": 2,\n                "last": "automatic"\n            },\n            "column_index": {\n                "first": "automatic",\n                "last": "automatic"\n            }\n        },\n        "data_type_config": [\n            {\n                "header": "hex number",\n                "fail_on_type_error": true,\n                "fail_on_empty_cell": false,\n                "fail_on_header_not_found": true,\n                "type": {\n                    "base": "string",\n                    "pattern": "^0x[A-F0-9]{6}$"\n                }\n            },\n            {\n                "header": "int number",\n                "type": {\n                    "base": "integer",\n                    "minimum": 2\n                }\n            }\n        ]\n    }\n',
    'author': 'Marco Heinemann',
    'author_email': 'marco.heinemann@useblocks.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://pypi.org/project/groundwork-spreadsheets/',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)

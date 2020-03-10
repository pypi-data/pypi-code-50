# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['jsomark']

package_data = \
{'': ['*']}

install_requires = \
['lxml>=4.5.0,<5.0.0', 'pytest>=5.3.5,<6.0.0']

setup_kwargs = {
    'name': 'jsomark',
    'version': '0.2.1',
    'description': 'json to xml composing and parsing convention.',
    'long_description': 'jsomark\n#######\n\n.. image:: https://travis-ci.org/knowark/jsomark.svg?branch=master\n    :target: https://travis-ci.org/knowark/jsomark\n\n.. image:: https://codecov.io/gh/knowark/jsomark/branch/master/graph/badge.svg\n    :target: https://codecov.io/gh/knowark/jsomark\n\nJSON <-> XML parsing and composing convention.\n\n\nWhat is jsomark?\n================\n\njsomark is a JSON to XML translation convention. jsomark accepts json in an\nstandardized format and converts it to XML. It should as well reverse the\noperation and produce a JSON document from an XML one.\n\nUsage\n=====\n\nTo **create an XML** from a **JSON** document just use\nthe **json_to_xml** function:\n\n.. code-block:: python\n\n    from jsomark import json_to_xml\n    \n    json_data = b\'{"hello": "world"}\'\n\n    xml_data = json_to_xml(json_data)\n\n    assert xml_data == b\'<hello>world</hello>\'\n\n*jsomark* also supports more complex documents, like **nested json**\nstructures and Python json serializable **dictionaries**:\n\n\n.. code-block:: python\n\n    from jsomark import json_to_xml\n    \n    json_data = {\n        "Company": {\n            "Name": "Knowark",\n            "Country": "Colombia"\n        }\n    }\n\n    xml_data = json_to_xml(json_data)\n\n    assert xml_data == (\n        b\'<Company><Name>Knowark</Name><Country>Colombia</Country></Company>\')\n\n\nAttributes\n----------\n\nXML can carry more information (i.e. metadata) than JSON, that is why a\nconvention in the format of a converting json document is needed to match the\noriginal XML semantics. In *jsomark*, **attributes** are defined with\nthe **symbol "&"**:\n\n.. note::\n    Attribute values can only be **text** or **bytes**\n\n.. code-block:: python\n\n    from jsomark import json_to_xml\n\n    json_data = {\n        "Device": {\n            "Reference": {\n                "&": {"ID": "XYZ2020", "Serial": "S10987"}\n            }\n        }\n    }\n\n    xml_data = json_to_xml(json_data)\n\n    assert xml_data == (\n        b\'<Device><Reference ID="XYZ2020" Serial="S10987"/></Device>\')\n\nIf the key with attributes also has a **text content**, then the\n**symbol "#"** should be used to carry it:\n\n\n.. code-block:: python\n\n    from jsomark import json_to_xml\n\n    json_data = {\n        "Employee": {\n            "Company": {\n                "&": {"VAT": "900123765"},\n                "#": "Servagro"\n            }\n        }\n    }\n\n    xml_data = json_to_xml(json_data)\n\n    assert xml_data == (\n        b\'<Employee><Company VAT="900123765">Servagro</Company></Employee>\')\n\n.. note::\n    If a JSON key doesn\'t have attributes, its value becomes the text\n    of the resulting XML element as seen in the previous examples.\n\n\nLists\n-----\n\nLists in the JSON document are interpreted as **repeating elements**\ninside the generated XML.\n\n\n.. code-block:: python\n\n    from jsomark import json_to_xml\n\n    json_data = {\n        "Order": {\n            "Line": [\n                {"&": {"ID": "1"}, "#": "Chocolate Ice Cream"},\n                {"&": {"ID": "2"}, "#": "Banana Split"},\n                {"&": {"ID": "3"}, "#": "Caramel Cake"}\n            ]\n        }\n    }\n\n    xml_data = json_to_xml(json_data)\n\n    assert xml_data == (\n        b\'<Order><Line ID="1">Chocolate Ice Cream</Line>\'\n        b\'<Line ID="2">Banana Split</Line>\'\n        b\'<Line ID="3">Caramel Cake</Line></Order>\')\n\n\nNamespaces\n----------\n\nIn jsomark, namespaces are provided as a **separate dictionary** whose keys\nare the prefixes that must be used in the json document itself. The default\nnamespace should be set in the *\'None\'* key of the namespaces dictionary and\nits keys in the json document don\'t have to be prefixed:\n\n.. Note::\n    Don\'t miss the **":"** separator in the non-default namespaced key\n    such as *\'isbn:number\'* in the following example.\n\n.. code-block:: python\n\n    from jsomark import json_to_xml\n\n    namespaces = {\n        None: \'urn:loc.gov:books\',\n        \'isbn\': \'urn:ISBN:0-395-36341-6\'\n    }\n\n    json_data = {\n        "book": {\n            "title": "Cheaper by the Dozen",\n            "isbn:number": 1568491379\n        }\n    }\n\n    xml_data = json_to_xml(json_data, namespaces=namespaces)\n\n    assert xml_data == (\n        b\'<book xmlns="urn:loc.gov:books" xmlns:isbn="urn:ISBN:0-395-36341-6">\'\n        b\'<title>Cheaper by the Dozen</title>\'\n        b\'<isbn:number>1568491379</isbn:number></book>\'\n',
    'author': 'Knowark',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/knowark/jsomark',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)

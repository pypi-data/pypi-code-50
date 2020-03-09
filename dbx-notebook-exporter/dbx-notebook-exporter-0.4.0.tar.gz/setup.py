# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['dbxnotebookexporter']

package_data = \
{'': ['*'], 'dbxnotebookexporter': ['databricks/*', 'json/*', 'python/*']}

install_requires = \
['ipython>=7,<8', 'nbconvert>=5,<6']

entry_points = \
{'nbconvert.exporters': ['dbx-json-notebook = '
                         'dbxnotebookexporter.json.JsonNotebookExporter:JsonNotebookExporter',
                         'dbx-python-notebook = '
                         'dbxnotebookexporter.python.PythonNotebookExporter:PythonNotebookExporter']}

setup_kwargs = {
    'name': 'dbx-notebook-exporter',
    'version': '0.4.0',
    'description': 'Databrics Notebook Exporter',
    'long_description': 'Databricks Notebook Exporter for nbconvert\n',
    'author': 'Jiri Koutny',
    'author_email': 'jiri.koutny@datasentics.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/DataSentics/dbx-notebook-exporter',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.5.2',
}


setup(**setup_kwargs)

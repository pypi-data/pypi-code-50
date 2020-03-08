# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['private_pypi', 'private_pypi.backends', 'private_pypi.backends.file_system']

package_data = \
{'': ['*']}

install_requires = \
['Jinja2>=2.11.1,<3.0.0',
 'Paste>=3.4.0,<4.0.0',
 'apscheduler>=3.6.3,<4.0.0',
 'cryptography>=2.8,<3.0',
 'dramatiq[redis]>=1.8.1,<2.0.0',
 'filelock>=3.0.12,<4.0.0',
 'fire>=0.2.1,<0.3.0',
 'flask-login>=0.5.0,<0.6.0',
 'flask>=1.1.1,<2.0.0',
 'psutil>=5.6.7,<6.0.0',
 'pydantic>=1.4,<2.0',
 'redis-server>=5.0.7,<6.0.0',
 'shortuuid>=0.5.0,<0.6.0',
 'toml>=0.10.0,<0.11.0',
 'waitress>=1.4.3,<2.0.0']

entry_points = \
{'console_scripts': ['private_pypi_server = '
                     'private_pypi.server:run_server_cli']}

setup_kwargs = {
    'name': 'private-pypi-core',
    'version': '0.1.0',
    'description': 'A private PyPI server powered by flexible backends.',
    'long_description': "# Private-PyPI: A private PyPI server powered by backend(s) like GitHub\n\n## CLI\n\n`private_pypi_server`:\n\n```txt\nRun the private-pypi server.\n\nSYNOPSIS\n    private_pypi_server CONFIG ROOT <flags>\n\nPOSITIONAL ARGUMENTS\n    CONFIG (str):\n        Path to the package repositories config.\n    ROOT (str):\n        Path to the root folder.\n\nFLAGS\n    --admin_secret (Optional[str]):\n        Path to the admin secrets config with read/write permission.\n        This field is required for local index synchronization.\n        Defaults to None.\n    --auth_read_expires (int):\n        The expiration time (in seconds) for read authentication.\n        Defaults to 3600.\n    --auth_write_expires (int):\n        The expiration time (in seconds) for write authentication.\n        Defaults to 300.\n    --extra_index_url (str):\n        Extra index url for redirection in case package not found.\n        If set to empty string explicitly redirection will be suppressed.\n        Defaults to 'https://pypi.org/simple/'.\n    --debug (bool):\n        Enable debug mode.\n        Defaults to False.\n    --host (str):\n        The interface to bind to.\n        Defaults to 'localhost'.\n    --port (int):\n        The port to bind to.\n        Defaults to 8080.\n    **waitress_options (Dict[str, Any]):\n        Optional arguments that `waitress.serve` takes.\n        Details in https://docs.pylonsproject.org/projects/waitress/en/stable/arguments.html.\n        Defaults to {}.\n```\n",
    'author': 'huntzhan',
    'author_email': 'huntzhan.dev@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/private-pypi/private-pypi-core',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)

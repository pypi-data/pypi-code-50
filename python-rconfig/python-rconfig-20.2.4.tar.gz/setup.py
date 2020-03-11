# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['rconfig']

package_data = \
{'': ['*']}

install_requires = \
['python-consul>=1.1.0,<2.0.0']

extras_require = \
{'cli': ['click>=7.0,<8.0'], 'yaml': ['pyyaml>=5.3,<6.0']}

entry_points = \
{'console_scripts': ['rconfig = rconfig.cli:cli']}

setup_kwargs = {
    'name': 'python-rconfig',
    'version': '20.2.4',
    'description': 'Helps bring configuration, stored remotely on a ``Consul`` server, to  your application',
    'long_description': 'rconfig\n=======\n\n  .. image:: https://travis-ci.org/ArtemAngelchev/python-rconfig.svg?branch=master\n      :target: https://travis-ci.org/ArtemAngelchev/python-rconfig\n\n  .. image:: https://coveralls.io/repos/github/ArtemAngelchev/python-rconfig/badge.svg?branch=master\n      :target: https://coveralls.io/github/ArtemAngelchev/python-rconfig?branch=master\n\n  .. image:: https://badge.fury.io/py/python-rconfig.svg\n      :target: https://badge.fury.io/py/python-rconfig\n\n  .. image:: http://img.shields.io/badge/license-MIT-brightgreen.svg?style=flat\n\n\n  ``rconfig`` helps bring configuration, stored remotely on a ``Consul``\n  server, to  your application.\n\n\nInstallation\n------------\n\n  Install the latest version with:\n\n  ::\n\n    pip3 install -U python-rconfig\n\n\n  For command-line support, use the CLI option during installation:\n\n  ::\n\n    pip3 install -U "python-rconfig[cli]"\n\n\n  For command-line and yaml support:\n\n  ::\n\n    pip3 install -U "python-rconfig[cli,yaml]"\n\n\nUsage\n-----\n\n  First off all ``rconfig`` expects that you have the following key structure\n  on the consul server:\n\n  ::\n\n    <root-key>\n        |____<common-config-key>\n        |          |\n        |          |___<some-env-key>\n        |          |           |_____<key-value>\n        |          |           |_____<key-value>\n        |          |\n        |          |___<another-env-key>\n        |                      |_____<key-value>\n        |                      |_____<key-value>\n        |____<app-config-key>\n                   |\n                   |___<some-env-key>\n                   |           |_____<key-value>\n                   |           |_____<key-value>\n                   |\n                   |___<another-env-key>\n                               |_____<key-value>\n                               |_____<key-value>\n\n\n  Here root key stands for the name of the project when some have multiple\n  applications that grouped under some kind of common purpose (often when talk\n  about microservices).\n  Under common configuration key, you should store configurations that common\n  to all your applications in the project, in this case, it\'s much easier to\n  change the config in one place than go to multiple.\n\n\nCommand-line Interface\n----------------------\n\n  CLI offers you an ability to load config from ``Consul`` (within a few ways)\n  without a need of changing application code.\n\n  ::\n\n    Usage: rconfig [OPTIONS] COMMAND [ARGS]...\n\n    Options:\n      -h, --host TEXT     Host of a consul server  [required]\n      -a, --access TEXT   Access key for a consul server  [required]\n      -p, --port INTEGER  Port of consul server  [default: 8500]\n      -k, --key TEXT      Consul key  [required]\n      --help              Show this message and exit.\n\n    Commands:\n      export  Print out bash command export for all found config\n      list    Show all config for given keys\n\n\n  Let\'s look at few examples.\n\n  ::\n\n    <your-awesome-app>\n        |____<prod>\n               |___<LOG_LEVEL -> "WARNING">\n               |___<LOG_FILE_HANDLER -> 1>\n\n\n  To load ``prod`` config of ``you-awesome-app``, issue:\n\n  ::\n\n    $ rconfig -h localhost -a access-key -k \'your-awesome-app/prod\' list\n\n    {\'LOG_LEVEL\': \'WARNING\',\n     \'LOG_FILE_HANDLER\': 1}\n\n\n  To export config to different formats, use:\n\n  Bash:\n  ::\n\n    $ rconfig -h localhost -a access-key -k \'your-awesome-app/prod\' export -f bash\n\n    export LOG_LEVEL=\'WARNING\'\n    export LOG_FILE_HANDLER=\'1\'\n\n  ::\n\n    $ rconfig -h localhost -a access-key -k \'your-awesome-app/prod\' export -f bash:inline\n\n    export LOG_LEVEL=\'WARNING\' LOG_FILE_HANDLER=\'1\'\n\n  Yaml:\n  ::\n\n    $ rconfig -h localhost -a access-key -k \'your-awesome-app/prod\' export -f yaml\n\n    LOG_LEVEL: WARNING\n    LOG_FILE_HANDLER: 1\n\n  Json:\n  ::\n\n    $ rconfig -h localhost -a access-key -k \'your-awesome-app/prod\' export -f json\n\n    {"LOG_LEVEL": "WARNING", "LOG_FILE_HANDLER": 1}\n\n  ::\n\n    $ rconfig -h localhost -a access-key -k \'your-awesome-app/prod\' export -f json:pretty\n\n    {\n        "LOG_LEVEL": "WARNING",\n        "LOG_FILE_HANDLER": 1\n    }\n',
    'author': 'Artem Angelchev',
    'author_email': 'artangelchev@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/ArtemAngelchev/python-rconfig',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4',
}


setup(**setup_kwargs)

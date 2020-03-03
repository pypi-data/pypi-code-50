# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['confme', 'confme.parsing', 'confme.source_backend']

package_data = \
{'': ['*']}

install_requires = \
['pyyaml>=5.3,<6.0']

setup_kwargs = {
    'name': 'confme',
    'version': '0.0.2',
    'description': 'Easy configuration management in python',
    'long_description': '# ConfMe: Configuration Made Easy 💖\n![Python package](https://github.com/iwanbolzern/confme/workflows/Python%20package/badge.svg)\n\nConfMe is a simple to use, production ready application configuration management library, which takes into consideration the following three thoughts:\n1. Access to configuration values must be safe at runtime. **No ```myconfig[\'value1\'][\'subvalue\']``` anymore!**\n2. The configuration must be checked for consistency at startup e.g. type check, range check, ...\n3. Secrets shall be injectable from environment variables\n\n## Installation\nConfMe can be installed from the official python package repository [pypi](https://pypi.org/project/confme/)\n```\npip install confme\n```\nOr, if you\'re using pipenv:\n```\npipenv install confme\n```\nOr, if you\'re using poetry:\n```\npoetry add confme\n```\n\n## Basic Usage of confme\nDefine your config structure as plain python objects with type annotations:\n```python\nfrom confme import configclass, load_config\n\n@configclass\nclass DatabaseConfig:\n    host: str\n    port: int\n    user: str\n\n@configclass\nclass MyConfig:\n    name: int\n    database: DatabaseConfig\n```\nCreate a configuration yaml file with the same structure as your classes have:\n```yaml\nname: "Database Application"\ndatabase:\n    host: "localhost"\n    port: 5000\n    user: "any-db-user"\n```\nLoad the yaml file into your Python object structure and access it in a secure manner:\n```python\nmy_config = load_config(MyConfig, \'config.yaml\')\n\nprint(f\'Using database connection {my_config.database.host} \'\n      f\'on port {my_config.database.port}\')\n```\nIn the background the yaml file is parsed and mapped to the defined object structure. While mapping the values to object properties, type checks are performed. If a value is not available or is not of the correct type, an error is generated already when the configuration is loaded.\n\n## Supported Annotations\nAt the moment the following type annotations are supported:\n- str\n- int\n- float\n- [Secret](#Secret)\n- Range\n\n### Secret[\'ENV_NAME\', TYPE]\nTo inject secrets from environment variables into the configuration structure the Secret annotation should be used. This is especially handy when you\'re deploying applications by using docker. Therefore, let\'s extend the previous example with a Secret annotation:\n```python\n...\nfrom confme import configclass, load_config\nfrom confme.annotation import Secret\n\n@configclass\nclass DatabaseConfig:\n    ...\n    password: Secret[\'highSecurePassword\', str]\n```\nNow set the password to the defined environment variable:\n```bash\nexport highSecurePassword="This is my password"\n```\nLoad your config and check for the injected password.\n```\nmy_config = load_config(MyConfig, \'config.yaml\')\nprint(f\'My password is: {my_config.database.password}\')\n```\n\n### Range[NUMBER_TYPE, FROM, TO]\n```python\n...\nfrom confme import configclass, load_config\nfrom confme.annotation import Secret\n\n@configclass\nclass DatabaseConfig:\n    ...\n    password: Range[int, 2, 3]\n```\n\n### SELECTION[args...]\n\n\n\n## LICENSE\nConfMe is released under the [MIT](LICENSE) license.',
    'author': 'Iwan Silvan Bolzern',
    'author_email': 'iwan.bolzern@zuehlke.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/iwanbolzern/confme',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.5,<4.0',
}


setup(**setup_kwargs)

# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['yamltable']

package_data = \
{'': ['*']}

install_requires = \
['fastjsonschema>=2.14.2,<3.0.0', 'pyyaml>=5.2,<6.0', 'typer>=0.0.8,<0.0.9']

entry_points = \
{'console_scripts': ['yamltable = yamltable.main:app']}

setup_kwargs = {
    'name': 'yamltable',
    'version': '0.0.6',
    'description': 'Command line utility for list organized YAML files.',
    'long_description': '# YamlTable \n\n![](https://img.shields.io/pypi/v/yamltable)\n![]( https://img.shields.io/pypi/pyversions/yamltable.svg)\n![](https://github.com/wolfgangwazzlestrauss/yamltable/workflows/build/badge.svg)\n![](https://img.shields.io/badge/code%20style-black-000000.svg)\n![](https://img.shields.io/github/repo-size/wolfgangwazzlestrauss/yamltable)\n![](https://img.shields.io/github/license/wolfgangwazzlestrauss/yamltable)\n\nYamlTable is a Python command line utility for working with YAML files organized similar to a\nrelational database table. It supports YAML files organized as a list of dictionaries, which share\nkey names and value types. YamlTable provides commands for listing, searching, sorting, etc. data\nfrom the supported files.\n\n\n## Supported YAML File Organizations\n\nYamlTable works with YAML files organized as a list of dictionaries with similar key names and value types.\n```yaml\n- name: awscli\n  description: Amazon Web Services command line client\n  website: https://aws.amazon.com/\n- name: glances\n  description: operating system monitoring interface\n  website: https://github.com/nicolargo/glances\n```\n\nThe JSON schema support is included for YAML files organized as:\n```yaml\nschema:\n  $schema: http://json-schema.org/draft-07/schema#\n  description: pipx package metadata schema\n  type: object\n  properties:\n    name:\n      type: string\n      pattern: "^[\\\\w-]+$"\n    description:\n      type: string\n    website:\n      type: string\n  required:\n  - name\n  - description\n  - website\n  additionalProperties: false\nrows:\n- name: awscli\n  description: Amazon Web Services command line client\n  website: https://aws.amazon.com/\n- name: glances\n  description: operating system monitoring interface\n  website: https://github.com/nicolargo/glances\n```\n\n\n## Getting Started\n\n### Installation\n\nYamlTable can be installed for Python 3.6+ with `pipx`.\n```bash\npipx install yamltable\n```\n\nTo reuse its library functions install with `pip`.\n```bash\npip install --user yamltable\n```\n\n\n### Commands\n\nYamlTable provides the following commands for working with YAML files:\n* `list`: list dictionary key values\n* `search`: search dictionaries by key and value\n* `sort`: sort dictionaries by key and value\n* `validate`: validate that dictionaries conform to the given JSON schema\n\n\n## Contributing\n\nSince YamlTable is in an early development phase, it is not currently open to contributors.\n\n\n## License\n\nLicensed under the [MIT](license.txt) license.\n\n',
    'author': 'Macklan Weinstein',
    'author_email': 'wolfgangwazzlestrauss@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/wolfgangwazzlestrauss/yamltable',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)

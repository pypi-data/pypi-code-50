# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pyinsights']

package_data = \
{'': ['*'], 'pyinsights': ['schema/*']}

install_requires = \
['boto3>=1.10.45,<2.0.0', 'jsonschema>=3.2.0,<4.0.0', 'pyyaml>=5.2,<6.0']

entry_points = \
{'console_scripts': ['pyinsights = pyinsights.cli:main']}

setup_kwargs = {
    'name': 'pyinsights',
    'version': '0.3.1',
    'description': 'AWS CloudWatch Logs Insights is wrapped by Python',
    'long_description': "# PyInsights\n\n![PyPI - Python Version](https://img.shields.io/pypi/pyversions/pyinsights)\n![PyPI](https://img.shields.io/pypi/v/pyinsights?color=blue)\n![GitHub](https://img.shields.io/github/license/homoluctus/pyinsights)\n\nA CLI tool To query CloudWatch Logs Insights.\n\n![usage1](https://raw.githubusercontent.com/homoluctus/pyinsights/master/images/usage1.png)\n\n![usage2](https://raw.githubusercontent.com/homoluctus/pyinsights/master/images/usage2.png)\n\n# ToC\n\n<!-- TOC depthFrom:2 -->\n\n- [Usage](#usage)\n  - [Write Configuration](#write-configuration)\n  - [Execute command](#execute-command)\n- [Configuration](#configuration)\n- [CLI Options](#cli-options)\n- [Environment Variable](#environment-variable)\n\n<!-- /TOC -->\n\n## Usage\n\n### Write Configuration\n\nWrite configuration to `pyinsights.yml` like:\n\n```yaml\nversion: '1.0'\nlog_group_name:\n  - '/ecs/sample'\nquery_string: 'field @message | filter @message like /ERROR/'\nduration: '30m'\nlimit: 10\n```\n\nI wrote examples, so see [examples folder](https://github.com/homoluctus/pyinsights/tree/master/examples).\n\n### Execute command\n\n```bash\npyinsights -c pyinsights.yml -p aws_profile -r region\n```\n\n## Configuration\n\n|Parameter|Type|Required|Description|\n|:--:|:--:|:--:|:--|\n|version|string|true|Choose configuration version from ['1.0']|\n|log_group_name|array|true|Target log group names to query|\n|query_string|string|true|Pattern to query|\n|duration|string or object|true||\n||string||Specify hours, minutes or seconds from now<br>Unit:<br>hours = `h`,<br>minutes = `m`,<br>seconds = `s`,<br>days = `d`,<br>weeks = `w`|\n||object||Specify `start_time` and `end_time`<br>Datetime format must be `YYYY-MM-DD HH:MM:SS`|\n|limit|integer|false|The number of log to fetch|\n\n## CLI Options\n\n|Option|Required|Description|\n|:--:|:--:|:--|\n|-c, --config|true|Specify yaml configuration by absolute or relative path|\n|-f, --format|false|Choose from json or table|\n|-p, --profile|false|AWS profile name|\n|-r, --region|false|AWS region|\n|-v, --version|false|Show version|\n\n## Environment Variable\n\nIf `profile` and `region` options are not specified, AWS Credentials must be set as environment variables.\n\n- AWS_ACCESS_KEY_ID\n- AWS_SECRET_ACCESS_KEY\n- AWS_DEFAULT_REGION\n\nPlease see [Environment Variable Configuration](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/configuration.html#environment-variable-configuration) for the detail.\n",
    'author': 'homoluctus',
    'author_email': 'w.slife18sy@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/homoluctus/pyinsights',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)

# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['doccron']

package_data = \
{'': ['*']}

install_requires = \
['pytz>=2019.3,<2020.0', 'tzlocal>=2.0.0,<3.0.0']

setup_kwargs = {
    'name': 'doccron',
    'version': '1.4.1',
    'description': 'Schedule with Docstrings',
    'long_description': '# DocCron\n\nSchedule with Docstrings\n\n<table>\n    <tr>\n        <td>License</td>\n        <td><img src=\'https://img.shields.io/pypi/l/DocCron.svg\' alt="License"></td>\n        <td>Version</td>\n        <td><img src=\'https://img.shields.io/pypi/v/DocCron.svg\' alt="Version"></td>\n    </tr>\n    <tr>\n        <td>Travis CI</td>\n        <td><img src=\'https://travis-ci.org/roniemartinez/DocCron.svg?branch=master\' alt="Travis CI"></td>\n        <td>Coverage</td>\n        <td><img src=\'https://codecov.io/gh/roniemartinez/DocCron/branch/master/graph/badge.svg\' alt="CodeCov"></td>\n    </tr>\n    <tr>\n        <td>AppVeyor</td>\n        <td><img src=\'https://ci.appveyor.com/api/projects/status/ceqj4tmh13r8hc79/branch/master?svg=true\' alt="AppVeyor"></td>\n        <td>Supported versions</td>\n        <td><img src=\'https://img.shields.io/pypi/pyversions/DocCron.svg\' alt="Python Versions"></td>\n    </tr>\n    <tr>\n        <td>Wheel</td>\n        <td><img src=\'https://img.shields.io/pypi/wheel/DocCron.svg\' alt="Wheel"></td>\n        <td>Implementation</td>\n        <td><img src=\'https://img.shields.io/pypi/implementation/DocCron.svg\' alt="Implementation"></td>\n    </tr>\n    <tr>\n        <td>Status</td>\n        <td><img src=\'https://img.shields.io/pypi/status/DocCron.svg\' alt="Status"></td>\n        <td>Downloads</td>\n        <td><img src=\'https://img.shields.io/pypi/dm/DocCron.svg\' alt="Downloads"></td>\n    </tr>\n</table>\n\n## Installation\n\n```bash\npip install DocCron\n```\n\n## Description\n\nCron-based scheduler inspired by [doctest](https://en.wikipedia.org/wiki/Doctest)\n\n## Example\n\nCron jobs can be embedded into docstrings by using a [literal block](http://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html#literal-blocks) (`::`). Literal blocks should start with `/etc/crontab`.\n\n### Standard/Extended Format\n\nRun `hello()` at every 2nd minute and 3rd minute:\n\n```python\nimport time\n\n\ndef hello():\n    """\n    Print "hello world" at every 2nd minute and 3rd minute:\n\n    /etc/crontab::\n\n        */2 * * * *\n        */3 * * * *\n    """\n    print(time.strftime(\'%Y-%m-%d %H:%M:%S\'), "hello world")\n\n\nif __name__ == \'__main__\':\n    import doccron\n    doccron.run_jobs()\n\n```\n\n### Quartz Format\n\nRun `hello()` at every 2nd second and 3rd second:\n\n```python\nimport time\n\n\ndef hello():\n    """\n    Print "hello world" every 2nd second and 3rd second:\n\n    /etc/crontab::\n\n        */2 * * * * *\n        */3 * * * * *\n    """\n    print(time.strftime(\'%Y-%m-%d %H:%M:%S\'), "hello world")\n\n\nif __name__ == \'__main__\':\n    import doccron\n    doccron.run_jobs(quartz=True)\n\n```\n\n### Timezone-Awareness (CRON_TZ)\n\nDocCron now support `CRON_TZ`. The value of `CRON_TZ` only applies to succeeding cron jobs.\nDocCron supports multiple `CRON_TZ` in a cron table. The default timezone value is the local/system timezone, if not specified. \n\n```python\nimport time\n\n\ndef hello():\n    """\n    Print "hello world" at every 2nd minute and 3rd minute:\n\n    /etc/crontab::\n    \n        CRON_TZ=UTC\n        */2 * * * *\n        */3 * * * *\n    """\n    print(time.strftime(\'%Y-%m-%d %H:%M:%S%z\'), "hello world")\n\n\nif __name__ == \'__main__\':\n    import doccron\n    doccron.run_jobs()\n\n```\n\n## Features\n\n- Standard and extended cron formats (see [CRON Expression](https://en.wikipedia.org/wiki/Cron#CRON_expression))\n- [Nonstandard predefined scheduling definitions](https://en.wikipedia.org/wiki/Cron#Nonstandard_predefined_scheduling_definitions)\n- [Non-standard characters](https://en.wikipedia.org/wiki/Cron#Non-standard_characters)\n- [Quartz format](http://www.quartz-scheduler.org/documentation/quartz-2.x/tutorials/crontrigger.html)\n- Works with documentation tools like [Sphinx](https://github.com/sphinx-doc/sphinx)\n- Timezone-awareness (CRON_TZ)\n\n## TODO\n\n- Human readable date/time strings \n\n## References\n\n- [Cron Format](http://www.nncron.ru/help/EN/working/cron-format.htm)\n- [Wikipedia - Cron](https://en.wikipedia.org/wiki/Cron)\n\n## Author\n\n- [Ronie Martinez](mailto:ronmarti18@gmail.com)',
    'author': 'Ronie Martinez',
    'author_email': 'ronmarti18@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/roniemartinez/DocCron',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.5,<4',
}


setup(**setup_kwargs)

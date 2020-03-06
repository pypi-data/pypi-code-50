# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['reschedule']

package_data = \
{'': ['*']}

install_requires = \
['google-api-python-client>=1.7.11,<2.0.0',
 'google-auth-oauthlib>=0.4.1,<0.5.0',
 'python-dateutil>=2.8.1,<3.0.0',
 'typing-extensions>=3.7.4,<4.0.0']

entry_points = \
{'console_scripts': ['reschedule = reschedule.console:run']}

setup_kwargs = {
    'name': 'reschedule',
    'version': '0.1.0',
    'description': 'Parser and scheduler for syncing a markdown(ish) todo list with google calendar.',
    'long_description': '# TODO MD Scheduler\n\n## Goal\n\nI have a markdown file of todos which I want to automatically schedule on my google calendar.\n\n```markdown\n- [ ] task name @related_person +task_project est:10m id:1f2a4b\n```\n\nEach task is assumed to have the following properties\n\n- **id**: a unique id\n- **description**: a description of the task\n- **estimate**: a time estimate written as `5m` or `2h` for 5 minutes and 2 hours respectively.\n\nThis program divides a day into chunks of size 15 minutes and schedules tasks during those chunks. The tasks are added to a unique calendar in Google Calendar.\n\n## Design\n\n`task_parser.py` parses the todo file and creates a list of tagged `task` objects.\n\n`calendar_api.py` is in charge of getting calendar information.\n',
    'author': 'Luke Murray',
    'author_email': 'lukepigeonmail@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/lukesmurray/reschedule',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.5,<4.0',
}


setup(**setup_kwargs)

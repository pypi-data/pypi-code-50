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
 'tqdm>=4.43.0,<5.0.0',
 'typing-extensions>=3.7.4,<4.0.0']

entry_points = \
{'console_scripts': ['reschedule = reschedule.console:run']}

setup_kwargs = {
    'name': 'reschedule',
    'version': '0.1.3',
    'description': 'Parser and scheduler for syncing a markdown(ish) todo list with google calendar.',
    'long_description': '# Reschedule\n\n[![PyPI version](https://badge.fury.io/py/reschedule.svg)](https://badge.fury.io/py/reschedule)\n\n## Goal\n\nI want to keep track of all my todos in a [plain text file](https://jeffhuang.com/productivity_text_file/) but also automatically schedule my todos on my google calendar. When I write my todos in a todo list I often fail to allocate time for them in my calendar. When I look at my week I feel like I have tons of free time but in reality I have a full day of work to do. As an example this is what my week looks like without todos vs. with todos (in orange).\n\n![Example week with todos and without todos](img/calendar.gif)\n\nThis program automatically parses todos from a markdown file and schedules them on a google calendar.\n\n```markdown\n- [ ] task name est:10m due:2020-03-20 id:1f2a4b\n```\n\n## Installation\n\nUsing python >3.6\n\n`pip install reschedule`\n\nNow you can reschedule your todos by running `reschedule` from the command line.\nThe first time you run `reschedule` you\'ll be prompted to authorize with google and a config file will be created for you at `~/.cache/reschedule/config.json`.\n\n## Configuration\n\n```json\n{\n  "work_start_time": "08:00",\n  "work_end_time": "18:00",\n  "task_file_path": "~/todo.md",\n  "task_calendar_name": "Reschedule Tasks",\n  "chunk_size": 15,\n  "default_est": "30m"\n}\n```\n\n- `work_start_time`: the earliest a task will be scheduled to start in `%H:%M` format. (i.e. military time such as 08:30 or 23:00)\n- `work_end_time`: the latest a task will be scheduled to end in `%H:%M` format. (i.e. military time such as 08:30 or 23:00)\n- `task_file_path`: the absolute path to your markdown file of tasks\n- `task_calendar_name`: the name of the google calendar this program will create to store your tasks. **Must be unique from an existing calendar**.\n- `chunk_size`: the minimum length of an event. 15 is a good default to keep your day from becoming too fragmented.\n- `default_est`: the default time estimate for a task\n\n## Task File Format\n\nTask are written using markdown task-list format. To create a task use a new line with `- [ ]`. To mark a task as complete use `- [x]`. Metadata is attached to tasks using a `key:value` syntax. The `key` and the `value` cannot contain spaces or `:`. I call an instance of a `key:value` pair a tag, for instance an `id` tag is a `key:value` pair with a `key` of `id`. Every task needs a unique `id` tag for example `id:1aab7d`. Tasks can have an `est` tag which contains a time estimate written as `30m` or `1h` for 30 minutes or 1 hour respectively. Any number followed by `m` or `h` is acceptable as a value for the `est` tag. Finally tasks can have a `due` tag which contains a due-date formatted as `YYYY-MM-dd`.\n\n```markdown\n<!-- A task with an estimate of 30 minutes, due March 6, 2020, with id 16cfe6 -->\n\n- [ ] What you want to do est:30m due:2020-03-06 id:16cfe6\n```\n\n## VSCode Snippets\n\nI use the following user defined [VSCode Markdown Snippets](https://code.visualstudio.com/docs/languages/markdown#_snippets-for-markdown) to create my tasks.\n\n```jsonc\n  // add a new task\n  "task": {\n    "prefix": "//task",\n    "body": [\n      "- [ ] ${1:What do you want to do?} est:${2:30m} id:$RANDOM_HEX"\n    ]\n  },\n  // add a due date to a task\n  "due": {\n    "prefix": "//due",\n    "body": "due:${1:$CURRENT_YEAR}-${2:$CURRENT_MONTH}-${3:$CURRENT_DATE}"\n  },\n  // create a random variable\n  "random": {\n    "prefix": "//random",\n    "body": "$RANDOM_HEX"\n  }\n```\n',
    'author': 'Luke Murray',
    'author_email': 'lukepigeonmail@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/lukesmurray/reschedule',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)

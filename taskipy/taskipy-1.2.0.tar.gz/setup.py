# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['taskipy']

package_data = \
{'': ['*']}

install_requires = \
['toml>=0.10.0,<0.11.0']

entry_points = \
{'console_scripts': ['task = taskipy.cli:main']}

setup_kwargs = {
    'name': 'taskipy',
    'version': '1.2.0',
    'description': 'tasks runner for python projects',
    'long_description': '<img src="./logo.svg" width="150" />\n\n> the complementary task runner for python poetry projects\n\n[![pypi](https://img.shields.io/pypi/v/taskipy?style=flat-square)](https://pypi.org/project/taskipy/)\n[![travis](https://img.shields.io/travis/illBeRoy/taskipy/master?style=flat-square)](https://travis-ci.org/illBeRoy/taskipy)\n<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->\n[![All Contributors](https://img.shields.io/badge/all_contributors-1-orange.svg?style=flat-square)](#contributors-)\n<!-- ALL-CONTRIBUTORS-BADGE:END -->\n\n## General\nEvery development pipeline has tasks, such as `test`, `lint` or `publish`. With taskipy, you can define those tasks in one file and run them with a simple command.\n\nFor instance, instead of running the following command:\n```bash\npython -m unittest tests/test_*.py\n```\n\nYou can create a task called `test` and simply run:\n```bash\npoetry run task test\n```\n\nIn addition, you can compose tasks and group them together, and also create dependencies between them.\n\nThis project is heavily inspired by npm\'s [run script command](https://docs.npmjs.com/cli/run-script).\n\n## Requirements\nPython 3.6 or newer.\n\nYour project directory should include a valid `pyproject.toml` file, as specified in [PEP-518](https://www.python.org/dev/peps/pep-0518/).\n\n## Usage\n### Installation\nTo install taskipy as a dev dependency, simply run:\n```bash\npoetry add --dev taskipy\n```\n\n### Adding Tasks \nIn your `pyproject.toml` file, add a new section called `[tool.taskipy.tasks]`.\n\nThe section is a key-value map, from the names of the task to the actual command that should be run in the shell.\n\nExample:\n\n__pyproject.toml__\n```toml\n[tool.taskipy.tasks]\ntest = "python -m unittest tests/test_*.py"\nlint = "pylint tests taskipy"\n```\n\n### Running Tasks\nIn order to run a task, run the following command in your terminal:\n```bash\npoetry run task test\n```\n\n### Passing Command Line Args to Tasks\nIf you want to pass command line arguments to tasks (positional or named), simply append them to the end of the task command.\n\nFor example, running the above task like this:\n```bash\npoetry run task test -h\n```\n\nIs equivalent to running:\n```bash\npython -m unittest tests/test_*.py -h\n```\n\nAnd will show unittest\'s help instead of actually running it.\n\n> ⚠️ Note: if you are using pre \\ post hooks, do notice that arguments are not passed to them, only to the task itself.\n\n### Composing Tasks\n#### Grouping Subtasks Together\nSome tasks are composed of multiple subtasks. Instead of writing plain shell commands and stringing them together, you can break them down into multiple subtasks:\n```toml\n[tool.taskipy.tasks]\nlint_pylint = "pylint tests taskipy"\nlint_mypy = "mypy tests taskipy"\n```\n\nAnd then create a composite task:\n```toml\n[tool.taskipy.tasks]\nlint = "task lint_pylint && task lint_mypy"\nlint_pylint = "pylint tests taskipy"\nlint_mypy = "mypy tests taskipy"\n```\n\n#### Pre Task Hook\nTasks might also depend on one another. For example, tests might require some binaries to be built. Take the two following commands, for instance:\n```toml\n[tool.taskipy.tasks]\ntest = "python -m unittest tests/test_*.py"\nbuild = "make ."\n```\n\nYou could make tests depend on building, by using the **pretask hook**:\n```toml\n[tool.taskipy.tasks]\npre_test = "task build"\ntest = "python -m unittest tests/test_*.py"\nbuild = "make ."\n```\n\nThe pretask hook looks for `pre_<task_name>` task for a given `task_name`. It will run it before running the task itself. If the pretask fails, then taskipy will exit without running the task itself.\n\n#### Post Task Hook\nFrom time to time, you might want to run a task in conjuction with another. For example, you might want to run linting after a successful test run. Take the two following commands, for instance:\n```toml\n[tool.taskipy.tasks]\ntest = "python -m unittest tests/test_*.py"\nlint = "pylint tests taskipy"\n```\n\nYou could make tests trigger linting, by using the **posttask hook**:\n```toml\n[tool.taskipy.tasks]\ntest = "python -m unittest tests/test_*.py"\npost_test = "task lint"\nlint = "pylint tests taskipy"\n```\n\nThe posttask hook looks for `post_<task_name>` task for a given `task_name`. It will run it after running the task itself. If the task failed, then taskipy will not run the posttask hook.\n\n### Using Taskipy Without Poetry\nTaskipy was created with poetry projects in mind, but actually only requires a valid `pyproject.toml` file in your project\'s directory. As a result, you can use it even eithout poetry:\n\n#### Installing With PIP\nInstall taskipy on your machine or in your virtualenv using:\n```bash\npip install taskipy\n```\n\n#### Running Tasks\nHead into your project\'s directory (don\'t forget to activate virtualenv if you\'re using one), and run the following command:\n```bash\ntask TASK\n```\nWhere `TASK` is the name of your task.\n\n### Advanced Use Cases\nIf you have a more specific use case, you might not be the first to run into it! Head over to the [ADVANCED_FEATURES](./docs/ADVANCED_FEATURES.md) doc, and look it up.\n\n## Contributors ✨\n\nThanks goes to these wonderful people ([emoji key](https://allcontributors.org/docs/en/emoji-key)):\n\n<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->\n<!-- prettier-ignore-start -->\n<!-- markdownlint-disable -->\n<table>\n  <tr>\n    <td align="center"><a href="https://twitter.com/merwok_"><img src="https://avatars0.githubusercontent.com/u/635179?v=4" width="100px;" alt=""/><br /><sub><b>Éric Araujo</b></sub></a><br /><a href="https://github.com/illBeRoy/taskipy/commits?author=merwok" title="Code">💻</a></td>\n  </tr>\n</table>\n\n<!-- markdownlint-enable -->\n<!-- prettier-ignore-end -->\n<!-- ALL-CONTRIBUTORS-LIST:END -->\n\nThis project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind welcome!\n',
    'author': 'Roy Sommer',
    'author_email': 'roy@sommer.co.il',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/illBeRoy/taskipy',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)

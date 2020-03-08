# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['stirfried']

package_data = \
{'': ['*']}

install_requires = \
['aioredis>=1.3.1,<2.0.0',
 'celery>=4.4.0,<5.0.0',
 'python-socketio>=4.4.0,<5.0.0',
 'redis>=3.4.1,<4.0.0',
 'uvicorn>=0.11.3,<0.12.0']

setup_kwargs = {
    'name': 'stirfried',
    'version': '0.2.0',
    'description': 'Socket.IO server to schedule Celery tasks from clients in real-time.',
    'long_description': '[![PyPI version](https://badge.fury.io/py/stirfried.svg)](https://badge.fury.io/py/stirfried)\n[![Docker Image Version (latest semver)](https://img.shields.io/docker/v/korijn/stirfried?label=docker%20image)](https://hub.docker.com/r/korijn/stirfried)\n\n# Stirfried \U0001f961\n\nSocket.IO server to schedule Celery tasks from clients in real-time.\n\n## Getting started\n\nStirfried has a three layered architecture:\n\n1. [Celery workers](#celery-workers)\n2. [Socket.IO server](#socketio-server)\n3. [Socket.IO clients](#socketio-clients)\n\n### Installation\n\nYou really only need to install Stirfried in your Celery workers via pip:\n\n `pip install stirfried`\n\nFor the Socket.IO server component you can use the prebuilt docker image\n`korijn/stirfried`, or you can copy the project and customize it to your\nliking (there\'s only about 40 lines of code in the server).\n\nClients can connect using standard [Socket.IO](https://socket.io/) libraries.\n\n### Celery workers\n\nIn your Celery workers, import the `StirfriedTask`:\n\n```python\nfrom stirfried.celery import StirfriedTask\n```\n\nConfigure `StirfriedTask` as the base class globally:\n\n```python\napp = Celery(..., task_cls=StirfriedTask)\n```\n\n...or per-task:\n\n```python\n@app.task(base=StirfriedTask)\ndef add(x, y, room=None):\n    return x + y\n```\n\n#### Rooms\n\nThe client passes the room to emit to via the keyword argument `room`.\n\nThe `StirfriedTask` base class depends on the presence of this keyword argument.\n\nThis means you are required to add the keyword argument `room=None` to your\ntask definitions in order to receive it.\n\nIt also gives the client control over whether the task results and progress\nupdates should be emitted to them or a certain room.\n\n#### Progress\n\nYou can emit progress from tasks by calling `self.emit_progress(current, total)`.\n\nNote that you are required to pass `bind=True` to the `celery.task` decorator\nin order to get access to the `self` instance variable.\n\n```python\n@celery.task(bind=True)\ndef add(self, x, y, room=None):\n    s = x\n    self.emit_progress(50, 100)  # 50%\n    s += y\n    self.emit_progress(100, 100)  # 100%\n    return s\n```\n\n\n### Socket.IO server\n\nYou are required to provide a `settings.py` file with the configuration\nfor the server.\n\nIt requires at a minimum:\n\n* `socketio_redis` - Redis connection string for the [Socket.IO](https://github.com/miguelgrinberg/python-socketio) server.\n* `broker_url` - Connection string for the [Celery](https://github.com/celery/celery/) [broker](http://docs.celeryproject.org/en/latest/getting-started/brokers/index.html).\n\nThe server sends tasks to the Celery broker\n[by name](https://docs.celeryproject.org/en/latest/reference/celery.html#celery.Celery.send_task),\nso it can act as a gateway to many different Celery workers with\ndifferent tasks. You can leverage Celery\'s\n[task routing configuration](http://docs.celeryproject.org/en/latest/userguide/routing.html)\nfor this purpose.\n\n#### Example\n\nLet\'s say you have two workers, one listening on the `feeds` queue and\nanother on the `web` queue. This is how you would configure the \nserver accordingly:\n\n```python\nsocketio_redis = "redis://localhost:6379/0"\nbroker_url = "redis://localhost:6379/1"\ntask_routes = {\n    "feed.tasks.*": {"queue": "feeds"},\n    "web.tasks.*": {"queue": "web"},\n}\n```\n\n#### Docker image\n\nYou can build the docker image and run it locally as follows (note that you need to create a `settings.py` file):\n\n```bash\ndocker run --rm -ti -v `pwd`/settings.py:/app/settings.py:ro -p 8000:8000 stirfried\n```\n\n### Socket.IO clients\n\nTODO\n',
    'author': 'Korijn van Golen',
    'author_email': 'korijn@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)

# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['gym_simple_cliffworld', 'gym_simple_cliffworld.envs']

package_data = \
{'': ['*']}

install_requires = \
['gym>=0.17.1,<0.18.0']

setup_kwargs = {
    'name': 'gym-simple-cliffworld',
    'version': '0.1.0',
    'description': 'A simplified version of Cliffworld in an OpenAI Gym Environment',
    'long_description': '# gym-simple-cliffworld\n\nA simplified version of Cliffworld in an OpenAI Gym Environment.\n\nThis is a project by [Winder Research](https://WinderResearch.com), a Cloud-Native Data Science consultancy.\n\n## Installation\n\n`pip install gym-simple-cliffworld`\n\n## Usage\n\n```python\nimport gym\nimport gym_simple_cliffworld\n\nenv = gym.make("SimpleCliffworld-v0")\nepisode_over = False\nrewards = 0\nwhile not episode_over:\n    state, reward, episode_over, _ = env.step(env.action_space.sample())\n    print(state, reward)\n    rewards += reward\nprint("Total reward: {}".format(rewards))\n```\n\n## Credits\n\nGitlab icon made by [Payungkead](https://www.flaticon.com/authors/payungkead) from [www.flaticon.com](https://www.flaticon.com/).',
    'author': 'Phil Winder',
    'author_email': 'phil@WinderResearch.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://gitlab.com/winderresearch/rl/environments/gym-simple-cliffworld/',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)

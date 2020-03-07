# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['shrimpy']

package_data = \
{'': ['*']}

install_requires = \
['fire>=0.2.1,<0.3.0', 'jsonschema>=3.2.0,<4.0.0']

entry_points = \
{'console_scripts': ['shrimpy = shrimpy:activate']}

setup_kwargs = {
    'name': 'shrimpy',
    'version': '0.1.13',
    'description': 'A minimal engine for choose-your-own-adventure games.',
    'long_description': '# :fried_shrimp: shrimpy\n\nA minimal engine for choose-your-own-adventure games.\n\n## Install\n\nInstalling shrimpy is easy. To install shrimpy on your computer, open your terminal and enter:\n\n`sudo pip3 install shrimpy`\n\n## About\n\nIn shrimpy, **a game is simply a folder that contains scene files.** Scene files are written in JSON.\n\n## Create\n\nTo create your first shrimpy game, make a new folder somewhere on your computer. Name your new folder `hello-shrimpy`.\n\nNext, create a new file called `start.json` inside `hello-shrimpy`. Copy the following code into `start.json`:\n\n````\n{\n  "id": "start",\n  "text": "You lose!",\n  "options": [\n    {\n      "text": "What? Already?",\n      "scene": "end"\n    }\n  ]\n}\n````\n\nOnce you have saved `start.json` inside of the `hello-shrimpy` folder, create a second file in `hello-shrimpy` and name it `end.json`. Copy the following code into `end.json`:\n\n````\n{\n  "id": "end",\n  "text": "GAME OVER. Enter q to quit.",\n  "options": [\n    {\n      "text": "(play again)",\n      "scene": ""\n    }\n  ]\n}\n````\n\nAt this point, you should have a folder called `hello-shrimpy` that contains two files: `start.json` and `end.json`.\n\nThat\'s it! Your new shrimpy game is finished and ready to play.\n\n## Play\n\nTo play the game you just created, navigate into the `hello-shrimpy` folder and run:\n\n`shrimpy play`\n\n## Quit\n\nTo quit playing a shrimpy game, you can always enter `q` when prompted for an option number.\n\n## Update\n\nShrimpy keeps getting better. To update shrimpy to the latest version, enter:\n\n`sudo pip3 install shrimpy -U`\n\n## Uninstall\n\nDown with shrimpy! To uninstall shrimpy from your computer, enter:\n\n`sudo pip3 uninstall shrimpy`\n\n## Scene Schema\n\nFor your reference, the following JSON schema is used to validate scene files:\n\n ````\n {\n \t"$schema": "http://json-schema.org/draft-04/schema#",\n \t"type": "object",\n \t"properties": {\n \t\t"id": {\n \t\t\t"type": "string"\n \t\t},\n \t\t"text": {\n \t\t\t"type": "string"\n \t\t},\n \t\t"options": {\n \t\t\t"type": "array",\n \t\t\t"items": [\n \t\t\t\t{\n \t\t\t\t\t"type": "object",\n \t\t\t\t\t"properties": {\n \t\t\t\t\t\t"text": {\n \t\t\t\t\t\t\t"type": "string"\n \t\t\t\t\t\t},\n \t\t\t\t\t\t"scene": {\n \t\t\t\t\t\t\t"type": "string"\n \t\t\t\t\t\t}\n \t\t\t\t\t},\n \t\t\t\t\t"required": [\n \t\t\t\t\t\t"text",\n \t\t\t\t\t\t"scene"\n \t\t\t\t\t]\n \t\t\t\t}\n \t\t\t]\n \t\t}\n \t},\n \t"required": [\n \t\t"id",\n \t\t"text",\n \t\t"options"\n \t]\n }\n ````\nTo learn more about JSON Schema, [click here](https://json-schema.org/).\n',
    'author': 'Yosoi',
    'author_email': 'yosoi@protonmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/yosoi/shrimpy',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)

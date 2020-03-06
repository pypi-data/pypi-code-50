# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pecrs']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'pecrs',
    'version': '0.12',
    'description': 'Pythonic Entity Collision Resolution System',
    'long_description': '![logo](https://raw.githubusercontent.com/solidsmokesoftware/pecrs-py/master/logo.png)\n\n# Pythonic Entity Collision Resolution System\n\npecrs is a pure Python 2D physics system with a focus on top-down games and simple platformers. \n\nPure Python makes pecrs portable and easy to modify to suit your own needs.\n\nFocused use-case makes pecrs simple to learn and use.\n\n# Installation\n\nVia pip\n\n`python -m pip install pecrs`\n\n# Quickstart\n```python\n\nfrom pecrs import *\n\n\nid = 0\nposition = Vector(100, 500)\nshape = Rect(10, 10)\nbody = Body(id, position, shape)\n\nid = 1\nposition_other = Vector(100, 495)\nother = Body(id, position_other, shape)\n\nspatial_hash_size = 128\nspace = Space(spatial_hash_size)\n\nspace.add(body)\nspace.add(other)\n\ncollision = space.check(body)\nprint(f"Are 0 and 1 colliding? {collision}")\n```\n\n# Structual Overview\n\nThe base functionality of pecrs is provided by Vector, Shape, SpatialHash, and Index. Vector and Shape are datatypes for describing a Body. SpatialHash keeps track of a collection of objects based on position, while Index keeps track of indentification numbers for Bodies.\n\nAt the core level of operations are Bodies and the Collider. A Body consists of a Shape, a position(Vector), and an id(Provided by Index) and is the key unit of simulation. The Collider works with Shapes and Vectors to detect intersections.\n\nAbove that exists the Space. The Space manages Bodies in a SpatialHash and detects collisions within via the Collider.\n\nAt the highest level exists the Controller. The Controller creates Bodies in a Space and handles their interactions, as well as the physics simulation itself. The Controller is follows Object-Oriented design principles and provides callbacks into all of its functionality that can be easily extended. \n\n# Real-world Usage\n```python\n\nfrom pecrs.controller import Controller\nfrom pecrs.body import Body\nfrom pecrs.shape import Rect\n\n\nclass Player(Body):\n   def __init__(self, id, position):\n      shape = Rect(32, 32)\n      super().__init__(id, position, shape)\n      self.name = "player"\n      self.speed = 100\n      self.moving = True\n\n\nclass Objects(Controller):\n   def __init__(self, collision_area_size):\n      super().__init__(collision_area_size)\n      self.factory["player"] = Player\n      \n   def on_make(self, body):\n      print(f"Objects made {body.name} {body.id} at {body.position.x}:{body.position.y}")\n      \n   def on_motion(self, body):\n      print(f"{body.name} {body.id} is at {body.position.x}:{body.position.y}")\n\n   def on_collision(self, body, collisions):\n      print(f"{body.name} is colliding with {len(collisions)} others")\n\nobjects = Objects(64)\n\nplayerA = objects.make(Player, 0, 0) # Bodies can be made with thier class\nplayerB = objects.make_key("player", 10, 0) # Or with a key that can be communicated easily over networks\n\ncollision = objects.space.check_two(playerA, playerB)\nif collision:\n   print("Bodies A and B are colliding")\n\nobjects.place(playerA, 100, 0)\nobjects.move_to(playerB, 1, 0, 1)\n\nobjects.turn(playerA, 0, 1)\nobjects.move(playerA, 1)\n\ncollision = objects.space.check(playerA)\nif collision:\n   print("Body A is colliding with another body")\n\nobjects.delete(playerA)\nobjects.delete(playerB)\n\nplayerC = objects.make(Player, 0, 0, dx=1)\nplayerD = objects.make(Player, 0, 0, dx=-1)\nplayerE = objects.make(Player, 0, 0, dy =1)\nplayerF = objects.make(Player, 0, 0, dy =-1)\n\ncollisions = objects.space.get_body(playerC)\nif collisions:\n   print(f"Body C is colliding with {len(collisions)} others")\n\nfor i in range(10):\n   objects.step(0.1)\n\n```\n\n# Documentation\n\nhttps://solidsmokesoftware.github.io/pecrs/\n\n# Demonstration\n\nhttps://github.com/solidsmokesoftware/solconomy\n\n![solconomy](https://camo.githubusercontent.com/de20b3b2014d20a8746f7346e777e323586d5a35/68747470733a2f2f692e696d6775722e636f6d2f566277677664372e706e67)\n\n# Requirements\n\nTested with Python3.6.9\n',
    'author': 'Solid Smoke Software',
    'author_email': 'solid.smoke.software@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/solidsmokesoftware/pecrs-py',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.6.9,<4.0.0',
}


setup(**setup_kwargs)

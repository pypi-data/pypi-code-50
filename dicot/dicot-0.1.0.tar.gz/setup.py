# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['dicot']

package_data = \
{'': ['*']}

install_requires = \
['pyserial']

setup_kwargs = {
    'name': 'dicot',
    'version': '0.1.0',
    'description': 'Controls Futaba Command-Type Servo motors.',
    'long_description': "# dicot\n\nControls Futaba Command-Type Servo motors. It is developed and tested with [RS204MD](http://www.futaba.co.jp/robot/command_type_servos/rs204md).\n\n## Installation\n\n```shell\n$ pip install dicot\n```\n\n## Usage\n\nCreate the serial port connection, enable the torque, and set the motor angle:\n\n```pycon\n>>> improt dicot\n>>>\n>>> cnx = dicot.open('COM1')\n>>>\n>>> motor = cnx.motor(1)  # id = 1\n>>> motor.torque_enabled = True\n>>>\n>>> motor.angle = 45  # degree\n```\n\nOr set with duration:\n\n```pycon\n>>> motor.rotate(90, msec=5000)  # with duration\n```\n\nCan get and set various parameters through the attributes:\n\n```pycon\n>>> motor.angle\n90  # degree\n>>>\n>>> motor.load\n6  # mA\n>>>\n>>> motor.temperature\n30  # Celsius\n>>>\n>>> motor.voltage\n5.2  # V\n>>>\n>>> motor.max_torque = 80  # %\n>>> motor.pid_coeff = 100  # %\n```\n\nThe value set in the ROM area must be written by executing `motor.rom.write()` in order to retain it even after the motor is turned off:\n\n```pycon\n>>> motor.torque_enabled = False\n>>> motor.rom.cw_angle_limit = 100  # degree\n>>> motor.rom.ccw_compliance_margin = 0.2  # degree\n>>> motor.rom.ccw_compliance_slope = 20  # degree\n>>> motor.rom.write()\n```\n\nCan also change the ID:\n\n```pycon\n>>> motor.rom.id = 2\n>>> motor.rom.write()\n```\n\nMotorList can handle multiple motors collectively:\n\n```pycon\n>>> motors = dicot.MotorList([motor, cnx.motor(2), cnx.motor(3)])\n>>> motors.torque_enabled = True\n>>> motors.angles = [30, 60, 90]\n```\n\nThe connection object supports the with statement:\n\n```python  \nimport dicot\n\nwith dicot.open('COM1') as cnx:\n    motor = cnx.motor(1)\n    print(motor.firm_version)\n```  \n",
    'author': 'lanius',
    'author_email': 'lanius@nirvake.org',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/lanius/dicot',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)

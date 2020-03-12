# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['capablerobot_usbhub', 'capablerobot_usbhub.registers']

package_data = \
{'': ['*'], 'capablerobot_usbhub': ['formats/*']}

install_requires = \
['click>=7.0,<8.0',
 'construct>=2.9.51,<3.0.0',
 'pyusb>=1.0.2,<2.0.0',
 'pyyaml>=5.3,<6.0']

entry_points = \
{'console_scripts': ['usbhub = capablerobot_usbhub.console:main']}

setup_kwargs = {
    'name': 'capablerobot-usbhub',
    'version': '0.2.6',
    'description': 'Host side driver for the Capable Robot Programmable USB Hub',
    'long_description': '# Capable Robot Programmable USB Hub Driver \n\nThis package has two functions:\n\n- It provides access to internal state of the Capable Robot USB Hub, allowing you to monitor and control the Hub from an upstream computer.\n- It creates a transparent CircuitPython Bridge, allowing unmodified CircuitPython code to run on the host computer and interact with I2C & SPI devices attached to the USB Hub.\n\n![Capable Robot logo & image of Programmable USB Hub](https://raw.githubusercontent.com/CapableRobot/CapableRobot_USBHub_Driver/master/images/logo-usbhub-header.jpg "Capable Robot logo & image of Programmable USB Hub")\n\n## Installing\n\nInstall and update using [pip](https://pip.pypa.io/en/stable/quickstart/):\n\n\tpip install capablerobot_usbhub\n\nThis driver requires Python 3.6 or newer.\n\nOn Linux, the the udev permission system will likely prevent normal users from accessing the USB Hub\'s endpoint which allows for Hub Monitoring, Control, and I2C Bridging.  To resolve this, install the provided udev rule:\n\n```\nsudo cp 50-capablerobot-usbhub.rules /etc/udev/rules.d/\nsudo udevadm control --reload\nsudo udevadm trigger\n```\n\nThen unplug and replug your USB Hub.  Note, the provided udev rule allows all system users to access the Hub, but can be changed to a specific user or user group.\n\n## Usage & Examples\n\nThe [examples](https://github.com/CapableRobot/CapableRobot_USBHub_Driver/tree/master/examples) folder has some code samples of how to use this Python API to control the Programmable USB Hub.  There is also another [example repository](https://github.com/CapableRobot/CapableRobot_USBHub_CircuitPython_Examples) which includes additional host-side code as well as examples of customizing behavior via changing the Hub\'s firmware.\n\n## Working Functionality\n\n- Reading USB Hub registers over USB and decoding of register data.\n- Writing USB Hub registers over USB.\n- Reading & writing I2C data thru the Hub.\n- Python API to control and read the two GPIO pins.\n- CircuitPython I2C Bridge to the rear I2C1 port.  \n- CircuitPython SPI Bridge to the internal mikroBUS header.\n\n## Not Working / Not Implemented Yet\n\n_No known errata at this time_\n\n## Contributing \n\nContributions are welcome! Please read our \n[Code of Conduct](https://github.com/capablerobot/CapableRobot_CircuitPython_USBHub_Bridge/blob/master/CODE_OF_CONDUCT.md)\nbefore contributing to help this project stay welcoming.',
    'author': 'Chris Osterwood',
    'author_email': 'osterwood@capablerobot.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/CapableRobot/CapableRobot_USBHub_Driver',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)

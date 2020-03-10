# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['websocks']

package_data = \
{'': ['*']}

install_requires = \
['asyncio-socks5>=0.2.7,<0.3.0', 'click>=7.0,<8.0', 'websockets>=8.1,<9.0']

extras_require = \
{':sys_platform != "win32" and sys_platform != "cygwin" and platform_python_implementation != "pypy"': ['uvloop']}

entry_points = \
{'console_scripts': ['websocks = websocks.commands:main']}

setup_kwargs = {
    'name': 'websocks',
    'version': '0.2.7',
    'description': 'A websocket-based socks5 proxy.',
    'long_description': '# websocks\n\n[![Docker Cloud Build Status](https://img.shields.io/docker/cloud/build/abersheeran/websocks?style=flat-square)](https://hub.docker.com/r/abersheeran/websocks) ![Docker Pulls](https://img.shields.io/docker/pulls/abersheeran/websocks)\n\n基于隧道与拟态流量混淆的匿名通信系统。\n\n可对传输层的流量数据进行加密混淆，保护用户上网时的信息、隐私安全。\n\nTCP: 使用隧道流量混淆技术，将需要传递的数据放在 WebSocket 的有效载荷中，作为二进制帧传递。\n\nUDP: 使用拟态流量混淆技术，将需要传递的数据混淆后传递与服务器。\n\n关于本项目使用方法、详细设计介绍以及其他内容请访问 [`websocks:wiki`](https://github.com/abersheeran/websocks/wiki)\n',
    'author': 'abersheeran',
    'author_email': 'me@abersheeran.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/abersheeran/websocks',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.6.1,<4.0.0',
}


setup(**setup_kwargs)

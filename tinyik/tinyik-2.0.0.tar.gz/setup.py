# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['tinyik']

package_data = \
{'': ['*']}

install_requires = \
['autograd', 'scipy']

extras_require = \
{'viz': ['open3d>=0.9.0,<0.10.0']}

setup_kwargs = {
    'name': 'tinyik',
    'version': '2.0.0',
    'description': 'A tiny inverse kinematics solver',
    'long_description': "tinyik\n======\n\ntinyik is a simple and naive inverse kinematics solver.\n\nIt defines the actuator as a set of links and revolute joints from an origin. Here is the example of a robot arm that consists of two joints that rotate around z-axis and two links of 1.0 length along x-axis:\n\n.. code-block:: python\n\n    >>> import tinyik\n    >>> arm = tinyik.Actuator(['z', [1., 0., 0.], 'z', [1., 0., 0.]])\n\nSince the joint angles are zero by default, the end-effector position is at (2.0, 0, 0):\n\n.. code-block:: python\n\n    >>> arm.angles\n    array([ 0.,  0.])\n    >>> arm.ee\n    array([ 2.,  0.,  0.])\n\nSets the joint angles to 30 and 60 degrees to calculate a new position of the end-effector:\n\n.. code-block:: python\n\n    >>> import numpy as np\n    >>> arm.angles = [np.pi / 6, np.pi / 3]  # or np.deg2rad([30, 60])\n    >>> arm.ee\n    array([ 0.8660254,  1.5      ,  0.       ])\n\nSets a position of the end-effector to calculate the joint angles:\n\n.. code-block:: python\n\n    >>> arm.ee = [2 / np.sqrt(2), 2 / np.sqrt(2), 0.]\n    >>> arm.angles\n    array([  7.85398147e-01,   3.23715739e-08])\n    >>> np.round(np.rad2deg(arm.angles))\n    array([ 45.,   0.])\n\nOptionally, it has the visualization feature. Passes the actuator to it to visualize its structure:\n\n.. code-block:: python\n\n    >>> leg = tinyik.Actuator([[.3, .0, .0], 'z', [.3, .0, .0], 'x', [.0, -.5, .0], 'x', [.0, -.5, .0]])\n    >>> leg.angles = np.deg2rad([30, 45, -90])\n    >>> tinyik.visualize(leg)\n\n.. image:: https://raw.githubusercontent.com/lanius/tinyik/master/assets/viz_structure.png\n\nPasses with the target position, can compare before and after the IK. The gray links are before IK and the white links are after it. The red sphere is the target position:\n\n.. code-block:: python\n\n    >>> tinyik.visualize(leg, target=[.8, .0, .8])\n\n.. image:: https://raw.githubusercontent.com/lanius/tinyik/master/assets/viz_ik.png\n\nInstallation\n------------\n\n.. code-block:: console\n\n    $ pip install tinyik\n\nWith the visualization feature:\n\n.. code-block:: console\n\n    $ pip install tinyik[viz]\n",
    'author': 'lanius',
    'author_email': 'lanius@nirvake.org',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/lanius/tinyik',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.5,<4.0',
}


setup(**setup_kwargs)

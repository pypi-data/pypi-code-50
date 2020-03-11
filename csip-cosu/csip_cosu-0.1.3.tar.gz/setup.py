"""
 * $Id:$
 *
 * This file is part of the Cloud Services Integration Platform (CSIP),
 * a Model-as-a-Service framework, API and application suite.
 *
 * 2012-2017, Olaf David and others, OMSLab, Colorado State University.
 *
 * OMSLab licenses this file to you under the MIT license.
 * See the LICENSE file in the project root for more information.
"""

from setuptools import setup, find_packages
import sys
sys.path.extend(['/od/projects/csip_cosu'])

import cosu

setup(name='csip_cosu',
      version=cosu.__version__,
      url='http://alm.engr.colostate.edu/cb/project/csip',
      license='MIT',
      author='Olaf David',
      author_email='odavid@colostate.edu',
      description='CSIP COSU library',
      packages=find_packages(include=['cosu']),
      long_description=open('README.md').read(),
      install_requires=[
            "pyswarms == 1.1.0",
            "csip == 0.9.3",
      ],
      zip_safe=False
)

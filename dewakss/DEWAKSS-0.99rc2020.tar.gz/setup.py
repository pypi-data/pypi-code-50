from setuptools import setup

DISTNAME = 'DEWAKSS'
VERSION = '0.99rc2020'
DESCRIPTION = "De-noising Expression by Weighted Affinity-based Kernal with Self Supervision."
# with open('README.rst') as f:
#     LONG_DESCRIPTION = f.read()
MAINTAINER = 'Andreas Tjarnberg'
MAINTAINER_EMAIL = 'andreas.tjarnberg@nyu.edu'
URL = 'https://gitlab.com/Xparx/dewakss'
DOWNLOAD_URL = 'https://gitlab.com/Xparx/dewakss/-/archive/Tjarnberg2020branch/dewakss-Tjarnberg2020branch.zip'
LICENSE = 'LGPL'


setup(name=DISTNAME,
      version=VERSION,
      description=DESCRIPTION,
      url=URL,
      author=MAINTAINER,
      author_email=MAINTAINER_EMAIL,
      license=LICENSE,
      packages=['dewakss'],
      python_requires='>=3.7',
      install_requires=[
          'sparse-dot-mkl',
          'scipy',
          'sklearn',
          'scanpy',
          'scvelo',
          'matplotlib',
      ],
      zip_safe=False)

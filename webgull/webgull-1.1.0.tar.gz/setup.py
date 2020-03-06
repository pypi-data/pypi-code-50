import pathlib
from setuptools import setup

cwd = pathlib.Path(__file__).parent
readme = (cwd / 'README.md').read_text()

setup(name='webgull',
      version='1.1.0',
      license='GPL3',
      long_description=readme,
      long_description_content_type='text/markdown',
      packages=[
          'webgull'
      ],
      entry_points = {
          'console_scripts': ['webgull=webgull.main:entry']
      },
      zip_safe=False
)

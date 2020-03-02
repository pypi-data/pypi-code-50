import os

from setuptools import setup, find_packages

install_requires = []
with open('requirements.txt', 'r') as f:
    for requirement in f.readlines():
        install_requires.append(requirement)

setup(name='twistream',
      version='0.1.1',
      description="Automate Twitter Stream data collection",
      long_description=open('README.md', 'r').read(),
      long_description_content_type="text/markdown",
      author='Guillermo Carrasco',
      author_email='guille.ch.88@gmail.com',
      url='https://github.com/guillermo-carrasco/twistream',
      packages=find_packages(exclude=('tests',)),
      include_package_data=True,
      keywords=['Social Media', 'Twitter', 'Data Mining', 'Data Collection'],
      zip_safe=True,
      install_requires=install_requires,
      data_files=[(os.path.join(os.environ['HOME'], '.twistream'), [])],
      entry_points={
          'console_scripts': ['twistream = twistream.cli.cli:twistream']
      },
      classifiers=[
          "Programming Language :: Python",
          "Programming Language :: Python :: 3"
      ]
      )

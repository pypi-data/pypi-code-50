from setuptools import setup, find_packages
from os import path
from io import open

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
      name='py_random_words',
      version='0.5',
      url='https://github.com/andreasonny83/py_random_words',
      license='MIT',
      author='andreasonny83',
      author_email='andreasonny83@gmail.com',
      description='Generate random names',
      packages=find_packages(),
      long_description=long_description,
      long_description_content_type="text/markdown",

      install_requires=['choice'],

      # Specify which Python versions you support. In contrast to the
      # 'Programming Language' classifiers above, 'pip install' will check this
      # and refuse to install the project if the version does not match. If you
      # do not support Python 2, you can simplify this to '>=3.5' or similar, see
      # https://packaging.python.org/guides/distributing-packages-using-setuptools/#python-requires
      python_requires='>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*, <4',
      data_files=[('animals.json', ['animals.json'])],
)

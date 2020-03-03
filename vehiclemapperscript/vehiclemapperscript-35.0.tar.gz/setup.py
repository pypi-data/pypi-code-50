from setuptools import setup
# read the contents of your README file
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'readme.md'), encoding='utf-8') as f:
    long_description = f.read()
setup(name='vehiclemapperscript',
      version='35.0',
      description='Vehicle Mapper',
      url='',
      long_description=long_description,
      long_description_content_type='text/markdown',
      author='yzcop',
      author_email='yadugkrishnan@gmail.com',
      license='MIT',
      install_requires=['pandas','fuzzywuzzy','python-Levenshtein','xlsxwriter'],
      packages=['vehiclemapperscript'],
      zip_safe=False)

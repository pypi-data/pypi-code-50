from setuptools import setup
from os import path

current_dir = path.abspath(path.dirname(__file__))

with open(path.join(current_dir, 'README.md')) as f:
    long_description = f.read()

setup(
      name='modelwithlog',
      version='0.1',
      description='Django model with log',
      long_description=long_description,
      long_description_content_type='text/markdown',
      url='https://gitlab.com/kas-factory/packages/django-model-with-log',
      author='Aurora @ KF',
      author_email='aurora@kasfactory.net',
      license='COPYRIGHT',
      packages=['modelwithlog'],
      install_requires=[
          'django>=3.0.2'
      ],
      zip_safe=False)

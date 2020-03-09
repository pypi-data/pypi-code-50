from setuptools import setup

# read the contents of your README file
from os import path

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(name='m-schedule',
      version='0.6.5',
      description='Tạo schedule chạy theo lịch',
      url='https://github.com/mobiovn',
      author='MOBIO',
      author_email='contact@mobio.vn',
      license='MIT',
      packages=['mobio/libs/schedule'],
      install_requires=['m-singleton',
                        'schedule',
                        'm-threadpool',
                        'redis',
                        'python-dateutil',
                        'unidecode'],
      long_description=long_description,
      long_description_content_type='text/markdown'
      )

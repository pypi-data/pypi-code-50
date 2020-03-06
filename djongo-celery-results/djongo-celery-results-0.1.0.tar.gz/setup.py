import os
from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()
# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='djongo-celery-results',
    version='0.1.0',
    packages=['djongo_celery_results'],
    include_package_data=True,
    description='A simple Django app to to integrate djongo and celery.',
    url='https://gitlab.com/Udalbert/djongo-celery-results',
    author='Udalbert',
    author_email='udgottschalk@gmail.com',
    keywords=['djongo-python', 'celery-djongo', 'django-djongo'],
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
    ],
)

import os
import subprocess

from setuptools import setup, find_packages


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname),
                encoding='utf-8').read()


def version():
    git_version = None
    try:
        git_tag = subprocess.check_output(['git', 'describe', '--tags'])
        if git_tag:
            git_version = git_tag.strip()[1:].decode('utf-8')
    except Exception as _e:
        pass
    if not git_version:
        git_version = 'SNAPSHOT'
    return git_version


setup(
    name='bottle-elastic-apm',
    version=version(),
    url='https://gitlab.com/TruckPad/utils/bottle-elastic-apm',
    author='TruckPad Dev Team',
    author_email='devs@truckpad.com.br',
    description='Plugin to implement instrumentation of elastic apm on a '
                'bottle server.',
    long_description=read('README.md'),
    long_description_content_type='text/markdown',
    install_requires=['bottle', 'elastic-apm'],
    packages=find_packages('.'),
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Operating System :: POSIX',
        'Programming Language :: Python :: 3',
        'Topic :: Internet :: WWW/HTTP'
    ]
)

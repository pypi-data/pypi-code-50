from setuptools import setup, find_packages

from cinnamon_task_base import __version__ as version

with open('requirements.txt') as file:
    install_requires = file.read()

setup(
    name='cinnamon-task-base',
    version=version,
    packages=find_packages(),
    author="Cinnamon",
    url='https://github.com/Cinnamon/podder-task-base',
    include_package_data=True,
    install_requires=install_requires,
    package_data={
        'cinnamon_task_base': [
            'task_initializer/templates/*',
            'task_initializer/templates/api/*',
            'task_initializer/templates/api/protos/*',
            'task_initializer/templates/scripts/*',
        ],
    },
)

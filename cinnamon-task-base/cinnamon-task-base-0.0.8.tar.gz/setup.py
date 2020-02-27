from setuptools import setup, find_packages

setup(
    name='cinnamon-task-base',
    version='0.0.8',
    packages=find_packages(),
    author="podder-ai",
    url='https://github.com/Cinnamon/podder-task-base',
    include_package_data=True,
    install_requires=[
        'grpcio-tools',
        'googleapis-common-protos',
        'python-daemon',
        'mysqlclient',
        'SQLAlchemy',
    ],
)

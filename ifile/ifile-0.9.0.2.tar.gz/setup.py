from setuptools import setup, find_packages

from ifile.version import __version__

setup(
    name='ifile',
    version=__version__,
    author='Greene',
    author_email='Glf9832@163.com',
    description='this is a file mange tool',
    url='https://github.com/Glf9832/ifile',
    packages=find_packages(exclude=['tests*']),
    package_data={
        '': ['ifile/default_config.ini', 'LICENSE',
             'MANIFEST.ini', 'README.md']},
    include_package_data=True,
    install_requires=[
        'Click',
        'SQLAlchemy==1.3.5',
        'Flask==1.0.3',
        'eventlet==0.25.0',
        'pymysql==0.9.3',
        'pymongo==3.9.0',
        'gunicorn==19.9.0',
        'pyftpdlib==1.5.5',
        'grpcio==1.26.0',
        'protobuf==3.11.2'
    ],
    entry_points='''
        [console_scripts]
        ifile=ifile.cli:cli
    ''',
    python_requires='>=3.6',
)

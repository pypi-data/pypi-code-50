import pathlib

from setuptools import setup

setup(
    name='fxq-commons',
    version='1.0.8',
    packages=[
        'fxq.core',
        'fxq.core.beans',
        'fxq.core.beans.factory',
        'fxq.core.beans.factory.annotation',
        'fxq.core.context',
        'fxq.core.stereotype',
        'fxq.commons'
    ],
    url='https://bitbucket.org/fxqlabs-oss/fxq-commons/',
    license='MIT',
    author='Jonathan Turnock',
    author_email='jonathan.turnock@outlook.com',
    description='Common python utilities and scripts for fxq labs',
    long_description=(pathlib.Path(__file__).parent / "README.md").read_text(),
    long_description_content_type="text/markdown",
    install_requires=[
        'stringcase',
        'requests',
        'multidispatch',
        'jsonpickle'
    ]
)

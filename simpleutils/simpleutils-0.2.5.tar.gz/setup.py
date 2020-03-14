import io
from setuptools import setup
from setuptools import find_packages

setup(
    name='simpleutils',
    version='0.2.5',
    packages=find_packages(),
    url='',
    license='MIT',
    author='wegamekinglc',
    author_email='wegamekinglc@hotmail.com',
    install_requires=io.open("requirements.txt", encoding='utf8').read(),
    description=''
)

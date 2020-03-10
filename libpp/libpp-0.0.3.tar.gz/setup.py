import os
import re
import sys

from setuptools import setup, find_packages


setup(
    name='libpp',
    version='0.0.3',
    description="peng's python library",
    author='hupeng,zhangpeng',
    author_email='hupeng@webprague.com',
    python_requires=">=3.5",
    url='https://github.com/imu-hupeng/libpp',
    packages=find_packages(exclude=["libpp"]),
    include_package_data=True,
    install_requires=['librosa>=0.6.2', 'numpy>=1.16.2', 
                      'PySoundFile>=0.9.0.post1', 'yagmail>=0.11.224',
                      'scipy>=1.1.0'],
    license='Apache License 2.0',
    zip_safe=False,
)

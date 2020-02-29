#-*- coding:utf-8 -*-

"""
Created on 2020/02/29
------
@author: LI Chao
Email: lichao19870617@gmail.com or lichao19870617@163.com
"""

from setuptools import setup, find_packages

setup(
    name='easylearn',
    version='0.1.6.alpha',
    description=(
        'This project is designed for machine learning in resting-state fMRI field'
    ),
    author='Chao Li',
    author_email='lichao19870617@gmail.com',
    maintainer='Chao Li +',
    maintainer_email='lichao19870617@gmail.com',
    license='MIT License',
    packages=find_packages(),
    platforms=["all"],
    url='https://github.com/lichao312214129/lc_rsfmri_tools_python',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Science/Research',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
)
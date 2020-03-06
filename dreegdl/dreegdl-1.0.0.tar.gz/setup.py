#!/usr/bin/python
#
# Copyright 2020 ToCodeForSoul
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# coding=utf-8
from setuptools import setup, find_packages

setup(
    name='dreegdl',
    version='1.0.0',
    description='Depression Rest EEG Deep Learning - Deep Learning tools for Depression Rest EEG signals',
    long_description=
    ('Depression Rest EEG Deep Learning package is intended to be used for works on'
     'the corresponding EEG signals dataset provided by http://predict.cs.unm.edu/downloads.php'
     'any further updates and changes may be applied soon.'),
    author='ToCodeForSoul',
    author_email='tocodeforsoul@gmail.com',
    url='https://github.com/tocodeforsoul/Depression-Rest-EEG-Deep-Learning',
    keywords=['EEG', 'Depression', 'Rest', 'Depression Rest', 'Depression Rest EEG',
              'Depression Rest EEG Deep Learning', 'Deep Learning', 'Regression', 'Classification'],
    install_requires=[
        'tensorflow',
        'keras',
        'numpy',
        'pywavelets',
        'scipy',
        'tqdm',
        'IPython',
        'statsmodels',
        'sklearn',
        'pandas',
        'matplotlib',
    ],
    packages=find_packages(),
    license='Apache 2.0')
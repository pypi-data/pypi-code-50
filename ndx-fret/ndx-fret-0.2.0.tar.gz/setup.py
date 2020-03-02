# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
from shutil import copy2
import os

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup_args = {
    'name': 'ndx-fret',
    'version': '0.2.0',
    'description': 'FRET',
    'long_description': long_description,
    'long_description_content_type': 'text/markdown',
    'author': 'Luiz Tauffer and Ben Dichter',
    'author_email': 'ben.dichter@gmail.com',
    'url': 'https://github.com/ben-dichter-consulting/ndx-fret',
    'license': '',
    'install_requires': ['pynwb'],
    'packages': find_packages('src/pynwb'),
    'package_dir': {'': 'src/pynwb'},
    'package_data': {'ndx_fret': [
        'spec/ndx-fret.namespace.yaml',
        'spec/ndx-fret.extensions.yaml',
    ]},
    'classifiers': [
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
    ],
    'zip_safe': False
}


def _copy_spec_files(project_dir):
    ns_path = os.path.join(project_dir, 'spec', 'ndx-fret.namespace.yaml')
    ext_path = os.path.join(project_dir, 'spec', 'ndx-fret.extensions.yaml')

    dst_dir = os.path.join(project_dir, 'src', 'pynwb', 'ndx_fret', 'spec')
    if not os.path.exists(dst_dir):
        os.mkdir(dst_dir)

    copy2(ns_path, dst_dir)
    copy2(ext_path, dst_dir)


if __name__ == '__main__':
    _copy_spec_files(os.path.dirname(__file__))
    setup(**setup_args)

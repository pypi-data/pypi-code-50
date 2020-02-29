#!/usr/bin/env python3
import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='jupyter_multiselection',
    version='0.1.1',
    author='Christian-Alexander Dudek',
    author_email='christian@dudek.me',
    description=('A nbextension to select occurences of the '
                 'currently selected text'),
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://gitlab.com/chdudek/jupyter_multiselection',
    packages=setuptools.find_packages('src'),
    package_dir={'': 'src'},
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        'Programming Language :: Python :: 3',
        'Development Status :: 4 - Beta',
        'Framework :: IPython',
        'Framework :: Jupyter',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
        'Programming Language :: JavaScript',
        'Topic :: Scientific/Engineering :: Information Analysis',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
        'Topic :: Utilities',
    ],
    python_requires='>=3.6',
    )

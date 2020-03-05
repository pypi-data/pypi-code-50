#!/usr/bin/env python
import re

from setuptools import setup, find_namespace_packages

with open('README.rst', 'r') as f:
    long_description = f.read()

with open('flatspin/__init__.py', 'r') as f:
    version = re.search(r'__version__ = \'(.*?)\'', f.read()).group(1)

setup(
    name='flatspin',
    version=version,
    url='https://flatspin.gitlab.io/',
    project_urls={
        "Source Code": "https://gitlab.com/flatspin/flatspin",
        "Documentation": "https://flatspin.readthedocs.io/en/latest/",
        "Bug Tracker": "https://gitlab.com/flatspin/flatspin/issues",
    },
    license='GPLv3',
    author='Johannes H. Jensen',
    author_email='johannes.jensen@ntnu.no',
    description='Artificial Spin Ice simulator',
    long_description=long_description,
    long_description_content_type='text/x-rst',
    packages=find_namespace_packages(include=["flatspin", "flatspin.*"]),
    package_data={
        "": ["*.c"],
    },
    python_requires='>=3.5',
    install_requires=[
        'numpy',
        'scipy',
        'pandas>=0.23.0',
        'tables',
        'matplotlib',
        'pyopencl',
        'pillow',
        'joblib',
        'numba',
        'tqdm',
        'scikit-image',
    ],
    extras_require={
        'dev': [
            'pytest',
            'pytest-benchmark',
            'sphinx',
            'sphinx-autoapi',
            'sphinx_rtd_theme',
        ],
        'docs': [
            'sphinx',
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
    ],
    entry_points={
        'console_scripts': [
            'flatspin-run = flatspin.tools.run:main',
            'flatspin-run-sweep = flatspin.tools.run_sweep:main',
            'flatspin-plot-table = flatspin.tools.plot_table:main',
            'flatspin-plot = flatspin.tools.plot:main',
            'flatspin-vectors = flatspin.tools.vectors:main',
            'flatspin-vertices = flatspin.tools.vertices:main',
            'flatspin-stats = flatspin.tools.stats:main',
            'flatspin-convert = flatspin.tools.convert:main',
            'flatspin-fsck = flatspin.tools.fsck:main',
            'flatspin-inspect = flatspin.tools.inspect:main',
            'flatspin-progress = flatspin.tools.progress:main',
        ],
    }
)

# pylint: disable=import-outside-toplevel
from __future__ import print_function

import sys
from setuptools import find_packages, setup, Extension

import sciencebeam_alignment


with open('requirements.txt', 'r') as f:
    REQUIRED_PACKAGES = f.readlines()


with open('README.md', 'r') as f:
    long_description = f.read()


NUMPY_REQUIREMENT = [r.rstrip() for r in REQUIRED_PACKAGES if r.startswith('numpy')][0]


def is_numpy_installed():
    try:
        import numpy # noqa pylint: disable=unused-variable, unused-import
        return True
    except ImportError:
        return False


def install_numpy_if_not_available():
    if not is_numpy_installed():
        import subprocess
        print('installing numpy:', NUMPY_REQUIREMENT)
        subprocess.check_output([sys.executable, '-m', 'pip', 'install', NUMPY_REQUIREMENT])


def get_numpy_include_dir():
    install_numpy_if_not_available()

    import numpy as np
    return np.get_include()


packages = find_packages()


def setup_package():
    setup_requires = [
        # Setuptools 18.0 properly handles Cython extensions.
        'setuptools>=18.0',
        'cython'
    ]

    if not setup_requires:
        # only add numpy if not already installed (see scipy setup.py)
        setup_requires = setup_requires + [NUMPY_REQUIREMENT]

    setup(
        name='sciencebeam_alignment',
        version=sciencebeam_alignment.__version__,
        install_requires=REQUIRED_PACKAGES,
        packages=packages,
        include_package_data=True,
        description='ScienceBeam Alignment',
        url='https://github.com/elifesciences/sciencebeam-alignment',
        license='MIT',
        keywords="sequence alignment",
        setup_requires=setup_requires,
        ext_modules=[
            Extension(
                'sciencebeam_alignment.align_fast_utils',
                sources=['sciencebeam_alignment/align_fast_utils.pyx']
            ),
        ],
        include_dirs=[get_numpy_include_dir()],
        long_description=long_description,
        long_description_content_type='text/markdown'
    )


if __name__ == '__main__':
    setup_package()

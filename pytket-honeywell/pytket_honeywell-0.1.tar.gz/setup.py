import setuptools
from setuptools import setup

def find_pytket_subpackages():
    locations = [('pytket', 'pytket'), ('pytket/backends', 'pytket.backends')]
    pkg_list = []

    for location, prefix in locations:
        pkg_list += list(
            map(lambda package_name: '{}.{}'.format(prefix, package_name),
                setuptools.find_packages(where=location))
        )

    return pkg_list

setup(
    name='pytket_honeywell',
    author='Seyon Sivarajah',
    author_email='seyon.sivarajah@cambridgequantum.com',
    python_requires='>=3.6',
    url='https://github.com/CQCL/pytket_honeywell',
    description='Extension for pytket, providing access to Honeywell backends',
    long_description= open('README.md').read(),
    license='CQC Non-Commercial Use Software Licence',
    packages = find_pytket_subpackages(),
    install_requires = [
        'pytket >= 0.4.2',
        'requests >= 2.2',
        'websockets >= 7.0',
        'nest_asyncio >= 1.2'

    ],
    classifiers=[
        "Environment :: Console",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "License :: Other/Proprietary License",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: POSIX :: Linux",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering"
    ],
    zip_safe=False,
    use_scm_version=True,
    setup_requires=['setuptools_scm']
)

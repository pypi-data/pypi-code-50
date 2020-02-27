import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='nrfsec',
    version='0.1',
    scripts=['nrfsec'],
    author='BuildXYZ',
    author_email='buildxyz@gmail.com',
    description='A security research tool for working with Nordic nRF51 chips',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/buildxyz-git/nrfsec',

    packages=setuptools.find_packages(),

    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
        'Natural Language :: English',
        'Intended Audience :: Developers'
     ],

    install_requires=[
        'tabulate',
        'binascii',
        'tqdm',
        'time',
        'coloredlogs',
        'logging',
        'argparse',
        'os'
    ],

    dependency_links=['https://github.com/cortexm/pyswd']
 )
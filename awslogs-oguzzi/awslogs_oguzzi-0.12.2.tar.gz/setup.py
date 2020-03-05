import sys

from setuptools import setup, find_packages


install_requires = [
    'boto3>=1.5.0',
    'jmespath>=0.7.1,<1.0.0',
    'termcolor>=1.1.0',
    'python-dateutil>=2.4.0'
]


# as of Python >= 2.7 argparse module is maintained within Python.
extras_require = {
    ':python_version in "2.4, 2.5, 2.6"': ['argparse>=1.1.0'],
}


if 'bdist_wheel' not in sys.argv and sys.version_info < (2, 7):
    install_requires.append('argparse>1.1.0')


setup(
    name='awslogs_oguzzi',
    version='0.12.2',
    url='https://github.com/olivierguzzi/awslogs',
    license='BSD',
    author='Olivier Guzzi',
    author_email='oguzzi@shopstyle.com',
    description='awslogs is a simple command line tool to read aws cloudwatch logs.',
    long_description='awslogs is a simple command line tool to read aws cloudwatch logs.',
    keywords="aws logs cloudwatch",
    packages=find_packages(),
    platforms='any',
    install_requires=install_requires,
    extras_require=extras_require,
    test_suite='tests',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 2',
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Topic :: Utilities'
    ],
    entry_points={
        'console_scripts': [
            'awslogs = awslogs_oguzzi.bin:main',
        ]
    },
    zip_safe=False
)

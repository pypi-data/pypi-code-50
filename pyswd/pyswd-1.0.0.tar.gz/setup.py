"""A setup tools based setup module.
"""

# pylint: disable=W0122

import setuptools

_ABOUT = {}

with open('README.md', 'r') as fh:
    long_description = fh.read()

exec(open('swd/__about__.py').read(), _ABOUT)

setuptools.setup(
    name=_ABOUT['APP_NAME'],
    version=_ABOUT['VERSION'],
    description='Is a python module for debugging microcontrollers with SWD using ST-Link/V2 (/V2-1) or V3 debugger. This package also contain small command line tool.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url=_ABOUT['URL'],
    author=_ABOUT['AUTHOR'],
    author_email=_ABOUT['AUTHOR_EMAIL'],
    license='MIT',
    keywords='SWD debugger STM32 STLINK CORTEX-M ARM',
    classifiers=[
        # https://pypi.python.org/pypi?%3Aaction=list_classifiers
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Embedded Systems',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],

    packages=[
        'swd',
        'swd.stlink',
    ],

    install_requires=[
        'pyusb (>=1.0.2)'
    ],

    entry_points={
        'console_scripts': [
            '%s=swd._app:main' % _ABOUT['APP_NAME'],
        ],
    },
)

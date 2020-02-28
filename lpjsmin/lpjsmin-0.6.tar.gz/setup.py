from setuptools import setup, find_packages
import os

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.rst')).read()
NEWS = open(os.path.join(here, 'NEWS.rst')).read()


version = '0.6'
install_requires = [
    'argparse; python_version<"2.7" or'
    ' (python_version>="3.0" and python_version<"3.2")',
    'six',
    ]

tests_require = [
    'nose',
]

setup(name='lpjsmin',
    version=version,
    description="JS Min script that provides cmd line and python processors",
    long_description=README + '\n\n' + NEWS,
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    keywords='javascript minification compress',
    author='Rick Harding',
    author_email='rharding@canonical.com',
    url='https://launchpad.net/lpjsmin',
    license='BSD',
    packages=find_packages('src'),
    package_dir = {'': 'src'},include_package_data=True,
    zip_safe=False,
    install_requires=install_requires,
    tests_require=tests_require,
    extras_require={'test': tests_require},
    entry_points={
        'console_scripts':
            ['lpjsmin=lpjsmin:main']
    }
)

import os
from setuptools import setup

README = open(os.path.join(os.path.dirname(__file__), 'README.md')).read()


setup(
    name="jenkins-test-job",
    version='0.0.3',
    description='This is just for testing jenkins job',
    long_description=README,
    long_description_content_type="text/x-rst",
    author='edX',
    author_email='ihassan@edx.org',
    url='https://github.com/edx/test-jenkis-travis',
    packages=[
        'jenkins-test'
    ],
    include_package_data=True,
    install_requires=[
        "pyparsing==2.2.0",
        "numpy",
        "scipy",
        'six',
    ],
    python_requires=">=3.5",
    license="AGPL 3.0",
    test_suite='calc.tests',
    tests_require=[
        'coverage',
    ],
    zip_safe=False,
    keywords='edx',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
)

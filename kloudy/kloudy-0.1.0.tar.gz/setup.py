# read the contents of your README file

from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="kloudy",
    version='0.1.0',
    description='kloudy - a human friendly command line utility for your cloud (AWS,GCP & Azure)',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/sdevang/kloudy',
    author='Dev Shah',
    author_email='dev@awsninja.co.uk',
    # py_modules=['kloudy'],
    packages=['kloudy'],
    include_package_data=True,
    install_requires=[
        'Click',
        'boto3',
        'requests',
        'texttable',
        'colorama',
        'click-completion',
        'oauth2client',
        'google-api-python-client'
    ],
    classifiers=[
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Intended Audience :: Education',
        'Intended Audience :: Information Technology',
        'Topic :: System :: Systems Administration',
        'License :: OSI Approved :: MIT License',
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Development Status :: 3 - Alpha"
    ],
    keywords='awscli kloudy gcpcli gcloud aws azure',
    python_requires='>=3.6',
    entry_points='''
        [console_scripts]
        kloudy=kloudy:cli
    ''',
)

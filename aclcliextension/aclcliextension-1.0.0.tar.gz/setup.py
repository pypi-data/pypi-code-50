from codecs import open
from setuptools import setup, find_packages

VERSION = "0.0.1"

CLASSIFIERS = [
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'Intended Audience :: System Administrators',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'License :: OSI Approved :: MIT License',
]

DEPENDENCIES = []

setup(
        name ='aclcliextension',
        version ='1.0.0',
        author ='Vivek Subramaniam',
        author_email='vivsubra@linkedin.com',
        description ='Demo Package.',
        long_description_content_type ="text/markdown",
        license ='MIT',
        packages = find_packages(),
        entry_points ={
            'console_scripts': [
                'gfg = aclcliextension.cli:main'
            ]
        },
        classifiers =(
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
        ),
        keywords ='geeksforgeeks gfg article python package vibhu4agarwal',
        install_requires=DEPENDENCIES,
        zip_safe = False
)
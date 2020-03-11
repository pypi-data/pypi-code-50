from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='ieeemac',
    version='0.5',
    include_package_data=True,
    long_description=long_description,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],

    keywords='macaddress MAC network development',

    packages=find_packages(exclude=["tests", "*.tests", "*.tests.*", "tests.*"]),

    python_requires='>=2.7',

    entry_points={
        'console_scripts': [
            'mac_address=ieeemac:main',
        ],
    },
)

from setuptools import setup, find_packages

setup(
    name='x-atp-cli',
    version='0.1.1',
    keywords=['x', 'atp', 'test', 'platform'],
    description='X automated test platform command line client',
    long_description='X automated test platform command line client',
    classifiers=[
        'Programming Language :: Python :: 3',
        "License :: OSI Approved :: MIT License",
        'Operating System :: OS Independent',
    ],
    url='https://github.com/hekaiyou/x-atp-cli',
    author="HeKaiYou",
    author_email="hekaiyou@gmail.com",
    packages=find_packages(),
    include_package_data=True,
    platforms='any',
    install_requires=[],
    entry_points={
        'console_scripts': [
            'x-atp-cli = atp.cli:main'
        ]
    },
)

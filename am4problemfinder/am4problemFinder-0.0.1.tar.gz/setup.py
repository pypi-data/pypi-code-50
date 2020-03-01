from setuptools import setup

def readme():
    with open('README.md') as f:
        README = f.read()
    return README

setup(
    name="am4problemFinder",
    version="0.0.1",
    description="A tool to help you find issues of your flights in Airline Manager 4.",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/cathaypacific8747/am4problemfinder/",
    author="Cathay Express",
    author_email="cathayexpress4@gmail.com",
    license="GNU AGPL-3.0",
    classifiers=[
        'Development Status :: 4 - Beta',
        "Programming Language :: Python :: 3",
    ],
    packages=['src'],
    include_package_data=True,
    install_requires=[
    	'lxml',
    	'colorama',
    	'prettytable',
    	'urllib3',
    	'bs4'
    ],
    entry_points={
    	'console_scripts': [
    		'src = src.dRun:main',
    	],
    },
)
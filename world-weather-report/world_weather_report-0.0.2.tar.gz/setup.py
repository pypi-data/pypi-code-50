from setuptools import setup, find_packages

def readme():
    with open('README.md') as f:
        readme = f.read()
    return readme

setup(
    name='world_weather_report',
    version='0.0.2',
    long_description = readme(),
    packages = find_packages(),
    long_description_content_type="text/markdown",
    include_package_data = True,
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={
        "console_scripts": [
            'world_weather_report=world_weather_report.cli:main'
        ]
    }

)
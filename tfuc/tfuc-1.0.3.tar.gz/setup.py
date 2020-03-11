from setuptools import find_packages, setup

with open("README.md" , "r" ) as fh :
    long_description = fh.read()

setup(
    name='tfuc',
    version='1.0.3',
    packages=find_packages(),
    long_description=long_description ,
    description="some useful tools",
    long_description_content_type="text/markdown",
    url="https://github.com/gitduk/tfuc.git",
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'bs4', 'fake_useragent', 'openpyxl', 'sqlalchemy', 'selenium', 'requests', 'urllib3'
    ],
)

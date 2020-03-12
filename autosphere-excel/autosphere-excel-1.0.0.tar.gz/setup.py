from setuptools import setup, find_packages

with open("README.txt", "r") as fh:
	long_description = fh.read()

setup(

    name='autosphere-excel',
    version='1.0.0',
    description='Autosphere library for excel xlsx file format',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/mercurialmindsrpa/autosphere-excel.git',
    author='Abdul Mateen',
    author_email='abdul.mateen@mercurialminds.com',
    packages=find_packages(),
    install_requires=['openpyxl']
    
)

from setuptools import setup

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name='sclass',
    version='1.0.0',
    description='Basic class used as a SuperClass for other classes',
    author='Lorenzo Bartolini',
    author_email='l.bartolini02@gmail.com',
    py_modules=['sclass'],
    package_dir={'':'src'},
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "Operating System :: OS Independent"
    ],
    long_description=long_description,
    long_description_content_type="text/markdown",
    )

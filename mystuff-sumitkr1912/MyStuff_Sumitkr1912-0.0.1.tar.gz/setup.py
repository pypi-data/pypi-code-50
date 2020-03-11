# from distutils.core import setup
#
# setup(
#     name='TowelStuff_Sumitkr1912',
#     version='0.3',
#     packages=[],
#     license='Creative Commons Attribution-Noncommercial-Share Alike license',
#     long_description=open('README.txt').read(), requires=['requests']
# )
from distutils.core import setup

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="MyStuff_Sumitkr1912", # Replace with your own username
    version="0.0.1",
    author="Sumit Kumar",
    author_email="sumit.2.kumar@continental-corporation.com",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Sumit/mystuff",
    packages=setuptools.find_packages(),
    python_requires='>=3.7',
)
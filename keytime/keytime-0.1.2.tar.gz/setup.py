from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='keytime',
    version='0.1.2',
    description='get time, how long a key is pressed',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/lfreist/keytime",
    author='lfreist',
    author_email='',
    packages=['keytime'],
    install_requires=[
              'pynput',
              ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        ],
)

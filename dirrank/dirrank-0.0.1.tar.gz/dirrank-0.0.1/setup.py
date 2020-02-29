from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='dirrank',
    version='0.0.1',
    packages=['dirrank'],
    url='https://github.com/liampulles/dirrank',
    license='MIT',
    author='Liam Pulles',
    author_email='me@liampulles.com',
    description='Rank files in a directory recursively, based on user preference.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)

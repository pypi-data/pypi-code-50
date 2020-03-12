import setuptools
from os import path


this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


setuptools.setup(
    name="dictschema",
    version="0.0.1",
    author="Kyle Beauregard",
    author_email="kylembeauregard@gmail.com",
    description="Schema validation for python dictionaries",
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/kbeauregard/dictschema',
    license='MIT',
    packages=setuptools.find_packages(
        include=[
            'dictschema*',
        ],
        exclude=["dictschema/tests"]
    ),
    py_modules=[
        'dictschema.__init__',
    ],
    keywords = ['dict', 'schema', 'validation'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Operating System :: OS Independent",
    ],
)

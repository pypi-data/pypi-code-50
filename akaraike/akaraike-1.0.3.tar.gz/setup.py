from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup (
    name = 'akaraike',
    version = '1.0.3',
    description = 'Generate passwords, API keys of any length and character combination',
    py_modules=["generate_password", "set_charset_types", "set_charset_length"],
    packages=['akaraike'],
    
    classifiers = [
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',       
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],

    long_description=long_description,
    long_description_content_type="text/markdown",
    
)
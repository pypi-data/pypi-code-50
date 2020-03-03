from setuptools import setup, find_packages

with open('README.md') as readme_file:
    README = readme_file.read()

setup_args = dict(
    name='xnatbidsfns',
    version='0.1',
    description='Utility functions for BIDS data',
    long_description_content_type="text/markdown",
    long_description=README,
    license='MIT',
    packages=find_packages(),
    author='Radiologcs/NRG',
    author_email='kate@radiologics.com',
    download_url='https://pypi.org/project/xnatbidsutils/',
    url='https://github.com/radiologics/docker-images'
)

if __name__ == '__main__':
    setup(**setup_args)

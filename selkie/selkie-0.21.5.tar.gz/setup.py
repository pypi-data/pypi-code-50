
from setuptools import setup, find_packages

setup(
    name='selkie',
    version='0.21.5',
    author='Steven Abney',
    author_email='abney@umich.edu',
    description='Computational Linguistics',
    long_description='Computational Linguistics',
    long_description_content_type='text/plain',
    url='http://www.umich.edu/~abney/',
    packages=find_packages(),
    package_data={
        'seal': ['__data__/census/*',
                 '__data__/conll/2006/*',
                 '__data__/conll/2006/universal-pos-tags/*',
                 '__data__/eng/*',
                 '__data__/iso/*',
                 '__data__/iso/639-3/*',
                 '__data__/seal/*']
        },
    python_requires='>=3.6'
)

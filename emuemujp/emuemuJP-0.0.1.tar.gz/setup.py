from setuptools import setup, find_packages

setup(
    name='emuemuJP',
    version='0.0.1',
    packages=find_packages(),

    author='emuemuJP',
    author_email='k.matsumoto.0807@gmail.com',

    description='This is a package for me.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',

    python_requires='~=3.6',

    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Operating System :: OS Independent',
    ],


)
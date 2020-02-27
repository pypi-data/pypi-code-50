import setuptools

from prgb_pkg.prgb import Prgb

with open('README.md', 'r') as f:
    long_description = f.read()

setuptools.setup(
    name='prgb-pkg',
    version=Prgb.version,
    author='Piotr Bernaskiewicz',
    author_email='mojczat0@gmail.com',
    maintainer='KodenejmBerni',
    description='Simple GUI class, which provides nice looking \'for\' loop progress tracking.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=setuptools.find_packages(),
    project_urls={
        "Source Code": "https://github.com/KodenejmBerni/prgb_pkg",
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: Microsoft :: Windows',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Intended Audience :: Developers',
        'Development Status :: 3 - Alpha',
        'Topic :: Software Development',
    ],
    python_requires='>=3.7',
)

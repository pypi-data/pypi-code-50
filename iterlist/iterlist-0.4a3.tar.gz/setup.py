import codecs
from glob import glob
from os.path import abspath, basename, dirname, join, splitext

import setuptools


def read(*parts):
    """Read a file in this repository."""
    here = abspath(dirname(__file__))
    with codecs.open(join(here, *parts), 'r') as file_:
        return file_.read()


setuptools.setup(
    name='iterlist',
    use_scm_version=True,
    description='Treat an iterator as a list',
    long_description=read('README.md'),
    long_description_content_type='text/markdown',
    author='Ryan Haining',
    author_email='haining.cpp@gmail.com',
    maintainer='Masen Furer',
    maintainer_email='m_github@0x26.net',
    url='https://github.west.isilon.com/masenf/iterlist',
    package_dir={"": 'src'},
    packages=setuptools.find_packages('src'),
    py_modules=[splitext(basename(path))[0] for path in glob('src/*.py')],
    python_requires='>=2.7,!=3.0.*,!=3.1.*,!=3.2.*,!=3.3.*,!=3.4.*,<4',
    setup_requires=[
        'setuptools_scm >= 3.3',
    ],
    classifiers=[
        'Intended Audience :: Developers',
        'Development Status :: 3 - Alpha',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: BSD License',
    ],
)

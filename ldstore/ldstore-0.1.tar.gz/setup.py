import setuptools

with open( 'README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name                           = 'ldstore',
    version                        = '0.1',
    author                         = 'Christian Benner',
    author_email                   = 'christian.benner@helsinki.fi',
    description                    = 'A package for reading files created by LDstore',
    url                            = 'http://www.finemap.me',
    data_files                     = [("", ["LICENSE"])],
    packages                       = setuptools.find_packages(),
    install_requires               = [ 'numpy', 'pandas', 'zstd' ],
    classifiers                    = [
        'Programming Language :: Python :: 2.7',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires                = '>=2.7',
)

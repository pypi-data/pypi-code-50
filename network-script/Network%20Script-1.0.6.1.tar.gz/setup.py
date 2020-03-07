import setuptools

setuptools.setup(
    name = 'Network Script',
    version = '1.0.6.1',
    url = 'https://github.com/gaming32/Network-Script',
    author = 'Gaming32',
    author_email = 'gaming32i64@gmail.com',
    license = 'License :: OSI Approved :: MIT License',
    description = 'Library for calling methods over sockets',
    long_description = open('README.md').read(),
    long_description_content_type = 'text/markdown',
    packages = [
        'netsc',
    ],
)
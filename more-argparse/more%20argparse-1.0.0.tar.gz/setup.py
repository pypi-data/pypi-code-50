import setuptools

with open('README.md') as fp:
    long_description = fp.read()

setuptools.setup(
    name = 'more argparse',
    version = '1.0.0',
    url = 'https://github.com/gaming32/more-argparse',
    author = 'Gaming32',
    author_email = 'gaming32i64@gmail.com',
    license = 'License :: OSI Approved :: MIT License',
    description = 'Extra types and actions for argparse',
    long_description = long_description,
    long_description_content_type = 'text/markdown',
    setup_requires = [
        'argparse',
    ],
    packages = [
        'margparse',
    ],
)
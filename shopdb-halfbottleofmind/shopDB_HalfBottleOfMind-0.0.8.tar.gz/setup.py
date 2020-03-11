import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name = 'shopDB_HalfBottleOfMind',
    version = '0.0.8',
    author = 'HalfBottleOfMind',
    author_email = 'andromalak222@gmail.com',
    description = 'Shop database',
    long_description = long_description,
    long_description_content_type = 'text/markdown',
    url = 'https://github.com/halfbottleofmind/shopdb',
    packages = setuptools.find_packages(),
    classifiers = [
        'Programming Language :: Python :: 3.8',
        'License :: OSI Approved :: MIT License',
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)
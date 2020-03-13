from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='mloyalty',
    version='0.2.3',
    packages=find_packages(),
    url='https://github.com/igorexa256/mloyalty',
    license='MIT',
    author='Igor Belyansky',
    author_email='igorexa256@gmail.com',
    description='Python API for Mloyalty',
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords='python mloyalty api wrapper',
    install_requires=['requests', 'pyjwt', 'tinydb', 'python-dotenv'],
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
    ],
)

from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='mloyalty',
    version='0.1.0',
    packages=['mloyalty'],
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

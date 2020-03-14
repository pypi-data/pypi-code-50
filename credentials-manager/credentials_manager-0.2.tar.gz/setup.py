from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()


setup(
    name='credentials_manager',
    version='0.2',
    description='Simple credential management',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/dreynolds/CredentialsManager',
    author='David Reynolds',
    author_email='david@reynoldsfamily.org.uk',
    license='GPL',
    packages=['credentials_manager'],
    zip_safe=False,
    install_requires=['keyring==21.1.1'],
    python_requires='>=3.6',
    classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="oxauth",
    version="0.0.2",
    author="JP Slavinsky",
    author_email="jps@rice.edu",
    description="OpenStax authentication strategies",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/openstax/auth-python",
    packages=setuptools.find_packages(),
    install_requires=[
        'PyJWT',
        'PyJWE'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)

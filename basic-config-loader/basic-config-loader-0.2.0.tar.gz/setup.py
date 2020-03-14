import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
    name='basic-config-loader',
    version='0.2.0',
    author="Bruce Blore",
    author_email="bruceblore@protonmail.com",
    description="A basic configuration loader intended for my own scripts, but might be useful for other people.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://gitlab.com/0100001001000010/config-loader",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
    ],
)

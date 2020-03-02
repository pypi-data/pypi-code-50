import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="key-logger",
    version="0.0.1",
    author="DannyK999",
    author_email="dannyk999@live.com",
    description="pip install key-logger",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://gitlab.com/DannyK999/keylogger",
    packages=setuptools.find_packages(),
    classifiers=[
        "Development Status :: 1 - Planning",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)

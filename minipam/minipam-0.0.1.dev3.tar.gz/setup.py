import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

version = {'__builtins__': None}

with open("minipam/version.py", "r") as fh:
    exec(fh.read(), version)

del version["__builtins__"]

setuptools.setup(
    name="minipam",
    version=version["VERSION"],
    author="Eric Geldmacher",
    author_email="egeldmacher@wustl.edu",
    description="Minimal IPAM using YAML file for data storage",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://gitlab.com/egeldmacher/minipam",
    license = "GPLv3",
    packages=setuptools.find_packages(),
    install_requires=["pyyaml"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
    entry_points={
        "console_scripts": [
            "minipam=minipam.__main__:main",
        ],
    },
)

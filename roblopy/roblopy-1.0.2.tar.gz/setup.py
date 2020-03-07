from distutils.core import setup

long_description = open("README.md", "r").read()

setup(
    name="roblopy",
    packages=["roblopy", "roblopy.api"],
    version="1.0.2",
    license="MIT",
    description="Roblox API built in Python",
    long_description=long_description,
    author="Jack Murrow",
    author_email="jack.murrow122005@gmail.com",
    url="https://github.com/jackprogramsjp/Roblopy",
    keywords=["Roblox", "Roblox Python", "Roblox Api"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License"
    ]
)
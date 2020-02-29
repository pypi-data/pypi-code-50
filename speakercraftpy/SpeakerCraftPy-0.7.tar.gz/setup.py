import setuptools

setuptools.setup(
    name="SpeakerCraftPy",
    packages = ['SpeakerCraft'],
    version="0.7",
    license="MIT",
    author="Fraser Price",
    author_email="fraserbcprice@gmail.com",
    description="A python library for controlling Speaker Craft MZC series amplifiers over serial.",
    url="https://github.com/Fraserbc/SpeakerCraftPy",
    install_requires=[
        'pyserial'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.0'
)